from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

REQUIRED_ROOT_FILES = [
    "README.md",
    "SKILL.md",
    "MANIFEST.json",
    "LICENSE",
    "LICENSE-MIT",
    "LICENSE-APACHE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "pyproject.toml",
    "requirements-dev.txt",
]

REQUIRED_DIRS = [
    "references",
    "reviewer_db",
    "templates",
    "scripts",
    "tests",
    "docs",
    "examples",
    "_internal",
    ".github/workflows",
]

REQUIRED_REFERENCE_FILES = [
    "references/referee_voice_style_gate.md",
    "references/gate_router.md",
    "references/claim_evidence_calibration_gate.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def validate_front_matter(skill_path: Path) -> None:
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML front matter")
    end = text.find("\n---", 4)
    if end == -1:
        fail("SKILL.md front matter is not closed")
    header = text[4:end]
    for key in ["name:", "description:", "version:", "domain:", "license:"]:
        if key not in header:
            fail(f"SKILL.md front matter missing {key}")


def validate_patterns(path: Path) -> None:
    if not path.exists():
        fail("reviewer_db/patterns.csv is missing")
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) < 20:
        fail("patterns.csv should contain at least 20 abstract patterns")
    for row in rows:
        if row.get("verbatim_source_text_included") != "false":
            fail("patterns.csv must not include verbatim source text")


def validate_manifest(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("license") != "MIT OR Apache-2.0":
        fail("MANIFEST.json must declare MIT OR Apache-2.0")
    if data.get("entrypoint") != "SKILL.md":
        fail("MANIFEST.json entrypoint must be SKILL.md")


def validate_package(root: Path) -> None:
    for name in REQUIRED_ROOT_FILES:
        if not (root / name).is_file():
            fail(f"missing required root file: {name}")
    for name in REQUIRED_DIRS:
        if not (root / name).is_dir():
            fail(f"missing required directory: {name}")
    for name in REQUIRED_REFERENCE_FILES:
        if not (root / name).is_file():
            fail(f"missing required reference file: {name}")
    validate_front_matter(root / "SKILL.md")
    validate_manifest(root / "MANIFEST.json")
    validate_patterns(root / "reviewer_db" / "patterns.csv")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate reviewer skill package structure.")
    parser.add_argument("root", type=Path, help="Repository root to validate")
    args = parser.parse_args()
    validate_package(args.root.resolve())
    print("Package validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
