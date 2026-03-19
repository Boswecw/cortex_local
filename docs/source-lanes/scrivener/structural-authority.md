# Scrivener Structural Authority

## Status

External evidence plus three local sanitized derivative fixtures, three local sanitized-derived negative fixtures, and one retained superseded raw-derived audit packet.

Local structural authority is not yet proven.

## Evidence base

| Evidence source | Type | Observation | Confidence |
| --- | --- | --- | --- |
| local workspace inspection | local | three extracted sanitized derivative fixtures exist under `fixtures/scrivener/ambiguous/` and `fixtures/scrivener/positive/`, three extracted sanitized-derived negative packets exist under `fixtures/scrivener/negative/`, and one earlier raw-derived negative packet is retained only as superseded provenance history | high |
| `scriv-sanitized-fixture-v1` extracted fixture | local sanitized derivative | direct inspection shows one top-level `.scriv` container, one sibling `.scrivx` file, and `Files/Data/<uuid>/...` storage artifacts including `content.rtf`, `notes.rtf`, `synopsis.txt`, `notes.styles`, and `content.styles` | medium |
| `faith-in-a-firestorm-sanitized-v1` extracted fixture | local sanitized derivative same-source baseline | direct inspection shows a readable sanitized `.scrivx`, explicit `DraftFolder`, `ResearchFolder`, `TrashFolder`, `TemplateFolderUUID`, and `BookmarksFolderUUID`, plus multiple `BinderItem UUID` values also present under `Files/Data/<UUID>/...` content storage paths | high |
| `scriv-mixed-structure-sanitized-v1` extracted fixture | local sanitized derivative | direct inspection shows `DraftFolder`, `ResearchFolder`, `TrashFolder`, `TemplateFolderUUID`, `BookmarksFolderUUID`, and multiple `BinderItem UUID` values also present under `Files/Data/<UUID>/...` content storage paths | medium |
| `faith-in-a-firestorm-sanitized-corrupt-scrivx-negative-fixture` extracted packet | local sanitized-derived negative | direct inspection shows a package-shaped `.scriv` container, sanitized `.scrivx` metadata, and a malformed `<Binder><BROKEN` surface; packet-local notes document removal of the closing `</ScrivenerProject>` tag, making the authority surface unreadable for trustworthy structural interpretation | high |
| `the-heart-of-the-storm-sanitized-missing-content-negative-fixture` extracted packet | local sanitized-derived negative | direct inspection shows readable `.scrivx` with `Creator="SCRWIN-3.1.6.0"`, `Version="2.0"`, and the same `BinderItem UUID="A5101A53-7D7B-425D-82F0-A2FDF9F156F5"` already present in `scriv-sanitized-fixture-v1`, while packet-local notes and archive listing show the expected `Files/Data/A5101A53-7D7B-425D-82F0-A2FDF9F156F5/content.rtf` is intentionally absent | high |
| `symbiogenesis-gunnach-protocol-sanitized-multi-authority-negative-fixture` extracted packet | local sanitized-derived negative | direct inspection shows two top-level readable authority files in the same package-shaped root; one preserves `Identifier="F101AD8E-09AC-4698-9380-3580DC648872"` and `Creator="SCRWIN-3.1.6.0"`, while the second alters authority-identifying metadata to `Identifier="CONFLICTING-SANITIZED-AUTHORITY"` and `Creator="SCRWIN-CONFLICT"` without removing readable binder structure | high |
| Scrivener 3 Windows manual | official external | on Windows a project appears as a `.scriv` folder and is opened by selecting the top-level `.scrivx` file inside it | medium |
| Scrivener 3 Mac manual | official external | the macOS bundle and Windows folder differ in appearance but not at the file level | medium |
| Scrivener 3 manuals | official external | the entire `.scriv` folder is the project, not the `.scrivx` file by itself | medium |

Official references:

