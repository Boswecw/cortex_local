# Scrivener Stage 2 Degraded-Or-Partial Extraction Truth Model

## Status

Governance and planning note only.

This note does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.

## Purpose

This note defines the narrowest truthful way Stage 2 planning could ever represent degraded or partially emittable Scrivener projects.

It exists to prevent Stage 2 from drifting into:

- best-effort emission disguised as success
- vague `partial_success` claims with no omission accounting
- silent scope reduction when structural trust breaks
- convenience upgrades from unresolved structure into emitted output

The question here is not "can some text probably be recovered?"

It is:

- when could a bounded degraded posture ever be honest?
- when must Stage 2 stay `unavailable` instead?
- what omission and exclusion accounting would be required before a degraded posture could be reviewed as truthful?

## 1. Truth-Model Posture

This note defines only degraded and partial truth posture.

It does not define:

- the admitted manuscript-side boundary
- the full Stage 2 output contract
- schema implementation
- authorization for runtime behavior

Within this note:

- `ready` means all contract-admitted Stage 2 units inside the proposed emission scope are truthfully emittable
- `partial_success` means a bounded subset may be emitted only because omissions can be described completely and honestly
- `unavailable` means structural trust is too weak for truthful emission, even if some apparently promising fragments exist

## 2. `partial_success` Is Exceptional

`partial_success` must remain exceptional.

It may be considered honest only when all of the following hold:

- the manuscript-side boundary is already settled for the proposed emission scope
- the emittable subset is structurally identifiable without semantic guessing
- the non-emittable subset is also structurally identifiable
- omission causes can be named explicitly rather than inferred vaguely
- omission does not contaminate the truth of the emitted subset's identity, ordering, or declared scope

If any of those conditions fail, Stage 2 must remain `unavailable`.

## 3. Required Omission Accounting

Any future degraded posture would need explicit omission accounting at minimum:

- emitted-unit count
- excluded-by-contract unit count
- withheld-unavailable unit count
- omission reason classes tied to structural causes rather than semantic speculation
- a scope statement clarifying whether the result covers all currently admitted manuscript-side units or only a bounded honest subset

Without that accounting, `partial_success` would be misleading.

## 4. Allowed And Prohibited Degraded Cases

| Case | Allowed posture | Why | Not allowed |
| --- | --- | --- | --- |
| some manuscript-side units are structurally intact, some are directly degraded, and the degraded units can be counted and isolated without contaminating the emitted subset | `partial_success` | omission can be explained truthfully | silent omission with `ready` |
| manuscript-side boundary itself is unresolved for some candidate items | `unavailable` | emission scope cannot be stated honestly | shrinking scope by convenience |
| ordering or item identity of omitted units contaminates the truth of emitted ordering | `unavailable` | emitted subset cannot be represented honestly as complete within scope | emitting easy fragments as if order were preserved |
| non-manuscript-side units are present but cleanly excluded by settled boundary rules | `ready` or `partial_success` | exclusion is contract truth, not degradation | treating excluded units as omitted failures |
| degraded correspondence exists inside otherwise manuscript-side structure, but exact omitted units cannot be isolated | `unavailable` | omission accounting is not trustworthy | best-effort emission |
| auxiliary or sidecar loss affects only non-emitted, out-of-scope surfaces and does not change the admitted emission scope | potentially `ready` or `partial_success` | degradation does not contaminate the claimed scope | inflating degradation into unsupported semantics |

## 5. Reason Classes A Future Contract Would Need

If `partial_success` were ever introduced, the contract would need bounded omission reason classes such as:

- `boundary_unresolved`
- `mapping_unavailable`
- `mapping_contaminated`
- `non_emittable_item_type`
- `excluded_by_contract`

These must remain structural.

They must not become:

- editorial judgments
- narrative-role claims
- semantic labels
- workflow interpretations

## 6. When `unavailable` Must Win

Stage 2 must remain `unavailable` when:

- the manuscript-side boundary is mixed or unresolved
- omitted units cannot be counted or identified honestly
- ordering, titles, or grouping of emitted units depend on omitted or degraded units in a way that contaminates the truth of the emitted subset
- degraded correspondence pressure is broad enough that the remaining apparently emittable subset may not represent a truthful contract scope
- a caller would likely infer more completeness than the repo can justify

This means `unavailable` remains the default fail-closed answer for pressured cases.

## 7. Contract Pressure Created By This Note

Before any Stage 2 implementation could be considered, later contract work would need to preserve all of the following:

- explicit distinction between `excluded_by_contract` and `withheld_unavailable`
- explicit omission accounting for any `partial_success`
- explicit proof that the emitted subset remains truthful within its declared scope
- explicit refusal to emit when omission accounting is weaker than the claimed result state

If a future contract cannot preserve those boundaries, `partial_success` should not be admitted for the first Stage 2 slice.

## 8. Schema Pressure Created By This Note

This note does not require a schema change by itself.

If later implementation authorization were considered, the smallest plausible schema support for degraded truth would be:

- omission counts
- omission reason classes
- an emission-scope summary explaining what the result does and does not cover

If the shared extraction-result surface plus bounded provenance cannot carry those fields honestly, Stage 2 should stay blocked until a minimal schema-delta note is accepted.

## 9. Non-Goals

This note must not be read as:

- authorization for `partial_success`
- proof that degraded Scrivener extraction is safe
- proof that omission accounting is currently possible
- a claim that Stage 2 implementation is ready

It is only a planning note for one degraded-truth seam.

## 10. Immediate Next Legitimate Move

The next legitimate planning move after this note is:

- acquire the next compatibility-oriented or item-type-diverse fixture packet

The item-type inclusion and exclusion note now exists in:

- `docs/source-lanes/scrivener/stage2-item-type-inclusion-exclusion.md`
