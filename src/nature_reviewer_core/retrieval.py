from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter
from collections.abc import Iterable
from typing import Literal

from .models import Pattern, SearchResult

TOKEN_RE = re.compile(r"[\w\-]+", re.UNICODE)
SYNONYMS: dict[str, tuple[str, ...]] = {
    "causal": ("causality", "attribution", "mechanism"),
    "mechanism": ("mechanistic", "causal", "pathway"),
    "validation": ("benchmark", "independent", "generalization"),
    "uncertainty": ("confidence", "error", "sensitivity", "robustness"),
    "novelty": ("advance", "prior", "comparison"),
    "leakage": ("cross-validation", "independence", "split"),
    "trend": ("time-series", "autocorrelation", "temporal"),
    "reproducibility": ("code", "data", "availability", "protocol"),
}
FIELD_WEIGHTS = {
    "title": 3.0,
    "gate": 2.2,
    "triggers": 2.0,
    "concern": 1.8,
    "evidence_risk": 1.5,
    "revision_direction": 1.2,
}


def tokenize(text: str) -> list[str]:
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return [
        token.strip("_-") for token in TOKEN_RE.findall(normalized) if len(token.strip("_-")) > 1
    ]


def expand_query(tokens: Iterable[str]) -> list[str]:
    expanded: list[str] = []
    for token in tokens:
        expanded.append(token)
        expanded.extend(SYNONYMS.get(token, ()))
    return list(dict.fromkeys(expanded))


def _field_tokens(pattern: Pattern) -> dict[str, list[str]]:
    return {
        "title": tokenize(pattern.title),
        "gate": tokenize(pattern.gate.replace("_", " ")),
        "triggers": tokenize(" ".join(pattern.triggers)),
        "concern": tokenize(pattern.concern),
        "evidence_risk": tokenize(pattern.evidence_risk),
        "revision_direction": tokenize(pattern.revision_direction),
    }


def _jaccard(left: Pattern, right: Pattern) -> float:
    a = set(tokenize(left.searchable_text()))
    b = set(tokenize(right.searchable_text()))
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def search_patterns(
    patterns: list[Pattern],
    query: str,
    *,
    limit: int = 10,
    diversify: bool = True,
    diversity_lambda: float = 0.78,
) -> list[SearchResult]:
    if limit < 1:
        raise ValueError("limit must be positive")
    original_tokens = tokenize(query)
    if not original_tokens:
        return []
    query_tokens = expand_query(original_tokens)
    field_documents = [_field_tokens(pattern) for pattern in patterns]
    document_frequencies: Counter[str] = Counter()
    for fields in field_documents:
        unique = set(token for values in fields.values() for token in values)
        document_frequencies.update(unique)
    count = max(len(patterns), 1)
    scored: list[SearchResult] = []
    query_phrase = " ".join(original_tokens)
    for pattern, fields in zip(patterns, field_documents, strict=True):
        score = 0.0
        matched: set[str] = set()
        for field_name, tokens in fields.items():
            frequencies = Counter(tokens)
            field_length = max(len(tokens), 1)
            average_length = max(sum(len(doc[field_name]) for doc in field_documents) / count, 1.0)
            weight = FIELD_WEIGHTS[field_name]
            for term in query_tokens:
                tf = frequencies[term]
                if not tf:
                    continue
                matched.add(term)
                df = document_frequencies[term]
                idf = math.log(1.0 + (count - df + 0.5) / (df + 0.5))
                k1, b = 1.5, 0.75
                denominator = tf + k1 * (1.0 - b + b * field_length / average_length)
                score += weight * idf * (tf * (k1 + 1.0) / denominator)
        haystack = " ".join(tokenize(pattern.searchable_text()))
        if len(original_tokens) > 1 and query_phrase in haystack:
            score += 5.0
        exact_original = sum(1 for token in original_tokens if token in matched)
        score += exact_original * 0.75
        if score > 0:
            confidence: Literal["high", "medium", "low"] = (
                "high" if exact_original >= 2 and score >= 5 else "medium" if score >= 2 else "low"
            )
            scored.append(
                SearchResult(
                    pattern=pattern,
                    score=round(score, 6),
                    confidence=confidence,
                    matched_terms=tuple(sorted(matched)),
                )
            )
    scored.sort(key=lambda result: (-result.score, result.pattern.pattern_id))
    if not diversify or len(scored) <= limit:
        return scored[:limit]
    selected: list[SearchResult] = []
    remaining = scored[:]
    max_score = remaining[0].score or 1.0
    while remaining and len(selected) < limit:
        best_index = 0
        best_value = float("-inf")
        for index, candidate in enumerate(remaining):
            relevance = candidate.score / max_score
            redundancy = max(
                (_jaccard(candidate.pattern, item.pattern) for item in selected), default=0.0
            )
            value = diversity_lambda * relevance - (1.0 - diversity_lambda) * redundancy
            if value > best_value:
                best_value = value
                best_index = index
        selected.append(remaining.pop(best_index))
    return selected


def duplicate_pairs(
    patterns: Iterable[Pattern], threshold: float = 0.82
) -> list[tuple[str, str, float]]:
    items = list(patterns)
    pairs: list[tuple[str, str, float]] = []
    for index, left in enumerate(items):
        for right in items[index + 1 :]:
            similarity = _jaccard(left, right)
            if similarity >= threshold:
                pairs.append((left.pattern_id, right.pattern_id, round(similarity, 4)))
    return pairs
