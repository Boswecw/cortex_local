# Scrivener Stage 2 Manuscript-Vs-Non-Manuscript Boundary Note

## Status

Governance and planning note only.

This note does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.

## Purpose

This note defines the narrowest truthful structural boundary between candidate manuscript-side surfaces and non-manuscript-side surfaces for Stage 2 planning.

It exists to keep Stage 2 from drifting into:

- research import by omission
- convenience-based draft inclusion
- semantic guesses about narrative role
- boundary decisions derived from labels, editor state, or workflow meaning

The question here is not "what content should Cortex emit?"

It is:

- what surfaces may ever count as candidate manuscript-side inputs for later planning?
- what surfaces must remain non-manuscript by default?
- what kinds of mixed or boundary-pressure cases must fail closed instead of being normalized by convenience?

## 1. Boundary Posture

This note defines only a structural boundary.

It does not define:

- extraction readiness
- emitted output shape
- completeness claims
- semantic manuscript meaning

Within this note:

- `manuscript-side` means candidate-only structural placement inside the future Stage 2 planning surface
- `non-manuscript-side` means structurally observable but excluded from manuscript-side planning by default
- `boundary-unresolved` means the structure is observable but the boundary is too pressured or mixed to support truthful manuscript-side treatment

Anything `boundary-unresolved` must fail closed for planning purposes.

## 2. Candidate Manuscript-Side Signals

An item may count as candidate manuscript-side only when all currently available structural signals point in the same direction.

Those signals are:

- the item is reachable through an explicitly observed `DraftFolder` subtree
- the item is text-bearing rather than folder-only or obviously non-text
- the item is not present only through research, trash, template, or bookmark-oriented surfaces
- expected text-side correspondence is not already known to be directly degraded
- identity and order can be discussed structurally without semantic inference

Even when those signals align, the item remains candidate-only.
This note does not make it emit-ready.

## 3. Non-Manuscript-Side By Default

The following remain non-manuscript-side by default during Stage 2 planning:

- anything under `ResearchFolder`
- anything under `TrashFolder`
- template and bookmarks surfaces
- folder-only items
- non-text item classes such as `PDF`, `Image`, or other obviously non-text types
- notes, synopsis, snapshots, comments, labels, keywords, metadata-only surfaces, and package-side auxiliary files
- settings, compile, style, search, icon, history, and other project-management or application-side surfaces
- any structurally observed item whose inclusion would require compile behavior, workflow meaning, or live-application semantics

These surfaces may still matter as evidence.
They do not become manuscript-side by default.

## 4. Boundary-Pressure Cases

The following cases remain fail-closed:

### Text-bearing item outside draft-root

A text-bearing item reachable only through research or other non-draft structural surfaces remains non-manuscript-side by default.

### Mixed-role reachability

If an item appears reachable through both draft-side and non-draft-side structural paths, the boundary is unresolved until evidence proves how that relationship should be interpreted.

Do not normalize it into manuscript-side by convenience.

### Bookmark or reference pressure

Bookmark or reference-style reachability does not expand the manuscript-side surface.

Bookmarks may point at items.
They do not make bookmark surfaces manuscript-side.

### Draft-root container pressure

Folder-like or container items inside draft-root may matter to ordering and boundaries later, but they are not manuscript text by themselves.

Treat them as structural boundary pressure, not emitted manuscript content.

### Degraded correspondence inside draft-root

An item that otherwise appears draft-side but has degraded, missing, or structurally unresolved correspondence must not remain manuscript-side for planning convenience.

It becomes `boundary-unresolved` or unavailable-to-planning, depending on the surrounding gate semantics.

### Metadata- or title-driven inclusion

If an item's inclusion would depend on labels, titles, status fields, or other metadata being interpreted semantically, the boundary remains unresolved.

## 5. What Stage 1 Proves Here And What It Does Not

Stage 1 proves only:

- role surfaces such as draft, research, trash, template, and bookmarks can be observed
- directly degraded correspondence can fail closed
- text-side correspondence can be described only as bounded status truth

Stage 1 does not prove:

- that `DraftFolder` is sufficient for manuscript-side inclusion
- that all draft-side text-bearing items belong to the future emission surface
- that all non-draft text-bearing items are safely excluded across versions and project shapes
- that titles, hierarchy, or container structure can be emitted without further contract proof
- that mixed-role items can be normalized safely

## 6. Contract Pressure Created By This Note

Before any Stage 2 implementation could be considered, later contract work would need to preserve this boundary explicitly.

At minimum, a future Stage 2 contract would need to distinguish:

- `emitted` manuscript-side items
- `excluded_by_contract` non-manuscript-side items
- `withheld_unavailable` items whose boundary or structural trust is unresolved

If a future implementation cannot make those distinctions clearly, it should not be authorized.

## 7. Non-Goals

This note must not be read as:

- a Stage 2 authorization artifact
- a Stage 2 output contract by itself
- proof that draft-side equals manuscript output
- proof that non-draft text-bearing items can never matter
- proof that compatibility pressure is solved

It is only a boundary note for one planning seam.

## 8. Immediate Next Legitimate Move

The next legitimate planning move after this note is:

- draft the item-type inclusion and exclusion note

The degraded or partial extraction truth-model note now exists in:

- `docs/source-lanes/scrivener/stage2-degraded-partial-truth-model.md`
