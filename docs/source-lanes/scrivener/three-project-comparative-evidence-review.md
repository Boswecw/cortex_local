# Scrivener Three-Project Comparative Evidence Review

## Status

Evidence-only comparative review.

This note does not admit Scrivener, does not authorize runtime implementation by itself, and does not convert three fixtures into compatibility proof.
`DECISIONS/0015-scrivener-stage1-authority-recon-authorization.md` is the separate authorization surface for bounded Stage 1 authority recon only.

## Purpose

This note compares the current three clean local `.scriv` project packets to determine which repeated structural observations are strong enough to narrow future Stage 1 authority-recon assumptions and which differences still require blocked or fail-closed treatment.

The review is bounded to:

- top-level authority candidate count and location
- authority readability and XML well-formedness
- binder hierarchy and role-surface visibility
- `BinderItem UUID` observation
- `Files/Data/<UUID>/...` correspondence observation at status level only
- package-surface differences that may matter for truthful Stage 1 status claims

It does not define extraction behavior.

## Reviewed Projects

| Fixture | Class | Provenance | Caveat |
| --- | --- | --- | --- |
| `fixtures/scrivener/ambiguous/scriv-sanitized-fixture-v1/` | `ambiguous` | sanitized derivative of a real project | original-source truth is not preserved; packet remains restricted evidence only |
| `fixtures/scrivener/positive/scriv-mixed-structure-sanitized-v1/` | `positive` | sanitized derivative of a real project | retained packet is text-side only and does not preserve binary asset behavior |
| `fixtures/scrivener/positive/faith-in-a-firestorm-sanitized-v1/` | `positive` | sanitized derivative of the same source lineage as the canonical malformed-authority negative packet | richer package surface is locally useful, but still restricted sanitized evidence only |

All three reviewed projects are Windows-shaped `.scriv` directories with top-level `.scrivx` authority files and `Version="2.0"` project XML.

## Per-Project Structural Observations

### `scriv-sanitized-fixture-v1`

- exactly one top-level `*.scrivx` authority candidate exists
- `xmllint --noout` validates the authority file as well-formed XML
- root metadata shows `Creator="SCRWIN-3.1.6.0"` and `Version="2.0"`
- binder surface contains 171 `BinderItem` nodes, max observed binder depth 4, and one each of `DraftFolder`, `ResearchFolder`, and `TrashFolder`
- `TemplateFolderUUID` and `BookmarksFolderUUID` are present
- 136 `Files/Data/<UUID>` directories also appear as binder UUIDs, with 35 binder UUIDs not mirrored as data directories and no observed data-only directories
- `Files/ProjectNotes`, `Files/styles.xml`, `Files/version.txt`, `Settings/`, and `Snapshots/` are present
- Stage 1 confidence impression: stronger for single-authority resolution and bounded structural role observation; weaker for complete correspondence claims because binder-only UUIDs are still present

### `scriv-mixed-structure-sanitized-v1`

- exactly one top-level `*.scrivx` authority candidate exists
- `xmllint --noout` validates the authority file as well-formed XML
- root metadata shows `Creator="SCRWIN-3.1.6.0"` and `Version="2.0"`
- binder surface contains 105 `BinderItem` nodes, max observed binder depth 4, and one each of `DraftFolder`, `ResearchFolder`, and `TrashFolder`
- `TemplateFolderUUID` and `BookmarksFolderUUID` are present
- 69 `Files/Data/<UUID>` directories also appear as binder UUIDs, with 36 binder UUIDs not mirrored as data directories and no observed data-only directories
- local item-type mix includes `Text`, `Folder`, `PDF`, and `Image`
- top-level package is lighter than the other two clean fixtures: no local `ProjectNotes`, `Snapshots`, `search.indexes.xml`, `binder.backup`, or `Icons/` were observed
- Stage 1 confidence impression: stronger for mixed manuscript/research/trash role observation and singular-authority resolution; weaker for complete correspondence claims because binder-only UUIDs remain

### `faith-in-a-firestorm-sanitized-v1`

- exactly one top-level `*.scrivx` authority candidate exists
- `xmllint --noout` validates the authority file as well-formed XML
- root metadata shows `Creator="SCRWIN-3.1.5.1"` and `Version="2.0"`
- binder surface contains 247 `BinderItem` nodes, max observed binder depth 3, and one each of `DraftFolder`, `ResearchFolder`, and `TrashFolder`
- `TemplateFolderUUID` and `BookmarksFolderUUID` are present
- 231 binder UUIDs are mirrored under `Files/Data/<UUID>`, 16 binder UUIDs are not mirrored, and 220 `Files/Data` directories have no matching binder UUID in the readable authority file
- top-level package is materially denser than the other two clean fixtures: `.xps`, `Files/ProjectNotes`, `Files/search.indexes.xml`, `Files/binder.backup`, `Files/binder.autosave.zip`, `Files/writing.history.xml`, `Icons/`, `Settings/`, and `Snapshots/` are all present
- this packet is also the clean same-source sibling for the canonical malformed-authority negative packet
- Stage 1 confidence impression: stronger for singular-authority resolution and richer package-surface observation; weaker for any generalized correspondence claim because the data-only surplus is large

