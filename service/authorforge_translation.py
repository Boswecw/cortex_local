"""Translation between ``cortex_runtime`` contracts and the AuthorForge seam.

Pure functions only — no IO, no global state. Each takes a native
``cortex_runtime`` result dict and produces the exact shape AuthorForge's
``apps/api/src/services/cortex.ts`` client expects.

Native Cortex contracts:
  - extraction-result.schema.json
  - retrieval-package.schema.json

AuthorForge contracts (apps/api/src/adapters/file-intel.ts):
  - ExtractionPacket
  - RetrievalPrepPacket-shaped retrieval-package passthrough
"""

from __future__ import annotations

from typing import Any

# MIME types AuthorForge admits, mapped to the suffix cortex_runtime lanes key on.
MIME_TO_SUFFIX: dict[str, str] = {
    "text/plain": ".txt",
    "text/markdown": ".md",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    "application/pdf": ".pdf",
    "text/rtf": ".rtf",
    "application/epub+zip": ".epub",
}

# cortex content-block kind -> AuthorForge segment kind (its enum is narrower).
_BLOCK_KIND_TO_SEGMENT_KIND = {
    "heading": "heading",
    "paragraph": "paragraph",
    "list": "paragraph",
    "table": "paragraph",
    "quote": "paragraph",
    "code": "paragraph",
}

_READY_STATES = {"ready", "partial_success", "stale"}


def degraded_reason_from_result(result: dict[str, Any]) -> str | None:
    """Pull the most specific operator-visible summary from a result dict."""
    refusal = result.get("refusal")
    if isinstance(refusal, dict) and refusal.get("operator_visible_summary"):
        return str(refusal["operator_visible_summary"])
    completeness = result.get("completeness")
    if isinstance(completeness, dict) and completeness.get("operator_visible_summary"):
        return str(completeness["operator_visible_summary"])
    freshness = result.get("freshness")
    if isinstance(freshness, dict) and freshness.get("operator_visible_summary"):
        return str(freshness["operator_visible_summary"])
    return None


def _segments_from_blocks(content_blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    segments: list[dict[str, Any]] = []
    for index, block in enumerate(content_blocks):
        text = block.get("text")
        if not isinstance(text, str) or not text:
            continue
        block_kind = block.get("block_kind", "paragraph")
        kind = _BLOCK_KIND_TO_SEGMENT_KIND.get(block_kind, "paragraph")
        segments.append(
            {
                "kind": kind,
                "title": text if kind == "heading" else None,
                "text": text,
                "order_index": index,
            }
        )
    return segments


def _retrieval_chunks_from_package(package: dict[str, Any]) -> list[dict[str, Any]]:
    """Map a retrieval-package's chunks into ExtractionPacket.retrieval_chunks."""
    if package.get("state") not in _READY_STATES:
        return []
    chunks = package.get("chunks")
    if not isinstance(chunks, list):
        return []
    out: list[dict[str, Any]] = []
    for chunk in chunks:
        text = chunk.get("text")
        if not isinstance(text, str) or not text:
            continue
        out.append(
            {
                "text": text,
                "metadata": {
                    "chunk_id": chunk.get("chunk_id"),
                    "ordinal": chunk.get("ordinal"),
                    "structure_kind": chunk.get("structure_kind"),
                    "source_ref": chunk.get("source_ref"),
                },
            }
        )
    return out


def extraction_result_to_packet(
    result: dict[str, Any],
    *,
    file_type: str,
    retrieval_package: dict[str, Any] | None,
) -> dict[str, Any]:
    """Translate a cortex extraction-result into an AuthorForge ExtractionPacket."""
    state = result.get("state")
    extraction_id = str(result.get("artifact_id") or "")

    structures = result.get("structures")
    content_blocks: list[dict[str, Any]] = []
    if isinstance(structures, dict):
        raw_blocks = structures.get("content_blocks")
        if isinstance(raw_blocks, list):
            content_blocks = raw_blocks

    is_ready = state in _READY_STATES
    segments = _segments_from_blocks(content_blocks) if is_ready else []
    text = "\n\n".join(seg["text"] for seg in segments) if segments else None
    retrieval_chunks = (
        _retrieval_chunks_from_package(retrieval_package)
        if (is_ready and retrieval_package is not None)
        else []
    )

    packet: dict[str, Any] = {
        "extraction_id": extraction_id,
        "file_type": file_type,
        "text": text,
        "segments": segments,
        "degraded": state != "ready",
        "retrieval_chunks": retrieval_chunks,
    }
    reason = degraded_reason_from_result(result)
    if state != "ready" and reason:
        packet["degraded_reason"] = reason
    return packet


def probe_to_response(probe: Any) -> dict[str, Any]:
    """Map a cortex_runtime PdfLaneProbeResult dataclass into the probe response."""
    return {
        "admitted": bool(getattr(probe, "admitted", False)),
        "operator_summary": str(getattr(probe, "operator_summary", "")),
        "pdfinfo_present": bool(getattr(probe, "pdfinfo_present", False)),
        "pdftotext_present": bool(getattr(probe, "pdftotext_present", False)),
    }


def semantic_refusal() -> dict[str, Any]:
    """The honest, doctrine-mandated refusal for the semantic lore step.

    AuthorForge's client reads ``candidates`` (empty -> falls back to the
    NeuronForge/backend NER lane). The refusal block makes the boundary explicit.
    """
    return {
        "candidates": [],
        "boundary": "syntax_only",
        "refusal": {
            "reason_class": "semantic_request_not_allowed",
            "operator_visible_summary": (
                "Cortex performs syntax-only extraction. Entity identification is a "
                "semantic task owned by NeuronForge; AuthorForge routes it there."
            ),
        },
    }
