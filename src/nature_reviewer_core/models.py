from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

Severity = Literal["critical", "major", "moderate", "minor", "editorial", "unknown"]
BenchmarkCaseType = Literal["positive", "negative_control"]


@dataclass(frozen=True, slots=True)
class Pattern:
    pattern_id: str
    gate: str
    title: str
    concern: str
    evidence_risk: str
    revision_direction: str
    severity: Severity
    triggers: tuple[str, ...] = ()
    domain: str = "unknown"
    source_path: Path | None = None
    raw: dict[str, Any] = field(default_factory=dict, compare=False, hash=False)

    def searchable_text(self) -> str:
        return " ".join(
            part
            for part in (
                self.gate,
                self.title,
                self.concern,
                self.evidence_risk,
                self.revision_direction,
                " ".join(self.triggers),
            )
            if part
        )


@dataclass(frozen=True, slots=True)
class SearchResult:
    pattern: Pattern
    score: float
    confidence: Literal["high", "medium", "low"]
    matched_terms: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class Concern:
    issue_id: str
    severity: Severity
    text: str
    anchors: tuple[str, ...] = ()
    reviewer_id: str = ""


@dataclass(frozen=True, slots=True)
class BenchmarkCase:
    case_id: str
    domain: str
    manuscript_text: str
    gold_concerns: tuple[Concern, ...]
    case_type: BenchmarkCaseType = "positive"
    pair_id: str = ""
    challenge: str = ""
    target_issue_id: str = ""
    suite: str = ""
