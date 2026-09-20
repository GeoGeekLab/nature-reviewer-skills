# Benchmark suite

This repository has two benchmark layers with different purposes.

## 1. Legacy infrastructure fixtures

`benchmarks/cases/` contains three small synthetic fixtures used to regression-test data loading, scoring, severity handling, evidence anchors, and panel-duplication logic.

These fixtures are software tests. Their perfect oracle scores are **not evidence of reviewer quality**.

## 2. Controlled Review Diagnostic v1

[`benchmarks/controlled_v1/`](controlled_v1/) is the public scientific development benchmark.

CRD-v1 contains:

- 48 synthetic scientific excerpts;
- 24 matched positive/control pairs;
- 8 review groups;
- 24 pre-specified evidence-risk challenges;
- source-backed case design;
- frozen generic and skill-assisted prompts;
- a blinded run protocol;
- an independent annotation protocol;
- negative-control specificity and paired bootstrap uncertainty.

Its core experimental question is not merely “does the reviewer find the injected problem?” It also asks “does the reviewer stop raising that problem when the evidence is repaired or the claim is correctly narrowed?”

CRD-v1 remains a **public, developer-authored diagnostic set**. It does not establish expert equivalence. A strong review-quality claim requires a separate held-out expert-labelled benchmark with blinded inference and adjudication.

## Reproduce the scorer checks

Legacy fixtures:

~~~bash
python scripts/run_benchmarks.py \
  benchmarks/cases \
  benchmarks/predictions/example_predictions.jsonl
~~~

CRD-v1 structure and scorer oracle:

~~~bash
python scripts/validate_benchmark_suite.py benchmarks/controlled_v1/cases.jsonl

python scripts/run_benchmarks.py \
  benchmarks/controlled_v1/cases.jsonl \
  benchmarks/controlled_v1/oracle_predictions.jsonl
~~~

The oracle file only verifies that the scorer behaves as specified. It must never be presented as model performance.

## Compare two blinded prediction files

After raw reviewer outputs have been independently coded into issue IDs:

~~~bash
python scripts/compare_benchmark_predictions.py \
  benchmarks/controlled_v1/cases.jsonl \
  predictions/generic.jsonl \
  predictions/skill_assisted.jsonl \
  --label-a generic \
  --label-b skill-assisted
~~~

The comparison script reports matched-pair bootstrap 95% intervals for the difference in essential-issue recall, specificity, balanced accuracy, paired pass rate, and micro-F1.

Read [CRD-v1 RUN_PROTOCOL.md](controlled_v1/RUN_PROTOCOL.md) and [ANNOTATION_PROTOCOL.md](controlled_v1/ANNOTATION_PROTOCOL.md) before generating benchmark results.