- https://www.literatureandlatte.com/docs/Scrivener_Manual-Win.pdf
- https://www.literatureandlatte.com/docs/Scrivener_Manual-Mac.pdf

## Bounded conclusions

The following appear supportable from current evidence:

1. A Scrivener project is a container, not a single-file document.
2. Across three local sanitized derivative fixtures, a top-level `.scrivx` file is preserved alongside the project container rather than as a standalone file.
3. The same-source clean baseline directly exposes distinct `DraftFolder`, `ResearchFolder`, `TrashFolder`, template, and bookmark surfaces inside `.scrivx`.
4. Multiple `BinderItem UUID` values in the same-source clean baseline are also observable as `Files/Data/<UUID>/...` storage paths, which strengthens candidate binder-item to storage linkage.
5. The same-source clean baseline and sanitized-corrupted sibling narrow the fail-closed claim to authority corruption rather than simple source variation.
6. The sanitized-derived negative packet shows that package-shaped `.scriv` structure without readable authoritative `.scrivx` must be treated as insufficient.
7. The sanitized-derived missing-content packet shows that readable `.scrivx` plus package shape do not by themselves guarantee complete text-body availability.
8. The sanitized-derived multi-authority packet shows that multiple readable top-level `*.scrivx` candidates in the same package-shaped root must be treated as ambiguous authority rather than convenience-selected authority.
9. The `.scrivx` file appears necessary control material, but it is not proven locally sufficient project truth.

## Not yet proven

The following are not yet proven locally and must not be treated as settled contract truth:

- whether `.scrivx` is the sole structural authority for hierarchy, ordering, and safe source selection
- whether any additional artifact is required for stable binder truth
- whether all binder item types map deterministically to `Files/Data/<UUID>/...`
- how manuscript admission should be derived safely when `DraftFolder`, `ResearchFolder`, `TrashFolder`, templates, and compile flags coexist
- how research, trash, templates, notes, or metadata-only nodes should be treated by an eventual bounded lane contract
- whether malformed-authority cases should be surfaced as denied, unavailable, unreadable-authority, or some other bounded failure status
- whether readable-authority but missing-content cases should be surfaced as denied, unavailable, partial, or some other bounded failure status
- whether multi-authority cases should be surfaced as denied, ambiguous-authority, unavailable, or some other bounded failure status
- whether sanitization preserved every structural dependency needed for authority proof

## Current authority judgment

Current evidence supports this narrow interim posture:

- `.scrivx` is necessary structural control material
- three local sanitized derivative fixtures provide repeat local evidence of the package shape
- the same-source clean baseline and the second positive fixture make draft, research, trash, template, and bookmark distinction directly observable
- candidate binder UUID to `Files/Data/<UUID>/...` linkage is stronger than before, but still not deterministic contract truth
- the sanitized-derived negative packet strengthens the fail-closed case that package shape alone is insufficient without readable authority
- the sanitized-derived missing-content packet strengthens the fail-closed case that readable authority alone does not guarantee content completeness
- the sanitized-derived multi-authority packet strengthens the fail-closed case that multiple readable authority candidates cannot be resolved by convenience
- the same-source clean baseline and negative sibling reduce provenance ambiguity around that fail-closed claim
- the earlier raw-derived negative packet is retained only as superseded audit history and is not relied on for the current authority judgment
- `.scrivx` is not sufficient by itself to define the admissible project surface
- sole-authority claims remain blocked pending local fixture inspection
- sanitization and restricted-derivation limits still prevent the current fixture packet from serving as full admission proof

## Implementation gate impact

Structural authority remains unresolved for admission purposes.

Implementation is blocked pending:

- compatibility or newer-version fixture coverage
- broader irregular coverage beyond one sanitized-derived corrupted-authority case, one sanitized-derived missing-content case, and one sanitized-derived multi-authority case
- read-only proof of safe binder selection and inclusion rules
- read-only proof of deterministic item identity and content linkage across item types
