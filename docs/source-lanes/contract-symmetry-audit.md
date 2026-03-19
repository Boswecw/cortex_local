# Cortex Source-Lane Contract Symmetry Audit

## Purpose

This note records the post-Slice-7 contract audit across current schemas, lane contracts, ADRs, runtime truth, service-status truth, and retrieval-package truth.

It is an audit note, not a roadmap.

## Audit scope

Reviewed together:

- `schemas/extraction-result.schema.json`
- `schemas/retrieval-package.schema.json`
- `schemas/service-status.schema.json`
- `docs/contracts/source-lane-text.md`
- `docs/contracts/source-lane-pdf.md`
- `docs/contracts/source-lane-docx.md`
- `docs/contracts/source-lane-rtf.md`
- `docs/source-lanes/*.md`
- `DECISIONS/0007-source-lane-framework.md`
- `DECISIONS/0008-docx-lane-admission.md`
- `DECISIONS/0009-rtf-lane-admission.md`
- current runtime slice implementations and operator entrypoints

## Alignment findings

- The extraction contract remains syntax-only across all admitted lanes.
- Retrieval remains lane-neutral and infrastructure-only: `ready` plus complete syntax structure is required, and non-ready upstream artifacts are denied.
- Service status remains registry-driven rather than parser-branch-driven.
- PDF, DOCX, and RTF lane contracts are explicit about admitted surface, deny conditions, unavailable conditions, and exclusions.

## Hardening findings addressed in this phase

- Text lanes were previously implicit in runtime truth but lacked a lane contract document. `source-lane-text.md` closes that symmetry gap.
- Empty `.md` and `.txt` inputs previously reached `ready` with no content blocks. Runtime now denies no-text text inputs to match the other lanes' honesty posture.
- Direct-source extraction and retrieval CLIs now accept optional declared media types so suffix and media-type mismatch behavior is visible through operator entrypoints as well as through in-process calls.

## No-schema-change judgment

This phase does not require schema expansion.

Current truthful runtime behavior is representable with the existing extraction, retrieval, and service-status schemas.
Hardening in this phase therefore stays in:

- lane docs
- runtime fail-closed behavior
- fixtures
- runtime tests
- operator-surface consistency

## Remaining truth posture

- PDF is the only admitted lane that may honestly emit `partial_success`.
- DOCX and RTF preserve narrower deterministic recovery and deny rich-review or rich-destination structures.
- Retrieval-package emission remains non-semantic and non-ranking for every admitted lane.
- Service status remains informational only and does not become a control surface for lane selection or downstream action.
