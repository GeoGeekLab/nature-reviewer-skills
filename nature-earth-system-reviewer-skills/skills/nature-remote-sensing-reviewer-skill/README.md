# Nature Remote Sensing Reviewer Skill

![Version](https://img.shields.io/badge/version-2.2.0-blue)
![Package type](https://img.shields.io/badge/package-domain%20skill-4c1)
![Domain](https://img.shields.io/badge/domain-remote%20sensing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-yellow)

**Evidence-centered review for Earth-observation retrievals, mapping, geospatial machine learning, multi-sensor products, validation, uncertainty, and transferability.**

This package is one of the seven foundational domain reviewer skills in
[Nature Reviewer Skills](https://github.com/GeoGeekLab/nature-reviewer-skills).

> The objective is not language polishing. The objective is to determine whether the manuscript's strongest scientific claims are supported by the evidence actually presented.

## Scientific value

Remote-sensing papers often conflate sensor measurements, algorithm outputs, mapped variables, and scientific interpretation. This skill separates those layers and checks whether validation, sampling, uncertainty, spatial dependence, and out-of-domain testing justify the claimed product or Earth-system conclusion.

The skill is intended for pre-submission review, internal research-group red teaming, revision planning, reviewer-response preparation, and evidence-centered training for early-career researchers.

## Appropriate scope

Use this skill for:

- optical, thermal, microwave, radar, lidar, altimetry, and multi-sensor studies
- retrieval algorithms and geophysical or biophysical products
- classification, segmentation, mapping, change detection, and trend products
- geospatial machine learning, foundation models, and transfer learning
- data fusion, downscaling, super-resolution, and gap filling
- satellite-derived products used in climate, hydrology, ecology, agriculture, or hazards

For interdisciplinary manuscripts, combine it with other domain skills or a relevant orchestrator rather than forcing all claims through one disciplinary lens.

## Core evidence gates

The gates are activated according to the manuscript's central claims; they are not applied as a mechanical checklist.

| Review area | What is stress-tested |
|---|---|
| **Measurement-to-variable chain** | Sensor response, preprocessing, retrieval assumptions, target definition, and physical meaning |
| **Reference data** | Label quality, temporal alignment, spatial support, independence, and representativeness |
| **Leakage and splitting** | Spatial, temporal, scene, tile, sensor, preprocessing, and benchmark leakage |
| **Validation and metrics** | Independent test design, class imbalance, thresholding, calibration, uncertainty, and error geography |
| **Resolution and scaling** | Mixed pixels, footprint mismatch, downscaling assumptions, aggregation, and change of support |
| **Transfer and product claims** | Cross-region, cross-season, cross-sensor, cross-year, and operational generalization |

The package contains **31 abstracted reviewer-reasoning patterns**. They support retrieval and review planning without reproducing raw referee reports.

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
nature-earth-system-reviewer-skills/skills/nature-remote-sensing-reviewer-skill/SKILL.md
```

For runtimes using `.agents/skills`, copy the complete package directory and keep `SKILL.md`, `reviewer_db/`, `references/`, `templates/`, and `scripts/` together.

Invoke the skill as:

```text
$nature-remote-sensing-reviewer
```

Example request:

```text
Use $nature-remote-sensing-reviewer to review the manuscript. Trace the measurement-to-product evidence chain, test reference-data independence, leakage, spatial and temporal validation, uncertainty, scale consistency, transferability, and whether mapped outputs support the scientific claims.
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
nature-reviewer-validate "nature-earth-system-reviewer-skills/skills/nature-remote-sensing-reviewer-skill"
```

Search its reviewer memory:

```bash
nature-reviewer-search \
  --root "nature-earth-system-reviewer-skills/skills/nature-remote-sensing-reviewer-skill" \
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
