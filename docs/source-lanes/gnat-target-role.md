# Cortex GNAT Support Target Role

## Status

Target role opened; runtime not promoted.

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
- `make test-gnats`

## Target Role

Cortex app support may receive a future GNAT promotion only as a bounded
AuthorForge-facing syntax extraction and run-summary surface over already proved
local-system GNAT contracts.

The support target role is limited to:

- preserving Cortex ownership of source eligibility and source-lane admission
- exposing bounded run request and run summary truth to AuthorForge support
- keeping missing, stale, failed, cancelled, and partial results visible
- preserving syntax-only extraction boundaries
- refusing semantic interpretation, workflow ownership, and execution routing

## Explicit Non-Goals

This target role does not authorize:

- copying GNAT runtime code into support in this slice
- adding service endpoints
- changing AuthorForge behavior
- adding scheduler, watcher, queue, or retry ownership
- routing execution through Cortex when FA Local owns integrated execution
- persisting durable records when DF Local owns storage/cache mechanics
- emitting semantic labels or candidate meaning

## Promotion Gate

Before any GNAT file is promoted into app support, the promotion slice must name:

- exact files to promote
- source proof command
- support proof command
- support service contract or adapter target
- post-promotion drift report
- rollback path

Until that gate exists, GNAT remains `source_local_hold` in the promotion ledger.
