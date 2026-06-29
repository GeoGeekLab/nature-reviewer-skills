from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    with (root / 'reviewer_db/patterns.csv').open(newline='', encoding='utf-8') as f:
        patterns = list(csv.DictReader(f))
    with (root / '_internal/review_unit_index.csv').open(newline='', encoding='utf-8') as f:
        units = list(csv.DictReader(f))
    summary = {
        'skill_name': 'nature-hydrology-reviewer',
        'pattern_count': len(patterns),
        'review_unit_index_count': len(units),
        'pattern_gates': dict(Counter(p['gate'] for p in patterns)),
        'unit_gates': dict(Counter(u['gate_primary'] for u in units)),
    }
    (root / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print('summary.json written')


if __name__ == '__main__':
    main()
