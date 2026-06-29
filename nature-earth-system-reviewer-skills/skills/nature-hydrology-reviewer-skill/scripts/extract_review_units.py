from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path

import fitz


def normalize_space(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def extract_text(pdf: Path) -> str:
    with fitz.open(pdf) as doc:
        return '\n'.join(page.get_text('text') for page in doc)


def split_units(text: str) -> list[str]:
    parts = re.split(r'\n\s*\n+', text)
    return [normalize_space(p) for p in parts if len(normalize_space(p)) > 120]


def main() -> None:
    parser = argparse.ArgumentParser(description='Extract non-verbatim review-unit index from Peer Review PDFs.')
    parser.add_argument('pdf_dir', type=Path)
    parser.add_argument('out_csv', type=Path)
    args = parser.parse_args()
    if not args.pdf_dir.is_dir():
        raise SystemExit(f'PDF directory not found: {args.pdf_dir}')
    rows = []
    for pdf in sorted(args.pdf_dir.glob('*.pdf')):
        for i, unit in enumerate(split_units(extract_text(pdf)), 1):
            rows.append({
                'source_pdf': pdf.name,
                'local_unit_number': i,
                'unit_length_chars': len(unit),
                'unit_text_sha256_prefix': hashlib.sha256(unit.encode('utf-8')).hexdigest()[:16],
                'raw_text_stored': False,
            })
    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.out_csv.open('w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'source_pdf',
            'local_unit_number',
            'unit_length_chars',
            'unit_text_sha256_prefix',
            'raw_text_stored',
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f'Wrote {len(rows)} non-verbatim unit rows to {args.out_csv}')


if __name__ == '__main__':
    main()
