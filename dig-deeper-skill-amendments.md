# Dig Deeper — Proposed Skill Amendments

**Status:** Draft v1.0 — **proposed, not applied.** Nothing in the installed skill has been changed.
**Date:** 2 September 2026
**Prepared for:** the process review of 2 September 2026
**Scope:** five amendments to `dig-deeper`, each with the exact file, anchor and text to change.

---

## How to read this document

Each amendment gives the **problem**, the **evidence from completed runs** that it is a real problem and not a tidiness preference, the **file and anchor** to edit, the **exact text**, and the **cost** of adopting it.

The evidence matters more than the proposals. Four of the five amendments are not new ideas: they are disciplines that completed runs already arrived at independently, wrote down in their own method notes, and then had no way to carry forward. The skill has no mechanism for learning from its own audits, so each run has had to rediscover the same lessons. These edits are that mechanism.

Nothing here should be adopted because it is written down. Each amendment is a claim to be tested against the next few runs, exactly as a book overview is.

---

## Summary

| | Amendment | Solves | Cost |
|---|---|---|---|
| **A** | Wire the local text corpus into the workflow | The substrate has to be pasted in; counts are unreproducible | One new Phase 0.2; two edited phase rows |
| **B** | Tanak order for the Old Testament | Canonical position is invisible; chronological and canonical order are silently conflated | One new subsection in Tool 14; one line in Tool 2 |
| **C** | The chain-verification gate | Lexical chains extended by inference into verses that do not contain the word | One new item in the Phase 10.5 gate; one line in the Declaration |
| **D** | NASB95 as reference version, ESV as pulpit text | A real divergence check was switched off on the assumption the two texts were one | Replace two paragraphs in Default Translation |
| **E** | Audit trigger for synthetic claims | Book-level claims fail at a much higher rate than passage-level ones, and nothing notices | One new subsection; one line in the sweep-mode workflow |

---

## The evidence, in the runs' own words

Five findings, each recorded in a completed report, none of them currently in the skill.

**1. A named failure mode, three instances.** From `dig-deeper-jonah-claim-audit.md`:

> "Both corrections are of the same type: **a verbal chain extended by inference into a verse that does not contain the word.** The Exodus audit found the identical failure in the descent-spine (*šākan* claimed at 40:34, where it does not occur). **That is now a named failure mode of this project's book-level work** — and the cheapest guard against it is to re-verify every claimed chain against the text before it reaches an overview."

The Exodus audit found a third: the Hur identification at 17:10 // 31:2, "third instance in this project of a chain extended by inference into a text that does not contain the link".

**2. Where the errors live.** From `book-overview-exodus.md`:

> "Every claim that needed correction was **synthetic** — assembled across passages — while every claim resting on a single verified passage held. **The sweep's passage-level work proved more reliable than its book-level work**, which is an argument for auditing again whenever new book-level claims are added."

**3. Primary texts, not search.** From `dig-deeper-exodus-claim-audit.md`:

> "Three research passes could not supply six Greek texts and a HALOT entry; one session with the books supplied all of them… **research tools are for the state of a scholarly question; primary texts are for the data. Do not ask a search engine what a verse says.**"

**4. The English text is not the evidence.** From `proverbs-questions-still-open.md`:

> "**Paste the Hebrew.** Every load-bearing finding in the 2A run came off the Hebrew, and several of them — the *kābēd* Leitwort, the marked/unmarked comparison split, the *petuchot* — are invisible in English. **The ESV alone would have reproduced the sweep.**"

**5. Counting is edition-specific and method-fragile.** From `dig-deeper-john-claim-audit.md`:

> "My first pass appeared to contradict Lincoln on four of his seven vocabulary statistics. Every one of those apparent contradictions was an artefact of my own regexes, not an error of his."

Two further notes from Proverbs are folded into Amendment E rather than given their own: **widen the window at the edges** (two of nineteen errors were units straddling the loaded range) and **derive blind, then compare** (reading a secondary structural map first destroys the independent-agreement check).

---

## Amendment A — Wire the local text corpus into the workflow

