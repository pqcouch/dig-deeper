#!/usr/bin/env python3
"""Rarity, exclusivity and rival-source scans over the WLC lemma index.
Companion to find.py (same lemma matcher). Drafted for Round 7 (AB/AC), 3 Oct 2026.

  contacts.py all 5375 6440 2205 2603            verses containing ALL the lemmas (exclusivity)
  contacts.py all 4307 3629 --window 1           ... within +/-1 verse of the same chapter
  contacts.py phrase "כמתי עולם"                  ordered phrase search, plain AND skeletal
  contacts.py scan Lam                           rank every chapter of the Hebrew Bible by rare-contact
  contacts.py scan Lam:1-2 --k 5 --top 20        density with the target (book, or book:chapters)
  contacts.py ntscan Col:1:15-20                 NT mode: rank every chapter of Swete's LXX against an
  contacts.py ntscan Col:1-2 --top 15            NT passage, in six runs (chapters, 8- and 16-verse
                                                 windows; all words / rarer words), with a stability table
  contacts.py ntscan Col:1:15-20 --check "Psa 88,Isa 9"   ... and list the actual Swete words each
                                                 stem matched there, to catch false friends by eye

A *rare contact* is a pair of content lemmas that occurs in a verse of the target and in a verse
of the comparison chapter, and in no more than K verses of the whole Hebrew Bible (default 5).
Content lemmas exclude the commonest lemmas (found in more than 1,500 verses). Density = rare
pairs per verse of the comparison chapter. A scan measures shared vocabulary, not borrowing,
and it cannot see a pair that straddles two verses, a single rare word, or syntax.
Every result names its edition: WLC (Open Scriptures morphhb).
"""
import os, sys, re, glob, itertools, collections, unicodedata, argparse, pickle, tempfile, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get('TEXTS_ROOT', os.path.join(HERE, '..'))
IDX = os.path.join(ROOT, 'hebrew-wlc', '_index')
TXT = os.path.join(ROOT, 'hebrew-wlc')

def _load():
    idx = collections.OrderedDict(); txt = {}
    for f in sorted(glob.glob(os.path.join(IDX, '**', '*.tsv'), recursive=True)):
        for l in open(f, encoding='utf-8'):
            p = l.rstrip('\n').split('\t')
            if len(p) == 4 and p[0] != 'ref':
                idx.setdefault(p[0], []).append(p[2])
    for f in sorted(glob.glob(os.path.join(TXT, '**', '*.txt'), recursive=True)):
        if '_index' in f: continue
        for l in open(f, encoding='utf-8'):
            p = l.rstrip('\n').split('\t', 1)
            if len(p) == 2: txt[p[0]] = p[1]
    return idx, txt
IDXD, TXTD = _load()
REFS = list(IDXD.keys())

def pat(lem): return re.compile(r'(^|/)%s( |$|/)' % re.escape(lem.lstrip('Hh')))   # = find.py
def has(ref, lem): return any(pat(lem).search(x) for x in IDXD.get(ref, []))
def verses(lem): p = pat(lem); return [r for r in REFS if any(p.search(x) for x in IDXD[r])]

def cmd_all(lems, window=0):
    sets = [set(verses(l)) for l in lems]
    if window == 0:
        return [r for r in REFS if all(r in s for s in sets)]
    pos = {r: i for i, r in enumerate(REFS)}; out = []
    for r in REFS:
        if r not in sets[0]: continue
        i = pos[r]; ch = r.rsplit(':', 1)[0]
        win = {REFS[j] for j in range(max(0, i - window), min(len(REFS), i + window + 1)) if REFS[j].rsplit(':', 1)[0] == ch}
        if all(win & s for s in sets[1:]): out.append(r)
    return out

