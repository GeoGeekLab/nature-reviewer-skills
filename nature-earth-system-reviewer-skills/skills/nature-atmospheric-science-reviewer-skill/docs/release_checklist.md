# Release checklist

- [ ] `python scripts/validate_package.py .`
- [ ] `python -m compileall -q scripts`
- [ ] `python -m pytest -q`
- [ ] `python -m ruff check .`
- [ ] `python -m ruff format --check .`
- [ ] `python -m bandit -q -r scripts`
- [ ] `python scripts/render_review_docx.py examples/example_review_report.md /tmp/example_review_report.docx`
- [ ] Tag `v1.0` exists.
- [ ] GitHub Release title is `nature-atmospheric-science-reviewer-skill-v1.0`.
- [ ] Repository root is not wrapped in an extra versioned folder.
- [ ] No raw Peer Review File PDFs or long original reviewer comments are included.
