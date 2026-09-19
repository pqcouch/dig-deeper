# Toolkit Amendments — Round 5

**Three amendments, lettered W–Y**, arising from the Ezra–Nehemiah clean-room book-overview rebuild of 19 September 2026.
**Status: drafted, not applied.**
**Target files:** `dig-deeper/SKILL.md`, `dig-deeper/references/04-words-and-translations.md`, `book-overview/SKILL.md`, and `_texts/README.md` in the prep folder.

---

## A correction to the record, first

Two status notes in circulation are wrong, and both were caught by checking the installed files rather than the previous document — which is Round 1's own lesson doing its work.

1. **Round 3 (K–N) *is* installed.** The note that it was "drafted, NOT yet applied" is stale. The installed `dig-deeper/SKILL.md` (711 lines) carries the real-file-plus-pointer filing rule, the two-pass skeletal diff, the set-the-extent-at-each-book's-own-seams rule and the run-Move-4-once-per-book rule, and the "adopted on trial" marker on Synoptic Mode has been retired. Nothing in Round 3 is outstanding.
2. **The installed `references/CHANGELOG.md` still stops at Round 2.** That is expected and was recorded at the close of Round 4: a proposal card replaces `SKILL.md` and nothing else, so the full record lives in `_skill-examples/CHANGELOG.md` in the prep folder. **This round's changelog entry belongs in the prep-folder copy**, and the lettering continues from V.

---

## Why this round exists

The Ezra–Nehemiah run produced two near-misses, and they are the same failure with two different causes.

**The first.** A whole-Bible search for the Exodus 34:6 formula וְרַב־חֶסֶד ("and abounding in covenant-love") returned seven verses — Exod 34:6; Num 14:18; Joel 2:13; Jonah 4:2; Pss 86:5, 86:15, 103:8 — and **did not return Nehemiah 9:17**, which is the book's clearest citation of that formula and was about to become a row in the intertextual map. The search was not at fault in any way the existing gate could see: accents were NFD-stripped, maqqef and paseq were normalised to spaces per amendment J, and a skeletal pass had been run. It missed because Codex L reads וְרַב־**וחסד** — a *ketiv* with an intruding waw, standing **unpointed** in the WLC reading text as ketiv forms do, and therefore unmatchable by any pattern spelling the qere. The lemma index had it right all along: its entry for that word is `c/2617 a`. The chain was caught, but only because the finding was cross-checked by lemma for another reason.

**The second.** The run's first pass at the lemma index was written as a bespoke script that split the lemma field on `/` and compared for equality. It returned **zero occurrences of חֶסֶד and zero of קוּם in Ezra–Nehemiah** — a book that contains both, eight times and many times respectively. The cause is that the WLC lemma field carries homograph suffixes and markers: `2617 a`, `6965 b`, `1121 a`, `1035+`. An equality test on `2617` matches none of them. **`_texts/tools/find.py` has always handled this correctly** — its pattern is `(^|/)<n>( |$|/)` — so the corpus was sound and the hand-rolled script was not.

Both produced a **nil return that is indistinguishable from a real absence**. The skill already names that phrase, twice. What it has not yet done is treat the family as a family.

### The evidence, measured

This is not an inference from one awkward verse. The ketiv exposure was measured across the whole corpus.

| | Hebrew/Aramaic words | Unpointed (ketiv) | % of words | % of verses carrying one |
|---|---:|---:|---:|---:|
| **WLC, whole OT** | 266,100 | 4,197 | **1.58 %** | **16.8 %** (3,911 of 23,213) |
| **Ezra** | 3,452 | 168 | **4.87 %** | **52.9 %** |
| **Nehemiah** | 4,738 | 138 | 2.91 % | 31.6 % |
| **Ezra–Nehemiah** | 8,190 | 306 | 3.74 % | **40.3 %** (276 of 685) |

`[T — counted from the WLC reading text: a word containing Hebrew consonants and no combining marks at all]`

