#!/usr/bin/env python3
"""Mechanical synoptic diff v2: Isa 36:1-39:8 // 2 Kgs 18:13-20:21 (WLC).

Two passes.
  Pass 1 -- consonantal: NFD-strip combining marks; maqqef, paseq, sof pasuq
            normalised to spaces; reduce to Hebrew consonants + space.
  Pass 2 -- skeletal: additionally delete waw and yod (the principal matres
            lectionis) and word-final he, so that a pair differing only in
            plene/defective spelling collapses to identity.

A pair identical in pass 2 but not pass 1 is ORTHOGRAPHIC.
A pair differing in pass 2 is SUBSTANTIVE (different words, not spelling).
"""
import unicodedata, difflib, sys, re, json

ISA_F, KGS_F = sys.argv[1], sys.argv[2]

def load(path):
    d = {}
    for line in open(path, encoding="utf-8"):
        if "\t" not in line: continue
        ref, txt = line.rstrip("\n").split("\t", 1)
        d[ref.strip()] = txt.strip()
    return d

def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    for ch in ("־", "׀", "׃", "׆"):   # maqqef paseq sof-pasuq nun
        s = s.replace(ch, " ")
    s = re.sub(r"[^א-ת ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

FIN = {"ך":"כ","ם":"מ","ן":"נ","ף":"פ","ץ":"צ"}
def skel(s):
    out = []
    for w in norm(s).split():
        w = "".join(FIN.get(c, c) for c in w)
        if w.endswith("ה") and len(w) > 2: w = w[:-1]      # final he
        w = w.replace("ו", "").replace("י", "")        # waw, yod
        out.append(w or "-")
    return " ".join(out)

isa, kgs = load(ISA_F), load(KGS_F)
ip = [k.rsplit(" ",1)[0] for k in isa if k.endswith(" 36:1")][0]
kp = [k.rsplit(" ",1)[0] for k in kgs if k.endswith(" 18:13")][0]
def I(cv): return isa.get(f"{ip} {cv}")
def K(cv): return kgs.get(f"{kp} {cv}")

# (isa refs, kgs refs) -- lists, so merges/transpositions are explicit
def rng(ch, a, b): return [f"{ch}:{v}" for v in range(a, b+1)]
PAIRS = []
PAIRS += [ (["36:1"], ["18:13"]) ]
PAIRS += [ ([f"36:{v}"], [f"18:{v+15}"]) for v in range(2, 23) ]
PAIRS += [ ([f"37:{v}"], [f"19:{v}"])    for v in range(1, 15) ]
PAIRS += [ (["37:15","37:16"], ["19:15"]) ]                    # Isaiah splits
PAIRS += [ ([f"37:{v}"], [f"19:{v-1}"])  for v in range(17, 39) ]
PAIRS += [ ([f"38:{v}"], [f"20:{v}"])    for v in range(1, 4) ]
PAIRS += [ (["38:4"], ["20:4"]), (["38:5"], ["20:5","20:6"]), (["38:6"], ["20:6"]) ]
PAIRS += [ (["38:7"], ["20:9"]), (["38:8"], ["20:10","20:11"]) ]
PAIRS += [ (["38:21"], ["20:7"]), (["38:22"], ["20:8"]) ]      # TRANSPOSED
PAIRS += [ ([f"39:{v}"], [f"20:{v+11}"]) for v in range(1, 9) ]

ISA_ONLY = rng("38", 9, 20)
KGS_ONLY = ["18:14","18:15","18:16","20:20","20:21"]

rows, missing = [], []
for irefs, krefs in PAIRS:
    a = " ".join(filter(None, (I(r) for r in irefs)))
    b = " ".join(filter(None, (K(r) for r in krefs)))
    if not a or not b:
        missing.append((irefs, krefs)); continue
    na, nb, sa, sb = norm(a), norm(b), skel(a), skel(b)
    if na == nb:      status = "IDENTICAL"
    elif sa == sb:    status = "ORTHOGRAPHIC"
    else:             status = "SUBSTANTIVE"
    r = difflib.SequenceMatcher(None, na.split(), nb.split()).ratio()
    wa, wb = na.split(), nb.split()
    sm = difflib.SequenceMatcher(None, skel(a).split(), skel(b).split())
    oi, ok = [], []
    for tag, i_, j_, k_, l_ in sm.get_opcodes():
        if tag in ("replace","delete"): oi += wa[i_:j_]
        if tag in ("replace","insert"): ok += wb[k_:l_]
    rows.append({"isa":"+".join(irefs), "kgs":"+".join(krefs), "sim":round(r,3),
                 "status":status, "isa_only":" ".join(oi), "kgs_only":" ".join(ok),
                 "iw":len(wa), "kw":len(wb)})

n = len(rows)
c = lambda s: sum(1 for r in rows if r["status"]==s)
iw = sum(r["iw"] for r in rows); kw = sum(r["kw"] for r in rows)
print(f"ALIGNED UNITS: {n}   (missing/unaligned: {len(missing)})")
print(f"  IDENTICAL to the consonant ........ {c('IDENTICAL'):>3}  ({c('IDENTICAL')/n:.0%})")
print(f"  ORTHOGRAPHIC difference only ...... {c('ORTHOGRAPHIC'):>3}  ({c('ORTHOGRAPHIC')/n:.0%})")
print(f"  SUBSTANTIVE difference ............ {c('SUBSTANTIVE'):>3}  ({c('SUBSTANTIVE')/n:.0%})")
print(f"  IDENTICAL + ORTHOGRAPHIC combined . {c('IDENTICAL')+c('ORTHOGRAPHIC'):>3}"
      f"  ({(c('IDENTICAL')+c('ORTHOGRAPHIC'))/n:.0%})")
print(f"Words in aligned material: Isaiah {iw} | Kings {kw}  (Kings longer by {kw-iw})")
print(f"Isaiah-only verses: {len(ISA_ONLY)} ({ISA_ONLY[0]}-{ISA_ONLY[-1]}) | Kings-only verses: {len(KGS_ONLY)} ({', '.join(KGS_ONLY)})")
print()
print("== SUBSTANTIVE DIFFERENCES ONLY ==")
print("ISA | KGS | sim | ISAIAH-ONLY WORDS || KINGS-ONLY WORDS")
for r in rows:
    if r["status"] == "SUBSTANTIVE":
        print(f'{r["isa"]} | {r["kgs"]} | {r["sim"]} | {r["isa_only"]} || {r["kgs_only"]}')
print()
print("== ORTHOGRAPHIC-ONLY PAIRS (spelling, not wording) ==")
print(", ".join(f'{r["isa"]}' for r in rows if r["status"]=="ORTHOGRAPHIC"))
print()
print("== IDENTICAL TO THE CONSONANT ==")
print(", ".join(f'{r["isa"]}={r["kgs"]}' for r in rows if r["status"]=="IDENTICAL"))
if missing: print("\nUNALIGNED:", missing)
json.dump(rows, open("/tmp/synoptic_rows.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
