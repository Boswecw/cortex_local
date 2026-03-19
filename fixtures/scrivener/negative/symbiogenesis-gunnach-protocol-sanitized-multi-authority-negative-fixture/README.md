# symbiogenesis-gunnach-protocol-sanitized-multi-authority-negative-fixture

## Classification

- class: `negative`
- intake status: accepted with restrictions
- source provenance: sanitized-derived negative copy of the same source lineage already represented by `fixtures/scrivener/positive/scriv-mixed-structure-sanitized-v1/`
- platform evidence: readable authority candidate `Creator="SCRWIN-3.1.6.0"`, conflicting authority candidate `Creator="SCRWIN-CONFLICT"`
- project metadata evidence: both top-level candidates report project `Version="2.0"`
- authority posture: multiple readable top-level `*.scrivx` candidates with conflicting authority-identifying metadata

## Packet contents

- `README.md`
- `sanitization-report.md`
- `corruption-note.md`
- `Symbiogenesis - Gunnach Protocol.scrivx`
- `Symbiogenesis - Gunnach Protocol - conflicting.scrivx`
- `Files/`
- `Settings/`
- `symbiogenesis-gunnach-protocol-sanitized-multi-authority-negative-fixture.zip`

## Intended use

- multi-authority fail-closed observation
- ambiguous-authority evidence
- same-source clean-vs-multi-authority comparison against `fixtures/scrivener/positive/scriv-mixed-structure-sanitized-v1/`
- governance-only reference

## Direct local observations

- the packet preserves a package-shaped root with `Files/`, `Settings/`, and two top-level readable `*.scrivx` candidates
- `Symbiogenesis - Gunnach Protocol.scrivx` preserves `Identifier="F101AD8E-09AC-4698-9380-3580DC648872"`, `Creator="SCRWIN-3.1.6.0"`, and readable binder structure
- `Symbiogenesis - Gunnach Protocol - conflicting.scrivx` preserves readable binder structure but alters authority-identifying metadata to `Identifier="CONFLICTING-SANITIZED-AUTHORITY"` and `Creator="SCRWIN-CONFLICT"`
- direct local comparison with `scriv-mixed-structure-sanitized-v1` shows the original authority candidate shares the clean baseline identifier and repeated binder/data UUIDs such as `0A7EDD9F-9DE0-4CC9-9AC1-EE0E3769B6A8`, `323E42B8-881A-4A72-938C-1D683D78D8DF`, `B23591A4-8EC3-4E1F-B242-ECCA0207561C`, and `4908D479-188E-4232-AA7D-38FD12692DC5`
- project authority is therefore ambiguous even though both candidates remain readable

## Not suitable for

- support proof
- parser readiness claims
- `.scrivx` sufficiency proof
- deterministic mapping proof
- compatibility claims

## Known limitations

- one multi-authority case does not establish broad irregular coverage
- same-source linkage is observational evidence, not admission proof
- this packet does not prove final ambiguous-authority status semantics
- this packet does not resolve manuscript inclusion or exclusion rules
- this packet does not resolve compatibility spread

Evidence only. Not proof of general Scrivener support.
