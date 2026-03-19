# Scrivener Stage 2 Evidence And Gate Packet

## Status

Companion governance and control note to `docs/source-lanes/scrivener/stage2-planning-packet.md`.

This packet does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.

## Purpose

This note narrows the evidence and gate portions of the canonical Stage 2 planning packet.

The current posture is explicit:

- Stage 1 authority recon is implemented
- Stage 2 planning is open
- the Stage 2 implementation gate remains closed

This packet exists to prevent the repo from treating better planning or additional fixtures as automatic implementation authority.
It is not a separate planning surface.

## 1. Current Gate Posture

The Stage 2 gate is closed.
`DECISIONS/0016-scrivener-stage2-implementation-remains-blocked.md` is the current explicit governance response to this packet and keeps the gate closed.

It may not be treated as open unless all of the following become true:

- the required evidence categories exist in materially broader form than the current lineage-limited packet
- the required contract prerequisites exist as bounded governance artifacts
- blocking findings listed in this packet have been retired or narrowed enough to support a truthful next slice
- a separate explicit governance decision authorizes a bounded Stage 2 implementation slice

Until then, the only legitimate work remains evidence gathering and contract hardening.

## 2. Required Stage 2 Evidence Categories

| Evidence category | Why it is required | Question it must pressure |
| --- | --- | --- |
| compatibility and version coverage | the current packet is still narrow and Windows-shaped | do Stage 1 authority and Stage 2 candidate rules survive version drift or migration differences? |
| item-type mapping diversity | current mapping proof is still limited to a narrow text-bearing slice | is binder-to-content correspondence deterministic across the relevant item classes without convenience inference? |
| manuscript-heavy vs research-heavy contrast | current fixtures show role surfaces, but not enough contrast to settle extraction boundaries | can manuscript vs non-manuscript inclusion and exclusion be enforced structurally rather than semantically? |
| degraded and partial correspondence coverage | current negatives prove direct missing-content and authority failure only | can degraded text-side states be represented truthfully without over-upgrading into extraction readiness? |
| irregular package and authority divergence beyond Stage 1 | current irregular cases are enough for Stage 1 fail-closed behavior, not for extraction planning trust | do divergent package states or structurally unusual authority surfaces collapse any bounded extraction claim? |
| migrated or structurally divergent project coverage | current evidence is still lineage-specific | are proposed Stage 2 rules durable across materially different project shapes rather than one source family? |
| same-source clean vs degraded comparison pairs | same-source pairs narrow causal claims better than unrelated negatives | which concrete failures force full unavailability, and which only narrow candidate eligibility? |

## 3. Evidence-To-Question Mapping

Each evidence category exists to retire a specific unresolved Stage 2 question.

### Compatibility and version coverage

This category must reduce uncertainty around:

- whether `*.scrivx` plus observed package correspondence remains stable across versions
- whether current Windows-shaped observations are too lineage-specific to support broader planning

### Item-type mapping diversity

This category must reduce uncertainty around:

- whether text-bearing item classes map deterministically enough for bounded extraction planning
- whether folder-like, auxiliary, or mixed-role items force semantic guessing

### Manuscript-heavy vs research-heavy contrast

This category must reduce uncertainty around:

- whether draft-root inclusion and research-root exclusion can be enforced structurally
- whether mixed-role projects pressure Stage 2 toward convenience heuristics

### Degraded and partial correspondence coverage

This category must reduce uncertainty around:

- whether missing auxiliary or partial text-side states can be represented honestly
- whether a future degraded truth model could exist without hiding uncertainty behind `ready`

### Irregular package and authority divergence

This category must reduce uncertainty around:

- whether readable authority plus package irregularity still blocks truthful extraction planning
- whether structurally unusual authority/package combinations can be categorized without broadening Stage 2 by convenience

### Migrated or structurally divergent project coverage

This category must reduce uncertainty around:

- whether Stage 2 planning rules survive materially different project layouts
- whether proposed constraints are robust enough to justify a later implementation discussion

### Same-source clean vs degraded pairs

This category must reduce uncertainty around:

- which failures break truth completely
- which failures only narrow candidate eligibility or keep a project planning-visible but implementation-blocked

## 4. Stage 2 Contract Prerequisites

Before any Stage 2 implementation could be considered, the repo must have all of the following contract work in place:

- the existing manuscript-eligibility scope note in `docs/source-lanes/scrivener/stage2-manuscript-eligibility-scope.md`
- the current manuscript-vs-non-manuscript boundary note in `docs/source-lanes/scrivener/stage2-manuscript-vs-non-manuscript-boundary.md`
- the current degraded or partial extraction truth-model note in `docs/source-lanes/scrivener/stage2-degraded-partial-truth-model.md`
- the current Stage 2 contract packet in `docs/source-lanes/scrivener/stage2-contract-packet.md`
- the current item-type inclusion and exclusion note in `docs/source-lanes/scrivener/stage2-item-type-inclusion-exclusion.md`

If contract drafting later shows that schema changes are necessary, the repo would also need:

- one minimal schema-delta note explaining exactly which fields or states are needed and why current schema surfaces are insufficient

No production schema broadening should occur before those documents exist and governance explicitly accepts them as implementation prerequisites.

## 5. Blocking Findings That Keep Stage 2 Closed

The following findings would keep Stage 2 implementation blocked even after more evidence is gathered:

- mapping remains inconsistent across relevant item classes or collapses outside the current narrow text-bearing slice
- manuscript vs research or workspace boundaries still require semantic interpretation, compile behavior, or workflow inference
- degraded states cannot be represented truthfully without overclaiming, concealment, or convenience-based `partial_success`
- compatibility evidence remains too narrow, too lineage-specific, or too version-local to justify a bounded implementation slice
- authority plus correspondence still does not support a truthful claim that candidate text-bearing items are extractable
- titles, ordering, hierarchy, or emitted section boundaries still depend on semantic guessing rather than explicit structural evidence
- text-side dependency posture remains unclear enough that Stage 2 would smuggle application behavior or unstable sidecar assumptions into Cortex

Any one of those is enough to keep the gate closed.

## 6. What Gate Readiness Would Mean

Even if the evidence packet improves, Stage 2 evidence readiness would mean only:

- the repo has enough bounded evidence to evaluate a Stage 2 implementation proposal
- the required contract surface exists
- the blocking findings have been narrowed to a reviewable implementation question

It would not mean:

- extraction is authorized
- Scrivener is admitted
- compatibility is solved
- the first Stage 2 proposal is automatically safe to build

Only a separate explicit governance decision could open a Stage 2 implementation slice.

## 7. Non-Goals And Still-Blocked Work

Even if the Stage 2 gate eventually opens, the following remain out of scope unless separately authorized:

- full Scrivener lane admission
- research extraction by default
- generalized Scrivener support claims
- compile, export, sync, collaboration, or live-application behavior
- convenience-based heuristics for manuscript inclusion
- compatibility claims broader than the evidence actually supports
- semantic, editorial, or workflow interpretation

This packet therefore hardens control.
It does not add capability.

## 8. Immediate Next Legitimate Move

The next legitimate move after this packet is still non-code.

It is one of:

- acquire the next compatibility-oriented or structurally divergent fixture packet

That remains evidence work only.