### Problem

The skill assumes the passage arrives in the conversation. `SKILL.md` reasons that no rule is needed to work from the Hebrew:

> "English OTs (ESV included) translate the Masoretic text, so the report's working text is *already* Hebrew and needs no rule to make it so."

That is true about the ESV's ancestry and false about the evidence in front of the run. Repetition, root-play, Leitwort, the petuchot and setumot, marked and unmarked comparison — none of it survives into any English version. The Proverbs note is the refutation: the ESV alone would have reproduced the sweep.

### What has changed

`_texts/` now exists in the dig-deeper folder: the Hebrew OT in Tanak order with a word-level lemma index, Swete's LXX, the SBLGNT with parsing, and the Logos exports, plus a search tool. Nothing needs pasting any more.

### File and anchor

`SKILL.md`, the **Workflow** phase table. Insert a new row between Phase 0 and Phase 0.5, and edit the Phase 0 row.

**Phase 0, replace:**

> | 0 | **Read the passage** in ESV. Read the surrounding chapter / section. Read enough of the book to know what's at stake. |

**with:**

> | 0 | **Read the passage in its original language first, then in ESV.** OT: the Hebrew from `_texts/hebrew-wlc/`. NT: the Greek from `_texts/greek-nt-sblgnt/`. Then the ESV, then the surrounding chapter / section, then enough of the book to know what's at stake. If the corpus is not reachable, say so in the Text-First Declaration and proceed from whatever text is supplied — but a run that never saw the original language may not report a count, a repetition, or a Leitwort as `[T]`. |

**Insert after Phase 0:**

> | **0.2** | **Load the substrate.** Locate `_texts/` in the connected prep folder and read its README before using it. Take the passage's Hebrew or Greek from the corpus, not from memory and not from a search. Every count, chain and repetition claim in the report is made against the corpus and **names its edition** — WLC, Swete, SBLGNT — because a count is edition-specific. Where a finding turns on a particular reading rather than on the wording generally (a variant, an apparatus question, a Rahlfs-vs-Swete divergence, an NA28 decision), the corpus is not enough: go to Logos and cite that. **Do not ask a search engine what a verse says.** |

Also add to **Phase 1** (Required reading), after the existing "Always view" bullets:

> - **Always view `_texts/README.md`** when the corpus is present. It states what each layer is and — more importantly — what each layer is *not*, so a proxy edition never gets cited as the edition it stands in for.

### Cost

One extra file read per run. In exchange, every lexical claim becomes reproducible by a third party months later, which is the precondition for Amendment C.

---

## Amendment B — Tanak order for the Old Testament

### Problem

Canonical position is evidence, and the skill does not ask for it. Of the 33 book overviews in the folder, **only three carry a Hebrew canon position section — and all three are the imported ones**, not produced by this toolkit. The house method has been silently working in English Bible order.

The consequences are not decorative. Ruth stands in the Ketuvim among the Megilloth, not after Judges. Daniel is in the Writings, not among the Prophets. Chronicles closes the Hebrew canon, which is what makes the Abel-to-Zechariah span of Matthew 23:35 reach from the first murder to the last — a reading that simply does not exist in English Bible order.

A second and separate point: **canonical order and compositional order are not the same thing, and the divergence is itself a finding.** Isaiah 36–39 and 2 Kings 18–20 is the standing example. Tanak order puts Kings (Former Prophets) *before* Isaiah (Latter Prophets); the argument from content runs the other way, since Isaiah predicts the fall of Jerusalem which Kings recounts. Both orders are data. The skill should record both and name the direction-of-dependence question rather than resolve it silently in either direction.

### File and anchor

**Edit 1** — `references/07-application-foundations.md`, Tool 14 (Bible Timeline). Insert a new subsection immediately after "### The three questions":

