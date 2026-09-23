# Toolkit amendments — Round 6: the markup that counted as text

**Date:** 23 September 2026 · **Letters:** Z, AA — continuing from Round 5's W–Y
**Skills touched:** `dig-deeper` (SKILL.md, `references/04-words-and-translations.md`), `book-overview` (SKILL.md), and `_texts/README.md`
**Status:** DRAFTED, not applied. Concrete find/replace pairs below, ready for a `.skill` package.
**Occasion:** the Ezra–Nehemiah whole-book sweep of 19 September 2026.

---

## Summary

Round 5 installed **W**, the ketiv rule, and sized it with a measurement: *16.8 % of the Hebrew Bible's verses carry at least one unpointed form, and in Ezra it is 52.9 %.* Those figures went into four files and are now quoted in three skills.

**They are wrong, by a factor of about three and a half, and the cause is that the measurement counted the corpus's own paragraph markers as words.**

The WLC prints a setumah as a bare **ס** and a petuchah as a bare **פ**, standing alone between verses. Each is a single Hebrew consonant carrying no vowel points — so a test of the form *"a token of Hebrew consonants with no combining marks"*, which is exactly the mechanical signal W teaches, matches every one of them. Ezra's register chapters are dense with them: **135 markers in 280 verses**, one after almost every line of Ezra 2.

The corrected figures are **4.7 % of the canon and 10.4 % of Ezra**.

**Z** corrects the figures in the four places they were planted. **AA** adds to Round 5's amendment **Y** the two cause-classes this run exposed — a tool's **output channel**, and the corpus's **own markup counted as text** — because both produced a wrong answer that looked entirely healthy.

**The rule W teaches is untouched and is if anything better supported.** Ezra remains an outlier: at 10.4 % it is the fifth densest book in the canon and carries more than twice the canonical average. What changes is the size of the claim, and one superlative that was never true.

---

## The evidence

Measured against `_texts/hebrew-wlc/`, all 23,213 verses, by the definition the gate itself states — a token of two or more Hebrew consonants carrying no combining marks, after NFD-decomposition and after splitting on whitespace, maqqef (־) and paseq (׀).

### Both definitions, side by side

| | Unpointed tokens | Verses carrying one | % of verses |
|---|---:|---:|---:|
| **WLC, markers counted as words** | 4,430 | 4,060 | **17.5 %** |
| **WLC, markers excluded** | 1,268 | 1,099 | **4.7 %** |
| *Round 5 published* | *4,197* | *3,911* | *16.8 %* |
| **Ezra, markers counted** | 172 | 149 | **53.2 %** |
| **Ezra, markers excluded** | 37 | 29 | **10.4 %** |
| *Round 5 published* | — | — | *52.9 %* |
| **Nehemiah, markers counted** | 143 | 132 | **32.6 %** |
| **Nehemiah, markers excluded** | 23 | 22 | **5.4 %** |
| *Round 5 published* | — | — | *31.6 %* |

### The identity that settles it

**The difference between the two token counts is 4,430 − 1,268 = 3,162.**

**The number of bare ס and פ markers in the WLC is 3,162** — 1,981 setumot and 1,181 petuchot.

They are the same number. Not approximately: exactly. Every token the inflated count adds is a paragraph marker, and nothing else differs between the two measurements.

### What remains unexplained, and why it does not matter

Round 5's published figures sit a little below the markers-counted column (4,197 against 4,430; 16.8 % against 17.5 %; 52.9 % against 53.2 %) and its token denominator was **266,100** where this run counts **308,678**. That is a tokenisation difference — a different way of splitting the text into words — and it has not been chased, because it cannot change the verdict: the published figures are within 5 % of the markers-counted measurement and are **3.3× the correct one**. The cause is established by the identity above; the residual is detail.

### The superlative that was never true

Round 5 states: *"Ezra is the densest book in the Hebrew Bible for ketiv forms, and more than half its verses carry one."*

**Neither half survives, and the first was wrong even on Round 5's own definition.**

