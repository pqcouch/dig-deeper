#!/usr/bin/env python3
"""Bridge academic transliteration to Strong's numbers.

The reports carry much of their lexical work in SBL-style transliteration
(shakan, `abad, kabed) rather than Hebrew script. TBESH (Tyndale Brief Lexicon of
Extended Strongs for Hebrew, CC BY) gives Strong's -> Hebrew -> its own
transliteration (sha.khan). Both schemes are reduced here to one consonantal
skeleton, so the two can be matched.

Observed TBESH conventions, read off the file rather than assumed:
  sh = shin      ch = het       kh = kaph      ts = tsade
  q  = qoph      v  = bet       t  = tav AND tet (collapsed)
  s  = samek AND sin (collapsed)
  aleph and ayin are DROPPED entirely (`abad -> a.vad, 'erets -> e.rets)

The skeleton therefore drops the gutturals on both sides and collapses the pairs
TBESH itself collapses. That widens the candidate set for a given skeleton, which
is the safe direction: a claim counts as verified if ANY candidate lemma is
present at the reference, so widening biases towards confirming, never towards
accusing.
"""
import os, re, sys, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LEX  = os.path.join(HERE, '..', 'source', 'lexicon', 'TBESH.txt')
OUT  = os.path.join(HERE, '..', '_bridge')

# Schwa has no base letter, so mark-stripping leaves it behind; without it here
# every shewa becomes a phantom consonant and nothing matches.
VOWELS = set('aeiou\u0259\u01dd\u04d9')

def _strip_marks(s):
    # remove macron, breve, circumflex, acute etc but keep the letters they sit on
    out = []
    for ch in unicodedata.normalize('NFD', s):
        if unicodedata.combining(ch):
            continue
        out.append(ch)
    return ''.join(out)

def canon(s, scheme='sbl'):
    """Reduce a transliteration to its consonantal skeleton.

    TBESH collapses sin and samek to plain s and writes shin as sh, so SBL's
    s-acute must go to s and only s-caron to S. A final -a-circumflex / -ah is a
    mater lectionis for he, which TBESH spells out (to.rah); restore it or torah
    loses its last consonant and matches unrelated words.
    """
    s = s.strip().lower()
    # A word ending in aleph or ayin does not end in a mater he: nasa' is TBESH's
    # na.sa, not na.sah. Note that before the gutturals are stripped.
    ends_guttural = bool(re.search(r'[\u02bf\u02be\u2018\u2019\'`]\s*$', s))
    for g in ('\u02bf', '\u02be', '\u2018', '\u2019', "'", '`', '\u02c8'):
        s = s.replace(g, '')                       # ayin, aleph and their stand-ins
    if scheme == 'sbl':
        if not ends_guttural and re.search(r'[\u00e2\u0101]h?$', s):
            s = re.sub(r'[\u00e2\u0101]h?$', 'ah', s)
        s = re.sub(r'\u00ea$', 'eh', s)
        for a, b in (('\u0161', 'S'),             # s-caron  = shin
                     ('\u015b', 's'), ('\u1e63\u030c', 'S'),
                     ('\u1e63', 'Z'),             # s-dot    = tsade
                     ('\u1e25', 'H'),             # h-dot    = het
                     ('\u1e6d', 't'), ('\u1e6f', 't'),
                     ('\u1e35', 'k'), ('\u1e2b', 'H'),
                     ('\u1e0f', 'd'), ('\u1e07', 'b'), ('\u1e21', 'g')):
            s = s.replace(a, b)
        s = s.replace('\u015b', 's')              # s-acute = sin -> s
    s = _strip_marks(s)
    for a, b in (('sh', 'S'), ('ts', 'Z'), ('tz', 'Z'), ('ch', 'H'),
                 ('kh', 'k'), ('ph', 'p'), ('th', 't')):
        s = s.replace(a, b)
    out = []
    for ch in s:
        if ch in VOWELS or ch in ' .-\u2013\u2014_':
            continue
        if ch in 'vw':
            out.append('b')
        elif ch == 'f':
            out.append('p')
        elif ch == 'c':
            out.append('k')
        elif ch == 'j':
            out.append('y')
        elif ch == 'x':
            out.append('Z')
        elif ch.isalpha() or ch in 'SZH':
            out.append(ch)
    sk = ''.join(out)
    sk = re.sub(r'(.)\1+', r'\1', sk)
    return sk


def variants(word):
    """Skeletons a single SBL transliteration could correspond to.

    SBL writes a mater lectionis as a vowel mark (`enayw, tohu), where TBESH
    writes the consonant it stands for (a.yin, to.hu -> y, v). A word must
    therefore be tried both ways.
    """
    out = [canon(word, 'sbl')]
    w = word
    for a, b in (('\u00ee', 'y'), ('\u00ea', 'y'), ('\u00f4', 'w'), ('\u00fb', 'w')):
        w = w.replace(a, b)
    if w != word:
        out.append(canon(w, 'sbl'))
    return [x for x in dict.fromkeys(out) if x]


def build():
    skel2strongs = collections.defaultdict(set)
    strongs_info = {}
    n = 0
    for line in open(LEX, encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) < 7 or not re.match(r'^H\d', p[0]):
            continue
        strongs = re.match(r'^H(\d+)', p[2] or p[0]).group(1).lstrip('0') or '0'
        heb, translit, gloss = p[3], p[4], p[6]
        sk = canon(translit, 'tbesh')
        if sk:
            skel2strongs[sk].add(strongs)
            n += 1
        strongs_info.setdefault(strongs, (heb, translit, gloss))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'translit-to-strongs.tsv'), 'w', encoding='utf-8') as f:
        f.write('skeleton\tstrongs\n')
        for sk in sorted(skel2strongs):
            f.write('%s\t%s\n' % (sk, ','.join(sorted(skel2strongs[sk], key=int))))
    with open(os.path.join(OUT, 'strongs-info.tsv'), 'w', encoding='utf-8') as f:
        f.write('strongs\thebrew\ttranslit\tgloss\n')
        for s in sorted(strongs_info, key=int):
            h, t, g = strongs_info[s]
            f.write('%s\t%s\t%s\t%s\n' % (s, h, t, g.replace('\t', ' ')[:80]))
    return skel2strongs, strongs_info, n

def load():
    d = {}
    p = os.path.join(OUT, 'translit-to-strongs.tsv')
    with open(p, encoding='utf-8') as f:
        next(f)
        for line in f:
            sk, ss = line.rstrip('\n').split('\t')
            d[sk] = set(ss.split(','))
    return d

if __name__ == '__main__':
    s2s, info, n = build()
    print('TBESH entries indexed: %d' % n)
    print('distinct skeletons:    %d' % len(s2s))
    amb = [k for k, v in s2s.items() if len(v) > 1]
    print('ambiguous skeletons:   %d (%.0f%%)' % (len(amb), 100.0*len(amb)/len(s2s)))
    print()
    for probe in ('šākan', 'ʿābad', 'kābēd',
                  'ḥesed', 'tôrâ', 'nāśāʾ',
                  'miškān', 'ṣedeq', 'qādôš'):
        sk = canon(probe, 'sbl')
        print('  %-12s -> %-8s -> %s' % (probe, sk,
              ','.join(sorted(s2s.get(sk, set()), key=int))[:44] or 'NO MATCH'))