> ### Canonical position — where the book stands, not only where the events fall
>
> Tool 14 asks where a passage sits in the *story*. Ask alongside it where the book sits in the *canon*, and keep the two apart.
>
> **For every OT passage, state the book's position in the Tanak** — Torah, Nevi'im (Former or Latter), or Ketuvim — and one line on what that position implies for reading. Use the BHS order, in which the Ketuvim run Psalms, Job, Proverbs, Ruth, Song of Songs, Ecclesiastes, Lamentations, Esther, Daniel, Ezra–Nehemiah, Chronicles.
>
> Three positions carry weight often enough to name:
>
> | Book | Tanak position | What it changes |
> |---|---|---|
> | Ruth | Ketuvim, among the Megilloth | Not a Judges appendix. Read as a Writings reflection on ḥesed and on the line to David, addressed to a community that already knows how the monarchy ended |
> | Daniel | Ketuvim, not the Prophets | The book is presented as wisdom-in-exile before it is presented as prophecy |
> | Chronicles | Last book of the canon (BHS order) | The OT closes on a decree to go up and build, not on Malachi's curse. Matthew 23:35's Abel-to-Zechariah spans the whole canon, first murder to last |
>
> **Where canonical order and compositional order diverge, report both and resolve neither by default.** Isaiah 36–39 // 2 Kings 18–20 is the paradigm: Kings stands earlier in the Tanak, while the content argues that Isaiah's material is prior, since Isaiah predicts an exile Kings narrates. Name the divergence, give the evidence each way, flag the direction of dependence as an open question, and do not let sequence in either list function as an argument on its own.
>
> **One caveat to state if it ever becomes load-bearing.** BHS prints the Ketuvim beginning with Psalms and ending with Chronicles; Codex Leningradensis itself puts Chronicles *first*. The "Chronicles closes the canon" reading rests on the BHS and Talmudic sequence, not on L. Say which sequence a claim depends on.

**Edit 2** — `references/01-purpose-and-context.md`, Tool 2, in the "Levels of context" list. Add:

> - **Canonical context (OT):** where does this book stand in the Tanak, and what has the reader of *that* sequence already met? For an OT passage this is asked before the English-Bible neighbours, because the English order is a later arrangement and can plant a context the book's own tradition does not.

**Edit 3** — `SKILL.md`, Output Format template, Tool 14 line. Append:

> [For OT passages: Tanak position of the book, and one line on what it implies. Note any divergence between canonical and compositional order, with the direction-of-dependence question left open.]

### Cost

Two or three sentences per OT report. It will occasionally overturn a reading built on English-Bible adjacency, which is the point.

---

## Amendment C — The chain-verification gate

### Problem

The single named, repeated, project-specific failure mode: a verbal chain extended by inference into a verse that does not contain the word. Three instances, two books, found only because someone audited by hand afterwards. It is invisible to every existing gate, because a chain claim looks exactly like a good finding.

It is also now mechanically checkable. From the corpus:

```
$ python3 _texts/tools/find.py verify 7931 Exod:40:34 Exod:40:35
FAIL Exod 40:34
OK   Exod 40:35
```

*šākan* is at 40:35; 40:34 has only the noun *miškān*. The audit that found this by hand took a full pass. The gate takes one line and returns a non-zero exit status.

### File and anchor

**Edit 1** — `SKILL.md`, Phase 10.5 (the hard gate). Insert a new item after (e2):

> (e3) **Chain verification.** Every claim that a word, root or formula recurs across two or more verses is verified against the corpus lemma index — *by lemma, never by pointed surface form or English gloss* — and each claimed reference is confirmed to contain it. A reference that fails is removed from the chain or the chain is restated; it is never hedged and left standing. Where the corpus was unavailable, every chain claim is tagged `[unverified — chain not checked]` and may not be reported above moderate confidence, nor carried into a book overview. Counts name their edition. **A chain is the one kind of finding this project has repeatedly got wrong; treat an unverified chain as a defect, not a caveat.**

**Edit 2** — `SKILL.md`, Text-First Declaration block. Add a line after "**Depth floors:**":

> **Chains verified:** [n chains, n references checked against `_texts/` — or "None claimed" / "Corpus unavailable — all chain claims tagged unverified"]

