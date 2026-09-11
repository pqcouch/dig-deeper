#!/usr/bin/env python3
"""Mechanical synoptic diff: Isa 36:1-39:8 // 2 Kgs 18:13-20:21 (WLC).

Normalises accents (NFD strip combining marks), maqqef and paseq to spaces,
then aligns verse by verse per the block map and reports, per pair:
  similarity ratio, identical y/n, and word-level added/removed.
"""
import unicodedata, difflib, sys, re, json

BASE = "/Users/x/mnt"  # replaced at runtime
ISA = sys.argv[1]
KGS = sys.argv[2]

def load(path, prefix):
    d = {}
    for line in open(path, encoding="utf-8"):
        if "\t" not in line: continue
        ref, txt = line.rstrip("\n").split("\t", 1)
        d[ref.strip()] = txt.strip()
    return d

def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("־", " ").replace("׀", " ")   # maqqef, paseq
    s = s.replace("׃", " ").replace("׆", " ")   # sof pasuq, nun hafukha
    s = re.sub(r"[֑-ֽֿ֯]", "", s)     # stray cantillation/meteg
    s = re.sub(r"[^א-ת ]", " ", s)              # consonants + space only
    return re.sub(r"\s+", " ", s).strip()

isa = load(ISA, "Isa")
kgs = load(KGS, "2Ki")

# Discover the actual ref prefix used in each file
isa_pref = [k.rsplit(" ",1)[0] for k in isa if k.endswith(" 36:1")][0]
kgs_pref = [k.rsplit(" ",1)[0] for k in kgs if k.endswith(" 18:13")][0]

def I(cv): return isa.get(f"{isa_pref} {cv}")
def K(cv): return kgs.get(f"{kgs_pref} {cv}")

# Block map: (isa_ch, isa_start, isa_end, kgs_ch, kgs_start) sequential runs
BLOCKS = [
    ("36", 1, 1,  "18", 13),
    ("36", 2, 22, "18", 17),
    ("37", 1, 38, "19", 1),
    ("38", 1, 8,  "20", 1),
    ("39", 1, 8,  "20", 12),
]
ISA_ONLY = [("38", v) for v in range(9, 23)]          # the psalm + 21-22
KGS_ONLY = [("18", v) for v in (14, 15, 16)] + [("20", v) for v in (20, 21)]

rows = []
for ich, i0, i1, kch, k0 in BLOCKS:
    for n, iv in enumerate(range(i0, i1 + 1)):
        kv = k0 + n
        a, b = I(f"{ich}:{iv}"), K(f"{kch}:{kv}")
        if a is None or b is None:
            rows.append((f"Isa {ich}:{iv}", f"2Ki {kch}:{kv}", None, "MISSING", "", ""))
            continue
        na, nb = norm(a), norm(b)
        r = difflib.SequenceMatcher(None, na.split(), nb.split()).ratio()
        wa, wb = na.split(), nb.split()
        sm = difflib.SequenceMatcher(None, wa, wb)
        only_i, only_k = [], []
        for tag, i_, j_, k_, l_ in sm.get_opcodes():
            if tag in ("replace", "delete"): only_i += wa[i_:j_]
            if tag in ("replace", "insert"): only_k += wb[k_:l_]
        rows.append((f"Isa {ich}:{iv}", f"2Ki {kch}:{kv}", round(r, 3),
                     "IDENT" if na == nb else "diff",
                     " ".join(only_i), " ".join(only_k)))

ident = sum(1 for r in rows if r[3] == "IDENT")
tot = len(rows)
print(f"ALIGNED PAIRS: {tot} | IDENTICAL (normalised): {ident} | DIFFERING: {tot-ident}")
print(f"ISAIAH-ONLY verses: {len(ISA_ONLY)} | KINGS-ONLY verses: {len(KGS_ONLY)}")
mean = sum(r[2] for r in rows if r[2] is not None)/sum(1 for r in rows if r[2] is not None)
print(f"MEAN SIMILARITY: {mean:.3f}")
print(f"PAIRS BELOW 0.60 SIMILARITY: {sum(1 for r in rows if r[2] is not None and r[2]<0.60)}")
print()
print("REF-ISA | REF-KGS | SIM | STATUS | ISAIAH-ONLY WORDS | KINGS-ONLY WORDS")
for r in rows:
    if r[3] == "IDENT":
        print(f"{r[0]} | {r[1]} | 1.000 | IDENT | | ")
    else:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")

with open("/tmp/synoptic_rows.json","w",encoding="utf-8") as f:
    json.dump([{"isa":r[0],"kgs":r[1],"sim":r[2],"status":r[3],"isa_only":r[4],"kgs_only":r[5]} for r in rows], f, ensure_ascii=False, indent=1)
