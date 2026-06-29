from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_valid() -> None:
    data = json.loads((ROOT / 'MANIFEST.json').read_text(encoding='utf-8'))
    assert data['skill_name'] == 'nature-hydrology-reviewer'
    assert data['license'] == 'MIT OR Apache-2.0'
    assert data['pattern_count'] >= 100


def test_patterns_are_abstract() -> None:
    with (ROOT / 'reviewer_db/patterns.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) >= 100
    joined = ' '.join(r['reviewer_concern'] for r in rows)
    assert 'Reviewer #' not in joined
    assert 'Corresponding Author' not in joined


def test_review_unit_index_is_non_verbatim() -> None:
    with (ROOT / '_internal/review_unit_index.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert rows
    assert all(str(r['raw_text_stored']).lower() == 'false' for r in rows)
    assert 'unit_text' not in rows[0]


def test_required_reference_gate_exists() -> None:
    assert (ROOT / 'references/referee_voice_style_gate.md').is_file()


def test_example_review_has_nature_referee_structure() -> None:
    text = (ROOT / 'examples/example_review_report.md').read_text(encoding='utf-8')
    assert 'Reviewer Reports on the Initial Version' in text
    assert text.count('Referee #') == 3
    assert text.count('Overall judgment:') == 3


def test_classic_stress_tests_are_non_weighted() -> None:
    data = json.loads((ROOT / 'MANIFEST.json').read_text(encoding='utf-8'))
    assert data['classic_stress_tests_weighted'] is False
    assert (ROOT / 'references/classic_hydrology_stress_test_gate.md').is_file()
    with (ROOT / 'reviewer_db/patterns.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    classic_rows = [r for r in rows if r['pattern_id'].startswith('HYDRO-PAT-1') and 'cross-literature' in r['abstraction_level']]
    assert classic_rows
    assert all(r['supporting_unit_count_by_gate'] == '0' for r in classic_rows)


def test_close_reading_controls_present() -> None:
    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    assert 'figure panels, tables and methods' in skill or 'figures, tables and methods' in skill
    assert 'short exact manuscript phrase' in skill
    assert 'Specific comments' in (ROOT / 'templates/nature_review_report_template.md').read_text(encoding='utf-8')


def test_pattern_files_are_synchronized() -> None:
    csv_rows = list(csv.DictReader((ROOT / 'reviewer_db/patterns.csv').open(newline='', encoding='utf-8')))
    jsonl_rows = [json.loads(line) for line in (ROOT / 'reviewer_db/patterns.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    assert len(csv_rows) == len(jsonl_rows)
    assert csv_rows[-1]['pattern_id'] == jsonl_rows[-1]['pattern_id']
    zero_weight = [r for r in csv_rows if r['abstraction_level'] == 'non-verbatim output-control pattern']
    assert zero_weight
    assert all(r['supporting_unit_count_by_gate'] == '0' for r in zero_weight)
