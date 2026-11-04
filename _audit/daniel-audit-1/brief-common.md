# Claim audit 1 — Daniel — brief for a blind auditor

You are one of two **blind auditors** testing intertextual and design claims made about the book of Daniel. Your job is to try to **break** each claim, not to defend it. A claim survives only if it survives your attempt.

## Blindness rules (strict)
- Read **only** this brief, your claims file, and the primary texts in `/home/claude/danaudit1/_texts/`.
- Do **not** open anything under `/mnt/user-data/` except to copy the bundle, any file named `auditor-*.md` (another auditor's report), any project document, any memory tool, or the web. Do not use the Projects, Artifact, memory, or remote-device tools. The reports that made these claims must not influence you.
- You may use your own knowledge of scholarship, but anything from memory is tagged `[S]` and cannot carry a verdict on its own.

## Setup
`mkdir -p /home/claude/danaudit1 && cd /home/claude/danaudit1 && tar xzf /mnt/user-data/uploads/dig-deeper/_audit/daniel-audit-1/texts-bundle.tgz` (if that path is missing, list `/mnt/user-data/uploads/` to find the staged bundle). Then read `_texts/README.md`.

## The corpus (`/home/claude/danaudit1/_texts/`)
- `hebrew-wlc/` — WLC Hebrew **and Aramaic**, Tanak order, one verse per line, with a lemma index `_index/` (ref, word, lemma, morph). **Count by lemma.** The lemma field carries homograph suffixes (`2617 a`); use the corpus tool, not an equality test. **Aramaic words have their own lemma numbers**, so a lemma search cannot find a Hebrew word answered by its Aramaic cognate: Daniel 2:4b–7:28 is Aramaic, and any Hebrew–Aramaic contact must be tested by reading the two texts, and said so. WLC prints ketiv forms unpointed; lemma searches survive them, surface searches do not.
- `greek-lxx-swete/` — Swete's LXX (no lemma index: search accent-stripped text, read every matched word for sense; counts are floors). `48-Daniel-OG.txt` and `49-Daniel-Theodotion.txt`.
- `greek-nt-sblgnt/` — SBLGNT with a lemma index.
- `logos-exports/` — BHS text and apparatus, **Rahlfs LXX** (incl. Daniel OG and `09-Daniel-LXX-Theodotion.txt`), NASB95, ESV, NIV84, laid out book-first under `01-Old-Testament/` and `02-New-Testament/`. Cite the Greek from Rahlfs where a finding rests on its wording.
- Tools (run from `/home/claude/danaudit1`): `python3 -I _texts/tools/find.py` (`lemma <n> [Book]`, `verify <n> Ref…`, `co <n> <n>…` verses containing all, `near <k> <n>…`); `python3 -I _texts/tools/contacts.py` (`all <n> <n>… [--window k]` rarity, `phrase "<hebrew words>"` ordered phrase plain and skeletal, `scan <Book>:<a>-<b>` density of rare shared vocabulary against every chapter of the Hebrew Bible). Book labels as the corpus has them (`Dan`, `Isa`, `Gen`). `find.py` writes its summary count to stderr. The phrase tool cannot match a phrase whose first word carries a prefix — confirm by lemma. You may write scripts in `/home/claude/danaudit1/work-<your letter>/`.

## Method (required)
1. **Reproduce every stated count first.** Say whether it holds exactly; correct it if not.
2. **Positive control before any nil or "only" result:** run the same search on a reference known to contain the item and see it returned.
3. **Rival search:** look for closer or equal sources the claim did not name.
4. **Chance baselines for design and field claims:** how often does the claimed pattern arise for comparable arbitrary passages? Report the null in plain numbers. Leave-one-out where a claim rests on a cluster.
5. **Hays criteria** for each allusion claim (Availability, Volume, Recurrence, Thematic coherence, Historical plausibility, History of interpretation — from your own knowledge, tagged `[S]` — Satisfaction), each Strong / Possible / Weak. For design claims, replace the table with: Counts verified · Baseline · Sense · Alternative explanation.
6. **Verdict** for each claim: Confirmed / Confirmed with nuance / Needs reframing / Uncertain — flag for research / Discard, with a **recommended rating** (high / moderate–high / moderate / low–moderate / low).

## Report (write to `/home/claude/danaudit1/auditor-<LETTER>.md`)
- British English. Hebrew, Aramaic and Greek in their own script with an English gloss in brackets after every use. **No code, commands, script names, file paths, word-index numbers or parameter symbols in the report** — state every search in words: the words searched, the edition, the result (e.g. "קִיץ ('awake') with עָפָר ('dust') in one verse: Isa 26:19 and Dan 12:2 only (WLC)").
- For each claim: what you tested; results; corrections; the Hays (or design) table; verdict, recommended rating, reason in two or three sentences; anything missed.
- A section **Decisive results for reproduction**: a numbered list of 8–15 one-sentence factual results (with edition) on which your verdicts turn.
- A section **New candidates** for anything significant the claims did not name.
- Roughly 4,000–7,000 words. Reply to the main session with a 10-line summary of verdicts only.
