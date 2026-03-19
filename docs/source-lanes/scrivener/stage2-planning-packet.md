# Scrivener Stage 2 Planning Packet

## Status

Canonical governance and planning packet.

This packet opens Stage 2 planning only.
It does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.
`DECISIONS/0016-scrivener-stage2-implementation-remains-blocked.md` is the current explicit governance response to this packet.

## Purpose

This note defines the maximum truthful meaning of Scrivener Stage 2 in bounded Cortex terms now that:

- Stage 1 authority recon is authorized and implemented
- a post-implementation review exists
- that review concluded the repo may open Stage 2 planning only

This file is the main Stage 2 planning surface.
Companion notes may narrow evidence-and-gate and contract seams only.

The planning question is narrow:

- what could a bounded Stage 2 mean without collapsing into general Scrivener support?
- what Stage 1 outcomes are solid enough to rely on?
- what still blocks any Stage 2 implementation authorization?
- what evidence, contract, and schema work would be required before implementation could even be considered?

## Packet Structure

The Stage 2 planning packet is intentionally small:

- this file is the canonical Stage 2 planning packet
- `docs/source-lanes/scrivener/stage2-evidence-and-gate.md` is the companion note that narrows evidence categories, gate conditions, and blocking findings
- `docs/source-lanes/scrivener/stage2-contract-packet.md` is the companion note that narrows future result, output, refusal, degraded-case, and minimal schema-planning boundaries
- `docs/source-lanes/scrivener/stage2-fixture-acquisition-plan.md` is the bounded fixture and evidence program that turns the Stage 2 packet into concrete acquisition waves only

Those companion notes do not create separate implementation authority.
They only tighten sections of this packet.
The fixture-acquisition plan also does not create implementation authority.
It only sequences evidence growth.

## 1. Maximum Truthful Stage 2 Scope

Stage 2 may be planned only as a bounded manuscript-eligible extraction-definition layer.

That means Stage 2 planning may define only:

- how candidate text-bearing project items could be classified for possible manuscript eligibility
- what binder-to-content mapping proof would be required before any item could be treated as extractable
- how manuscript, research, trash, template, and bookmarks boundaries would need to be separated contractually
- what degraded or partial extraction truth model would be needed if eligibility is not uniform across a project
- what dependency posture, including text-side storage expectations, would need explicit governance before implementation

Stage 2 must not be defined as:

- general Scrivener support
- full `.scriv` extraction
- research import
- workflow, compile, or export behavior
- lane admission by another name

## 2. What Stage 1 Proved And Stage 2 May Rely On

Stage 2 planning may rely only on the following Stage 1 results:

- one local `.scriv` project directory can be observed at a time without widening into general folder ingestion
- exactly one top-level `*.scrivx` authority candidate can be resolved or fail closed truthfully
- missing, multiple, malformed, and directly incomplete authority or correspondence states can fail closed as `unavailable`
- unsupported input and operator-disabled posture can fail closed as `denied`
- draft, research, trash, template, and bookmarks role surfaces can be observed structurally
- candidate `Files/Data/<UUID>/...` correspondence can be described only as status truth, including `candidate_mapping_observed`, `mapping_unresolved`, and `mapping_unavailable`
- service status can report the implemented slice without promoting Scrivener into `admitted_source_lanes`

Stage 2 planning must not rely on any claim that Stage 1 did not prove, including:

- deterministic binder-to-content mapping across item types
- `.scrivx` sufficiency by itself for extraction truth
- manuscript eligibility of any observed item
- compatibility breadth beyond the currently observed Windows-shaped `SCRWIN-3.1.x` / `Version="2.0"` slice

## 3. What Still Blocks Any Stage 2 Implementation

The following remain unresolved and block any Stage 2 implementation authorization:

- whether `*.scrivx` plus currently observed package correspondence is sufficient for bounded extraction truth
- deterministic binder-to-content mapping across the relevant text-bearing item classes
- manuscript vs research/workspace inclusion and exclusion rules
- whether titles, folders, and hierarchy order can be emitted without semantic guessing
- what degraded or partial extraction truth model would be honest if only some candidate items are eligible
- compatibility breadth across versions, migrations, and structurally different projects
- what text-side dependency posture, including `content.rtf` and related sidecars, would be required for truthful extraction
- which item classes force semantic or application-behavior guessing and must therefore remain excluded

