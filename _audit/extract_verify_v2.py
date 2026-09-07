#!/usr/bin/env python3
"""Chain audit, pass 2: transliterated Hebrew and Greek-script claims.

Pass 1 (extract_verify.py) checked Hebrew-script claims only, which left most of
the Torah untested because its lexical work is transliterated. This pass adds:

  * transliterated Hebrew, via the TBESH bridge (_texts/tools/translit.py)
  * Greek script, matched directly against the SBLGNT lemma index
  * versification tolerance, detected empirically rather than from a table

Verdicts:
  CONFIRMED          the word is at the reference claimed
  CONFIRMED-OFFSET   not at the reference, but at a neighbouring verse in a way
                     consistent with English/Hebrew versification -- reported,
                     never silently accepted
  NEAR-MISS          found within two verses but not explained by versification
  FAILED             not found at or near the reference
  WEAK               the skeleton maps to so many lemmas that a hit proves little
  UNRESOLVED         the quoted form could not be mapped to any lemma
"""
import os, re, sys, glob, collections, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_texts', 'tools'))
import translit

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
AUD  = os.path.join(ROOT, '_audit')
HIDX = os.path.join(ROOT, '_texts', 'hebrew-wlc', '_index')
GIDX = os.path.join(ROOT, '_texts', 'greek-nt-sblgnt', '_index')

AMBIG_LIMIT = 8          # above this many candidate lemmas the check proves little

# Books where English and Hebrew verse numbering are known to diverge. Used only
# to LABEL an offset the checker found for itself, never to create a match.
VERSIFICATION = {
 'Gen': 'ch 31/32 boundary', 'Exod': 'chs 8, 22', 'Lev': 'ch 6', 'Num': 'chs 17, 30',
 'Deut': 'chs 13, 23', '1Sam': 'chs 21, 24', '2Sam': 'ch 19', '1Kgs': 'chs 5, 20',
 '2Kgs': 'ch 12', '1Chr': 'chs 6, 12', '2Chr': 'chs 2, 14', 'Neh': 'chs 4, 10',
 'Job': 'chs 40, 41', 'Ps': 'superscriptions counted as verse 1', 'Eccl': 'ch 5',
 'Song': 'ch 7', 'Isa': 'chs 9, 64', 'Jer': 'ch 9', 'Ezek': 'ch 21',
 'Dan': 'chs 4, 6', 'Hos': 'chs 2, 12, 14', 'Joel': 'chs 3, 4',
 'Jonah': 'ch 2 (Eng 1:17 = Heb 2:1)', 'Mic': 'ch 5', 'Nah': 'ch 2',
 'Zech': 'ch 2', 'Mal': 'ch 3 (Eng ch 4 = Heb 3:19-24)',
}

# ------------------------------------------------------------------ corpus load
def load_hebrew():
    verse_lemmas, verse_skels, lemma_forms = (collections.defaultdict(set),
                                              collections.defaultdict(set),
                                              collections.defaultdict(set))
    POINTS = re.compile(r'[֑-ׇ]')
    LET = re.compile(r'[א-ת]+')
    FIN = str.maketrans('ךםןףץ', 'כמנפצ')
    def sk(w):
        w = POINTS.sub('', unicodedata.normalize('NFC', w))
        return ''.join(LET.findall(w)).translate(FIN)
    for f in glob.glob(os.path.join(HIDX, '**', '*.tsv'), recursive=True):
        with open(f, encoding='utf-8') as fh:
            next(fh, None)
            for line in fh:
                p = line.rstrip('\n').split('\t')
                if len(p) != 4:
                    continue
                ref, word, lemma, _m = p
                wp, lp = word.split('/'), lemma.split('/')
                for i, l in enumerate(lp):
                    m = re.match(r'(\d+)', l.strip())
                    if not m:
                        continue
                    n = m.group(1).lstrip('0') or '0'
                    verse_lemmas[ref].add(n)
                    if i < len(wp) and sk(wp[i]):
                        lemma_forms[n].add(sk(wp[i]))
                for w in wp:
                    if sk(w):
                        verse_skels[ref].add(sk(w))
    skel2lem = collections.defaultdict(set)
    for n, forms in lemma_forms.items():
        for s in forms:
            skel2lem[s].add(n)
    return verse_lemmas, verse_skels, skel2lem, sk

def load_greek():
    verse_lemmas, verse_words = collections.defaultdict(set), collections.defaultdict(set)
    def norm(w):
        w = unicodedata.normalize('NFD', w.lower())
        w = ''.join(c for c in w if not unicodedata.combining(c))
        return w.replace('ς', 'σ').strip('·,.;:·')
    for f in sorted(glob.glob(os.path.join(GIDX, '*.tsv'))):
        with open(f, encoding='utf-8') as fh:
            next(fh, None)
            for line in fh:
                p = line.rstrip('\n').split('\t')
                if len(p) < 3:
                    continue
                verse_lemmas[p[0]].add(norm(p[2]))
                verse_words[p[0]].add(norm(p[1]))
    return verse_lemmas, verse_words, norm