| Rank | Markers counted (Round 5's definition) | Markers excluded (correct) |
|---|---|---|
| 1 | **Lamentations 63.0 %** | **Daniel 22.4 %** |
| 2 | Ezra 53.2 % | Lamentations 13.0 % |
| 3 | Nehemiah 32.6 % | 2 Samuel 10.9 % |
| 4 | 1 Chronicles 29.7 % | Ruth 10.6 % |
| 5 | Jeremiah 29.5 % | **Ezra 10.4 %** |
| 6 | Daniel 28.9 % | 2 Kings 9.0 % |

Under the inflated definition Ezra is **second**, behind Lamentations — whose acrostic structure gives it a petuchah after almost every stanza. Under the correct definition Ezra is **fifth**, and Daniel leads. Lamentations does not appear in Round 5's published ranking at all, which is itself the tell: on its own measure it should have topped it.

**Ezra is still worth naming.** 10.4 % against a canonical 4.7 % is 2.2× the average, and within Ezra the Aramaic is denser again — **17.9 % of its 67 Aramaic verses against 8.0 % of its 213 Hebrew ones**. The block of the book least at home in Hebrew is the block where the reading tradition most often departs from the consonants. That is a better sentence than the one it replaces, and it is true.

---

## Amendment Z — correct the ketiv density figures

**Four locations. Each is a straight replacement; no surrounding text moves.**

### Z1 — `dig-deeper/SKILL.md`, Phase 10.5 gate item (e3)

**Find:**

> **This is not a rare case: 16.8 % of the Hebrew Bible's verses carry at least one unpointed form, and in Ezra it is 52.9 %.**

**Replace with:**

> **This is not a rare case: 4.7 % of the Hebrew Bible's verses carry at least one unpointed form, and in Ezra it is 10.4 % — the fifth densest book in the canon, behind Daniel, Lamentations, 2 Samuel and Ruth, and more than twice the canonical average. Inside Ezra the Aramaic is denser again: 17.9 % of its 67 Aramaic verses against 8.0 % of its 213 Hebrew ones.** *(Corrected in Round 6. The figures W carried — 16.8 % and 52.9 % — counted the WLC's bare* ס *and* פ *paragraph markers as unpointed words; they are single Hebrew consonants with no pointing, so the mechanical signal this very rule teaches matches all 3,162 of them.)*

### Z2 — `dig-deeper/references/04-words-and-translations.md`, Tool 7, *Verify before you report*

**Find:**

> This is not rare — 16.8 % of the Hebrew Bible's verses carry an unpointed form, and in Ezra 52.9 % do.

**Replace with:**

> This is not rare — 4.7 % of the Hebrew Bible's verses carry an unpointed form, and in Ezra 10.4 % do, which makes it the fifth densest book in the canon and more than twice the average. (Corrected in Round 6; the figures first published counted the bare ס and פ paragraph markers as unpointed words.)

### Z3 — `book-overview/SKILL.md`, Phase 10.5 gate item (a)

**Find:**

> One verse in six of the Hebrew Bible carries an unpointed form and in some books more than half do (Ezra, 52.9 %);

**Replace with:**

> About one verse in twenty of the Hebrew Bible carries an unpointed form, and in the densest books about one in five (Daniel 22.4 %, Ezra 10.4 %);

### Z4 — `_texts/README.md`, the ketiv paragraph

**Find:**

> Measured across the WLC: **4,197 unpointed words, 1.58 % of the text, in 3,911 verses — 16.8 % of the canon.** The densest books are **Ezra (4.87 % of words, 52.9 % of verses)**, 1 Chronicles (3.07 %), Nehemiah (2.91 %), Daniel (2.45 %), 2 Samuel (2.31 %) and Jeremiah (2.29 %).

**Replace with:**

