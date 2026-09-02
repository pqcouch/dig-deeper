#!/usr/bin/env python3
"""OT chain audit: extract Hebrew-script claims from the reports and verify each
claimed reference against the WLC lemma index.

Stage 1 writes _audit/02-claims.tsv   (every candidate claim found)
Stage 2 writes _audit/03-verdicts.tsv (one row per claim x reference)

Verification is by LEMMA, not surface form. For each Strong's number the corpus
gives every attested morpheme-form; a quoted word is reduced to its consonantal
skeleton, matched to the lemmas that skeleton can represent, and those lemmas are
looked for at the claimed verse. That handles pointing, prefixes and inflection --
the three things that make surface search unreliable.
"""
import os, re, sys, glob, unicodedata, collections, json

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
IDX  = os.path.join(ROOT, '_texts', 'hebrew-wlc', '_index')
AUD  = os.path.join(ROOT, '_audit')

HEB = r'֐-׿'
POINTS = re.compile(r'[֑-ׇ]')          # cantillation + vowel points
LETTERS = re.compile(r'[א-ת]+')
FINALS = str.maketrans('ךםןףץ', 'כמנפצ')
PREFIXES = ('ושה','וש','וה','וב','ול','וכ','ומ','ו','ה','ב','ל','כ','מ','ש')

def skel(w):
    w = POINTS.sub('', unicodedata.normalize('NFC', w))
    w = ''.join(LETTERS.findall(w))
    return w.translate(FINALS)

# ---------------------------------------------------------------- corpus index
def load_corpus():
    lemma_forms = collections.defaultdict(set)   # strongs -> {skeleton}
    verse_lemmas = collections.defaultdict(set)  # ref -> {strongs}
    verse_words  = collections.defaultdict(list) # ref -> [skeleton]
    for f in glob.glob(os.path.join(IDX, '**', '*.tsv'), recursive=True):
        with open(f, encoding='utf-8') as fh:
            next(fh, None)
            for line in fh:
                p = line.rstrip('\n').split('\t')
                if len(p) != 4:
                    continue
                ref, word, lemma, _morph = p
                wparts, lparts = word.split('/'), lemma.split('/')
                for i, lp in enumerate(lparts):
                    m = re.match(r'(\d+)', lp.strip())
                    if not m:
                        continue
                    n = m.group(1)
                    verse_lemmas[ref].add(n)
                    if i < len(wparts):
                        s = skel(wparts[i])
                        if s:
                            lemma_forms[n].add(s)
                for wp in wparts:
                    s = skel(wp)
                    if s:
                        verse_words[ref].append(s)
    skel2lem = collections.defaultdict(set)
    for n, forms in lemma_forms.items():
        for s in forms:
            skel2lem[s].add(n)
    return skel2lem, verse_lemmas, verse_words

