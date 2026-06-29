# Distillation sufficiency

Date: 2026-06-25

## Executive judgment

The v1.0 package is sufficiently distilled for a first public GitHub release of `nature-hydrology-reviewer-skill-v1.0`. The package meets the SOP baseline: it contains a complete repository structure, abstract reviewer-memory files, hydrology-specific gates, non-verbatim reviewer-unit indices, reproducible validation scripts, tests, CI configuration, dual licensing and release instructions.

The main limitation is that several specialized gates have lower corpus support than the dominant hydrological-variable, basin-scale and detail-audit gates. These lower-support gates should be treated as necessary expert-control gates rather than fully saturated empirical reviewer-memory clusters.

## Checks performed

| Check | Result |
|---|---:|
| Source peer-review files represented in metadata | 44 |
| Journals represented | Nature Communications:31, Nature:11, Nature Water:2 |
| high_core sources | 34 |
| medium_high_related sources | 10 |
| Non-verbatim review-unit rows | 3905 |
| Raw text stored in unit index | False |
| Abstract reviewer patterns | 158 |
| Gate classes in patterns | 17 |
| Raw PDF files inside repository | 0 |
| DOCX files inside repository | 0 |
| Maximum pattern-field length | 122 chars |
| Raw-review marker hits in pattern fields | 0 |
| Classic stress-test anchors | 10, non-weighted |
| Package validation | PASS |
| compileall | PASS |
| pytest | PASS |

## Gate support profile

The corpus strongly supports the main hydrology gates: scale/basin consistency, hydrological variable validity, claim-evidence calibration, trend/attribution support, model assumptions, sampling representativeness and extreme-event definition.

Low-support gates are still retained because they are important for Nature-style hydrology review, but they should not be overinterpreted as equally frequent in the source corpus.

```text
gate_primary
scale_basin_consistency               940
detail_audit                          592
hydrological_variable_validity        587
claim_evidence_calibration            339
trend_attribution_temporal_support    305
model_assumption_sensitivity          254
extreme_event_definition              173
sampling_gauge_representativeness     173
novelty_related_work_positioning      121
human_water_interaction               108
remote_sensing_data_assimilation       74
validation_independent_testing         74
statistical_uncertainty                69
reproducibility_data_code              51
water_quality_transport                33
management_policy_interpretation       12
```

## Abstraction and copyright check

- `reviewer_db/patterns.csv` and `patterns.jsonl` store abstracted patterns in the form claim type -> evidence risk -> reviewer concern -> revision direction.
- `_internal/review_unit_index.csv` stores source metadata, gate labels, unit length, trigger terms and hash prefixes only.
- No source peer-review PDFs are redistributed inside the repository.
- No long original reviewer comments are stored in the repository.
- No reviewer identities are stored or inferred.

## Classic stress-test layer

The package includes a small cross-literature stress-test layer from high-impact Nature/Science hydrology debates. These records are bibliographic and abstract only. They are not counted as peer-review-file units and carry zero support weight in `reviewer_db/patterns.csv`. They can sharpen claim calibration but cannot by themselves raise severity.


The package also includes close-reading controls for figure-level, table-level and method-level review. These controls are treated as output discipline and detail-audit guidance, not as a separate high-weight empirical gate. They help referee reports anchor major and specific comments to manuscript evidence while preserving the claim-dependent structure of the skill.

## Sufficiency decision

Status: **sufficient for v1.0 release with explicit evidence boundaries**.

Future corpus expansion priority: continue collecting Nature Water, Nature Climate Change and Nature Geoscience transparent-review files as transparent-review files become available, especially for management/policy interpretation, water-quality transport, statistical uncertainty and reproducibility gates.
