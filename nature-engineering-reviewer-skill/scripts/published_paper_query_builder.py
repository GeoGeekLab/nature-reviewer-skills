#!/usr/bin/env python3
"""Build conservative scholarly-search queries from local manuscript text.

The script does not perform web search. It extracts title-like phrases, domain
terms, and method terms so a reviewer agent can run allowed literature retrieval
with precise, auditable queries.
"""

from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path

STOP_WORDS = {
    "about", "across", "after", "also", "analysis", "and", "are", "based",
    "between", "data", "during", "figure", "from", "has", "have", "into",
    "its", "manuscript", "material", "method", "methods", "model", "models",
    "our", "over", "paper", "results", "section", "study", "table", "that",
    "the", "their", "this", "under", "using", "were", "with", "within",
}

METHOD_PATTERNS = (
    r"\bmachine learning\b",
    r"\bdeep learning\b",
    r"\brandom forest\b",
    r"\bBayesian\b",
    r"\bcausal inference\b",
    r"\bfield experiment\b",
    r"\bcontrolled experiment\b",
    r"\breanalysis\b",
    r"\bsatellite\b",
    r"\bremote sensing\b",
    r"\bfirst-principles\b",
    r"\bdensity functional theory\b",
    r"\bDFT\b",
    r"\bcatalysis\b",
    r"\belectrochemical\b",
)


def read_text(paths: list[str]) -> str:
    """Read UTF-8-compatible local text inputs."""
    chunks: list[str] = []
    for item in paths:
        path = Path(item)
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(chunks)


def title_candidates(text: str) -> list[str]:
    """Return title-like lines from the top of the manuscript text."""
    candidates: list[str] = []
    for line in text.splitlines()[:80]:
        cleaned = line.strip("# \t")
        word_count = len(cleaned.split())
        if 5 <= word_count <= 22 and not cleaned.endswith("."):
            candidates.append(cleaned)
    return candidates[:3]


def method_terms(text: str) -> list[str]:
    """Return method terms matched by conservative phrase patterns."""
    found: list[str] = []
    for pattern in METHOD_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            term = match.group(0)
            if term.lower() not in {item.lower() for item in found}:
                found.append(term)
    return found[:8]


def top_terms(text: str, limit: int = 20) -> list[str]:
    """Return frequent content terms from manuscript text."""
    words = [word.lower() for word in re.findall(r"[A-Za-z][A-Za-z0-9-]{2,}", text)]
    words = [word for word in words if word not in STOP_WORDS and not word.isdigit()]
    counts = collections.Counter(words)
    return [word for word, _ in counts.most_common(limit)]


def build_queries(text: str, limit: int) -> list[str]:
    """Build deduplicated scholarly-search queries."""
    titles = title_candidates(text)
    methods = method_terms(text)
    terms = top_terms(text)
    queries: list[str] = []
    if titles:
        queries.append(f'"{titles[0]}"')
    if titles and methods:
        queries.append(f'"{titles[0]}" {" ".join(methods[:2])}')
    if methods and terms:
        queries.append(f'{" ".join(terms[:6])} {" ".join(methods[:2])}')
    if terms:
        queries.append(f'{" ".join(terms[:8])} Nature Communications related work')
    if methods:
        queries.append(f'{" ".join(methods[:3])} validation uncertainty benchmark')

    deduplicated: list[str] = []
    seen: set[str] = set()
    for query in queries:
        normalized = " ".join(query.split())
        if normalized.lower() not in seen:
            seen.add(normalized.lower())
            deduplicated.append(normalized)
    return deduplicated[:limit]


def main() -> int:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(description="Build literature-search queries from local text.")
    parser.add_argument("--input", nargs="+", required=True, help="Markdown or text files")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    text = read_text(args.input)
    if not text.strip():
        print("No readable input text found.")
        return 1
    for index, query in enumerate(build_queries(text, args.limit), start=1):
        print(f"{index}. {query}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