def norm(s, skeletal=False):
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))
    s = re.sub(r'[־׀׃׀]', ' ', s); s = re.sub(r'[^א-ת ]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    if skeletal:
        s = ' '.join((lambda w: w[:-1] if w.endswith('ה') else w)(re.sub('[וי]', '', w)) for w in s.split())
    return ' ' + s + ' '

def cmd_phrase(p):
    a = [r for r, t in TXTD.items() if norm(p) in norm(t)]
    b = [r for r, t in TXTD.items() if norm(p, True) in norm(t, True)]
    unp = [r for r in b if r not in a]
    return a, b, unp

def _content():
    key = hashlib.md5(str(len(REFS)).encode() + IDX.encode()).hexdigest()[:10]
    cache = os.path.join(tempfile.gettempdir(), 'contacts-%s.pkl' % key)
    if os.path.exists(cache): return pickle.load(open(cache, 'rb'))
    VL = {}
    for r, ws in IDXD.items():
        s = set()
        for w in ws:
            for part in w.split('/'):
                m = re.match(r'(\d+)', part.strip())
                if m: s.add(m.group(1))
        VL[r] = s
    freq = collections.Counter(l for s in VL.values() for l in s)
    stop = {l for l, c in freq.items() if c > 1500}
    CV = {r: tuple(sorted(s - stop)) for r, s in VL.items()}
    pc = collections.Counter(p for s in CV.values() for p in itertools.combinations(s, 2))
    pickle.dump((CV, pc), open(cache, 'wb')); return CV, pc

def _target(spec):
    b, _, ch = spec.partition(':')
    if not ch: return [r for r in REFS if r.split(' ')[0] == b]
    lo, _, hi = ch.partition('-'); hi = hi or lo
    return [r for r in REFS if r.split(' ')[0] == b and int(lo) <= int(r.split(' ')[1].split(':')[0]) <= int(hi)]

def cmd_scan(spec, K=5, minv=10, top=20):
    CV, pc = _content(); tgt = _target(spec); book = spec.split(':')[0]
    tp = collections.defaultdict(set)
    for r in tgt:
        for p in itertools.combinations(CV[r], 2):
            if pc[p] <= K: tp[p].add(r)
    chaps = collections.defaultdict(list)
    for r in REFS:
        if r.split(' ')[0] != book: chaps[r.rsplit(':', 1)[0]].append(r)
    res = []
    for c, refs in chaps.items():
        if len(refs) < minv: continue
        hits = collections.defaultdict(set)
        for r in refs:
            for p in itertools.combinations(CV[r], 2):
                if p in tp: hits[p].add(r)
        res.append((round(len(hits) / len(refs), 3), len(hits), len(refs), c,
                    sorted({(a, b) for p in hits for a in tp[p] for b in hits[p]})[:6]))
    res.sort(key=lambda x: (-x[0], -x[1]))
    return res[:top], len(res)

# ---------------------------------------------------------------------------
# NT mode (added 19 Oct 2026, after the Colossians 1:15-20 dig).
# Ranks every chapter of Swete's LXX against an NT passage. Swete has no lemma
# index, so each content lemma of the passage (SBLGNT index) is reduced to an
# accent-free stem and matched against word-beginnings in Swete. Cognates that
# share a stem are counted together. Counts are FLOORS: a compound verb with an
# internal augment, or a suppletive form, is missed. A stem can also catch a
# different word (a false friend) -- every hit must be checked for sense.
# Six runs: whole chapters, 8-verse windows and 16-verse windows, each once
# with all shared words and once with the rarer words only. Edition: Swete.
# ---------------------------------------------------------------------------
GNT_IDX = os.path.join(ROOT, 'greek-nt-sblgnt', '_index')
LXX_DIR = os.path.join(ROOT, 'greek-lxx-swete')
_KEEP_POS = ('N-', 'V-', 'A-')            # nouns, verbs, adjectives
_SKIP = {'εἰμί', 'γίνομαι', 'ἔχω', 'λέγω', 'ποιέω', 'πᾶς', 'αὐτός', 'ἐγώ', 'σύ', 'οὗτος', 'ὅς', 'τίς', 'τις'}
_ENDS = ['ομαι', 'μαι', 'ευω', 'σσω', 'ττω', 'οω', 'εω', 'αω', 'μι', 'ευς', 'ος', 'ον', 'ης', 'ις', 'υς',
         'ια', 'ας', 'ων', 'η', 'α', 'ω', 'ς']

def _strip(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c)).lower()

def _stems(lemma, pos):
    """Return (key, [prefixes]) for a lemma; key merges cognates."""
    s = _strip(lemma)
    if len(s) <= 3:
        return s, ['=' + s, '=' + s + 'ς', '=' + s + 'ν']          # exact forms only (γη, γης, γην)
    st, end = s, ''
    for e in _ENDS:
        if s.endswith(e) and len(s) - len(e) >= 3:
            st, end = s[:-len(e)], e; break
    if end == 'ων' and not pos.startswith('V'):
        return st + 'ον', [st + 'ον', st + 'ων']                   # εἰκών: εικον-/εικων-, never εἴκοσι
    pre = [st]
    if st.endswith('ζ'): pre.append(st[:-1] + 'σ')                # κτιζ- / κτισ-
    if pos.startswith('V'):
        pre += ['ε' + p for p in pre]                              # simple augment
    key = pre[1] if st.endswith('ζ') else st                       # κτίζω and κτίσις share 'κτισ'
    return key, pre

