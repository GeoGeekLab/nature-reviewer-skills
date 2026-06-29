# Distillation report

## Source corpus

The skill was distilled from `atmospheric_peer_review_corpus_2024_2026_best_effort`, a public, best-effort Nature Portfolio peer-review corpus for atmospheric-science manuscripts.

- Peer Review File PDFs: 35
- Total pages: 1421
- Journals: {'Nature': 9, 'Nature Communications': 23, 'Nature Geoscience': 1, 'Nature Climate Change': 2}
- Relevance levels: {'high_core': 26, 'medium_high_related': 9}
- Date range: 2024-01-01 to 2026-06-25

## Processing summary

1. Extracted text from public peer-review PDFs.
2. Removed author response and rebuttal material where detectable.
3. Split reviewer-facing material into candidate reviewer-comment units.
4. Classified units into atmospheric-science gates using domain keyword and semantic rules.
5. Compressed repeated concerns into transferable, non-verbatim reviewer patterns.
6. Released only abstracted patterns, source metadata, and non-verbatim indices.

## Candidate unit distribution

| gate                                        |   count |
|:--------------------------------------------|--------:|
| atmospheric_claim_evidence_calibration      |     264 |
| ai_weather_climate_model_fidelity           |     222 |
| observational_product_reanalysis_validity   |     210 |
| model_physics_assumption_sensitivity        |     204 |
| detail_audit                                |     187 |
| sampling_event_representativeness           |     166 |
| scale_resolution_boundary_consistency       |     162 |
| aerosol_cloud_radiation_microphysics        |      77 |
| mechanism_causality_circulation_dynamics    |      77 |
| trend_internal_variability_signal_detection |      69 |
| chemistry_emissions_budget                  |      54 |
| uncertainty_statistics_skill_metrics        |      46 |
| extreme_event_attribution_counterfactual    |      45 |
| reproducibility_data_code                   |      24 |

## Released reviewer memory

- Candidate reviewer-comment units: 1807
- Released abstract patterns: 56
- Raw reviewer text stored: no
- Raw PDFs stored: no

## Quality-control notes

The corpus is sufficient for a v1.0 atmospheric reviewer skill because it covers observations, reanalysis/satellite products, AI weather models, numerical modelling, aerosols, atmospheric chemistry, extremes, attribution, land-atmosphere feedbacks, trend detection, and atmospheric mechanism claims. Classic controversies are used only as low-weight stress-test anchors and are not treated as primary peer-review evidence.
