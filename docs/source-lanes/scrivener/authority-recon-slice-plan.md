# Scrivener Authority Recon Slice Plan

## Status

Authorized and implemented Stage 1 plan only.

This plan is authorized only through `DECISIONS/0015-scrivener-stage1-authority-recon-authorization.md`.
It does not authorize manuscript extraction, research extraction, lane admission, or broader Scrivener support.
The broader Scrivener gate remains blocked beyond Stage 1.

## Purpose

This note turns the current Scrivener evidence base into a bounded first-slice plan for authority reconnaissance only.

The slice answers structural truth questions.
It does not emit manuscript content.

Stage 1 status meanings for this plan are further tightened in:

- `docs/source-lanes/scrivener/authority-recon-status-semantics.md`
- `docs/source-lanes/scrivener/authority-recon-correspondence-semantics.md`

## Stage 1 scope

The first runtime slice should answer only:

- is there exactly one resolvable authority candidate?
- is the authority candidate readable and well-formed?
- what project-role surfaces are directly observable?
- can binder identifiers be observed?
- can candidate `Files/Data/<UUID>/...` correspondences be observed?
- can Cortex return `ready`, `denied`, or `unavailable` honestly without best-effort drift?

The slice must not:

- emit manuscript text
- emit research text
- decide manuscript eligibility
- normalize project items
- infer editorial or workflow semantics

## Denial and fail-closed taxonomy

| Condition | Stage 1 result | Notes |
| --- | --- | --- |
| input is not a local `.scriv` project directory | `denied` | outside the source boundary |
| request asks for manuscript extraction or workflow semantics | `denied` | outside Stage 1 scope |
| Scrivener observation is operator-disabled | `denied` | governance or operator posture only |
| no `*.scrivx` candidate is resolvable | `unavailable` | trust cannot begin |
| multiple conflicting `*.scrivx` candidates are present | `unavailable` | authority ambiguous |
| `*.scrivx` is malformed or unreadable | `unavailable` | fail closed on authority trust |
| directly expected correspondence for observed binder or item surfaces is missing or incomplete | `unavailable` | do not treat degraded correspondence as `ready` |
| required package surfaces are missing | `unavailable` | structure not trustworthy |
| candidate mapping can be stated only as unresolved and no direct correspondence incompleteness is observed | `ready` with constrained mapping status | honest observation without extraction permission |
| package state falls outside current evidence bounds | `unavailable` | do not invent repair behavior |

## Test plan outline

Positive structural tests:

- readable authority fixture yields `ready`
- role surfaces are observable when directly encoded
- candidate mapping surfaces are observable when directly encoded

Negative structural tests:

- malformed authority fixture yields `unavailable`
- directly incomplete correspondence fixture yields `unavailable`
- package resemblance without readable authority is insufficient
- fail-closed reason details remain structural only

Comparison tests:

- same-source clean baseline and malformed-authority sibling diverge only at the documented authority break
- unrelated positive fixtures still agree on role-surface and UUID-observation posture

Future ambiguity tests, not yet satisfiable:

- partial-package states
- degraded-correspondence cases beyond the direct missing or incomplete rule
- mapping-present but policy-ambiguous manuscript roots
- version-drift or migrated project shapes

## Implementation sequence

1. Add a bounded detector for local `.scriv` project directories only.
2. Enumerate top-level `*.scrivx` candidates and fail closed on zero or many.
3. Parse `*.scrivx` as XML and fail closed on unreadable or malformed authority.
4. Observe direct role surfaces such as draft, research, trash, template, and bookmarks when present.
5. Observe binder identifiers and candidate `Files/Data/<UUID>/...` correspondences without making inclusion decisions.
6. Emit a status-first result using the authority-recon draft contract.
7. Stop. Do not continue into manuscript extraction without separate approval.

If a case falls into the unresolved semantics described in `authority-recon-status-semantics.md`, stop and fail closed rather than invent a narrower runtime rule.
If a case falls into the degraded-correspondence boundary described in `authority-recon-correspondence-semantics.md`, do not upgrade it to `ready` by convenience.

## Exit conditions for this slice

This slice is complete only when:

- the authority-recon contract is implemented without content emission
- positive and negative structural tests pass
- outputs remain within `ready`, `denied`, and `unavailable`
- no policy or extraction claims leak into runtime behavior

## Non-goals

This slice must not become:

- a provisional Scrivener parser
- a manuscript exporter
- a research importer
- a project-management integration
- a bridge to generalized folder ingestion
