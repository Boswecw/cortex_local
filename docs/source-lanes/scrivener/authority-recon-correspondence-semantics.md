# Scrivener Authority Recon Correspondence Semantics

## Status

Governance hardening note only.

This note does not authorize runtime implementation by itself.
`DECISIONS/0015-scrivener-stage1-authority-recon-authorization.md` is the separate authorization surface for bounded Stage 1 authority recon only.
It narrows one specific Stage 1 semantic seam so future work cannot treat incomplete correspondence as structural success by convenience.

## Purpose

Stage 1 authority recon is allowed to observe candidate `Files/Data/<UUID>/...` correspondence only at status level.

Current evidence is now strong enough to tighten one boundary:

- singular readable authority does not by itself make incomplete or missing correspondence `ready`

This note decides only what can be decided safely now.
Anything still under-evidenced remains explicitly unresolved and fail closed.

## Scope

This note applies only to cases where:

- exactly one top-level `*.scrivx` authority candidate is present
- that authority candidate is readable and well-formed
- binder or item surfaces can be observed at least partially
- the open question is correspondence completeness, not authority readability

This note does not define:

- manuscript inclusion policy
- research inclusion policy
- extraction permission
- any new runtime status vocabulary beyond current repo terms

## Settled Stage 1 correspondence boundary

### `ready` with `mapping_unresolved`

Stage 1 may remain `ready` with `mapping_unresolved` only when all of the following are true:

- authority is singular, readable, and well-formed
- package shape remains structurally intact enough for honest observation
- correspondence can be discussed only as unresolved because deterministic interpretation is still under-evidenced
- no direct missing or incomplete expected content-path target has been observed for the binder or item surfaces being reported

This is an authority-observation result only.
It does not imply extractable manuscript support.

### `unavailable` with `mapping_unavailable`

Stage 1 must default to `unavailable` when readable authority is present but correspondence trust is directly degraded.

This includes:

- one or more expected content-path targets are directly missing for observed binder or item surfaces
- correspondence is present for some observed items but incomplete in a way that indicates partial package damage or partial package copy
- package resemblance remains but correspondence cannot be stated truthfully because required supporting surfaces are missing
- binder or item surfaces are readable but the correspondence needed to describe structural availability honestly is broken

These cases are not `ready`.
They are not extraction-denial cases.
They are fail-closed structural unavailability cases.

## Case table

| Condition | Stage 1 lane state | Mapping summary | Boundary |
| --- | --- | --- | --- |
| singular readable authority, structurally intact package, deterministic correspondence not yet proven, no direct missing target observed | `ready` | `mapping_unresolved` | observation only; no extraction claim |
| singular readable authority, one or more expected content-path targets directly missing | `unavailable` | `mapping_unavailable` | incomplete correspondence breaks truthful readiness |
| singular readable authority, some correspondences present but package looks partially degraded or incomplete | `unavailable` | `mapping_unavailable` | fail closed on degraded structural trust |
| singular readable authority, binder or item surfaces observed, role inclusion still policy-ambiguous, correspondence otherwise intact enough for honest observation | `ready` | mapping summary stated separately | not extraction-ready; policy remains out of scope |
| singular readable authority, partial package resemblance too weak to support truthful correspondence claims | `unavailable` | `mapping_unavailable` | structure cannot be trusted enough for Stage 1 readiness |

## Current evidence anchor

The current same-source missing-content pair narrows this rule directly:

- clean baseline: `fixtures/scrivener/ambiguous/scriv-sanitized-fixture-v1/`
- degraded sibling: `fixtures/scrivener/negative/the-heart-of-the-storm-sanitized-missing-content-negative-fixture/`

That pair is sufficient to support this narrow conclusion:

- direct missing expected correspondence must not be treated as `ready`

It is not sufficient to prove:

- extraction permission
- manuscript eligibility
- deterministic correspondence across all item types
- a broader repair or recovery rule

## What remains unresolved by design

The following still require more evidence before this boundary can be tightened further:

- mixed cases where some correspondence is absent outside the currently observed text-backed surfaces
- degraded auxiliary surfaces that may or may not matter to truthful Stage 1 observation
- compatibility or version-drift cases where correspondence conventions may differ
- correspondence irregularities for item types not yet well represented in the fixture set

Until that evidence exists, keep unresolved edge cases fail closed.

## Future evidence needed

To tighten this note further, the repo would need at least:

- additional same-source clean vs degraded pairs beyond the current missing-content case
- irregular fixtures showing partial-package or missing-auxiliary states
- compatibility fixtures showing whether correspondence conventions hold across version drift
- repeated observation that a narrower rule remains truthful across more than one source lineage

## Governance effect

This note sharpens Stage 1 semantics without granting runtime authority by itself.

It preserves the blocked posture beyond Stage 1.
It preserves the distinction between authority observation and content support.
It prevents future implementation from treating incomplete correspondence as `ready` by convenience.
