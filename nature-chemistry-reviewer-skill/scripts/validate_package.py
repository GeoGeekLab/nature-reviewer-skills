#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

REQUIRED_FILES = [
    'README.md', 'SKILL.md', 'MANIFEST.json', 'LICENSE', 'LICENSE-MIT', 'LICENSE-APACHE',
    'CHANGELOG.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'SECURITY.md', 'pyproject.toml',
    'requirements-dev.txt', '.gitignore', '.editorconfig', '.github/workflows/ci.yml',
    '.github/PULL_REQUEST_TEMPLATE.md', 'references/referee_voice_style_gate.md',
    'reviewer_db/patterns.csv', 'reviewer_db/patterns.jsonl', '_internal/review_unit_index.csv',
    'docs/distillation_report.md', 'docs/distillation_qc.csv', 'examples/example_review_report.md',
    'scripts/render_review_docx.py',
    'scripts/extract_text_with_anchors.py',
    'scripts/published_paper_query_builder.py',
    'scripts/reviewer_db.py',
    'scripts/sample_referee_style.py', 'summary.json'
]
REQUIRED_DIRS = ['references', 'reviewer_db', 'templates', 'scripts', 'tests', 'docs', 'examples', '_internal']
FORBIDDEN_EXTENSIONS = {'.pdf'}
FORBIDDEN_NAMES = {'corpus.zip'}


def fail(message: str) -> None:
    raise SystemExit(f'validation failed: {message}')


def check_required(root: Path) -> None:
    for rel in REQUIRED_DIRS:
        if not (root / rel).is_dir():
            fail(f'missing directory: {rel}')
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            fail(f'missing file: {rel}')


def check_no_raw_pdfs(root: Path) -> None:
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            fail(f'raw PDF should not be included: {path.relative_to(root)}')
        if path.name.lower() in FORBIDDEN_NAMES:
            fail(f'raw corpus archive should not be included: {path.relative_to(root)}')


def check_skill_front_matter(root: Path) -> None:
    text = (root / 'SKILL.md').read_text(encoding='utf-8')
    if not text.startswith('---'):
        fail('SKILL.md must start with YAML front matter')
    for key in ['name:', 'description:', 'version:', 'license:']:
        if key not in text.split('---', 2)[1]:
            fail(f'SKILL.md front matter missing {key}')


def check_patterns(root: Path) -> None:
    csv_path = root / 'reviewer_db/patterns.csv'
    with csv_path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    if len(rows) < 20:
        fail('patterns.csv must contain at least 20 abstract patterns')
    required = {'pattern_id', 'gate', 'pattern_name', 'claim_type', 'evidence_risk', 'reviewer_concern', 'revision_direction'}
    if not required.issubset(rows[0].keys()):
        fail('patterns.csv missing required columns')
    if any(row.get('verbatim_text_included') == 'yes' for row in rows):
        fail('patterns.csv must not include verbatim reviewer text')

    jsonl_path = root / 'reviewer_db/patterns.jsonl'
    count = 0
    with jsonl_path.open(encoding='utf-8') as f:
        for line in f:
            if line.strip():
                json.loads(line)
                count += 1
    if count != len(rows):
        fail('patterns.jsonl count does not match patterns.csv')


def check_example(root: Path) -> None:
    text = (root / 'examples/example_review_report.md').read_text(encoding='utf-8')
    required_phrases = ['Reviewer Reports on the Initial Version', 'Referees\' comments:', 'Referee #1', 'Referee #2', 'Referee #3']
    for phrase in required_phrases:
        if phrase not in text:
            fail(f'example report missing phrase: {phrase}')


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate reviewer skill package structure.')
    parser.add_argument('root', nargs='?', default='.', help='package root')
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        fail(f'not a directory: {root}')
    check_required(root)
    check_no_raw_pdfs(root)
    check_skill_front_matter(root)
    check_patterns(root)
    check_example(root)
    print('validation passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
