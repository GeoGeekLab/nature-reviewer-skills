# Contributing

Contributions should improve the skill's clarity, transferability, validation, or chemistry-domain coverage.

Do not contribute raw Peer Review PDF files, long verbatim reviewer comments, or any material intended to identify anonymous reviewers.

Before opening a pull request, run:

```bash
python scripts/validate_package.py .
python -m pytest -q
python -m ruff check .
python -m bandit -q -r scripts
```
