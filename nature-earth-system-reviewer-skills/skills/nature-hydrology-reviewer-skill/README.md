# Nature Hydrology Reviewer Skill

![Version](https://img.shields.io/badge/version-2.2.0-blue)
![Package type](https://img.shields.io/badge/package-domain%20skill-4c1)
![Domain](https://img.shields.io/badge/domain-hydrology-brightgreen)
![License](https://img.shields.io/badge/license-MIT-yellow)

**Evidence-centered review for hydrological observations, catchment and groundwater processes, floods, droughts, water quality, models, remote sensing, and water-resource claims.**

This package is one of the seven foundational domain reviewer skills in
[Nature Reviewer Skills](https://github.com/GeoGeekLab/nature-reviewer-skills).

> The objective is not language polishing. The objective is to determine whether the manuscript's strongest scientific claims are supported by the evidence actually presented.

## Scientific value

Hydrological conclusions are especially sensitive to variable identity, scale, storage and flux accounting, calibration choices, equifinality, human regulation, and extrapolation across catchments. This skill tests whether the water-system evidence chain closes physically and inferentially.

The skill is intended for pre-submission review, internal research-group red teaming, revision planning, reviewer-response preparation, and evidence-centered training for early-career researchers.

## Appropriate scope

Use this skill for:

- catchment, river, lake, wetland, groundwater, snow, and soil-moisture studies
- flood, drought, water-quality, and hydroclimate attribution
- hydrological, hydraulic, land-surface, groundwater, and coupled models
- remote-sensing and reanalysis products used for hydrological inference
- water balance, evapotranspiration, recharge, runoff, storage, and flux estimates
- water-resource, infrastructure, management, and risk implications

For interdisciplinary manuscripts, combine it with other domain skills or a relevant orchestrator rather than forcing all claims through one disciplinary lens.

## Core evidence gates

The gates are activated according to the manuscript's central claims; they are not applied as a mechanical checklist.

| Review area | What is stress-tested |
|---|---|
| **Hydrological variable identity** | Flux versus storage, discharge versus runoff, recharge versus infiltration, proxy and product comparability |
| **Water and mass balance** | Closure, residuals, boundary fluxes, storage changes, units, density, and time integration |
| **Sampling and scale** | Gauge representativeness, basin delineation, spatial dependence, event selection, and point-to-catchment transfer |
| **Calibration and validation** | Data independence, equifinality, parameter identifiability, split design, benchmark fairness, and structural error |
| **Human and climatic controls** | Reservoirs, withdrawals, irrigation, land use, regulation, climate variability, and attribution |
| **Extremes and decisions** | Non-stationarity, tail estimation, return periods, scenario dependence, and operational or policy claims |

The package contains **158 abstracted reviewer-reasoning patterns**. They support retrieval and review planning without reproducing raw referee reports.

## Expected review output

A standard run produces **2–4 complementary referee-style reports**, defaulting to three. Each report should:

1. identify the manuscript's central contribution and strongest claims;
2. distinguish direct evidence from derived products, models, correlations, mechanisms, and extrapolations;
3. anchor major concerns to figures, tables, methods, results, supplementary evidence, or explicit missing evidence;
4. explain why each concern matters to the central claim;
5. propose a proportionate resolution: additional analysis, stronger validation, a discriminating experiment, clearer uncertainty, or narrower wording;
6. separate major concerns from local reporting and presentation issues.

A major concern should follow this logic:

```text
claim under review
→ evidence or missing evidence
→ scientific risk
→ alternative explanation or failure mode
→ actionable revision path
```

## Use with an agent runtime

Clone the suite and install the shared runtime:

```bash
git clone https://github.com/GeoGeekLab/nature-reviewer-skills.git
cd nature-reviewer-skills
python -m pip install -e ".[documents]"
```

Point the agent runtime to:

```text
nature-earth-system-reviewer-skills/skills/nature-hydrology-reviewer-skill/SKILL.md
```

For runtimes using `.agents/skills`, copy the complete package directory and keep `SKILL.md`, `reviewer_db/`, `references/`, `templates/`, and `scripts/` together.

Invoke the skill as:

```text
$nature-hydrology-reviewer
```

Example request:

```text
Use $nature-hydrology-reviewer to review the manuscript. Audit hydrological variable definitions, water and mass balance, sampling and scale, calibration and validation independence, equifinality, uncertainty, attribution, extremes, and whether management conclusions exceed the evidence.
```

## Package contents

```text
README.md                         user-facing overview
SKILL.md                          agent instructions and review workflow
MANIFEST.json                     version, type, runtime, and pattern metadata
reviewer_db/patterns.jsonl        canonical reviewer-pattern database
reviewer_db/patterns.csv          tabular reviewer-pattern export
reviewer_db/summary.json          pattern and gate statistics
references/                       evidence protocol, domain gates, and evaluation contract
templates/review_report.md        report structure
scripts/                          validation, retrieval, extraction, and DOCX rendering wrappers
tests/                            package-level regression tests
checksums.sha256                  package integrity manifest
```

## Validation and reviewer-memory search

From the repository root:

```bash
python scripts/validate_all.py
python -m pytest
```

Validate this package directly:

```bash
nature-reviewer-validate "nature-earth-system-reviewer-skills/skills/nature-hydrology-reviewer-skill"
```

Search its reviewer memory:

```bash
nature-reviewer-search \
  --root "nature-earth-system-reviewer-skills/skills/nature-hydrology-reviewer-skill" \
  --query "describe the scientific concern to stress-test" \
  --limit 5
```

## v2.1 at a glance

Compared with the v1 generation, v2.1 provides:

- a shared, typed `nature_reviewer_core` runtime instead of duplicated package logic;
- field-weighted BM25 retrieval with phrase support, query expansion, confidence reporting, and diversity-aware selection;
- standardized manifests, package validation, checksums, tests, and benchmark contracts;
- safer manuscript extraction and report generation with explicit input and evidence boundaries;
- clearer multi-referee roles, evidence anchoring, severity calibration, and non-fabrication requirements.

These improvements strengthen consistency and auditability. They do not replace expert scientific judgment.

## Reliability boundary

This skill is a research-assistance and manuscript-quality-control tool. It does not:

- replace qualified domain experts, editors, or formal peer review;
- guarantee correctness, novelty, acceptance, or reproducibility;
- justify unsupported research-misconduct allegations;
- treat a model, retrieval, proxy, correlation, or benchmark as direct proof without validation.

The reviewer memory contains abstracted, non-verbatim reasoning patterns. Raw referee reports are not redistributed.

This project is not affiliated with Nature Portfolio or Springer Nature.

## License

Released under the [MIT License](LICENSE).
