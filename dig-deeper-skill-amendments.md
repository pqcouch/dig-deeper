# Dig Deeper — Proposed Skill Amendments

**Status:** Draft v1.1 — **proposed, not applied.** Nothing in the installed skill has been changed.
**Date:** 2 September 2026 · **revised** 4 September 2026 (Amendment B gains a field template and a worked example)
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

**Edit 3** — `SKILL.md`, the **Hebrew and Greek — the Three-Way Triage** section. Replace the "Working default, stated plainly" paragraph with:

> **Working default, stated plainly — and the distinction it turns on.** English OTs, the ESV included, translate the Masoretic text. That settles one question and not another.
>
> It settles the **variant** question: because the ESV's *Vorlage* is the MT, no rule is needed to make the report's *textual basis* Hebrew rather than Greek. The confessional warrant for privileging the Hebrew (WCF 1.8, "immediately inspired… kept pure in all ages") is a claim about the Hebrew **original** and about providential preservation; it is not a ruling on any particular variant, and the Reformed themselves distinguished the two. Preserve that distinction: work from the Hebrew, and still weigh the variant on the evidence.
>
> It settles nothing about the **evidence** question. A translation of the Hebrew is not the Hebrew. Repeated roots, wordplay, a Leitwort, the count of a formula, a name-pun, the *petuchot* — none of these survives into any English version, so a report working from the ESV cannot see them and must not claim them. **The report's textual basis is already Hebrew; its evidence is not, until the Hebrew is opened.** That is what Phase 0.2 exists to do.

*Rationale: as it stands the paragraph is true of the first question and reads as though it settled the second, and that reading is what licenses a run to work from the ESV as though it were the Hebrew. The Proverbs 2A note is the refutation — "the ESV alone would have reproduced the sweep."*

**Edit 4** — `references/extensions/textual-variants.md`, the subsection "The working default, stated plainly". Same correction, same reason: the paragraph there carries the identical sentence ("The report's working text is therefore already Hebrew, and needs no rule to make it so"), and that file is mandatory viewing whenever the textual-variants extension applies. Replace its opening two sentences with the two-question distinction above, keeping the Owen/Walton material that follows.

> **This edit cannot be made by replacing `SKILL.md`.** It lives in the reference tree, which a SKILL.md replacement does not touch. If Amendment A is applied through a SKILL.md replacement alone, **the skill will carry the corrected paragraph in `SKILL.md` and the uncorrected one in `textual-variants.md`.** That is a tolerable interim state — `SKILL.md` governs, and the reference file's claim is narrower than it reads — but it is not the finished job, and it should be recorded as outstanding rather than forgotten.

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
> Where the passage is being worked at book level — a book-overview, a sweep, a
> macro-synthesis — state it as five fields. The first three are required; the
> last two are worth having when the series planning will use them.
>
> | Field | The question it answers |
> |---|---|
> | **Section** | Which canon division, and where within it |
> | **Reading implication** | What does standing *there* do to how the book is read? |
> | **Presupposes** | What has a reader of *this* sequence already met by the time they arrive? |
> | **Handoff** | What does the book pass to the one that follows it? |
> | **Neighbours** | What sits either side, and what would be missing without this book? |
>
> **`Presupposes` is the field that does the work, and the only one that produces
> testable claims.** Every item in it is a reference; every reference either
> supports the claim or does not. Fill it with references, not with themes, and
> check them — a canon-position section built on unchecked references is
> orientation dressed as evidence. The other fields orient; this one argues.
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

### Worked example — Ruth

The clearest case for the whole amendment, because the reading it produces cannot exist in English Bible order, and because it verifies exactly.

- **Section:** Ketuvim, among the Megilloth. In the order BHS prints, Ruth stands **immediately after Proverbs**.
- **Reading implication:** Not an appendix to Judges. A Writings reflection, read by a community that already knows how the monarchy ended, on how the line to David ran through *ḥesed* and through a Moabite.
- **Presupposes:** Proverbs, and specifically its closing poem. Deuteronomy 23:3–4 (no Moabite in the assembly). Genesis 38 (Tamar, named at Ruth 4:12). The Judges period as setting, not as literary neighbour.
- **Handoff:** the genealogy of 4:18–22 hands the sequence to David, whom the Ketuvim have already been reading about in the Psalter.

**The seam, verified.** Proverbs closes by asking *ʾēšet-ḥayil mî yimṣāʾ* — "a woman of worth, who can find?" (31:10). The next book in the sequence answers: *kî ʾēšet ḥayil ʾātt* — "for you are a woman of worth" (Ruth 3:11), said of a Moabite, by the whole town gate.

אֵשֶׁת חַיִל occurs three times in the Hebrew Bible — Proverbs 12:4, Proverbs 31:10, Ruth 3:11 — counted from `_texts/hebrew-wlc/` by searching for lemma 802 immediately followed by lemma 2428. In English Bible order the question and its answer never meet: Ruth sits after Judges, and Proverbs is nineteen books away.

### Provenance of this pattern

