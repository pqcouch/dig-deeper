#!/usr/bin/env python3
"""Split a Logos Rahlfs-Hanhart LXX export (running paragraphs, verse numbers inline) into one
verse per line, in the same layout as the Swete layer:  "Isa 1:1<TAB>text".

  split_rahlfs.py ../logos-exports/.../01-Isaiah-LXX.txt Isa
      -> writes 01-Isaiah-LXX-verses.txt beside the export, and prints a per-chapter check

Written 6 Nov 2026 (Mark claim audit 2 found that Rahlfs readings could be checked by string
but Rahlfs counts could not be run). The export itself is left untouched: it stays the copy of
record, and the -verses file is an observation layer derived from it.

Rules. A chapter starts at a line "CHAPTER n". A verse number is a bare 1-3 digit number not
attached to another digit, colon, comma or full stop, and it is accepted only if it is the next
number in sequence, so a stray number in the text cannot start a verse. The Logos footer
(the edition line and "Exported from Logos ...") is cut before splitting. Logos's dagger (†)
is kept as printed. Single-book exports only: a file that combines two books (the Reigns and
Chronicles files) is refused, because their chapter numbers restart.
"""
import re, sys, os

def split(path, label):
    t = open(path, encoding='utf-8').read()
    cut = re.search(r'\n\s*(Septuaginta:|Exported from Logos)', t)
    if cut: t = t[:cut.start()]
    parts = re.split(r'\n\s*CHAPTER (\d+)\s*\n', t)
    chs = [int(parts[i]) for i in range(1, len(parts), 2)]
    if chs != list(range(1, len(chs) + 1)):
        raise SystemExit('chapters are not 1..n in order (a combined-book file?): refusing')
    out, report = [], []
    for i in range(1, len(parts), 2):
        c, body = int(parts[i]), parts[i + 1]
        marks = []; exp = 1
        for m in re.finditer(r'(?<![\d:,.])(\d{1,3})(?![\d:,.])', body):
            if int(m.group(1)) == exp: marks.append((m.start(), m.end(), exp)); exp += 1
        for j, (s, e, v) in enumerate(marks):
            stop = marks[j + 1][0] if j + 1 < len(marks) else len(body)
            txt = re.sub(r'\s+', ' ', body[e:stop]).strip()
            out.append('%s %d:%d\t%s' % (label, c, v, txt))
        stray = len(re.findall(r'(?<![\d:,.])\d{1,3}(?![\d:,.])', body)) - len(marks)
        report.append((c, len(marks), stray))
    dst = re.sub(r'\.txt$', '-verses.txt', path)
    open(dst, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    return dst, report, len(out)

if __name__ == '__main__':
    if len(sys.argv) != 3: print(__doc__); sys.exit(1)
    dst, report, n = split(sys.argv[1], sys.argv[2])
    for c, k, stray in report:
        if stray: print('chapter %d: %d verses; %d number(s) in the text NOT taken as verses — check' % (c, k, stray))
    print('wrote %s: %d chapters, %d verses' % (os.path.basename(dst), len(report), n))
