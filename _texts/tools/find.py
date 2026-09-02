#!/usr/bin/env python3
"""Search the dig-deeper text corpus. Lemma-based, so it finds a root wherever
it occurs regardless of pointing, prefixes or suffixes.

  find.py lemma 7931                 every OT occurrence of shakan
  find.py lemma 7931 Exodus          ... within one book
  find.py verify 7931 Exod:40:34 Exod:40:35    check a claimed chain
  find.py glemma λόγος John          Greek NT lemma, one book or all
  find.py text בְּרֵאשִׁית            surface search of the Hebrew reading text
  find.py show "Gen 1:1"             print a verse from every layer that has it

Exit status of `verify` is non-zero if any claimed reference fails, so it can
be used as a gate in a script.
"""
import os, sys, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
HEB_IDX = os.path.join(ROOT, 'hebrew-wlc', '_index')
HEB_TXT = os.path.join(ROOT, 'hebrew-wlc')
GNT_IDX = os.path.join(ROOT, 'greek-nt-sblgnt', '_index')

def files(base, ext, book=None):
    out = sorted(glob.glob(os.path.join(base, '**', '*' + ext), recursive=True))
    if book:
        b = book.lower()
        out = [f for f in out if b in os.path.basename(f).lower()]
    return out

def hits_hebrew(lemma, book=None):
    # a lemma field looks like "c/1961", "l/1481 a", "8199"; match the number
    pat = re.compile(r'(^|/)%s( |$|/)' % re.escape(lemma.lstrip('Hh')))
    for f in files(HEB_IDX, '.tsv', book):
        for line in open(f, encoding='utf-8'):
            p = line.rstrip('\n').split('\t')
            if len(p) == 4 and pat.search(p[2]):
                yield p[0], p[1], p[2], p[3]

def hits_greek(lemma, book=None):
    for f in files(GNT_IDX, '.tsv', book):
        for line in open(f, encoding='utf-8'):
            p = line.rstrip('\n').split('\t')
            if len(p) >= 3 and p[2] == lemma:
                yield p[0], p[1], p[2], p[3] if len(p) > 3 else ''

def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    cmd = argv[1]
    if cmd == 'lemma':
        refs = [h[0] for h in hits_hebrew(argv[2], argv[3] if len(argv) > 3 else None)]
        seen = list(dict.fromkeys(refs))
        for r in seen:
            print(r)
        print('-- %d occurrences in %d verses' % (len(refs), len(seen)), file=sys.stderr)
    elif cmd == 'glemma':
        refs = [h[0] for h in hits_greek(argv[2], argv[3] if len(argv) > 3 else None)]
        seen = list(dict.fromkeys(refs))
        for r in seen:
            print(r)
        print('-- %d occurrences in %d verses' % (len(refs), len(seen)), file=sys.stderr)
    elif cmd == 'verify':
        lemma, claims = argv[2], [c.replace(':', ' ', 1) for c in argv[3:]]
        found = set(h[0] for h in hits_hebrew(lemma)) | set(h[0] for h in hits_greek(lemma))
        bad = 0
        for c in claims:
            ok = c in found
            print('%-4s %s' % ('OK' if ok else 'FAIL', c))
            bad += 0 if ok else 1
        if bad:
            print('\n%d of %d claimed references do NOT contain lemma %s.'
                  % (bad, len(claims), lemma), file=sys.stderr)
        return 1 if bad else 0
    elif cmd == 'text':
        for f in files(HEB_TXT, '.txt'):
            for line in open(f, encoding='utf-8'):
                if argv[2] in line:
                    sys.stdout.write(line)
    elif cmd == 'show':
        ref = argv[2]
        for base in (HEB_TXT, os.path.join(ROOT, 'greek-lxx-swete'),
                     os.path.join(ROOT, 'greek-nt-sblgnt')):
            for f in files(base, '.txt'):
                for line in open(f, encoding='utf-8'):
                    if line.startswith(ref + '\t'):
                        print('[%s] %s' % (os.path.basename(os.path.dirname(f)) or
                                           os.path.basename(base), line.rstrip()))
    else:
        print(__doc__); return 2
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
