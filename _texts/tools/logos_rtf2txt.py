"""Convert a Logos RTF apparatus export to plain UTF-8 text.
Keeps: Unicode text (sigla, Hebrew in logical order), paragraphs, superscripts (as Unicode
superscripts, or ^{...} where none exists). Drops: footnotes (Logos pop-up abbreviation notes),
field instructions (hyperlink targets), header/footer, formatting."""
import re,sys
SUP=dict(zip('0123456789abcdeghijklmnoprstuvwxyzABDEGHIJKLMNOPRTUVW+-=()',
 '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂ⁺⁻⁼⁽⁾'))
SUP['f']='ᶠ'; SUP['.']='·'
def sup(s):
    if not s.strip(): return s
    if all(c in SUP for c in s): return ''.join(SUP[c] for c in s)
    return '^{'+s+'}'
SKIP={'footnote','fldinst','fonttbl','colortbl','stylesheet','footer','header','info','pict','*'}
SYMS={'emdash':'—','endash':'–','lquote':'‘','rquote':'’','ldblquote':'“','rdblquote':'”','bullet':'•','tab':'\t','line':'\n','par':'\n','~':'\u00a0','_':'\u2011'}
tok=re.compile(r'\\([a-zA-Z]+)(-?\d+)? ?|\\\'([0-9a-fA-F]{2})|\\(.)|([{}])|([^\\{}\r\n]+)|[\r\n]+')
def convert(data):
    # Cocoa/TextEdit RTF writes a paragraph break as a backslash at end of line
    data=re.sub(r'(?<!\\)\\\r?\n',lambda m:'\\par ',data)
    stack=[]; skip=False; supon=False; uc=1; out=[]; buf=[]  # buf collects superscript chars
    pending_skip=0; hi=None
    def emit(s):
        if skip: return
        out.append('\x01'+s+'\x02' if supon else s)
    def flush(): pass
    for m in tok.finditer(data):
        word,arg,hexc,sym,brace,text=m.groups()
        if pending_skip and (text or hexc):
            # skip the fallback char(s) after \u
            if text:
                n=min(pending_skip,len(text)); text=text[n:]; pending_skip-=n
                if not text: continue
            else:
                pending_skip-=1; continue
        if brace=='{':
            stack.append((skip,supon,uc)); continue
        if brace=='}':
            if stack:
                skip,supon,uc=stack.pop()
            continue
        if word:
            if word in SKIP: skip=True; continue
            if word=='super': supon=True; continue
            if word in ('nosupersub','plain') : 
                if supon: flush()
                supon=False; continue
            if word=='uc': uc=int(arg); continue
            if word=='u':
                n=int(arg); n = n+65536 if n<0 else n
                pending_skip=uc
                if 0xD800<=n<0xDC00: hi=n; continue
                if 0xDC00<=n<0xE000 and hi is not None:
                    n=0x10000+((hi-0xD800)<<10)+(n-0xDC00); hi=None
                emit(chr(n)); continue
            if word in SYMS:
                if supon and word in('par','line'): pass
                emit(SYMS[word]); continue
            continue
        if sym:
            if sym=='*': skip=True; continue
            if sym in '\\{}': emit(sym)
            elif sym in SYMS: emit(SYMS[sym])
            continue
        if hexc: emit(bytes([int(hexc,16)]).decode('cp1252')); continue
        if text: emit(text)
    flush()
    s=''.join(out)
    s=s.replace('\ue91e','\U0001D508')  # Logos private-use glyph = versio Aethiopica (confirmed in Logos, 16 Sep 2026)
    s=s.replace('\x02\x01','')
    def _sup(m):
        body=m.group(1); core=body.strip(); lead=body[:len(body)-len(body.lstrip())]; trail=body[len(body.rstrip()):]
        return lead+(sup(core) if core else '')+trail
    s=re.sub('\x01([^\x02]*)\x02',_sup,s)
    s=re.sub(r'[ \t]+\n','\n',s); s=re.sub(r'[ \t]{2,}',' ',s); s=re.sub(r'\n{3,}','\n\n',s)
    return s.strip()+'\n'
if __name__=='__main__':
    print(convert(open(sys.argv[1],encoding='cp1252',errors='replace').read()))
