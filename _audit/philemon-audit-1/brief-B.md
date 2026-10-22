# Brief — Auditor B (design claims and chance baselines)

You are a blind auditor of two design claims about Paul's letter to Philemon. Read `claims.md` in this folder. **Your remit: P1c and P2b–P2c — whether the claimed patterns occur more often than chance would produce.** A first auditor has checked the lexical constituents; you may read `auditor-A/report.md` *after* you have designed your baselines (not before), and should say where you agree or disagree.

## Blindness — strict
Work **only** from `/home/claude/phlm-audit/` (this folder and `corpus/`). **Do not open** anything under `/mnt/user-data`, `/home/claude/.private-hold`, `/tmp`, `~/.claude`, `/root`, or any other folder; do not search the web. Your own knowledge is allowed, marked as recalled.

## The corpus
- `corpus/README.md` first. SBLGNT text and word index in `corpus/greek-nt-sblgnt/` (index columns ref, word, lemma, pos, parse). `corpus/tools/find.py glemma <lemma> [Book]`. Swete LXX in `corpus/greek-lxx-swete/` (no lemma index; word-beginning searches, read hits for sense).

## What to test

**P1c — the frame.** Is a pair of verses in a short letter that (i) share two content lemmas found together nowhere else in the letter, (ii) sit near the two ends of the letter body, and (iii) also share a third feature (here the vocative ἀδελφέ) unusual? Design at least two baselines, for example:
- **Within-Philemon:** of all verse pairs in Philemon at least 8 verses apart, how many share two or more content lemmas (exclude articles, pronouns, conjunctions, particles, prepositions, εἰμί, and very common words — state your stoplist) that co-occur nowhere else in the letter? Where do 7/20 rank?
- **Cross-letter:** in comparably short letters (2 John, 3 John, Jude, Titus; and in sliding 25-verse windows across Paul's letters), how often does some verse pair near the two ends of a body share two exclusive content lemmas? A pattern that most short texts show is not evidence of design.
- **Leave-one-out:** does the result survive if σπλάγχνον, or ἀναπαύω, or the vocative is removed?
Also weigh the Pauline idiom (2 Cor 7:13–15) as a rival: if the words are idiom, is their placement still design?

**P2b–c — the ὑπέρ escalation.** ὑπέρ is a common preposition. Test whether three occurrences in Philemon, spread across the body, is more than expected from ὑπέρ's rate in Paul (per 1,000 words; SBLGNT) — that is, whether any "sequence" exists that a reader would notice, and whether the claim depends on English translations rendering two different constructions with "more". Then say whether P2c (v. 13 → v. 21 leaning v. 21 towards release to Paul's service) follows from the text, follows only from the "sequence", or does not follow; consider the alternatives (manumission; better treatment; no specific content).

## Rules
- Lemma searches for NT chains; **positive controls before any nil**; "only" is a measurement.
- Report windows and thresholds in words ("25-verse windows"; "lemmas in at most 3 verses of the letter"), never as code or parameter symbols; state every search in words in the report.
- Keep the number of runs proportionate; a few clear baselines beat many.

## Deliverable
Write `auditor-B/report.md`: for P1c and for P2b–c — the baselines run, the results (with numbers), a verdict (Confirmed / Confirmed with nuance / Needs reframing / Uncertain / Discard) and a confidence; your agreement or disagreement with auditor A; and a list of spot checks the main session can reproduce (as sentences). Under about 2,500 words.
