from __future__ import annotations

from pathlib import Path

EXCLUDED_PARTS = {".git", ".venv", "build", "dist", "__pycache__"}


def discover_skill_roots(root: Path) -> list[Path]:
    """Return directories containing a top-level SKILL.md and reviewer database."""
    roots: list[Path] = []
    for skill_file in root.rglob("SKILL.md"):
        if any(part in EXCLUDED_PARTS for part in skill_file.parts):
            continue
        candidate = skill_file.parent
        if (candidate / "reviewer_db").is_dir():
            roots.append(candidate)
    return sorted(set(roots), key=lambda path: path.as_posix())


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
