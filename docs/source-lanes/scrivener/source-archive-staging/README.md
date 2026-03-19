# Scrivener Source Archive Staging

This directory is a non-canonical staging surface for raw or user-supplied Scrivener source archives that are kept in the repo workspace for provenance or local sanitization work.

It is not the canonical fixture intake surface.

Canonical evidence packets belong under `fixtures/scrivener/`.

Rules for this directory:

- do not treat staged raw archives here as admitted fixtures
- do not cite staged raw archives here as support proof
- keep provenance language explicit when a staged raw archive is used to derive a sanitized fixture
- prefer moving loose root-level Scrivener source archives here rather than leaving them directly under `docs/`
- keep any staged raw archives untracked unless there is an explicit repo decision to retain them

This directory exists to keep `docs/` organized without weakening the boundary between provenance staging and canonical fixture evidence.
