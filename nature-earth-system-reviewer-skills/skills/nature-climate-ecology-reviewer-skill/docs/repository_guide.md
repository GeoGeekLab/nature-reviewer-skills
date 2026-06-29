# Repository Guide

## Core files

- `SKILL.md`: main skill contract and operating rules.
- `MANIFEST.json`: machine-readable package metadata and file inventory.
- `README.md`: public-facing overview, quick start and validation commands.

## Knowledge files

- `reviewer_db/`: abstracted reviewer concern patterns.
- `references/`: gate definitions and review standards.
- `templates/`: final report templates.
- `_internal/`: non-public operational metadata. Do not treat it as user-facing documentation.

## Tooling

- `scripts/validate_package.py`: validates package completeness and output-format constraints.
- `scripts/render_review_docx.py`: renders Markdown referee reports to Word DOCX.
- `tests/`: smoke tests for validation and rendering behavior.
