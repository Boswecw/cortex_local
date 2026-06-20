#!/usr/bin/env bash
#
# Build the Cortex AuthorForge service sidecar as a single frozen binary
# (PyInstaller onefile). Consumed by AuthorForge as a Tauri externalBin so
# document import / file-intelligence works in local desktop mode.
#
#   Output: packaging/dist/cortex-local
#
# Usage:
#   packaging/build.sh                # build (creates .venv-freeze if missing)
#   TARGET_TRIPLE=x86_64-unknown-linux-gnu packaging/build.sh
#       # also copy the artifact to packaging/dist/<name>-<triple> for Tauri
#
# Runtime deps are intentionally minimal: FastAPI + uvicorn + pydantic +
# jsonschema. cortex_runtime's lanes (epub/odt/rtf) are stdlib-only (zipfile /
# xml), so no extra parser library is bundled.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$HERE")"
VENV="$ROOT/.venv-freeze"
cd "$ROOT"

if [ ! -x "$VENV/bin/pyinstaller" ]; then
  echo "[build] creating freeze venv at $VENV"
  python3 -m venv "$VENV"
  "$VENV/bin/python" -m pip install -q --upgrade pip
  "$VENV/bin/python" -m pip install -q \
    "pydantic>=2.7.0" "fastapi>=0.109.0" "uvicorn>=0.27.0" "jsonschema>=4.21" pyinstaller
fi

"$VENV/bin/pyinstaller" packaging/cortex-local.spec --clean --noconfirm \
  --distpath packaging/dist --workpath packaging/build

BIN="packaging/dist/cortex-local"
echo "[build] built: $BIN"

# Optionally stamp a Tauri target-triple copy for externalBin consumption.
if [ -n "${TARGET_TRIPLE:-}" ]; then
  cp "$BIN" "packaging/dist/cortex-local-${TARGET_TRIPLE}"
  echo "[build] tauri sidecar copy: packaging/dist/cortex-local-${TARGET_TRIPLE}"
fi
