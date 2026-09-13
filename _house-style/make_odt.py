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

# The canonical house .odt converter. Skills that cannot rely on the prep folder
# being connected carry a GENERATED copy of this file, stamped with the version
# and hash below; see bundle_converter.py. Bump the version on any behavioural
# change, then regenerate every bundled copy.
HOUSE_ODT_VERSION = "2026-09-13.1"

import xml.etree.ElementTree as ET

NS = {
 'office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
 'style':'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
 'fo':'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
 'text':'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
 'svg':'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
 'office':'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
}
for k, v in NS.items():
    ET.register_namespace(k, v)
def q(t):
    p, l = t.split(':'); return '{%s}%s' % (NS[p], l)

PAGE = {'fo:page-width':'14.8cm','fo:page-height':'21cm','style:print-orientation':'portrait',
        'fo:margin-top':'1.5cm','fo:margin-bottom':'1cm','fo:margin-left':'1cm','fo:margin-right':'1cm'}
# Three script classes, and LibreOffice treats them separately. Western covers
# Latin and Greek; Asian covers CJK; COMPLEX (CTL) covers Hebrew, Arabic, Syriac.
# pandoc's reference document leaves the complex font at Tahoma, so pointed Hebrew
# silently renders in the wrong face at the wrong size unless it is set here too.
BODY_T = {'style:font-name':'Liberation Serif','fo:font-size':'12pt',
          'style:font-name-asian':'Liberation Serif','style:font-size-asian':'12pt',
          'style:font-name-complex':'Liberation Serif','style:font-size-complex':'15pt',
          'fo:language':'en','fo:country':'GB',
          'style:language-complex':'he','style:country-complex':'IL'}
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

HOUSE = 'Liberation Serif'

def ensure_font_face(root):
    """Declare the house font as an ODF font face.

    `style:font-name` is a *reference* to a declared face. pandoc's reference
    document declares Tahoma, Arial, Times New Roman and friends but not
    Liberation Serif, so the reference dangles. LibreOffice papers over that for
    western text (its own default is Liberation Serif anyway) but falls back to
    its configured default *complex* font for Hebrew -- which is how pointed
    Hebrew kept coming out in Tahoma even with every style attribute set right.
    """
    decls = root.find(q('office:font-face-decls'))
    if decls is None:
        decls = ET.Element(q('office:font-face-decls'))
        root.insert(0, decls)
    for ff in decls.findall(q('style:font-face')):
        if ff.get(q('style:name')) == HOUSE:
            return
    ff = ET.SubElement(decls, q('style:font-face'))
    ff.set(q('style:name'), HOUSE)
    ff.set(q('svg:font-family'), "'%s'" % HOUSE)
    ff.set(q('style:font-family-generic'), 'roman')
    ff.set(q('style:font-pitch'), 'variable')

def sweep(root):
    """House rule: Hebrew is set three points larger than the English around it.

    Complex-script size is a separate attribute from the western one, so every
    style that states a western size gets a complex size three points above it,
    and any complex face pandoc hard-coded is normalised to the house font.
    """
    for tp in root.iter(q('style:text-properties')):
        cur = tp.get(q('style:font-name-complex'))
        if cur and cur.startswith('Tahoma'):
            tp.set(q('style:font-name-complex'), HOUSE)
        west = tp.get(q('fo:font-size')) or ''
        m = re.fullmatch(r'([0-9]+(?:\.[0-9]+)?)pt', west)
        if m:
            tp.set(q('style:font-size-complex'), '%gpt' % (float(m.group(1)) + 3))

def patch_content(content_path):
    tree = ET.parse(content_path); root = tree.getroot()
    ensure_font_face(root)
    sweep(root)
    tree.write(content_path, xml_declaration=True, encoding='UTF-8')

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
                'fo:font-size':'18pt','style:font-size-asian':'18pt',
                'style:font-size-complex':'21pt','fo:font-weight':'bold',
                'style:font-weight-complex':'bold'}))
            apply(st, 'style:paragraph-properties', {'fo:text-align':'left','fo:margin-bottom':'0.4cm'})
        elif re.match(r'^Heading_20_[1-6]$', name):
            apply(st, 'style:text-properties', dict(BODY_T, **{
                'fo:font-size':'14pt','style:font-size-asian':'14pt',
                'style:font-size-complex':'17pt','fo:font-weight':'bold',
                'style:font-weight-complex':'bold'}))
            apply(st, 'style:paragraph-properties',
                  {'fo:margin-top':'0.35cm','fo:margin-bottom':'0.15cm','fo:line-height':'115%',
                   'fo:keep-with-next':'always','fo:border-bottom':'none'})
        elif name in ('Footnote', 'Footnote_20_Symbol', 'Endnote'):
            apply(st, 'style:text-properties', dict(BODY_T, **{
                'fo:font-size':'10pt','style:font-size-asian':'10pt',
                'style:font-size-complex':'13pt'}))
            apply(st, 'style:paragraph-properties',
                  {'fo:margin-left':'0.6cm','fo:text-indent':'-0.6cm','fo:line-height':'100%',
                   'fo:margin-top':'0cm','fo:margin-bottom':'0.1cm'})
    # Sweep: pandoc's reference document hard-codes a Tahoma complex font on a
    # handful of styles (List and Index among them, which is where most Hebrew in
    # a report actually sits). Inheritance never reaches them, so normalise the
    # complex face everywhere it is stated.
    ensure_font_face(root)
    sweep(root)
    tree.write(styles_path, xml_declaration=True, encoding='UTF-8')

def main():
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + '.odt'
    tmp = tempfile.mkdtemp()
    try:
        # Pre-flight, same as the HTML path: these reports use bare `---` lines as
        # section separators, and pandoc can read one as a YAML metadata delimiter
        # and SILENTLY SWALLOW the block after it. Normalise every standalone
        # hyphen-rule to `***`, which is unambiguous. Pipe tables contain `|` and
        # are untouched.
        md = open(src, encoding='utf-8').read()
        md = re.sub(r'(?m)^[ \t]*-{3,}[ \t]*$', '***', md)
        # Count the sections pandoc should produce. Headings quoted inside a
        # blockquote (proposed replacement text, in these documents) DO become
        # real headings in the .odt, so they count; headings inside a fenced code
        # block do not, so the fences come out first.
        counted = re.sub(r'(?ms)^(```+|~~~+).*?^\1[ \t]*$', '', md)
        n_h2_src = len(re.findall(r'(?m)^[ \t]*(?:>[ \t]*)*## (?!#)', counted))
        fixed = os.path.join(tmp, 'source.md')
        with open(fixed, 'w', encoding='utf-8') as fh:
            fh.write(md)
        subprocess.run(['pandoc', fixed, '-f', 'markdown', '-t', 'odt', '-o', dst,
                        '--metadata', 'lang=en-GB'], check=True)
        with zipfile.ZipFile(dst) as z:
            names = z.namelist(); z.extractall(tmp)
        patch(os.path.join(tmp, 'styles.xml'))
        patch_content(os.path.join(tmp, 'content.xml'))
        # Verify before writing back: every `##` section in the source must have
        # produced a level-2 heading in the document.
        body = open(os.path.join(tmp, 'content.xml'), encoding='utf-8').read()
        n_h2_out = len(re.findall(r'text:outline-level="2"', body))
        if n_h2_out != n_h2_src:
            sys.exit('REFUSED %s: %d "##" sections in source but %d level-2 '
                     'headings in the document - content was dropped'
                     % (dst, n_h2_src, n_h2_out))
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