**Ezra is the densest book in the Hebrew Bible for ketiv forms**, ahead of 1 Chronicles (3.07 %), Nehemiah, Daniel (2.45 %), 2 Samuel and Jeremiah. **More than half of Ezra's verses contain at least one word a qere-spelled pattern cannot match**, against an OT average of one verse in six. A surface or phrase search run anywhere in this book is more likely than not to be looking at a verse it cannot fully see — and the same is true, at lower odds, of every sixth verse in the canon.

---

## Amendment W — the ketiv rule

**Files:** `dig-deeper/SKILL.md` (gate item e3), `book-overview/SKILL.md` (Phase 10.5 item a), `dig-deeper/references/04-words-and-translations.md` (Tool 7, "Verify before you report"), `_texts/README.md`.

### W1 — `dig-deeper/SKILL.md`, Phase 10.5 gate item (e3)

Item (e3) currently carries the phrase-search rule in two clauses: the maqqef/paseq normalisation (amendment J) and the skeletal plene/defective pass. **Insert a third clause after the skeletal-pass clause**, before "a reference that fails is removed from the chain":

> **and where any word in the search window stands *unpointed*, the search has met a ketiv and cannot match it:** the WLC prints the ketiv consonants without vowels and the qere only in the Masorah, so a pattern spelling the qere silently skips the verse — **a word carrying Hebrew consonants and no combining marks at all is the mechanical signal**, and the chain must then be confirmed against the lemma index, which carries the correct lemma for the ketiv form regardless of its spelling. **This is not a rare case: 16.8 % of the Hebrew Bible's verses carry at least one unpointed form, and in Ezra it is 52.9 %.** The Neh 9:17 ketiv וְרַב־**וחסד** hid that verse's citation of Exod 34:6 from a phrase search that was otherwise correctly normalised;

### W2 — `book-overview/SKILL.md`, Phase 10.5 item (a)

The book-overview gate carries the shorter form of the same rule. **Current text:**

> Where a phrase search is unavoidable, normalise maqqef, paseq and sof pasuq to spaces as well as NFD-stripping combining marks, and run a second *skeletal* pass with waw, yod and word-final *he* deleted, since a defective spelling drops a verse silently and an undercount is indistinguishable from a count.

**Replace with:**

> Where a phrase search is unavoidable, normalise maqqef, paseq and sof pasuq to spaces as well as NFD-stripping combining marks; run a second *skeletal* pass with waw, yod and word-final *he* deleted, since a defective spelling drops a verse silently and an undercount is indistinguishable from a count; and **treat any unpointed word in the window as a ketiv the pattern cannot match — confirm the chain by lemma before trusting the result.** One verse in six of the Hebrew Bible carries an unpointed form, and in some books more than half do.

### W3 — `dig-deeper/references/04-words-and-translations.md`, Tool 7, "Verify before you report"

The bullet ends: *"Two searches in the Decalogue run returned nil on texts that contained the phrase for exactly this reason, and **a nil return is indistinguishable from a real absence.**"*

**Append:**

> **The third cause is the ketiv.** Where the Masoretes read a word other than the one the consonants spell, the WLC prints the ketiv **unpointed** and leaves the qere to the Masorah — so a pattern spelling the qere, however carefully normalised, does not see the verse. The signal is mechanical: **a word with Hebrew consonants and no combining marks at all**. The lemma index is unaffected and carries the right lemma either way, so **any nil or short return from a phrase search is confirmed by lemma before it is reported as an absence**. Neh 9:17's וְרַב־**וחסד** cost a correctly-normalised whole-Bible search the book's clearest citation of Exod 34:6.

### W4 — `_texts/README.md`

Under **File formats**, after the sentence *"Search the lemma column, not the pointed surface form — pointing, prefixes and suffixes make surface search unreliable, which is exactly how a chain gets claimed at a verse that does not contain the word"*, add:

