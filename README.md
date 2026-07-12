# Nature Reviewer Skills — Reliability & Evaluation Edition

This repository is a hardened, testable refactor of the public `GeoGeekLab/nature-reviewer-skills` project. It preserves the seven domain skills and their distilled reviewer-pattern databases, while adding a shared runtime, root-level CI, deterministic retrieval, security controls, package validation, benchmark infrastructure, and reviewer-panel diversity controls.

## What changed

- One root CI workflow discovers and validates every skill package.
- Shared Python implementation removes duplicated validators, retrieval logic, and extractors.
- Heterogeneous pattern schemas are normalized without deleting original CSV fields.
- Retrieval uses deterministic BM25-style ranking, phrase boosts, query expansion, confidence reporting, and diversity-aware selection.
- File ingestion applies path, file-size, archive-expansion, page-count, and extracted-text limits.
- Reviewer personas are assigned non-overlapping evidence responsibilities to reduce correlated repetition.
- A benchmark format measures issue recall, false-positive rate, severity agreement, evidence-anchor coverage, and panel duplication.
- Every skill receives a consistent manifest, generated JSONL database, package tests, security guidance, and output template.

## Scope and limitations

This remains a research-assistance system. It does not establish that generated reviews are equivalent to independent domain-expert peer review. The included benchmark cases are synthetic infrastructure tests, not a claim of scientific validity. Production use requires domain-expert gold sets and prospective evaluation.

## Quick start

```bash
python -m pip install -e .
python scripts/sync_skill_assets.py
python scripts/validate_all.py
python -m pytest
python scripts/run_benchmarks.py benchmarks/cases benchmarks/predictions/example_predictions.jsonl
```

Search a skill's pattern database:

```bash
python nature-chemistry-reviewer-skill/scripts/reviewer_db.py \
  --root nature-chemistry-reviewer-skill \
  --query "mechanism claim without discriminating controls" \
  --limit 5
```

Extract a manuscript with defensive limits:

```bash
python nature-chemistry-reviewer-skill/scripts/extract_text_with_anchors.py \
  manuscript.pdf --output extracted.jsonl
```

## Repository layout

```text
src/nature_reviewer_core/        shared runtime
scripts/                         repository-wide commands
tests/                           shared runtime tests
benchmarks/                      benchmark schema and synthetic fixtures
.github/workflows/ci.yml         actual root-level CI
nature-*-reviewer-skill/         standalone domain skills
nature-earth-system-reviewer-skills/skills/
                                 four Earth-system skills
```

## License

MIT. Distilled pattern databases retain their upstream provenance and copyright notices. No raw peer-review reports are redistributed.
