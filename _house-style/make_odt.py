#!/usr/bin/env python3
"""Markdown -> .odt in the house style.

  python3 make_odt.py report.md [report.odt]

House style: A5 portrait; margins 15 mm top, 10 mm bottom/left/right;
Liberation Serif (18 pt title, 14 pt bold headings, 12 pt body, 10 pt footnotes);
1.15 line spacing; 0 above / 2 mm below paragraphs; footnote hanging indent
0.6 cm; language en-GB; widow/orphan control at 2 lines.

Works by letting pandoc build the document, then patching styles.xml in place --
the same shape as the .docx pipeline, so the two stay in step.
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile
import xml.etree.ElementTree as ET

NS = {
 'office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
 'style':'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
 'fo':'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
 'text':'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
}
for k, v in NS.items():
    ET.register_namespace(k, v)
def q(t):
    p, l = t.split(':'); return '{%s}%s' % (NS[p], l)

PAGE = {'fo:page-width':'14.8cm','fo:page-height':'21cm','style:print-orientation':'portrait',
        'fo:margin-top':'1.5cm','fo:margin-bottom':'1cm','fo:margin-left':'1cm','fo:margin-right':'1cm'}
BODY_T = {'style:font-name':'Liberation Serif','fo:font-size':'12pt',
          'style:font-name-asian':'Liberation Serif','style:font-size-asian':'12pt',
          'fo:language':'en','fo:country':'GB'}
BODY_P = {'fo:line-height':'115%','fo:margin-top':'0cm','fo:margin-bottom':'0.2cm',
          'fo:orphans':'2','fo:widows':'2','fo:text-align':'justify'}

def sub(el, tag):
    found = el.find(q(tag))
    if found is None:
        found = ET.SubElement(el, q(tag))
    return found

def apply(el, tag, attrs):
    child = sub(el, tag)
    for k, v in attrs.items():
        child.set(q(k), v)

def patch(styles_path):
    tree = ET.parse(styles_path); root = tree.getroot()
    # page geometry
    for pl in root.iter(q('style:page-layout')):
        apply(pl, 'style:page-layout-properties', PAGE)
    # document default
    for ds in root.iter(q('style:default-style')):
        if ds.get(q('style:family')) == 'paragraph':
            apply(ds, 'style:text-properties', BODY_T)
            apply(ds, 'style:paragraph-properties',
                  {k: v for k, v in BODY_P.items() if k != 'fo:text-align'})
    for st in root.iter(q('style:style')):
        name = st.get(q('style:name')) or ''
        fam = st.get(q('style:family'))
        if fam != 'paragraph':
            continue
        if name == 'Standard':
            apply(st, 'style:text-properties', BODY_T); apply(st, 'style:paragraph-properties', BODY_P)
        elif name in ('Title', 'Subtitle'):
            apply(st, 'style:text-properties', dict(BODY_T, **{
                'fo:font-size':'18pt','style:font-size-asian':'18pt','fo:font-weight':'bold'}))
            apply(st, 'style:paragraph-properties', {'fo:text-align':'left','fo:margin-bottom':'0.4cm'})
        elif re.match(r'^Heading_20_[1-6]$', name):
            apply(st, 'style:text-properties', dict(BODY_T, **{
                'fo:font-size':'14pt','style:font-size-asian':'14pt','fo:font-weight':'bold'}))
            apply(st, 'style:paragraph-properties',
                  {'fo:margin-top':'0.35cm','fo:margin-bottom':'0.15cm','fo:line-height':'115%',
                   'fo:keep-with-next':'always','fo:border-bottom':'none'})
        elif name in ('Footnote', 'Footnote_20_Symbol', 'Endnote'):
            apply(st, 'style:text-properties', dict(BODY_T, **{
                'fo:font-size':'10pt','style:font-size-asian':'10pt'}))
            apply(st, 'style:paragraph-properties',
                  {'fo:margin-left':'0.6cm','fo:text-indent':'-0.6cm','fo:line-height':'100%',
                   'fo:margin-top':'0cm','fo:margin-bottom':'0.1cm'})
    tree.write(styles_path, xml_declaration=True, encoding='UTF-8')

def main():
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + '.odt'
    subprocess.run(['pandoc', src, '-f', 'markdown', '-t', 'odt', '-o', dst,
                    '--metadata', 'lang=en-GB'], check=True)
    tmp = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(dst) as z:
            names = z.namelist(); z.extractall(tmp)
        patch(os.path.join(tmp, 'styles.xml'))
        with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
            z.write(os.path.join(tmp, 'mimetype'), 'mimetype', zipfile.ZIP_STORED)
            for n in names:
                if n != 'mimetype':
                    z.write(os.path.join(tmp, n), n)
    finally:
        shutil.rmtree(tmp)
    print('wrote', dst)

if __name__ == '__main__':
    main()
