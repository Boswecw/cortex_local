"""Cortex AuthorForge HTTP service.

Bounded FastAPI front door over ``cortex_runtime`` exposing the file-intelligence
seam AuthorForge consumes:

  GET  /health
  GET  /api/v1/authorforge/pdf-lane-probe
  POST /api/v1/authorforge/admit-and-extract
  POST /api/v1/authorforge/prepare-for-retrieval
  POST /api/v1/authorforge/lore-entity-extraction   (syntax-only refusal)

Doctrine (ADR 0004 / BOUNDARIES.md): Cortex is syntax-only. This service adds no
semantics and no durable truth. It holds a single bounded, TTL'd cache of
extraction results so ``prepare-for-retrieval`` can reference a prior extraction
by id — an explicitly-allowed bounded retrieval artifact, nothing more.
"""

from __future__ import annotations

import base64
import binascii
import os
import tempfile
import threading
import time
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from cortex_runtime.extraction_emission import (
    emit_extraction_result_from_source_file,
)
from cortex_runtime.retrieval_package_emission import (
    emit_retrieval_package_from_extraction_result,
)
from cortex_runtime.service_status import emit_service_status
from cortex_runtime.source_lanes import probe_pdf_lane_admission

from .authorforge_translation import (
    MIME_TO_SUFFIX,
    extraction_result_to_packet,
    probe_to_response,
    semantic_refusal,
)

# ── Bounded extraction artifact cache ────────────────────────────────────────
# extraction_id -> (stored_at_epoch, extraction_result_dict)
_CACHE_TTL_SECONDS = int(os.environ.get("CORTEX_EXTRACTION_TTL_SECONDS", "3600"))
_CACHE_MAX_ENTRIES = int(os.environ.get("CORTEX_EXTRACTION_CACHE_MAX", "256"))
_cache: dict[str, tuple[float, dict[str, Any]]] = {}
_cache_lock = threading.Lock()


def _cache_put(extraction_id: str, result: dict[str, Any]) -> None:
    if not extraction_id:
        return
    now = time.time()
    with _cache_lock:
        # Evict expired, then oldest if over capacity. Bounded by construction.
        expired = [k for k, (ts, _) in _cache.items() if now - ts > _CACHE_TTL_SECONDS]
        for k in expired:
            _cache.pop(k, None)
        while len(_cache) >= _CACHE_MAX_ENTRIES:
            oldest = min(_cache, key=lambda k: _cache[k][0])
            _cache.pop(oldest, None)
        _cache[extraction_id] = (now, result)


def _cache_get(extraction_id: str) -> dict[str, Any] | None:
    now = time.time()
    with _cache_lock:
        entry = _cache.get(extraction_id)
        if entry is None:
            return None
        stored_at, result = entry
        if now - stored_at > _CACHE_TTL_SECONDS:
            _cache.pop(extraction_id, None)
            return None
        return result


# ── Request models ───────────────────────────────────────────────────────────


class AdmitAndExtractRequest(BaseModel):
    file_content_b64: str
    file_type: str
    project_id: str


class ExtractionRefRequest(BaseModel):
    extraction_id: str
    project_id: str


app = FastAPI(
    title="Cortex AuthorForge Service",
    description="Syntax-only file-intelligence seam for AuthorForge.",
    version="1.0.0",
)


@app.get("/health")
def health() -> JSONResponse:
    try:
        status = emit_service_status()
    except Exception as exc:  # never let status reporting take the service down
        status = {"service_id": "cortex", "service_class": "file_intelligence", "error": str(exc)}
    return JSONResponse(status)


@app.get("/api/v1/authorforge/pdf-lane-probe")
def pdf_lane_probe() -> JSONResponse:
    return JSONResponse(probe_to_response(probe_pdf_lane_admission()))


@app.post("/api/v1/authorforge/admit-and-extract")
def admit_and_extract(req: AdmitAndExtractRequest) -> JSONResponse:
    suffix = MIME_TO_SUFFIX.get(req.file_type)
    if suffix is None:
        return JSONResponse(
            {
                "extraction_id": "",
                "file_type": req.file_type,
                "text": None,
                "segments": [],
                "degraded": True,
                "degraded_reason": f"Unsupported file_type for Cortex admission: {req.file_type}",
                "retrieval_chunks": [],
            }
        )

    try:
        raw = base64.b64decode(req.file_content_b64, validate=True)
    except (binascii.Error, ValueError):
        return JSONResponse(
            {
                "extraction_id": "",
                "file_type": req.file_type,
                "text": None,
                "segments": [],
                "degraded": True,
                "degraded_reason": "file_content_b64 is not valid base64.",
                "retrieval_chunks": [],
            }
        )

    tmp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(raw)
            tmp_path = Path(tmp.name)
        result = emit_extraction_result_from_source_file(
            tmp_path,
            request_id=f"authorforge:{req.project_id}",
            source_ref=f"import{suffix}",
            media_type=req.file_type,
        )
    finally:
        if tmp_path is not None:
            tmp_path.unlink(missing_ok=True)

    retrieval_package: dict[str, Any] | None = None
    if result.get("state") in {"ready", "partial_success", "stale"}:
        try:
            retrieval_package = emit_retrieval_package_from_extraction_result(result)
        except Exception:
            retrieval_package = None

    _cache_put(str(result.get("artifact_id") or ""), result)
    packet = extraction_result_to_packet(
        result, file_type=req.file_type, retrieval_package=retrieval_package
    )
    return JSONResponse(packet)


@app.post("/api/v1/authorforge/prepare-for-retrieval")
def prepare_for_retrieval(req: ExtractionRefRequest) -> JSONResponse:
    result = _cache_get(req.extraction_id)
    if result is None:
        return JSONResponse(
            {
                "state": "denied",
                "refusal": {
                    "reason_class": "stale_input",
                    "operator_visible_summary": (
                        "No extraction is available for this extraction_id "
                        "(it expired or was never produced by this Cortex instance)."
                    ),
                },
            }
        )
    package = emit_retrieval_package_from_extraction_result(result)
    return JSONResponse(package)


@app.post("/api/v1/authorforge/lore-entity-extraction")
def lore_entity_extraction(req: ExtractionRefRequest) -> JSONResponse:
    # Syntax/semantics separation is constitutional (ADR 0004). Cortex refuses
    # the semantic step; AuthorForge falls back to its NeuronForge/NER lane.
    return JSONResponse(semantic_refusal())
