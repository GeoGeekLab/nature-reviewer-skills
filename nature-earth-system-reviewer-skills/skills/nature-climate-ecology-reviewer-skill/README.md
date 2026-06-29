# Nature Climate Ecology Reviewer Skill

![License: MIT OR Apache-2.0](https://img.shields.io/badge/License-MIT%20OR%20Apache--2.0-yellow.svg) ![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue) ![Status](https://img.shields.io/badge/status-v1.0.1-green) ![Domain](https://img.shields.io/badge/domain-climate%20ecology-brightgreen) ![Repo Size](https://img.shields.io/github/repo-size/GeoGeekLab/nature-climate-ecology-reviewer-skill)

A Nature-style reviewer skill for rigorous evaluation of climate-ecology manuscripts.

Distilled from publicly available Nature and Nature Communications peer-review files, it helps researchers stress-test manuscripts against high-level reviewer concerns using review-pattern distillation, evidence-chain checks, and referee-style reasoning before submission or revision.

> This project is not affiliated with Nature Portfolio. It does not include raw peer-review PDFs or reproduce copyrighted review reports.

## What this skill does

This skill helps researchers conduct a strict, journal-level review of climate-ecology manuscripts. It focuses on ecological inference, climate exposure, biodiversity and ecosystem responses, carbon-cycle evidence, causal attribution, scale transfer, uncertainty, management relevance, and claim calibration.

It is especially useful for:

- pre-submission review of climate-change ecology, biodiversity, ecosystem, carbon-cycle, and conservation manuscripts;
- major revision preparation for climate-impact and ecological-attribution studies;
- stress-testing claims that connect environmental change to biological or ecosystem responses;
- checking whether management or policy implications follow from the evidence rather than from overgeneralization;
- improving the scientific defensibility of climate-ecology papers.

## Key capabilities

- Generates Nature-style referee reports.
- Reviews main manuscripts and supplementary materials together.
- Identifies weaknesses in sampling design, ecological inference, climate exposure metrics, confounding, attribution, uncertainty, novelty, and reproducibility.
- Checks whether species-, community-, ecosystem-, or carbon-cycle claims are supported at the scale being claimed.
- Provides detailed comments anchored to lines, pages, sections, figures, tables, or supplementary text when available.
- Can compare the manuscript with closely related published work when literature search is available and permitted.
- Can generate both Markdown and Word review outputs in file-capable environments.

## Repository structure

```text
nature-climate-ecology-reviewer-skill/
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
git clone https://github.com/GeoGeekLab/nature-climate-ecology-reviewer-skill.git ~/.agents/skills/nature-climate-ecology-reviewer
```

Expected structure:

```text
~/.agents/skills/nature-climate-ecology-reviewer/SKILL.md
~/.agents/skills/nature-climate-ecology-reviewer/reviewer_db/
~/.agents/skills/nature-climate-ecology-reviewer/references/
~/.agents/skills/nature-climate-ecology-reviewer/templates/
~/.agents/skills/nature-climate-ecology-reviewer/scripts/
```

### Option 2: Project-level installation

Use this option if you want the skill available only inside one manuscript project.

```text
your-manuscript-project/
├─ manuscript.docx
├─ supplementary.docx
└─ .agents/
   └─ skills/
      └─ nature-climate-ecology-reviewer/
         ├─ SKILL.md
         ├─ reviewer_db/
         ├─ references/
         ├─ templates/
         └─ scripts/
```

Clone into the project-level skill directory:

```bash
mkdir -p .agents/skills
git clone https://github.com/GeoGeekLab/nature-climate-ecology-reviewer-skill.git .agents/skills/nature-climate-ecology-reviewer
```

## Windows installation

For Windows PowerShell, user-level installation can be done with:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
git clone https://github.com/GeoGeekLab/nature-climate-ecology-reviewer-skill.git "$env:USERPROFILE\.agents\skills\nature-climate-ecology-reviewer"
```

Expected structure:

```text
%USERPROFILE%\.agents\skills\nature-climate-ecology-reviewer\SKILL.md
%USERPROFILE%\.agents\skills\nature-climate-ecology-reviewer\reviewer_db\
%USERPROFILE%\.agents\skills\nature-climate-ecology-reviewer\references\
%USERPROFILE%\.agents\skills\nature-climate-ecology-reviewer\templates\
%USERPROFILE%\.agents\skills\nature-climate-ecology-reviewer\scripts\
```

## Optional validation

After installation, you can validate the package:

```bash
python ~/.agents/skills/nature-climate-ecology-reviewer/scripts/validate_package.py --root ~/.agents/skills/nature-climate-ecology-reviewer
```

On Windows PowerShell:

```powershell
python "$env:USERPROFILE\.agents\skills\nature-climate-ecology-reviewer\scripts\validate_package.py" --root "$env:USERPROFILE\.agents\skills\nature-climate-ecology-reviewer"
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
nature-climate-ecology-reviewer
```

Then ask Codex to review the manuscript:

```text
Use $nature-climate-ecology-reviewer to review the uploaded files.
```

If the files are already in the project directory, you can be more specific:

```text
Use $nature-climate-ecology-reviewer to review manuscript.docx and supplementary.docx. Treat manuscript.docx as the main paper and supplementary.docx as supplementary material.
```

## Using the skill in Codex GUI / App

1. Open the manuscript project in Codex GUI / App.
2. Upload or reference the main manuscript, supplementary materials, figures, tables, or appendices.
3. Invoke the skill:

```text
Use $nature-climate-ecology-reviewer to review the uploaded files.
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
Use $nature-climate-ecology-reviewer to review the uploaded files.

Please produce a Nature-style referee report. Treat the main manuscript as the primary paper and all other files as supplementary or supporting materials. Save the review as both Markdown and Word.
```

For a shorter prompt:

```text
Use $nature-climate-ecology-reviewer to review the uploaded files.
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
- detailed line-, paragraph-, page-, figure-, or table-specific comments;
- novelty and prior-work positioning;
- sampling, exposure, confounding, and attribution concerns;
- ecological scale, mechanism, and management-relevance concerns;
- reproducibility and data/code availability concerns;
- editorial-level suitability comments when ecological evidence does not support broad climate or conservation claims.

## Notes on literature search

When web or literature search is available and permitted, the skill may compare the manuscript with closely related published work to evaluate novelty, methodological positioning, and evidence strength.

If literature search is unavailable or prohibited, the skill should not invent references. It will base the review only on the provided manuscript files and clearly state the evidence boundary.

## Citation and copyright policy

This repository contains distilled review patterns and workflow instructions. It does not include raw peer-review PDFs and does not reproduce full copyrighted review reports.

Users should cite or acknowledge the repository when reusing or adapting the skill in their own research workflows.

## Disclaimer

This skill is an independent research-assistance tool. It is not affiliated with Nature Portfolio, Springer Nature, or any journal. It does not provide official editorial decisions. Its output should be treated as a rigorous pre-submission or revision-stage review aid.
