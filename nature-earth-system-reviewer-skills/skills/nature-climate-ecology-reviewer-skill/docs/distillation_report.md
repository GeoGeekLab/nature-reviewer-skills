# Nature Climate Ecology Reviewer Skill v1.0 Distillation Report

## Corpus basis

The reviewer memory is based on a best-effort corpus of publicly accessible Nature Portfolio
peer-review files covering Climate sciences and Ecology. The package contains abstracted review
patterns, not raw reviewer comments or Peer Review PDFs.

## Corpus snapshot

- Source peer-review PDFs: 63
- Source articles represented in distilled units: 61
- Distilled reviewer-comment units: 5774
- Peer-review-corpus patterns: 100
- Conditional controversy-derived stress-test patterns: 12
- Total reviewer-memory patterns: 112
- Raw reviewer text included: no

## Gate system

The skill uses claim-dependent gate routing. Gates are applied only when the manuscript's own
claims trigger them. A gate is treated as major only when the central contribution depends on that
evidence layer.

Core gate families:

1. Contribution, novelty and related-work positioning.
2. Climate trend and attribution.
3. Carbon and nitrogen biogeochemistry.
4. Forest, land-use, restoration and conservation.
5. Biodiversity, community structure and ecosystem function.
6. Sampling design and representativeness.
7. Observational product and proxy uncertainty.
8. Model assumptions, validation and sensitivity.
9. Statistical inference and uncertainty.
10. Mechanism and causal explanation.
11. Policy, management and decision-scale claims.
12. Reproducibility, data and code availability.
13. Generalist clarity, figures and micro-consistency.

## Controversy-derived stress-test layer

A small conditional layer was abstracted from public Nature and Science article/comment metadata.
It covers recurrent failure modes in:

- tree-restoration and carbon-removal potential;
- dryland forest, woodland and savanna definitions;
- Amazon resilience, tipping-point and critical-transition inference;
- soil organic carbon and microbial carbon-use-efficiency model uncertainty;
- safe/just Earth-system boundary and threshold definitions;
- biodiversity time-series scale, richness, composition and turnover interpretation.

This layer is designed as a reviewer-sensitivity aid. It should not be cited or applied unless the
manuscript triggers a similar evidence-chain risk.

## Review format

The default output follows public Nature Portfolio Peer Review File conventions:

```text
Reviewer Reports on the Initial Version:
Referees' comments:
Referee #1 (Remarks to the Author):
Referee #2 (Remarks to the Author):
Referee #3 (Remarks to the Author):
```

The three referee sections should have distinct emphases and should not read as identical checklist
outputs.

## Copyright and identity boundary

- No raw reviewer comments are included.
- No Peer Review PDFs are redistributed in this skill package.
- No attempt is made to identify anonymous reviewers.
- All reviewer memory content is abstracted into issue types, evidence expectations, routing rules
  and non-verbatim stress-test patterns.
