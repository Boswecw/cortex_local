# Scrivener Authority Recon Status Semantics

## Status

Governance hardening note only.

This note does not authorize runtime implementation by itself.
`DECISIONS/0015-scrivener-stage1-authority-recon-authorization.md` is the separate authorization surface for bounded Stage 1 authority recon only.
It exists to prevent the implemented Stage 1 authority-recon slice from drifting into convenience semantics.

## Purpose

Current Scrivener evidence is strong enough to narrow some Stage 1 status meanings and still too weak to settle others.

This note separates:

- status meanings that are already safe enough to specify
- status meanings that must remain unresolved and fail closed
- test boundaries that must not be crossed before further governance

Detailed handling of readable-authority but incomplete correspondence cases is recorded in:

- `docs/source-lanes/scrivener/authority-recon-correspondence-semantics.md`

## Settled Stage 1 status meanings

The following meanings are stable enough for the bounded Stage 1 implementation now authorized by Decision 0015.

### `denied`

Use `denied` only for out-of-scope or operator-refused work.

Settled `denied` cases:

- input is not a local `.scriv` project directory
- request asks for manuscript extraction, research extraction, or workflow semantics
- Scrivener observation is operator-disabled

### `unavailable`

Use `unavailable` when truthful structural status cannot be trusted enough to continue.

Settled `unavailable` cases:

- no resolvable top-level `*.scrivx` authority candidate exists
- top-level authority is unreadable or malformed
- multiple conflicting top-level `*.scrivx` candidates exist
- readable authority is present but directly expected content-path correspondence is incomplete or missing for the observed binder or item surfaces
- package shape is missing required structural surfaces before trust can begin
- project state falls outside currently observed evidence bounds

### `ready`

Use `ready` only when Stage 1 structural observation completed honestly.

`ready` does not mean manuscript extraction is allowed.

Settled `ready` requirements:

- exactly one resolvable top-level authority candidate exists
- authority is readable and well-formed XML
- package shape can be described honestly
- binder identifier surfaces can be observed
- mapping posture can be stated structurally without implying extraction permission
- no directly degraded correspondence surface requires `unavailable` under `authority-recon-correspondence-semantics.md`

## Current evidence-to-semantics mapping

The current fixture packet supports the following bounded mappings:

- `fixtures/scrivener/negative/faith-in-a-firestorm-sanitized-corrupt-scrivx-negative-fixture/`
  - evidence supports `unavailable`
  - reason class: malformed authority
- `fixtures/scrivener/negative/symbiogenesis-gunnach-protocol-sanitized-multi-authority-negative-fixture/`
  - evidence supports `unavailable`
  - reason class: ambiguous authority
- `fixtures/scrivener/positive/faith-in-a-firestorm-sanitized-v1/`
  - evidence supports clean same-source authority comparison only
- `fixtures/scrivener/positive/scriv-mixed-structure-sanitized-v1/`
  - evidence supports clean same-source authority comparison only
- `fixtures/scrivener/ambiguous/scriv-sanitized-fixture-v1/`
  - evidence supports clean same-source comparison for the missing-content case only

## Explicitly unresolved semantics

The following cases must not be silently operationalized as settled Stage 1 truth yet:

- correspondence irregularities beyond the direct incomplete or missing cases already narrowed in `authority-recon-correspondence-semantics.md`
- package states that preserve authority but lose auxiliary surfaces outside the currently observed negative set
- structurally readable projects whose draft or manuscript roots are still policy-ambiguous

The current missing-content fixture remains evidence for the broader degraded-correspondence zone:

- `fixtures/scrivener/negative/the-heart-of-the-storm-sanitized-missing-content-negative-fixture/`

That fixture now supports one narrowed conclusion:

- direct missing expected correspondence is not `ready`

It does not settle every degraded-correspondence edge case.

## Interim fail-closed rule

Until separate governance narrows these unresolved semantics, do not:

- treat missing-content cases as `ready` by convenience
- introduce `partial_success`
- infer recovery or repair behavior
- blur missing-content, ambiguous-authority, and malformed-authority into one opaque success path

Until separate governance tightens these unresolved semantics, the implemented Stage 1 slice must keep unresolved structural-trust cases fail-closed.

## Test boundary

The bounded Stage 1 implementation may assert only the settled cases in this note.

Initial Stage 1 tests may cover:

- denied for out-of-scope or operator-disabled requests
- unavailable for missing, malformed, or multi-authority top-level authority
- unavailable for directly incomplete or missing expected correspondence
- ready only for single-authority structural observation without content emission

Initial Stage 1 tests must not yet assert:

- `partial_success`
- manuscript extraction or manuscript ordering
- research extraction
- inclusion or exclusion policy decisions
- broader degraded-correspondence semantics beyond the direct missing or incomplete case

## Governance effect

This note hardens the Stage 1 authority boundary.

It does not authorize runtime work by itself.
It does not widen authorization beyond bounded Stage 1 authority recon.
It exists so that Stage 1 authorization remains narrower than implementation drift.