**Edit 3** — `references/04-words-and-translations.md`, Tool 7 (Vocabulary), operational guidance. Add:

> **Verify before you report.** A recurrence claim is a claim about specific verses, so check those verses. Search the lemma, not the surface form: pointing, prefixes and suffixes make surface search unreliable, and that unreliability is exactly how a chain comes to be claimed at a verse that does not contain the word. If a link in a chain rests on sense rather than on the word, say so — a thematic chain and a verbal chain are different findings and should never be presented as one.

### Cost

A minute per chain. It would have caught all three known errors before they reached an overview.

---

## Amendment D — NASB95 as reference version, ESV as pulpit text

### Problem

`SKILL.md` currently switches off the pulpit-divergence check on the ground that report and pulpit share one text:

> "Because the report's default translation and the pulpit translation are now the same text, the report's ESV wording transfers directly into the manuscript — there is no ESV→pulpit gap to guard. Tool 8 therefore does **not** run a pulpit-divergence check."

That collapses a distinction worth keeping. The reference version and the pulpit version are two different things doing two different jobs, and where they diverge the pulpit text is doing interpretive work the congregation will hear and the preacher may not have noticed.

### File and anchor

`SKILL.md`, **Default Translation** section. Replace the "Pulpit translation note" paragraph with:

> **Reference version and pulpit version.** These are two texts with two jobs. The **NASB95** is the reference version — the more wooden rendering, used to see what the original is doing. The **ESV (Anglicised)** is the pulpit text: what the congregation hears read at CCH and what `/sermon-creator` quotes. Quote the ESV at the head of the report, because that is the wording the sermon will carry.
>
> **Tool 8 runs a live divergence check between them.** Where NASB95 and ESV differ in a way that bears on the finding — a connective dropped or supplied, a repeated root levelled into synonyms, a participle resolved into a finite verb, an ambiguity closed — say so, say which is closer to the original, and say what the congregation will therefore hear. This is not a translation-quality verdict; it is a note to the preacher about where the pulpit text has already made an interpretive decision on his behalf. KJV remains available as the historic witness where it earns its place, and the ancient-versions check runs as before.
>
> Where NASB95 and ESV agree, say nothing: silence is the normal case and the check should not generate filler.

### Cost

One extra comparison in Tool 8, reported only when it bears. Note that NASB95 is not redistributable and is not in the corpus; it comes from Logos per book, like the ESV.

---

## Amendment E — Audit trigger for synthetic claims

### Problem

The Exodus overview's finding is the most useful methodological sentence the project has produced: every claim needing correction was synthetic; every single-passage claim held. Passage-level work is more reliable than book-level work. Yet the skill applies the same standard of care to both, and the audit that catches book-level errors is an optional mode a user has to think to ask for.

### File and anchor

**Edit 1** — `SKILL.md`, after the **Adaptive Depth Principle** section, insert:

> ## Synthetic Claims Carry a Higher Burden
>
> A **passage-level** claim rests on one verified stretch of text. A **synthetic** claim is assembled across passages — a chain, a spine, an arc, a structural proposal, a count across a book, an argument that a theme develops. This project's audits agree, across two books independently, that synthetic claims fail at a much higher rate while single-passage claims hold.
>
> Treat them differently:
>
> 1. **Mark them.** Any finding assembled from more than one passage is flagged as synthetic in the report, so a later reader can see which claims carry the higher risk without re-deriving them.
> 2. **Verify every constituent.** A synthetic claim is only as good as its weakest reference. Each verse it rests on is checked against the text (Amendment C for verbal chains; re-read for anything else). Confirmation by the run that produced the claim is not evidence.
> 3. **Cap the confidence.** A synthetic claim whose constituents have not each been verified may not exceed moderate confidence, and may not enter a book overview.
> 4. **Widen the window at the edges.** Where a proposed unit boundary sits at the edge of the loaded passage, load more text before recording it. Two of the nineteen errors found in the Proverbs work were of exactly this shape.
> 5. **Derive blind, then compare.** Where a secondary source offers a structural map, derive the structure from the text first and open the source afterwards. A structure read first cannot then be independently confirmed, and the agreement is worth nothing.

