# GitHub release instructions

Create the repository without initializing README, license, or `.gitignore`.

Recommended repository name:

```text
nature-chemistry-reviewer-skill
```

Upload from inside the package root:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial release of nature chemistry reviewer skill v1.0"
git remote add origin https://github.com/GeoGeekLab/nature-chemistry-reviewer-skill.git
git push -u origin main
```

Create the release tag:

```powershell
git tag v1.0
git push origin v1.0
```

Create a GitHub Release from tag `v1.0`.

Release title:

```text
nature-chemistry-reviewer-skill-v1.0
```

Recommended About description:

```text
Nature-style chemistry manuscript reviewer skill for claim calibration, evidence-chain stress testing, and referee-style reports.
```

Recommended topics:

```text
nature
peer-review
scientific-writing
manuscript-review
codex-skill
research-tools
ai-skill
chemistry
catalysis
chemical-sciences
```

Post-publish checks:

- README renders properly.
- `SKILL.md` front matter is valid.
- `LICENSE`, `LICENSE-MIT`, `LICENSE-APACHE` exist.
- `references/referee_voice_style_gate.md` exists.
- CI workflow runs.
- Repository root is not wrapped in an extra folder.
- Release exists under GitHub Releases.
- Tag `v1.0` exists.
