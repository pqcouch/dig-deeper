# Toolkit amendments — Round 8: reports are written for a reader

**Date:** 8 October 2026 · **Letter:** AE (continuing from Round 7's AB–AD)
**Skills touched:** `dig-deeper` (`SKILL.md` gate item (j); `references/claim-audit-format.md`) and `book-overview` (`SKILL.md` Phase 10.5)
**Corpus touched:** `_texts/tools/find.py` (two new commands) and `_texts/README.md`
**Status:** INSTALLED and verified 9 October 2026, with Rounds 6–8 together. dig-deeper is byte-identical to the intended build (`_skill-backup/dig-deeper-rounds-6-8.skill`). book-overview v0.3.0 has its body text and reference files byte-identical; the installer reformatted only the YAML description line. The corpus edits (`_texts/README.md`, `contacts.py`, `find.py`) are applied.
**Occasion:** Patrick's reading of Job claim audit 3, which found lines such as "`co(['1350','2555','1818'])` returns Ps 72:14" in the body of the report.

---

## Summary

The claim audits since Job claim audit 2 had begun to report their searches in the auditors' working shorthand. A line such as `co(['1350','2555','1818'])` means "the verses of the WLC in which גָּאַל ('redeem'), חָמָס ('violence') and דָּם ('blood') all occur". The numbers are the word-index numbers of the WLC lemma file, and `co`, `lem`, `ph`, `win` and `base.rank` were short search routines written in the session workspace.

**The findings were sound.** A sample of the searches was re-run with the folder's own `find.py`, and every result came back as reported: the witness / rise / testify triad at Deut 19:16 and Job 16:8; redeem / violence / blood at Ps 72:14; cobra with poison at Deut 32:33 and Job 20:16; violence with "argue" at 1 Chr 12:18; bow with bronze at 2 Sam 22:35, Ps 18:35 and Job 20:24; and the חֶסֶד positive control in Job at 6:14; 10:12; 37:13.

**The fault was in the writing, and it was threefold.**

1. **Unreadable.** Many lines named a word only by its index number, with no Hebrew and no gloss. That breaks the house rule of the original word in its own script with a gloss at every occurrence. A reader could not tell what had been searched for.
2. **Unrepeatable.** The routines lived only in the temporary session workspace and were never saved to the folder. Those behind the Matthew and Lamentations audits had already gone, so their "spot-check lines" could not be re-run by anyone.
3. **Unchecked.** No gate item looked for it. The habit entered at Job claim audit 2 (three lines) and grew with each audit: about 54 lines in audit 3, about 56 in audit 4.

This round corrects the reports, gives the searches a permanent home in `find.py`, and adds one gate item so that it does not recur.

---

## The evidence

### What was found, report by report

All 18 claim audits in the folder were scanned for search commands, routine names, script names, word-index numbers and the window-ranking parameters (`k`, `maxf`, `IDF`).

| Report | What it had | Lines rewritten | Now |
|---|---|---|---|
| Job claim audit 3 | spot-check lists in code; the positive control in code; window settings as `k` / `maxf` | about 130 | v1.1 |
| Job claim audit 4 | the same, plus script names (`c1c.py` … `c7b.py`) | about 145 | v1.1 |
| Matthew claim audit 2 | 41 "spot-check lines" written as commands, with Swete abbreviations (`Dat`, `Sut`, `Tbs`) | 46 | v1.1 |
| Job claim audit 2 | positive control and method in code; `maxfreq` | 30 | v1.1 |
| Lamentations claim audit 2 | two commands; routine names in the method | 6 | v1.1 |
| Lamentations claim audit 3 | routine names; two index numbers | 4 | v1.1 |
| Mark claim audit | four `verify` commands; a session script path | 7 | v1.1 |
| Matthew claim audit 1 | index numbers (`H7225`, `lemma 4771`) | 7 | v1.1 |
| Genesis claim audit | index numbers beside each word | 18 | v1.1 |
| Job claim audit 1 | two index numbers | 2 | v1.1 |
| John claim audit | two search patterns | 2 | v1.2 |
| Lamentations claim audit 1 | a routine described by name | 1 | v1.1 |
| Ecclesiastes, Ezra–Nehemiah, Proverbs, Habakkuk, Jonah, Exodus | none | 0 | unchanged |

Six other reports carried a session script name or a single command in a provenance line: the Job digs on 15:1–21:34, 19:1–29, 22:1–28:28 and 28:1–28; the Proverbs 30:1–31:9 dig (`len(V)==23213`); the Matthew sweep (one `show(...)`); and the Genesis 1:1–2:3 and 2:4–25 digs (morphology codes `Ncfsa`, `Vqi1cs`). Three more reports said their counts were "reproducible from" a session-workspace path that no longer exists: the Lamentations 3:1–33 and 5:1–22 digs and the Job 4:1–14:22 dig. Those lines were rewritten to say plainly that the work was done in the session and is not retained. All these lines were rewritten in words. No version change was made, because nothing but the provenance wording moved.

Every corrected audit carries a **Revised** line under its date, saying what changed and that no verdict, count, rank or rating moved. Originals are kept in `_backup/round8-prose-2026-10-08/`.

### One misreading caught in the rewriting

In Job claim audit 3, the setting written `k=12` was first decoded as "the 12 rarest words". The ranking routine shows that `k` is the **window length in verses**: the ranker finds, in each non-Job chapter, the run of *k* verses that shares the most of the target's rarer words. Every instance was corrected to "12-verse windows" before the file was saved. The episode is itself the argument for this round. If the author of the shorthand can misread it a week later, a reader cannot be expected to read it at all.

### Pre-existing glyph faults fixed while re-rendering

Re-rendering the corrected files exposed some characters with no glyph in the house font, all from older runs:

- the check mark (John claim audit, Lamentations claim audit 2, the two Genesis digs);
- the star symbol (Lamentations claim audit 2, the Proverbs 30 dig);
- Fraktur (black-letter) sigla for G, Q, m, C and P (Matthew claim audit 1, the Proverbs 30 dig, the Mark claim audit).

These were replaced with words, or with roman G, Q, m, C and P, as the house convention already requires. Two fallbacks remain: the NA28 raised critical signs in the Matthew audits, and some apparatus signs in the Matthew sweep. They have no roman equivalent, so they were left as they are. The two Lamentations digs also carry older glyph fallbacks, not yet traced; they were left for the follow-up pass.

---

## Amendment AE — every search stated in words

### AE1 · `dig-deeper/SKILL.md`, Phase 10.5: new gate item (j)

**Find:**

> If any item fails, return to the relevant phase and fix it — do not ship with a noted failure.

**Replace with:**

> **(j) every search the report relies on is stated in words, not in code:** the original-language words in their own script with a gloss, the edition searched, and the result — "עֵד ('witness') + קוּם ('rise') + עָנָה ('testify') in one verse: Deut 19:16 and Job 16:8 only (WLC)". **No search command, routine name, script name, file path in the session workspace, word-index number (Strong's or the WLC lemma field), or parameter symbol (`k`, `maxf`) appears in the report's text**, the spot-check lists of a claim audit included. A homograph is named in words ("חבל I, 'take in pledge', which the WLC index files apart from חבל II"), not by its index letter. A window rank states its window length in verses and its frequency ceiling in words ("10-verse windows, words in at most 150 verses"). Searches that need to be re-runnable are run with `_texts/tools/find.py`, which lives in the folder, never with a routine that exists only in the session. The mechanical check: search the finished Markdown for `(['`, `('`, `.py`, `maxf`, `k=` and four-digit numbers in brackets; every hit is a defect. If any item fails, return to the relevant phase and fix it — do not ship with a noted failure.

### AE2 · `dig-deeper/references/claim-audit-format.md`: the spot-check list

**Find:**

> [Repeat for each claim]

**Replace with:**

> [Repeat for each claim]
>
> **Spot checks and positive controls are written as prose** (gate item (j)): "Positive control: חֶסֶד ('covenant-kindness') in Job returns 6:14; 10:12; 37:13 (WLC)", never as the command that produced the result. A spot-check list is a list of sentences a reader can check against the text, not a script log.

### AE3 · `book-overview/SKILL.md`, Phase 10.5: the same rule

Apply after Round 7, whose AB and AD add items (f) and (g) to this gate. If Round 7 has not been installed, letter this item (f).

**Find:**

> Record the results in the colophon. **This is where the overview's highest-risk claims are made:**

**Replace with:**

> **(h) Every search is stated in words** — the original-language words in their own script with a gloss, the edition and the result — with no search command, routine or script name, word-index number or parameter symbol anywhere in the overview (the rule of `dig-deeper` gate item (j)). Record the results in the colophon. **This is where the overview's highest-risk claims are made:**

---

## The tool: `find.py co` and `find.py near` (applied)

Two commands were added to `_texts/tools/find.py` so that the searches the audits depend on live in the folder:

- `find.py co 5707 6965 6030` lists the verses in which all the given lemmas occur, and `--book Job` limits it to one book;
- `find.py near 4 2555 3709 3198` lists the places where all the lemmas fall within four verses of one another in the same chapter.

A homograph entry can be searched on its own by quoting it with its letter (`"1350 b"`); the bare number searches every entry under it, as `lemma` always has. The original `find.py` is kept in the backup folder.

**Validation against known results.**

| Command | Expected (from the audits) | Returned |
|---|---|---|
| `co 5707 6965 6030` | Deut 19:16; Job 16:8 | Deut 19:16; Job 16:8 |
| `co 1350 2555 1818` | Ps 72:14 | Ps 72:14 |
| `co 7198 5154` | 2 Sam 22:35; Ps 18:35; Job 20:24 | the same three |
| `co 2555 3709 --book Job` | Job 16:17 | Job 16:17 |
| `near 4 2555 3709 3198` | 1 Chr 12:18; Job 16:17–21 | the same two |
| `near 1 1350 314` | Isa 44:6; Job 19:25; Ruth 3:9–10 | the same three |
| `near 3 4671 6098` | Ps 1; Job 21:16–18 | Ps 1:1–4; Job 21:16–18 |
| `co "1350 b"` | Isa 63:4 only | Isa 63:4 |
| `lemma 2617 Job` (control) | 6:14; 10:12; 37:13 | the same |

`_texts/README.md` now lists the two commands and adds the rule: commands are for running, not for reports.

The window ranker (the chapter-by-chapter rank with its Job-passage null) has **not** been moved into `find.py`. It is a heavier tool with settings that matter, and Round 7's `contacts.py` (drafted, not installed) overlaps it. It should be built once, properly, when Rounds 6–8 are packaged, not copied in a hurry.

---

## What this round does not change

- **No verdict, count, rank or rating** in any audit. The rewrite was checked by re-running a sample of searches and by decoding every index number against the WLC lemma file before it was replaced with the Hebrew word.
- **Index numbers beside the Hebrew in digs and sweeps.** Many digs cite the lemma number in brackets *after* the Hebrew word, as provenance: "חבל I ('take in pledge') … (lemma 2254 a)". This is readable, because the word and gloss are there, but it falls under AE1. These will be cleaned when each report is next revised, not in one sweep now. The heaviest are the Job digs on 19:1–29 and 22:1–28:28 and the Genesis digs.
- **Runnable `find.py` commands left in a few older sweeps and digs.** These are the same fault in milder form: the command is for Patrick's own tool, so it can be re-run, but it is still code in a report. They were found in:
  - the Psalm 51 dig (25 lines);
  - the Matthew sweep (15);
  - the two Ezra–Nehemiah sweeps (12);
  - the Mark sweep, the Mark 1:1–13 dig and the Mark overview (5);
  - the Luke sweep and overview (2);
  - the Ecclesiastes overview, the Decalogue dig and the Matthew overview (4).
  
  They are listed here for a follow-up pass.

---

## Verification done on this round

- **Scan before and after.** All 18 claim audits were scanned for calls, list output, script names, parameter symbols and index numbers. After correction every one returns zero hits, apart from naming `find.py` as the tool used.
- **Decoding.** Every word-index number replaced in the audits was decoded against the WLC lemma file (the most frequent surface forms for each entry) before the Hebrew word was written in.
- **Re-running.** The searches quoted in Patrick's message were re-run with `find.py`, and every result matched.
- **Rendering.** All 23 corrected files were re-rendered:
  - each `.odt` is A5 in Liberation Serif;
  - every `.html` nav anchor resolves, and `lang="en-GB"` is present;
  - the fonts are clean, apart from the NA28 critical signs noted above.
- **Device copies.** The md5 of each committed Markdown file was checked on the device against the cloud copy.