**Edit 2** — `SKILL.md`, Multi-Passage Sweep Mode. Add a third adjustment:

> 3. **Book-level claims are provisional until audited.** A sweep produces synthetic claims faster than any other mode and verifies them less, because proportional depth cuts the checking first. Every cross-passage claim a sweep makes is marked synthetic and capped at moderate confidence until a claim audit or a chain verification has tested it. When the sweep hands off to a Finalise pass, name the synthetic claims explicitly as the audit's first targets.

### Cost

A flag on some findings and a confidence cap on others. It slows the passage from sweep to overview, which is precisely where the errors have been entering.

---

## Changelog entry to add

To be placed at the top of `references/CHANGELOG.md` if these are adopted:

> *Revised September 2026 (Primary-text corpus, Tanak order, chain verification, reference-vs-pulpit versions, synthetic-claim burden). Five amendments arising from the 2 September process review, each derived from a discipline that completed runs had already recorded in their own method notes with no mechanism to carry it forward. (A) A new Phase 0.2 loads a local primary-text corpus (`_texts/`: WLC with lemma index, Swete LXX, SBLGNT with parsing, Logos exports) and requires the original language to be read before the ESV, every count to name its edition, and readings that turn on a variant or apparatus to go to Logos — replacing the prior reasoning that the working text is "already Hebrew" because English OTs translate the MT, which the Proverbs 2A note refuted ("the ESV alone would have reproduced the sweep"). (B) Tool 14 gains a canonical-position subsection requiring the Tanak position of every OT book, with Ruth, Daniel and Chronicles tabulated, the BHS-vs-Leningrad Ketuvim caveat stated, and an explicit rule that where canonical and compositional order diverge (Isa 36–39 // 2 Kgs 18–20) both are reported and neither resolves the other; Tool 2 gains a canonical-context level. (C) Phase 10.5 gains hard gate item (e3) requiring every verbal-chain claim to be verified lemma-by-lemma against the corpus, with failing references removed rather than hedged and unverified chains barred from book overviews; the Text-First Declaration gains a chains-verified line. Rationale: three instances across Exodus and Jonah of "a verbal chain extended by inference into a verse that does not contain the word", the failure mode the Jonah audit named. (D) Default Translation now distinguishes NASB95 as reference version from ESV (Anglicised) as pulpit text and restores a live Tool 8 divergence check between them, replacing the note that switched the check off on the ground that report and pulpit shared one text. (E) A new section, Synthetic Claims Carry a Higher Burden, marks cross-passage claims, requires each constituent verified, caps unverified synthetic claims at moderate confidence, and adds the widen-the-window and derive-blind disciplines from the Proverbs runs; sweep mode marks its book-level claims provisional. Rationale: the Exodus overview's finding that every claim needing correction was synthetic while every single-passage claim held.*

---

## What is deliberately not proposed

**A blanket re-run of existing digs.** The evidence argues against it. Passage-level work has held; the errors are in book-level and synthetic material. The proportionate response is a chain-verification sweep across the OT documents first — mechanical, cheap, and it would have caught all three known errors — and then re-runs only where the audit moves a claim or the passage is next in the preaching diary. Jeremiah and Leviticus have already been rebuilt from the Hebrew and are the model.

**A Rahlfs layer in the corpus.** Every free machine-readable Rahlfs descends from CCAT/CATSS at Penn, whose licence asks the user to send a declaration first. Swete stands in as the search-and-count layer and Rahlfs-Hanhart comes from Logos for citation. If the CCAT declaration is ever sent, the corpus can gain a Rahlfs layer without any change to these amendments.

**Anything about the model.** No instruction in a skill or a project can select Opus over Sonnet; the model is chosen by the client. The only mechanism that works through project instructions is a request that the run state its configured model in the first line and stop if it is not the intended one — a project-instruction change, not a skill change, and so out of scope here.

---

*Prepared 2 September 2026. Proposed only — the installed skill is unchanged.*
