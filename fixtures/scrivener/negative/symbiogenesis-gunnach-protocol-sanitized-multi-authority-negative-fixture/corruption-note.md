# Corruption Note

Negative case type:
- multiple conflicting `*.scrivx` authority candidates

How it was created:
- started from a sanitized derivative
- retained the readable original sanitized `*.scrivx`
- added a second conflicting top-level `*.scrivx` copy with altered authority-identifying metadata

Why it matters:
- package shape may still appear normal
- project authority is now ambiguous
- Stage 1 authority resolution should fail closed rather than choose one candidate by convenience
