# CRD-v1 three-domain pilot — results template

> Do not fill this document from scorer-oracle output. Only report results from fresh blinded model inference and adjudicated annotations.

## Run identity

- Model/version:
- Runtime/provider:
- Date(s):
- Runs per case:
- Temperature / top-p / seed:
- Tool policy:
- Web/retrieval:
- Pilot commit:
- Packet-preparation manifest SHA-256:

## Completion

- Expected outputs per condition: 54
- Generic outputs obtained:
- Skill-assisted outputs obtained:
- Technical reruns:
- Missing outputs:
- Exclusions: none unless pre-specified technical failure rule applies

## Annotation

- Annotators:
- Domain qualifications:
- Blinding procedure:
- Pre-adjudication agreement:
- Adjudication procedure:

## Primary results

| Endpoint | Generic | Skill-assisted | Δ skill − generic | 95% pair-bootstrap CI for Δ |
|---|---:|---:|---:|---:|
| Essential-issue recall |  |  |  |  |
| Target specificity |  |  |  |  |
| Essential balanced accuracy |  |  |  |  |
| Paired-pass rate |  |  |  |  |

## Secondary results

| Endpoint | Generic | Skill-assisted | Δ skill − generic | 95% pair-bootstrap CI for Δ |
|---|---:|---:|---:|---:|
| Micro precision |  |  |  |  |
| Micro recall |  |  |  |  |
| Micro F1 |  |  |  |  |

## Domain breakdown

Report Remote Sensing, Chemistry, and Engineering separately. With only three matched pairs per domain, domain-level uncertainty is highly discrete and should be treated as descriptive.

## Error analysis

For every miss or target-specific false positive, record:

- domain;
- challenge;
- condition;
- run;
- whether the failure is a miss, over-critique, severity error, or anchoring error;
- concise qualitative explanation.

## Required interpretation language

Results apply to a **public synthetic controlled diagnostic subset** whose challenge taxonomy overlaps the reviewer skills.

Do not describe this pilot as proof of expert-level scientific reviewing or general superiority on real manuscripts.
