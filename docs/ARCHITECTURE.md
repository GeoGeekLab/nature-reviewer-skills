# Architecture

The project separates domain knowledge from runtime behavior.

- `SKILL.md`, references, and source CSV records contain domain instructions and review knowledge.
- `nature_reviewer_core.patterns` maps heterogeneous source fields into a stable `Pattern` model while retaining each raw record.
- `nature_reviewer_core.retrieval` performs deterministic lexical retrieval and diversity-aware selection.
- `nature_reviewer_core.security` and `extractors` enforce defensive ingestion boundaries.
- `nature_reviewer_core.panel` assigns complementary reviewer responsibilities and measures overlap.
- `nature_reviewer_core.evaluation` scores predictions against expert-labelled benchmark cases.
- Package scripts are intentionally thin, preventing seven diverging implementations.

The language model remains responsible for manuscript interpretation. The runtime cannot independently establish scientific truth; it provides structured evidence retrieval, constraints, and measurable outputs.
