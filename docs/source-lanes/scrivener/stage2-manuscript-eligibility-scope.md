# Scrivener Stage 2 Manuscript-Eligibility Scope Note

## Status

Governance and planning note only.

This note does not authorize Stage 2 implementation.
It does not authorize extraction.
It does not admit the Scrivener lane.

## Purpose

This note defines the narrowest truthful meaning of manuscript-eligible observation for Stage 2 planning.

It exists to prevent Stage 2 from collapsing into:

- general Scrivener extraction
- convenience-based draft inclusion
- research import by omission
- semantic guesses about what the manuscript "really is"

The planning question here is not "what can Cortex extract now?"

It is:

- what item surfaces could ever become candidates for bounded manuscript extraction planning?
- what item surfaces must remain excluded by default?
- what proof would still be required before any candidate could be treated as extractable?

## 1. Manuscript-Eligible Means Candidate Only

Within Stage 2 planning, manuscript-eligible must mean candidate-only observation.

It does not mean:

- extraction-ready
- admitted for output
- safe to emit as manuscript text
- globally representative across Scrivener projects

At most, a future item may be considered candidate manuscript-eligible only if planning can eventually justify all of the following:

- the project is already in a bounded Stage 1 `ready` posture
- one singular readable top-level `*.scrivx` authority candidate is resolved
- the candidate item is reachable through an explicitly observed draft-root path rather than through research, trash, template, or bookmark-only surfaces
- the candidate item is structurally text-bearing rather than folder-only or obviously non-text
- the candidate item has non-degraded text-side correspondence sufficient for truthful bounded extraction planning
- the item can be ordered and identified from explicit project structure rather than semantic guesswork

Even when those conditions appear to hold, the result remains planning input only until separate governance proves the rest of the Stage 2 boundary.

## 2. Candidate Inclusion Signals Only

The following are allowed only as candidate inclusion signals for planning:

- membership under an explicitly observed `DraftFolder` subtree
- a text-bearing binder item type rather than `Folder`, `PDF`, `Image`, or another non-text item class
- direct UUID-level correspondence to a text-side content location that is present and not already known to be degraded
- explicit binder order that can be described structurally without inferring narrative meaning
- item titles or labels only when they are treated as structural identifiers, not semantic headings by default

No single signal above is sufficient by itself.

Stage 2 planning must treat them as cumulative evidence questions, not as shortcut admission rules.

## 3. Excluded By Default

The following must remain non-manuscript-eligible by default during Stage 2 planning:

- anything under `ResearchFolder`
- anything under `TrashFolder`
- template or bookmark surfaces
- folder-only items
- non-text item types such as `PDF` or `Image`
- project notes, snapshots, backups, indexes, styles, icons, and other auxiliary package surfaces
- any item with degraded, missing, or structurally unresolved correspondence
- any item whose role would have to be inferred from labels, status, keywords, editorial metadata, or compile behavior
- any item whose inclusion would require live-application semantics, workflow meaning, or export logic

These exclusions preserve the fail-closed posture while Stage 2 remains planning-only.

## 4. What Stage 1 Proves Here And What It Does Not

Stage 1 provides only the following usable prerequisites for this note:

- singular authority can be resolved
- role surfaces such as draft, research, trash, template, and bookmarks can be observed
- candidate correspondence can be described structurally
- directly degraded correspondence can fail closed

Stage 1 does not prove:

- that all items under `DraftFolder` are manuscript-eligible
- that text-bearing items outside `DraftFolder` are automatically excluded or includable
- that `content.rtf` alone is sufficient for truthful emission
- that item titles or binder order can be emitted as manuscript structure without further proof
- that mapping anomalies can be ignored safely

## 5. Evidence Still Needed Before Any Eligibility Rule Could Be Authorized

Before any Stage 2 implementation could use a manuscript-eligibility rule, the repo would need fixture-backed proof for at least:

- repeated draft-root patterns across more than one source lineage
- explicit contrast between draft-root and research-root text-bearing items
- repeated evidence about which text-bearing item classes actually correspond to candidate manuscript text
- same-source clean vs degraded pairs showing when a candidate item stays eligible and when it must fail closed
- repeated evidence about whether binder order and item titles are structurally trustworthy enough for bounded emission
- compatibility-oriented fixtures showing whether the same planning rule survives version drift

Without that evidence, manuscript-eligible must remain a planning label only.

## 6. Planning Questions This Note Leaves Open

This note intentionally does not settle:

- whether `DraftFolder` is necessary, sufficient, or only one strong signal
- whether nested folders inside draft roots should ever emit titles or only ordering
- whether synopsis, notes, or related sidecars matter to extraction truth
- whether partially mapped draft items could ever support `partial_success`
- whether some text-bearing item classes should remain permanently excluded from the first extraction slice

Those questions belong to later Stage 2 governance artifacts, not to this note alone.

## 7. Non-Goals

This note must not be read as:

- a Stage 2 contract
- a Stage 2 schema plan by itself
- manuscript extraction authorization
- a claim that Stage 2 implementation is now safe
- a claim that Scrivener lane admission is getting close

It is only a bounded scope note for one planning seam.

## 8. Immediate Next Legitimate Move

The next legitimate planning move after this note is:

- draft the manuscript-vs-non-manuscript boundary note

That follow-on note should define how draft, research, trash, template, bookmarks, and auxiliary surfaces interact when item roles are mixed or boundary pressure is high.
