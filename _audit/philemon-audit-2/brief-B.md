# Brief — Auditor B (cross-letter and design claims: P6, P8)

You are a blind auditor of claims about Paul's letter to Philemon. Read `claims.md`. **Your remit: P6 and P8** — claims that read Philemon together with Colossians (and Ephesians). The first auditor's report on P3, P4, P5 and P7 will be given to you only after you have designed your tests; comment on it briefly at the end.

## Blindness — strict
Work only inside `/home/claude/phlm-audit-2/`. Do not open anything outside it (not `/mnt/user-data`, `/home/claude/.private-hold`, `/home/claude/phlm-audit`, `/tmp`, `~/.claude`, `/root`), and do not use the web. Your own knowledge is allowed, marked *recalled*.

## Corpus
`corpus/README.md` first. SBLGNT text and word index in `corpus/greek-nt-sblgnt/` (columns ref, word, lemma, pos, parse; parse = person, tense, voice, mood, case, number, gender, degree). `corpus/tools/find.py glemma <lemma> [Book]`.

## What to test

**P6.** Is ἀγαπητὸς ἀδελφός ("beloved brother") distinctive enough that Col 4:9 and Phlm 16 can be said to answer each other, or is it a Pauline formula for co-workers? Count every NT verse with ἀγαπητός and ἀδελφός together (and with πιστός, "faithful"), and say of whom each is said. Test the claim's premise — that the two letters went together — against what the texts themselves say (the shared names; Tychicus and Onesimus as carriers, Col 4:7–9; Archippus, Col 4:17 / Phlm 2), and say what follows for P6 if they did not. Is the "public / private" reading supported by anything in the texts beyond the shared phrase?

**P8.** Verify the claimed co-occurrence (σάρξ with κύριος in one verse) across Colossians, Ephesians and Philemon, and **then across all Paul's letters and the NT** — and separate the senses (κύριος as "the Lord" and as human "master"; σάρξ as "body, human sphere" and as "sinful nature"). Find every NT instance of κατὰ σάρκα ("according to the flesh") and ἐν σαρκί ("in the flesh") with a human-relations sense. Is the contrast between Col 3:22 / Eph 6:5 and Phlm 16 more than the ordinary Pauline pairing of "flesh" and "Lord" spheres (compare, e.g., Rom 9:3–5; 2 Cor 5:16; Phil 3:3 — recalled; verify)? Run a simple baseline: how often do two Pauline verses in different letters share σάρξ + κύριος in any sense?

## Rules
- Lemma searches; positive controls before any nil; "only" is a measurement.
- State every search in words (Greek in its own script with a gloss; edition; result) — no code or parameter symbols in the report.

## Deliverable
You will probably not be allowed to write files: **return your full report as your final reply.** For P6 and P8 — the tests, the results with numbers, a verdict (Confirmed / Confirmed with nuance / Needs reframing / Uncertain / Discard) and confidence, a restated claim if needed; then brief comments on auditor A's report; then spot checks as sentences. Under about 2,500 words. British English.
