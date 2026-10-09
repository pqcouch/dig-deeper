#!/usr/bin/env python3
"""Rarity, exclusivity and rival-source scans over the WLC lemma index.
Companion to find.py (same lemma matcher). Drafted for Round 7 (AB/AC), 3 Oct 2026.

  contacts.py all 5375 6440 2205 2603            verses containing ALL the lemmas (exclusivity)
  contacts.py all 4307 3629 --window 1           ... within +/-1 verse of the same chapter
  contacts.py phrase "כמתי עולם"                  ordered phrase search, plain AND skeletal
  contacts.py scan Lam                           rank every chapter of the Hebrew Bible by rare-contact
  contacts.py scan Lam:1-2 --k 5 --top 20        density with the target (book, or book:chapters)

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

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd'); ap.add_argument('args', nargs='+')
    ap.add_argument('--window', type=int, default=0); ap.add_argument('--k', type=int, default=5)
    ap.add_argument('--min', type=int, default=10); ap.add_argument('--top', type=int, default=20)
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
    else: print(__doc__)
