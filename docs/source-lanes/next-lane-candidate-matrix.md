# Cortex Next-Lane Candidate Matrix

## Purpose

This document records the formal post-hardening evaluation of the next source-lane candidate set.

It does not admit a new lane.
It exists to choose one next target deliberately through the lane-admission playbook.

## Candidate set

Evaluated candidates:

- `ODT`
- `HTML`
- `EPUB`
- `Scrivener` as a special bounded project-source lane

## Comparison matrix

| Candidate | Authority clarity | Deterministic admitted surface | Failure taxonomy cleanliness | Semantic-drift pressure | Retrieval compatibility | Tooling posture | Fixture/test tractability | Constitutional fit | Judgment |
|---|---|---|---|---|---|---|---|---|---|
| `ODT` | strong | strong | strong | low to medium | strong | strong | strong | strong | select next |
| `HTML` | medium | weak to medium | medium | high | medium | strong | medium | weak to medium | defer |
| `EPUB` | medium | medium | medium | medium to high | medium | medium | medium | medium | defer |
| `Scrivener` | low as a routine lane, medium as a special lane | medium | weak to medium | high | low to medium | weak | weak | weak as a routine lane, medium as a special lane | defer as special project-source track |

## Candidate notes

### ODT

Why it scores strongest:

- it has a clear local package authority model based on OpenDocument XML rather than rendering output
- it can likely admit a bounded syntax-only surface close to DOCX:
  - paragraphs
  - headings when explicit style family or outline evidence is trustworthy
  - simple lists when explicit list markup exists
  - bounded table text when cell order is deterministic
- fail-closed behavior is easier to define:
  - encrypted or unreadable package
  - corrupt or missing `content.xml`
  - tracked changes, annotations, or embedded objects outside the bounded lane
- ready extraction should feed the current retrieval path without semantic special-casing
- local zip/xml handling is compatible with the repo's current bounded tooling posture

Main anti-drift risks to control later:

- style semantics being over-read as structure
- office-suite convenience pressure
- comments, tracked changes, embedded objects, and layout semantics

### HTML

Why it is deferred:

- HTML does not provide a single stable authoring-truth surface; boilerplate, navigation, layout scaffolding, and content blocks are easy to confuse
- the lane would quickly pressure Cortex toward:
  - boilerplate stripping
  - rendering-aware interpretation
  - content-vs-layout heuristics
  - web-page rather than authoring-source semantics
- ready extraction can feed retrieval, but only after hard problems about what the "real text" is have already been answered

HTML may still be viable later, but not as the next clean syntax-first lane.

### EPUB

Why it is deferred:

- EPUB is more structured than HTML, but it is still a composite publication package with:
  - spine ordering
  - navigation documents
  - package metadata
  - multiple HTML/XHTML content documents
- this creates more composite-structure pressure than the current lane set
- failure taxonomy is workable, but less clean than ODT because package truth and reading-order truth are split across files

EPUB remains plausible later, but it is not the narrowest next admission.

### Scrivener

Why it is explicitly deferred as a special case:

- Scrivener changes the authority model from "single bounded document lane" to "bounded project-source lane"
- it pressures Cortex toward:
  - project composition
  - binder semantics
  - snapshot or research-material boundaries
  - multi-file project truth rather than one-document truth

Scrivener should remain a later special-track evaluation, not a routine peer to ODT, HTML, or EPUB.

## Recommendation

Recommend exactly one next target:

- `ODT`

Reason:

- it offers the clearest next structured-authoring lane after DOCX and RTF
- it has the lowest combined drift pressure among the remaining conventional candidates
- it is most likely to fit the current shared lane framework without schema growth or retrieval special-casing

## Explicit deferrals

Defer for now:

- `HTML` because web-content and rendering drift pressure is too high for the next step
- `EPUB` because composite publication-package complexity is higher than needed for the next step
- `Scrivener` because it should be evaluated later as a special bounded project-source lane rather than as a routine document lane
