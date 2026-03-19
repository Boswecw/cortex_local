# Sanitization Report

## Intent

This packet is a sanitized-derived negative fixture for Scrivener Phase 0 evidence only.
It preserves a readable sanitized authority candidate while adding a second conflicting top-level authority file.

## Observed lineage

- started from a sanitized derivative of the same source lineage already represented by `fixtures/scrivener/positive/scriv-mixed-structure-sanitized-v1/`
- retained the readable sanitized `Symbiogenesis - Gunnach Protocol.scrivx`
- added `Symbiogenesis - Gunnach Protocol - conflicting.scrivx` with altered authority-identifying metadata

## Sanitization and derivation changes

- replaced `content.rtf` and `notes.rtf` with placeholders
- replaced `synopsis.txt` with placeholder text
- sanitized binder/display titles in `*.scrivx`
- scrubbed selected device / modification metadata in `*.scrivx`
- removed bundled PDF exports if present
- removed autosave / backup binder artifacts if present
- added a second readable top-level `*.scrivx` authority candidate only in the negative derivative represented by this packet

## Caveats

- this is negative evidence only and does not prove general support
- same-source linkage is based on direct local comparison of readable authority metadata and repeated UUID-bearing structure
- multiple readable `*.scrivx` candidates do not resolve authority by themselves
