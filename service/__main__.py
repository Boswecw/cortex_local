"""Run the Cortex AuthorForge service.

    python -m service                       # binds 127.0.0.1:8004
    CORTEX_SERVICE_PORT=8010 python -m service

Loopback-only by default: Cortex receives file/manuscript text, so it must not
be exposed off-host. Override the host explicitly only inside a trusted runtime.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import uvicorn

# Ensure the repo root (parent of this package) is importable so `cortex_runtime`
# resolves regardless of the working directory uvicorn is launched from.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


def main() -> None:
    host = os.environ.get("CORTEX_SERVICE_HOST", "127.0.0.1")
    port = int(os.environ.get("CORTEX_SERVICE_PORT", "8004"))
    uvicorn.run("service.authorforge_app:app", host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
