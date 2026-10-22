# Brief — Auditor A (single contacts: P3, P4, P5, P7)

You are a blind auditor of claims about Paul's letter to Philemon. Read `claims.md`. **Your remit: P3, P4, P5 and P7** — wording, rarity, rival texts, Greek sense. A second auditor will take P6 and P8 (the cross-letter claims); you may note anything relevant to them briefly.

## Blindness — strict
Work only inside `/home/claude/phlm-audit-2/`. Do not open anything outside it (not `/mnt/user-data`, `/home/claude/.private-hold`, `/home/claude/phlm-audit`, `/tmp`, `~/.claude`, `/root`), and do not use the web. Your own knowledge of Greek, Hebrew, Paul and the scholarship is allowed; mark anything not verified in the corpus as *recalled*.

## Corpus
`corpus/README.md` first. SBLGNT text and word index (columns ref, word, lemma, pos, parse). Swete has no lemma index: search accent-stripped word-beginnings, **search augmented stems as well** (e.g. ἀπετισ- / ἀπετει- for aorists of ἀποτίνω; ἠδικ- for ἀδικέω), and **read every hit for sense** — a stem can catch another word. WLC Torah and Job in `corpus/hebrew-wlc/` (index columns ref, word, lemma, morph; the lemma field carries homograph letters such as "5650 a" — match the number, not the whole string).

## Rules
1. NT chains by lemma. Every "only", "once", "nowhere else" is a measurement — test it over the stated corpus.
2. **Positive control before any nil**: show the same search returning a case known to be present.
3. For P4 and P5, read the Swete passages in context (Exod 21–22; Lev 5:20–6:7 and 25:39–46 in Swete's numbering; Deut 15:12–18; Job 40:23) and the Hebrew where it helps; say what Hebrew each Greek word renders.
4. For each claim, name **every rival** that shares the wording as closely as the claimed source, or more closely — in Swete, in the NT, and in ordinary Greek where you can (recalled). An allusion whose shared wording occurs in more than about ten verses is idiom and cannot be rated above moderate on wording alone.
5. For P3, check what can be checked (NT occurrences of ἄχρηστος, εὔχρηστος, ὀνίνημι, Ὀνήσιμος, χρηστός, Χριστός; any Swete occurrences); say what cannot be checked in a corpus (pronunciation) and how strong the case is on recalled evidence.
6. State every search in words in the report (the Greek or Hebrew in its own script with a gloss, the edition, the result) — no code.

## Deliverable
You will probably not be allowed to write files: **return your full report as your final reply.** For each claim — what you checked, the results, rivals, a verdict (Confirmed / Confirmed with nuance / Needs reframing / Uncertain / Discard) and a confidence, and a restated claim if it needs one. End with spot checks the main session can reproduce, written as sentences. Under about 2,800 words. British English; Greek and Hebrew in their own script with an English gloss in brackets.
