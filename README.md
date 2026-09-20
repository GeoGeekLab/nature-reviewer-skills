<h1 align="center">Nature Reviewer Skills</h1>

<p align="center"><strong>Find the evidence bug before peer review does.</strong></p>

<p align="center">Nature-style scientific review for claims, controls, validation, uncertainty, mechanism, and generalization.</p>

<p align="center">
  <a href="https://github.com/GeoGeekLab/nature-reviewer-skills/actions/workflows/ci.yml"><img src="https://github.com/GeoGeekLab/nature-reviewer-skills/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/GeoGeekLab/nature-reviewer-skills/releases"><img src="https://img.shields.io/github/v/release/GeoGeekLab/nature-reviewer-skills" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python 3.10+"></a>
</p>

<p align="center">
  <a href="docs/ARCHITECTURE.md">Architecture</a> ·
  <a href="#included-reviewer-skills">Reviewers</a> ·
  <a href="#see-it-in-60-seconds">Failure cases</a> ·
  <a href="#what-has-actually-been-validated">Validation</a> ·
  <a href="docs/SECURITY.md">Security</a> ·
  <a href="CHANGELOG.md">Changelog</a> ·
  <a href="https://github.com/GeoGeekLab/nature-reviewer-skills/releases">Releases</a>
</p>

<p align="center">
  <img src="./assets/reffox/reffox-main.png" alt="RefFox — the evidence-first mascot for Nature Reviewer Skills" width="230">
</p>

<p align="center"><strong>Your paper has bugs. RefFox tries to find them.</strong><br>
<em>Suspicious by default. Evidence first.</em></p>

<p align="center">Domain-aware reviewer skills that stress-test scientific claims and turn evidence failures into actionable revision paths.</p>

<p align="center">
  <code>7 domain reviewers</code> ·
  <code>1 polar orchestrator</code> ·
  <code>644 reasoning patterns</code> ·
  <code>48 controlled cases</code> ·
  <code>24 matched pairs</code> ·
  <code>108 blinded outputs</code>
</p>

~~~text
claim → evidence → domain gate → failure mode → major concern → revision path
~~~

> **Core principle:** the stronger the claim, the stronger and more discriminating the evidence must be.

> This is an independent open-source project. It is not affiliated with Nature Portfolio or Springer Nature.

**[Meet RefFox →](assets/reffox/BRAND.md)**

## See it in 60 seconds

Three synthetic failures. Three domains. One question: **does the evidence actually support the claim?**

| Remote sensing | Chemistry | Engineering |
|---|---|---|
| ![RefFox checking controls](assets/reffox/reffox-control-check.png) | ![RefFox asking for stronger evidence](assets/reffox/reffox-evidence-please.png) | ![RefFox finding a scientific bug](assets/reffox/reffox-bug-found.png) |
| **BUG**: `trend ≠ sensor shift` | **BUG**: `peak area ≠ yield` | **BUG**: `human recovery ≠ autonomous` |
| Sensor transition can masquerade as a vegetation breakpoint. | Raw HPLC-UV area is not automatically comparable quantitative yield. | Human recovery and data-quality decisions break a “fully autonomous” claim. |
| **CHECK**: harmonization + independent validation | **CHECK**: calibrated quantification + response factors | **CHECK**: autonomy boundary + failure recovery |
| [Open case →](examples/remote-sensing-trend-harmonization/) | [Open case →](examples/chemistry-quantification-integrity/) | [Open case →](examples/engineering-autonomy-boundary/) |

Each case contains a **synthetic manuscript excerpt**, a **curated reference review**, and the reasoning behind the concern. These demonstrate intended reviewer behavior; they are not model-performance scores.

[Browse all examples →](examples/)

## What has actually been validated

Think of this as the project’s evidence stack. **PASS means executed/verified at that layer — not “AI reviewer proven superior.”**

| Layer | Artifact | Scale | Status | Claim ceiling |
|---|---|---:|---|---|
| Runtime | CI + package matrix | Python 3.10–3.13 + 8 reviewer packages | `PASS` | Repository installs, validates, and tests across the stated matrix |
| Controlled diagnostic | CRD-v1 | 48 cases / 24 matched pairs / 8 review groups | `PASS` | Scoring harness can test target detection + repaired-control specificity |
| Counterfactual controls | Matched negative controls | 24 repaired counterparts | `PASS` | Reviewer can be penalized for repeating a defect after it is repaired/narrowed |
| Uncertainty | Pair-cluster bootstrap | Matched-pair resampling | `PASS` | Confidence intervals can respect pair dependence |
| Blinded pilot protocol | 3 domains | 18 cases / 9 pairs / 3 repeats / 2 conditions | `LOCKED` | Comparison design is preregistered and reproducible |
| Formal inference | Generic vs skill-assisted | **108 outputs** = 54 + 54 | `PASS` | The blinded inference protocol was fully executed |
| Automated annotation | Condition-blinded AI annotation | Pilot outputs | `PROVISIONAL` | Exploratory analysis only; not independent expert validation |
| Generic-vs-skill effect | Performance comparison | — | `OPEN` | No published superiority claim yet |
| Human expert gold | Independent domain annotation | — | `OPEN` | No expert-equivalence claim |
| Real submissions | Prospective manuscripts | — | `OPEN` | No real-world generalization claim yet |

