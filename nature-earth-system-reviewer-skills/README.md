# nature-earth-system-reviewer-skills

Umbrella repository for four independent Nature-style Earth-system reviewer skills.

## Included skills

- `skills/nature-remote-sensing-reviewer-skill`
- `skills/nature-atmospheric-science-reviewer-skill`
- `skills/nature-hydrology-reviewer-skill`
- `skills/nature-climate-ecology-reviewer-skill`

Each skill remains a standalone Codex-compatible package with its own `SKILL.md`, `README.md`, `MANIFEST.json`, `reviewer_db/`, `references/`, `templates/`, `scripts/`, and tests. The umbrella repository is a distribution and maintenance layer, not a merged mega-skill.

## Validation

```bash
python scripts/validate_umbrella.py .
python -m compileall -q scripts
python -m pytest -q
```
