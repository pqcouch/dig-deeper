# Claim audit 1 — Obadiah — brief for a blind auditor

You are one of two **blind auditors** testing intertextual and design claims made about the book of Obadiah. Your job is to try to **break** each claim, not to defend it. A claim survives only if it survives your attempt.

## Blindness rules (strict)
- Read **only** this brief, your claims file, and the primary texts in `/home/claude/obaudit/_texts/`.
- Do **not** open anything under `/mnt/user-data/`, `/home/claude/*.md`, `/home/claude/obaudit/auditor-*.md` (another auditor's report), any project document, any memory tool, or the web. Do not use the Projects, Artifact or memory tools, or any tool that reaches the user's computer. The reports that made these claims must not influence you.
- You may use your own knowledge of scholarship, but anything from memory is tagged `[S]` and cannot carry a verdict on its own.

## The corpus (`/home/claude/obaudit/_texts/`; read `README.md` first)
- `hebrew-wlc/` — WLC Hebrew, Tanak order, with a lemma index in `_index/`. **Count Hebrew by lemma.** The index carries homograph letters and prefixed morphemes, so use the tools rather than an equality test. Bare ס and פ are paragraph markers, not words. Unpointed words are ketivs. **WLC uses Hebrew versification:** Joel 3:5 = English 2:32; Joel 4 = English 3; Ps 7:17 = English 7:16; Ps 22:29 = 22:28; Ps 41:10 = 41:9; Mal 3:19 = 4:1. Check the neighbouring verse before reporting a miss.
- `greek-lxx-swete/` — Swete's LXX (no lemma index; search accent-stripped text; **read every matched word for sense**; word-beginning searches miss augmented verbs). Counts are floors. Swete's Twelve are in LXX order.
- `greek-nt-sblgnt/` — SBLGNT with lemma index.
- `logos-exports/` — **Rahlfs LXX** for the Hebrew canon; for Obadiah also BHS, the BHS apparatus, NASB95 and ESV. The BHS text file carries note letters inside the words; search the WLC, cite BHS.
- Tools, run from `/home/claude/obaudit`: `python3 -I _texts/tools/find.py --help` (lemma search, co-occurrence, `near`, `verify`) and `python3 -I _texts/tools/contacts.py` (`all <lemmas> [--window n]` for how rare a set is; `phrase "<words>"` for an ordered phrase, plain and skeletal; `scan Obad [--min 5] [--top n]` for chapters ranked by rare shared vocabulary). A scan works verse against verse and measures vocabulary, not borrowing. You may write your own scripts in `/home/claude/obaudit/work-<your letter>/`, validating them against `find.py` on a known-positive lemma first.

## Method (required)
1. **Reproduce every stated count first.** State whether it holds exactly, and correct it if not. *Only*, *identical*, *verbatim* and superlatives are claims about shape: test with an ordered phrase search, plain and skeletal.
2. **Positive control before any nil or "only" result:** run the same search on a reference known to contain the item and see it returned.
3. **Rival search:** look for closer or equal sources the claim did not name, in the WLC, Swete and the NT. An allusion whose wording occurs in more than about ten verses is idiom.
4. **Read the source in context.** Does the source passage's own sense support the claimed use? Check that a shared lemma has the same sense in both places.
5. **Chance baselines for design and field claims:** ask how often the claimed pattern arises for comparable, arbitrary passages or by reshuffling. Evidence counts only if it beats the null; report the null in plain numbers. Use leave-one-out where a pattern may rest on one word.
6. **Direction of dependence is not assumed.** Say "shares wording with", not "quotes", unless the text marks it; say what evidence, if any, bears on direction.
7. **Hays criteria** for each allusion claim (Availability, Volume, Recurrence, Thematic coherence, Historical plausibility, History of interpretation — from your own knowledge, tagged `[S]` — Satisfaction), each Strong / Possible / Weak. For design claims, replace the table with: Counts verified · Baseline · Sense · Alternative explanation.
8. **Verdict** for each claim: Confirmed / Confirmed with nuance / Needs reframing / Uncertain — flag for research / Discard, with a **recommended rating** (high / moderate–high / moderate / low–moderate / low).

## Report (write to `/home/claude/obaudit/auditor-<LETTER>.md`)
- British English. Hebrew and Greek in their own script with an English gloss in brackets after every use. **No code, commands, script names, file paths, word-index numbers or parameter symbols in the report** — state every search in words: the words searched, the edition, the result (e.g. "עֵד ('witness') with קוּם ('rise') in one verse: Deut 19:16 and Job 16:8 only (WLC)").
- For each claim: what you tested; results; corrections to the stated counts; the table; verdict, recommended rating, and the reason in two or three sentences; anything the claim missed.
- A section **Decisive results for reproduction**: a numbered list of 8–15 one-sentence factual results (with edition) on which your verdicts turn, so the main session can re-check them.
- A section **New candidates** for anything significant you found that the claims did not name.
- Roughly 4,000–7,000 words. History of interpretation: only what you recall, tagged `[S]`; it cannot move a verdict.
- Reply to the main session with a 10-line summary of verdicts only.
