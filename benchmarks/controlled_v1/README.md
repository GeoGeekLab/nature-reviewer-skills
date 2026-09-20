# Controlled Review Diagnostic v1

Controlled Review Diagnostic (CRD-v1) tests whether a scientific reviewer detects a deliberately injected evidence failure **without inventing the same concern when that failure is repaired**.

## Scope

- 8 review groups: seven domain reviewers plus the Polar Earth-System Review Orchestrator.
- 3 challenge families per group.
- 24 matched counterfactual pairs.
- 48 synthetic manuscript excerpts: 24 positive cases and 24 negative controls.
- Exactly one primary gold concern per positive case.
- No real manuscripts, confidential reviews, or copied referee text.

CRD-v1 is a **public development benchmark**, not an expert-equivalence benchmark. Gold labels are developer-authored from controlled perturbations and methodological guidance. They have not yet been independently labelled by two domain experts.

## Why matched controls?

A reviewer can obtain high issue recall by criticizing everything. Each challenge therefore contains one flawed excerpt and one matched control in which the target defect is repaired or the claim is narrowed to match the evidence.

Primary endpoints are essential-issue recall, negative-control specificity, essential balanced accuracy, and matched-pair pass rate. Secondary metrics include micro precision/F1, severity agreement, evidence-anchor coverage, and duplicate-concern rate.

## Domains

| Domain | Challenges |
|---|---|
| Remote sensing | spatial leakage; QA selection bias; spatial-support mismatch |
| Atmospheric science | assimilation/validation circularity; attribution without internal variability; extreme-regime metric mismatch |
| Hydrology | ungauged-basin leakage; water-balance nonclosure; flood-metric mismatch |
| Climate & ecology | causal confounding; spatial pseudoreplication; scope extrapolation |
| Chemistry | mechanism discrimination; identity/purity; transport limitation |
| Engineering | validated operating envelope; benchmark fairness; batch replication |
| Materials science | phase identity; benchmark comparability; stability claim envelope |
| Polar Earth system | sea-ice metric identity; state-dependent missingness; assimilation lineage |

## Design rules

- Scientific settings and numerical values must be plausible for the domain.
- Positive/control excerpts are closely matched so the target risk drives the expected review.
- Each positive case has one pre-specified primary defect; incidental omissions are not automatically gold concerns.
- Controls are short excerpts, not complete manuscripts. Missing unrelated sections are not benchmark defects.
- Claims in controls are calibrated to available evidence rather than made artificially perfect.
- Each case stores methodological source keys resolved in sources.json.

## Files

~~~text
controlled_v1/
  cases.jsonl
  codebook.json
  sources.json
  oracle_predictions.jsonl
  prompts/
    generic_review.md
    skill_assisted_review.md
  RUN_PROTOCOL.md
  ANNOTATION_PROTOCOL.md
~~~

oracle_predictions.jsonl is a scorer self-test only. It is **not a model result**.

## Validate

~~~bash
python scripts/validate_benchmark_suite.py benchmarks/controlled_v1/cases.jsonl
python scripts/run_benchmarks.py \
  benchmarks/controlled_v1/cases.jsonl \
  benchmarks/controlled_v1/oracle_predictions.jsonl
~~~

## Interpretation limit

Because cases and gold metadata are public, future models may ingest them. Results must be described as public development-set performance. Claims about general reviewer quality require a separate access-controlled expert-labelled set, blinded inference, independent adjudication, and prospective evaluation.
