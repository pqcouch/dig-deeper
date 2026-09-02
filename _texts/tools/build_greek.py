#!/usr/bin/env python3
"""Build the Greek layers of the dig-deeper text corpus.

  greek-lxx-swete/  -- Swete's LXX (1909-1930), in the LXX's own book order,
                       one verse per line. Reading and searching layer only:
                       Swete is Vaticanus-based and is NOT Rahlfs-Hanhart.
  greek-nt-sblgnt/  -- SBLGNT with MorphGNT parsing, one verse per line,
                       plus a word index carrying lemma and parsing.
"""
import os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, '..', 'source')

# ---------------------------------------------------------------- Swete LXX
def build_swete():
    out = os.path.join(HERE, '..', 'greek-lxx-swete')
    d = os.path.join(SRC, 'swete-lxx')
    words = {}
    for line in open(os.path.join(d, '01-Swete_word_with_punctuations.csv'), encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) >= 2 and p[0].isdigit():
            words[int(p[0])] = p[1]
    starts = []
    for line in open(os.path.join(d, '00-Swete_versification.csv'), encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) >= 2 and p[0].isdigit():
            starts.append((int(p[0]), p[1]))
    starts.sort()
    hi = max(words) if words else 0
    books, order = collections.defaultdict(list), []
    for i, (idx, ref) in enumerate(starts):
        end = starts[i + 1][0] - 1 if i + 1 < len(starts) else hi
        text = ' '.join(words[j] for j in range(idx, end + 1) if j in words)
        text = re.sub(r'\s+([,.;:·])', r'\1', re.sub(r'\s+', ' ', text)).strip()
        bk = ref.split('.')[0]
        if bk not in books:
            order.append(bk)
        books[bk].append('%s\t%s' % (ref.replace('.', ' '), text))
    os.makedirs(out, exist_ok=True)
    for n, bk in enumerate(order, 1):
        with open(os.path.join(out, '%02d-%s.txt' % (n, bk)), 'w', encoding='utf-8') as f:
            f.write('\n'.join(books[bk]) + '\n')
    print('Swete LXX: %d books, %d verses' % (len(order), sum(len(v) for v in books.values())))
    return order

# ------------------------------------------------------------- SBLGNT (NT)
NT = ['Matt','Mark','Luke','John','Acts','Rom','1Cor','2Cor','Gal','Eph','Phil','Col',
      '1Thess','2Thess','1Tim','2Tim','Titus','Phlm','Heb','Jas','1Pet','2Pet',
      '1John','2John','3John','Jude','Rev']

def build_sblgnt():
    out = os.path.join(HERE, '..', 'greek-nt-sblgnt')
    idx = os.path.join(out, '_index')
    os.makedirs(idx, exist_ok=True)
    d = os.path.join(SRC, 'sblgnt-morph')
    files = sorted(f for f in os.listdir(d) if f.endswith('-morphgnt.txt'))
    tv = tw = 0
    for f in files:
        num = int(f.split('-')[0]) - 60           # 61-Mt -> 1
        name = NT[num - 1]
        verses, words, cur, buf = [], [], None, []
        for line in open(os.path.join(d, f), encoding='utf-8'):
            p = line.rstrip('\n').split(' ')
            if len(p) < 7:
                continue
            bcv, pos, parse, text, word, norm, lemma = p[0], p[1], p[2], p[3], p[4], p[5], p[6]
            ref = '%s %d:%d' % (name, int(bcv[2:4]), int(bcv[4:6]))
            if ref != cur:
                if cur:
                    verses.append('%s\t%s' % (cur, ' '.join(buf)))
                cur, buf = ref, []
            buf.append(text)
            words.append('%s\t%s\t%s\t%s\t%s' % (ref, word, lemma, pos, parse))
        if cur:
            verses.append('%s\t%s' % (cur, ' '.join(buf)))
        with open(os.path.join(out, '%02d-%s.txt' % (num, name)), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(verses) + '\n')
        with open(os.path.join(idx, '%02d-%s.tsv' % (num, name)), 'w', encoding='utf-8') as fh:
            fh.write('ref\tword\tlemma\tpos\tparse\n' + '\n'.join(words) + '\n')
        tv += len(verses); tw += len(words)
    print('SBLGNT: %d books, %d verses, %d words' % (len(files), tv, tw))

if __name__ == '__main__':
    build_swete()
    build_sblgnt()