if False:
    print('loading Hebrew corpus...'); sys.stdout.flush()
    hv, hs, h2l, hsk = load_hebrew()
    print('  %d verses, %d skeletons' % (len(hv), len(h2l)))
    print('loading Greek corpus...'); sys.stdout.flush()
    gv, gw, gnorm = load_greek()
    print('  %d verses' % len(gv))
    print('loading transliteration bridge...'); sys.stdout.flush()
    t2s = translit.load()
    print('  %d skeletons' % len(t2s))

# ============================================================== extraction stage
import extract_verify as v1

NT_BOOKS = {'matt':'Matt','mt':'Matt','matthew':'Matt','mark':'Mark','mk':'Mark',
 'luke':'Luke','lk':'Luke','john':'John','jn':'John','acts':'Acts','ac':'Acts',
 'rom':'Rom','romans':'Rom','1cor':'1Cor','2cor':'2Cor','gal':'Gal','eph':'Eph',
 'phil':'Phil','php':'Phil','philippians':'Phil','col':'Col','1thess':'1Thess',
 '2thess':'2Thess','1tim':'1Tim','2tim':'2Tim','titus':'Titus','phlm':'Phlm',
 'heb':'Heb','hebrews':'Heb','jas':'Jas','james':'Jas','1pet':'1Pet','1pe':'1Pet',
 '2pet':'2Pet','2pe':'2Pet','1john':'1John','1jn':'1John','2john':'2John',
 '2jn':'2John','3john':'3John','3jn':'3John','jude':'Jude','rev':'Rev'}
v1.BOOKS.update(NT_BOOKS)
v1.HOME.extend([('John','John'),('Philippians','Phil'),('Acts','Acts'),
                ('Matthew','Matt'),('Luke','Luke'),('1 Peter','1Pet'),
                ('2-3 John/2 John','2John'),('2-3 John/3 John','3John'),
                ('2-3 John','2John')])

DIAC = 'šśḥṭṣʿʾāēīōūûôêîăĕŏēġḏḵḇḡṯ'

# Metatextual vocabulary: these name features OF the text, not words IN it, so a
# reference beside them is not a claim that the word occurs there. The petuchah
# and setumah claims ARE checkable, but against the paragraph markers, not the
# lexicon -- handled separately below.
META = {'petuhah','petuhot','petuha','setumah','setumot','setuma','qere','ketiv',
        'kethib','maqqef','paseq','sof','pasuq','waṣf','wasf','leitwort','inclusio',
        'gattung','vorlage','masorah','masoretes','matres','lectionis','tiqqun',
        'soferim','sopherim','nun','hapax','legomenon'}
TRANSLIT = re.compile(r'\*([^*\n]{2,40})\*')
GREEK = re.compile(r'[Ͱ-Ͽἀ-῿]{2,}')

XCHAP = re.compile(r'(\d{1,3}):(\d{1,3})\s*[\u2013\u2014-]\s*(\d{1,3}):(\d{1,3})')

def refs_with_pos(seg, home):
    """[(char position, ref)] -- so a token can be paired with its nearest one."""
    out = []
    for m in XCHAP.finditer(seg):
        if home:
            out.append((m.start(), '%s %s:%s=%s:%s' % (home, m.group(1), m.group(2),
                                                       m.group(3), m.group(4))))
    taken = [(m.start(), m.end()) for m in XCHAP.finditer(seg)]
    last = home
    for m in v1.REF.finditer(seg):
        if any(a <= m.start() < b for a, b in taken):
            continue
        bk = m.group('bk')
        if bk:
            code = v1.BOOKS.get(re.sub(r'[^a-z0-9]', '', bk.lower()))
            if code is None:
                last = None
                continue
            last = code
        else:
            code = last
        if not code:
            continue
        ch, v = int(m.group('ch')), int(m.group('v'))
        v2 = int(m.group('v2')) if m.group('v2') else v
        if v2 < v or v2 - v > 12:
            v2 = v
        out.append((m.start(), '%s %d:%d%s' % (code, ch, v, '-%d' % v2 if v2 > v else '')))
    return out

def documents():
    out = []
    for l in open(os.path.join(AUD, '01-documents.tsv'), encoding='utf-8'):
        out.append(l.rstrip('\n').split('\t')[1])
    for d in ('John', 'Philippians', 'Acts', 'Matthew', 'Luke', '1 Peter', '2-3 John'):
        for dp, _, fs in os.walk(os.path.join(ROOT, d)):
            for fn in sorted(fs):
                if fn.endswith('.md'):
                    out.append(os.path.relpath(os.path.join(dp, fn), ROOT))
    return sorted(set(out))

