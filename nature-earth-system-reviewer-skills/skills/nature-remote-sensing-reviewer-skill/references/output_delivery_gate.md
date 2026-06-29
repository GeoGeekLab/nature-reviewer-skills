# Output Delivery Gate

For normal review tasks, deliver the review in three forms:

1. Show the Markdown report directly in the chat.
2. Save the same content as a `.md` file.
3. Save the same content as a `.docx` file.

In a file-capable environment such as Codex, file creation is mandatory. Do not only say that files can be generated. Create them, verify that they exist, and report their paths after the Markdown content.

## Required output directory and filenames

Use this default directory unless the user specifies another:

```text
review_outputs/
```

Use these default filenames:

```text
review_outputs/nature_review_report.md
review_outputs/nature_review_report.docx
```

If an internal audit is requested or useful, write it separately:

```text
review_outputs/internal_review_audit.md
```

## Opening completeness statement

The chat response and the saved Markdown should begin with a short statement of submitted-material completeness, for example:

- "Material scope: main manuscript and supplementary material were readable; figures were available as captions only."
- "Material scope: only the abstract was provided, so this is an abstract-level review."
- "Material scope: the manuscript text was readable, but equations embedded as images could not be extracted."

## Markdown and DOCX generation procedure

When working in Codex or another local filesystem environment:

1. Create `review_outputs/`.
2. Write the complete Markdown report to `review_outputs/nature_review_report.md`.
3. If line/page/paragraph anchors are not already available, create anchored extracted text first when input files are accessible, for example:

```bash
python <skill-root>/scripts/extract_text_with_anchors.py <input-files> --out-dir review_inputs_extracted --prefix M
```

4. Generate DOCX using:

```bash
python <skill-root>/scripts/render_review_docx.py review_outputs/nature_review_report.md review_outputs/nature_review_report.docx
```

5. Confirm both files exist and are non-empty.
6. Then provide the Markdown report in chat and list the two output paths.

If `.docx` generation fails, still provide the Markdown report, keep the `.md` file, and explain the `.docx` failure briefly. If the environment cannot write files at all, provide the Markdown content and explicitly state that file output was unavailable.

## Do not under-deliver

A response that only says "I reviewed the files" and then prints the report in chat, without creating `.md` and `.docx` in a file-capable environment, does not satisfy this skill.
