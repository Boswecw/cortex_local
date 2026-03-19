# ADR 0010 - Next Lane Selection After Slice 7 Hardening

## Status

Accepted

## Context

After Slices 1 through 7 and the post-Slice-7 hardening pass, Cortex has:

- a shared source-lane framework
- explicit lane contracts for current admitted lanes
- deeper ugly-case coverage
- a lane-admission playbook

At this point, continuing format expansion by momentum would create more drift risk than value.
The next step therefore needs to be a formal selection decision rather than a parser implementation sprint.

## Decision

Cortex selects exactly one next-lane target for future implementation work:

- `ODT`

This is a governance selection only.
No new lane is admitted by this ADR.

## Why ODT was selected

- it has the clearest conventional structured-authoring authority model among the evaluated candidates
- it is the best fit for syntax-only extraction without rendering semantics
- it appears compatible with the current retrieval path without semantic special-casing
- it can likely be implemented through bounded local package parsing rather than broad external tooling
- it adds less drift pressure than HTML or EPUB

## Deferred alternatives

### HTML

Deferred because it creates too much pressure toward:

- rendering-aware interpretation
- boilerplate stripping
- content-vs-layout heuristics
- web-content semantics rather than authoring-source truth

### EPUB

Deferred because it is a more composite publication package than needed for the next step, with spine and package-structure complexity that increases failure-taxonomy and authority-surface pressure.

### Scrivener

Deferred explicitly as a special bounded project-source candidate rather than a routine lane.

It changes the authority model enough that it should not be admitted as just another document-family increment.

## Required anti-drift controls for future ODT work

If ODT is implemented later, the admission must stay narrow:

- local `.odt` only
- syntax-only extraction only
- no rendering or layout-fidelity claims
- no comment or tracked-change semantics
- no embedded object or media interpretation
- no semantic labels or summaries
- no `partial_success` unless a later pass can justify it honestly

## Consequences

Positive:

- the next implementation target is now chosen by governance rather than convenience
- future lane work can stay anchored to the shared lane framework
- Cortex keeps Scrivener on a separate special-track path

Negative:

- no new capability lands in this phase
- ODT still requires a future dedicated admission and implementation pass
