# nature-earth-system-reviewer-skills

![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)
![Earth System Science](https://img.shields.io/badge/Domain-Earth%20System%20Science-green)
![Status](https://img.shields.io/badge/Status-Research%20Skill%20Umbrella-brightgreen)

An umbrella repository for four independent Nature-style reviewer skills in Earth system science:

* `nature-remote-sensing-reviewer`
* `nature-atmospheric-science-reviewer`
* `nature-hydrology-reviewer`
* `nature-climate-ecology-reviewer`

This repository is not a merged mega-skill. It is a coordinated Earth-system review layer that keeps each skill scientifically independent while placing them within a shared intellectual frame: observing, modeling, explaining, and governing the Earth as a coupled natural-human system.

The central premise is simple:

> Earth-system manuscripts do not fail only because a model is weak, a dataset is sparse, or a figure is unclear.
> They fail when claims about Earth processes exceed the observational, mechanistic, spatial, temporal, and causal evidence that supports them.

`nature-earth-system-reviewer-skills` is designed to stress-test that boundary.

---

## Why Earth-system review needs its own skill layer

Earth system science is not a loose collection of environmental topics. It is the study of coupled processes across atmosphere, hydrosphere, biosphere, cryosphere, lithosphere, and human-modified landscapes.

A manuscript in this domain often moves across multiple epistemic layers:

```text
observation → retrieval → product → model → process inference → attribution → projection → governance implication
```

Each transition creates risk.

A satellite index may become an ecosystem conclusion.
A reanalysis pattern may become an atmospheric mechanism.
A precipitation anomaly may become a drought claim.
A catchment result may become a regional water-security narrative.
A biodiversity correlation may become a conservation prescription.

Top-tier peer review in Earth system science therefore requires more than general scientific criticism. It requires domain-specific pressure on scale, mechanism, uncertainty, causality, representativeness, and sustainability relevance.

This umbrella exists to organize that pressure.

---

## Included skills

```text
nature-earth-system-reviewer-skills/
└── skills/
    ├── nature-remote-sensing-reviewer-skill/
    ├── nature-atmospheric-science-reviewer-skill/
    ├── nature-hydrology-reviewer-skill/
    └── nature-climate-ecology-reviewer-skill/
```

Each skill remains an independent Codex-compatible package with its own:

* `SKILL.md`
* `README.md`
* `MANIFEST.json`
* `reviewer_db/`
* `references/`
* `templates/`
* `scripts/`
* `tests/`

The umbrella repository provides coordination, validation, distribution, and conceptual integration. It does not dilute disciplinary specificity.

---

## The four reviewer directions

### 1. Remote sensing and Earth observation

`nature-remote-sensing-reviewer` is designed for manuscripts involving satellite remote sensing, Earth observation products, geospatial machine learning, retrieval algorithms, image time series, spatial products, environmental monitoring, and large-scale mapping.

It is especially concerned with the fragile transition from sensor signal to Earth-system inference.

Primary reviewer questions include:

* Is the target variable directly observed, retrieved, proxied, modeled, or inferred?
* Does validation support the spatial, temporal, and environmental domain claimed?
* Are out-of-domain conditions, sensor limitations, cloud/turbidity/surface effects, and preprocessing choices treated seriously?
* Does the manuscript separate product accuracy from scientific inference?
* Are uncertainty and error propagation carried from retrieval to trend, attribution, or management conclusion?
* Are geographic coordinates, seasonality, or spatial autocorrelation leaking into model performance?

This skill is most useful when a paper claims that a satellite-derived product reveals a pattern, process, trend, risk, or intervention-relevant signal.

---

### 2. Atmospheric science and atmospheric systems

`nature-atmospheric-science-reviewer` is designed for manuscripts involving atmospheric observation, reanalysis, numerical modeling, weather and climate dynamics, aerosol-cloud-radiation interactions, atmospheric chemistry, extreme events, circulation change, and AI weather or climate systems.

It focuses on the relationship between atmospheric evidence and atmospheric explanation.

Primary reviewer questions include:

* Is the atmospheric variable observational, reanalysis-derived, simulated, diagnosed, or parameterized?
* Are dynamical mechanisms separated from statistical associations?
* Are forcing, internal variability, boundary conditions, and model dependence treated explicitly?
* Does the analysis respect scale coupling across local process, synoptic pattern, regional circulation, and global climate background?
* Are aerosol-cloud-radiation claims supported by process-sensitive evidence rather than correlation alone?
* Are AI weather or climate claims evaluated against physically meaningful baselines and failure modes?

This skill is most useful when a paper claims atmospheric mechanism, predictability, attribution, circulation change, or weather-climate relevance.

---

### 3. Hydrology, water systems, and hydroclimatic risk

`nature-hydrology-reviewer` is designed for manuscripts involving catchment hydrology, river discharge, groundwater, soil moisture, floods, droughts, water quality, water resources, hydroclimatic extremes, watershed management, and water-security implications.

It is especially concerned with hydrological meaning: whether the variable being analyzed is the variable being claimed.

Primary reviewer questions include:

* Is the manuscript confusing precipitation anomaly, meteorological drought, hydrological drought, agricultural drought, or water scarcity?
* Are river stage, discharge, runoff, storage, groundwater, and total water storage distinguished correctly?
* Is the water balance physically plausible?
* Are concentration and load separated in water-quality inference?
* Are calibration, validation, equifinality, and transferability handled transparently?
* Does evidence from a station, catchment, or short period justify broader basin-scale or policy claims?

This skill is most useful when a paper moves from hydrological data to claims about water processes, extremes, management, resilience, or risk.

---

### 4. Climate, ecology, carbon, and coupled human-natural systems

`nature-climate-ecology-reviewer` is designed for manuscripts involving climate impacts, ecological response, biodiversity, ecosystem stability, carbon and nutrient cycles, vegetation dynamics, conservation inference, land-use change, nature-based solutions, and coupled climate-ecology systems.

It focuses on the boundary between ecological association, climate driver, process mechanism, and sustainability implication.

Primary reviewer questions include:

* Are climate drivers separated from land use, management, disturbance, sampling bias, and spatial confounding?
* Does the evidence support ecological mechanism, or only statistical association?
* Are biodiversity, ecosystem function, resilience, and carbon-cycle claims measured at compatible scales?
* Are temporal lags, nonlinear responses, thresholds, and legacy effects considered?
* Are conservation or sustainability recommendations proportional to the evidence?
* Does the manuscript distinguish global relevance from local or biome-specific inference?

This skill is most useful when a paper links climate, ecosystems, carbon, biodiversity, and human decision-making.

---

## Shared review philosophy

Although the four skills are independent, they share a common reviewer logic.

### Claim-dependent routing

The first task is not to apply a checklist. The first task is to identify the manuscript’s strongest claims.

Different claims require different evidence:

```text
global mapping claim
trend detection claim
mechanistic claim
attribution claim
forecasting claim
risk assessment claim
management implication claim
sustainability transition claim
```

The skill then routes review pressure toward the evidence standards required by that claim.

### Evidence-chain stress testing

Earth-system manuscripts often depend on long evidence chains:

```text
data source
→ preprocessing
→ retrieval, measurement, model, or experiment
→ validation
→ uncertainty analysis
→ process interpretation
→ spatial or temporal generalization
→ Earth-system or sustainability claim
```

The reviewer task is to find where the chain becomes weaker than the conclusion.

### Scale discipline

Scale is one of the central problems in Earth system science.

A local observation does not automatically support a regional claim.
A short time series does not automatically support a climate interpretation.
A pixel-level product does not automatically support process attribution.
A catchment result does not automatically support global water-security inference.

The skills therefore test whether the manuscript respects spatial scale, temporal scale, process scale, and governance scale.

### Causality and mechanism

Earth-system science is full of correlated variables. The reviewer question is whether the paper demonstrates a mechanism, rules out alternatives, or merely describes co-variation.

The skills pressure manuscripts on:

* confounding
* alternative explanations
* physical consistency
* ecological plausibility
* hydrological closure
* atmospheric dynamics
* observational representativeness
* model dependence

### Sustainability relevance without overclaiming

Many Earth-system papers now speak to climate adaptation, carbon neutrality, biodiversity conservation, disaster risk reduction, food-water-energy security, and sustainable development.

The skills encourage these links, but require proportionality.

A manuscript may contribute to sustainability science without overstating policy readiness. A reviewer should help the author locate the strongest defensible contribution.

---

## A broader intellectual frame

Earth system science sits between measurement and meaning.

It asks how the Earth works, how human systems transform it, and how knowledge can support more responsible forms of inhabitation.

In this sense, Earth-system review is not only technical. It is also epistemic and geographic:

* What can be known from a given observation?
* At what scale does a pattern become a process?
* When does a model become an explanation?
* Where does environmental inference become governance advice?
* How should uncertainty be carried into decisions rather than hidden beneath confidence?

This umbrella repository treats reviewer skills as instruments for scientific humility.

The goal is not to make manuscripts sound more certain. The goal is to make their uncertainty, evidence, and claims better aligned.

That alignment is essential for Earth observation, climate science, hydrology, ecology, and sustainability research.

---

## Repository structure

```text
nature-earth-system-reviewer-skills/
├── skills/
│   ├── nature-remote-sensing-reviewer-skill/
│   ├── nature-atmospheric-science-reviewer-skill/
│   ├── nature-hydrology-reviewer-skill/
│   └── nature-climate-ecology-reviewer-skill/
├── scripts/
├── tests/
├── MANIFEST.json
├── README.md
├── pyproject.toml
└── requirements-dev.txt
```

Responsibilities:

| Path                   | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| `skills/`              | Four independent Earth-system reviewer skill packages |
| `scripts/`             | Umbrella-level validation and maintenance utilities   |
| `tests/`               | Umbrella-level structure and integrity tests          |
| `MANIFEST.json`        | Machine-readable package metadata                     |
| `README.md`            | Conceptual and operational entry point                |
| `pyproject.toml`       | Python tooling and validation configuration           |
| `requirements-dev.txt` | Development and validation dependencies               |

---

## Validation

Run umbrella-level validation:

```bash
python scripts/validate_umbrella.py .
python -m compileall -q scripts
python -m pytest -q
```

Run individual skill validation from the umbrella root:

```bash
python skills/nature-remote-sensing-reviewer-skill/scripts/validate_package.py skills/nature-remote-sensing-reviewer-skill
python skills/nature-atmospheric-science-reviewer-skill/scripts/validate_package.py skills/nature-atmospheric-science-reviewer-skill
python skills/nature-hydrology-reviewer-skill/scripts/validate_package.py skills/nature-hydrology-reviewer-skill
python skills/nature-climate-ecology-reviewer-skill/scripts/validate_package.py skills/nature-climate-ecology-reviewer-skill
```

A valid Earth-system skill package should preserve:

* domain-specific `SKILL.md`
* independent reviewer-memory patterns
* no raw peer-review PDFs
* no long verbatim reviewer comments
* consistent metadata
* runnable validation scripts
* testable package structure

---

## Usage

Use the umbrella to select the skill that matches the manuscript’s strongest scientific claim.

Example:

```text
Use nature-remote-sensing-reviewer to review this manuscript. Focus on whether the satellite product, validation design, uncertainty propagation, and spatial generalization support the central Earth-observation claim.
```

Example:

```text
Use nature-hydrology-reviewer to review this manuscript. Focus on hydrological variable identity, water-balance plausibility, calibration and validation, uncertainty, and whether the water-security conclusions exceed the evidence.
```

Example:

```text
Use nature-climate-ecology-reviewer to review this manuscript. Focus on climate-driver separation, ecological mechanism, biodiversity or carbon-cycle evidence, spatial confounding, and sustainability implications.
```

Example:

```text
Use nature-atmospheric-science-reviewer to review this manuscript. Focus on atmospheric dynamics, reanalysis or model dependence, attribution, scale consistency, and physical interpretation.
```

---

## Intended users

This umbrella is intended for:

* Earth system scientists preparing high-level submissions
* remote sensing, climate, hydrology, and ecology researchers
* graduate students learning how top-tier reviewers reason
* manuscript teams performing internal pre-review
* GeoAI and Earth AI researchers auditing scientific claims
* sustainability researchers connecting evidence to decision relevance
* AI-assisted research systems requiring domain-aware review logic

---

## What this repository is not

This repository is not:

* a replacement for real peer review
* an official Nature Portfolio resource
* a publication guarantee
* a generic environmental writing prompt
* a redistributed peer-review corpus
* a single merged Earth-system mega-skill
* a tool for identifying or imitating individual reviewers

It is a research-oriented skill umbrella for strengthening Earth-system manuscripts before formal peer review.

---

## Provenance and copyright boundary

The reviewer-memory layer is abstracted and non-verbatim.

The repository is designed not to redistribute:

* raw peer-review PDFs
* long reviewer reports
* identifiable reviewer language
* full article text
* private or non-public review material

The included reviewer logic is represented as generalized evidence-risk patterns, domain gates, validation expectations, and revision directions.

---

## Relationship to `nature-reviewer-skills`

`nature-earth-system-reviewer-skills` is the Earth-system pillar inside the broader `nature-reviewer-skills` suite.

The broader suite includes Earth-system science, chemistry, engineering, and materials science. This umbrella focuses only on Earth-system reasoning: Earth observation, atmosphere, water, climate, ecology, and sustainability-facing environmental inference.

---

## Disclaimer

This is an independent research and engineering project by GeoGeekLab.

It is not affiliated with, endorsed by, or approved by Nature Portfolio, Springer Nature, or any journal publisher.

The skills are intended to support scientific self-review, manuscript improvement, and research-quality control. They should not be treated as editorial decisions, peer-review outcomes, or publication guarantees.