# ------------------------------------------------------------ reference parsing
BOOKS = {
 'gen':'Gen','genesis':'Gen','exod':'Exod','exodus':'Exod','ex':'Exod','lev':'Lev',
 'leviticus':'Lev','num':'Num','numbers':'Num','deut':'Deut','deuteronomy':'Deut','dt':'Deut',
 'josh':'Josh','joshua':'Josh','judg':'Judg','judges':'Judg','ruth':'Ruth',
 '1sam':'1Sam','2sam':'2Sam','1kgs':'1Kgs','2kgs':'2Kgs','1kings':'1Kgs','2kings':'2Kgs',
 '1chr':'1Chr','2chr':'2Chr','ezra':'Ezra','neh':'Neh','nehemiah':'Neh','esth':'Esth','esther':'Esth',
 'job':'Job','ps':'Ps','psa':'Ps','psalm':'Ps','psalms':'Ps','prov':'Prov','proverbs':'Prov',
 'eccl':'Eccl','ecclesiastes':'Eccl','song':'Song','isa':'Isa','isaiah':'Isa',
 'jer':'Jer','jeremiah':'Jer','lam':'Lam','lamentations':'Lam','ezek':'Ezek','ezekiel':'Ezek',
 'dan':'Dan','daniel':'Dan','hos':'Hos','hosea':'Hos','joel':'Joel','amos':'Amos',
 'obad':'Obad','obadiah':'Obad','jonah':'Jonah','jon':'Jonah','mic':'Mic','micah':'Mic',
 'nah':'Nah','nahum':'Nah','hab':'Hab','habakkuk':'Hab','zeph':'Zeph','zephaniah':'Zeph',
 'hag':'Hag','haggai':'Hag','zech':'Zech','zechariah':'Zech','mal':'Mal','malachi':'Mal',
}
HOME = [('Torah/Genesis','Gen'),('Torah/Exodus','Exod'),('Torah/Leviticus','Lev'),
 ('Torah/Numbers','Num'),('Torah/Deuteronomy','Deut'),('Isaiah','Isa'),('Jeremiah','Jer'),
 ('Ezekiel','Ezek'),('Psalms','Ps'),('Proverbs','Prov'),('Ruth','Ruth'),('Song of Solomon','Song'),
 ('Ezra-Nehemiah','Ezra'),('The Twelve/Hosea','Hos'),('The Twelve/Joel','Joel'),
 ('The Twelve/Amos','Amos'),('The Twelve/Obadiah','Obad'),('The Twelve/Jonah','Jonah'),
 ('The Twelve/Micah','Mic'),('The Twelve/Nahum','Nah'),('The Twelve/Habakkuk','Hab'),
 ('The Twelve/Zephaniah','Zeph'),('The Twelve/Haggai','Hag'),('The Twelve/Zechariah','Zech'),
 ('The Twelve/Malachi','Mal')]

def home_book(path):
    for prefix, code in HOME:
        if path.startswith(prefix):
            return code
    return None

REF = re.compile(r'(?:(?P<bk>[1-3]?\s?[A-Z][a-zA-Z]{1,11})\.?\s+)?(?P<ch>\d{1,3}):(?P<v>\d{1,3})(?:[–—-](?P<v2>\d{1,3}))?')

def parse_refs(text, default_book, limit=14):
    out, last = [], default_book
    for m in REF.finditer(text):
        bk = m.group('bk')
        code = None
        if bk:
            code = BOOKS.get(re.sub(r'[^a-z0-9]', '', bk.lower()))
            if code is None:
                # a named book we do not hold (Rom, Matt, 4QIsa...) -- skip it
                # entirely rather than silently attributing it to the home book
                last = None
                continue
            last = code
        else:
            code = last
        if not code:
            continue
        ch = int(m.group('ch'))
        v1 = int(m.group('v'))
        v2 = int(m.group('v2')) if m.group('v2') else v1
        if v2 < v1 or v2 - v1 > 12:
            v2 = v1
        if v2 > v1:
            r = '%s %d:%d-%d' % (code, ch, v1, v2)   # range: satisfied by any verse in it
        else:
            r = '%s %d:%d' % (code, ch, v1)
        if r not in out:
            out.append(r)
        if len(out) >= limit:
            break
    return out

# ------------------------------------------------------------------- extraction
HEB_TOK = re.compile(r'[א-ת][֑-תװ-״]*')
STOP = {skel(x) for x in ('את','אשר','כי','לא','אל','על','כל','הוא','היא','אם','מן','גם','זה','אך','או')}

SEG = re.compile(r'\s*(?:\||;|\u00b7|\u2014|\u2013\s|\.\s)\s*')

