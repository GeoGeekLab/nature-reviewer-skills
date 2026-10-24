<h1 align="center">Nature Reviewer Skills</h1>

<p align="center">Better questions. Stronger manuscripts.</p>

<p align="center">
  <a href="https://github.com/GeoGeekLab/nature-reviewer-skills/actions/workflows/ci.yml"><img src="https://github.com/GeoGeekLab/nature-reviewer-skills/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/GeoGeekLab/nature-reviewer-skills/releases"><img src="https://img.shields.io/github/v/release/GeoGeekLab/nature-reviewer-skills" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python 3.10+"></a>
</p>

<p align="center">
  <a href="#meet-the-reviewers">Reviewers</a> ·
  <a href="#see-it-in-60-seconds">Examples</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#what-has-been-validated">Validation</a> ·
  <a href="docs/ARCHITECTURE.md">Architecture</a> ·
  <a href="docs/SECURITY.md">Security</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <img src="./assets/reffox/reffox-main.png" alt="RefFox, the Nature Reviewer Skills mascot" width="230">
</p>

<p align="center"><strong>Meet RefFox: sharper questions, clearer revisions.</strong></p>

Here's the thing: A thoughtful scientific review does more than identify concerns. It helps you see which questions matter most — and what to improve next.

Before submitting a paper, you want to know whether its central claims match the methods, controls, results, and validation. You also want to understand how a specialist might challenge the mechanism, uncertainty, or scope of those claims.

