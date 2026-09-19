#!/usr/bin/env python3
"""check_card_transmission.py — the standing post-card check, in one command.

A skill proposal card replaces a whole SKILL.md by retyping it, and this project
has twice had that go wrong silently: Round 3 lost a paragraph, Round 4 damaged
three Hebrew words (an Arabic letter for a segol, two missing dageshim). So a card
is not finished until the installed file has been checked against the text that was
intended.

    python3 check_card_transmission.py <installed SKILL.md> <intended SKILL.md> [WLC dir]

Reports, in order:
  1. Byte-identical?  (the happy case — stop here)
  2. NFC/NFD-equivalent?  A card's transmission applies NFC; the WLC corpus does not.
     Two files that differ only in combining-mark ORDER are canonically equal, render
     identically, and are harmless. This check separates that from real damage.
  3. Line-level diff, if any.
  4. Hebrew audit: every Hebrew string in the installed file, checked for stray
     non-Hebrew codepoints (the Round 4 failure) and, where a WLC directory is given,
     for presence in the corpus.

Exit status 0 = clean (identical, or equivalent with no Hebrew damage); 1 = look at it.
"""
import sys, os, re, glob, difflib, unicodedata

HEB = re.compile(r'[֐-׿יִ-ﭏ]+')


def load(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def nfc(s):
    return unicodedata.normalize("NFC", s)


def strip_marks(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if not unicodedata.combining(c))


def hebrew_strings(s):
    return HEB.findall(s)


def wlc_index(wlc_dir):
    """Map every Hebrew word-form and verse text in the corpus, for presence checks."""
    texts = []
    for p in glob.glob(os.path.join(wlc_dir, "**", "*.txt"), recursive=True):
        if "_index" in p:
            continue
        with open(p, encoding="utf-8") as fh:
            for line in fh:
                if "\t" in line:
                    ref, txt = line.rstrip("\n").split("\t", 1)
                    texts.append((ref, txt))
    return texts


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    installed, intended = sys.argv[1], sys.argv[2]
    wlc = sys.argv[3] if len(sys.argv) > 3 else None

    for p in (installed, intended):
        if not os.path.isfile(p):
            print("MISSING: %s" % p)
            return 2

    a, b = load(installed), load(intended)
    print("installed : %7d bytes  %4d lines  %s" % (len(a.encode()), a.count("\n"), installed))
    print("intended  : %7d bytes  %4d lines  %s" % (len(b.encode()), b.count("\n"), intended))
    print()

    problems = 0

    # ---- 1. byte-identical ----------------------------------------------
    if a == b:
        print("1. BYTE-IDENTICAL — the card transmitted the file exactly. Nothing else to check.")
        return 0
    print("1. Not byte-identical. Continuing.")

    # ---- 2. canonical equivalence ---------------------------------------
    if nfc(a) == nfc(b):
        print("2. CANONICALLY EQUAL under NFC — the files differ only in the order of")
        print("   combining marks. This is the known, harmless card/corpus difference:")
        print("   the card applies NFC (marks sorted by canonical class), the WLC does not")
        print("   (dagesh kept immediately after its consonant). Renders identically;")
        print("   compares equal under NFD-stripping, so chain verification is unaffected.")
    else:
        problems += 1
        print("2. NOT canonically equal — there is a real difference in content.")

    # ---- 3. line diff ----------------------------------------------------
    al, bl = a.split("\n"), b.split("\n")
    diff = [l for l in difflib.unified_diff(bl, al, "intended", "installed", n=0, lineterm="")]
    if diff:
        changed = [l for l in diff if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        print()
        print("3. %d changed line(s):" % len(changed))
        for l in diff[:80]:
            if l[:3] in ("+++", "---"):
                continue
            print("   " + (l[:300] + (" …" if len(l) > 300 else "")))
        if len(diff) > 80:
            print("   … (%d more diff lines)" % (len(diff) - 80))
    else:
        print()
        print("3. No line-level differences.")

    # ---- 4. Hebrew audit -------------------------------------------------
    print()
    print("4. Hebrew audit of the INSTALLED file")
    inst_heb = sorted(set(hebrew_strings(a)))
    intd_heb = sorted(set(hebrew_strings(b)))
    print("   distinct Hebrew strings: installed %d, intended %d" % (len(inst_heb), len(intd_heb)))

    # 4a. strays: any codepoint that is not Hebrew-block inside a Hebrew run
    stray = []
    for w in inst_heb:
        bad = [c for c in w if not (0x0590 <= ord(c) <= 0x05FF or 0xFB1D <= ord(c) <= 0xFB4F)]
        if bad:
            stray.append((w, bad))
    if stray:
        problems += 1
        print("   !! STRAY NON-HEBREW CODEPOINTS (the Round 4 failure mode):")
        for w, bad in stray:
            print("      %s  ->  %s" % (w, " ".join("U+%04X (%s)" % (ord(c), unicodedata.name(c, "?")) for c in bad)))
    else:
        print("   OK  no stray codepoints — every character sits in the Hebrew block")

    # 4b. anything present in one file but not the other, ignoring mark order
    ai = {nfc(w) for w in inst_heb}
    bi = {nfc(w) for w in intd_heb}
    only_i = sorted(w for w in ai - bi)
    only_b = sorted(w for w in bi - ai)
    if only_i or only_b:
        problems += 1
        print("   !! Hebrew present in one file and not the other (NFC-normalised):")
        for w in only_b:
            print("      MISSING from installed: %s" % w)
        for w in only_i:
            print("      EXTRA in installed    : %s" % w)
    else:
        print("   OK  the same set of Hebrew strings in both, NFC-normalised")

    # 4c. corpus presence, if a WLC directory was supplied
    if wlc:
        print()
        print("   Corpus check against %s" % wlc)
        verses = wlc_index(wlc)
        for w in inst_heb:
            hits = [r for r, t in verses if w in t]
            if hits:
                print("   OK  %-22s %d verse(s), e.g. %s" % (w, len(hits), hits[0]))
            else:
                skel = strip_marks(w)
                sk = [r for r, t in verses if skel and skel in strip_marks(t)]
                if sk:
                    print("   ~   %-22s 0 exact, %d consonantal (accents differ — normal for a "
                          "citation form)" % (w, len(sk)))
                else:
                    problems += 1
                    print("   !!  %-22s not found in the corpus, even consonantally — check it" % w)

    print()
    print("VERDICT: %s" % ("clean" if problems == 0 else "%d thing(s) to look at" % problems))
    return 0 if problems == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