def extract():
    docs = [l.rstrip('\n').split('\t')[1] for l in open(os.path.join(AUD, '01-documents.tsv'), encoding='utf-8')]
    rows = []
    for rel in docs:
        p = os.path.join(ROOT, rel)
        hb = home_book(rel)
        try:
            lines = open(p, encoding='utf-8').read().split('\n')
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            if not HEB_TOK.search(line):
                continue
            # A word is claimed at the references standing in its OWN segment of
            # the line. Pairing every word with every reference in a line is the
            # single largest source of false positives: these documents put one
            # word and its own references in one table cell or clause.
            for seg in SEG.split(line):
                toks = [t for t in HEB_TOK.findall(seg) if len(skel(t)) >= 2]
                if not toks:
                    continue
                refs = parse_refs(seg, hb, limit=10)
                if len(refs) > 6:
                    continue
                if not refs:
                    continue
                seen = []
                for t in toks:
                    sk = skel(t)
                    if sk and sk not in STOP and sk not in seen:
                        seen.append(sk)
                if not seen or len(seen) > 3:
                    # more than three distinct words in one segment means the
                    # segment is a list, not a claim about a single word
                    continue
                for sk in seen:
                    rows.append((rel, str(i), sk, ';'.join(refs),
                                 seg.strip()[:260].replace('\t', ' ')))
    with open(os.path.join(AUD, '02-claims.tsv'), 'w', encoding='utf-8') as f:
        f.write('doc\tline\tskeleton\trefs\tcontext\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    return rows

# ----------------------------------------------------------------- verification
def candidates(s, skel2lem):
    if s in skel2lem:
        return skel2lem[s], s
    for p in PREFIXES:
        if s.startswith(p) and len(s) - len(p) >= 2:
            t = s[len(p):]
            if t in skel2lem:
                return skel2lem[t], t
    for cut in (1, 2):
        t = s[:-cut]
        if len(t) >= 2 and t in skel2lem:
            return skel2lem[t], t
    return set(), s

def verify(rows, skel2lem, verse_lemmas, verse_words):
    out = []
    for rel, line, s, refs, ctx in rows:
        lems, matched = candidates(s, skel2lem)
        for ref in refs.split(';'):
            m = re.match(r'^(.+ )(\d+):(\d+)-(\d+)$', ref)
            if m:
                bk, ch, a, b = m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
                span = ['%s%s:%d' % (bk, ch, v) for v in range(a, b + 1)]
                span = [r for r in span if r in verse_lemmas]
                if not span:
                    out.append(('NO-SUCH-VERSE', rel, line, s, ref, ctx)); continue
                if not lems:
                    out.append(('UNRESOLVED-WORD', rel, line, s, ref, ctx)); continue
                if any(lems & verse_lemmas[r] for r in span):
                    out.append(('CONFIRMED', rel, line, s, ref, ctx))
                elif any(matched in w or w in matched for r in span for w in verse_words[r]):
                    out.append(('CONFIRMED-SURFACE', rel, line, s, ref, ctx))
                else:
                    out.append(('FAILED', rel, line, s, ref, ctx))
                continue
            if ref not in verse_lemmas:
                verdict = 'NO-SUCH-VERSE'
            elif not lems:
                verdict = 'UNRESOLVED-WORD'
            elif lems & verse_lemmas[ref]:
                verdict = 'CONFIRMED'
            elif any(matched in w or w in matched for w in verse_words[ref]):
                verdict = 'CONFIRMED-SURFACE'
            else:
                verdict = 'FAILED'
            out.append((verdict, rel, line, s, ref, ctx))
    with open(os.path.join(AUD, '03-verdicts.tsv'), 'w', encoding='utf-8') as f:
        f.write('verdict\tdoc\tline\tskeleton\tref\tcontext\n')
        for r in out:
            f.write('\t'.join(r) + '\n')
    return out

if __name__ == '__main__':
    print('building corpus index...'); sys.stdout.flush()
    skel2lem, verse_lemmas, verse_words = load_corpus()
    print('  %d skeletons, %d verses' % (len(skel2lem), len(verse_lemmas)))
    rows = extract()
    print('claims extracted: %d (from %d documents)'
          % (len(rows), len(set(r[0] for r in rows))))
    out = verify(rows, skel2lem, verse_lemmas, verse_words)
    c = collections.Counter(r[0] for r in out)
    print('checks: %d' % len(out))
    for k, v in c.most_common():
        print('  %-18s %d' % (k, v))
