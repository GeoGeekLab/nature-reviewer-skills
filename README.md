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

![RefFox — the evidence-first mascot for Nature Reviewer Skills](assets/reffox/reffox-main.png)

<p align="center"><strong>Your paper has bugs. RefFox tries to find them.</strong><br>
<em>Suspicious by default. Evidence first.</em></p>

Nature Reviewer Skills is not a grammar checker and not a generic “review my paper” prompt. It routes manuscript claims through discipline-specific evidence gates, retrieves relevant reviewer-reasoning patterns, and turns scientifically meaningful failures into evidence-anchored concerns with revision paths.

<p align="center"><code>7 domain reviewers</code> · <code>1 polar orchestrator</code> · <code>644 reasoning patterns</code> · <code>48 controlled cases</code> · <code>24 matched pairs</code> · <code>108 blinded outputs</code></p>

~~~text
claim → evidence → domain gate → failure mode → major concern → revision path
~~~

> **Core principle:** the stronger the claim, the stronger and more discriminating the evidence must be.

> This is an independent open-source project. It is not affiliated with Nature Portfolio or Springer Nature.

**[Meet RefFox →](assets/reffox/BRAND.md)**

## See it in 60 seconds

Three synthetic manuscript failures. Three domain reviewers. No installation required.

| Remote sensing | Chemistry | Engineering |
|---|---|---|
| **`trend ≠ sensor shift`** | **`peak area ≠ yield`** | **`human recovery ≠ autonomous`** |
| A vegetation-trend breakpoint is confounded with a sensor transition. | Raw HPLC-UV area is treated as quantitative yield across chemically different products. | Human fault recovery and data-quality decisions sit inside a system claimed to be fully autonomous. |
| [Open example →](examples/remote-sensing-trend-harmonization/) | [Open example →](examples/chemistry-quantification-integrity/) | [Open example →](examples/engineering-autonomy-boundary/) |

Each example contains a **synthetic manuscript excerpt**, a **curated reference review**, and the reasoning behind the concern. These are demonstrations of expected reviewer behavior, not benchmark performance results.

[Browse all examples →](examples/)

## What has actually been validated

The repository includes a controlled diagnostic benchmark, a preregistered blinded pilot, and full package/runtime validation. The status below separates **completed execution** from **scientific conclusions that are not yet established**.

| Evidence layer | Current status |
|---|---|
| Repository/runtime validation | ✅ Python 3.10–3.13 CI + 8 independent reviewer-package matrices |
| CRD-v1 controlled diagnostic | ✅ 48 synthetic cases / 24 matched counterfactual pairs / 8 review groups |
| Negative-control specificity design | ✅ Matched repaired controls + target-specific specificity scoring |
| Paired uncertainty analysis | ✅ Pair-cluster bootstrap confidence intervals supported |
| Three-domain blinded pilot protocol | ✅ 18 cases / 9 matched pairs / 3 repeats / 2 conditions |
| Formal blinded inference | ✅ **108 review outputs completed** — 54 generic + 54 skill-assisted |
| Condition-blinded automated annotation | 🧪 Provisional experiment; separate from v2.2.0 release claims |
| Published generic-vs-skill performance claim | ⏳ Not yet published |
| Independent human/domain-expert gold validation | ⬜ Not yet established |
| Prospective evaluation on real submissions | ⬜ Not yet established |

The formal pilot covers **remote sensing, chemistry, and engineering**. Completing 108 blinded outputs establishes that the comparison protocol was executed; it does **not** by itself establish that the skill-assisted condition performs better.

**Evidence trail:** [CRD-v1 benchmark card](benchmarks/controlled_v1/README.md) · [Pilot harness](benchmarks/pilot_v1/README.md) · [Pilot preregistration](benchmarks/pilot_v1/PREREGISTRATION.md) · [Run protocol](benchmarks/controlled_v1/RUN_PROTOCOL.md) · [Evaluation protocol](docs/EVALUATION.md)

> **Boundary:** CRD-v1 is public, synthetic, and developer-authored. Oracle predictions are scorer/harness self-tests, not model-performance results. Independent expert validation and prospective real-manuscript evidence are still required before making strong claims about review quality.

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