**Formal pilot domains:** remote sensing · chemistry · engineering

**Evidence trail:** [CRD-v1](benchmarks/controlled_v1/README.md) · [Pilot harness](benchmarks/pilot_v1/README.md) · [Preregistration](benchmarks/pilot_v1/PREREGISTRATION.md) · [Run protocol](benchmarks/controlled_v1/RUN_PROTOCOL.md) · [Evaluation protocol](docs/EVALUATION.md)

> **Boundary:** CRD-v1 is public, synthetic, and developer-authored. Oracle predictions are scorer/harness self-tests, not model-performance results. The 108 blinded outputs prove protocol execution, not that skill-assisted review is better. Independent expert validation and prospective real-manuscript evidence remain open.

## Quick start

### 1. Clone the repository

~~~bash
git clone https://github.com/GeoGeekLab/nature-reviewer-skills.git
cd nature-reviewer-skills
~~~

### 2. Load a reviewer skill

For basic agent use, you do **not** need to install the Python runtime first.

Point a `SKILL.md`-capable agent runtime at the full skill directory you want to use, or copy that directory into the skills location used by your runtime.

Example:

~~~text
nature-earth-system-reviewer-skills/
  skills/
    nature-remote-sensing-reviewer-skill/
      SKILL.md
      reviewer_db/
      references/
      templates/
~~~

Then ask the agent to use that reviewer:

~~~text
Use the remote-sensing reviewer skill to conduct a rigorous pre-submission review.

Identify the manuscript's central claims and test spatial independence, product validity,
uncertainty, validation design, transferability, alternative explanations, and whether
the conclusions exceed the evidence.

For each major concern, anchor the criticism to manuscript evidence and give a concrete
revision path.
~~~

> Runtime note: installation paths differ across agent systems. The repository is designed around `SKILL.md` packages; runtime-specific compatibility should be treated as tested only when that runtime has been explicitly validated.

### 3. Optional: install the shared Python runtime

Install this when you want the repository's validation, retrieval, extraction, or evaluation CLI tooling.

Core runtime:

~~~bash
python -m pip install -e .
~~~

Add PDF/DOCX extraction support:

~~~bash
python -m pip install -e ".[documents]"
~~~

Development tools:

~~~bash
python -m pip install -e ".[dev]"
~~~

### 4. Optional: validate the repository

~~~bash
python scripts/sync_skill_assets.py
python scripts/validate_all.py
python -m pytest
~~~

## Why not use a generic reviewer prompt?

| Generic review prompt | Nature Reviewer Skills |
|---|---|
| Broad criticism across many dimensions | Claim-dependent, domain-specific evidence gates |
| Often treats all concerns similarly | Distinguishes central scientific risks from local issues |
| May criticize without locating the evidence | Requires evidence anchors when manuscript content is available |
| Generic reproducibility and statistics checks | Discipline-specific failure modes such as spatial leakage, gauge representativeness, purity, benchmark fairness, or operating-envelope limits |
| Usually one undifferentiated voice | Supports complementary reviewer roles and panel deduplication |
| Can stop at criticism | Requires a revision direction for major concerns |

The intended advantage is **domain-specific evidence stress testing**, not simply a longer review.

## Included reviewer skills

### Earth-system science

| Reviewer | Typical stress tests |
|---|---|
| [Remote sensing](nature-earth-system-reviewer-skills/skills/nature-remote-sensing-reviewer-skill/) | spatial leakage, product validity, mixed pixels, QA screening, independent validation, uncertainty propagation, out-of-domain transfer |
| [Atmospheric science](nature-earth-system-reviewer-skills/skills/nature-atmospheric-science-reviewer-skill/) | observation-model consistency, attribution, scale mismatch, forcing assumptions, internal variability, extremes |
| [Hydrology](nature-earth-system-reviewer-skills/skills/nature-hydrology-reviewer-skill/) | water balance, gauge representativeness, calibration/validation separation, equifinality, event sampling, basin transfer |
| [Climate and ecology](nature-earth-system-reviewer-skills/skills/nature-climate-ecology-reviewer-skill/) | confounding, mechanism, representativeness, driver separation, ecological scale, impact and policy overreach |

