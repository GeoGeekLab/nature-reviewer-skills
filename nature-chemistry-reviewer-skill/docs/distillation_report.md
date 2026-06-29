# Distillation report

## Skill

`nature-chemistry-reviewer-skill-v1.0`

## Corpus basis

- Corpus type: public, best-effort Nature Portfolio peer-review corpus.
- Collection window: 2024-01-01 to 2026-06-25.
- Downloaded peer-review files: 20.
- Journals represented: Communications Chemistry, Nature, Nature Catalysis, Nature Chemistry, Nature Communications, Nature Synthesis.
- Candidate records reviewed: 38.
- Failure/excluded records: 18.

## Distillation workflow

1. Extracted text locally from downloaded Peer Review PDF files.
2. Removed or filtered obvious author-response and rebuttal material using section and phrase filters.
3. Split reviewer material into review-unit candidates.
4. Retained only non-trivial units with reviewer-concern signals.
5. Stored only unit hashes, metadata, abstract gate labels, and word counts.
6. Classified units into transferable chemistry review gates.
7. Distilled non-verbatim reviewer-memory patterns using the structure `claim type -> evidence risk -> reviewer concern -> revision direction`.
8. Excluded raw Peer Review PDF files and long original reviewer comments from the public skill package.

## Output statistics

- Non-verbatim review-unit index rows: 262.
- Abstract reviewer-memory patterns: 51.
- Gates represented in unit index: 11.

## Gate distribution

| abstract_gate                                      |   count |
|:---------------------------------------------------|--------:|
| catalysis_and_performance                          |      95 |
| novelty_and_positioning                            |      51 |
| mechanism_and_causality                            |      38 |
| detail_audit_and_clarity                           |      21 |
| reaction_scope_and_selectivity                     |      18 |
| synthesis_characterization_and_analytical_evidence |      13 |
| controls_and_validation                            |      11 |
| claim_evidence_calibration                         |       5 |
| reproducibility_data_and_code                      |       5 |
| computational_model_assumptions                    |       4 |
| statistical_inference_and_uncertainty              |       1 |

## Journal distribution

| journal                  |   count |
|:-------------------------|--------:|
| Nature Communications    |       9 |
| Nature                   |       5 |
| Nature Chemistry         |       2 |
| Communications Chemistry |       2 |
| Nature Catalysis         |       1 |
| Nature Synthesis         |       1 |

## Copyright and privacy controls

No raw reviewer text is included in `reviewer_db/`. The internal unit index contains only hashes and metadata. The package does not attempt to identify anonymous reviewers and does not redistribute Peer Review PDF files.
