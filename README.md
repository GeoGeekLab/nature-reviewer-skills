# nature-reviewer-skills

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)
![Status](https://img.shields.io/badge/Status-Research%20Skill%20Suite-brightgreen)

A research-grade suite of Nature-style scientific reviewer skills, distilled from public peer-review reasoning patterns and organized as domain-specific, independently installable skill packages.

This repository is built around one premise:

> High-level scientific review is not a checklist.
> It is a disciplined stress test of claims, evidence chains, uncertainty, novelty, mechanism, and scope.

`nature-reviewer-skills` provides a structured skill system for pre-submission manuscript review, scientific claim auditing, reviewer-perspective simulation, and research-quality improvement across Earth system science, chemistry, engineering, and materials science.

It is not a journal, not a referee replacement, and not an official Nature Portfolio product. It is a research-oriented skill suite for making manuscripts more falsifiable, more evidence-aligned, and more resistant to high-level peer-review failure.

---

## Why this repository exists

Most manuscript feedback tools operate at the surface layer: writing polish, structure, grammar, or generic review checklists.

Top-tier scientific reviewing operates at a different level.

It asks:

* What is the strongest claim in the paper?
* What evidence chain is required for that claim to be defensible?
* Which assumptions silently carry the conclusion?
* Where does validation stop and extrapolation begin?
* Are uncertainty, failure modes, controls, baselines, and alternative explanations treated as first-class scientific objects?
* Does the manuscript demonstrate what it claims, or only something narrower?

This repository treats peer review as a form of **scientific reasoning distillation**. The goal is to convert recurring high-level reviewer logic into reusable, domain-aware, claim-dependent skills.

The result is a suite of reviewer systems that do not merely ask whether a manuscript is well written. They ask whether the manuscript is scientifically overclaiming.

---

## Core idea: reviewer reasoning distillation

The skills in this suite are designed around abstracted reviewer memory.

That means the repository does not redistribute raw peer-review PDFs, long reviewer reports, or identifiable reviewer language. Instead, it preserves generalized reviewer reasoning patterns:

```text
claim type → evidence risk → stress-test gate → reviewer concern → revision direction
```

For example, a reviewer memory pattern is not stored as a copied reviewer paragraph. It is distilled into a reusable scientific logic unit:

```text
If a manuscript makes a broad spatial, temporal, mechanistic, or application claim,
test whether the validation design actually spans the claimed domain.
If the evidence is narrower than the conclusion, request either stronger validation
or a narrower claim.
```

This distinction is central to the project.

The suite is intended to encode review intelligence, not reproduce reviewer text.

---

## Suite architecture

```text
nature-reviewer-skills/
├── nature-earth-system-reviewer-skills/
│   └── skills/
│       ├── nature-remote-sensing-reviewer-skill/
│       ├── nature-atmospheric-science-reviewer-skill/
│       ├── nature-hydrology-reviewer-skill/
│       └── nature-climate-ecology-reviewer-skill/
├── nature-chemistry-reviewer-skill/
├── nature-engineering-reviewer-skill/
└── nature-materials-science-reviewer-skill/
```

The Earth-system repository is an umbrella distribution layer. It does not collapse the four Earth-system skills into a single mega-prompt.

Each skill remains independent:

* independent `SKILL.md`
* independent reviewer-memory patterns
* independent evidence gates
* independent templates
* independent scripts
* independent validation tests
* independent disciplinary review logic

The suite structure exists to support coordinated development, shared maintenance, and coherent distribution without erasing domain specificity.

---

## Included skills

### Earth system science

#### `nature-remote-sensing-reviewer`

For manuscripts involving satellite remote sensing, Earth observation products, geospatial machine learning, retrieval models, spatial validation, trend inference, uncertainty propagation, and large-scale environmental mapping.

Primary review stress tests include:

* product validity versus downstream scientific inference
* spatial and temporal validation sufficiency
* out-of-domain generalization
* leakage through geography, seasonality, or preprocessing
* uncertainty propagation from retrieval to conclusion
* distinction between optical proxy, geophysical variable, and causal interpretation

#### `nature-atmospheric-science-reviewer`

For manuscripts involving atmospheric observation, reanalysis, satellite retrievals, numerical modeling, weather and climate dynamics, aerosol-cloud-radiation interactions, atmospheric chemistry, extreme events, and AI weather or climate systems.

Primary review stress tests include:

* observation-model consistency
* attribution versus correlation
* reanalysis dependence
* scale mismatch between process and evidence
* aerosol-cloud-radiation causal ambiguity
* dynamical interpretation under uncertain forcing or boundary conditions

#### `nature-hydrology-reviewer`

For manuscripts involving hydrological processes, catchment response, river discharge, groundwater, drought, flood, water quality, water resources, hydrological extremes, and hydroclimatic attribution.

Primary review stress tests include:

* variable identity and hydrological meaning
* water balance closure
* scale transfer from station to basin
* precipitation anomaly versus drought
* concentration versus load
* model calibration, validation, equifinality, and transferability

#### `nature-climate-ecology-reviewer`

For manuscripts involving climate impacts, ecological response, carbon and nutrient cycles, biodiversity, ecosystem resilience, conservation inference, land-use change, and coupled climate-ecology systems.

Primary review stress tests include:

* causal inference under observational confounding
* spatial and temporal representativeness
* ecological mechanism versus statistical association
* carbon-cycle and biodiversity claim scope
* management implication versus evidence strength
* climate-driver separation and attribution uncertainty

### Other scientific domains

#### `nature-chemistry-reviewer-skill`

For manuscripts involving synthesis, catalysis, analytical chemistry, mechanistic chemistry, chemical biology, computational chemistry, and AI-enabled molecular discovery.

Primary review stress tests include:

* compound identity and purity
* controls and reproducibility
* reaction scope and selectivity
* catalyst performance metrics
* mechanistic evidence
* computational assumptions and experimental support

#### `nature-engineering-reviewer-skill`

For manuscripts involving devices, platforms, systems, robotics, biomedical engineering, environmental engineering, algorithms embodied in physical systems, and translational engineering claims.

Primary review stress tests include:

* requirement-design-validation coherence
* prototype versus platform overclaiming
* benchmark fairness
* real-world versus laboratory evidence
* failure modes and operating envelope
* engineering utility beyond demonstration

#### `nature-materials-science-reviewer-skill`

For manuscripts involving materials design, synthesis, processing, characterization, structure-property relationships, performance metrics, stability, degradation, and application-facing materials claims.

Primary review stress tests include:

* material identity and structural evidence
* synthesis-processing-property linkage
* benchmark comparability
* mechanism of performance
* durability and degradation
* application boundary and scalability

---

## What these skills do

Each skill is designed to produce a Nature-style pre-review of a manuscript.

The expected review does not simply summarize the paper. It actively interrogates:

```text
central claim
supporting evidence chain
validation design
controls and baselines
uncertainty and sensitivity
alternative explanations
mechanistic or causal interpretation
generalization boundary
novelty and significance
revision pathway
```

The default output is a set of independent referee-style reports, usually 2–4 reviewers, each with a distinct angle of attack. The reports are intended to resemble rigorous pre-submission review rather than editorial copyediting.

---

## Review philosophy

The skills follow several common principles.

### 1. Claim-dependent review

A manuscript should not be reviewed by applying the same checklist to every paper.

A paper claiming a new global trend, a new mechanism, a new catalyst, a new platform, or a new material property requires different evidence.

Each skill first asks what kind of claim the manuscript makes, then activates the corresponding review gates.

### 2. Evidence-chain stress testing

The central unit of review is not the paragraph. It is the evidence chain:

```text
data → preprocessing → model or experiment → validation → uncertainty → interpretation → claim
```

Weakness at any link can invalidate a strong conclusion.

### 3. Scope discipline

Many manuscripts fail because the conclusion is broader than the evidence.

The skills explicitly test whether claims should be supported, strengthened, narrowed, qualified, or reframed.

### 4. Domain specificity

Scientific rigor is not generic.

Remote sensing validation is not hydrological validation. Atmospheric attribution is not ecological association. Catalytic activity is not engineering utility. Materials performance is not application readiness.

Each skill carries its own domain gates and failure modes.

### 5. Revision-oriented criticism

The output should be critical but usable.

A strong review identifies not only what is wrong, but what evidence, analysis, control, sensitivity test, or claim narrowing would make the manuscript stronger.

---

## Repository structure

Each skill package follows a GitHub-ready structure:

```text
nature-*-reviewer-skill/
├── SKILL.md
├── README.md
├── MANIFEST.json
├── reviewer_db/
├── references/
├── templates/
├── scripts/
├── tests/
├── docs/
├── examples/
├── LICENSE
├── LICENSE-MIT
└── LICENSE-APACHE
```

Typical responsibilities:

| Path           | Purpose                                                                  |
| -------------- | ------------------------------------------------------------------------ |
| `SKILL.md`     | Main executable instruction file for the skill                           |
| `reviewer_db/` | Abstracted reviewer-memory patterns and domain gates                     |
| `references/`  | Provenance notes, source metadata, and non-verbatim reference structures |
| `templates/`   | Review report templates and output formats                               |
| `scripts/`     | Validation, rendering, extraction, and maintenance utilities             |
| `tests/`       | Package and behavior checks                                              |
| `docs/`        | Additional documentation                                                 |
| `examples/`    | Minimal examples and usage demonstrations                                |

---

## Installation

Clone the suite:

```bash
git clone https://github.com/GeoGeekLab/nature-reviewer-skills.git
cd nature-reviewer-skills
```

Install an individual skill by copying the desired skill folder into your skill runtime or Codex skill directory.

For example, for Earth-system skills:

```text
nature-earth-system-reviewer-skills/skills/nature-remote-sensing-reviewer-skill
nature-earth-system-reviewer-skills/skills/nature-atmospheric-science-reviewer-skill
nature-earth-system-reviewer-skills/skills/nature-hydrology-reviewer-skill
nature-earth-system-reviewer-skills/skills/nature-climate-ecology-reviewer-skill
```

For other domains:

```text
nature-chemistry-reviewer-skill
nature-engineering-reviewer-skill
nature-materials-science-reviewer-skill
```

---

## Validation

Each skill includes package-level validation scripts.

Example:

```bash
python nature-chemistry-reviewer-skill/scripts/validate_package.py nature-chemistry-reviewer-skill
python -m compileall -q nature-chemistry-reviewer-skill/scripts
python -m pytest -q nature-chemistry-reviewer-skill/tests
```

For Earth-system skills:

```bash
python nature-earth-system-reviewer-skills/scripts/validate_umbrella.py nature-earth-system-reviewer-skills
python -m compileall -q nature-earth-system-reviewer-skills/scripts
python -m pytest -q nature-earth-system-reviewer-skills/tests
```

A valid package should preserve:

* a readable `SKILL.md`
* consistent skill metadata
* expected repository structure
* reviewer-memory files without raw peer-review text
* runnable validation scripts
* template and output integrity

---

## Example use

A typical instruction to the skill runtime:

```text
Use nature-hydrology-reviewer to review this manuscript as if it were being evaluated for a Nature Portfolio journal. Focus on claim strength, hydrological validity, validation design, uncertainty, causality, and whether the conclusions exceed the evidence.
```

Another example:

```text
Use nature-materials-science-reviewer to perform a rigorous pre-submission review. Identify whether the structure-property claims, benchmark comparisons, stability evidence, and application claims are sufficiently supported.
```

---

## Intended users

This suite is designed for:

* researchers preparing high-level journal submissions
* graduate students learning how top-tier peer review thinks
* principal investigators seeking stronger internal pre-review
* scientific teams building manuscript quality-control workflows
* AI-assisted research systems that need domain-aware review logic
* developers building structured scientific-review agents

---

## What this repository is not

This repository is not:

* an official Nature Portfolio resource
* a replacement for real peer review
* a guarantee of acceptance
* a source of raw reviewer reports
* a corpus of redistributed peer-review PDFs
* a generic writing-polish prompt library
* a tool for imitating or identifying individual reviewers

The suite is intended for research-quality improvement and scientific reasoning support.

---

## Provenance and copyright boundary

The reviewer-memory layer is based on abstracted, non-verbatim reasoning patterns.

The repository is designed to avoid redistribution of:

* raw peer-review PDFs
* long reviewer comments
* identifiable reviewer language
* copyrighted reviewer reports
* full article text
* private or non-public review material

Only generalized review logic, domain gates, metadata, templates, and validation utilities are included.

---

## Design standard

A skill in this suite should satisfy four conditions:

1. **Scientifically specific**
   It should encode the evidence standards of its domain.

2. **Claim-dependent**
   It should route review pressure according to the manuscript’s central claims.

3. **Review-realistic**
   It should produce criticism that resembles serious expert peer review, not generic feedback.

4. **Revision-useful**
   It should help authors identify what to add, test, qualify, or remove.

---

## Roadmap

Potential future directions include:

* additional disciplinary reviewer skills
* stronger manuscript anchoring and evidence localization
* structured reviewer-memory schema evolution
* benchmark manuscripts for skill evaluation
* reproducible pre-review workflows
* richer DOCX / Markdown report generation
* cross-domain reviewer panels for interdisciplinary manuscripts

---

## License

This repository is released under the MIT License.

Individual skill packages may also include dual-license metadata where applicable. See the license files inside each package for package-level details.

---

## Disclaimer

This repository is an independent research and engineering project by GeoGeekLab.

It is not affiliated with, endorsed by, or approved by Nature Portfolio, Springer Nature, or any journal publisher.

The skills are intended to support scientific self-review, manuscript improvement, and research-quality control. They should not be treated as editorial decisions, peer-review outcomes, or publication guarantees.