> Measured across the WLC: **1,268 unpointed words, 0.41 % of the text, in 1,099 verses — 4.7 % of the canon.** The densest books by share of verses are **Daniel (22.4 %)**, Lamentations (13.0 %), 2 Samuel (10.9 %), Ruth (10.6 %), **Ezra (10.4 %)** and 2 Kings (9.0 %). Within Ezra the Aramaic is denser than the Hebrew around it — 17.9 % of its 67 Aramaic verses against 8.0 % of its 213 Hebrew ones.
>
> **A warning about measuring this, corrected in Round 6.** The figures first published here — 16.8 % of the canon and 52.9 % of Ezra — were **3.3× too high**, because the count treated the corpus's own paragraph markers as words. The WLC prints a setumah as a bare **ס** and a petuchah as a bare **פ**; each is a single Hebrew consonant with no pointing, so the very test this section teaches matches every one of the **3,162** of them in the canon, and Ezra's register chapters carry **135 in 280 verses**. Any scan of this corpus for unpointed forms must require a token of **two or more** consonants, or exclude ס and פ by name. The markers are markup, not text.

---

## Amendment AA — two more cause-classes for the positive control

Round 5's **Y** made a nil return unreportable until a positive control has passed, and enumerated the causes it generalises. **Both faults in this round are new members of that family, and neither is a spelling or a normalisation problem** — which is the point. They are faults in *how the answer was obtained*, not in *how the word was written, and they are the two that look healthiest from the inside.

### AA1 — a tool's output channel

At the end of the Ezra–Nehemiah sweep a scripted re-check of 27 verified headline counts **returned zero for all 27**. Every one of them had already been confirmed individually. The cause was that `find.py` writes its summary line to **stderr**, and the script captured only stdout.

**The tell that nearly did not fire:** the single "pass" in that run was the one check whose *expected* value was zero — דרש in Nehemiah. A broken harness and a real absence are indistinguishable from the inside, and a table of failures with one pass reads as 26 bad findings rather than one bad script. Re-run with a control first — חזק in Nehemiah, expected non-zero, returned 34 — the harness was shown sound and all 27 checks passed.

### AA2 — the corpus's own markup counted as text

Amendment Z above. A measurement of the text that silently included the text's *markup*, producing a figure that was plausible, quotable, and repeated into four files and three skills.

**Why this one is the harder of the two:** AA1 produced an answer that was obviously wrong (everything zero). AA2 produced an answer that was **wrong in a believable direction** — it made a real phenomenon look more common than it is, which is exactly what a rule's author wants to find. Nothing in the number itself invited a second look.

### The edits

**AA-a — `dig-deeper/SKILL.md`, Phase 10.5 gate item (e3), inside Y**

**Find:**

> One command, and it catches every member of a family this gate has so far been patching one cause at a time — maqqef and paseq, plene and defective spelling, the ketiv, a hand-written lemma matcher that does not allow for the index's homograph suffixes (`2617 a`, `6965 b`), a wrong book filter, a versification offset.

**Replace with:**

> One command, and it catches every member of a family this gate has so far been patching one cause at a time — maqqef and paseq, plene and defective spelling, the ketiv, a hand-written lemma matcher that does not allow for the index's homograph suffixes (`2617 a`, `6965 b`), a wrong book filter, a versification offset, **a tool whose answer goes to a channel the script is not reading** (a scripted re-check of 27 verified counts returned zero for all 27 because `find.py` writes its summary to stderr — and its only "pass" was the one check whose expected value was zero), **and a scan that counts the corpus's own markup as text** (the WLC's bare ס and פ paragraph markers are single unpointed Hebrew consonants, and counting them inflated this gate's own ketiv figures by 3.3× — see Round 6). **The last two are the dangerous ones, because neither is a spelling fault and neither makes the answer look wrong.**

**AA-b — `book-overview/SKILL.md`, Phase 10.5 gate item (a), after the positive-control sentence**

**Find:**

> if the control fails the search is broken, not the text. *(Positive control adopted on trial, Round 5.)*

**Replace with:**

> if the control fails the search is broken, not the text. **The two faults likeliest to survive every other check are a tool whose answer goes to a channel the script is not reading, and a scan that counts the corpus's own markup — the bare ס and פ paragraph markers — as text.** *(Positive control adopted on trial, Round 5; two cause-classes added Round 6.)*

**AA-c — `_texts/README.md`**

