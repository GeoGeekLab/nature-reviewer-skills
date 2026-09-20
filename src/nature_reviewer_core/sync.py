from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from .discovery import discover_orchestrator_roots, discover_skill_roots
from .patterns import load_patterns, pattern_to_normalized_dict
from .validation import sha256


def _json_dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sync_skill(skill_root: Path) -> dict[str, object]:
    patterns = load_patterns(skill_root)
    database = skill_root / "reviewer_db"
    normalized_path = database / "patterns.jsonl"
    normalized_path.write_text(
        "".join(
            json.dumps(pattern_to_normalized_dict(item), ensure_ascii=False, sort_keys=True) + "\n"
            for item in patterns
        ),
        encoding="utf-8",
    )
    gates = Counter(item.gate for item in patterns)
    severities = Counter(item.severity for item in patterns)
    summary = {
        "schema_version": 2,
        "generated_from": "patterns.csv"
        if (database / "patterns.csv").exists()
        else "issue_patterns.jsonl",
        "pattern_count": len(patterns),
        "gate_count": len(gates),
        "patterns_by_gate": dict(sorted(gates.items())),
        "patterns_by_severity": dict(sorted(severities.items())),
        "normalized_sha256": sha256(normalized_path),
    }
    _json_dump(database / "summary.json", summary)
    existing_manifest: dict[str, object] = {}
    manifest_path = skill_root / "MANIFEST.json"
    if manifest_path.exists():
        loaded = json.loads(manifest_path.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            existing_manifest = loaded
    package_type = existing_manifest.get("package_type")
    if package_type not in {"domain_skill", "orchestrator"}:
        package_type = "orchestrator" if "orchestrators" in skill_root.parts else "domain_skill"
    manifest = {
        **existing_manifest,
        "schema_version": 2,
        "name": skill_root.name,
        "version": "2.2.0",
        "license": "MIT",
        "package_type": package_type,
        "skill_entrypoint": "SKILL.md",
        "pattern_count": len(patterns),
        "shared_runtime": "nature-reviewer-core>=2.2.0,<3",
        "generated": True,
        "evidence_boundary": "research-assistance only; expert validation required",
    }
    _json_dump(skill_root / "MANIFEST.json", manifest)
    transient_parts = {".git", ".pytest_cache", "__pycache__", ".mypy_cache", ".ruff_cache"}
    checksum_targets = [
        path
        for path in skill_root.rglob("*")
        if path.is_file()
        and path.name != "checksums.sha256"
        and not any(part in transient_parts for part in path.parts)
        and path.suffix not in {".pyc", ".pyo"}
    ]
    checksum_text = "".join(
        f"{sha256(path)}  {path.relative_to(skill_root).as_posix()}\n"
        for path in sorted(checksum_targets)
    )
    (skill_root / "checksums.sha256").write_text(checksum_text, encoding="utf-8")
    return {"skill": skill_root.name, **summary}


def sync_repository(root: Path) -> list[dict[str, object]]:
    packages = [*discover_skill_roots(root), *discover_orchestrator_roots(root)]
    return [sync_skill(package) for package in packages]
