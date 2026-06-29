## What changed


## Why it changed


## Validation

- [ ] `python scripts/validate_package.py .`
- [ ] `python -m compileall -q scripts`
- [ ] `python -m pytest -q`
- [ ] `python -m ruff check .`
- [ ] `python -m ruff format --check .`

## Risk check

- [ ] No raw reviewer text or peer-review PDFs added.
- [ ] Default output remains 2-4 independent referees.
- [ ] Internal gate routing is not exposed in default reports.
- [ ] Markdown and DOCX output path remains supported.
