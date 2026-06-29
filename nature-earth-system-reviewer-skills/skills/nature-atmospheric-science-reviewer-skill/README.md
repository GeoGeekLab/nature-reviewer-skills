# Nature Atmospheric Science Reviewer Skill

![License: MIT OR Apache-2.0](https://img.shields.io/badge/License-MIT%20OR%20Apache--2.0-yellow.svg) ![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue) ![Status](https://img.shields.io/badge/status-v1.0.1-green) ![Domain](https://img.shields.io/badge/domain-atmospheric%20science-brightgreen) ![Repo Size](https://img.shields.io/github/repo-size/GeoGeekLab/nature-atmospheric-science-reviewer-skill)

A Nature-style reviewer skill for rigorous evaluation of atmospheric-science manuscripts.

Distilled from publicly available Nature and Nature Communications peer-review files, it helps researchers stress-test manuscripts against high-level reviewer concerns using review-pattern distillation, evidence-chain checks, and referee-style reasoning before submission or revision.

> This project is not affiliated with Nature Portfolio. It does not include raw peer-review PDFs or reproduce copyrighted review reports.

## What this skill does

This skill helps researchers conduct a strict, journal-level review of atmospheric-science manuscripts. It focuses on observational representativeness, reanalysis and model dependence, circulation mechanisms, aerosol-cloud-radiation interactions, extreme-event attribution, AI weather or climate claims, uncertainty, and claim calibration.

It is especially useful for:

- pre-submission review of atmospheric observation, reanalysis, model, and satellite studies;
- major revision preparation for aerosol, cloud, radiation, circulation, and extreme-event papers;
- stress-testing AI weather, climate-model, and attribution claims;
- checking whether atmospheric mechanisms are demonstrated rather than only described;
- improving the evidential defensibility of atmospheric-science manuscripts.

## Key capabilities

- Generates Nature-style referee reports.
- Reviews main manuscripts and supplementary materials together.
- Identifies weaknesses in observational support, reanalysis dependence, model physics, mechanism tests, attribution design, uncertainty, novelty, and reproducibility.
- Checks whether circulation, forcing, aerosol-cloud-radiation, and extreme-event claims are supported by the correct evidence chain.
- Provides locatable comments tied to sections, figures, tables, equations, or supplementary diagnostics when available.
- Can compare the manuscript with closely related published work when literature search is available and permitted.
- Can generate both Markdown and Word review outputs in file-capable environments.

## Repository structure

```text
nature-atmospheric-science-reviewer-skill/
├─ README.md
├─ SKILL.md
├─ MANIFEST.json
├─ LICENSE
├─ LICENSE-APACHE
├─ LICENSE-MIT
├─ reviewer_db/
├─ references/
├─ templates/
├─ examples/
├─ scripts/
└─ tests/
```

## Installation

Codex skills are installed as folders containing a `SKILL.md` file. The folder name should be stable and easy to invoke.

### Option 1: User-level installation

Use this option if you want the skill available across all projects.

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/GeoGeekLab/nature-atmospheric-science-reviewer-skill.git ~/.agents/skills/nature-atmospheric-science-reviewer
```

Expected structure:

```text
~/.agents/skills/nature-atmospheric-science-reviewer/SKILL.md
~/.agents/skills/nature-atmospheric-science-reviewer/reviewer_db/
~/.agents/skills/nature-atmospheric-science-reviewer/references/
~/.agents/skills/nature-atmospheric-science-reviewer/templates/
~/.agents/skills/nature-atmospheric-science-reviewer/scripts/
```

### Option 2: Project-level installation

Use this option if you want the skill available only inside one manuscript project.

```text
your-manuscript-project/
├─ manuscript.docx
├─ supplementary.docx
└─ .agents/
   └─ skills/
      └─ nature-atmospheric-science-reviewer/
         ├─ SKILL.md
         ├─ reviewer_db/
         ├─ references/
         ├─ templates/
         └─ scripts/
```

Clone into the project-level skill directory:

```bash
mkdir -p .agents/skills
git clone https://github.com/GeoGeekLab/nature-atmospheric-science-reviewer-skill.git .agents/skills/nature-atmospheric-science-reviewer
```

## Windows installation

For Windows PowerShell, user-level installation can be done with:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
git clone https://github.com/GeoGeekLab/nature-atmospheric-science-reviewer-skill.git "$env:USERPROFILE\.agents\skills\nature-atmospheric-science-reviewer"
```

Expected structure:

```text
%USERPROFILE%\.agents\skills\nature-atmospheric-science-reviewer\SKILL.md
%USERPROFILE%\.agents\skills\nature-atmospheric-science-reviewer\reviewer_db\
%USERPROFILE%\.agents\skills\nature-atmospheric-science-reviewer\references\
%USERPROFILE%\.agents\skills\nature-atmospheric-science-reviewer\templates\
%USERPROFILE%\.agents\skills\nature-atmospheric-science-reviewer\scripts\
```

## Optional validation

After installation, you can validate the package:

```bash
python ~/.agents/skills/nature-atmospheric-science-reviewer/scripts/validate_package.py --root ~/.agents/skills/nature-atmospheric-science-reviewer
```

On Windows PowerShell:

```powershell
python "$env:USERPROFILE\.agents\skills\nature-atmospheric-science-reviewer\scripts\validate_package.py" --root "$env:USERPROFILE\.agents\skills\nature-atmospheric-science-reviewer"
```

## Using the skill in Codex CLI

Open a terminal in the manuscript project directory:

```bash
cd path/to/your/manuscript-project
codex
```

Inside Codex CLI, select the skill:

```text
/skills
```

Choose:

```text
nature-atmospheric-science-reviewer
```

Then ask Codex to review the manuscript:

```text
Use $nature-atmospheric-science-reviewer to review the uploaded files.
```

If the files are already in the project directory, you can be more specific:

```text
Use $nature-atmospheric-science-reviewer to review manuscript.docx and supplementary.docx. Treat manuscript.docx as the main paper and supplementary.docx as supplementary material.
```

## Using the skill in Codex GUI / App

1. Open the manuscript project in Codex GUI / App.
2. Upload or reference the main manuscript, supplementary materials, figures, tables, or appendices.
3. Invoke the skill:

```text
Use $nature-atmospheric-science-reviewer to review the uploaded files.
```

You can also type:

```text
/skills
```

or start typing:

```text
$nature
```

to check whether the skill is available.

If the skill does not appear, check that `SKILL.md` is located directly inside the installed skill folder, then restart Codex.

## Recommended input files

The skill can work with one or more files, for example:

```text
manuscript.docx
supplementary.docx
appendix.pdf
figures.pdf
tables.xlsx
response_letter.docx
```

If multiple files are provided, the skill will infer their roles as main manuscript, supplementary material, figures, tables, appendices, or supporting files.

## Expected output

In a file-capable environment, the skill writes:

```text
review_outputs/nature_review_report.md
review_outputs/nature_review_report.docx
```

It also prints the Markdown version of the review in the chat for immediate reading, copying, and revision.

## Example prompt

```text
Use $nature-atmospheric-science-reviewer to review the uploaded files.

Please produce a Nature-style referee report. Treat the main manuscript as the primary paper and all other files as supplementary or supporting materials. Save the review as both Markdown and Word.
```

For a shorter prompt:

```text
Use $nature-atmospheric-science-reviewer to review the uploaded files.
```

## Review style

The skill produces reviewer-style reports rather than language-polishing feedback. A typical report includes:

```text
Reviewer Reports on the Initial Version:
Referees' comments:

Referee #1 (Remarks to the Author):
...

Referee #2 (Remarks to the Author):
...

Referee #3 (Remarks to the Author):
...
```

The report may include:

- major concerns;
- figure-, diagnostic-, section-, equation-, or supplement-specific comments;
- novelty and prior-work positioning;
- observation, reanalysis, model, and retrieval validity concerns;
- mechanism, attribution, and uncertainty concerns;
- reproducibility and data/code availability concerns;
- editorial-level suitability comments when atmospheric evidence does not support the claimed contribution.

## Notes on literature search

When web or literature search is available and permitted, the skill may compare the manuscript with closely related published work to evaluate novelty, methodological positioning, and evidence strength.

If literature search is unavailable or prohibited, the skill should not invent references. It will base the review only on the provided manuscript files and clearly state the evidence boundary.

## Citation and copyright policy

This repository contains distilled review patterns and workflow instructions. It does not include raw peer-review PDFs and does not reproduce full copyrighted review reports.

Users should cite or acknowledge the repository when reusing or adapting the skill in their own research workflows.

## Disclaimer

This skill is an independent research-assistance tool. It is not affiliated with Nature Portfolio, Springer Nature, or any journal. It does not provide official editorial decisions. Its output should be treated as a rigorous pre-submission or revision-stage review aid.
