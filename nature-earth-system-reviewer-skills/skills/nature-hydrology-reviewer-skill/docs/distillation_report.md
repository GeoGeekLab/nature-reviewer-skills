# Distillation report: nature-hydrology-reviewer-skill-v1.0

## Corpus boundary

This v1.0 skill uses a best-effort public corpus of hydrology-centered Nature Portfolio peer-review files from 2024-01-01 to 2026-06-25.

Included journals in the distilled source corpus:

- Nature
- Nature Communications
- Nature Water

The second-round search was restricted to Nature, Nature Water, Nature Climate Change and Nature Geoscience; only Nature and Nature Water yielded additional hydrology-centered peer-review files that met the inclusion criteria.

## Source corpus scale

- Peer-review files in source corpus: 44
- Manifest page count: 2025
- Nature: 11
- Nature Communications: 31
- Nature Water: 2
- high_core sources: 34
- medium_high_related sources: 10

## Distillation procedure

1. Extracted PDF text from public peer-review files.
2. Kept reviewer-report regions and excluded author rebuttal regions where rule-detectable.
3. Removed administrative boilerplate, editor/rebuttal markers and source-file headers.
4. Split text into reviewer-comment units.
5. Classified units into hydrology-specific gate families using lexical and semantic cues.
6. Stored only non-verbatim unit metadata: source, gate, claim-axis label, length, trigger terms and text hash prefix.
7. Distilled abstract patterns in the form: claim type -> evidence risk -> reviewer concern -> revision direction.
8. Excluded raw reviewer text from this GitHub-ready repository.

## Reviewer-unit index

- Non-verbatim reviewer-comment units indexed: 3905
- Gate classes detected: 16
- Raw text stored in repository: no

Top gate counts:

```text
scale_basin_consistency: 940
detail_audit: 592
hydrological_variable_validity: 587
claim_evidence_calibration: 339
trend_attribution_temporal_support: 305
model_assumption_sensitivity: 254
sampling_gauge_representativeness: 173
extreme_event_definition: 173
novelty_related_work_positioning: 121
human_water_interaction: 108
remote_sensing_data_assimilation: 74
validation_independent_testing: 74
```

## Pattern database

- Abstracted reviewer patterns: 158
- Files: `reviewer_db/patterns.csv` and `reviewer_db/patterns.jsonl`
- Pattern fields: pattern ID, gate, claim type, evidence risk, reviewer concern, revision direction, triggers, severity hint and gate-level support count.

## Quality controls

- Article-level source metadata preserved in `_internal/source_index.csv`.
- Excluded/deferred candidates preserved in `corpus/failures_excluded.csv`.
- PDF checksums preserved in `corpus/checksums.sha256`.
- Non-verbatim reviewer-unit QC preserved in `docs/distillation_qc.csv`.
- Raw PDF files and long original reviewer comments are not included.

## Limitations

This is not an official complete dataset. The corpus is public, article-verified and best-effort. The pattern database captures recurring reviewer concerns but does not reproduce, quote or redistribute source reviews.
