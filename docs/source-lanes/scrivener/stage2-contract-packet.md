# Scrivener Stage 2 Contract Packet

## Status

Companion governance and control note to `docs/source-lanes/scrivener/stage2-planning-packet.md`.

This packet does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.

## Purpose

This note narrows the contract portions of the canonical Stage 2 planning packet.

It exists to answer a narrow question:

- what could Stage 2 emit honestly?
- what must Stage 2 refuse to emit?
- how would degraded or mixed-validity cases need to be represented?
- what schema change, if any, would be minimally necessary before implementation?

This packet does not describe current runtime behavior.
Current runtime remains capped at the implemented Stage 1 authority-recon slice.
It is not a separate implementation authorization surface.

## 1. Contract Posture

Any future Stage 2 slice should inherit Cortex's shared extraction-result posture rather than invent a Scrivener-only success vocabulary.

That means a future Stage 2 contract should remain bounded by:

- `docs/contracts/extraction-result.md`
- `docs/contracts/source-lane-scrivener-draft.md`
- `docs/source-lanes/scrivener/stage2-planning-packet.md`
- `docs/source-lanes/scrivener/stage2-manuscript-vs-non-manuscript-boundary.md`
- `docs/source-lanes/scrivener/stage2-degraded-partial-truth-model.md`
- `docs/source-lanes/scrivener/stage2-item-type-inclusion-exclusion.md`
- `docs/source-lanes/scrivener/stage2-evidence-and-gate.md`

Stage 2 therefore must remain:

- syntax-only
- manuscript-eligible only
- structurally provenance-backed
- fail-closed on unresolved boundary pressure

Stage 2 must not become:

- general Scrivener support
- research import
- project normalization
- editorial or workflow interpretation

## 2. Minimum Stage 2 Result And Status Model

If Stage 2 were later authorized, it should reuse the shared extraction-result state vocabulary and define only the following operational meanings:

### `ready`

`ready` should mean:

- bounded Stage 2 output was emitted for the full contract-admitted manuscript-eligible surface
- emitted items were structurally identifiable and contract-admitted
- no unresolved or directly degraded item inside the admitted emission scope was silently dropped

`ready` must not mean:

- the whole `.scriv` project is fully extractable
- research or workspace content was considered in-bounds
- compatibility breadth is solved

### `partial_success`

`partial_success` may exist only if all of the following are true:

- some contract-admitted manuscript-eligible items can be emitted honestly
- some in-scope candidate items cannot be emitted and must be omitted explicitly
- omission accounting is precise enough to explain what was emitted, what was withheld, and why
- the remaining uncertainty does not contaminate the truth of the emitted subset

`partial_success` must not be used as:

- a convenience bucket for unresolved manuscript boundaries
- a cover for semantically guessed item inclusion
- a substitute for `unavailable` when structural trust is broken

If those conditions cannot be met, Stage 2 must fail closed to `unavailable` instead.

### `unavailable`

`unavailable` should mean:

- project, authority, mapping, or boundary trust is too weak to support truthful emission
- candidate manuscript-eligible scope cannot be separated honestly from unresolved or degraded structure
- omission accounting is too weak to support bounded `partial_success`

### `denied`

`denied` should remain reserved for:

- requests outside the authorized Scrivener Stage 2 boundary
- research or workspace extraction requests when those remain out of scope
- requests that require semantic, editorial, compile, export, or workflow behavior
- operator or governance posture that disables Stage 2 work

### `stale`

No Scrivener-specific `stale` posture is needed for Stage 2 planning at this time.

If later runtime caching or freshness semantics require it, `stale` should remain governed by the shared extraction-result contract rather than by a Scrivener-only rule.

## 3. Potential Output Boundary

If later authorized, Stage 2 could emit only the following bounded output classes:

- bounded manuscript-eligible extraction units from contract-admitted text-bearing items
- bounded structural order only when explicit project truth supports it
- limited item titles only when they are explicitly encoded and contract-admitted as identifiers rather than semantic headings
- structural provenance sufficient to identify the authority basis and emitted item identities
- omission and exclusion summaries needed for truthful downstream handling

Stage 2 must not emit:

