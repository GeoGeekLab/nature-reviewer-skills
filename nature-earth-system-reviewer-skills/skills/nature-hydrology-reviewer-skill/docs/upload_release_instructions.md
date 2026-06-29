# GitHub upload and release instructions

Create the GitHub repository without initializing README, license or `.gitignore`.

Recommended repository name:

```text
nature-hydrology-reviewer-skill
```

From inside the package root:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial release of nature hydrology reviewer skill v1.0"
git remote add origin https://github.com/GeoGeekLab/nature-hydrology-reviewer-skill.git
git push -u origin main
```

Create tag:

```powershell
git tag v1.0
git push origin v1.0
```

Create GitHub Release from tag `v1.0`.

Release title:

```text
nature-hydrology-reviewer-skill-v1.0
```

Recommended repository description:

```text
Nature-style hydrology manuscript reviewer skill for claim calibration, evidence-chain stress testing, and referee-style reports.
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
hydrology
hydroclimate
water-resources
```