def tokens_in(seg):
    """(kind, surface) for every quotable lexical token in a segment."""
    out = []
    for t in v1.HEB_TOK.findall(seg):
        if len(v1.skel(t)) >= 2:
            out.append(('heb', t))
    for m in TRANSLIT.finditer(seg):
        raw = m.group(1)
        if not any(c in raw for c in DIAC):
            continue
        for w in re.split(r'[\s/,;\u2013\u2014-]+', raw):
            w = w.strip('.,;:()[]"’“”')
            if len(w) >= 3 and any(c in w for c in DIAC):
                bare = ''.join(c for c in unicodedata.normalize('NFD', w.lower())
                               if not unicodedata.combining(c))
                bare = bare.replace('\u02bf','').replace('\u02be','')
                if bare in META:
                    continue
                out.append(('translit', w))
    for t in GREEK.findall(seg):
        if len(t) >= 3:
            out.append(('grk', t))
    return out

def extract():
    rows = []
    for rel in documents():
        p = os.path.join(ROOT, rel)
        hb = v1.home_book(rel)
        try:
            lines = open(p, encoding='utf-8').read().split('\n')
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            for seg in v1.SEG.split(line):
                toks = tokens_in(seg)
                if not toks:
                    continue
                rp = refs_with_pos(seg, hb)
                if not rp or len(rp) > 8:
                    continue
                # positions of each token in the segment
                placed = []
                for k, t in toks:
                    j = seg.find(t)
                    if (k, t) not in [(a, b) for a, b, _ in placed]:
                        placed.append((k, t, j if j >= 0 else 0))
                if not placed or len(placed) > 3:
                    continue
                if len(placed) == 1:
                    # one word, several references: a genuine distribution claim
                    k, t, _ = placed[0]
                    rows.append((rel, str(i), k, t,
                                 ';'.join(r for _, r in rp), seg.strip()[:260].replace('\t', ' ')))
                    continue
                # several words in one clause: each belongs to its NEAREST
                # reference. Pairing every word with every reference was the
                # largest source of false failures in pass 1.
                for k, t, pos in placed:
                    # A reference in brackets after the word is the normal
                    # convention, so a following one wins over an equally close
                    # preceding one.
                    after = [pr for pr in rp if 0 <= pr[0] - pos <= 45]
                    best = (min(after, key=lambda pr: pr[0] - pos) if after
                            else min(rp, key=lambda pr: abs(pr[0] - pos)))
                    rows.append((rel, str(i), k, t, best[1],
                                 seg.strip()[:260].replace('\t', ' ')))
    with open(os.path.join(AUD, '04-claims-v2.tsv'), 'w', encoding='utf-8') as f:
        f.write('doc\tline\tkind\ttoken\trefs\tcontext\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    return rows

# ============================================================ verification stage
def expand(ref):
    m = re.match(r'^(.+) (\d+):(\d+)=(\d+):(\d+)$', ref)
    if m:
        bk, c1, v1_, c2, v2_ = (m.group(1), int(m.group(2)), int(m.group(3)),
                                int(m.group(4)), int(m.group(5)))
        span = []
        for c in range(c1, c2 + 1):
            lo = v1_ if c == c1 else 1
            hi = v2_ if c == c2 else 200
            span += ['%s %d:%d' % (bk, c, v) for v in range(lo, hi + 1)]
        return bk, span
    m = re.match(r'^(.+ )(\d+):(\d+)(?:-(\d+))?$', ref)
    if not m:
        return None, []
    bk, ch, a = m.group(1), int(m.group(2)), int(m.group(3))
    b = int(m.group(4)) if m.group(4) else a
    return bk.strip(), ['%s %d:%d' % (bk.strip(), ch, v) for v in range(a, b + 1)]

def neighbours(ref):
    m = re.match(r'^(.+) (\d+):(\d+)', ref)
    if not m:
        return []
    bk, ch, v = m.group(1), int(m.group(2)), int(m.group(3))
    out = []
    for d in (-1, 1, -2, 2):
        if v + d >= 1:
            out.append('%s %d:%d' % (bk, ch, v + d))
    for c in (ch - 1, ch + 1):
        if c >= 1:
            out += ['%s %d:%d' % (bk, c, x) for x in (1, 2)]
    return out

def candidates(kind, tok, h2l, t2s):
    if kind == 'heb':
        s = v1.skel(tok)
        c, matched = v1.candidates(s, h2l)
        return set(c), matched
    if kind == 'translit':
        # Union over every plausible reading rather than the first that hits:
        # a construct form's skeleton often collides with an unrelated word, so
        # stopping at the first match silently returns the wrong lemma set.
        found, used = set(), []
        for base in translit.variants(tok):
            trials = [base]
            # nominal prefixes, then the imperfect prefixes y/t/n and the
            # participial m-, which the reports quote as freely as lexical forms
            for pre in ('mS', 'kS', 'bS', 'lS', 'wh', 'wb', 'wl', 'wk', 'wm',
                        'wy', 'wt', 'S', 'b', 'l', 'k', 'm', 'w', 'h',
                        'y', 't', 'n'):
                if base.startswith(pre) and len(base) - len(pre) >= 1:
                    trials.append(base[len(pre):])
            more = []
            for t in trials:
                if t.endswith('t'):
                    more += [t[:-1] + 'h', t[:-1]]      # construct state
                elif t.endswith('h'):
                    more += [t[:-1] + 't', t[:-1]]
                more += [t[:-1], t[:-2], t[:-3]]        # pronominal, dual, plural
            for t in trials + more:
                # biliteral and uniliteral roots are real (av, af, yad), so a
                # one-letter skeleton is allowed when it is an exact lexicon key
                if len(t) >= 1 and t in t2s:
                    found |= set(t2s[t]); used.append(t)
        return found, (used[0] if used else (translit.variants(tok) or [tok])[0])

    return set(), tok

def verify(rows, hv, hs, h2l, t2s, gv, gw, gnorm):
    out = []
    for rel, line, kind, tok, refs, ctx in rows:
        lems, matched = candidates(kind, tok, h2l, t2s)
        for ref in refs.split(';'):
            bk, span = expand(ref)
            if bk is None:
                continue
            ref_is_nt = bk in set(NT_BOOKS.values())
            if (kind == 'grk') != ref_is_nt:
                out.append(('CROSS-TESTAMENT', rel, line, kind, tok, ref, '', ctx))
                continue
            if kind == 'grk':
                n = gnorm(tok)
                span = [r for r in span if r in gv]
                if not span:
                    out.append(('NO-SUCH-VERSE', rel, line, kind, tok, ref, '', ctx)); continue
                hit = any(n in gv[r] or n in gw[r] for r in span)
                near = [r for r in neighbours(span[0]) if r in gv and (n in gv[r] or n in gw[r])]
                v = 'CONFIRMED' if hit else ('NEAR-MISS' if near else 'FAILED')
                out.append((v, rel, line, kind, tok, ref, near[0] if (not hit and near) else '', ctx))
                continue
            span_h = [r for r in span if r in hv]
            if not span_h:
                out.append(('NO-SUCH-VERSE', rel, line, kind, tok, ref, '', ctx)); continue
            if not lems:
                if any(matched in w or w in matched for r in span_h for w in hs[r]):
                    out.append(('CONFIRMED', rel, line, kind, tok, ref, 'surface', ctx))
                else:
                    out.append(('UNRESOLVED', rel, line, kind, tok, ref, '', ctx))
                continue
            if any(lems & hv[r] for r in span_h):
                v = 'WEAK' if len(lems) > AMBIG_LIMIT else 'CONFIRMED'
                out.append((v, rel, line, kind, tok, ref, '%d cand' % len(lems), ctx))
                continue
            if any(matched in w or w in matched for r in span_h for w in hs[r]):
                out.append(('CONFIRMED', rel, line, kind, tok, ref, 'surface', ctx))
                continue
            near = [r for r in neighbours(span_h[0]) if r in hv and lems & hv[r]]
            if near:
                lbl = VERSIFICATION.get(bk)
                out.append(('CONFIRMED-OFFSET' if lbl else 'NEAR-MISS',
                            rel, line, kind, tok, ref, near[0], ctx))
                continue
            out.append(('FAILED', rel, line, kind, tok, ref, '%d cand' % len(lems), ctx))
    with open(os.path.join(AUD, '05-verdicts-v2.tsv'), 'w', encoding='utf-8') as f:
        f.write('verdict\tdoc\tline\tkind\ttoken\tref\tnote\tcontext\n')
        for r in out:
            f.write('\t'.join(r) + '\n')
    return out

def main():
    hv, hs, h2l, _ = load_hebrew()
    gv, gw, gnorm = load_greek()
    t2s = translit.load()
    rows = extract()
    print('claims extracted: %d from %d documents' % (len(rows), len(set(r[0] for r in rows))))
    print('  by kind: %s' % dict(collections.Counter(r[2] for r in rows)))
    out = verify(rows, hv, hs, h2l, t2s, gv, gw, gnorm)
    print('checks: %d' % len(out))
    for k, n in collections.Counter(r[0] for r in out).most_common():
        print('  %-18s %d' % (k, n))

main()