> **The ketiv is the sharpest form of this.** The reading text prints a ketiv with its consonants and **no pointing**; the qere is not in the file. So an unpointed word is the corpus telling you that what the Masoretes read is not what you are looking at. Measured across the WLC: **4,197 unpointed words, 1.58 % of the text, in 3,911 verses — 16.8 % of the canon.** The densest books are Ezra (4.87 % of words, 52.9 % of verses), 1 Chronicles (3.07 %), Nehemiah (2.91 %), Daniel (2.45 %), 2 Samuel (2.31 %) and Jeremiah (2.29 %). The `_index/` lemma files are unaffected — they carry the correct lemma for the ketiv form — so **lemma searches survive the ketiv and surface searches do not**.

---

## Amendment X — use the supplied tool, and prove any replacement

**Files:** `dig-deeper/references/04-words-and-translations.md`, `book-overview/SKILL.md` Phase 10.5(a), `_texts/README.md`.

### X1 — `_texts/README.md`, under **Using it**

After the command block, add:

> **The lemma field is not a plain number.** It carries homograph letters and markers — `2617 a`, `6965 b`, `1121 a`, `1035+` — and morphemes separated by `/` (`c/1961`). `find.py` accounts for all of this; its matcher is `(^|/)<number>( |$|/)`. **An equality test on the split field returns a silent zero for many of the commonest words in the Bible**, and a silent zero from a lemma search is the one result this corpus exists to make impossible. So: **run chain checks with `find.py`.** If a run needs something `find.py` does not do, the bespoke script is checked against `find.py` on one lemma known to be present *before* any of its output is believed.

### X2 — `04-words-and-translations.md`, Tool 7, new bullet after "Verify before you report"

> - **Verify with the corpus's own tool.** `python3 tools/find.py lemma <strongs> [Book]` lists every occurrence; `python3 tools/find.py verify <strongs> <Ref> <Ref> …` tests a claimed chain and **exits non-zero if any reference fails**, so it can gate a script. Use them. A hand-written lemma matcher is a known failure mode, not a hypothetical one: in the Ezra–Nehemiah run of 19 September one returned **zero** occurrences of חֶסֶד ("covenant-love") and **zero** of קוּם ("to arise") in a book that contains both, because the WLC lemma field carries homograph suffixes (`2617 a`, `6965 b`) that an equality test does not match. `find.py` had the right answer in one line.

### X3 — `book-overview/SKILL.md`, Phase 10.5 item (a)

Append to the item, after the W2 sentence:

> Chains are checked with `_texts/tools/find.py` (`lemma` to list, `verify` to gate); a bespoke matcher is validated against it on a known-positive lemma before its output is used, since the lemma field's homograph suffixes make a naive equality test return a silent zero.

---

## Amendment Y — the silent-zero principle, and a positive control

**File:** `dig-deeper/SKILL.md`, Phase 10.5 gate item (e3); `book-overview/SKILL.md`, Phase 10.5 item (a).

W and X are the third and fourth members of a family the toolkit has been extending one patch at a time:

| Cause | Added | Effect |
|---|---|---|
| Maqqef and paseq survive accent-stripping | Round 2 (J) | Phrase pattern returns nil on a text containing the phrase |
| Plene / defective spelling | Round 2 (e3, skeletal pass) | Verse silently dropped; an undercount looks like a count |
| **Ketiv stands unpointed** | **Round 5 (W)** | Verse invisible to any qere-spelled pattern |
| **Hand-rolled lemma matcher** | **Round 5 (X)** | Zero occurrences of a word the book uses repeatedly |

Four causes, one effect. A fifth will arrive, and the gate should not have to wait for it. **Add to gate item (e3) in `dig-deeper/SKILL.md`, and to Phase 10.5(a) in `book-overview/SKILL.md`, as the item's closing sentence:**

> **A nil or surprisingly short return is never reported as an absence until a positive control has passed.** Run the identical search against one reference the item is *known* to contain — a lexicon entry, a concordance line, a verse already read — and see it returned. If the control fails, the search is broken and the text is innocent; if the control passes, the absence is evidence. This costs one command and catches every member of the family at once, including the causes not yet met: maqqef and paseq, plene and defective spelling, the ketiv, a mis-written matcher, a wrong book filter, a versification offset. **An unverified absence is a claim like any other, and it is the one kind this corpus makes easiest to get wrong.**