### Chemistry, engineering, and materials

| Reviewer | Typical stress tests |
|---|---|
| [Chemistry](nature-chemistry-reviewer-skill/) | identity and purity, discriminating controls, substrate scope, selectivity, mechanism, quantitative comparison |
| [Engineering](nature-engineering-reviewer-skill/) | requirement-design-validation coherence, benchmark fairness, robustness, failure modes, operating envelope, deployment claims |
| [Materials science](nature-materials-science-reviewer-skill/) | phase identity, characterization, structure-property relations, benchmark comparability, durability, processability, scalability |

### Polar Earth-System Review Orchestrator

The [Polar Earth-System Review Orchestrator](nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/) is an upper-layer coordinator, not an eighth foundational reviewer.

It routes Arctic, Antarctic, Southern Ocean, cryosphere, polar atmosphere/ocean, ecology, biogeochemistry, remote-sensing, paleoclimate, and instrumentation claims to the relevant domain reviewers; adds polar-specific evidence gates; assigns non-overlapping reviewer responsibilities; and consolidates the final review.

## What a major concern should contain

A strong concern should make the scientific logic inspectable:

1. **Claim under review**
2. **Evidence anchor** — figure, table, section, method, result, or explicit missing evidence
3. **Why it matters**
4. **Severity**
5. **Alternative explanation or failure mode**
6. **Actionable revision path**

A concern should be major only when it affects the central contribution or the reader's confidence in the evidence chain.

## What the review stress-tests

| Review target | Core question |
|---|---|
| Central claim | What is the strongest claim, and what evidence would be required to defend it? |
| Evidence chain | Do data, preprocessing, methods, validation, interpretation, and conclusion form a defensible chain? |
| Controls and baselines | Can the comparison distinguish the proposed explanation from plausible alternatives? |
| Validation | Is testing independent, representative, and aligned with the claimed operating domain? |
| Uncertainty | Are important measurement, model, sampling, and inferential uncertainties quantified and propagated? |
| Causality and mechanism | Does the evidence support mechanism or causality, or only association and consistency? |
| Generalization | Where does the evidence end, and where does extrapolation begin? |
| Novelty and significance | Is the contribution positioned against the strongest relevant prior work? |
| Reproducibility | Are methods, parameters, data, code, and reporting sufficient for verification? |
| Revision path | What additional evidence, analysis, control, or claim narrowing would resolve the concern? |

## How it works

~~~text
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
~~~

The reviewer-memory layer stores **abstracted, non-verbatim scientific reasoning patterns**, not copied referee reports. A pattern follows the logic:

~~~text
claim type → evidence risk → stress-test gate → reviewer concern → revision direction
~~~

## Evaluation protocol and evidence boundary

The compact status table near the top of this README is the current evidence summary. The repository keeps the underlying protocol and diagnostic artifacts inspectable rather than collapsing them into a single “AI reviewer score.”

[CRD-v1](benchmarks/controlled_v1/) is a source-backed **public development benchmark**. Every positive case has a matched negative control so a reviewer is rewarded for detecting a specific evidence failure and penalized for continuing to raise it after the failure has been repaired or the claim has been narrowed.

The benchmark contains **48 synthetic cases in 24 matched pairs across 8 review groups**. Controlled gold labels are developer-authored. The included oracle predictions are only scorer self-tests and must not be presented as model performance.

The preregistered three-domain pilot covers remote sensing, chemistry, and engineering. Its formal blinded inference run completed **108 outputs: 54 generic and 54 skill-assisted**, with 3 repeated runs per case. Those outputs remain evidence about execution until they are annotated and analyzed under the locked protocol.

Automated condition-blinded annotation is treated as **provisional analysis**, not independent human validation. A credible real-world performance claim still requires independent expert-labelled data, blinded annotation/adjudication, confidence intervals, per-domain error analysis, and prospective evaluation on real submissions.

The evaluation framework supports essential-issue recall, target-specific negative-control specificity, balanced accuracy, concern precision, severity agreement, evidence anchors, panel duplication, matched-pair bootstrap uncertainty, and run-to-run stability.

See:

- [CRD-v1 benchmark card](benchmarks/controlled_v1/README.md)
- [Three-domain blinded pilot harness](benchmarks/pilot_v1/README.md)
- [Pilot preregistration](benchmarks/pilot_v1/PREREGISTRATION.md)
- [Blinded run protocol](benchmarks/controlled_v1/RUN_PROTOCOL.md)
- [Annotation protocol](benchmarks/controlled_v1/ANNOTATION_PROTOCOL.md)
- [Evaluation protocol](docs/EVALUATION.md)
- [Legacy synthetic benchmark report](benchmark-report.json)
- [Test report](TEST_REPORT.md)

## Reliability and defensive behavior

The shared runtime includes:

- typed Python models and validation;
- deterministic field-weighted BM25 retrieval;
- phrase boosts and query expansion;
- confidence reporting and diversity-aware selection;
- matrix CI and package validation;
- defensive PDF/DOCX/archive/path/size/page-count limits;
- checks intended to prevent fabricated citations, figures, page numbers, evidence, or misconduct allegations.

Technical details:

- [Architecture](docs/ARCHITECTURE.md)
- [Evaluation](docs/EVALUATION.md)
- [Security](docs/SECURITY.md)
- [Migration notes](docs/MIGRATION.md)
- [Changelog](CHANGELOG.md)

## Command-line tools

Search a skill's reviewer-pattern database:

~~~bash
nature-reviewer-search \
  --root nature-chemistry-reviewer-skill \
  --query "mechanism claim without discriminating controls" \
  --limit 5
~~~

Validate a package:

~~~bash
nature-reviewer-validate nature-chemistry-reviewer-skill
~~~

Evaluate structured predictions:

~~~bash
nature-reviewer-evaluate \
  benchmarks/cases \
  benchmarks/predictions/example_predictions.jsonl
~~~

Extract manuscript text with anchors and defensive limits:

~~~bash
python nature-chemistry-reviewer-skill/scripts/extract_text_with_anchors.py \
  manuscript.pdf \
  --output extracted.jsonl
~~~

## Repository layout

~~~text
src/nature_reviewer_core/                 shared runtime
scripts/                                  repository-wide validation and sync commands
tests/                                    shared-runtime tests
examples/                                 60-second curated review demonstrations
benchmarks/                               benchmark schemas and fixtures

nature-earth-system-reviewer-skills/
  skills/
    nature-remote-sensing-reviewer-skill/
    nature-atmospheric-science-reviewer-skill/
    nature-hydrology-reviewer-skill/
    nature-climate-ecology-reviewer-skill/
    polar-earth-system-review-orchestrator/

nature-chemistry-reviewer-skill/
nature-engineering-reviewer-skill/
nature-materials-science-reviewer-skill/
~~~

The current layout reflects the project's history. A future migration may normalize all domain reviewers under one top-level `skills/` directory; paths should not be changed casually because agent integrations may already depend on them.

## Who it is for

- researchers preparing manuscripts for selective journals;
- principal investigators running internal pre-submission review;
- graduate students learning evidence-centered scientific criticism;
- research teams building manuscript quality-control workflows;
- editors and reviewers structuring an initial claim-evidence audit;
- agent developers building domain-aware scientific review systems.

## Important limitations

Nature Reviewer Skills is a **research-assistance and quality-control system**.

It is not:

- a replacement for qualified domain experts;
- an editorial decision system;
- a guarantee of acceptance;
- evidence that a manuscript is scientifically correct;
- a tool for making unsupported research-misconduct allegations;
- an official Nature Portfolio or Springer Nature product.

Figures, spectra, equations, maps, chemical structures, and other visual evidence require a multimodal runtime capable of inspecting the original manuscript content.

The current public benchmark fixtures validate software and evaluation infrastructure. Independent expert gold sets, blinded manuscript studies, calibration, and prospective evaluation are still needed before making strong claims about review quality.

## Provenance and copyright boundary

The reviewer-memory databases contain generalized, non-verbatim reasoning patterns distilled from public peer-review materials and domain evidence standards.

The repository does not redistribute raw referee reports, identifiable reviewer language, private review material, or full copyrighted manuscripts.

See the package-level provenance files and [security documentation](docs/SECURITY.md) for additional details.

## Contributing

Useful contributions include:

- expert-annotated benchmark cases;
- false-positive and negative-control cases;
- new disciplinary reviewer skills;
- stronger domain evidence gates;
- retrieval and deduplication improvements;
- documentation and reproducibility improvements.

Behavior-changing contributions should add or update benchmark cases.

Scientific benchmark gold labels require at least two domain experts, an adjudication record, and inter-rater agreement reporting.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE).

---

**Stress-test the evidence before reviewers stress-test the paper.**