No separate edit: Z4's second paragraph carries AA2 for this file, and AA1 is a property of `find.py`, better stated where the tool is described. **Optional, if the round is being packaged anyway:** add to the `find.py` description that *its summary line goes to stderr, so a script that captures only stdout sees an empty result.*

---

## A status note: the trial on Y

Round 5 adopted **Y** on trial, in the position G held in Round 2, with the withdrawal test: *withdraw if three runs pass with no control ever having failed.*

**The Ezra–Nehemiah sweep is run one of that trial, and the control fired.** It caught AA1, and it caught it in the only configuration that would have been misread — 26 failures and one pass, where the pass was the expected-zero case. Without it the sweep's verified findings would have been "corrected" against a broken instrument.

**Recommendation: retire the "adopted on trial" marker on Y now rather than waiting for two more runs.** The trial existed because Y generalised four observed causes without resting on a run of its own. It now rests on a run of its own, and that run added two further cause-classes — which is stronger evidence than three quiet passes would have been. Three runs with no failure would have argued for withdrawal; one run with a failure argues for permanence.

Drafted as a recommendation, not an edit; the marker's removal should go in the same package as Z and AA if accepted.

---

## What this round says about the method

Three of the last four rounds have been caused by a measurement or a search that returned a clean, plausible, wrong answer. Round 5's two near-misses, and both of this round's. **The gate is now long, and every clause in it was bought by a specific failure** — which is the right way to build one, but it is worth noticing what the failures have in common.

None of them was an error of judgement about a text. Every one was an error in an instrument, and in each case the instrument reported success. The ketiv did not announce itself; the maqqef did not announce itself; the homograph suffix did not announce itself; stderr did not announce itself; and 3,162 paragraph markers presented themselves as Hebrew words.

**The generalisation Y reaches for is the right one**, and this round's two additions are why it should be permanent rather than provisional: *the corpus is more willing to give a confident wrong answer than a visible error.* A positive control is the only cheap defence, because it is the only check that tests the instrument rather than the claim.

One further observation, offered without an edit attached. **Round 5's figures were wrong in the direction that flattered the rule they were introduced to support.** That is not carelessness; it is the ordinary shape of a number nobody has a reason to doubt. Where a round's own evidence makes its own rule look more necessary, the measurement deserves the positive-control treatment before it is published — which in this case would have meant asking what the 3,162 extra tokens actually were.

---

## Verification done on this spec

- **Both measurements re-run** against `_texts/hebrew-wlc/`, all 39 files, 23,213 verses — the WLC total independently reproduced.
- **The identity checked:** unpointed tokens with markers (4,430) minus without (1,268) = 3,162 = the exact count of bare ס and פ in the canon (1,981 + 1,181). Asserted programmatically, returned `True`.
- **Both rankings computed** over all 39 books, by share of verses, under each definition.
- **Ezra's Aramaic/Hebrew split** computed on the morphologically-fixed extent (Ezra 4:8–6:18; 7:12–26), whose 67-verse total this run reproduced independently of the overview's morph-code result.
- **All four *find* strings confirmed present and unique** in the installed files as this session reads them — `dig-deeper/SKILL.md`, `dig-deeper/references/04-words-and-translations.md`, `book-overview/skills/book-overview/SKILL.md`, and `_texts/README.md`.
- **Caveat on the installed-file check, per Round 5's own lesson:** the copy of an installed skill a session can read is a snapshot taken when the session starts. This session began after Round 5 was installed, and the snapshot contains W, X and Y, so it is post-Round-5 — but **the find strings should be re-confirmed against the live files at package time**, in a new task, before anything is replaced.
- **Hebrew in this spec:** ס, פ, ס/פ, דרש, חזק, וְרַב־וחסד — six strings, every codepoint a legitimate Hebrew character.

---

## Consequential edit outside the skills

**`Ezra-Nehemiah/dig-deeper-ezra-nehemiah-sweep.md` states that the skill's ketiv figures "do not reproduce" without naming the cause**, because the cause was not known when it was written. That passage is true but incomplete, and slightly unfair to Round 5 — the figures reproduce *exactly*, under a definition nobody intended. The sweep is being corrected in the same pass as this draft, in its Textual notes section and in Open Question 11.
