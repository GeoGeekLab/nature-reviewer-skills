# Defensive ingestion model

Default limits are deliberately conservative:

- 25 MiB per input file.
- 100 MiB total uncompressed archive content.
- Archive expansion ratio no greater than 100:1.
- 500 PDF pages.
- 5 million extracted characters.
- No symlink or path-traversal archive members.

Callers can reduce limits but should not raise them for public upload services without additional sandboxing, CPU quotas, memory quotas, and parser isolation.
