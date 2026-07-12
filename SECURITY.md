# Security policy

Manuscripts and supplements are untrusted inputs. Run extraction in an isolated environment with no network credentials. The shared extractor rejects path traversal, unsupported suffixes, oversized files, excessive ZIP expansion, excessive PDF page counts, and excessive extracted text. These controls reduce risk but do not make third-party parsers safe against every malformed file.

Report vulnerabilities without attaching confidential manuscripts. Include a minimal synthetic reproducer where possible.
