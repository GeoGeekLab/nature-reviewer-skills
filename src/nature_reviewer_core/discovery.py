from __future__ import annotations

import json
from pathlib import Path

EXCLUDED_PARTS = {".git", ".venv", "build", "dist", "__pycache__"}
VALID_PACKAGE_TYPES = {"domain_skill", "orchestrator"}


def _manifest_package_type(candidate: Path) -> str:
    """Return package type from MANIFEST.json with a legacy path fallback."""
    manifest_path = candidate / "MANIFEST.json"
    if manifest_path.is_file():
        try:
            value = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            value = None
        if isinstance(value, dict):
            package_type = value.get("package_type")
            if package_type in VALID_PACKAGE_TYPES:
                return str(package_type)
    # Backward compatibility for pre-manifest or legacy layouts.
    return "orchestrator" if "orchestrators" in candidate.parts else "domain_skill"


def _discover(root: Path, *, package_type: str) -> list[Path]:
    roots: list[Path] = []
    for skill_file in root.rglob("SKILL.md"):
        if any(part in EXCLUDED_PARTS for part in skill_file.parts):
            continue
        candidate = skill_file.parent
        if not (candidate / "reviewer_db").is_dir():
            continue
        if _manifest_package_type(candidate) == package_type:
            roots.append(candidate)
    return sorted(set(roots), key=lambda path: path.as_posix())


def discover_skill_roots(root: Path) -> list[Path]:
    """Return the seven foundational domain skill directories."""
    return _discover(root, package_type="domain_skill")


def discover_orchestrator_roots(root: Path) -> list[Path]:
    """Return upper-layer review orchestrators without counting them as domain skills."""
    return _discover(root, package_type="orchestrator")


def discover_review_package_roots(root: Path) -> list[Path]:
    return [*discover_skill_roots(root), *discover_orchestrator_roots(root)]


def repository_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").exists() and (
            candidate / "src" / "nature_reviewer_core"
        ).is_dir():
            return candidate
    raise FileNotFoundError(
        "Could not locate repository root containing pyproject.toml and src/nature_reviewer_core"
    )
