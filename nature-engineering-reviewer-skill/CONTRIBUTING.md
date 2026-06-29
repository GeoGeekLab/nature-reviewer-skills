# Contributing

Contributions should improve the skill's review quality without adding raw copyrighted reviewer text or exposing anonymous reviewer identities.

## Acceptable contributions

- Concise domain gates that generalize across engineering manuscripts.
- Abstract reviewer-memory patterns written in original language.
- Tests, validation scripts and documentation improvements.
- Examples that do not contain confidential manuscripts.

## Not acceptable

- Long verbatim peer-review excerpts.
- Attempts to identify anonymous reviewers.
- Case-specific gates that overfit to one manuscript.
- Claims that the corpus is an official Nature Portfolio dataset.

Run validation before opening a pull request:

```bash
python scripts/validate_package.py .
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
```
