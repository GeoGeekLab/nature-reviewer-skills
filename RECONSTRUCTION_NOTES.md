# Source reconstruction note

The execution environment used for this refactor could not resolve `github.com` through Git and could not download repository archives. Public raw files were therefore retrieved individually. The seven upstream `SKILL.md` files, seven package READMEs where available, and six upstream CSV pattern databases were preserved. The upstream remote-sensing package used a different multi-JSONL database; its 31 public issue-pattern concepts were normalized into the common schema.

This deliverable is a functional enhanced source tree, not a byte-for-byte clone and not a Git-history mirror. Generated manifests, wrappers, tests, documentation, benchmarks, and shared runtime are new.
