# Cortex Contract - Source Lane Text

## Purpose

This document defines the bounded local text lanes for Cortex.

The text lanes admit local `.md` and `.txt` sources only when Cortex can recover syntax-only text structure honestly through the existing extraction-result contract.

## Admission

These lanes admit only:

- local file paths
- UTF-8 `.md` sources in the Markdown lane
- UTF-8 `.txt` sources in the plain-text lane
- declared media type `text/markdown` for Markdown when media type is present
- declared media type `text/plain` for plain text when media type is present

These lanes do not admit:

- remote text sources
- non-UTF-8 text payloads
- hidden format widening through generic binary fallback
- semantic markup interpretation

## Extraction scope

The text lanes admit only:

- paragraphs
- literal line-bounded text recovery
- Markdown heading recovery only from explicit leading `#` markers in the Markdown lane

The text lanes do not admit:

- inferred headings in plain text
- tables beyond literal delimiter counting already exposed through the extraction contract
- semantic labels
- summaries
- workflow hints

## Metadata posture

The text lanes expose only bounded structure metadata already allowed by the extraction contract:

- file name
- file extension
- source lane identifier

## Completeness posture

`ready` is allowed only when bounded text structures are recoverable honestly.

`denied` is required when:

- the source declares a media type outside the admitted text lane
- the file contains no bounded extractable text structures
- the source is not UTF-8 text
- the source crosses other existing bounded-lane rules

`unavailable` is required when:

- the file cannot be read

`partial_success` is not introduced by the text lanes.

## Retrieval compatibility

Ready text-lane extraction outputs may flow into the existing retrieval-package path only through the existing extraction-result contract.

Retrieval remains:

- deterministic
- syntax-derived
- non-ranking
- non-semantic
- non-canonical

## Explicit exclusions

These lanes explicitly exclude:

- semantic classification
- hidden markup interpretation beyond explicit Markdown heading markers
- workflow hints
- downstream action language
