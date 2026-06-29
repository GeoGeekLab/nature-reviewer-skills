# Uploaded-File Autorun Gate

The skill must support minimal user instructions such as "review these uploaded files" or "Use $nature-remote-sensing-reviewer to review the uploaded manuscript."

When one or more files are available:

1. Identify all uploaded or provided files.
2. Classify each file as main manuscript, supplementary material, appendix, figures, tables, references, response letter, or unknown supporting file.
3. Treat the largest manuscript-like file as the main manuscript unless filenames or content indicate otherwise.
4. Treat filenames containing appendix, supplement, supplementary, SI, supporting information, figures, tables, or references as supporting material.
5. Extract readable text, headings, captions, tables, references, availability statements, and supplementary sections when possible.
6. Preserve original files unchanged.
7. State extraction limitations and material scope.
8. Search reviewer memory using manuscript-specific keywords and broad validation/uncertainty queries.
9. Generate the author-facing Nature-style referee report.
10. Generate an internal audit separately only if requested or useful.

Do not require the user to manually restate no-web, no-fabricated-line-number, no-invented-citation, or reviewer-role rules. These safeguards are part of the skill behavior.
