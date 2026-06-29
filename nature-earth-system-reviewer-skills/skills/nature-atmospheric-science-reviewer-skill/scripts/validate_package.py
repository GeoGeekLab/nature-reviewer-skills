from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = [
    'README.md',
    'SKILL.md',
    'MANIFEST.json',
    'LICENSE',
    'LICENSE-MIT',
    'LICENSE-APACHE',
    'CHANGELOG.md',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'SECURITY.md',
    'pyproject.toml',
    'requirements-dev.txt',
    '.gitignore',
    '.editorconfig',
    '.github/workflows/ci.yml',
    'references/referee_voice_style_gate.md',
    'references/claim_dependent_gate_router.md',
    'references/atmospheric_science_gates.md',
    'references/gate_index.md',
    'references/claim_evidence_calibration_gate.md',
    'references/observational_product_reanalysis_gate.md',
    'references/sampling_event_representativeness_gate.md',
    'references/scale_resolution_boundary_gate.md',
    'references/model_physics_sensitivity_gate.md',
    'references/ai_weather_climate_model_gate.md',
    'references/aerosol_cloud_radiation_gate.md',
    'references/chemistry_emissions_budget_gate.md',
    'references/extreme_event_attribution_gate.md',
    'references/trend_signal_detection_gate.md',
    'references/circulation_mechanism_causality_gate.md',
    'references/statistical_uncertainty_gate.md',
    'references/reproducibility_data_code_gate.md',
    'references/novelty_related_work_positioning_gate.md',
    'references/detail_audit_gate.md',
    'reviewer_db/patterns.csv',
    'reviewer_db/patterns.jsonl',
    'reviewer_db/gate_counts.csv',
    'templates/review_report_template.md',
    'scripts/render_review_docx.py',
    'scripts/extract_text_with_anchors.py',
    'scripts/published_paper_query_builder.py',
    'scripts/reviewer_db.py',
    'scripts/sample_referee_style.py',
    'tests/test_package.py',
    'docs/distillation_report.md',
    'docs/distillation_qc.csv',
    'docs/distillation_sufficiency.md',
    'examples/example_review_report.md',
    '_internal/review_unit_index.csv',
    'corpus/README.md',
    'corpus/index.csv',
    'corpus/failures_excluded.csv',
    'corpus/keyword_expansion.csv',
    'corpus/qa_report.csv',
    'corpus/checksums.sha256',
    'corpus/summary.json',
]


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED:
        path = root / rel
        if not path.exists():
            errors.append(f'missing required file: {rel}')
        elif path.is_file() and path.stat().st_size == 0:
            errors.append(f'empty required file: {rel}')

    manifest_path = root / 'MANIFEST.json'
    if manifest_path.exists():
        data = json.loads(manifest_path.read_text(encoding='utf-8'))
        if data.get('license') != 'MIT OR Apache-2.0':
            errors.append('MANIFEST.json license must be MIT OR Apache-2.0')
        if data.get('distillation', {}).get('raw_reviewer_text_in_release') is not False:
            errors.append('raw reviewer text must not be released')
        if data.get('distillation', {}).get('raw_pdfs_in_release') is not False:
            errors.append('raw PDFs must not be released')

    patterns_path = root / 'reviewer_db/patterns.csv'
    if patterns_path.exists():
        text = patterns_path.read_text(encoding='utf-8')
        if 'verbatim_reviewer_text' not in text or 'not_stored' not in text:
            errors.append('patterns.csv must mark non-verbatim reviewer text handling')

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description='Validate reviewer skill package.')
    parser.add_argument('root', type=Path)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        raise SystemExit('\n'.join(errors))
    print('PASS: package validation complete')


if __name__ == '__main__':
    main()
