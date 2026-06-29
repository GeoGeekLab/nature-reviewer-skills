# Release Checklist

- [ ] `python scripts/validate_package.py .`
- [ ] `python -m compileall -q scripts`
- [ ] `python -m pytest -q`
- [ ] `python -m ruff check .`
- [ ] `python -m ruff format --check .`
- [ ] `python -m bandit -q -r scripts`
- [ ] `python scripts/render_review_docx.py examples/example_review_report.md /tmp/example_review_report.docx`
- [ ] README badges render.
- [ ] `SKILL.md` front matter is valid.
- [ ] No raw peer-review PDFs are included.
- [ ] `references/referee_voice_style_gate.md` exists.
- [ ] Tag `v1.0` exists.
- [ ] GitHub Release title: `nature-materials-science-reviewer-skill-v1.0`.
