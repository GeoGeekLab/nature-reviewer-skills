# Evaluation protocol

Scientific review quality cannot be established by package tests or by a public synthetic benchmark alone. This repository therefore separates three levels of evidence.

## Level 1 — software regression fixtures

The legacy synthetic cases under `benchmarks/cases/` test loading, scoring, severity normalization, evidence anchors, and panel deduplication. They are not a scientific performance benchmark.

## Level 2 — controlled diagnostic benchmark

[Controlled Review Diagnostic v1](../benchmarks/controlled_v1/) uses matched counterfactual synthetic excerpts to test targeted scientific issue detection.

Each challenge contains:

- one positive case with one pre-specified evidence failure;
- one matched negative control in which that failure is repaired or the claim is narrowed;
- a methodological source basis;
- one pre-specified major gold concern for the positive case.

This design measures both sensitivity and restraint. A reviewer that flags every possible problem should lose specificity on the controls.

The primary CRD-v1 endpoints are:

- **essential-issue recall** on positive cases;
- **negative-control specificity** — fraction of controls with no benchmark-coded false-positive concern;
- **essential balanced accuracy** — mean of essential-issue recall and specificity;
- **matched-pair pass rate** — fraction of pairs where the target problem is detected in the positive case and no benchmark concern is emitted for the matched control.

Secondary endpoints include micro precision/F1, severity agreement, evidence-anchor coverage, panel duplication, and run-to-run stability.

Uncertainty is reported using bootstrap resampling at the **matched pair** level. Pair members must remain together during resampling because they are not independent observations.

CRD-v1 gold labels are developer-authored controlled labels. They are useful for method development and regression testing, but are not independent expert gold.

## Level 3 — held-out expert evaluation

A credible claim about real manuscript-review quality requires an evaluation set that is separate from skill development and inaccessible during model/prompt development.

Recommended data include authorized manuscript excerpts or full manuscripts spanning:

- genuine scientific vulnerabilities;
- clean negative controls;
- deliberately perturbed counterfactuals;
- accepted and rejected work where use is authorized;
- multiple domains and claim types.

Gold concerns should contain an issue identifier, severity, evidence anchors, acceptable equivalent formulations, and whether the issue is essential.

Use at least two independent domain experts. Record pre-adjudication labels, adjudication decisions, and agreement statistics such as Cohen's kappa or Krippendorff's alpha where applicable.

## Blinded system comparison

For a generic-prompt versus domain-skill comparison:

1. pre-register models, versions, prompts, inference parameters, tools, number of runs, and endpoints;
2. use the same base model and manuscript text in both arms;
3. expose only the frozen condition prompt and manuscript text; expose the domain skill only in the skill-assisted arm;
4. hide case metadata, pair membership, gold labels, issue IDs, and source keys from the tested model;
5. randomize case order;
6. preserve raw outputs before coding;
7. have annotators code concerns independently after inference;
8. use paired resampling for system-to-system confidence intervals.

See [CRD-v1 RUN_PROTOCOL.md](../benchmarks/controlled_v1/RUN_PROTOCOL.md) and [ANNOTATION_PROTOCOL.md](../benchmarks/controlled_v1/ANNOTATION_PROTOCOL.md).

## Additional metrics for expert evaluation

A held-out study should also measure:

- concern precision and false-positive burden;
- severity macro-F1 or weighted agreement;
- evidence-anchor validity;
- unsupported-citation rate;
- duplicate-concern rate across panel members;
- human usefulness and actionability;
- run-to-run stability;
- calibration where the system emits confidence.

Report results by domain with uncertainty. Do not pool domains in a way that hides failure in a low-volume specialty.

## Interpretation

Public CRD-v1 performance should be described as **public synthetic development-set performance**. Because the cases and gold metadata are public, benchmark contamination is possible for future models.

Neither CRD-v1 nor the scorer oracle establishes:

- expert equivalence;
- editorial decision accuracy;
- novelty assessment quality;
- literature-review completeness;
- performance on full-length multimodal manuscripts;
- prospective impact on manuscript acceptance or scientific correctness.
