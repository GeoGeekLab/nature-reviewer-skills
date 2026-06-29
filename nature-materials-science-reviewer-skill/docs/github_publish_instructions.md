# GitHub Publishing Instructions

Create the GitHub repository without initializing README, license or `.gitignore`.

Repository name:

```text
nature-materials-science-reviewer-skill
```

Upload from inside the package root:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial release of nature materials science reviewer skill v1.0"
git remote add origin https://github.com/GeoGeekLab/nature-materials-science-reviewer-skill.git
git push -u origin main
```

Create tag and release:

```powershell
git tag v1.0
git push origin v1.0
```

Release title:

```text
nature-materials-science-reviewer-skill-v1.0
```

Recommended description:

```text
Nature-style materials science manuscript reviewer skill for claim calibration, evidence-chain stress testing, and referee-style reports.
```

Recommended topics:

```text
nature peer-review scientific-writing manuscript-review codex-skill research-tools ai-skill materials-science materials-characterization structure-property
```
