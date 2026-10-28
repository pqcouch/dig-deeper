# Claim audit 3 — Colossians — brief for a blind auditor

You are one of two **blind auditors** testing intertextual and design claims made about Paul's letter to the Colossians. Your job is to try to **break** each claim, not to defend it. A claim survives only if it survives your attempt.

## Blindness rules (strict)
- Read **only** this brief, your claims file, and the primary texts in `/home/claude/colaudit3/_texts/`.
- Do **not** open anything under `/mnt/user-data/`, `/home/claude/colaudit3/auditor-*.md` (another auditor's report), any project document, any memory tool, or the web. Do not use the Projects, Artifact or memory tools. The reports that made these claims, and any earlier audit, must not influence you.
- You may use your own knowledge of scholarship, but anything from memory is tagged `[S]` and cannot carry a verdict on its own.

## The corpus (`/home/claude/colaudit3/_texts/`; read `README.md` first)
- `greek-nt-sblgnt/` — SBLGNT text by book (`12-Col.txt`, lines like `Col 1:1<TAB>text`) and a lemma index `_index/NN-Book.tsv` (ref, word, lemma, pos, parse). **Count NT words by lemma.** Beware: the index files many verbs under a deponent form (ῥιζόομαι, συνθάπτομαι, δογματίζομαι), so check the lemma in the index before concluding a nil. Rom 16:25–27 is not in the SBLGNT index; it is in the NA28 export.
- `greek-lxx-swete/` — Swete's LXX by book (one verse per line, e.g. `Psa 67:17`; Psalms in LXX numbering; `Tob`/`Tbs` are Tobit's two texts, `Dat` is Theodotion's Daniel, `Pss` is the Psalms of Solomon — do not count it as Psalms). **No lemma index**: search accent-stripped text, and **read every matched word for sense** (a stem can catch a different word). **Word-beginning searches miss augmented and reduplicated verbs** (ἐβράβευσεν under βραβεύω; ἁψάμενος under ἅπτω) — search for the stem anywhere in the word as a control. Counts in Swete are floors.
- `hebrew-wlc/` — WLC Hebrew with a lemma index.
- `logos-exports/` — NA28 and NA28 apparatus for Colossians; NA28 Romans, 1 Corinthians, Ephesians; ESV/NASB95/NIV84 Colossians; **Rahlfs LXX and BHS** for Genesis, Exodus, Leviticus, Deuteronomy, Joshua, Isaiah, Psalms, Proverbs, Daniel (OG and Theodotion), Chronicles (1 and 2 in one file), Haggai, and Rahlfs for Hosea; NA28 for Romans, 1 Corinthians, Galatians (if present) and Ephesians. **There is no Rahlfs export for Wisdom, Sirach, Tobit, Judith or the Maccabees**: for those books Swete is the only Greek text available; say so where a finding depends on it.
- Tools: `python3 -I _texts/tools/find.py --help` (lemma search, co-occurrence, `near`), and `python3 -I _texts/tools/contacts.py ntscan <Book>:<ch>:<v>-<v> [--check "Wis 6,Isa 29"]`, which ranks every Swete chapter and 8- and 16-verse window against an NT passage in six runs and prints the matched stems with `--check`. It takes a passage within one chapter only. Run commands from `/home/claude/colaudit3`. You may write your own scripts in `/home/claude/colaudit3/work-<your letter>/`.

## Method (required)
1. **Reproduce every stated count first.** State whether it holds exactly, and correct it if not.
2. **Positive control before any nil or "only" result:** run the same search on a reference known to contain the item and see it returned. A search that fails its control proves nothing.
3. **Rival search:** look for closer or equal sources the claim did not name, in Swete and (where relevant) the WLC and the NT.
4. **Chance baselines for design and field claims:** ask how often the claimed pattern or rank arises for comparable, arbitrary passages (null passages). A rank or overlap is evidence only if it beats the null; report the null distribution in plain numbers. Report any window rank under at least two settings. Use leave-one-out for field claims (does the result survive without its single strongest word?).
5. **Hays criteria** for each allusion claim (Availability, Volume, Recurrence, Thematic coherence, Historical plausibility, History of interpretation — from your own knowledge, tagged `[S]` — Satisfaction), each Strong / Possible / Weak. For design claims inside Colossians, replace the Hays table with: Counts verified · Baseline · Sense · Alternative explanation.
6. **Verdict** for each claim: Confirmed / Confirmed with nuance / Needs reframing / Uncertain — flag for research / Discard, with a **recommended rating** (high / moderate–high / moderate / low–moderate / low).

## Report (write to `/home/claude/colaudit3/auditor-<LETTER>.md`)
- British English. Greek and Hebrew in their own script with an English gloss in brackets after every use. **No code, commands, script names, file paths, or parameter symbols in the report** — state every search in words: the words searched, the edition, the result (e.g. "εὐδοκέω ('be pleased') with κατοικέω ('dwell') in one verse: Ps 67:17 only (Swete)").
- For each claim: what you tested; results; corrections to the stated counts; the Hays (or design) table; verdict, recommended rating, and the reason in two or three sentences; anything the claim missed.
- A section **Decisive results for reproduction**: a numbered list of 8–15 one-sentence factual results (with edition) on which your verdicts turn, so the main session can re-check them.
- A section **New candidates** for anything significant you found that the claims did not name.
- Keep it to roughly 4,000–7,000 words.
- History of interpretation: give only what you recall, tagged `[S]`; it will be checked separately against Patrick's Logos answers and cannot move a verdict. Reply to the main session with a 10-line summary of verdicts only.
