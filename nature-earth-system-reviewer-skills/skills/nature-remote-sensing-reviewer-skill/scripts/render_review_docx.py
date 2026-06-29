#!/usr/bin/env python3
import argparse
import html
import re
import zipfile
from pathlib import Path
from datetime import datetime

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
'''
RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
'''
DOC_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
'''
APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Nature Remote-Sensing Reviewer Skill</Application></Properties>
'''
STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr><w:rPr><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="240" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:sz w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="180" w:after="100"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:sz w:val="26"/></w:rPr></w:style>
</w:styles>
'''

def paragraph_xml(text, style=None):
    text = text.strip()
    if not text:
        return '<w:p/>'
    style_xml = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ''
    safe = html.escape(text)
    return f'<w:p>{style_xml}<w:r><w:t xml:space="preserve">{safe}</w:t></w:r></w:p>'

def md_to_doc_xml(md):
    body=[]
    for raw in md.splitlines():
        line=raw.rstrip()
        if line.startswith('### '): body.append(paragraph_xml(line[4:], 'Heading2'))
        elif line.startswith('## '): body.append(paragraph_xml(line[3:], 'Heading1'))
        elif line.startswith('# '): body.append(paragraph_xml(line[2:], 'Heading1'))
        elif re.match(r'^[-*]\s+', line): body.append(paragraph_xml('• '+re.sub(r'^[-*]\s+', '', line)))
        else: body.append(paragraph_xml(line))
    sect='<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'+''.join(body)+sect+'</w:body></w:document>'

def write_docx(md_path, out_path):
    md=Path(md_path).read_text(encoding='utf-8')
    out=Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    now=datetime.utcnow().isoformat()+'Z'
    core=f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Nature Review Report</dc:title><dc:creator>Nature Remote-Sensing Reviewer Skill</dc:creator><cp:lastModifiedBy>Nature Remote-Sensing Reviewer Skill</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>'''
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', CONTENT_TYPES)
        z.writestr('_rels/.rels', RELS)
        z.writestr('word/_rels/document.xml.rels', DOC_RELS)
        z.writestr('word/document.xml', md_to_doc_xml(md))
        z.writestr('word/styles.xml', STYLES)
        z.writestr('docProps/core.xml', core)
        z.writestr('docProps/app.xml', APP_XML)

def main():
    ap=argparse.ArgumentParser(description='Render a Markdown review report to a simple DOCX file.')
    ap.add_argument('input_md')
    ap.add_argument('output_docx')
    args=ap.parse_args()
    write_docx(args.input_md, args.output_docx)
    print(f'Wrote {args.output_docx}')
if __name__=='__main__': main()
