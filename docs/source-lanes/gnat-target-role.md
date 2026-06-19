# Cortex GNAT Support Target Role

## Status

Contract schemas and GNAT status summary promoted; GNAT execution runtime not
promoted.

## Source Authority

The local-system proving repo at
`/home/charlie/Forge/ecosystem/local-systems/cortex` owns GNAT authority,
contracts, and proof. The support repo must not treat this document as runtime
admission by itself.

Current source authority evidence:

- `docs/architecture/gnats-boundary-matrix.md`
- `docs/contracts/gnat-run-request.md`
- `docs/contracts/gnat-run-summary.md`
- `schemas/gnat-*.schema.json`
- `cortex_runtime/gnats/`
- `cortex_runtime/gnats/status.py`
- `cortex_runtime/service_status.py`
- `make test-gnats`

## Target Role

Cortex app support may receive GNAT promotion only as bounded
AuthorForge-facing truth over already proved local-system GNAT contracts.

The support target role is limited to:

- preserving Cortex ownership of source eligibility and source-lane admission
- exposing service-status truth that GNAT parallel execution is not ready until
  FA Local reports readiness
- exposing bounded run request and run summary truth to AuthorForge support
- keeping missing, stale, failed, cancelled, and partial results visible
- preserving syntax-only extraction boundaries
- refusing semantic interpretation, workflow ownership, and execution routing

## Explicit Non-Goals

This contract-schema and status-summary promotion does not authorize:

- copying GNAT execution runtime code into support in this slice
- adding service endpoints
- changing AuthorForge behavior
- adding scheduler, watcher, queue, or retry ownership
- routing execution through Cortex when FA Local owns integrated execution
- persisting durable records when DF Local owns storage/cache mechanics
- emitting semantic labels or candidate meaning

## Promoted Contract Files

This support role now includes the GNAT contract schemas and their valid/invalid
contract fixtures:

- `schemas/gnat-*.schema.json`
- `tests/contracts/fixtures/valid/gnat-*.json`
- `tests/contracts/fixtures/invalid/gnat-*.json`

## Promoted Status Files

This slice promotes only the support-safe GNAT service-status summary:

- `cortex_runtime/gnats/__init__.py`
- `cortex_runtime/gnats/models.py`
- `cortex_runtime/gnats/status.py`
- `cortex_runtime/source_lanes.py`
- `cortex_runtime/service_status.py`
- `schemas/service-status.schema.json`
- `tests/runtime/test_gnat_status.py`

The support `gnats` package intentionally exports only `FaLocalCapabilityState`
and `gnat_status_summary`; planners, workers, dispatch, persistence, retrieval
preparation, semantic handoff, and execution runners remain source-local.

## Runtime Promotion Gate

Before any GNAT execution runtime file is promoted into app support, the
promotion slice must name:

- exact files to promote
- source proof command
- support proof command
- support service contract or adapter target
- post-promotion drift report
- rollback path

Until that gate exists, GNAT execution runtime remains `source_local_hold` in
the promotion ledger.
