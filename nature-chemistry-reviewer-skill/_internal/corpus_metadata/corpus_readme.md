# Nature Chemistry Reviewer Skill – Peer Review File Corpus

## Basic information

- Dataset name: `nature_chemistry_peer_review_corpus_2024-01-01_2026-06-25`
- Skill target: `nature-chemistry-reviewer-skill`
- Search date: 2026-06-25
- Research field: chemistry / chemical sciences / molecular chemistry / synthesis / catalysis / computational chemistry / chemical biology
- Time range: 2024-01-01 to 2026-06-25
- Corpus type: publicly accessible, article-by-article verified best-effort corpus

## Journal scope

### Core journals

- Nature
- Nature Communications
- Nature Chemistry

### Priority extension journals

- Nature Catalysis
- Nature Synthesis
- Communications Chemistry

### Conditional extension journals

- Nature Chemical Biology
- Nature Chemical Engineering
- Nature Materials
- Nature Energy
- Nature Nanotechnology
- Communications Materials
- Communications Biology
- Communications Engineering
- Scientific Data
- Other Nature Portfolio journals where chemistry is a central evidence chain and a public peer-review file is available

## Keyword expansion strategy

The search did not rely only on the literal phrase `chemistry`. It used seven keyword families:

1. Core field terms: chemistry, chemical science, molecular chemistry, chemical reaction, reaction mechanism, chemical bonding.
2. Synonyms and near-synonyms: molecular design, molecular engineering, reaction discovery, chemical transformation, bond activation, functionalization.
3. Method terms: synthesis, catalysis, electrocatalysis, photocatalysis, organocatalysis, biocatalysis, C-H activation, cross-coupling, polymerization, supramolecular assembly, kinetic analysis, in situ/operando spectroscopy.
4. Data/platform/instrument/model terms: NMR, MS, LC-MS, GC-MS, HRMS, X-ray crystallography, XPS, XAS, FTIR, Raman, EPR, cyclic voltammetry, DFT, quantum chemistry, molecular dynamics, retrosynthesis, cheminformatics.
5. Application contexts: drug discovery, chemical biology, energy conversion, CO2 reduction, water splitting, battery chemistry, green synthesis, polymer upcycling, chemical sensing.
6. Abbreviations: DFT, MD, ML, AI, NMR, MS, XRD, XPS, XAS, FTIR, EPR, CV, HER, OER, ORR, CO2RR, MOF, COF.
7. Easily missed high-relevance expressions: molecular editing, late-stage functionalization, active site, transition state, reaction coordinate, substrate scope, catalyst reconstruction, interfacial chemistry, solvation structure, redox mediator.

The detailed query log is available at `logs/search_queries_used.md`.

## Inclusion criteria

Articles were included only when all conditions were satisfied:

- Publication date fell inside 2024-01-01 to 2026-06-25.
- Article type was research article / Article / Research.
- The article was `high_core` or `medium_high_related` to chemistry.
- The article page explicitly exposed a Peer Review File / Peer Reviewer Reports / Transparent Peer Review file.
- The file was publicly accessible and successfully downloaded as PDF.
- The file was not ordinary Supplementary Information, Source Data, Reporting Summary or Extended Data.

## Exclusion criteria

Articles were excluded or recorded in the failure table when:

- no public Peer Review File was found;
- the page/file link could not be verified or downloaded;
- the article was low-related or unrelated to chemistry;
- the article was a review, perspective, comment, editorial, correction, retraction, News & Views, research highlight or other non-research type;
- the DOI duplicated a previously retained row;
- the publication date was outside scope;
- the journal or article topic was outside corpus scope.

## Counts

- Candidate records reviewed: 38
- Downloaded Peer Review PDF files: 20
- Failure / excluded records: 18

Downloaded by journal:

- Nature Chemistry: 2
- Nature: 5
- Nature Communications: 9
- Communications Chemistry: 2
- Nature Catalysis: 1
- Nature Synthesis: 1

Downloaded by relevance level:

- high_core: 18
- medium_high_related: 2

Failure/exclusion status summary:

- no_public_peer_review_file: 11
- excluded_low_relevance: 2
- excluded_unrelated: 1
- excluded_wrong_article_type: 2
- duplicate: 1
- failed_link_error: 1

## File inventory

- `pdfs/`: successfully downloaded public Peer Review PDFs
- `index/nature_chemistry_peer_review_index.csv`: downloaded-file index
- `index/nature_chemistry_candidate_full_index.csv`: downloaded + failure/excluded candidate index
- `index/nature_chemistry_failure_excluded.csv`: failure/exclusion table
- `logs/search_queries_used.md`: search query log
- `logs/download_log.csv`: download log with file size and SHA256
- `logs/duplicate_check.csv`: duplicate DOI/SHA256 check
- `logs/qc_report.md`: quality-control report
- `corpus_manifest.json`: machine-readable manifest

## Quality control

QC checks completed:

- PDF file count equals downloaded-index row count.
- Every PDF file size is greater than 0.
- Every PDF opens through PyPDF2 or passes PDF-header validation.
- Duplicate DOI check completed.
- Duplicate PDF SHA256 check completed.
- Publication-date range check completed.
- Journal-scope check completed.
- SHA256 hash calculated for every downloaded PDF.
- Failure/excluded records created.

See `logs/qc_report.md` for details.

## Compliance and limitations

本数据集仅包含 Nature Portfolio 网站公开可访问的 Peer Review File / Peer Reviewer Reports / Transparent Peer Review File。未尝试绕过权限限制，未尝试识别匿名审稿人身份。由于 Nature 搜索页面、索引服务和文章页面结构可能变化，本数据集应视为基于公开网页检索和逐篇验证的 best-effort corpus，而非 Nature 官方导出的全集。

This data package is intended for local corpus distillation, reviewer-pattern abstraction and `nature-chemistry-reviewer-skill` development. If a public GitHub skill repository is released later, it should not redistribute raw Peer Review PDFs, raw reviewer reports, or long text excerpts that substitute for the original files. The public repository should contain only abstracted reviewer-memory patterns, provenance, validation scripts and skill instructions.
