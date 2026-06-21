# PyInstaller spec — Cortex AuthorForge service sidecar (onefile).
#
# Produces a single self-contained binary that boots the :8004 local Cortex
# surface (FastAPI/uvicorn over cortex_runtime). Bundled as a Tauri externalBin
# by AuthorForge so document import / file-intelligence works in local desktop
# mode without a separately-run Python service.
#
# Build (from repo root, inside a venv with runtime deps + pyinstaller):
#     pyinstaller packaging/cortex-local.spec --clean --noconfirm
# Output: dist/cortex-local
#
# Data files:
#   schemas/  — cortex_runtime resolves its JSON schemas via
#               Path(__file__).resolve().parent.parent / "schemas/<name>"; for a
#               collected module that anchors to _MEIPASS, so the schema dir must
#               be bundled at the archive root ("schemas") for /health
#               (emit_service_status) and every emission validator to resolve.
#   jsonschema_specifications / referencing — vendored JSON meta-schemas the
#               Draft 2020-12 validator loads through importlib.resources.

import os
import sys

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# SPECPATH is the directory holding this spec (…/packaging); the repo root is its
# parent. Anchor every path to it so the build is invocation-directory agnostic.
repo_root = os.path.dirname(SPECPATH)

# The `pyinstaller` console-script does NOT put the build cwd on sys.path, so
# collect_submodules("cortex_runtime" / "service") below would import nothing and
# return [] — silently dropping any submodule reached only via
# importlib.import_module(<string>). That is exactly how
# cortex_runtime.scrivener_authority_recon (enumerated by
# service_status._implemented_runtime_slices) was being left out of the freeze,
# making the Scrivener Stage 1 slice report "unavailable" at runtime even though
# it is implemented. Put the repo root on the path so the packages are importable
# and their submodules are actually collected.
sys.path.insert(0, repo_root)

hiddenimports = []
hiddenimports += collect_submodules("uvicorn")
hiddenimports += collect_submodules("fastapi")
hiddenimports += collect_submodules("cortex_runtime")
hiddenimports += collect_submodules("service")
hiddenimports += collect_submodules("jsonschema")
hiddenimports += [
    "service.authorforge_app",
    "service.authorforge_translation",
]

datas = [
    (os.path.join(repo_root, "schemas"), "schemas"),
]
# Draft 2020-12 validation pulls vendored JSON resources from these packages.
datas += collect_data_files("jsonschema_specifications")
datas += collect_data_files("referencing")

a = Analysis(
    [os.path.join(SPECPATH, "freeze_entry.py")],
    pathex=[repo_root],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=["tests"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="cortex-local",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=True,
)
