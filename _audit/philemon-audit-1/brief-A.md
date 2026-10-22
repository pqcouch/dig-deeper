# Brief — Auditor A (lexical constituents, rivals, Greek)

You are a blind auditor of two claims about Paul's letter to Philemon. Read `claims.md` in this folder. **Your remit: the lexical and grammatical constituents — P1a, P1b, P1d, P2a — and the Greek sense questions under P2b and P2c.** A second auditor will run the chance baselines for the design claims (P1c, P2b); do not do that work at length, but say anything a baseline must take into account.

## Blindness — strict
Work **only** from `/home/claude/phlm-audit/` (this folder and `corpus/`). **Do not open** anything under `/mnt/user-data`, `/home/claude/.private-hold`, `/tmp`, `~/.claude`, `/root`, or any other folder; do not search the web. Your knowledge of the Greek, of Paul and of the scholarship is allowed and expected, but mark anything not verified in the corpus as recalled.

## The corpus
- `corpus/README.md` — read it first.
- SBLGNT text `corpus/greek-nt-sblgnt/NN-Book.txt`; word index `corpus/greek-nt-sblgnt/_index/NN-Book.tsv` (columns ref, word, lemma, pos, parse; parse is person, tense, voice, mood, case, number, gender, degree).
- `corpus/tools/find.py glemma <lemma> [Book]` lists every NT occurrence of a lemma.
- Swete LXX `corpus/greek-lxx-swete/*.txt`: no lemma index. Search accent-stripped word-beginnings, and **read every hit for sense** (a stem can match another word). Augmented verbs are missed by word-beginning searches (ἀνέπαυσα vs ἀναπαυ- is fine; ὑπήκουσα vs ὑπακου- is not) — search augmented stems as well.
- NA28 text and apparatus for Philemon in `corpus/logos-exports/02-New-Testament/`.

## Rules
1. **Lemma, never surface form**, for NT chains. Confirm each claimed reference contains the lemma.
2. **Positive control before any nil or "only" result:** run the identical search on a case known to be present and show it returned. If the control fails, the search is broken.
3. **"Only" and "nowhere else" are measurements.** Test each one over the stated corpus (NT; Swete).
4. For P1b, check the vocative by parse, and say how many NT letters were searched.
5. For P2a–c: classify each ὑπέρ by case and sense (genitive "on behalf of" / accusative "beyond, more than"); say whether the three constitute a lexical chain in any meaningful sense, or a common preposition in two different constructions. Give ὑπέρ's frequency per 1,000 words in Philemon against Paul's other letters (SBLGNT) so the second auditor has it.
6. For P1d, verify the 2 Cor 7 claims and say whether shared idiom across two letters strengthens or weakens a design claim in one of them, and why.
7. Look for **rivals and omissions**: any other pair of verses in Philemon that frames the body as well as or better than 7/20; any other Pauline text where the same σπλάγχνα / ἀναπαύω pattern frames a request.
8. State every search in words in your report (the Greek in its own script with a gloss, the edition, the result) — no code in the report.

## Deliverable
Write `auditor-A/report.md`: for each sub-claim — what you checked, the result, a verdict (Confirmed / Confirmed with nuance / Needs reframing / Uncertain / Discard) and a confidence. End with a list of spot checks the main session can reproduce (as sentences), and any corrections to the claims as worded. Keep it under about 2,500 words.