## Cross-Project Invariant Matrix

| Observation | Repeats In | Stage 1 Reading | Notes |
| --- | --- | --- | --- |
| exactly one top-level `*.scrivx` candidate exists | all 3 | Stage-1-safe | strongest repeated authority invariant in the current clean set |
| top-level `*.scrivx` validates as well-formed XML | all 3 | Stage-1-safe | supports bounded authority readability checks only |
| root project `Version="2.0"` | all 3 | insufficient for general support | useful only as narrow observed scope, not compatibility proof |
| root `Creator` values are Windows `SCRWIN-3.1.x` | all 3 | insufficient for general support | all evidence remains inside a narrow Windows-shaped slice |
| one `DraftFolder`, one `ResearchFolder`, and one `TrashFolder` are visible | all 3 | Stage-1-safe | supports role-surface observation only, not subtree admission policy |
| `TemplateFolderUUID` and `BookmarksFolderUUID` are visible | all 3 | Stage-1-safe | structural role-surface observation only |
| some `BinderItem UUID` values are mirrored under `Files/Data/<UUID>` | all 3 | Stage-1-safe as observation only | supports status-level mapping observation, not extraction readiness |
| complete deterministic binder-to-data correspondence | none | not safe for Stage 1 readiness claims | all three fixtures show partial or uneven correspondence rather than complete proof |
| package auxiliaries such as `ProjectNotes`, `Snapshots`, `search.indexes.xml`, `binder.backup`, `Icons/`, or `.xps` | varies materially | harmless for Stage 1 if ignored | relevant later for fuller package understanding, not current authority truth |
| non-text binder item types | two of 3 | extraction-stage relevant only | `Image` and `PDF` visibility must not be upgraded into extraction support claims |

## Divergence And Blocker Analysis

| Difference | Classification | Why |
| --- | --- | --- |
| `Creator="SCRWIN-3.1.5.1"` vs `SCRWIN-3.1.6.0` | unresolved but tolerable for Stage 1 if fail-closed | enough to show minor Windows-version variation, not enough to claim compatibility breadth |
| binder UUIDs without matching `Files/Data/<UUID>` directories in all three clean fixtures | unresolved but tolerable for Stage 1 if treated as structural-only | this blocks complete mapping claims but does not prevent singular-authority observation |
| 220 data-only `Files/Data` directories in `faith-in-a-firestorm-sanitized-v1` | blocker for generalized correspondence or extraction claims | a readable authority file does not imply clean one-to-one correspondence truth |
| presence or absence of `ProjectNotes`, `Snapshots`, `search.indexes.xml`, `binder.backup`, `Icons/`, `.xps`, and similar auxiliaries | harmless for Stage 1 if ignored | these surfaces should not control first-slice authority truth by convenience |
| manuscript/research density and non-text item-type mix | blocker only for later extraction stages | useful for structural awareness, but not for extraction or inclusion policy |
| sanitized-derivative provenance across all three projects | blocker for admission or support claims | enough for disciplined observation, not enough for support certification |

## What This Review Supports

The current three clean fixtures are strong enough to support the following narrow claims only:

- within the current observed Windows-shaped slice, singular top-level authority resolution is a real repeated pattern rather than a one-project accident
- singular readable authority can truthfully expose binder role surfaces such as draft, research, trash, template, and bookmark references
- UUID-to-data correspondence is observable as a status surface across all three projects, but only as partial or conditional observation
- package-surface density varies enough that Stage 1 must ignore non-authority auxiliaries rather than infer meaning from them

## What This Review Does Not Prove

- Scrivener compatibility breadth
- `.scrivx` sufficiency by itself
- deterministic binder-to-content mapping across item types
- safe manuscript inclusion or research exclusion policy
- extraction readiness
- lane admission readiness

## Recommendation

Authorize docs-only tightening only.

Why:

- the strongest repeated invariant is now clear: one readable top-level `*.scrivx` inside a Windows-shaped `.scriv` package is a stable structural authority pattern across all three reviewed clean fixtures
- the same review also shows materially uneven correspondence density, including one project with a large data-only surplus, which means Stage 1 must still fail closed around mapping truth
- all three clean fixtures remain sanitized Windows `3.1.x` / `Version="2.0"` evidence only, so compatibility spread is still not proven

This review informed the later bounded Stage 1 authority-recon authorization decision, but it did not earn that authorization by itself.

Decision 0015 is the later explicit governance response to this evidence note.
This review remains evidence-only.
