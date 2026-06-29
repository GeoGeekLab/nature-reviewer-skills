#!/usr/bin/env python3
"""Extract readable manuscript text with stable review anchors.

This helper is intentionally dependency-light. It supports .docx through the
Open XML package format and .txt/.md directly. PDF extraction is attempted via
pypdf if available. The output anchors are review aids; they do not claim that
original Word files contain line numbers.
"""
import argparse
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

WORD_NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def _clean_text(s: str) -> str:
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s


def extract_docx(path: Path):
    paras = []
    with zipfile.ZipFile(path) as zf:
        names = [n for n in zf.namelist() if n.startswith('word/') and n.endswith('.xml')]
        preferred = ['word/document.xml'] + [n for n in names if n.startswith('word/footnotes') or n.startswith('word/endnotes')]
        seen = set()
        for name in preferred:
            if name not in names or name in seen:
                continue
            seen.add(name)
            root = ET.fromstring(zf.read(name))
            for p in root.findall('.//w:p', WORD_NS):
                texts = []
                for t in p.findall('.//w:t', WORD_NS):
                    if t.text:
                        texts.append(t.text)
                txt = _clean_text(''.join(texts))
                if txt:
                    paras.append(txt)
    return paras


def extract_text(path: Path):
    return [_clean_text(x) for x in path.read_text(encoding='utf-8', errors='ignore').splitlines() if _clean_text(x)]


def extract_pdf(path: Path):
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return [f'[PDF text extraction unavailable without pypdf: {path.name}]']
    reader = PdfReader(str(path))
    out = []
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ''
        for line in text.splitlines():
            line = _clean_text(line)
            if line:
                out.append(f'[Page {i}] {line}')
    return out


def extract_any(path: Path):
    ext = path.suffix.lower()
    if ext == '.docx':
        return extract_docx(path)
    if ext in {'.txt', '.md', '.markdown', '.csv'}:
        return extract_text(path)
    if ext == '.pdf':
        return extract_pdf(path)
    return [f'[Unsupported file type for anchored extraction: {path.name}]']


def write_anchored(path: Path, paras, out: Path, prefix: str):
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8') as f:
        f.write(f'# Anchored extraction for {path.name}\n\n')
        f.write('These anchors are generated from extracted readable text for review-specific referencing. They are not original manuscript line numbers unless the source text already contained line numbers.\n\n')
        for i, para in enumerate(paras, 1):
            anchor = f'{prefix}{i:04d}'
            f.write(f'[{anchor}] {para}\n\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('inputs', nargs='+', help='Input manuscript/supplement files')
    ap.add_argument('--out-dir', default='review_inputs_extracted')
    ap.add_argument('--prefix', default='P')
    args = ap.parse_args()
    out_dir = Path(args.out_dir)
    made = []
    for idx, item in enumerate(args.inputs, 1):
        path = Path(item)
        prefix = f'{args.prefix}{idx:02d}-'
        paras = extract_any(path)
        safe = re.sub(r'[^A-Za-z0-9_.-]+', '_', path.stem)[:80] or f'file_{idx}'
        out = out_dir / f'{idx:02d}_{safe}_anchored.md'
        write_anchored(path, paras, out, prefix)
        made.append(out)
    for out in made:
        print(out)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
