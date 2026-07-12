from __future__ import annotations

import csv
import json
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .models import Pattern, Severity

FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "id": ("pattern_id", "id"),
    "gate": ("gate", "gate_id", "parent_cluster"),
    "title": ("title", "pattern_name", "gate_name", "claim_type", "abstract_risk_pattern"),
    "concern": (
        "concern",
        "reviewer_concern",
        "abstract_risk_pattern",
        "trigger",
        "why_it_matters",
        "claim_type",
    ),
    "risk": ("evidence_risk", "why_it_matters", "claim_language_risk"),
    "revision": ("revision_direction", "requested_actions", "evidence_expected"),
    "severity": (
        "severity",
        "default_severity",
        "severity_default",
        "severity_hint",
        "severity_rule",
    ),
    "triggers": ("triggers", "common_triggers", "trigger", "subfield_signals"),
}

SEVERITY_ORDER = {"critical", "major", "moderate", "minor", "editorial", "unknown"}


def _first(record: dict[str, Any], aliases: Iterable[str]) -> Any:
    for key in aliases:
        value = record.get(key)
        if value not in (None, "", [], ()):
            return value
    return ""


def _text(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(str(item).strip() for item in value if str(item).strip())
    return str(value or "").strip()


def normalize_severity(value: Any) -> Severity:
    text = _text(value).lower()
    if "critical" in text or "fatal" in text:
        return "critical"
    if "major" in text or "central" in text or "high" in text:
        return "major"
    if "moderate" in text or "medium" in text:
        return "moderate"
    if "minor" in text or "low" in text:
        return "minor"
    if "editor" in text:
        return "editorial"
    return "unknown"


def _split_triggers(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        items = [_text(item) for item in value]
    else:
        items = re.split(r"[;,|]", _text(value))
    cleaned = tuple(dict.fromkeys(item.strip() for item in items if item.strip()))
    return cleaned


def normalize_record(
    record: dict[str, Any], *, domain: str, source_path: Path | None = None
) -> Pattern:
    pattern_id = _text(_first(record, FIELD_ALIASES["id"]))
    if not pattern_id:
        raise ValueError("Pattern record has no pattern_id")
    gate = _text(_first(record, FIELD_ALIASES["gate"])) or "general_evidence_integrity"
    title = _text(_first(record, FIELD_ALIASES["title"])) or pattern_id
    concern = _text(_first(record, FIELD_ALIASES["concern"]))
    if not concern:
        raise ValueError(f"Pattern {pattern_id} has no reviewer concern")
    risk = _text(_first(record, FIELD_ALIASES["risk"]))
    revision = _text(_first(record, FIELD_ALIASES["revision"]))
    severity = normalize_severity(_first(record, FIELD_ALIASES["severity"]))
    triggers = _split_triggers(_first(record, FIELD_ALIASES["triggers"]))
    return Pattern(
        pattern_id=pattern_id,
        gate=gate,
        title=title,
        concern=concern,
        evidence_risk=risk,
        revision_direction=revision,
        severity=severity,
        triggers=triggers,
        domain=domain,
        source_path=source_path,
        raw=dict(record),
    )


def load_csv(path: Path, *, domain: str) -> list[Pattern]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return [normalize_record(dict(row), domain=domain, source_path=path) for row in rows]


def load_jsonl(path: Path, *, domain: str) -> list[Pattern]:
    patterns: list[Pattern] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"Expected JSON object at {path}:{line_number}")
            patterns.append(normalize_record(record, domain=domain, source_path=path))
    return patterns


def load_patterns(skill_root: Path) -> list[Pattern]:
    database = skill_root / "reviewer_db"
    domain = skill_root.name.removesuffix("-reviewer-skill")
    csv_path = database / "patterns.csv"
    jsonl_path = database / "patterns.jsonl"
    if csv_path.exists():
        return load_csv(csv_path, domain=domain)
    if jsonl_path.exists():
        return load_jsonl(jsonl_path, domain=domain)
    issue_path = database / "issue_patterns.jsonl"
    if issue_path.exists():
        return load_jsonl(issue_path, domain=domain)
    raise FileNotFoundError(f"No supported pattern database found under {database}")


def validate_patterns(patterns: list[Pattern]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for pattern in patterns:
        if pattern.pattern_id in seen:
            errors.append(f"duplicate pattern_id: {pattern.pattern_id}")
        seen.add(pattern.pattern_id)
        if len(pattern.concern) < 20:
            errors.append(f"{pattern.pattern_id}: concern is too short")
        if pattern.severity not in SEVERITY_ORDER:
            errors.append(f"{pattern.pattern_id}: invalid severity {pattern.severity}")
        if not pattern.revision_direction:
            errors.append(f"{pattern.pattern_id}: missing revision direction")
    return errors


def pattern_to_normalized_dict(pattern: Pattern) -> dict[str, Any]:
    return {
        "pattern_id": pattern.pattern_id,
        "domain": pattern.domain,
        "gate": pattern.gate,
        "title": pattern.title,
        "concern": pattern.concern,
        "evidence_risk": pattern.evidence_risk,
        "revision_direction": pattern.revision_direction,
        "severity": pattern.severity,
        "triggers": list(pattern.triggers),
        "source_fields": pattern.raw,
    }