def _nt_target(spec):
    b, _, rest = spec.partition(':')
    lo = hi = None
    if rest:
        c, _, v = rest.partition(':')
        if v:
            v1, _, v2 = v.partition('-'); lo, hi = (int(c), int(v1)), (int(c), int(v2 or v1))
        else:
            c1, _, c2 = c.partition('-'); lo, hi = (int(c1), 0), (int(c2 or c1), 999)
    out = []
    for f in sorted(glob.glob(os.path.join(GNT_IDX, '*.tsv'))):
        for l in open(f, encoding='utf-8'):
            p = l.rstrip('\n').split('\t')
            if len(p) < 4 or p[0] == 'ref' or p[0].split(' ')[0] != b: continue
            cv = tuple(int(x) for x in p[0].split(' ')[1].split(':'))
            if lo is None or lo <= cv <= hi: out.append((p[2], p[3]))
    return out

def _lxx_units():
    key = hashlib.md5(LXX_DIR.encode()).hexdigest()[:10]
    cache = os.path.join(tempfile.gettempdir(), 'lxxunits-%s.pkl' % key)
    if os.path.exists(cache): return pickle.load(open(cache, 'rb'))
    ch = collections.OrderedDict()
    for f in sorted(glob.glob(os.path.join(LXX_DIR, '*.txt'))):
        for l in open(f, encoding='utf-8'):
            if '\t' not in l: continue
            r, t = l.rstrip('\n').split('\t', 1)
            b, cv = r.split(' ', 1)
            ch.setdefault(b + ' ' + cv.split(':')[0], []).append(set(re.findall(r'\w+', _strip(t))))
    pickle.dump(ch, open(cache, 'wb')); return ch

def _match(tokens, pres):
    for p in pres:
        if p.startswith('='):
            if p[1:] in tokens: return True
        elif any(w.startswith(p) for w in tokens): return True
    return False

CHECK = []
def cmd_ntscan(spec, top=10):
    import math
    words = _nt_target(spec)
    if not words: raise SystemExit('no SBLGNT words for %r (book label as the index has it, e.g. Col, 1Cor, Heb)' % spec)
    lem = {}
    for lemma, pos in words:
        if not pos.startswith(_KEEP_POS) or lemma in _SKIP: continue
        k, pre = _stems(lemma, pos)
        lem.setdefault(k, [set(), set(pre)]); lem[k][0].add(lemma); lem[k][1].update(pre)
    ch = _lxx_units()
    # each Greek word is credited to the LONGEST stem it begins with, so a short
    # stem (πρωτ-) never double-counts a word a longer one (πρωτοτοκ-) already owns
    exact, prefix = {}, {}
    for k, (_, ps) in lem.items():
        for p in ps:
            if p.startswith('='): exact[p[1:]] = k
            else: prefix[p] = k
    lens = sorted({len(p) for p in prefix}, reverse=True)
    def keys(tokens):
        out = set()
        for w in tokens:
            if w in exact: out.add(exact[w]); continue
            for L in lens:
                if len(w) >= L and w[:L] in prefix: out.add(prefix[w[:L]]); break
        return out
    pres = {c: [keys(vs) for vs in vss] for c, vss in ch.items()}
    if CHECK:
        for c in CHECK:
            hit = collections.defaultdict(set)
            for vs in ch.get(c, []):
                for w in vs:
                    k = exact.get(w)
                    if not k:
                        for L in lens:
                            if len(w) >= L and w[:L] in prefix: k = prefix[w[:L]]; break
                    if k: hit[k].add(w)
            print('== sense check, %s: Swete words credited to each stem' % c)
            for k in sorted(hit): print('   %-12s %s' % (k, ', '.join(sorted(hit[k]))))
    runs = {}
    for W, label in ((0, 'chapters'), (8, '8-verse windows'), (16, '16-verse windows')):
        units = []
        for c, vl in pres.items():
            if W == 0: units.append((c, set().union(*vl) if vl else set()))
            else:
                for i in range(0, max(1, len(vl) - W + 1)): units.append((c, set().union(*vl[i:i + W])))
        N = len(units); df = collections.Counter(k for _, s in units for k in s)
        idf = {k: math.log(N / df[k]) if df[k] else 0 for k in lem}
        cap = N / 6 if W == 0 else N / 15
        for rare in (False, True):
            best = {}
            for c, s in units:
                ks = [k for k in s if (not rare or df[k] <= cap)]
                sc = sum(idf[k] for k in ks)
                if sc > best.get(c, (-1,))[0]: best[c] = (sc, sorted(ks))
            order = sorted(best.items(), key=lambda x: -x[1][0])
            runs[(label, 'rarer words' if rare else 'all words')] = {c: (i + 1, v) for i, (c, v) in enumerate(order)}
    zero = sorted(k for k in lem if not any(k in s for vl in pres.values() for s in vl))
    return lem, runs, zero, len(ch)

