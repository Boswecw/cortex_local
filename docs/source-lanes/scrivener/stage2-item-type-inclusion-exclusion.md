# Scrivener Stage 2 Item-Type Inclusion And Exclusion Note

## Status

Governance and planning note only.

This note does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.

## Purpose

This note defines the narrowest truthful item-type posture for a future bounded Stage 2 slice.

It exists to prevent Stage 2 from drifting into:

- convenience-based inclusion of any item with text-side files
- folder or container emission by category confusion
- non-text import by omission
- support claims for item classes that the current evidence packet does not actually stabilize

The question here is not "what items can probably be rendered?"

It is:

- which observed item classes could ever become candidates for the first Stage 2 slice?
- which observed item classes must remain structural-only?
- which observed item classes remain excluded by default?
- which unproven or not-yet-observed classes must remain out of scope until evidence improves?

## 1. Current Observed Item-Type Vocabulary

Across the current clean fixture set, the repo has directly observed at least the following binder item types or role-root item classes:

- `Text`
- `Folder`
- `DraftFolder`
- `ResearchFolder`
- `TrashFolder`
- `PDF`
- `Image`

The current packet also exposes template and bookmarks as structural role surfaces, but not as evidence that they belong to a first extraction slice.

This note stays bounded to that observed vocabulary.
It does not generalize to unseen Scrivener item classes.

## 2. Candidate-Includable Item Class

Only one observed binder item class is currently plausible as a first-slice candidate:

- `Text`

Even `Text` remains candidate-only, not emit-ready by default.

`Text` may count as candidate-includable only when all of the following are true:

- the item is manuscript-side under the settled structural boundary
- correspondence is present and non-degraded
- item identity can be stated structurally
- order can be stated structurally
- the item does not depend on semantic, compile, or workflow inference

This note does not prove that every observed `Text` item will qualify.

## 3. Structural-Only Item Classes

The following classes may matter structurally but must not be treated as emitted text units in the first Stage 2 slice:

- `DraftFolder`
- `ResearchFolder`
- `TrashFolder`
- `Folder`

These classes may support:

- scope boundaries
- ordering boundaries
- hierarchy description
- exclusion reasoning

They must not be treated as:

- emitted manuscript text
- semantic section labels by default
- implicit proof that child items are safely emittable

## 4. Excluded-By-Default Item Classes

The following observed classes remain excluded by default from the first Stage 2 slice:

- `PDF`
- `Image`

The following non-binder but structurally visible surfaces also remain excluded by default:

- notes
- synopsis
- snapshots
- comments
- labels and keywords
- metadata-only surfaces
- compile and settings surfaces
- styles, icons, history, search, and other auxiliary package files

These may still matter as evidence or provenance context.
They do not become manuscript emission units.

## 5. Unknown Or Under-Evidenced Classes

Any binder item class not stabilized by the current evidence packet must remain excluded by default.

That includes:

- classes not yet observed locally
- classes observed only through narrow or ambiguous lineage pressure
- classes whose mapping or role would require semantic interpretation

Until repeated fixture evidence exists, do not widen the first Stage 2 slice beyond the currently observed and bounded item-type posture.

## 6. What Stage 1 Proves Here And What It Does Not

Stage 1 proves only:

- item identity and role surfaces can be observed structurally
- current clean fixtures contain `Text`, `Folder`, `PDF`, and `Image` item types plus explicit draft/research/trash role roots
- degraded correspondence can fail closed

Stage 1 does not prove:

- that all `Text` items are manuscript-side
- that any `Folder`-like class should emit titles or boundaries by default
- that `PDF` or `Image` classes can ever enter the first extraction slice
- that unseen item classes can be categorized safely from analogy
- that binder-to-content mapping is deterministic across all observed classes

## 7. Contract Pressure Created By This Note

Before any Stage 2 implementation could be considered, later contract work would need to distinguish at least:

- `emitted_text_item`
- `structural_only_container`
- `excluded_by_contract_non_text`
- `withheld_unavailable_text_item`
- `unknown_type_excluded`

The exact field names remain a contract question.
The distinction itself is not optional.

If a future implementation cannot keep those classes separate, it should not be authorized.

## 8. Non-Goals

This note must not be read as:

- proof that `Text` equals safe emission
- proof that all `Folder`-like surfaces are harmless
- proof that `PDF` or `Image` can never matter in later stages
- an authorization artifact for Stage 2
- a general Scrivener item taxonomy

It is only a bounded inclusion-and-exclusion note for the first Stage 2 slice.

## 9. Immediate Next Legitimate Move

The next legitimate move after this note is:

- acquire the next compatibility-oriented or item-type-diverse fixture packet

That evidence should pressure whether the current bounded item-type posture survives version drift and broader project shapes without forcing convenience-based widening.