- research, trash, template, bookmarks, or workspace content by default
- notes, synopsis, comments, snapshots, labels, keywords, or other auxiliary surfaces unless separately admitted by contract
- semantic manuscript categories, chapter claims, editorial state, or workflow meaning
- completeness claims broader than the contract-admitted emission scope
- output whose inclusion depends on compile behavior, application behavior, or semantic guesswork

## 4. Degraded And Mixed-Validity Truth Model

Degraded or mixed-validity cases would need to follow a strict truth model.

| Condition | Allowed state | Required contract behavior | Prohibited shortcut |
| --- | --- | --- | --- |
| all contract-admitted manuscript-eligible items are emittable and structurally trustworthy | `ready` | emit bounded output with explicit structural provenance | implying whole-project completeness |
| some contract-admitted items are emittable and some are explicitly non-emittable or degraded, but the emitted subset remains truthful and omission accounting is explicit | `partial_success` | report emitted subset plus omission counts and reason classes | silently dropping hard cases while claiming `ready` |
| candidate items exist but manuscript boundary remains unresolved | `unavailable` | emit no extraction output | treating unresolved candidates as a smaller `partial_success` subset by convenience |
| structurally present items are outside the settled contract boundary and cleanly separable from the admitted surface | `ready` or `partial_success` | record exclusion as contract-boundary truth, not as failure | pretending excluded items were part of the emitted manuscript surface |
| mapping is partially resolvable but unresolved items contaminate the truth of ordering, titles, or item inclusion | `unavailable` | fail closed | emitting only the apparently easy items while hiding structural contamination |
| authority is readable but correspondence is too degraded for truthful item emission | `unavailable` | preserve fail-closed posture | upgrading degraded correspondence into extractable output |

Within this model, three item-level dispositions would need to remain explicit:

- `emitted`: contract-admitted and actually emitted
- `excluded_by_contract`: structurally observable but outside the admitted Stage 2 surface
- `withheld_unavailable`: candidate or in-scope item that cannot be emitted truthfully

If a future implementation cannot distinguish those three dispositions cleanly, it should not be authorized.

## 5. Non-Emission And Refusal Rules

Stage 2 would need explicit refusal rules before code exists.

It must not emit extraction outputs when:

- manuscript vs non-manuscript boundary is unresolved for the candidate item population
- degraded mapping drops below the truthful completeness threshold for the proposed emission scope
- item types fall outside the settled inclusion and exclusion contract
- titles, ordering, or grouping would require semantic inference
- any requested output would imply research import, workflow meaning, or compile semantics
- the project is only partially understandable in a way that cannot be represented honestly as `partial_success`

In those cases, Stage 2 must:

- return `denied` when the request is out of scope
- return `unavailable` when the structure is in scope but not truthfully emittable

It must not respond by:

- downgrading silently to a smaller hidden subset
- emitting "best effort" content without omission accounting
- masking unresolved boundaries behind generalized completeness wording

## 6. Minimum Schema Planning Need

No production schema change should be assumed yet.

If Stage 2 were later authorized and current extraction-result surfaces proved insufficient, the smallest plausible schema delta should be limited to:

- one bounded emission-scope summary that distinguishes contract-admitted scope from broader project scope
- one omission-summary structure that records omitted count and omission reason classes
- one per-unit structural provenance addition sufficient to identify the emitted item without semantic labeling

No Stage 2 schema plan should introduce:

- semantic item categories
- editorial or workflow fields
- generalized project models
- broad completeness claims outside the admitted Stage 2 scope

If existing `extraction-result` plus bounded provenance can already carry the required truth, then no schema delta should be added at all.

## 7. What Remains Blocked Even With This Packet

Even with a drafted Stage 2 contract packet, the following remain blocked:

- Stage 2 implementation
- Scrivener lane admission
- research extraction by default
- compatibility claims broader than the evidence actually supports
- convenience-based inclusion heuristics
- any output shape not backed by future evidence, gate narrowing, and explicit authorization

This packet therefore drafts a contract boundary only.
It does not make that boundary build-ready by itself.

## 8. Immediate Next Legitimate Move

The next legitimate move after this packet is still non-code.

It is one of:

- acquire the next compatibility-oriented or item-type-diverse fixture packet needed by the Stage 2 evidence gate

Only after those exist could the repo truthfully revisit whether a narrower Stage 2 implementation proposal should even be reviewed.
