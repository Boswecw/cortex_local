"""PyInstaller entrypoint for the Cortex AuthorForge service sidecar.

AuthorForge launches Cortex Local as a Tauri-managed sidecar — a single frozen
binary. uvicorn is handed the FastAPI app *object* (not the
``"service.authorforge_app:app"`` import string), so the frozen binary never
depends on re-importing ``service.authorforge_app`` from a writable source tree
at runtime.

Host/port come from the environment the desktop shell bridges in
(``CORTEX_SERVICE_HOST`` / ``CORTEX_SERVICE_PORT``), defaulting to the loopback
:8004 surface AuthorForge's local-support lane probes (``CORTEX_URL`` /
``/health``). Cortex is loopback-only by default: it receives file/manuscript
text and must not be exposed off-host.
"""

from __future__ import annotations

import os

import uvicorn

from service.authorforge_app import app


def main() -> None:
    host = os.environ.get("CORTEX_SERVICE_HOST", "127.0.0.1")
    port = int(os.environ.get("CORTEX_SERVICE_PORT", "8004"))
    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
