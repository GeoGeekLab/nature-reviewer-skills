# Nature Engineering Peer Review Corpus, 2024–2026 — Expanded Best-Effort Version

## Overview

This package is an expanded, publicly accessible, article-verified peer-review corpus for building `nature-engineering-reviewer-skill`.

- Retrieval / packaging date: 2026-06-25
- Research field: Engineering / engineering sciences
- Time range: 2024-01-01 to 2026-06-25
- Core journals prioritized in this expansion: Nature; Nature Communications
- Secondary Nature Portfolio subjournals retained from the initial build: Nature Chemical Engineering; Nature Biomedical Engineering
- Corpus status: best-effort corpus, not an official Nature export

## Expansion summary

- Previous downloaded peer-review PDFs: 20
- Incrementally added peer-review PDFs: 22
- Expanded downloaded peer-review PDFs: 42
- Downloaded Nature count: 19
- Downloaded Nature Communications count: 20
- Downloaded Nature Portfolio subjournal count: 3
- Failure / excluded records retained: 12

## Keyword expansion strategy

The search used a broad engineering keyword table rather than the literal phrase “engineering” alone.

1. Core field terms: engineering, engineered system, system design, device engineering, platform engineering.
2. Synonyms and near-synonyms: design, fabrication, integrated system, programmable system, automation, reconfigurable system.
3. Method terms: control, optimization, genetic algorithm, machine learning control, data-driven design, photonic programming, genome engineering.
4. Platforms and technologies: robots, wearable robots, electronic skin, event cameras, quantum devices, photonic chips, actuators, soft materials, genome-editing systems.
5. Application scenarios: autonomous laboratory, automotive perception, rehabilitation robotics, structural inspection, biomedical robotics, extended reality sensing.
6. Abbreviations: AI, ML, e-skin, QEC, CMOS-adjacent sensing terms where article context warranted inclusion.
7. Easily missed expressions: fiberscopic robot, metastructure, magnetoreceptive skin, variable-geometry truss, on-chip nonlinear photonics, recoded organism.

## Inclusion criteria

Articles were included only when all of the following applied:

- Article type was Research Article / Article / Research-equivalent.
- Publication date was within 2024-01-01 to 2026-06-25 using the Nature article page date, not DOI year alone.
- The article was high_core or medium_high_related to engineering.
- The Nature page exposed a Peer Review File / Peer Reviewer Reports / Transparent Peer Review file, or a corresponding static Springer Nature peer-review PDF was verified and opened.
- The downloaded PDF passed file-size and pypdf openability checks.

## Exclusion criteria

The corpus excludes reviews, perspectives, comments, news, editorials, correspondence, protocols, brief communications, corrections, retractions, low-related articles, unrelated false positives, inaccessible links, and duplicate DOI records.

## Files

- `pdfs/`: downloaded Peer Review File PDFs
- `nature_engineering_peer_review_index_expanded.csv`: full downloaded-file index
- `nature_engineering_peer_review_failures_excluded_expanded.csv`: failure and excluded candidate records
- `nature_engineering_peer_review_quality_control_report_expanded.json`: package-level QC report
- `nature_engineering_peer_review_README_expanded.md`: this README

## Quality control

Completed checks:

1. PDF count matches index downloaded count: True
2. Zero-byte PDF files: 0
3. pypdf openability check performed for each downloaded PDF.
4. Duplicate DOI count: 0
5. Duplicate PDF SHA256 count: 0
6. Publication dates were constrained to the declared time range.
7. Journal group was recorded as Nature, Nature Communications, or Nature Portfolio subjournal.
8. SHA256 was calculated for every downloaded PDF.
9. Failure / excluded records were retained in a separate CSV.

## Required declaration

本数据集仅包含 Nature Portfolio 网站公开可访问的 Peer Review File / Peer Reviewer Reports / Transparent Peer Review File。未尝试绕过权限限制，未尝试识别匿名审稿人身份。由于 Nature 搜索页面、索引服务和文章页面结构可能变化，本数据集应视为基于公开网页检索和逐篇验证的 best-effort corpus，而非 Nature 官方导出的全集。

## Limitations

This dataset is not an official Nature Portfolio export and should not be described as a complete universe of all engineering-related peer review files. It is a reproducible, public-web, article-level, best-effort corpus optimized for reviewer-skill distillation.
