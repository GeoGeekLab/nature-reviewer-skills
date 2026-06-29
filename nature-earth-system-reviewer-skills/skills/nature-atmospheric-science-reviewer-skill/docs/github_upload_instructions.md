# GitHub upload instructions

Create the GitHub repository without initializing README, license, or `.gitignore`.

```powershell
git init
git branch -M main
git add .
git commit -m "Initial release of nature atmospheric science reviewer skill v1.0"
git remote add origin https://github.com/GeoGeekLab/nature-atmospheric-science-reviewer-skill.git
git push -u origin main

git tag v1.0
git push origin v1.0
```

Create a GitHub Release from tag `v1.0`.

Release title:

```text
nature-atmospheric-science-reviewer-skill-v1.0
```

Recommended description:

```text
Nature-style atmospheric science manuscript reviewer skill for claim calibration, evidence-chain stress testing, and referee-style reports.
```

Recommended topics:

```text
nature, peer-review, scientific-writing, manuscript-review, codex-skill, research-tools, ai-skill, atmospheric-science, weather, climate, aerosol, attribution
```