**Nature Reviewer Skills** brings that review process into your AI-assisted writing workflow. It is an open-source collection of domain-aware [Agent Skills](https://agentskills.io/) that examines scientific claims, asks discipline-specific questions, and turns major concerns into practical revision paths.

The goal? **Help you strengthen the scientific argument before submission.**

<p align="center">
  <code>7 domain reviewers</code> ·
  <code>1 polar orchestrator</code> ·
  <code>644 reasoning patterns</code> ·
  <code>48 controlled cases</code> ·
  <code>24 matched pairs</code> ·
  <code>108 blinded outputs</code>
</p>

```text
research claim → domain-specific checks → scientific concern → revision path
```

---

## ⚡ What Can You Do With It?

Where are you in the manuscript process? Start with the question you want answered.

| Your task | How the skills help |
| :--- | :--- |
| **Review before submission** | Identify central claims and examine controls, validation, uncertainty, interpretation, and generalization. |
| **Find the most important revisions** | Separate major scientific concerns from local issues and connect each concern to a specific section, figure, or result. |
| **Check a specialist claim** | Apply review questions tailored to remote sensing, hydrology, chemistry, engineering, materials science, and other supported fields. |
| **Coordinate a broader review** | Combine complementary reviewer perspectives and consolidate overlapping concerns. |
| **Build a review workflow** | Use the shared Python tools for pattern search, document extraction, package validation, and structured evaluation. |

You can start with one reviewer skill and bring in others when your manuscript crosses disciplines.

---

## 🔎 See It in 60 Seconds

What does a domain-aware review actually catch? Consider these three synthetic manuscript examples.

| Field | Manuscript claim to examine | Key review question | Example |
| :--- | :--- | :--- | :--- |
| **Remote sensing** | A vegetation trend changes sharply at a particular date. | Could a sensor transition explain the apparent breakpoint? Check harmonization and independent validation. | [Open case →](examples/remote-sensing-trend-harmonization/) |
| **Chemistry** | HPLC-UV peak areas are used to compare product yields. | Are calibration and response factors sufficient for a quantitative comparison? | [Open case →](examples/chemistry-quantification-integrity/) |
| **Engineering** | A system is described as fully autonomous. | Which recovery and data-quality decisions still require human intervention? | [Open case →](examples/engineering-autonomy-boundary/) |

Each example includes a synthetic manuscript excerpt, a curated reference review, and the reasoning behind the concern.

[Browse all examples →](examples/)

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/GeoGeekLab/nature-reviewer-skills.git
cd nature-reviewer-skills
```

### 2. Load a reviewer skill

For a basic agent workflow, start with the skill directory. The shared Python runtime is optional.

Point a `SKILL.md`-capable agent at a complete skill directory, or copy that directory to the skill location supported by your agent. For example:

```text
nature-earth-system-reviewer-skills/
  skills/
    nature-remote-sensing-reviewer-skill/
      SKILL.md
      reviewer_db/
      references/
      templates/
```

Then give the agent a focused task:

```text
Use the remote-sensing reviewer skill to review this manuscript before submission.

Identify the central claims. Examine spatial independence, product validity,
uncertainty, validation design, transferability, and alternative explanations.

For each major concern, cite the relevant manuscript section, figure, or result.
Explain why the concern matters and propose a concrete revision path.
```

The skill-directory location depends on your agent runtime. Keep each skill's supporting files together.

### 3. Optional: install the Python runtime

Use the shared runtime for validation, retrieval, extraction, and evaluation commands.

Core installation:

```bash
python -m pip install -e .
```

Add PDF and DOCX extraction:

```bash
python -m pip install -e ".[documents]"
```

Add development tools:

```bash
python -m pip install -e ".[dev]"
```

### 4. Optional: run repository checks

```bash
python scripts/sync_skill_assets.py
python scripts/validate_all.py
python -m pytest
```

---

## 🧪 Meet the Reviewers

Different disciplines ask different questions. A convincing mechanism in chemistry needs different checks from a robust spatial trend in remote sensing.

That's why the collection has seven foundational domain reviewers.

### Earth-system science

| Reviewer | What it examines |
| :--- | :--- |
| [**Remote sensing**](nature-earth-system-reviewer-skills/skills/nature-remote-sensing-reviewer-skill/) | Spatial leakage, product validity, mixed pixels, QA screening, independent validation, uncertainty propagation, and transfer to new regions or conditions. |
| [**Atmospheric science**](nature-earth-system-reviewer-skills/skills/nature-atmospheric-science-reviewer-skill/) | Observation–model consistency, attribution, scale mismatch, forcing assumptions, internal variability, and extremes. |
| [**Hydrology**](nature-earth-system-reviewer-skills/skills/nature-hydrology-reviewer-skill/) | Water balance, gauge representativeness, calibration and validation separation, equifinality, event sampling, and basin transfer. |
| [**Climate and ecology**](nature-earth-system-reviewer-skills/skills/nature-climate-ecology-reviewer-skill/) | Confounding, mechanism, representativeness, driver separation, ecological scale, and the scope of impact or policy claims. |

### Chemistry, engineering, and materials

| Reviewer | What it examines |
| :--- | :--- |
| [**Chemistry**](nature-chemistry-reviewer-skill/) | Identity and purity, discriminating controls, substrate scope, selectivity, mechanism, and quantitative comparisons. |
| [**Engineering**](nature-engineering-reviewer-skill/) | Requirements, design and validation coherence, benchmark fairness, robustness, failure modes, operating envelopes, and deployment claims. |
| [**Materials science**](nature-materials-science-reviewer-skill/) | Phase identity, characterization, structure–property relations, benchmark comparability, durability, processability, and scalability. |

### Polar Earth-System Review Orchestrator

Working on the Arctic, Antarctic, Southern Ocean, or cryosphere? Your research may draw on several disciplines at once.

The [**Polar Earth-System Review Orchestrator**](nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/) coordinates the relevant reviewers. It routes polar atmosphere, ocean, ecology, biogeochemistry, paleoclimate, remote-sensing, and instrumentation claims to the right specialists; adds polar-specific checks; assigns complementary responsibilities; and combines the findings into a consolidated review.

It is **one coordinating skill**, alongside the seven foundational domain reviewers.

---

## 🧭 How Does a Review Work?

The process starts with the manuscript's central claims. Each claim is matched to relevant disciplinary checks and reviewer-reasoning patterns.

```text
                    Manuscript
                        |
                        v
                Find central claims
                        |
                        v
              Select domain reviewers
                        |
                        v
             Retrieve reasoning patterns
                        |
                        v
            Check controls and validation
           Examine mechanism and scope
                        |
                        v
              Write major concerns
                        |
                        v
           Consolidate + prioritize
                        |
                        v
                Propose revisions
```

The reviewer-memory layer contains **644 abstracted, non-verbatim scientific reasoning patterns**. They help the agent recognize recurring relationships between a claim, a scientific risk, a useful check, and a possible revision.

```text
claim type → scientific risk → review check → major concern → revision direction
```

### What makes a major concern useful?

A useful review comment helps you locate the issue and decide what to do next. Each major concern follows six components:

1. **Claim under review** — the statement being examined.
2. **Manuscript anchor** — the relevant figure, table, method, result, or section.
3. **Scientific importance** — why this issue affects the argument.
4. **Severity** — how strongly it affects the manuscript's main contribution.
5. **Alternative explanation or failure mode** — what else could account for the result.
6. **Revision path** — the analysis, control, clarification, or claim refinement that would address it.

The focus is on the questions that shape the manuscript's central contribution.

### What does it check?

| Review area | Guiding question |
| :--- | :--- |
| **Central claims** | What does the paper claim, and how do the methods and results support it? |
| **Controls and baselines** | Can the comparison separate the proposed explanation from plausible alternatives? |
| **Validation** | Are the tests independent, representative, and aligned with the intended use? |
| **Uncertainty** | Which measurement, model, sampling, and inferential uncertainties matter most? |
| **Causality and mechanism** | What do the results establish about association, mechanism, or causation? |
| **Generalization** | Which populations, settings, materials, or operating conditions fall within the findings' scope? |
| **Novelty and significance** | How does the contribution compare with the most relevant prior work? |
| **Reproducibility** | Can readers trace the methods, parameters, data, code, and reporting choices? |
| **Revision planning** | What should the authors analyze, clarify, validate, or reconsider next? |

---

## 📊 What Has Been Validated?

The project uses several layers of checking. Package tests examine the software and skill structure. Controlled cases test specific review behaviors. Blinded comparisons provide a framework for measuring generated reviews across conditions.

| Layer | Scope | Reported status |
| :--- | :--- | :--- |
| **Runtime and package checks** | Python 3.10–3.13; eight review packages; CI and validation | `PASS` |
| **CRD-v1 controlled cases** | 48 synthetic cases; 24 matched pairs; eight review groups | `PASS` |
| **Matched controls** | 24 repaired counterparts | `PASS` |
| **Uncertainty procedure** | Matched-pair / pair-cluster bootstrap | `PASS` |
| **Three-domain pilot protocol** | Remote sensing, chemistry, engineering; 18 cases; nine pairs; three repeats; two conditions | `LOCKED` |
| **Blinded inference execution** | 108 outputs: 54 generic and 54 skill-assisted | `PASS` |
| **Automated annotation** | Condition-blinded annotation of pilot outputs | `PROVISIONAL` |
| **Comparative performance analysis** | Generic vs. skill-assisted review quality | `OPEN` |
| **Independent expert labels** | Human domain-expert review | `OPEN` |
| **Real-manuscript evaluation** | Prospective submissions | `OPEN` |

The [test report](TEST_REPORT.md) also records **644 patterns**, **8/8 review packages validated**, and **18/18 root tests passed** for the reported repository checks.

### How the evaluation is organized

**CRD-v1** is a public development benchmark with 48 synthetic cases arranged into 24 matched pairs. Each pair includes a targeted scientific concern and a counterpart in which the issue has been addressed or the claim has been narrowed.

The preregistered three-domain pilot covers remote sensing, chemistry, and engineering. Its formal blinded inference run produced **108 outputs**, with 54 in each condition.

The evaluation framework tracks issue recall, negative-control specificity, balanced accuracy, precision of concerns, severity agreement, manuscript anchors, reviewer overlap, pair-cluster uncertainty, and stability across repeated runs.

Read the protocols and reports:

- [CRD-v1 benchmark card](benchmarks/controlled_v1/README.md)
- [Three-domain pilot harness](benchmarks/pilot_v1/README.md)
- [Pilot preregistration](benchmarks/pilot_v1/PREREGISTRATION.md)
- [Blinded run protocol](benchmarks/controlled_v1/RUN_PROTOCOL.md)
- [Annotation protocol](benchmarks/controlled_v1/ANNOTATION_PROTOCOL.md)
- [Evaluation protocol](docs/EVALUATION.md)
- [Legacy synthetic benchmark report](benchmark-report.json)
- [Test report](TEST_REPORT.md)

---

## 🛠️ Tools and Architecture

The domain skills provide scientific review instructions and reasoning patterns. The shared Python runtime supplies common tools for retrieval, extraction, validation, and evaluation.

Its components include typed Python models, deterministic field-weighted BM25 retrieval, phrase boosts, query expansion, confidence reporting, diversity-aware selection, package validation, and document-ingestion limits.

### Command-line tools

Search a skill's reviewer-pattern database:

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

Extract manuscript text with source anchors and input limits:

```bash
python nature-chemistry-reviewer-skill/scripts/extract_text_with_anchors.py \
  manuscript.pdf \
  --output extracted.jsonl
```

### Repository layout

```text
src/nature_reviewer_core/                 shared Python runtime
scripts/                                  repository-wide validation and sync
tests/                                    shared-runtime tests
examples/                                 synthetic review demonstrations
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
```

The directory paths reflect the project's current package layout. Keep these paths intact when connecting existing agent integrations.

For implementation details, see [Architecture](docs/ARCHITECTURE.md), [Evaluation](docs/EVALUATION.md), [Security](docs/SECURITY.md), [Migration notes](docs/MIGRATION.md), and the [Changelog](CHANGELOG.md).

---

## 👥 Who Is It For?

- **Researchers** preparing manuscripts for selective journals.
- **Principal investigators** organizing internal pre-submission review.
- **Graduate students** learning discipline-specific scientific criticism.
- **Research teams** building manuscript quality-control workflows.
- **Editors and reviewers** structuring an initial review of scientific claims.
- **Agent developers** creating domain-aware scientific review systems.

---

## 🤝 Contributing

Want to improve how scientific reviews work? Contributions are welcome in several areas:

- Expert-annotated benchmark cases and matched controls.
- New disciplinary reviewer skills and domain-specific checks.
- Better reasoning-pattern retrieval and review deduplication.
- Clearer documentation, evaluation methods, and reproducibility tooling.

Changes to reviewer behavior should include corresponding benchmark cases. Scientific gold-label benchmarks require at least two domain experts, an adjudication record, and inter-rater agreement reporting.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📜 Provenance and License

The reviewer-memory databases contain generalized, non-verbatim reasoning patterns developed from public peer-review materials and domain standards. See the package-level provenance records and [Security](docs/SECURITY.md) for documentation of the sources and safeguards.

Nature Reviewer Skills is an independent open-source project and is not affiliated with Nature Portfolio or Springer Nature.

Released under the [MIT License](LICENSE).

---

**“Work, Finish, Publish.”** — *Michael Faraday*
