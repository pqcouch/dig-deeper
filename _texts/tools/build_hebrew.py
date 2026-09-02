#!/usr/bin/env python3
"""Build the Hebrew (WLC) layer of the dig-deeper text corpus.

Reads the OSIS XML of the Open Scriptures Hebrew Bible (morphhb) and writes,
per book, in BHS/Tanak order:
  * a reading text  -- one verse per line, pointed Hebrew, "Ref<TAB>text"
  * a word index    -- one word per line, "Ref<TAB>word<TAB>lemma<TAB>morph"

The word index is what makes a claimed lexical chain checkable: search the
lemma column, not the pointed surface form.
"""
import os, re, sys, unicodedata
import xml.etree.ElementTree as ET

NS = '{http://www.bibletechnologies.net/2003/OSIS/namespace}'
SRC = os.path.join(os.path.dirname(__file__), '..', 'source', 'wlc-osis')
OUT = os.path.join(os.path.dirname(__file__), '..', 'hebrew-wlc')

# BHS printed order (Torah / Nevi'im / Ketuvim). Note: BHS prints the Ketuvim
# beginning with Psalms and ending with Chronicles, which departs from the
# sequence of Codex Leningradensis itself (where Chronicles stands first).
ORDER = [
    ('01-Torah', [('01-Genesis','Gen'),('02-Exodus','Exod'),('03-Leviticus','Lev'),
                  ('04-Numbers','Num'),('05-Deuteronomy','Deut')]),
    ('02-Neviim/01-Former', [('01-Joshua','Josh'),('02-Judges','Judg'),
                  ('03a-1-Samuel','1Sam'),('03b-2-Samuel','2Sam'),
                  ('04a-1-Kings','1Kgs'),('04b-2-Kings','2Kgs')]),
    ('02-Neviim/02-Latter', [('01-Isaiah','Isa'),('02-Jeremiah','Jer'),('03-Ezekiel','Ezek')]),
    ('02-Neviim/02-Latter/04-The-Twelve', [('01-Hosea','Hos'),('02-Joel','Joel'),('03-Amos','Amos'),
                  ('04-Obadiah','Obad'),('05-Jonah','Jonah'),('06-Micah','Mic'),('07-Nahum','Nah'),
                  ('08-Habakkuk','Hab'),('09-Zephaniah','Zeph'),('10-Haggai','Hag'),
                  ('11-Zechariah','Zech'),('12-Malachi','Mal')]),
    ('03-Ketuvim', [('01-Psalms','Ps'),('02-Job','Job'),('03-Proverbs','Prov'),('04-Ruth','Ruth'),
                  ('05-Song-of-Songs','Song'),('06-Ecclesiastes','Eccl'),('07-Lamentations','Lam'),
                  ('08-Esther','Esth'),('09-Daniel','Dan'),
                  ('10a-Ezra','Ezra'),('10b-Nehemiah','Neh'),
                  ('11a-1-Chronicles','1Chr'),('11b-2-Chronicles','2Chr')]),
]

def verse_words(verse):
    """Yield (kind, text, lemma, morph) per element, skipping note subtrees.

    kind is 'w' for a word, or the seg type ('x-maqqef', 'x-sof-pasuq',
    'x-paseq', 'x-pe', 'x-samekh'). The pe/samekh markers are the petuchot and
    setumot -- the Masoretic paragraph divisions, which no English version
    carries and which are load-bearing for structure work.
    """
    for el in verse:
        tag = el.tag.replace(NS, '')
        if tag == 'note':
            continue
        if tag == 'w':
            yield ('w', ''.join(el.itertext()), el.get('lemma', ''), el.get('morph', ''))
        elif tag == 'seg':
            yield (el.get('type', 'x-seg'), ''.join(el.itertext()), '', '')


def build(code, out_txt, out_tsv):
    tree = ET.parse(os.path.join(SRC, code + '.xml'))
    verses, words, nverse = [], [], 0
    for verse in tree.iter(NS + 'verse'):
        osis = verse.get('osisID')
        if not osis:
            continue
        bk, ch, vs = osis.split('.')
        ref = '%s %s:%s' % (bk, ch, vs)
        nverse += 1
        surface, join_next = [], False
        for kind, txt, lemma, morph in verse_words(verse):
            if kind == 'w':
                w = txt.replace('/', '')
                if join_next and surface:
                    surface[-1] += w
                else:
                    surface.append(w)
                join_next = False
                words.append('%s\t%s\t%s\t%s' % (ref, txt, lemma, morph))
            elif kind == 'x-maqqef':
                # maqqef binds the words on both sides into one accent unit
                if surface:
                    surface[-1] += txt
                else:
                    surface.append(txt)
                join_next = True
            elif kind == 'x-sof-pasuq':
                if surface:
                    surface[-1] += txt
                else:
                    surface.append(txt)
            else:
                # paseq, petuchah, setumah -- stand alone
                surface.append(txt)
        line = ' '.join(surface)
        line = re.sub(r'\s+', ' ', line).strip()
        verses.append('%s\t%s' % (ref, line))
    with open(out_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(verses) + '\n')
    with open(out_tsv, 'w', encoding='utf-8') as f:
        f.write('ref\tword\tlemma\tmorph\n' + '\n'.join(words) + '\n')
    return nverse, len(words)

def main():
    total_v = total_w = 0
    for section, books in ORDER:
        d = os.path.join(OUT, section)
        os.makedirs(d, exist_ok=True)
        os.makedirs(os.path.join(OUT, '_index', section), exist_ok=True)
        for name, code in books:
            v, w = build(code, os.path.join(d, name + '.txt'),
                         os.path.join(OUT, '_index', section, name + '.tsv'))
            total_v += v; total_w += w
            print('%-34s %5d verses  %7d words' % (section + '/' + name, v, w))
    print('TOTAL  %d verses  %d words' % (total_v, total_w))

if __name__ == '__main__':
    main()
