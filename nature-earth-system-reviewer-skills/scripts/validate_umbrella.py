from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_SKILLS = (
    'nature-remote-sensing-reviewer-skill',
    'nature-atmospheric-science-reviewer-skill',
    'nature-hydrology-reviewer-skill',
    'nature-climate-ecology-reviewer-skill',
)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skills_dir = root / 'skills'
    if not skills_dir.is_dir():
        return ['missing skills directory']
    for name in EXPECTED_SKILLS:
        skill_root = skills_dir / name
        if not skill_root.is_dir():
            errors.append(f'missing skill directory: {name}')
            continue
        for required in ('README.md', 'SKILL.md', 'MANIFEST.json', 'scripts/validate_package.py'):
            if not (skill_root / required).exists():
                errors.append(f'{name} missing {required}')
        manifest_path = skill_root / 'MANIFEST.json'
        if manifest_path.exists():
            data = json.loads(manifest_path.read_text(encoding='utf-8'))
            if data.get('repository') != name:
                errors.append(f'{name} has inconsistent MANIFEST.json repository')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate Earth-system reviewer skill umbrella repository.')
    parser.add_argument('root', nargs='?', default='.', type=Path)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        for error in errors:
            print(f'FAIL: {error}')
        return 1
    print('Umbrella validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
