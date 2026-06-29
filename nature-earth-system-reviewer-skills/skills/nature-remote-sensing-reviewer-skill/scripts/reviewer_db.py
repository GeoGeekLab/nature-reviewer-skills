import argparse
import json
import re
from pathlib import Path


SEARCH_FILES = [
    "review_units.jsonl",
    "issue_patterns.jsonl",
    "contribution_patterns.jsonl",
    "style_moves.jsonl",
    "style_motifs.jsonl",
    "trend_issue_patterns.jsonl",
    "inference_integrity_patterns.jsonl",
    "referee_voice_profiles.jsonl",
    "method_reference_patterns.jsonl", "anchor_comment_patterns.jsonl",
]


WEIGHTED_KEYS = {
    "pattern_name": 4,
    "dimension": 4,
    "issue_axis": 4,
    "requested_action": 4,
    "requested_actions": 4,
    "move_name": 4,
    "cluster": 3,
    "claim_target": 3,
    "trigger": 3,
    "why_it_matters": 2,
    "severity_rule": 2,
    "text": 1,
    "reviewer_language_patterns": 1,
    "language_patterns": 1,
    "review_language": 1,
    "gate": 2,
    "pattern_id": 2,
    "profile_id": 3,
    "method_family": 4,
    "suggested_reference": 3,
    "use_when": 3,
    "safe_phrase": 2,
    "name": 4,
    "style": 3,
    "best_for": 3,
}


def tokens(text):
    return re.findall(r"[a-z0-9_+-]+", text.lower())


def flatten(value):
    if isinstance(value, dict):
        return " ".join(flatten(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(flatten(v) for v in value)
    return str(value)


def iter_records(db):
    for name in SEARCH_FILES:
        path = db / name
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                record["_source_file"] = name
                record["_line"] = line_no
                yield record


def score_record(record, query_terms):
    score = 0
    for key, value in record.items():
        if key.startswith("_"):
            continue
        text = flatten(value).lower()
        if not text:
            continue
        weight = WEIGHTED_KEYS.get(key, 1)
        for term in query_terms:
            if term in text:
                score += weight * (1 + text.count(term) // 3)
    return score


def label(record):
    for key in ("pattern_name", "dimension", "move_name", "unit_id"):
        if key in record:
            return str(record[key])
    return f"{record.get('_source_file', 'record')}:{record.get('_line', '?')}"


def snippet(record):
    for key in ("text", "trigger", "purpose", "review_language", "reviewer_language_patterns", "language_patterns"):
        value = record.get(key)
        if value:
            text = flatten(value)
            return text[:260] + ("..." if len(text) > 260 else "")
    return flatten(record)[:260]


def search(args):
    db = Path(args.db)
    query_terms = tokens(args.query)
    if not query_terms:
        print("No query terms supplied.")
        return 0
    results = []
    for record in iter_records(db):
        score = score_record(record, query_terms)
        if score > 0:
            results.append((score, record))
    results.sort(key=lambda item: (-item[0], item[1].get("_source_file", ""), item[1].get("_line", 0)))
    if not results:
        print("No results found.")
        return 0
    for rank, (score, record) in enumerate(results[: args.limit], 1):
        print(f"{rank}. [{record['_source_file']}] {label(record)} (score={score})")
        print(f"   {snippet(record)}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Search the local reviewer behavior memory.")
    sub = parser.add_subparsers(dest="command", required=True)
    search_parser = sub.add_parser("search", help="Search reviewer memory.")
    search_parser.add_argument("query")
    search_parser.add_argument("--db", default="reviewer_db")
    search_parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    if args.command == "search":
        raise SystemExit(search(args))


if __name__ == "__main__":
    main()