The five fields are not invented here. They are distilled from the only three documents in the folder that carry a canon-position section — the imported Genesis, Ezra-Nehemiah and 1 Peter overviews — which are reproduced verbatim, with a health warning on their content, in **`canon-position-pattern.md`**. That document exists because two other imported overviews, Jeremiah and Leviticus, were superseded on 28 August by fresh builds written to the same filenames, and the repository holds no earlier copy of either. The pattern is preserved here so that it survives whatever becomes of the three documents it came from.

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

## Amendment D — NASB95 as study text, pulpit text declared per engagement

### Problem

`SKILL.md` switches the pulpit-divergence check **off**, and does so by an argument that no longer holds:

> "Because the report's default translation and the pulpit translation are now the same text, the report's ESV wording transfers directly into the manuscript — there is no ESV→pulpit gap to guard. Tool 8 therefore does **not** run a pulpit-divergence check."

Two things are wrong with this. First, it collapses two texts doing two different jobs: the text used to see what the original is doing, and the text a congregation will hear. Second, and decisively, **the premise is false** — the pulpit text is not a constant. It is the ESV at the preacher's own church, but he preaches elsewhere, where it may be the NIV84 or another version entirely.

That makes the check more valuable, not less. A dynamic version such as the NIV84 will smooth exactly the features a text-first report is built on — a repeated root levelled into synonyms, a connective dropped, an ambiguity closed. Those are the moments the preacher most needs warning about, and they are invisible if the report assumes its own wording is what will be read aloud.

### File and anchor

`SKILL.md`, **Default Translation** section. Replace the "Pulpit translation note" paragraph with:

> **Study text and pulpit text.** These are two texts with two jobs, and only one of them is fixed.
>
> The **study text is the NASB95** — the 1995 edition specifically, not the 2020 revision, which is a substantially different text. Its woodenness is the point: it is the English that gets closest to showing what the original is doing. Quote it as the report's English reference.
>
> The **pulpit text is a variable and is declared per engagement.** It is the ESV (Anglicised) at the preacher's own church; when he preaches elsewhere it may be the NIV84 (not the 2011 revision) or another version. **If a sermon is in view and the pulpit text has not been stated, ask.** Do not assume the ESV. Where no sermon is in view — a book overview, a sweep, a claim audit — no pulpit text is needed and none should be invented.
>
> **Tool 8 runs a live divergence check between the study text and the declared pulpit text.** Where they differ in a way that bears on a finding — a connective dropped or supplied, a repeated root levelled into synonyms, a participle resolved into a finite verb, an ambiguity closed — say so, say which is closer to the original, and say **what the congregation will actually hear**. This is not a translation-quality verdict; it is a note to the preacher about where the pulpit text has already made an interpretive decision on his behalf. Expect the check to find more, and more that matters, when the pulpit text is a dynamic version.
>
> Where the two agree, say nothing. Silence is the normal case and the check must not generate filler. KJV remains available as the historic witness where it earns its place, and the ancient-versions check runs as before.

### A note on where the versions come from

Neither text is in the corpus, and neither can be: both are in copyright with no redistributable bulk source. Both come from Logos, exported per book into `_texts/logos-exports/`, with the version named in the filename — `NASB95 Ruth.txt`, not `NASB Ruth.txt`, because the 1995 and 2020 texts differ and a file that does not say which is worthless in two years.

### Cost

One extra comparison in Tool 8, reported only when it bears, plus one question asked when a sermon is in view and the pulpit text is unstated. The cost of *not* doing it is a report whose careful wording work is silently undone between the desk and the lectern.

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

