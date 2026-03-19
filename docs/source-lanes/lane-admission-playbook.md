# Cortex Source-Lane Admission Playbook

## Purpose

This playbook defines the required evaluation path for any future Cortex source-lane candidate before implementation begins.

It exists to slow format momentum down to constitutional truth.

## Required questions

Every candidate lane must answer all of the following before admission work starts:

1. What is the structural authority model?
2. What is the admitted input boundary?
3. What is the admitted extraction surface?
4. What is explicitly excluded?
5. What are the deny conditions?
6. What makes the lane unavailable?
7. Is `partial_success` ever honest for this lane?
8. What provenance must be reported?
9. What fixture families are required before admission?
10. What anti-drift risks does this lane create?

## Decision gates

### Gate 1 - authority clarity

Do not proceed if the lane cannot state:

- what it can recover literally
- what it cannot recover honestly
- where semantics would begin

### Gate 2 - admitted surface honesty

Do not proceed if the lane would require:

- OCR
- image interpretation
- semantic labeling
- summarization
- layout-faithful rendering claims
- best-effort structure invention

### Gate 3 - failure taxonomy clarity

Do not proceed unless the lane can state:

- exact deny conditions
- exact unavailable conditions
- whether `partial_success` is allowed
- why any incomplete success is still honest

### Gate 4 - provenance and privacy

Do not proceed unless the lane can preserve:

- source hash
- extractor version
- source modified time when available
- byte count when available

Do not proceed if the lane would pressure Cortex toward raw-content diagnostics or privacy-breaching previews.

### Gate 5 - testability

Do not proceed unless the lane has a bounded fixture plan covering:

- ready
- denied
- unavailable
- any claimed `partial_success`
- suffix or media-type mismatch
- retrieval compatibility
- ugly but realistic malformed inputs

## Required admission artifacts

Before implementation, prepare:

- a lane contract doc in `docs/contracts/`
- an ADR recording the admission judgment
- fixture families for admitted, denied, and unavailable cases
- runtime test cases proving fail-closed behavior

## Anti-drift checklist

Reject a lane if it creates pressure toward:

- semantic authority
- retrieval authority
- workflow ownership
- orchestration behavior
- executor or agent-host behavior
- generic ETL posture
- generic rich-document abstraction

## Candidate comparison posture

Future candidates should be compared on:

- authority clarity
- deterministic admitted surface
- clean failure taxonomy
- low semantic-drift pressure
- fit with Cortex's bounded local role

## Candidate note template

Use this structure when evaluating a future lane:

- candidate lane:
- structural authority model:
- admitted input boundary:
- admitted extraction surface:
- explicit exclusions:
- deny conditions:
- unavailable conditions:
- `partial_success` posture:
- required provenance:
- required fixtures:
- anti-drift risks:
- admission judgment:
