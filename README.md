# Nature Reviewer Skills

[![CI](https://github.com/GeoGeekLab/nature-reviewer-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/GeoGeekLab/nature-reviewer-skills/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/GeoGeekLab/nature-reviewer-skills)](https://github.com/GeoGeekLab/nature-reviewer-skills/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](pyproject.toml)

**Domain-aware scientific reviewer skills for stress-testing a manuscript before journal reviewers do.**

Nature Reviewer Skills helps researchers find the weaknesses that matter most in high-level peer review: unsupported claims, incomplete evidence chains, weak controls, invalid generalization, unresolved alternative explanations, uncertainty gaps, and conclusions that exceed the data.

It is not a grammar checker and not a generic “review my paper” prompt. Each skill applies discipline-specific review gates and distilled reviewer-reasoning patterns to produce structured, revision-oriented scientific criticism.

> **Core principle:** the stronger the claim, the stronger and more discriminating the evidence must be.

## Why use it?

A manuscript can be clearly written and still fail peer review because its central scientific claim is not adequately supported. This suite is designed to expose that mismatch before submission.

Use it to:

- identify major scientific vulnerabilities before they appear in referee reports;
- test whether conclusions are broader than the validation domain;
- distinguish correlation, attribution, mechanism, and causality;
- check whether controls, baselines, uncertainty analyses, and failure modes are sufficient;
- simulate several reviewer perspectives with different evidence responsibilities;
- convert criticism into specific experiments, analyses, controls, or claim revisions;
- help students and research teams learn how rigorous scientific review reasons.

## What the review focuses on

| Review target | Questions the skills ask |
|---|---|
| Central claim | What is the strongest claim, and what evidence would be required to defend it? |
| Evidence chain | Do data, preprocessing, methods, validation, interpretation, and conclusion form a defensible chain? |
| Controls and baselines | Are the comparisons capable of distinguishing the proposed explanation from alternatives? |
| Validation | Is testing independent, representative, and aligned with the claimed operating domain? |
| Uncertainty | Are measurement, model, sampling, and inferential uncertainties quantified and propagated? |
| Causality and mechanism | Does the evidence support mechanism, or only association and consistency? |
| Generalization | Where does the evidence end, and where does extrapolation begin? |
| Novelty and significance | Is the contribution genuinely new, consequential, and positioned against the strongest prior work? |
| Reproducibility | Are methods, parameters, data, code, and reporting sufficient for verification? |
| Revision path | What additional evidence, analysis, qualification, or narrowing would resolve the concern? |

## What you receive

A typical run produces **2–4 referee-style reports** with complementary perspectives rather than one undifferentiated checklist.

Each major concern should include:

1. **Claim under review**
2. **Evidence anchor** — figure, table, section, method, result, or explicit missing evidence
3. **Why it matters**
4. **Severity**
5. **Alternative explanation or failure mode**
6. **Actionable revision path**

Example concern structure:

```text
Major concern — Generalization exceeds the validation domain

Claim:
The model is presented as transferable across regions and seasons.

Evidence:
Validation is limited to random splits from the same geographic and temporal distribution.

Why this matters:
Random splitting does not test geographic or seasonal transfer and may preserve spatial,
temporal, or preprocessing leakage.

Required revision:
Add geographically and temporally independent evaluation, quantify performance degradation,
and either support the transferability claim or narrow it to the tested domain.
```

## Included reviewer skills

The suite contains seven domain-specific skills, one Polar Earth-System Review Orchestrator, and 644 abstracted reviewer-reasoning patterns.

| Skill | Best suited for | Typical stress tests |
|---|---|---|
| **Remote sensing** | Earth observation, retrievals, geospatial ML, mapping and trend products | spatial leakage, product validity, independent validation, uncertainty propagation, out-of-domain transfer |
| **Atmospheric science** | observations, reanalysis, numerical models, atmospheric chemistry, extremes, AI weather/climate | observation–model consistency, attribution, scale mismatch, internal variability, forcing and boundary assumptions |
| **Hydrology** | catchments, discharge, groundwater, drought, floods, water quality and water resources | water balance, variable identity, gauge representativeness, calibration/validation, equifinality, scale transfer |
| **Climate and ecology** | climate impacts, ecosystems, carbon cycles, biodiversity, land use and conservation | confounding, ecological mechanism, representativeness, driver separation, management and policy overreach |
| **Chemistry** | synthesis, catalysis, analytical chemistry, mechanisms, chemical biology and molecular discovery | identity and purity, discriminating controls, scope, selectivity, mechanistic support, reproducibility |
| **Engineering** | devices, systems, robotics, biomedical and environmental engineering, physical AI | requirement–design–validation coherence, benchmark fairness, operating envelope, failure modes, real-world utility |
| **Materials science** | synthesis, characterization, structure–property relations, stability and applications | phase identity, benchmark comparability, mechanism, durability, processability, scalability and application boundaries |


## Polar Earth-System Review Orchestrator

The repository now includes **one upper-layer polar orchestrator in addition to the seven domain skills**. It is not counted as an eighth discipline. It routes Arctic, Antarctic and Southern Ocean claims to the existing domain reviewers, applies 104 polar-specific evidence patterns, assigns non-overlapping reviewer roles, and consolidates the review.

Typical checks include sparse and logistics-driven sampling, season and regional scope, sea-ice/glacier/permafrost variable identity, satellite-product lineage, mass and energy budgets, model geometry, internal variability, proxy chronology, community/Indigenous knowledge governance, and Antarctic environmental reporting.

See [`nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/`](nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/). The package is colocated with the Earth-system skills but remains classified as an orchestrator by its manifest.

## Who it is for

- **Researchers** preparing manuscripts for selective journals
- **Principal investigators** running internal pre-submission review
- **Graduate students** learning evidence-centered scientific criticism
- **Research teams** building manuscript quality-control workflows
- **Editors and reviewers** structuring an initial claim–evidence audit
- **Agent developers** building domain-aware scientific review systems

## How it works

```text
manuscript
   ↓
identify central claims
   ↓
route claims to discipline-specific evidence gates
   ↓
retrieve relevant reviewer-reasoning patterns
   ↓
stress-test controls, validation, uncertainty, mechanism, and scope
   ↓
generate complementary referee-style reports
   ↓
deduplicate concerns and propose revision paths
```

The reviewer-memory layer stores **abstracted, non-verbatim scientific reasoning patterns**, not copied referee reports. A pattern follows the logic:

```text
claim type → evidence risk → stress-test gate → reviewer concern → revision direction
```

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/GeoGeekLab/nature-reviewer-skills.git
cd nature-reviewer-skills
```

### 2. Install the shared runtime

Core installation:

```bash
python -m pip install -e .
```

Install document support and development tools when needed:

```bash
python -m pip install -e ".[documents,dev]"
```

### 3. Validate the repository

```bash
python scripts/sync_skill_assets.py
python scripts/validate_all.py
python -m pytest
```

### 4. Install or load a skill

Copy the required skill directory into the skills directory used by your agent runtime, or point the runtime directly to its `SKILL.md`.

Earth-system skills are under:

```text
nature-earth-system-reviewer-skills/skills/
```

Other domain skills are at the repository root:

```text
nature-chemistry-reviewer-skill/
nature-engineering-reviewer-skill/
nature-materials-science-reviewer-skill/
```

## Example requests

### Hydrology

```text
Use the hydrology reviewer skill to conduct a rigorous pre-submission review.
Identify the central claims and test water-balance consistency, variable validity,
validation independence, uncertainty, scale transfer, attribution, and whether the
conclusions exceed the evidence.
```

### Materials science

```text
Review this manuscript using the materials-science reviewer skill. Focus on material
identity, structure–property causality, benchmark comparability, stability, degradation,
replicates, scalability, and whether the application claims are experimentally supported.
```

### Interdisciplinary manuscript

```text
Use the remote-sensing, atmospheric-science, and climate-ecology reviewer skills as a panel.
Assign distinct responsibilities to each reviewer, avoid duplicate concerns, and produce a
consolidated list of the highest-priority revisions.
```

## Command-line tools

Search a skill’s reviewer-pattern database:

```bash
nature-reviewer-search \
  --root nature-chemistry-reviewer-skill \
  --query "mechanism claim without discriminating controls" \
  --limit 5
```

Validate a package:

```bash
nature-reviewer-validate nature-chemistry-reviewer-skill
```

Evaluate structured predictions:

```bash
nature-reviewer-evaluate \
  benchmarks/cases \
  benchmarks/predictions/example_predictions.jsonl
```

Extract manuscript text with anchors and defensive limits:

```bash
python nature-chemistry-reviewer-skill/scripts/extract_text_with_anchors.py \
  manuscript.pdf \
  --output extracted.jsonl
```

## Reliability and evaluation

The repository includes:

- a shared typed Python runtime;
- deterministic field-weighted BM25 retrieval;
- phrase boosts, query expansion, confidence reporting, and diversity-aware selection;
- root-level matrix CI;
- package validation for all seven skills;
- benchmark schemas and synthetic infrastructure fixtures;
- metrics for issue recall, precision, severity agreement, evidence anchoring, and panel duplication;
- defensive PDF, DOCX, archive, path, size, page-count, and extraction limits;
- explicit safeguards against fabricated citations, figures, page numbers, evidence, or misconduct allegations.

Technical design and evaluation details are documented in:

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/EVALUATION.md`](docs/EVALUATION.md)
- [`docs/SECURITY.md`](docs/SECURITY.md)
- [`docs/MIGRATION.md`](docs/MIGRATION.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Repository layout

```text
src/nature_reviewer_core/           shared runtime
scripts/                            repository-wide commands
tests/                              shared-runtime tests
benchmarks/                         schemas and benchmark fixtures
.github/workflows/ci.yml            root-level continuous integration
nature-chemistry-reviewer-skill/    chemistry skill
nature-engineering-reviewer-skill/  engineering skill
nature-materials-science-reviewer-skill/
nature-earth-system-reviewer-skills/skills/
                                    four Earth-system skills
```

## Important limitations

Nature Reviewer Skills is a **research-assistance and quality-control system**.

It is not:

- a replacement for qualified domain experts;
- an editorial decision system;
- a guarantee of acceptance;
- evidence that a manuscript is scientifically correct;
- a tool for making unsupported research-misconduct allegations;
- an official Nature Portfolio or Springer Nature product.

The included synthetic benchmarks validate the software and evaluation pipeline, not expert-level scientific-review performance. Independent expert gold sets, blinded manuscript studies, negative controls, calibration, and prospective evaluation are still required.

Figures, spectra, equations, maps, chemical structures, and other visual evidence require a multimodal runtime capable of inspecting the original manuscript content.

## Provenance and copyright boundary

The reviewer-memory databases contain generalized, non-verbatim reasoning patterns distilled from public peer-review materials and domain evidence standards.

The repository does not redistribute raw referee reports, identifiable reviewer language, private review material, or full copyrighted manuscripts.

## Contributing

Contributions are welcome in the form of:

- new disciplinary reviewer skills;
- stronger domain evidence gates;
- expert-annotated benchmark cases;
- false-positive and negative-control tests;
- retrieval and deduplication improvements;
- documentation and reproducibility improvements.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE).

---

**Nature Reviewer Skills helps researchers ask the difficult scientific questions before journal reviewers ask them.**
