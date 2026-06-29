#!/usr/bin/env python3
"""Build conservative scholarly-search queries from manuscript text.

This helper does not perform web search. It extracts candidate terms from local
manuscript text so an agent can run allowed literature retrieval with precise,
high-similarity queries and then verify any published-paper comparisons.
"""
import argparse, re, collections
from pathlib import Path

STOP = set('''a an and are as at be by for from has have in into is it its of on or that the their this to using use used with without within across between during over under we our study manuscript paper results method methods data model models based satellite remote sensing analysis water quality nutrient nutrients validation uncertainty trend trends figure table section supplementary material'''.split())
PHRASE_PATTERNS = [
    r"\b[A-Z][A-Za-z]+ River Estuary\b",
    r"\b[A-Z][A-Za-z]+ Estuary\b",
    r"\bMODIS\b", r"\bSentinel-?\d*\b", r"\bLandsat\b", r"\bSeaWiFS\b", r"\bVIIRS\b",
    r"\btotal nitrogen\b", r"\btotal phosphorus\b", r"\bTN\b", r"\bTP\b",
    r"\bchlorophyll[- ]?a\b", r"\bturbidity\b", r"\bsuspended sediment\b",
    r"\brandom forest\b", r"\bquantile regression forest\b", r"\bmachine learning\b",
    r"\batmospheric correction\b", r"\bin situ\b", r"\bmatch[- ]?up\b",
]

def read_text(paths):
    chunks=[]
    for p in paths:
        pp=Path(p)
        if pp.is_file():
            chunks.append(pp.read_text(encoding='utf-8', errors='ignore'))
    return '\n'.join(chunks)

def extract_phrases(text):
    out=[]
    for pat in PHRASE_PATTERNS:
        for m in re.finditer(pat, text, flags=re.I):
            s=m.group(0).strip()
            if s.lower() not in {x.lower() for x in out}:
                out.append(s)
    for line in text.splitlines()[:40]:
        line=line.strip('# ').strip()
        if 8 <= len(line) <= 180 and not line.endswith('.') and len(line.split()) >= 4:
            out.insert(0, line)
            break
    return out[:20]

def top_terms(text, n=18):
    words=[w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{2,}", text)]
    words=[w for w in words if w not in STOP and not w.isdigit()]
    counts=collections.Counter(words)
    return [w for w,_ in counts.most_common(n)]

def build_queries(text, limit):
    phrases=extract_phrases(text)
    terms=top_terms(text)
    def pick(cands, contains=None):
        for c in cands:
            if contains is None or contains.lower() in c.lower():
                return c
        return None
    region = pick(phrases, 'Estuary') or pick(phrases, 'River') or ''
    sensor = pick(phrases, 'MODIS') or pick(phrases, 'Sentinel') or pick(phrases, 'Landsat') or ''
    targets=[]
    for p in phrases:
        if p.lower() in {'total nitrogen','total phosphorus','tn','tp','chlorophyll-a','turbidity'}:
            targets.append(p)
    target=' '.join(targets[:3])
    method = pick(phrases, 'forest') or pick(phrases, 'machine learning') or ''
    base_terms=' '.join(terms[:8])
    qs=[]
    if region and target:
        qs.append(f'"{region}" {target} satellite remote sensing')
    if target and sensor:
        qs.append(f'{target} {sensor} remote sensing validation uncertainty')
    if region and method:
        qs.append(f'"{region}" {method} water quality satellite')
    if target:
        qs.append(f'{target} estuary remote sensing in situ match-up validation')
    if sensor:
        qs.append(f'{sensor} estuarine water quality trend retrieval')
    if base_terms:
        qs.append(base_terms + ' remote sensing published article')
    seen=set(); dedup=[]
    for q in qs:
        q=' '.join(q.split())
        if q.lower() not in seen:
            seen.add(q.lower()); dedup.append(q)
    return dedup[:limit]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', nargs='+', required=True, help='Markdown/text files extracted from manuscript materials')
    ap.add_argument('--limit', type=int, default=8)
    args=ap.parse_args()
    text=read_text(args.input)
    if not text.strip():
        print('No readable input text found.')
        return 1
    for i,q in enumerate(build_queries(text,args.limit),1):
        print(f'{i}. {q}')
    return 0
if __name__=='__main__':
    raise SystemExit(main())