Until those questions are answered by separate evidence and contract work, Stage 2 implementation must remain blocked.

## 4. Evidence Requirements Before Any Stage 2 Authorization

The repo would need additional evidence before any Stage 2 implementation could be considered, including at least:

- one or more compatibility-oriented or newer-version fixtures
- additional manuscript-heavy fixtures showing repeated text-item patterns
- additional research-heavy or mixed manuscript/research fixtures showing boundary pressure explicitly
- item-type diversity fixtures that distinguish text-bearing, folder-like, and non-text item classes without convenience inference
- degraded fixtures beyond the current direct missing-content case, such as partial-package, missing-auxiliary, or structurally incomplete correspondence states
- repeated same-source clean vs degraded pairs that clarify which failures break truthful extraction and which only narrow availability
- fixture-backed evidence about whether manuscript ordering and item titles are explicitly encoded enough to recover without semantic guessing

The current sanitized and restricted evidence packet is enough for planning.
It is not enough for implementation authorization by itself.

The current Stage 2 evidence-and-gate control surface is now defined in:

- `docs/source-lanes/scrivener/stage2-evidence-and-gate.md`

That companion note narrows evidence categories, gate conditions, and blocking findings only.

## 5. Contract And Schema Planning Needs

Before implementation, Stage 2 planning would need to produce at least:

- one bounded Stage 2 scope note defining what counts as manuscript-eligible observation
- one manuscript-vs-non-manuscript boundary note defining inclusion and exclusion pressure
- one degraded or partial extraction truth note defining when `ready`, `partial_success`, or continued `unavailable` could ever be honest
- one item-type inclusion and exclusion note defining which observed classes could ever enter the first slice and which remain structural-only or excluded
- one Stage 2 contract draft describing the maximum truthful result shape for any future manuscript-eligible extraction slice

The first of these planning artifacts is now defined in:

- `docs/source-lanes/scrivener/stage2-manuscript-eligibility-scope.md`
- `docs/source-lanes/scrivener/stage2-manuscript-vs-non-manuscript-boundary.md`
- `docs/source-lanes/scrivener/stage2-degraded-partial-truth-model.md`
- `docs/source-lanes/scrivener/stage2-item-type-inclusion-exclusion.md`

The next control-layer packet that turns these needs into an explicit pre-implementation gate is now:

- `docs/source-lanes/scrivener/stage2-evidence-and-gate.md`

The current Stage 2 contract packet for future result, refusal, and degraded-case boundaries is now:

- `docs/source-lanes/scrivener/stage2-contract-packet.md`

That companion note narrows future output and refusal boundaries only.

Schema planning, if it becomes necessary, must remain minimal.

No production schema deltas should be added until:

- Stage 2 contract boundaries are settled
- the evidence packet justifies the new fields or states
- governance explicitly authorizes implementation work

## 6. Explicit Non-Goals And Still-Blocked Work

Even with Stage 2 planning open, the following remain blocked:

- Stage 2 runtime implementation
- full Scrivener lane admission
- generalized Scrivener extraction support
- research extraction by default
- compile, export, sync, collaboration, or live-application behavior
- convenience-based inclusion heuristics
- compatibility claims from the current narrow fixture set
- semantic labeling, chapter inference, editorial-state inference, or workflow interpretation

Stage 2 planning must remain constitutional and fail closed.

## 7. Authorization Boundary

This packet does not authorize Stage 2 implementation.

Any future Stage 2 implementation would still require a separate explicit governance decision grounded in:

- the Stage 1 review
- new Stage 2 evidence
- Stage 2 contract and semantics artifacts
- a narrowed implementation gate showing why the next slice is safe to build

That separate governance decision now exists as `DECISIONS/0016-scrivener-stage2-implementation-remains-blocked.md`.
It concludes that the current packet is strong enough for explicit review but not yet strong enough for implementation authorization.

Until materially broader evidence exists and a later decision supersedes Decision 0016, Cortex remains capped at the implemented Stage 1 Scrivener authority-recon slice.

## 8. Immediate Next Legitimate Planning Move

The next legitimate move after this packet is not code.

It is one of the following planning/evidence actions only:

- execute Wave 1 acquisition under `docs/source-lanes/scrivener/stage2-fixture-acquisition-plan.md`

That remains evidence work only, not implementation.