def _print_ntscan(spec, top):
    lem, runs, zero, n = cmd_ntscan(spec, top)
    print('NT passage %s: %d content stems (SBLGNT lemmas, cognates merged) against %d chapters of Swete\'s LXX' % (spec, len(lem), n))
    if zero: print('stems with NO match anywhere in Swete (check: absence, or a stem fault?):', ', '.join(zero))
    names = list(runs)
    for r in names:
        print('\n== %s, %s' % r)
        for c, (i, (sc, ks)) in sorted(runs[r].items(), key=lambda x: x[1][0])[:top]:
            print('%3d  %6.1f  %-10s %s' % (i, sc, c, ' '.join(ks)))
    cand = {c for r in names for c, (i, _) in runs[r].items() if i <= top}
    rows = sorted(((sorted(runs[r][c][0] for r in names)[len(names) // 2], c) for c in cand))
    print('\n== stability across the six runs (rank in each; median first)')
    print('      ' + ' | '.join('%s/%s' % (a[:7], b[:3]) for a, b in names))
    for med, c in rows:
        print('%-10s ' % c + ' | '.join('%11d' % runs[r][c][0] for r in names) + '   median %d' % med)
    print('\n-- Swete, accent-free word-beginnings: counts are FLOORS; compounds with an internal augment are missed.'
          '\n-- Check every hit for SENSE: a stem can catch a different word (καταλλαγή "exchange" at Isa 9:5).'
          '\n-- A partner high in one run only is a setting artefact; quote ranks only where they hold across runs.'
          '\n-- Where a finding rests on the wording, cite it from the Rahlfs export in logos-exports/, not from Swete.', file=sys.stderr)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd'); ap.add_argument('args', nargs='+')
    ap.add_argument('--window', type=int, default=0); ap.add_argument('--k', type=int, default=5)
    ap.add_argument('--min', type=int, default=10); ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--check', default='', help='ntscan: comma-separated chapters to sense-check, e.g. "Psa 88,Isa 9"')
    a = ap.parse_args()
    if a.cmd == 'all':
        out = cmd_all(a.args, a.window); print('\n'.join(out))
        print('-- %d verses (WLC) contain all of %s%s' % (len(out), ' '.join(a.args), ' within ±%d' % a.window if a.window else ''), file=sys.stderr)
    elif a.cmd == 'phrase':
        p, s, u = cmd_phrase(' '.join(a.args))
        print('plain   :', ', '.join(p)); print('skeletal:', ', '.join(s))
        if u: print('found only by the skeletal pass (spelling differs):', ', '.join(u))
        print('-- ordered phrase; a reordered or ketiv form will not match — confirm by `all`', file=sys.stderr)
    elif a.cmd == 'scan':
        res, n = cmd_scan(a.args[0], a.k, a.min, a.top)
        print('rank  density  pairs  verses  chapter   (sample verse contacts)')
        for i, (d, h, v, c, s) in enumerate(res, 1):
            print('%3d   %6.3f  %5d  %6d  %-9s %s' % (i, d, h, v, c, ' '.join('%s~%s' % x for x in s)))
        print('-- %d chapters of >= %d verses scanned; K=%d (WLC)' % (n, a.min, a.k), file=sys.stderr)
    elif a.cmd == 'ntscan':
        CHECK[:] = [x.strip() for x in a.check.split(',')] if a.check else []
        _print_ntscan(a.args[0], a.top if a.top != 20 else 10)
    else: print(__doc__)
