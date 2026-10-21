# Claim audit — Colossians — brief for a blind auditor

You are one of two **blind auditors** testing intertextual and design claims made about Paul's letter to the Colossians. Your job is to try to **break** each claim, not to defend it. A claim survives only if it survives your attempt.

## Blindness rules (strict)
- Read **only** this brief, your claims file, and the primary texts in `/home/claude/colaudit/_texts/`.
- Do **not** open anything under `/home/claude/col/`, `/home/claude/edit/`, `/mnt/user-data/`, `/home/claude/colaudit/auditor-*.md` (another auditor's report), any project document, any memory tool, or the web. Do not use the Projects, Artifact or memory tools. The reports that made these claims must not influence you.
- You may use your own knowledge of scholarship, but anything from memory is tagged `[S]` and cannot carry a verdict on its own.

## The corpus (`/home/claude/colaudit/_texts/`; read `README.md` first)
- `greek-nt-sblgnt/` — SBLGNT text by book (`12-Col.txt`, lines like `Col 1:1<TAB>text`) and a lemma index `_index/NN-Book.tsv` (ref, word, lemma, pos, parse). **Count NT words by lemma.**
- `greek-lxx-swete/` — Swete's LXX by book (plain text, one verse per line, e.g. `Psa 67:17`; Psalms use LXX numbering). **No lemma index**: search accent-stripped word-beginnings, and **read every matched word for sense** (a stem can catch a different word — καταλλαγή "exchange" under καταλλάσσω; ὁρᾶτε "see!" under ὁρατός). Counts in Swete are floors.
- `hebrew-wlc/` — WLC Hebrew with a lemma index.
- `logos-exports/` — NA28 and NA28 apparatus for Colossians, NA28 Ephesians, ESV/NASB95/NIV84 Colossians; Rahlfs LXX for Psalms, Proverbs, Isaiah, Genesis, Daniel (OG and Theodotion); BHS Psalms, Isaiah. Use Rahlfs to check that a wording claim made from Swete holds in Rahlfs.
- Tools: `python3 -I _texts/tools/find.py --help` (lemma search, co-occurrence, `near`), and `python3 -I _texts/tools/contacts.py ntscan <Book>:<ch>:<v>-<v> [--check "Psa 88,Isa 45"]`, which ranks every Swete chapter and 8- and 16-verse window against an NT passage in six runs (chapters / 8-verse / 16-verse, each with all words and with rarer words) and prints the matched stems. It takes a passage within one chapter only. Run commands from `/home/claude/colaudit`. You may write your own scripts in `/home/claude/colaudit/work-<your letter>/`.

## Method (required)
1. **Reproduce every stated count first.** State whether it holds exactly, and correct it if not.
2. **Positive control before any nil or "only" result:** run the same search on a reference known to contain the item and see it returned. A search that fails its control proves nothing.
3. **Rival search:** look for closer or equal sources the claim did not name, in Swete and (where relevant) the WLC and the NT.
4. **Chance baselines for design and field claims:** ask how often the claimed pattern or rank arises for comparable, arbitrary passages (null passages). A rank or overlap is evidence only if it beats the null; report the null distribution in plain numbers. Report any window rank under at least two settings.
5. **Hays criteria** for each allusion claim (Availability, Volume, Recurrence, Thematic coherence, Historical plausibility, History of interpretation — from your own knowledge, tagged `[S]` — Satisfaction), each Strong / Possible / Weak.
6. **Verdict** for each claim: Confirmed / Confirmed with nuance / Needs reframing / Uncertain — flag for research / Discard, with a **recommended rating** (high / moderate–high / moderate / low–moderate / low).

## Report (write to `/home/claude/colaudit/auditor-<LETTER>.md`)
- British English. Greek and Hebrew in their own script with an English gloss in brackets. **No code, commands, script names, file paths, or parameter symbols in the report** — state every search in words: the words searched, the edition, the result (e.g. "εὐδοκέω ('be pleased') with κατοικέω ('dwell') in one verse: Ps 67:17 only (Swete)").
- For each claim: what you tested; results; corrections to the stated counts; the Hays table; verdict, recommended rating, and the reason in two or three sentences; anything the claim missed.
- A section **Decisive results for reproduction**: a numbered list of 8–15 one-sentence factual results (with edition) on which your verdicts turn, so the main session can re-check them.
- A section **New candidates** for anything significant you found that the claims did not name.
- Keep it to roughly 4,000–7,000 words. Reply to the main session with a 10-line summary of verdicts only.
