# Decision 0016 - Scrivener Stage 2 implementation remains blocked

This record is governance-only.
It does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.

## Status

Accepted

## Date

2026-03-19

## Context

Decision 0015 authorized bounded Scrivener Stage 1 authority recon only and explicitly withheld any broader implementation authority.

Since that decision, the repo has accumulated a fuller Scrivener Stage 2 planning-control packet:

- `docs/source-lanes/scrivener/stage1-post-implementation-review.md`
- `docs/source-lanes/scrivener/stage2-planning-packet.md`
- `docs/source-lanes/scrivener/stage2-evidence-and-gate.md`
- `docs/source-lanes/scrivener/stage2-contract-packet.md`
- `docs/source-lanes/scrivener/stage2-manuscript-eligibility-scope.md`
- `docs/source-lanes/scrivener/stage2-manuscript-vs-non-manuscript-boundary.md`
- `docs/source-lanes/scrivener/stage2-degraded-partial-truth-model.md`
- `docs/source-lanes/scrivener/stage2-item-type-inclusion-exclusion.md`
- `docs/source-lanes/scrivener/stage2-fixture-acquisition-plan.md`

That packet now gives the repo a materially clearer planning surface than existed at the Stage 1 decision point.

It defines:

- candidate-only manuscript-side scope
- explicit non-manuscript and item-type exclusions
- explicit non-emission and refusal boundaries
- a bounded degraded or mixed-validity truth model
- a bounded fixture-acquisition and evidence-growth program
- blocking findings that would still keep Stage 2 closed

That planning maturity is real.
It is not implementation authority.

The controlling packet still records decisive unresolved gaps:

- no compatibility-oriented or newer-version fixture exists
- no materially broader manuscript-heavy, research-heavy, or structurally divergent clean baseline exists
- irregular coverage remains limited to malformed authority, one direct missing-content case, and one multi-authority case
- deterministic binder-to-content mapping across relevant text-bearing item classes remains unproven
- manuscript-side inclusion and non-manuscript exclusion remain planning boundaries rather than evidence-retired implementation rules
- degraded truth and `partial_success` remain explicitly constrained, hypothetical, or under-evidenced
- text-side dependency posture, including `content.rtf` and related sidecars, remains unresolved
- the current fixture packet remains sanitized, restricted, lineage-limited, and still below compatibility-grade or admission-grade breadth

Stage 1 runtime and tests remain bounded support only.
They prove status-first authority observation.
They do not prove bounded manuscript emission truth.

## Decision

Cortex explicitly does not authorize Scrivener Stage 2 implementation at this time.

The current Stage 2 planning-control packet is sufficient to justify an explicit authorization review.
It is not sufficient to justify a bounded Stage 2 build slice.

Planning completeness, contract clarity, or control-surface maturity must not be converted into implementation authority by momentum.

## Why Stage 2 remains blocked

### Evidence remains too narrow

The repo still lacks the evidence categories that the Stage 2 packet itself names as prerequisites for implementation review:

- compatibility or version-drift coverage
- materially broader manuscript-heavy and research-heavy contrast
- migrated or structurally divergent project coverage
- broader degraded, partial-package, or missing-auxiliary evidence
- repeated same-source clean vs degraded pairs beyond the current narrow set

Without those, the repo cannot claim that the proposed Stage 2 boundaries survive beyond the current Windows-shaped restricted packet.

### Candidate boundaries are not yet evidence-retired rules

The Stage 2 notes now define a narrower candidate shape, but they also preserve that those boundaries are still provisional:

- manuscript-eligible remains candidate-only rather than emit-ready
- `Text` remains candidate-includable only, not generally admitted for emission
- draft-side placement is not yet proven sufficient
- non-draft text-bearing exclusion is not yet proven durable across broader project shapes
- titles, order, hierarchy, and container handling remain blocked where semantic guessing would be required

That is good control discipline.
It is not a build-ready scope.

### Degraded truth is still under-evidenced

The current contract packet and degraded-truth note correctly constrain `partial_success`, omission accounting, and non-emission rules.

They do not prove that:

- omitted units can currently be counted and isolated truthfully
- degraded manuscript-side scope can be represented honestly across more than one narrow lineage
- omission accounting can be supported without new evidence or schema work

The repo therefore still lacks proof that a degraded Stage 2 slice could emit anything without concealment risk.

### Dependency posture remains unresolved

The current packet still does not retire the dependency question around `content.rtf` and related sidecars.

That means the repo cannot yet state the narrowest truthful Stage 2 emission surface without risking hidden assumptions about:

- text-body sufficiency
- auxiliary-surface irrelevance
- item identity and order durability when sidecars or partial-package states diverge

### The gate is still explicitly closed

The controlling Stage 2 packet, evidence-and-gate note, fixture-acquisition plan, and implementation gate all say the same thing:

- the gate remains closed
- broader evidence is still required
- only a later explicit governance decision could open a bounded Stage 2 slice

No decisive blocker named in those documents has yet been retired by new evidence.

## Decision boundaries

This decision does not authorize:

- Stage 2 runtime implementation
- manuscript extraction
- research or workspace extraction by default
- generalized Scrivener parser expansion
- tests for unimplemented Stage 2 behavior
- generalized Scrivener schema broadening
- convenience-based inclusion heuristics
- semantic, editorial, or workflow inference
- Scrivener lane admission
- compatibility claims broader than the current evidence actually supports

## Consequences

### Immediate consequences

- the current Stage 2 planning-control packet becomes explicit decision input only, not build authority
- `docs/source-lanes/scrivener/implementation-gate.md` should continue to show anything beyond Stage 1 as blocked
- outward repo surfaces should cite this decision so the current posture cannot be mistaken for conditional approval
- the runtime remains capped at the implemented Stage 1 authority-recon slice

### Boundary consequences

This decision does not reject Stage 2 forever.

It does require that any future Stage 2 authorization be earned by:

- materially broader evidence
- a rerun of the implementation gate
- a later explicit governance decision that supersedes this one

### Ongoing blocked posture

Scrivener remains unadmitted.

Everything beyond bounded Stage 1 authority recon remains blocked pending materially broader evidence and a later explicit authorization decision.

## Next legitimate move

The next legitimate move is still non-code:

- execute Wave 1 acquisition under `docs/source-lanes/scrivener/stage2-fixture-acquisition-plan.md`
- add compatibility-oriented and structurally divergent clean baselines before deriving new negative families
- revisit `docs/source-lanes/scrivener/stage2-evidence-and-gate.md` and `docs/source-lanes/scrivener/implementation-gate.md` only after that evidence exists

If this decision is later read as partial implementation clearance, it has been misread.
