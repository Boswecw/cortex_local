# Cortex AuthorForge Service

A bounded HTTP front door over `cortex_runtime` exposing exactly the
file-intelligence seam AuthorForge consumes. It adds **no semantics**, no
workflow control, and no durable truth (ADR 0004 — syntax before semantics).

## Run

```bash
# from the cortex/ repo root
pip install -r requirements.txt
python -m service                       # binds 127.0.0.1:8004
CORTEX_SERVICE_PORT=8010 python -m service
```

Loopback-only by default — Cortex receives manuscript/file text and must not be
exposed off-host.

Point AuthorForge at it with `CORTEX_URL=http://localhost:8004`.

## Surface

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/health` | `cortex_runtime` service status (readiness, admitted lanes) |
| GET | `/api/v1/authorforge/pdf-lane-probe` | Host admission probe (`pdfinfo`/`pdftotext` presence) |
| POST | `/api/v1/authorforge/admit-and-extract` | Admit a base64 file, return an `ExtractionPacket` |
| POST | `/api/v1/authorforge/prepare-for-retrieval` | Retrieval-package chunks for a prior `extraction_id` |
| POST | `/api/v1/authorforge/lore-entity-extraction` | **Refuses** — semantic step belongs to NeuronForge |

### admit-and-extract

Request: `{ file_content_b64, file_type, project_id }`. `file_type` is one of the
admitted MIME types (`text/plain`, `text/markdown`, `.docx`, `application/pdf`,
`text/rtf`, `application/epub+zip`). Returns the AuthorForge `ExtractionPacket`
(`extraction_id`, `text`, `segments[]`, `degraded`, `retrieval_chunks[]`).

### prepare-for-retrieval

Request: `{ extraction_id, project_id }`. References a prior extraction held in a
**bounded, TTL'd** in-memory cache (`CORTEX_EXTRACTION_TTL_SECONDS`, default
3600; `CORTEX_EXTRACTION_CACHE_MAX`, default 256). Unknown/expired ids return a
`denied` retrieval-package — no silent empty success.

### lore-entity-extraction

Returns `{ candidates: [] }` with a `semantic_request_not_allowed` refusal.
Entity identification is semantic and owned by NeuronForge; AuthorForge falls
back to its NeuronForge/NER lane automatically when candidates are empty.

## Boundaries

This service is a thin adapter. All extraction logic lives in `cortex_runtime`;
translation to the AuthorForge contract lives in `service/authorforge_translation.py`
(pure functions). The only state is the bounded retrieval-artifact cache.
