# Distillation sufficiency

This skill stores abstract reviewer memory rather than raw peer-review text. The v1.0 pattern set is intended to support claim-dependent atmospheric-science review, not to reproduce any individual review report.

## Corpus-to-skill conversion

- Public Peer Review Files used as corpus inputs: 35.
- Candidate reviewer-comment units extracted for internal indexing: 1807.
- Released abstract reviewer patterns: 56.
- Raw Peer Review File PDFs in this release: no.
- Long original reviewer comments in this release: no.

## Gate support profile

The strongest corpus support is associated with claim calibration, AI/weather-climate model fidelity, observational product and reanalysis validity, model assumptions and sensitivity, detail audit, sampling and representativeness, and scale-resolution consistency. These areas recur frequently in public Nature-family atmospheric review material and are central to the skill's default review behavior.

Moderate support is associated with aerosol-cloud-radiation, circulation mechanism and causality, and trend/signal detection. These gates are activated only when the manuscript's main claims depend on those pathways.

Compact support is associated with chemistry/emissions budget, extreme-event attribution, statistical uncertainty, and reproducibility. These gates remain included because they are critical atmospheric-review controls when triggered by the manuscript, but they should not dominate reports unless the paper's central evidence chain requires them.

See `reviewer_db/gate_counts.csv` for the gate-level support profile.

## Sufficiency judgment

The released pattern set is sufficient for v1.0 use when the skill is applied as a claim-dependent reviewer assistant. It is not a comprehensive database of all atmospheric-science reviewer behavior. The correct use is to identify the manuscript's central claims, activate the small number of materially relevant gates, and convert the resulting concerns into independent referee reports.

## Use limits

- Do not infer reviewer identities.
- Do not reproduce or redistribute raw peer-review text.
- Do not treat any gate as a universal checklist.
- Do not escalate a concern to major unless it affects a central claim, evidence chain, validation design, uncertainty treatment, mechanism, or reproducibility.
