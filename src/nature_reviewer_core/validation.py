from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path

from .discovery import discover_skill_roots
from .patterns import load_patterns, validate_patterns

REQUIRED_FILES = ("SKILL.md", "README.md", "MANIFEST.json", "LICENSE")
REQUIRED_DIRS = ("reviewer_db", "references", "templates", "scripts", "tests")


@dataclass(slots=True)
class ValidationReport:
    root: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    pattern_count: int = 0

    @property
    def ok(self) -> bool:
        return not self.errors


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_skill(root: Path) -> ValidationReport:
    report = ValidationReport(root=root)
    for filename in REQUIRED_FILES:
        if not (root / filename).is_file():
            report.errors.append(f"missing required file: {filename}")
    for dirname in REQUIRED_DIRS:
        if not (root / dirname).is_dir():
            report.errors.append(f"missing required directory: {dirname}/")
    skill_text = (
        (root / "SKILL.md").read_text(encoding="utf-8") if (root / "SKILL.md").exists() else ""
    )
    for phrase in ("evidence", "review"):
        if phrase not in skill_text.casefold():
            report.warnings.append(f"SKILL.md does not mention {phrase!r}")
    try:
        patterns = load_patterns(root)
        report.pattern_count = len(patterns)
        report.errors.extend(validate_patterns(patterns))
    except (FileNotFoundError, ValueError) as exc:
        report.errors.append(str(exc))
    manifest_path = root / "MANIFEST.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            report.errors.append(f"invalid MANIFEST.json: {exc}")
        else:
            if manifest.get("schema_version") != 2:
                report.errors.append("MANIFEST.json schema_version must be 2")
            if manifest.get("license") != "MIT":
                report.errors.append("MANIFEST.json license must match root MIT license")
            expected = manifest.get("pattern_count")
            if isinstance(expected, int) and expected != report.pattern_count:
                report.errors.append(
                    f"manifest pattern_count={expected}, actual={report.pattern_count}"
                )
    checksum_path = root / "checksums.sha256"
    if checksum_path.exists():
        for line_number, line in enumerate(
            checksum_path.read_text(encoding="utf-8").splitlines(), 1
        ):
            if not line.strip():
                continue
            try:
                expected_hash, relative_name = line.split("  ", 1)
            except ValueError:
                report.errors.append(f"invalid checksum line {line_number}")
                continue
            relative = Path(relative_name)
            if relative.is_absolute() or ".." in relative.parts:
                report.errors.append(f"unsafe checksum path at line {line_number}")
                continue
            target = root / relative
            if not target.is_file():
                report.errors.append(f"checksum target missing: {relative_name}")
            elif sha256(target) != expected_hash:
                report.errors.append(f"checksum mismatch: {relative_name}")
    else:
        report.warnings.append("checksums.sha256 is missing")
    forbidden = list(root.rglob("*.pdf"))
    if forbidden:
        report.errors.append("raw PDF files must not be distributed in skill packages")
    return report


def validate_repository(root: Path) -> list[ValidationReport]:
    skills = discover_skill_roots(root)
    if len(skills) != 7:
        missing = ValidationReport(root=root)
        missing.errors.append(f"expected 7 skills, discovered {len(skills)}")
        return [missing, *(validate_skill(skill) for skill in skills)]
    return [validate_skill(skill) for skill in skills]
