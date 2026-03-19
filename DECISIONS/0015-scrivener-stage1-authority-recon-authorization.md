# Decision 0015 - Scrivener Stage 1 authority recon authorization

This record is governance-only.
It does not admit the Scrivener lane.
It does not authorize manuscript extraction, research extraction, or generalized Scrivener support.

## Status

Accepted

## Date

2026-03-19

## Context

Decision 0014 selected Scrivener as the next planning target after Slice 9 and explicitly withheld implementation authority pending separate governance.

Since that decision, the repo has accumulated a bounded Phase 0 evidence base and control surface for Scrivener:

- six active local evidence packets exist in the canonical intake surface
- three clean sanitized derivatives are available for read-only structural comparison
- three sanitized-derived negative packets now cover malformed authority, multiple readable top-level authority candidates, and directly missing expected correspondence
- Stage 1 status meanings have been tightened in `docs/source-lanes/scrivener/authority-recon-status-semantics.md`
- readable-authority but incomplete-correspondence handling has been tightened in `docs/source-lanes/scrivener/authority-recon-correspondence-semantics.md`
- a three-project comparative review now records the repeated clean-fixture authority patterns and the remaining divergence limits in `docs/source-lanes/scrivener/three-project-comparative-evidence-review.md`

The current evidence base still does not justify Scrivener lane admission, compatibility claims, extraction readiness, or deterministic binder-to-content truth across item types.

It does now show one narrower thing with sufficient repetition and failure coverage:

- within the currently observed Windows-shaped `SCRWIN-3.1.x` / project `Version="2.0"` slice, exactly one top-level readable `*.scrivx` authority candidate is a repeated structural invariant across the clean fixtures
- malformed, ambiguous, and directly incomplete authority or correspondence cases can already be described honestly as fail-closed `unavailable`

## Decision

Cortex explicitly authorizes bounded Scrivener Stage 1 authority recon only.

This authorization is narrower than lane admission and narrower than any extraction implementation.

Authorized Stage 1 work may only:

- inspect one local `.scriv` project directory at a time
- resolve exactly one authoritative top-level `*.scrivx` candidate
- fail closed on zero candidates, multiple candidates, malformed XML, unreadable XML, or package states outside current evidence bounds
- read well-formed project XML only
- observe binder identifiers, directly encoded role surfaces, and candidate `Files/Data/<UUID>/...` correspondence only at status level
- return bounded `ready`, `denied`, or `unavailable` results under the Stage 1 contract and semantics notes already present in the repo

Authorized Stage 1 work must not:

- emit manuscript text
- emit research text
- decide manuscript inclusion or non-manuscript exclusion policy
- normalize project items into broader Scrivener models
- upgrade incomplete correspondence into `ready`
- claim compatibility breadth beyond the current observed slice
- imply lane admission or general Scrivener support
- broaden CLI or README language into support claims
- use generalized Scrivener schema expansion as a back door to later-stage support

## Why Stage 1 is authorized

Stage 1 is authorized because the current repo now has enough evidence to support a bounded, fail-closed structural authority slice:

- three clean fixtures repeat singular readable top-level authority
- three negative fixtures cover the first necessary fail-closed authority and correspondence breaks
- current semantics notes already separate `denied`, `unavailable`, and `ready` for the cases the fixture set honestly supports
- Stage 1 is status-first and can remain within current evidence bounds without making extraction or admission claims

## Why No More Than Stage 1 Is Authorized

This decision does not clear the broader Scrivener gate.

The following remain blocking beyond Stage 1:

- no compatibility-oriented or newer-version fixture exists
- `.scrivx` is still not proven sufficient for full lane truth
- deterministic binder-to-content mapping across item types remains unproven
- manuscript inclusion and non-manuscript exclusion policy remain unresolved
- the evidence base is still sanitized and restricted rather than admission-grade

## Consequences

### Immediate consequences

- the repo may now implement the bounded Stage 1 authority-recon slice described in the existing Stage 1 contract and slice-plan artifacts
- those artifacts are now authorized build inputs for Stage 1 only
- the three-project comparative review remains evidence-only and must not be read as admission proof

### Boundary consequences

This decision does not authorize:

- a Scrivener admission ADR
- manuscript or research extraction
- generalized Scrivener parser momentum beyond Stage 1
- workflow, editorial, compile, export, sync, or application-host behavior
- compatibility claims from the current fixture set

### Ongoing blocked posture

Scrivener remains not admitted.

Everything beyond bounded Stage 1 authority recon remains blocked pending further evidence and separate governance.
