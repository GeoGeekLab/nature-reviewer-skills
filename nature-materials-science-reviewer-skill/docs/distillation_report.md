# Distillation Report

## Scope

This report documents the non-verbatim distillation process for `nature-materials-science-reviewer-skill-v1.0`.

## Input corpus

- Public peer-review files: 44
- Journals: {'Nature Communications': 29, 'Nature': 11, 'Communications Materials': 4}
- Time range: 2024-01-01 to 2026-06-25
- Corpus status: best-effort corpus, not an official complete dataset

## Processing steps

1. Extracted text from public peer-review PDFs.
2. Removed editorial decisions, author rebuttals, response text, and administrative material where detectable.
3. Split review text into reviewer-comment units.
4. Converted each unit into non-verbatim metadata: gate, claim type, evidence risk, reviewer concern and revision direction.
5. Aggregated units into abstract reviewer patterns.
6. Excluded raw reviewer text from the public repository.

## Distilled outputs

- `_internal/review_unit_index.csv`: 3817 non-verbatim reviewer-comment units.
- `reviewer_db/patterns.csv`: 95 abstract reviewer patterns.
- `reviewer_db/patterns.jsonl`: JSONL version of the same pattern database.
- `docs/distillation_qc.csv`: gate-level QC counts.

## Gate counts

| gate                                                |   unit_count |   source_files |   dois |
|:----------------------------------------------------|-------------:|---------------:|-------:|
| reader_logic_and_figure_narrative                   |          707 |             42 |     42 |
| structural_characterization_and_spatial_evidence    |          655 |             42 |     42 |
| editorial_significance_and_novelty                  |          444 |             41 |     41 |
| data_code_materials_and_reporting_completeness      |          395 |             39 |     39 |
| synthesis_route_and_reproducibility                 |          278 |             39 |     39 |
| structure_property_causality_and_mechanism          |          249 |             39 |     39 |
| property_measurement_and_metric_validity            |          247 |             35 |     35 |
| composition_phase_purity_and_identity               |          197 |             33 |     33 |
| computational_design_and_model_validation           |          169 |             28 |     28 |
| stability_durability_and_operando_relevance         |          149 |             21 |     21 |
| scalability_processability_and_application_boundary |          146 |             28 |     28 |
| control_materials_and_benchmarking                  |          142 |             33 |     33 |
| statistical_inference_uncertainty_and_replicates    |           39 |             17 |     17 |

## Copyright and identity safeguards

No long original reviewer comments are redistributed. Anonymous reviewer identities are not inferred or linked to individuals. The index stores hashes of source text for internal deduplication/provenance, but not the source text itself.