> *Revised September 2026 (Primary-text corpus, Tanak order, chain verification, reference-vs-pulpit versions, synthetic-claim burden). Five amendments arising from the 2 September process review, each derived from a discipline that completed runs had already recorded in their own method notes with no mechanism to carry it forward. (A) A new Phase 0.2 loads a local primary-text corpus (`_texts/`: WLC with lemma index, Swete LXX, SBLGNT with parsing, Logos exports) and requires the original language to be read before the ESV, every count to name its edition, and readings that turn on a variant or apparatus to go to Logos — replacing the prior reasoning that the working text is "already Hebrew" because English OTs translate the MT, which the Proverbs 2A note refuted ("the ESV alone would have reproduced the sweep"). (B) Tool 14 gains a canonical-position subsection requiring the Tanak position of every OT book, with a five-field template for book-level work (Section, Reading implication, Presupposes, Handoff, Neighbours) in which Presupposes carries the testable claims and must be filled with checked references, with Ruth, Daniel and Chronicles tabulated, the BHS-vs-Leningrad Ketuvim caveat stated, and an explicit rule that where canonical and compositional order diverge (Isa 36–39 // 2 Kgs 18–20) both are reported and neither resolves the other; Tool 2 gains a canonical-context level. (C) Phase 10.5 gains hard gate item (e3) requiring every verbal-chain claim to be verified lemma-by-lemma against the corpus, with failing references removed rather than hedged and unverified chains barred from book overviews; the Text-First Declaration gains a chains-verified line. Rationale: three instances across Exodus and Jonah of "a verbal chain extended by inference into a verse that does not contain the word", the failure mode the Jonah audit named. (D) Default Translation now names the NASB95 (1995 edition, not the 2020 revision) as the fixed study text and makes the pulpit text a variable declared per engagement — ESV (Anglicised) at the preacher's own church, NIV84 or another version elsewhere — to be asked for when a sermon is in view and not assumed; Tool 8 runs a live divergence check between the study text and the declared pulpit text, reporting what the congregation will actually hear. This replaces the note that switched the check off on the ground that report and pulpit shared one text, a premise that was false as soon as the preacher left his own church. (E) A new section, Synthetic Claims Carry a Higher Burden, marks cross-passage claims, requires each constituent verified, caps unverified synthetic claims at moderate confidence, and adds the widen-the-window and derive-blind disciplines from the Proverbs runs; sweep mode marks its book-level claims provisional. Rationale: the Exodus overview's finding that every claim needing correction was synthetic while every single-passage claim held.*

---

## Consequential edits — found only by applying the amendments

Building the amended `SKILL.md` on 7 September surfaced something the spec had missed. Amendments A–E were each written against the passage they correct, but the ESV-as-both-texts assumption was **repeated in seven further places**, and applying the five amendments literally would have left the skill contradicting itself. All seven are now in the built file; they are recorded here so the spec is the reliable record.

| # | Where | What it said | Now |
|---|---|---|---|
| F1 | Default Translation, opening | "ESV unless the user has specified otherwise… Default to ESV for the passage quote" | Originals are the substrate; NASB95 is the English reference |
| F2 | Report template header | `**Pulpit translation:** ESV (Anglicised) — same text as the report default` | Three fields: primary texts opened, study text, pulpit text declared |
| F3 | Template, The Passage | "Quote the passage in full, ESV" | Hebrew or Greek from `_texts/`, NASB95 beneath |
| F4 | Template, Tool 8 | "Where ESV/NASB/KJV diverge" | NASB95, declared pulpit text, KJV |
| F5 | Template, Pulpit edition note | "State *Pulpit text matches report default*" | A real divergence note, or an explicit N/A where no sermon is in view |
| F6 | Quality Markers | "because the pulpit hears the ESV… no divergence to reconcile" | Findings rest on the originals; Tool 8 reports where the pulpit text has already decided something |
| F7 | Key Principles | "Report and pulpit share one text, so no pulpit-divergence check is needed" | Originals first, NASB95 as study text, pulpit text declared and checked |

**The lesson for any future amendment.** An assumption stated once in a governing section is usually restated in the template, the quality markers and the key principles, because those sections exist to summarise it. **Grep the whole file for the assumption, not just for the paragraph that argues it.** A spec written against the argument alone will leave the summaries contradicting the new rule, and the summaries are what a run under context pressure actually reads.

## What cannot be applied through `SKILL.md` at all

Four proposed edits live in the reference tree, which a `SKILL.md` replacement does not touch:

| Edit | File | Status |
|---|---|---|
| Amendment A, Edit 4 | `references/extensions/textual-variants.md` | the "needs no rule" paragraph, uncorrected |
| Amendment B, Edit 1 | `references/07-application-foundations.md` | Tool 14 canonical-position subsection |
| Amendment B, Edit 2 | `references/01-purpose-and-context.md` | Tool 2 canonical-context level |
| Amendment C, Edit 3 | `references/04-words-and-translations.md` | Tool 7 "verify before you report" |

Amendments B and C were therefore **re-sited into `SKILL.md` itself** in the built file — B as a new Phase 0.55 and an Output Format line, C as gate item (e3) and a Declaration line — so that the rules take effect even though the reference files are out of reach. That is the right call, because `SKILL.md` is read every run while a reference file is read only when its extension applies. **But it leaves the four files above stating the old position**, and that should be recorded as outstanding rather than forgotten.

## What is deliberately not proposed

**A blanket re-run of existing digs.** The evidence argues against it. Passage-level work has held; the errors are in book-level and synthetic material. The proportionate response is a chain-verification sweep across the OT documents first — mechanical, cheap, and it would have caught all three known errors — and then re-runs only where the audit moves a claim or the passage is next in the preaching diary. Jeremiah and Leviticus have already been rebuilt from the Hebrew and are the model.

**A Rahlfs layer in the corpus.** Every free machine-readable Rahlfs descends from CCAT/CATSS at Penn, whose licence asks the user to send a declaration first. Swete stands in as the search-and-count layer and Rahlfs-Hanhart comes from Logos for citation. If the CCAT declaration is ever sent, the corpus can gain a Rahlfs layer without any change to these amendments.

**Anything about the model.** No instruction in a skill or a project can select Opus over Sonnet; the model is chosen by the client. The only mechanism that works through project instructions is a request that the run state its configured model in the first line and stop if it is not the intended one — a project-instruction change, not a skill change, and so out of scope here.

---

*Prepared 2 September 2026. Proposed only — the installed skill is unchanged.*
