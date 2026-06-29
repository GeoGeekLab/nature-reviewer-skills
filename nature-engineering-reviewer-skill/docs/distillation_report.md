# Distillation Report

## Corpus basis

- Skill: `nature-engineering-reviewer-skill-v1.0`
- Corpus type: public, best-effort Nature Portfolio engineering peer-review corpus
- Source date range: 2024-01-01 to 2026-06-25
- Downloaded peer-review PDF count in source metadata: 42
- Source index rows: 42
- Raw peer-review text redistributed in this repository: no

## Distillation workflow

1. Extracted text from public peer-review PDFs.
2. Conservatively removed common author-response and editorial-response blocks.
3. Split likely referee text into reviewer-comment units.
4. Classified units into engineering gates by transparent keyword-assisted routing.
5. Wrote non-verbatim summaries for internal QC.
6. Distilled transferable reviewer-memory patterns in original language.
7. Stored only abstracted patterns, metadata and hashes.

## Retained internal review units

- Retained non-verbatim internal units: 72
- Abstract reviewer patterns: 37

## Gate distribution in retained units

| Gate | Meaning | Retained unit count |
|---|---:|---:|
| `automation_ai_and_closed_loop_systems` | Automation, AI and closed-loop systems | 4 |
| `benchmark_and_comparability` | Benchmarking and comparability | 5 |
| `biomedical_and_bioengineering_translation` | Biomedical and bioengineering translation | 6 |
| `claim_evidence_calibration` | Claim-evidence calibration | 12 |
| `design_specification_and_requirements` | Design specification and requirement fit | 8 |
| `detail_audit_and_presentation` | Detail audit and presentation | 5 |
| `experimental_validation_and_controls` | Experimental validation and controls | 9 |
| `materials_devices_and_fabrication` | Materials, devices and fabrication | 5 |
| `mechanism_and_causality` | Mechanism and causality | 3 |
| `model_assumptions_and_sensitivity` | Model assumptions and sensitivity | 2 |
| `novelty_and_positioning` | Novelty and related-work positioning | 4 |
| `reproducibility_data_and_code` | Reproducibility, data and code | 1 |
| `robotics_control_and_embodiment` | Robotics, control and embodiment | 3 |
| `scaling_boundary_and_operating_envelope` | Scaling, boundary and operating envelope | 1 |
| `uncertainty_statistics_and_failure_modes` | Uncertainty, statistics and failure modes | 4 |

## Quality and copyright boundary

This distillation does not redistribute long original reviewer comments. Internal rows contain source DOI, unit hash and non-verbatim summaries only. The source corpus should be treated as a best-effort corpus rather than an official complete Nature Portfolio export.

## Design decision

The final skill intentionally emphasizes transferable engineering review logic over case-specific details. The strongest recurrent reviewer pattern is claim calibration: reviewers commonly accept that an engineering demonstration is interesting while requiring clearer limits on novelty, validation, benchmarking, uncertainty, operating envelope, failure modes and reproducibility.
