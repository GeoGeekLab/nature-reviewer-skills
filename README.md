# nature-reviewer-skills

A suite-level distribution for GeoGeekLab Nature-style reviewer skills.

## Structure

- `nature-earth-system-reviewer-skills/` — umbrella repository for four independent Earth-system skills:
  - remote sensing
  - atmospheric science
  - hydrology
  - climate and ecology
- `nature-chemistry-reviewer-skill/`
- `nature-engineering-reviewer-skill/`
- `nature-materials-science-reviewer-skill/`

The Earth-system umbrella is a maintenance and distribution layer. It does not collapse the four skills into one prompt. Each included skill remains independently installable and keeps its own `SKILL.md`, reviewer memory, gates, templates, scripts, tests, and license metadata.
