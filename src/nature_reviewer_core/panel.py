from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from .models import Concern


@dataclass(frozen=True, slots=True)
class ReviewerPerspective:
    reviewer_id: str
    primary_focus: tuple[str, ...]
    prohibited_primary_focus: tuple[str, ...]
    question: str


DEFAULT_PANEL = (
    ReviewerPerspective(
        "referee-1",
        ("claim-evidence", "novelty", "causal scope", "conceptual advance"),
        ("copyediting",),
        "Does the central claim follow from the strongest directly demonstrated evidence?",
    ),
    ReviewerPerspective(
        "referee-2",
        ("methods", "controls", "statistics", "validation", "uncertainty"),
        ("editorial fit",),
        "Could the result survive an independent replication and adversarial sensitivity analysis?",
    ),
    ReviewerPerspective(
        "referee-3",
        ("generality", "reproducibility", "figures", "alternative explanations"),
        ("language polish",),
        "Where does the evidence chain break when transferred beyond the sampled system?",
    ),
)


def assign_perspectives(count: int = 3) -> tuple[ReviewerPerspective, ...]:
    if count < 1 or count > len(DEFAULT_PANEL):
        raise ValueError(f"count must be between 1 and {len(DEFAULT_PANEL)}")
    return DEFAULT_PANEL[:count]


def _fingerprint(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9\-]+", text.casefold()))


def concern_overlap(concerns: list[Concern], threshold: float = 0.72) -> dict[str, object]:
    duplicate_pairs: list[tuple[str, str, float]] = []
    reviewer_counts: Counter[str] = Counter(concern.reviewer_id for concern in concerns)
    for index, left in enumerate(concerns):
        left_tokens = _fingerprint(left.text)
        for right in concerns[index + 1 :]:
            if left.reviewer_id and left.reviewer_id == right.reviewer_id:
                continue
            right_tokens = _fingerprint(right.text)
            similarity = len(left_tokens & right_tokens) / max(len(left_tokens | right_tokens), 1)
            if similarity >= threshold:
                duplicate_pairs.append((left.issue_id, right.issue_id, round(similarity, 4)))
    denominator = max(len(concerns), 1)
    return {
        "reviewer_concern_counts": dict(sorted(reviewer_counts.items())),
        "duplicate_pairs": duplicate_pairs,
        "duplicate_rate": round(len(duplicate_pairs) / denominator, 4),
    }
