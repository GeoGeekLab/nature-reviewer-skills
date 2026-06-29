# GitHub Publish Guide

Create a GitHub repository named:

```text
nature-engineering-reviewer-skill
```

Do not initialize it with README, license or `.gitignore`.

From inside the package root, run:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial release of nature engineering reviewer skill v1.0"
git remote add origin https://github.com/GeoGeekLab/nature-engineering-reviewer-skill.git
git push -u origin main
git tag v1.0
git push origin v1.0
```

Create a GitHub Release from tag `v1.0` with title:

```text
nature-engineering-reviewer-skill-v1.0
```

Recommended About description:

```text
Nature-style engineering manuscript reviewer skill for claim calibration, evidence-chain stress testing, and referee-style reports.
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
engineering
robotics
bioengineering
materials-engineering
```
