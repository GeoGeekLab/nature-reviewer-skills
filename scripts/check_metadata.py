from __future__ import annotations

import json
from pathlib import Path

import _bootstrap  # noqa: F401

from nature_reviewer_core.discovery import discover_skill_roots

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    errors = []
    for skill in discover_skill_roots(ROOT):
        manifest = json.loads((skill / "MANIFEST.json").read_text(encoding="utf-8"))
        if manifest["name"] != skill.name:
            errors.append(f"{skill}: manifest name mismatch")
        if manifest["license"] != "MIT":
            errors.append(f"{skill}: inconsistent license")
    print("metadata consistent" if not errors else "\n".join(errors))
    raise SystemExit(bool(errors))
