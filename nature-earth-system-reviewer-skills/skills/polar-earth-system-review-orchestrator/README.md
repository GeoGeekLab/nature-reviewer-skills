# Polar Earth-System Review Orchestrator

**A cross-disciplinary review layer for Arctic, Antarctic and Southern Ocean manuscripts.**

This product coordinates the seven existing Nature Reviewer Skills rather than adding an eighth foundational discipline. It identifies the polar subsystems and claim types in a manuscript, routes them to the appropriate domain reviewers, applies polar-specific evidence checks, and consolidates a non-redundant referee panel.


## Repository placement

The orchestrator is located under `nature-earth-system-reviewer-skills/skills/` alongside the four foundational Earth-system skills. Its manifest declares `package_type: orchestrator`, so repository discovery, validation, and CI do not count it as an eighth domain skill.

## Scientific value

Polar papers are unusually vulnerable to evidence gaps caused by sparse and logistics-driven observations, extreme seasonality, rapidly changing surface states, satellite-algorithm dependence, strong internal variability, unresolved geometry, coupled feedbacks and local-to-circumpolar extrapolation. The orchestrator is designed to expose these weaknesses before submission.

It is useful for:

- ice-sheet, glacier, ice-shelf and sea-level studies;
- Arctic and Antarctic sea-ice observations and projections;
- permafrost, snow and thermokarst research;
- polar ocean-atmosphere coupling and extreme events;
- polar ecosystems, carbon, methane, mercury and biological-pump studies;
- polar remote sensing, geospatial machine learning and data products;
- ice-core, sediment and paleo-oceanographic reconstructions;
- interdisciplinary manuscripts that otherwise receive repetitive or disconnected reviews.

## Architecture

```text
7 domain reviewer skills
        +
polar claim router
        +
104 polar-specific reviewer patterns
        +
3 default / 4 conditional reviewer roles
        +
evidence-linked synthesis and deduplication
```

The package includes 34 hashed public peer-review files in its provenance index: 24 Nature Portfolio peer-review files and 10 open referee comments from The Cryosphere Discussions. It also cites eight official methodological and governance sources. Raw peer-review PDFs are deliberately excluded.

## Routes

| Polar manuscript component | Primary existing skills | Added polar checks |
|---|---|---|
| Sea ice | Remote sensing + atmosphere | metric identity, melt-state retrieval bias, threshold definition, momentum and stratification coupling |
| Ice sheet / glacier | Hydrology + remote sensing | firn/density conversion, grounding line, buttressing, calving, ocean access and mass-budget closure |
| Permafrost / snow | Hydrology + climate-ecology | depth/season identity, network bias, thaw versus degradation, carbon-pathway evidence |
| Polar ocean-atmosphere | Atmosphere + climate-ecology | internal variability, event detection, feedback direction, heat/freshwater budgets |
| Ecology / biogeochemistry | Climate-ecology + chemistry | habitat sampling, stocks versus fluxes, functional evidence, moving ice-edge confounding |
| Paleoclimate | Climate-ecology + chemistry | chronology, proxy non-uniqueness, archive processes, effective resolution |
| Instrumentation | Engineering + remote sensing | extreme operating envelope, calibration, coverage, representativeness and field impact |

## Quick start

From the repository root:

```bash
python -m pip install -e ".[documents,dev]"
python scripts/sync_skill_assets.py
python scripts/validate_all.py
python -m pytest
```

Search the polar reviewer memory:

```bash
python nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/scripts/reviewer_db.py \
  --root nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator \
  --query "Arctic sea ice trend spans multiple sensors and summer melt conditions" \
  --limit 8
```

Route a manuscript summary:

```bash
python nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/scripts/route_review.py \
  --text "We estimate Antarctic ice-shelf basal melt from radar and an ocean model..."
```

## Suggested invocation

```text
Use the polar Earth-system review orchestrator. Route the manuscript to the relevant existing
reviewer skills, apply polar-specific evidence gates, assign distinct reviewer responsibilities,
and produce three evidence-anchored referee reports plus a deduplicated revision priority list.
```

## Package contents

```text
SKILL.md                    agent instruction entry point
router.json                 subsystem-to-domain routing
reviewer_roles.json         non-overlapping panel responsibilities
gates/                      polar-specific evidence gates
reviewer_db/                104 non-verbatim reviewer patterns
corpus/                     source metadata, hashes and distillation report
benchmarks/                 polar positive and negative-control cases
references/                 architecture, evidence and evaluation contracts
scripts/                    validation, routing, retrieval and extraction tools
tests/                      package and routing tests
```

## Limitations

This is a research-assistance and pre-submission quality-control system. It does not replace cryosphere, ocean, atmosphere, ecology, Indigenous/community research, treaty, or legal experts. Synthetic benchmark fixtures test software behavior, not expert-equivalent reviewing.

## License

MIT. Source metadata and abstract reviewer patterns are distributed; raw peer-review files are not.
