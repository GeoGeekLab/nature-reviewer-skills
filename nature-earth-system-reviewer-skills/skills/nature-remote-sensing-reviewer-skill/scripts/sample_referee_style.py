#!/usr/bin/env python3
"""Sample phrase-level Nature referee style motifs from the local reviewer DB.

This script does not require raw PDFs and does not reproduce long review passages. It reports
short motif hits from review_units.jsonl for package maintenance and style inspection.
"""
import argparse, json, re
from pathlib import Path

MOTIFS = [
    r"my foremost concern", r"my main concern", r"I am not convinced",
    r"I suggest", r"I find", r"I do not agree", r"Page \d+", r"lines? \d+",
    r"Figure \d+", r"Table S?\d+", r"the manuscript addresses"
]

def load_units(db: Path):
    p = db / "review_units.jsonl"
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="reviewer_db")
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()
    db = Path(args.db)
    hits = []
    for row in load_units(db):
        txt = row.get("text", "")
        for motif in MOTIFS:
            if re.search(motif, txt, re.I):
                snippet = re.sub(r"\s+", " ", txt).strip()[:220]
                hits.append({"motif": motif, "unit_id": row.get("unit_id"), "source_id": row.get("source_id"), "snippet": snippet})
                break
        if len(hits) >= args.limit:
            break
    for h in hits:
        print(json.dumps(h, ensure_ascii=False))
    if not hits:
        print("No motif hits found in review_units.jsonl.")

if __name__ == "__main__":
    main()
