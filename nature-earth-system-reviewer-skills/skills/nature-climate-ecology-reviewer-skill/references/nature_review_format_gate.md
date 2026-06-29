# Nature review format gate

## Purpose

Produce an author-facing referee report that resembles public Nature Portfolio peer-review files in structure and level of detail without copying any real reviewer text.

## Default report shape

Use 2-4 independent referees. Use 3 by default. Use 2 only for narrow manuscripts. Use 4 when the manuscript spans distinct domains that require separate methodological, ecological, climatic, or applied expertise.

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

## Referee distribution

- Referee #1: contribution, novelty, related-work positioning, scope and claim-evidence alignment.
- Referee #2: data, sampling, validation, modelling, statistics, robustness and uncertainty.
- Referee #3: mechanism, interpretation, ecological or policy implications, reproducibility and detail integrity.
- Referee #4, when needed: additional domain expertise, cross-scale synthesis, high-stakes applied interpretation, or data/code audit.


## Voice standard

Apply `referee_voice_style_gate` when writing the final report. The report should be balanced, evidence-centred, precise, and revision-oriented. Each major comment should connect the concern to claim strength, interpretation, uncertainty, novelty, reproducibility, or scope.

## Required elements

- State the submitted-material boundary briefly before the referee reports or in the opening sentence of Referee #1.
- Recognize the manuscript's plausible contribution briefly.
- Put decision-relevant concerns early within each referee report.
- Use direct judgment when a claim is not established.
- Include locatable comments when page, paragraph, figure, table, method, supplement, or data/code anchors are available.
- Include claim-language calibration for overextended wording.
- Include a compact editorial tendency only when requested or clearly useful.

## Do not expose internal machinery

Do not put the following in the author-facing report unless the user explicitly asks for diagnostics:

- gate routing tables;
- global major-concern matrices;
- decision-threshold tables;
- detail-audit tables;
- reviewer-memory or pattern IDs;
- implementation notes about the skill.

## File-output mode

When the user asks for files, deliver both:

- a Markdown `.md` report;
- a Word `.docx` report rendered from the same content.

The `.docx` should be visually checked after rendering.

## Avoid

- generic comments that could apply to any paper;
- identical structure across referees;
- invented line numbers or unsupported literature claims;
- long minor-comment lists that obscure central evidence gaps;
- soft phrasing when the evidence does not support the claim;
- a single report organized only as Major concern 1, Major concern 2, etc.
