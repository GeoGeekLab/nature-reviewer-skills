# Comprehensive improvement report

## Delivered scope

- Seven discoverable and independently validatable skills.
- 540 normalized reviewer patterns; original heterogeneous CSV fields remain embedded in generated JSONL records.
- Root CI for Python 3.10–3.13 and a seven-skill validation matrix.
- One shared implementation for retrieval, extraction, validation, security, evaluation, and reviewer-panel control.
- Synthetic benchmark fixtures and quantitative scoring.

## Defects addressed

1. **Inactive nested CI** — replaced by `.github/workflows/ci.yml` at repository root.
2. **Duplicated scripts** — package scripts are thin wrappers around `src/nature_reviewer_core`.
3. **Weak substring retrieval** — replaced with weighted BM25-style scoring, phrase boosts, synonym expansion, confidence labels, and MMR diversification.
4. **No behavior-evaluation framework** — added schemas, gold cases, prediction format, per-case metrics, macro metrics, and per-domain metrics.
5. **Correlated three-reviewer output** — added explicit non-overlapping perspective contracts, cross-reviewer duplicate measurement, and synthesis requirements.
6. **Unsafe document ingestion** — added type allow-listing, file limits, archive path/symlink/ratio checks, page limits, encryption rejection, and extracted-text limits.
7. **Schema drift** — added a normalization layer and generated stable schema-v2 JSONL while retaining all source fields.
8. **Metadata/license inconsistency** — generated uniform v2 manifests and MIT package licences.
9. **Unpinned dependencies** — added exact versions in `requirements.lock`.
10. **Figure/evidence overclaim risk** — extended every `SKILL.md` with explicit non-invention, missing-modality, anchoring, and human-escalation rules.

## Deliberately unresolved scientific claims

No software refactor can prove expert-review equivalence. The repository now makes that claim testable, but a real benchmark still requires authorized manuscripts, independent domain experts, adjudication, and prospective validation. The included synthetic cases test infrastructure only.

## Verification status

The final tree passed 7/7 package validations, 15 shared-runtime tests, 14 per-skill tests, whole-tree Ruff lint/format checks, strict MyPy, Bandit, CLI smoke tests, DOCX/PDF extraction tests, and the synthetic benchmark pipeline. See `TEST_REPORT.md`.
