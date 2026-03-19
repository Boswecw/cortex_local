# Cortex Source Lanes

This directory defines the shared admission framework for governed Cortex source lanes.

Cortex does not support "documents" as one broad ingestion category.
Cortex admits only explicit local source lanes with:

- bounded eligibility
- bounded failure posture
- bounded provenance
- deterministic syntax-only recovery
- independent tests

Current admitted lanes:

- local Markdown files
- local plain-text files
- local text-layer PDF files
- local DOCX files
- local RTF files
- local ODT files
- local EPUB files

Lane-specific rules remain in `docs/contracts/source-lane-*.md`.
Shared lane rules live in this directory so future lane admission does not become a series of one-off branches.

Governance references in this directory:

- `lane-admission-criteria.md`
- `shared-failure-taxonomy.md`
- `shared-provenance-model.md`
- `lane-admission-playbook.md`
- `contract-symmetry-audit.md`
- `scrivener/` (phase-0 evidence packet)
- `scrivener/authority-recon-status-semantics.md` (Stage 1 status boundary note, still non-authorizing)
- `scrivener/authority-recon-correspondence-semantics.md` (Stage 1 degraded-correspondence boundary note, still non-authorizing)
- `scrivener/three-project-comparative-evidence-review.md` (three-clean-project comparative review, still non-authorizing)
- `scrivener/authority-recon-slice-plan.md` (Stage 1-only build packet, authorized only through Decision 0015)
- `scrivener/stage1-post-implementation-review.md` (post-implementation governance review; may open Stage 2 planning only)
- `scrivener/stage2-planning-packet.md` (canonical bounded Stage 2 planning packet; still non-authorizing)
- `scrivener/stage2-fixture-acquisition-plan.md` (bounded Stage 2 fixture and evidence acquisition program; still non-authorizing)
- `scrivener/stage2-manuscript-eligibility-scope.md` (candidate-only manuscript-eligibility planning seam; still non-authorizing)
- `scrivener/stage2-manuscript-vs-non-manuscript-boundary.md` (structural manuscript boundary note; still non-authorizing)
- `scrivener/stage2-degraded-partial-truth-model.md` (degraded/partial truth-model note; still non-authorizing)
- `scrivener/stage2-item-type-inclusion-exclusion.md` (item-type inclusion/exclusion note; still non-authorizing)
- `scrivener/stage2-evidence-and-gate.md` (Stage 2 evidence-and-gate companion note; still non-authorizing)
- `scrivener/stage2-contract-packet.md` (Stage 2 contract companion note; still non-authorizing)
- `../../DECISIONS/0015-scrivener-stage1-authority-recon-authorization.md` (Stage 1-only Scrivener authorization decision; lane still unadmitted)
- `../../DECISIONS/0016-scrivener-stage2-implementation-remains-blocked.md` (explicit Stage 2 authorization review decision; implementation still blocked)
- `../fixtures/scrivener/` (canonical fixture intake packet)
- `next-lane-candidate-matrix.md` (historical, pre-ODT)
- `next-lane-candidate-matrix-v2.md` (historical, pre-Slice-9)
- `next-lane-candidate-matrix-v3.md`
- `odt-admission-draft.md` (historical)
- `../contracts/source-lane-epub.md`
- `../contracts/source-lane-epub-draft.md` (historical)
- `../contracts/source-lane-scrivener-draft.md`
- `../contracts/scrivener-authority-recon-status-draft.md`
