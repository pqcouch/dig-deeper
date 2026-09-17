import pdfplumber,re,sys,unicodedata
SUP=dict(zip('0123456789abcdeghijklmnoprstuvwxyzABDEGHIJKLMNOPRTUVW+-=()',
 '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂ⁺⁻⁼⁽⁾'))
SUP['f']='ᶠ'; SUP['.']='·'
def sup(s):
    if all(c in SUP for c in s): return ''.join(SUP[c] for c in s)
    return '^{'+s+'}'
def symbol(ch):
    t=ch['text']
    if 'Sirba' in ch['fontname'] and t in '!"#$%&\'':
        r=round(ch['width']/ch['size'],3)
        if t=='!' and abs(r-0.327)<0.01: return '!'
        if abs(r-0.706)<0.005: return 'tt'
        if abs(r-1.185)<0.005: return 'Th'
        return '<LIG%s:%s>'%(t,r)
    if 'LogosSymbol' in ch['fontname'] and t in '!"#$%&\'()':
        r=round(ch['width']/ch['size'],3)
        if abs(r-0.819)<0.005: return '𝔓'
        if abs(r-0.915)<0.005: return '𝔐'
        if abs(r-0.779)<0.005: return '𝔊'
        return '<?%s:%s>'%(t,r)
    return t
def keep(ch):
    fn=ch['fontname'].split('+')[-1]; s=round(ch['size'],1)
    if fn.startswith('Georgia'): return False
    if 'Hebrew' in fn and s<15: return False
    if fn.startswith('SirbaGRK') and s in (10.8,8.1,10.0): return False
    return True
START=re.compile(r'^(\d+(,\d+)?(/\d+)?(–\d+)?\s+[⸀⸁⸂⸄⸆⸇⸈⸉⸋°˸]|[¦⸀⸁⸂⸄⸆⸇⸈⸉⸋°˸]|Inscriptio|Subscriptio)')
def lines_of(pdf):
    for pg in pdf.pages:
        cs=sorted([c for c in pg.chars if keep(c)],key=lambda c:c['top'])
        clusters=[]
        for c in cs:
            if clusters and c['top']-clusters[-1][0]<=6: clusters[-1][1].append(c)
            else: clusters.append([c['top'],[c]])
        for top,cl in clusters:
            cl.sort(key=lambda c:c['x0'])
            out=''; run=''
            for c in cl:
                t=symbol(c)
                if round(c['size'],1)==9.0 and t.strip():
                    run+=t; continue
                if run: out+=sup(run); run=''
                out+=t
            if run: out+=sup(run)
            out=out.replace('ﬀ','ff').replace('\xa0',' ')
            yield top,out.rstrip()
        yield None,None  # page break
def convert(paths):
    entries=[];prevtop=None
    for p in paths:
        with pdfplumber.open(p) as pdf:
            for top,l in lines_of(pdf):
                if top is None: prevtop=None; continue
                if not l.strip(): continue
                if re.fullmatch(r'\s*\d+\s*',l) and False: continue
                gap = (top-prevtop) if prevtop is not None else 0
                prevtop=top
                if START.match(l.lstrip()) or not entries:
                    if re.match(r'^\d',l.lstrip()) and gap>28 and entries: entries.append('')
                    entries.append(l.strip())
                else:
                    entries[-1]+=' '+l.strip()
    return entries
if __name__=='__main__':
    out=sys.argv[1]; paths=sys.argv[2:]
    e=convert(paths)
    open(out,'w',encoding='utf-8').write('\n'.join(e)+'\n')
    print(out,len(e))