**Honest note on Y's warrant.** W and X are data-driven: each rests on a measured failure in a live run, and W's scope is quantified canon-wide. Y is a **generalisation from four data points**, in the same position amendment G occupied in Round 2 — a design inferred from a pattern rather than demonstrated by a run. It should go in on the same terms G did, **marked in the file as adopted on trial**, and be withdrawn if the positive control proves to be friction without yield after three runs. The test is simple: does any run in the next three report a control that failed? If none does, the control is ceremony and should go.

---

## What can and cannot be delivered by a proposal card

Learned in Rounds 3 and 4 and still true:

- **`SKILL.md` only.** A proposal card replaces the whole of one skill's `SKILL.md` and touches nothing else. **W1, W2, X3 and Y can be delivered that way** — two cards, one per skill.
- **The reference tree cannot.** **W3, X2** live in `dig-deeper/references/04-words-and-translations.md` and need either a `.skill` package (`skill-creator`'s `scripts/package_skill.py`) or a mirrored copy in `_skill-examples/`. Round 4's package built cleanly but its install card never became visible, so the prep-folder mirror is the reliable route until that is fixed.
- **`_texts/README.md` (W4, X1) is not part of any skill** — it is a file in the prep folder and can simply be edited.
- **Two standing checks apply after any card is saved.** Diff the installed `SKILL.md` against the intended text (Round 3 lost a paragraph silently). And check every Hebrew word the card touched against the WLC (Round 4's card damaged three in transmission, one of them inside the sentence teaching the paronomasia exception). Note that a card's transmission applies **NFC** while the corpus is not NFC, so compare after NFD-stripping, never byte for byte.

---

## Proposed order of work

1. Edit `_texts/README.md` directly — **W4, X1**. No card, no package, immediate.
2. Card 1: `book-overview/SKILL.md` — **W2, X3, Y**. Diff and Hebrew-check after saving.
3. Card 2: `dig-deeper/SKILL.md` — **W1, Y**. Diff and Hebrew-check after saving.
4. Mirror **W3, X2** into `_skill-examples/` and add the pointer, or build the `.skill` package if the install card is working again.
5. Add the Round 5 entry to `_skill-examples/CHANGELOG.md` — **not** the installed `references/CHANGELOG.md`, which is superseded.

---

## Colophon

**Round** 5 · **Amendments** W, X, Y · **Date** 19 September 2026 · **Status** drafted, not applied

**Source run.** The Ezra–Nehemiah clean-room book-overview rebuild and its import claim audit, both of 19 September 2026, filed in `Ezra-Nehemiah/`.

**Evidence base.** W: one live near-miss (Neh 9:17) plus a canon-wide measurement of ketiv density over all 266,100 Hebrew and Aramaic words of the WLC. X: one live failure in the same run, plus inspection of `_texts/tools/find.py`, which was found to be correct — the fault was in a replacement for it, not in the corpus. Y: inferred from the four-member pattern tabulated above; **marked for trial, not settled**.

**Installed files checked before drafting, not assumed.** `dig-deeper/SKILL.md` (711 lines; Rounds 1–4 present, Round 3's K–N confirmed installed and the Synoptic Mode trial marker retired); `dig-deeper/references/04-words-and-translations.md` (Tool 7's "Verify before you report" carries amendment J); `dig-deeper/references/CHANGELOG.md` (stops at Round 2, as Round 4 recorded); `book-overview/SKILL.md` (v0.2.0 shape, Phase 10.5 present); `_texts/tools/find.py`; `_texts/README.md`.

**Health note.** Two amendments that close measured holes and one that tries to stop the next one being a fifth patch. Nothing here changes what the toolkit looks for — only what it is willing to believe when it finds nothing.
