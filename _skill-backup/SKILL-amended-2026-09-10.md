---
name: dig-deeper
description: "Run the Dig Deeper 16-tool exegetical toolkit on a Bible passage, plus seven extensions (original languages, textual variants, historical background, biblical theology, difficult verses, Christological reading, original audience reception). Trigger when the user says dig deeper, run the toolkit, analyse this passage, prepare to preach, or wants to understand a passage before preaching. Also for claim audits: checking whether allusions hold, testing intertextual claims, auditing a book overview, or testing a new commentary, article or lecture before it enters an overview or sermon. Also for macro-synthesis: drawing together what a completed set of dig-deeper runs jointly demonstrates. Do not attempt serious passage-level exegetical work without this skill. Complements book-overview and point-purpose. Works from the original languages (the _texts/ corpus) as substrate, with NASB95 as study text and the pulpit text declared per engagement."
---

# Dig Deeper

Run a thorough exegetical analysis on a Bible passage using the sixteen tools from Beynon & Sach, *Dig Deeper: Tools to Unearth the Bible's Treasure* (IVP, 2005), supplemented by seven extensions that take the work to depth a preacher needs.

The skill produces **pure exegesis**. It does not produce a Teaching Point, Purpose Statement, or sermon structure. Hand off to `/point-purpose` for that.

---

## Reference Materials

### Core tools (one file per tool family)

| File | Tools covered |
|------|---------------|
| `references/01-purpose-and-context.md` | 1. Author's Purpose · 2. Context |
| `references/02-structure-and-flow.md` | 3. Structure · 4. Linking Words |
| `references/03-poetic-and-narrative.md` | 5. Parallels · 6. Narrator's Comment |
| `references/04-words-and-translations.md` | 7. Vocabulary · 8. Translations |
| `references/05-emphasis.md` | 9. Tone and Feel · 10. Repetition |
| `references/06-canonical-reading.md` | 11. Quotation/Allusion · 12. Genre |
| `references/07-application-foundations.md` | 13. Copycat · 14. Bible Timeline · 15. Who Am I? · 16. So What? |

### Extensions

| File | Purpose |
|------|---------|
| `references/extensions/original-languages.md` | Hebrew/Greek lexical, grammatical, and syntactical work |
| `references/extensions/textual-variants.md` | Manuscript variants that affect preaching |
| `references/extensions/historical-background.md` | Cultural, political, social context the original audience knew |
| `references/extensions/biblical-theology.md` | Theme tracing across the canon (kingdom, covenant, temple, exodus, etc.) |
| `references/extensions/difficult-verses.md` | Ethical, doctrinal, weaponised, apologetic, pastoral difficulties |
| `references/extensions/christological-reading.md` | Typology and Christological trajectory for OT (raw material for /point-purpose) |
| `references/extensions/original-audience.md` | What the first hearers would have understood, felt, or expected |
| `references/extensions/schnittjer-pass.md` | Schnittjer narrative-reading pass for Torah passages (Genesis–Deuteronomy) — book skeleton, narrative selectivity/space/shape, repetition, first-vs-second reading, polyacoustic intertextuality, irreducibility |

### Preacher extras

| File | Purpose |
|------|---------|
| `references/extensions/preacher-extras.md` | Operational guidance for Headline Findings (top of report) and Preaching Pitfalls (near bottom) |

### Mode-specific (load on demand)

| File | When to load |
|------|--------------|
| `references/claim-audit-format.md` | Only in Claim Audit Mode (Phase 0.5b) — standalone vs embedded decision, filename, full claim-audit file template, consumption rules |
| `references/macro-synthesis-format.md` | Only in Macro-Synthesis Mode (Phase 0.5c) — trigger/prerequisites, the standalone-file + book-overview-section deliverables, filename, the pattern-category checklist, the ≥3-pericope threshold, full template, and guardrails |

### Worked examples

| File | Purpose |
|------|---------|
| `examples/psalm-33-worked.md` | Full current-skill report on an OT poetry passage (Psalm 33:1–9). Demonstrates the Positional Necessity Check on a psalm (Psalter-sequence positioning), the OT Citation Triad with a Psalter-level Move 2, and warrant tagging without a book-overview in context. **Primary example for OT poetry.** |
| `examples/romans-8-31to39-worked.md` | Full current-skill report on an NT epistle passage with OT citations (Romans 8:31–39). Demonstrates Phase 0.6 (Positional Necessity Check), OT Citation Triad (Moves 1–3), warrant tagging (`[T]`/`[I]`/`[S]`), and the complete report format. **Use this as the primary worked example.** |

### Required reading

**Before producing the report**, view the tool/extension files relevant to the passage. Different passages will lean on different tools and extensions:

- **Always view:** all seven core tool files (01–07).
- **Always view:** `preacher-extras.md`.
- **Always view one worked example as a calibration anchor** — `examples/romans-8-31to39-worked.md` for NT prose/epistle passages, `examples/psalm-33-worked.md` for OT poetry; for other genres, view the Romans example. The worked example defines the *standard* the report must match: its depth per tool, its confidence-flagging density, its warrant-tagging habits, and its prose register. Before writing, ask: *would my report sit comfortably beside the worked example, or does it look thinner?* If thinner, deepen before writing.
- **Always view at least these extensions:** `historical-background.md`, `original-audience.md` — they apply to almost every passage.
- **View as applicable:** `original-languages.md` (where Hebrew/Greek work materially matters), `textual-variants.md` (check the catalogue against the passage), `biblical-theology.md` (most passages), `difficult-verses.md` (scan against your passage), `christological-reading.md` (always for OT; for NT when typology is in view).
- **Always view `_texts/README.md`** when the corpus is present. It states what each layer is and — more importantly — what each layer is *not*, so a proxy edition is never cited as the edition it stands in for.

Do not work from memory of the tool names. The reference files contain the operational details (worked examples, common pitfalls, decision rules) that make the difference between a competent report and an excellent one.

---

## Required Input

| Required | Notes |
|----------|-------|
| **Passage reference** | E.g. "Ruth 1:1–22", "John 3:16", "Romans 8:1–11" — **or a passage pair, for Synoptic Mode** (e.g. "Exodus 20:1–17 // Deuteronomy 5:1–33") |

If the passage isn't given, ask.

---

## Optional Inputs (Auto-Detect from Conversation)

| If present | How to use it |
|------------|---------------|
| `/book-overview` output (microscript, arc map, intertextual map, presenting situation, Christological trajectory, preaching traps) | **Front-load at Phase 0.5** (see Workflow). Extract the four active threads (Christological trajectory, intertextual map, preaching traps, presenting situation) before working the tools. Then use reactively: where findings confirm the overview, note agreement briefly; where they extend or contradict it, flag explicitly. |
| Prior `/point-purpose` output for the same passage | Reference for orientation. Do not let it constrain findings — Dig Deeper is meant to surface what the TP/PS might have missed. |
| Series context | Note briefly in the report header. |

### Text-First Discipline

The book-overview is a **planning document** — and it is only one of the secondary documents that may be sitting in context. A project may also contain a full **commentary, study notes, sermon manuscripts, lecture transcripts, or a prior dig-deeper report** on the same passage. All of these are *secondary sources*. Dig Deeper may legitimately surface evidence that any of them — the book-overview included — should be revised: a presenting situation the passage contradicts, an intertextual link the map missed, a structural arc that needs adjustment, a commentary claim the words won't bear.

> **The substrate is the biblical text — never a secondary exposition.** The single most damaging failure mode for this skill is letting a rich secondary source (especially a detailed commentary in the project files) become the *substrate* of the report rather than a *check* on it. A dig-deeper that reorganises a commentary's exposition into the sixteen tools is not a dig-deeper — it is a reformatting, and it is worthless as an audit, because a process that re-reads a source can only agree with it. If the conclusions could have been produced by reading the commentary **without opening the Bible**, the work has not been done.

Rules:

1. **Work the text first — before opening any secondary source.** Each tool's findings must be derivable from the passage itself (words, Hebrew/Greek where it matters, structure, immediate context, standard reference knowledge), **not** deduced from a book-overview, commentary, transcript, or prior report. Reach your own conclusions on the tools *first*; only then bring secondary sources in.
2. **Quarantine secondary expositions to a checking stage.** When a commentary, transcript, or other secondary exposition of the passage is present in context, do **not** read it as the basis for the tools. Work the text, then — in a distinct, later stage — consult the secondary source to *confirm, nuance, or resist* what you already found. Treat teaching transcripts and sermon notes as secondary too, even when they are the user's own.
3. **Tag findings by warrant.** For each non-trivial finding, make its basis visible: `[T]` derivable from the text itself; `[I]` a reasonable inference *from* the text but not stated by it; `[S]` supplied by a secondary source and held provisionally until checked. This keeps a recalled or commentary-sourced claim from being smuggled in as though the text demanded it.

   **The `[T]` boundary — do not stamp reconstruction as text.** `[T]` is for what the passage *on the page* states or directly shows: a superscription's attribution, a word that is present, a repetition you can point to, a connector that is written. It is **not** for claims about the book's **authorship, date, composition history, audience, occasion, liturgical or cultic use, *Sitz im Leben*, or its traditional title/label** — these are reconstructions or received descriptions, and are `[I]` at best, usually `[S]`, however venerable or conservative-sounding they are. *Sniff test:* could this be known only by someone standing **outside** the text — a historian, a form critic, church tradition? If yes, it is not `[T]`. Beware especially the **imported scholarly construct wearing conservative clothing**: e.g. "the Psalter was Israel's hymnbook" reads like a plain fact but is a Second-Temple, form-critical (Gunkel-Mowinckel) description — `[S]`, not `[T]`, and in tension with a canonical-shape reading of the book. What the text attests (a superscription; a temple-singer guild named in a narrative) and what tradition supplies about the *collection's* use are different warrants and must be tagged apart — **even within a single sentence** (`[T]` for the attribution, `[S]` for the "hymnbook" description). When a claim genuinely straddles categories, split it and tag each part rather than averaging to one comfortable tag.
4. **When findings agree with a secondary source, the agreement is only meaningful if the text-work was independent.** Note brief agreement ("Confirms book-level microscript X"; "Commentary concurs") — but remember that a confirmation is worthless if the finding *came from* that source. An earned confirmation requires `[T]` or `[I]` warrant reached before the source was opened.
5. **When findings disagree with or extend a secondary source, flag it explicitly** — `**Book-overview note:**` for the overview; `**Commentary note:**` (or similar) for other sources. Surfacing a claim the text won't bear is as valuable as surfacing one it confirms.
6. **Never silently overwrite a secondary source.** Surface the tension; let the user decide.

**Self-check before writing the report:** *Could this report have been written by someone who read the commentary/overview but never opened the Bible?* If yes, stop and re-work the tools from the text. *Are my "confirmations" of the commentary independent, or did the finding originate in the commentary?* If the latter, re-tag them honestly — they are not text-confirmations.

---

## Workflow

**Choose the mode first.** Fresh Exegesis (default — the full report, table below); **Claim Audit Mode** (Phase 0.5b — testing named claims from an overview or a new source); **Macro-Synthesis Mode** (Phase 0.5c — drawing together the cross-pericope arguments a completed set of dig-deeper runs jointly demonstrates); or **Synoptic Mode** (Phase 0.5d — one passage told twice in the canon, worked as a pair). The decision rules are at the end of each. If the ask is "is this claim/overview/source right?", it's a claim audit; if it's "what do all these runs add up to / what wider arguments emerge across the book?", it's a macro-synthesis; **if the passage has a canonical twin and the differences between them are part of what is being asked, it is a synoptic run** — and a synoptic run is a modified Fresh Exegesis, not a separate report format.

Work through the report in this order:

| Phase | What you do |
|-------|-------------|
| 0 | **Read the passage in its original language first, then in English.** OT: the Hebrew from `_texts/hebrew-wlc/`. NT: the Greek from `_texts/greek-nt-sblgnt/`. Then the English study text, the surrounding chapter / section, and enough of the book to know what's at stake. If the corpus is unreachable, say so in the Text-First Declaration and proceed from whatever text is supplied — but a run that never saw the original language may not report a count, a repetition, or a Leitwort as `[T]`. |
| **0.2** | **Load the substrate.** Locate `_texts/` in the connected prep folder and read its README before using it. Take the passage's Hebrew or Greek from the corpus, not from memory and not from a search. Every count, chain and repetition claim in the report is made against the corpus and **names its edition** — WLC, Swete, SBLGNT — because a count is edition-specific. Where a finding turns on a particular reading rather than on the wording generally (a variant, an apparatus question, a Rahlfs-vs-Swete divergence, an NA28 decision), the corpus is not enough: go to Logos and cite that. **Do not ask a search engine what a verse says.** **And know what the corpus cannot show you:** it holds **one** Hebrew manuscript tradition, so it can verify wording, counts and chains, and it can never report how widely an *apparatus* feature — a paragraph marker, an accent system, a ketiv — is attested. See gate item (e4). |
| 0.5 | **Book-overview active layer** — if a book-overview is in the conversation, extract the four threads described below and hold them in peripheral vision. Skip if no book-overview is present. |
| **0.55** | **Canonical position (OT passages).** State where the book stands in the Tanak — Torah, Nevi'im (Former or Latter), or Ketuvim — and one line on what that position implies for reading. Use the BHS order, in which the Ketuvim run Psalms, Job, Proverbs, Ruth, Song of Songs, Ecclesiastes, Lamentations, Esther, Daniel, Ezra–Nehemiah, Chronicles. Ruth stands among the Megilloth, not after Judges; Daniel is in the Writings; Chronicles closes the canon. **Where canonical order and compositional order diverge — Isa 36–39 ‖ 2 Kgs 18–20 is the paradigm — report both and resolve neither by default**, leaving the direction of dependence as a named open question. At book level state it as five fields: Section · Reading implication · Presupposes · Handoff · Neighbours, of which **Presupposes carries the testable claims and must be filled with checked references**. |
| **0.6** | **Positional Necessity Check** — for every passage, ask the two required questions from Tool 2 before working any other tool: (1) what has the preceding movement predicted, required, or set up that this passage now provides? (2) why does this passage exist *here* and not elsewhere? See `references/01-purpose-and-context.md`. |
| 1 | **View the seven core tool files** in `references/`. View `historical-background.md`, `original-audience.md`, and `preacher-extras.md`. View the genre-matching worked example in `examples/` as the calibration anchor (see Required reading). |
| 2 | **Identify which extensions apply** to this passage. View those files. |
| 3 | **Auto-detect** any book-overview or prior point-purpose work in the conversation. |
| 4 | **Work the 16 tools** in book order. Adaptive depth: rich where the tool surfaces something, brief where it doesn't, *N/A with a one-line reason* where the tool genuinely doesn't apply. **Note for Tool 11:** every significant OT citation requires the OT Citation Triad (Move 1 source context, Move 2 book usage, Move 3 OT-to-OT). *Significant = every direct quotation and every high-confidence allusion; moderate-confidence allusions receive Move 1 only.* **Move 4 (internal echo) is required for every passage, citation or not** — does this passage answer or plant something within its own book? Hold the book's opening unit(s) open while asking; run the addressee-differentiation check where the book opens by naming distinct parties. See `references/06-canonical-reading.md`. |
| 5 | **Work the extensions** for the passage. |
| 5.2 | **Schnittjer Pass** (Torah passages only) — if the passage is in Genesis–Deuteronomy, run the Schnittjer Pass (see `references/extensions/schnittjer-pass.md`). Skip with a one-line N/A for non-Torah passages. |
| 5.5 | **Checking stage (secondary sources).** *Only now* consult any commentary, lecture/sermon transcript, study notes, or prior report on the passage that is present in context. Use them to confirm, nuance, or resist the text-first findings already reached — not to generate findings. Re-tag warrants honestly: a point that turns out to have originated in the commentary is `[S]`, not `[T]`. (The book-overview, front-loaded at 0.5 as a thread-set, is also reconciled here for tensions.) When reconciling against neighbouring reports, **"neighbouring" means thematically adjacent reports *plus, always, any report covering the book's opening unit(s)*** — the opening is a permanent neighbour of every passage in the book, because it is where differentiated parties are named and quiet anticipations planted (Move 4's territory); thematic adjacency alone will not surface an opening-chapter boast answered fifteen chapters later. **If a claim audit for this passage is already in the conversation** (e.g. a `dig-deeper-[book]-claim-audit.md`), treat it as the checking-stage secondary source: do not re-derive what it has already tested; surface any tensions between its verdicts and the fresh text-first findings; note where the text-first work confirms, extends, or overturns the audit's conclusions. A claim audit that already rates an allusion "Confirmed with nuance" or "Discard" does not need to be reconstructed — accept the verdict and tag the relevant tool finding with `[S: audit]`. |
| 6 | **Generate Headline Findings** by reviewing convergent, high-confidence findings across tools and extensions. |
| 7 | **Generate Preaching Pitfalls** by reviewing common misreadings of this specific passage. |
| 8 | **Generate Convergent Findings** — places where multiple tools agreed (different from Headline Findings; the full list). |
| 9 | **Generate Open Questions** — anything flagged as uncertain that would benefit from verification. |
| 10 | **Generate Book-Overview Tensions** — if any tools disagreed with or extended the book-overview. |
| 10.5 | **Pre-output audit — a hard gate, not a review.** Check each item and treat any failure as a defect to fix *before* writing the file: (a) every significant OT citation carries the full triad; (b) every N/A has its one-line reason; (c) confidence flags present on all lexical/manuscript/intertextual claims; (d) every `[S]` finding was actually checked at Phase 5.5; (e) the Tool 8 ancient-versions check ran (or was considered and marked N/A with its reason); (e1) **every Hebrew/Greek divergence reported anywhere in the report is assigned to one of the three triage categories** — translation loss, substantive variant, or the NT's own text — with category 2 carrying evidence and a confidence flag, no divergence resolved by a blanket preference for either text, and every count stated or implied "in the Hebrew"; (e2) the proper-noun inventory ran, every load-bearing name-hyperlink and character dossier honoured the load-the-story rule, and every non-verbal allusion carrier (dossier, route, pattern-break absence) carries a stated weight — with any absence claim citing its established pattern; **(e3) every claim that a word, root or formula recurs across two or more verses is verified against the corpus lemma index — *by lemma, never by pointed surface form or English gloss* — and each claimed reference confirmed to contain it; and where a **phrase** search is unavoidable, **maqqef (־) and paseq (׀) are normalised to spaces** as well as NFD-stripping combining marks, since neither is a combining mark and both defeat a whitespace pattern silently, returning a nil on a text that contains the phrase; a reference that fails is removed from the chain or the chain restated, never hedged and left standing; where the corpus was unavailable every chain claim is tagged `[unverified — chain not checked]`, may not be reported above moderate confidence, and may not enter a book overview; counts name their edition. A chain is the one kind of finding this project has repeatedly got wrong — treat an unverified chain as a defect, not a caveat**; **(e4) every finding resting on a feature of the *apparatus* rather than on the wording — *parashoth* (petuchah/setumah), accentuation, ketiv/qere, Masorah, sigla — names its witness rather than the tradition** ("in Leningrad", "as BHS prints it", never "the Masoretic text" unqualified), **states that the feature is a reading tradition and not authorial** where that is so, and has had **one library pass on its manuscript spread** before it enters a book overview or a sermon; where that pass has not been run the finding is tagged `[unchecked — apparatus spread]`, capped at moderate confidence, and barred from an overview on the same terms as an unverified chain. The corpus holds **one manuscript tradition** and prints these features without variants, so **a verified count and an unrepresentative witness look identical from inside it**; (f) the depth floors are met (five substantial tools; Headline Findings 3–5; Pitfalls ≥2); (g) the report would sit comfortably beside the genre-matching worked example; (h) all mandatory reference files were viewed; (i) **no `[T]` tag sits on an authorship / date / composition / audience / occasion / setting / cultic-use / traditional-label claim the passage does not itself state** — every such claim is re-tagged `[I]`/`[S]`, and split-warrant sentences tag each part (the `[T]` boundary, Text-First Discipline). If any item fails, return to the relevant phase and fix it — do not ship with a noted failure. Record the results as the report's **Text-First Declaration**. |
| 11 | **Write the report and render it to `.odt`** as `dig-deeper-[passage-slug].odt`, applying the house style (see Output Format for style spec and location). |
| 12 | **Present** the file: on claude.ai use `present_files`; in Claude Code report the file path. |

### Multi-Passage Sweep Mode

When asked to run dig-deeper on **six or more passages from the same book in a single session**, the standard one-passage workflow applies to each passage in turn, but with two adjustments:

1. **Proportional depth per passage.** With six or more passages, each receives less depth than a solo passage analysis — the adaptive depth principle applies at session level. Prioritise Headline Findings, the tools where depth matters most for that passage (Tool 11 for OT books; Tool 2 and the Positional Necessity Check for every passage; the passage's dominant tool from genre), and the extensions that are live. Brief N/As are more common in sweep mode.

2. **Cross-passage convergent findings.** After all passages have been worked, add a **Cross-Passage Convergent Findings** section at the end of the combined report. This section collects findings that emerge from the *intertextual network between the passages* — allusion threads that run across multiple passages, structural patterns that only become visible when passages are read in sequence, vocabulary threads that carry across the arc, and presuppositions from an earlier passage that are required by a later one. This is materially different from the within-passage convergent findings — it is what only becomes visible when the passages are read as a sequential whole.

3. **Book-level claims are provisional until audited.** A sweep produces synthetic claims faster than any other mode and verifies them less, because proportional depth cuts the checking first. Every cross-passage claim a sweep makes is marked synthetic and capped at moderate confidence until a claim audit or a chain verification has tested it. When the sweep hands off to a Finalise pass, name the synthetic claims explicitly as the audit's first targets.

Multi-passage sweep mode is not for deep exegetical preparation of any single sermon; it is for auditing a book-overview, producing planning material across a series arc, or identifying which claims need the most careful checking before the series begins. For any ⭐ HIGH-weight passage, a full solo dig-deeper should be run before pulpit preparation.

---

### Phase 0.5 — Book-overview active layer

When a book-overview is present, extract these four threads before working the tools and hold them in *peripheral vision* throughout — they orient the exegesis without driving it.

| Thread | What to extract |
|--------|----------------|
| **Christological trajectory** | How this book points to Christ |
| **Intertextual map** | Which OT texts are mapped as active in or near this passage — and critically, which OT sources have been used *earlier* in this book (for Tool 11 Move 2 book usage tracking) |
| **Preaching traps** | Book-level traps that may have passage-level manifestations |
| **Presenting situation** | The concrete historical/canonical circumstances shaping how the book is heard |

These are background awareness, not a confirmation checklist. Not every thread will be live in every passage. The goal is to orient what "deeply worked" looks like for this particular book. Dig Deeper may legitimately produce evidence that the book-overview should be revised — surface it; don't suppress it to protect the overview.

**Intertextual map — specific preparation for Tool 11:** When extracting the intertextual map thread, note which OT *sources* (not just verses) have been used earlier in the book. This is the input for Tool 11's Move 2 (book usage tracking). For example: if the book-overview shows Deuteronomy 32 cited at three earlier points, any new Deuteronomy 32 citation in the current passage must be read against those earlier uses — the author may be following Deuteronomy 32's own internal arc.

**No book-overview present?** If no book-overview is in conversation, Move 2 still applies. Build the source-tracking yourself: scan the passage's immediate context for earlier citations from the same OT source, and note what they did. For a series passage, check any prior dig-deeper reports in the conversation. A minimal Move 2 ("no earlier citation of this source found in the surrounding context") is better than skipping the move.

**Monograph-sourcing flag:** If the book-overview draws significantly on a single scholarly source (monograph or commentary), identify which claims are sourced primarily from that source. For each, ask what 2–3 major commentaries say. A claim that appears in only one monograph and no other major commentary should be treated with additional scrutiny — it may be a minority reading, a speculative connection, or an overclaimed allusion. Flag these explicitly under the relevant tool as `**Single-source claim:**`.

---

### Phase 0.6 — Positional Necessity Check *(universal — every passage)*

**Before working Tools 1–16**, run the Positional Necessity Check from Tool 2 (`references/01-purpose-and-context.md`). This applies to every passage in every genre — not only NT epistles.

**The two required questions:**

1. *What has the preceding argument, narrative, or movement predicted, required, made possible, or set up — that this passage now provides, answers, enacts, or resolves?*
2. *Why does this passage exist here — after what has preceded it — and not somewhere else in the book?*

Record the answers in the Tool 2 section of the report before proceeding.

**Revisit after Tool 11:** Once Tool 11's Move 2 (book usage tracking) is complete in Phase 4, briefly check whether the book-usage findings add to or sharpen the doctrinal-prediction answer. A source tracked across multiple earlier passages may reveal a structural argument not visible at Phase 0.6.

**The implicit-connection case is the most commonly missed.** When there is an explicit connector ("therefore," "for this reason") the check is easy. When the connection is implicit — the passage exists because the preceding movement has predicted a pattern or opened a question that now requires this passage, without naming it — the check is most critical. Do not skip Phase 0.6 on the grounds that no explicit connector is visible; the absence of a verbal bridge does not mean the positional relationship is absent.

**Depth is proportional to what the check surfaces.** For many passages the positional relationship is obvious and the check is brief. For passages where the relationship is implicit or has been missed (as in Claim Audit Mode), it warrants detailed treatment before the tools are worked.

---

### Phase 0.5b — Claim Audit Mode (alternative to Fresh Exegesis)

When the task is to *test* specific claims from a book-overview, a new secondary source (commentary, article, lecture, monograph), or both — rather than to develop exegesis from scratch — use **Claim Audit Mode**:

1. **Run the Positional Necessity Check first (Phase 0.6).** Before scoping the specific claims to audit, ask both required questions about this passage's position in the book. A claim that looks like a historical-background question may actually be a positional-argument question — and Phase 0.6 will surface this (see the Romans 14–15 worked example in `references/01-purpose-and-context.md` § Positional Necessity Check, where the Claudius-expulsion claim turned out to be a positional-argument question). Do not skip Phase 0.6 in Claim Audit Mode — the positional frame determines the frame within which individual claims should be evaluated.

2. **Name the claims upfront.** List the specific claims being tested — from the book-overview, from the external source, or both (e.g., "the verbal echo between Gen 3:6 and 2 Sam 11:2–4"; "David's last words use Balaam's prophetic formula"; "Scacewater's proposed governing concern for Ephesians 1–3").

3. **Apply the Hays criteria to each allusion claim.** For each intertextual claim: score it on Availability, Volume, Recurrence, Thematic Coherence, Historical Plausibility, History of Interpretation, and Satisfaction. State a confidence level.

4. **Reorient tool depth.** In Claim Audit Mode, Tools 7 (Vocabulary), 8 (Translations), and 11 (Quotation/Allusion) receive the deepest treatment. Tools 9 (Tone), 12 (Genre), and 13 (Copycat) may be brief. **For intertextual claims specifically:** apply the full OT Citation Triad (Move 1 source context, Move 2 book usage, Move 3 OT-to-OT) to the cited OT passage — even for claims the overview marks as confident. The triad commonly surfaces evidence that changes the confidence verdict.

5. **Produce explicit verdicts.** Each claim receives one of: Confirmed / Confirmed with nuance / Needs reframing / Uncertain — flag for research / Discard.

6. **Surface what the overview missed.** Claim Audit Mode should also be alert to significant connections the overview *didn't* note — a strong allusion the overview overlooked is as important a finding as an overclaimed one. The Positional Necessity Check (Phase 0.6) is specifically designed to surface these structural misses.

**The Claim Audit Mode failure pattern to avoid:**

Scoping the audit to the passage level before running Phase 0.6. The positional question — *why does this passage exist here, after what has preceded it?* — must precede the claim-level audit. Scoping claims first, then asking positional questions, means the positional question is answered within the frame the claim-level scope has already established, which forecloses the most important findings. This applies for every passage in every genre, not only NT epistles.

**Choosing the mode (Fresh Exegesis vs Claim Audit vs Macro-Synthesis vs Synoptic):**
- **Fresh Exegesis:** When beginning passage preparation from scratch; when no book-overview is present; when the preacher wants a full exegetical report on one passage.
- **Claim Audit:** When a book-overview exists and the goal is to test its claims before the preacher enters the pulpit; when a new commentary, article, or lecture arrives mid-series and its claims must be tested before incorporating them into the overview (see `book-overview/references/upgrading-overviews.md`); after a long preparation session that has produced a body of claims needing verification; when the audit question is "Is this overview correct?" or "Does this source add anything the text warrants?"
- **Macro-Synthesis:** When all (or nearly all) pericopes of a book already have full solo dig-deeper runs and the goal is to draw out the cross-pericope arguments the sweep jointly demonstrates; when the question is "what do all these runs add up to?" or "what wider arguments emerge across the book?" Operates *across* completed runs, not on a single passage — so it presupposes a finished (or near-finished) sweep, where Fresh Exegesis and Claim Audit operate on one passage at a time.
- **Synoptic:** When the passage is told twice in the canon and the differences are part of the question. Operates on **two passages at once**, where Fresh Exegesis and Claim Audit operate on one and Macro-Synthesis operates across completed runs.

---

### Claim Audit Output Format

**When Claim Audit Mode is active, view `references/claim-audit-format.md` before scoping the audit.** It covers: the standalone-file vs embedded-verdicts decision (make it upfront — it shapes how the audit is worked), the filename convention (`dig-deeper-[book]-claim-audit.md`), the full file template (Hays criteria table, verdict categories, summary counts, confidence change propagation), and how subsequent dig-deepers consume the audit file at Phase 5.5.

---

### Phase 0.5c — Macro-Synthesis Mode (alternative to Fresh Exegesis)

When the task is not to exegete a passage or test a claim but to *read across a completed set of dig-deeper runs* for the cross-pericope arguments no single run could establish — use **Macro-Synthesis Mode**. This mode is the toolkit turned sideways: its raw material is the **Convergent Findings** and **Book-Overview Tensions** the runs have already produced, not the biblical text directly.

1. **Check the prerequisite gate first.** Run Macro-Synthesis Mode only when all, or nearly all, pericopes of the book have full solo dig-deeper runs in hand (a single missing Standard-weight pericope is acceptable; a missing HIGH-weight one is not — finish it first). If the sweep is incomplete, say so and either finish it or scope the synthesis explicitly to the runs in hand, flagged as provisional. **Do not run it early** — a synthesis built on three or four runs manufactures patterns from too little evidence.

2. **Mine the runs, do not re-exegete.** For each run read its Convergent Findings, Book-Overview Tensions, Headline Findings, and Christological Reading. Macro-Synthesis consumes the runs' conclusions; it does not re-open the sixteen tools. If a finding looks wrong, that is a signal to re-run *that pericope*, not to overrule it here.

3. **Cluster by category, honour the ≥3-pericope gate.** Sort recurring observations into the pattern-categories in the reference file. A pattern qualifies as a *macro-argument* only when it recurs across **≥3 pericopes** (or is NT-authorised across ≥2). One-pericope threads are listed, if at all, as candidates flagged "not yet macro".

4. **Rank confidence with the toolkit's discipline.** NT-authorised links = high; converging text-first findings reached independently across runs = strong; looser trajectories = moderate. Carry the runs' own `[T]`/`[I]`/`[S]` warrant tags forward honestly — an `[S]` chain stays `[S]`; do not launder it into a confident pattern.

5. **Produce both deliverables.** A standalone synthesis file (`[book]-dig-deeper-macro-synthesis.md`) and a condensed "Cross-Pericope Macro-Arguments" section patched back into the book-overview. Apply the overview patch with the standard discipline (copy to working dir, `str_replace`, colophon bump, provenance tag).

**The Macro-Synthesis Mode failure pattern to avoid:**

Manufacturing patterns — imposing a thematic grid on the runs rather than letting it emerge from them. The ≥3-pericope threshold is a hard gate against this; an honest "this book does not do X" is a finding, not a gap to fill. A connection the runs individually noted but never drew together is exactly what this mode exists to catch — but the catch must still clear the gate.

---

### Macro-Synthesis Output Format

**When Macro-Synthesis Mode is active, view `references/macro-synthesis-format.md` before scanning the runs.** It covers: the trigger and prerequisite gate, the standalone-file + book-overview-section deliverables, the filename convention (`[book]-dig-deeper-macro-synthesis.md`), the book-agnostic pattern-category checklist, the full long-form and condensed-section templates, the guardrails against manufactured patterns, and how the synthesis is consumed in later overview-upgrade and sermon-prep work.

---

### Phase 0.5d — Synoptic Mode (a modified Fresh Exegesis)

**Adopted on trial, September 2026.** Unlike the other amendments of its round, this mode rests on a single completed run. Treat it as a hypothesis to be tested by the next synoptic run, not as settled method — and if a synoptic report turns out worse than two separate digs would have been, say so and withdraw the mode.

Run this when the passage is told **twice** in the canon and the relation between the tellings is part of the question. It is not a separate report format: the sixteen tools, the extensions and the template all stand. What changes is the shape of the work.

**1. Settle the direction of dependence before anything else, and never by default.** Three cases, and they are not interchangeable:

| Case | Signal | How the run treats the pair |
|---|---|---|
| **Stated** | The later text names the earlier (Deut 5:12, 16 *"as the LORD your God commanded you"*) | Original and authorised re-issue. Differences are the later author's own application, and are read as homiletic moves |
| **Open** | Neither text marks priority; canonical and compositional order may diverge (**Isa 36–39 ‖ 2 Kgs 18–20** — the case Phase 0.55 already names) | **Report both orders, resolve neither.** Differences are evidence in an unresolved question and may not be narrated as one text "editing" the other |
| **Contested** | A scholarly hypothesis supplies the direction, the texts do not | Name the hypothesis as `[S]`, work the differences without it, and say what each direction would imply |

**Getting this wrong is the mode's characteristic failure.** A run that assumes priority will describe a difference as a deliberate change, which is a claim about an author's intention that the "open" case cannot support.

**2. Work in three movements.** Passage A in its own frame; passage B in its own frame; then the comparison. Do not average the two into a composite: **the harmonised text exists nowhere and is the mode's first pitfall.** Where one passage already has a completed solo dig, consume it at Phase 0.5 rather than re-working it, and say so in the scope note.

**3. Run Phase 0.6 twice.** Each passage's positional necessity is a fact about its own book and cannot be inherited from its twin.

**4. Diff mechanically before reading either text closely.** Align the passages verse by verse and compare the originals with accents, maqqef and paseq normalised (gate item (e3)). A mechanical diff is reproducible, catches what the eye slides over, and — crucially — **establishes what is identical**, which is as much a finding as what differs. Report the count of unchanged material explicitly.

**5. Expect the Triad to behave differently.** Where the source is inside the same corpus as the citing text (Deuteronomy quoting Exodus), Move 2 (book usage) and Move 4 (internal echo) largely coincide. Say so rather than filing a nil return for one of them.

**6. Reconcile against *both* book-overviews, and report the asymmetry.** Two overviews are live and they are rarely equally mature. Where one is materially behind the other — older, pre-corpus, built on a sweep rather than on solo digs — **that gap is a finding for the Book-Overview Tensions section**, because the weaker overview will systematically lack whatever the run's original-language work produced.

**7. File it where it belongs to neither passage.** A report spanning two books goes at the level above both — the Torah root, the corpus root — not in either book's folder, with a cross-reference from each. Filename per the two-passage convention below.

**Known pairs.** Exod 20:1–17 // Deut 5:1–33 (stated); Isa 36–39 ‖ 2 Kgs 18–20 (open); 2 Sam 22 ‖ Ps 18 (open); Ps 14 ‖ Ps 53 (open); Obad 1–9 ‖ Jer 49:7–22 (open); Exod 23:10–19 ‖ Exod 34:11–26 (within one book); Samuel–Kings ‖ Chronicles; the Synoptic Gospels (contested).

**Choosing Synoptic Mode.** Use it when the user names both passages; when the user names one and asks about its twin; or when a passage in the table of known pairs is brought for a full dig and the differences bear on the findings. **Do not** use it to compare thematically similar passages that are not textual twins — two accounts of a similar event are not a synoptic pair, and the mode's discipline (mechanical diff, direction of dependence) has nothing to work on.

**Depth floors in Synoptic Mode** are met **per report, not per passage** — the comparison is where the depth goes.

---

## Adaptive Depth Principle

**Depth is proportional to what each tool surfaces.**

- A tool that opens up the passage gets a paragraph or several. Linking Words in Romans 1, Parallels in a Psalm, Genre in Revelation, Repetition in Daniel 3 — these warrant detail.
- A tool that is technically applicable but adds little gets one or two sentences.
- A tool that genuinely doesn't apply gets a brief `**N/A** — [one-line reason]`.

Legitimate N/A:
- Narrator's Comment on an epistle (epistles aren't narrative)
- Parallels on a NT prose argument with no poetic structure
- Copycat on a Pauline imperative passage with no narrative characters

**Depth floors (solo Fresh Exegesis runs).** Adaptive depth is a ceiling-setter, not a licence to thin the report. For a solo run, the following are minimums, whatever model is executing. **In Synoptic Mode they are met per report, not per passage** — the comparison is where the depth goes:

- At least **five tools** receive substantial treatment (multiple paragraphs or structured detail), including the passage's genre-dominant tool and Tool 2 (with its Positional Necessity Check).
- Tools 1, 2, 7, 8, 11, and 16 are **never** dispatched in a single sentence unless marked N/A with reason (7 and 11 rarely qualify for N/A).
- Headline Findings: exactly 3–5, each a full sentence or two of claim-plus-evidence, not a topic label.
- Preaching Pitfalls: at least 2, each with a corrective.
- Confidence flags: every lexical, manuscript, or intertextual claim carries one — a solo report with fewer than five confidence flags has almost certainly under-flagged.
- **When uncertain whether a tool deserves brief or full treatment, choose full.** Under-writing is the characteristic failure; over-writing is easily trimmed.

**Resist the pull to skip tools that feel hard.** Vocabulary, Translations, Quotation/Allusion, and the extensions often feel skippable but reward the effort — they're frequently where the best findings live. Attempt them and flag uncertainty rather than skipping.

---

## Synthetic Claims Carry a Higher Burden

A **passage-level** claim rests on one verified stretch of text. A **synthetic** claim is assembled across passages — a chain, a spine, an arc, a structural proposal, a count across a book, an argument that a theme develops. This project's audits agree, across three books independently, that synthetic claims fail at a much higher rate while single-passage claims hold.

1. **Mark them.** Any finding assembled from more than one passage is flagged as synthetic, so a later reader can see which claims carry the higher risk without re-deriving them.
2. **Verify every constituent.** A synthetic claim is only as good as its weakest reference. Confirmation by the run that produced the claim is not evidence.
3. **Cap the confidence.** A synthetic claim whose constituents have not each been verified may not exceed moderate confidence, and may not enter a book overview.
4. **Widen the window at the edges.** Where a proposed unit boundary sits at the edge of the loaded passage, load more text before recording it.
5. **Derive blind, then compare.** Where a secondary source offers a structural map, derive the structure from the text first and open the source afterwards. A structure read first cannot then be independently confirmed.
6. **A stated count is the most auditable claim a report can make** — and both real findings of the September 2026 audits came from checking numbers, not word-presence. Every count names its edition and is reproducible in one command.

---

## Consistency Contract *(applies to every model executing this skill)*

This skill must produce reports of the same shape, depth, and discipline whether run by Opus, Sonnet, or any other model. The following rules remove the discretion where runs diverge:

1. **Follow the phase table literally and in order.** Do not merge, reorder, or skip phases. If a phase genuinely doesn't apply (e.g. 0.5 with no book-overview), say so in one line and move on — don't silently omit it.
2. **View every mandatory reference file; never work from memory of what a file "probably says".** If a file was viewed earlier in the conversation and its content is still fully in context, that counts; otherwise re-view. Working the tools from recalled tool-names instead of the operational files is the primary way runs degrade.
3. **Reproduce the output template exactly.** Every heading, in order, verbatim, including sections that end up brief or N/A. Never collapse sections together, rename them, or invent a shorter format because the passage feels small.
4. **Match the worked example's standard, not your instinct.** The genre-matching example in `examples/` is the calibration anchor for depth, register, and flagging density. Deviations should be passage-driven, not model-driven.
5. **Under context pressure, shed nothing from the report.** If the session is long, prefer re-viewing reference files over trimming tools; if truly forced to economise, economise in your working notes, never in the delivered template or the depth floors.
6. **Honour every hard gate mechanically:** the OT Citation Triad significance rule, the ≥3-pericope macro gate, the Phase 0.6 two questions, the Tool 8 ancient versions check, the systematic-sweep trigger. These are checks to run, not judgements to weigh.
7. **When judgement is genuinely required** (an interpretive crux, a contested allusion), don't resolve it silently with a confident sentence — show the options, flag confidence, and route it to Open Questions if unresolved. Consistency across models comes from displaying the reasoning, not from every model landing the same verdict.

---

## Handling Tools That Need External Data

Several tools and extensions benefit from a lexicon, multiple Bible versions, a concordance, or a commentary.

Protocol:

1. **Attempt from training knowledge first.** Claude has strong knowledge of biblical Hebrew/Greek vocabulary, major translation differences, common intertextual links, textual variants, historical background, and typological connections — use it.

2. **Flag confidence levels explicitly:**
   - `*High confidence:*` for well-known data (e.g., *ḥesed* meaning; "I AM" in John 8 alluding to Exodus 3)
   - `*Moderate confidence:*` for plausible but not certain claims
   - `*Uncertain — consider verifying:*` for anything where Claude is reaching

3. **When uncertain, ask the user or suggest web search.** Frame it as a choice when the claim materially affects the report:
   > "I'm not certain whether the Greek behind 'redemption' here (*apolytrōsis*) is the same word used in Ephesians 1:7. Want me to (a) attempt + flag, (b) get you to check a lexicon, or (c) web-search to confirm?"

   For minor points, just attempt + flag without asking.

4. **Point any available cross-reference tool (Logos, a concordance, a parallel-passage tool) at a *systematic sweep* for Tool 10 and Tool 11 — not only at known uncertainties.** Targeted queries answer a question you have already framed (a contested preposition, a textual crux, a piece of historical background); they cannot surface citations or repetitions you never thought to ask about. A cross-reference tool's strength is bulk phrase-matching across the whole canon — exactly what the phrase-level Move 2 check (`06-canonical-reading.md`) and a thorough Repetition pass need. **Before closing out Tool 10/11 on a passage that names five or more distinct concrete things (places, objects, peoples, numbers), or on any OT citation a secondary source named, run at least one systematic sweep** in addition to your targeted queries. Tag the results `[S]` and treat them as checking-stage material — confirming or extending the text-first work, never replacing it.

5. **Treat a research tool's answers as claims to test, exactly as you would a commentary's — and know its two characteristic errors.** A cited answer is not a verified answer, and the citation is what makes it feel like one.

   **(a) It reasons from the English version by default.** Any answer about what "the text says", what a term "is", or how Scripture "refers to" something must be checked against the corpus before it is reported. *Worked example:* asked how the Bible designates the Decalogue, a Study Assistant answered that the biblical texts "consistently employ 'Ten Commandments'", citing Exod 34:28; Deut 4:13; 10:4 — the three verses whose Hebrew reads עֲשֶׂרֶת הַדְּבָרִים, "the ten words". The citations were right and the conclusion was an artefact of reading a rendering as the designation. **Where a tool's answer and the corpus disagree about wording, the corpus wins and the disagreement is itself worth reporting.**

   **(b) It will answer from general knowledge when the library has nothing.** Such answers usually carry a disclaimer, and the disclaimer is easy to miss beside a well-cited paragraph in the same reply. **Check every claim for a source before relying on it**, and downgrade an uncited claim to the same standing as Claude's own recall — which is to say, flag it and verify it.

   Where a tool's answer **corrects** the run, say so at the point of use and rewrite the finding around it rather than appending a caveat. Where the run **corrects the tool**, argue it from the text rather than asserting it. Both are reportable; neither is embarrassing.

---

## Translations — Study Text and Pulpit Text

**The original languages are the substrate; the English versions are references.** See Phase 0.2. When quoting:
- Quote the **NASB95** as the report's English reference at the head of the report, alongside the Hebrew or Greek the findings actually rest on.
- Under the Translations tool, compare the NASB95 with the declared pulpit text (below) and with the KJV as the historic witness where it earns its place. Bring in a dynamic version only when the point is to show what a smoother rendering obscures — and note that a dynamic version *is* the pulpit text at some engagements.

**Study text and pulpit text.** Two texts, two jobs, and only one of them is fixed.

The **study text is the NASB95** — the 1995 edition specifically, not the 2020 revision, which is a substantially different text. Its woodenness is the point: it is the English that gets closest to showing what the original is doing. Quote it as the report's English reference.

The **pulpit text is a variable, declared per engagement.** It is the ESV (Anglicised) at the preacher's own church; when he preaches elsewhere it may be the NIV84 (not the 2011 revision) or another version. **If a sermon is in view and the pulpit text has not been stated, ask.** Do not assume the ESV. Where no sermon is in view — a book overview, a sweep, a claim audit — no pulpit text is needed and none should be invented.

**Tool 8 runs a live divergence check between the study text and the declared pulpit text.** Where they differ in a way that bears on a finding — a connective dropped or supplied, a repeated root levelled into synonyms, a participle resolved into a finite verb, an ambiguity closed — say so, say which is closer to the original, and say **what the congregation will actually hear**. This is not a translation-quality verdict; it is a note to the preacher about where the pulpit text has already made an interpretive decision on his behalf. Expect the check to find more, and more that matters, when the pulpit text is a dynamic version. Where the two agree, say nothing: silence is the normal case and the check must not generate filler. KJV remains available as the historic witness where it earns its place, and the ancient-versions check runs as before.

**Quote accuracy.** The wording-dependent tools (7 Vocabulary, 8 Translations, 10 Repetition, 11 Quotation/Allusion) are corrupted if the quoted text is wrong. Never reconstruct the passage from memory and present it as verified: use a pasted or otherwise verified text where available; where working from recall, mark the quotation `[unverified — check wording]` and re-check any finding that hangs on exact wording before presenting it.

---

## Hebrew and Greek — the Three-Way Triage

**Governing rule for every OT passage where the Hebrew and the Greek diverge. There is no blanket preference for either.** A divergence is not one kind of thing, and the commonest error is to treat all three of the following as the same finding. **Classify first, then report.**

**1 — Translation loss (not a variant at all).** The Hebrew carries a literary feature no translation into any language can carry: a repeated root, a wordplay, a Leitwort, a count of formulaic occurrences, a pun on a name. The Greek "breaks" it because *translation* breaks it — the English versions break it too.

- *Report as:* a fact about the Hebrew, with a note that the Greek cannot carry it.
- *Do **not** report as:* a reliability judgement, a text-critical finding, or a `**Translation-tradition split:**`.
- **Standing formula for counts.** Where a report gives a count of anything — occurrences, formulae, speeches, compliance-refrains — state or imply **"in the Hebrew"**. A count is a feature of a language, not of a book.
- *Examples:* *tēbâ* (Exod 2:3), shared in the Hebrew Bible only with Noah's ark, rendered θῖβις here but κιβωτός at Gen 6:14; *pānîm* resolved to αὐτός at Exod 33:14, breaking the face/presence hinge.

**2 — Substantive variant (no default; weigh it).** The Greek reflects a different *Vorlage*, recension, or whole edition — a clause absent, a law materially different, a book differently arranged.

- **No presumption in favour of the MT.** The LXX translates a Hebrew text sometimes older than the MT, and Qumran has vindicated it in real places: LXX Jeremiah is roughly an eighth shorter and 4QJer-b supports the shorter Hebrew; 4QSam-a repeatedly sides with the LXX against an MT that has suffered haplography; Deut 32:8's "sons of God" (LXX + 4QDeut-j) now stands in the ESV text against MT's "sons of Israel".
- *Weigh case by case:* external evidence (age, breadth, Qumran); which reading explains the other; whether the difference is the translator's habit or his *Vorlage*; whether the shorter or harder reading is likelier original.
- *Report as:* a variant with both readings, the evidence, a stated position **and a confidence flag** — never a bare preference.
- *Examples:* the LXX's absence of Exod 32:9; the materially different law at Exod 21:22–25; the shorter, differently-ordered LXX Exodus 35–40, where **which edition is prior is genuinely unsettled** and the report should say so rather than resolve it.

**3 — The Greek as the NT's own text (stands regardless).** Where the NT quotes or argues from the Greek, that rendering is a fact about how the NT reads the OT, and it is load-bearing whichever text is prior. **Never set it aside on the ground that the Hebrew is the original.**

- *Examples:* *kappōret* → *hilastērion* → Rom 3:25; *tabnît* → *typos* → Heb 8:5; *qāran* (Exod 34:29) → δεδόξασται, which is what Paul's whole *doxa* argument in 2 Cor 3:7–18 is reading; Hab 2:4 as quoted at Rom 1:17.
- *Report as:* a Tool 11 / biblical-theology finding, cross-referenced from Tool 8 — **not** as a translation error.

**Working default, stated plainly — and the distinction it turns on.** English OTs, the ESV and NASB95 included, translate the Masoretic text. That settles one question and not another.

It settles the **variant** question: because the English version's *Vorlage* is the MT, no rule is needed to make the report's *textual basis* Hebrew rather than Greek. The confessional warrant for privileging the Hebrew (WCF 1.8, "immediately inspired… kept pure in all ages") is a claim about the Hebrew **original** and about providential preservation; it is not a ruling on any particular variant, and the Reformed themselves distinguished the two. **Preserve that distinction: work from the Hebrew, and still weigh the variant on the evidence.**

It settles nothing about the **evidence** question. A translation of the Hebrew is not the Hebrew. Repeated roots, wordplay, a Leitwort, the count of a formula, a name-pun, the *petuchot* — none of these survives into any English version, so a report working from an English text cannot see them and must not claim them. **The report's textual basis is already Hebrew; its evidence is not, until the Hebrew is opened.** That is what Phase 0.2 exists to do.

**Pitfall.** Collapsing all three categories into "the LXX is less reliable." It produces three specific failures: a translation-loss finding dressed up as a text-critical one; a genuine variant decided by default rather than by evidence; and an NT argument quietly undercut because it rests on a Greek reading. **If a report cannot say which of the three categories a divergence belongs to, it has not yet done the work.**

---

## Output Format

Produce the report as a **LibreOffice Writer document (`.odt`)**, formatted to the house style below. Work the content first as Markdown internally (it follows the template below), then render to `.odt` — do **not** deliver the raw Markdown as the final artefact.

**Location by environment:** on claude.ai (Cowork), write the `.odt` to `/mnt/user-data/outputs/` and present via `present_files`; in Claude Code, write to the project's `outputs/` directory (matching `/sermon-creator`'s convention) and report the path.

**House style (LibreOffice-compatible — apply to the `.odt`):**

- **Language:** English (UK) throughout.
- **Page:** A5 portrait; margins — top 15 mm, bottom 10 mm, left/right 10 mm.
- **Document title:** Liberation Serif 18 pt.
- **Body default:** Liberation Serif 12 pt; paragraph line spacing 1.15, space above 0, space below 2 mm.
- **Headings (all levels):** Liberation Serif 14 pt, bold, no line below.
- **Footnotes:** Liberation Serif 10 pt; footnote paragraph indent — before text 0.6 cm, first line −0.6 cm; space above 0 cm, below 0.10 cm; single line spacing.

**Recommended conversion path:** build the Markdown, then convert with a reference document that encodes the house style — `pandoc report.md -o dig-deeper-[slug].odt --reference-doc=house-style.odt`. If no reference document is available, generate the `.odt` directly (LibreOffice `soffice --headless`, or a scripted odfpy/docx build) and apply the settings above. **Before presenting, verify** the delivered file opens in LibreOffice as A5 with Liberation Serif.

The report content follows this template:

````markdown
# Dig Deeper: [Passage Reference — or, in Synoptic Mode, [Passage A] // [Passage B]]

**Primary texts:** [WLC Hebrew / Swete LXX / SBLGNT — name what was actually opened, from `_texts/`]
**Study text:** NASB95
**Pulpit text:** [Declared per engagement — ESV (Anglicised), NIV84, other; or "None — no sermon in view"]
**Date:** [today]
**Book-overview context:** [None / In-conversation / Referenced from prior work]
**Series context:** [If applicable]
**Scope note (Synoptic Mode only):** [The three movements; which passage's frame is supplied by an existing dig rather than re-worked; and **the direction of dependence — stated, open, or contested — with its evidence**.]

---

## The Passage

[Quote the passage in full with verse numbers: the Hebrew or Greek from `_texts/`, then the NASB95 beneath it. Where a pulpit text is declared and differs in a way that bears on a finding, give that wording too.]

[**Synoptic Mode:** present the pair side by side in a two-column table, aligned verse by verse, with identical verses marked as identical and paragraph markers shown where they carry an argument. Quote each passage's frame separately beneath the table, since the frames are usually where the two differ most.]

---

## Headline Findings

[3–5 bullets: highest-conviction, multi-tool-convergent claims. See `preacher-extras.md`.]

---

## The Sixteen Tools

### 1. Author's Purpose

[Findings. Reference book-overview if present.]

### 2. Context

[Open with a `#### Positional Necessity Check` subsection recording the Phase 0.6 answers (what the preceding movement set up that this passage provides; why this passage exists *here*), then the general contextual notes: immediate before/after, section, book.]

### 3. Structure

[Sections with titles. Bookends, sandwiches, chiasm. How sections relate.]

### 4. Linking Words

[Every logical connector with its referent. Arrow notation where helpful.]

### 5. Parallels

[Synonymous, antithetical, chiastic. N/A with reason if not applicable.]

### 6. Narrator's Comment

[Authorial breaks. N/A with reason for non-narrative.]

### 7. Vocabulary

[Big Bible words, familiar-but-redefined, significant names. Include the proper-noun inventory (one line for routine names) and any name-hyperlink findings — canonical history, outstanding words, name-wordplay — cross-reporting load-bearing ones under Tool 11. Confidence flagged.]

### 8. Translations

[Where the NASB95, the declared pulpit text and the KJV diverge meaningfully — note which is closer to the original and why. Bring in a dynamic version only to show what it smooths over.]

**Ancient versions check:** When the modern translations compared above substantively agree on a rendering that carries exegetical weight, check whether the LXX, Vulgate, or Peshitta diverge from them. A split between the ancient and modern traditions is an exegetical finding in its own right — flag it as `**Translation-tradition split:**` with both readings and their preaching implications. Do not mark N/A without having considered the check. **Where the divergence is between the Hebrew and the Greek, classify it first under the Three-Way Triage above** — translation loss, substantive variant, or the NT's own text — and report it in that category's terms; only category 2 is a `**Translation-tradition split:**`. Full procedure and trigger conditions: `references/04-words-and-translations.md` § Ancient versions check.

**Pulpit divergence note:** [Name the declared pulpit text. Where it diverges from the NASB95 in a way that bears on a finding — a connective dropped or supplied, a repeated root levelled into synonyms, an ambiguity closed — say so and say what the congregation will actually hear. Where they agree, state "No divergence bearing on the findings". Where no sermon is in view, state "N/A — no pulpit text declared".]

### 9. Tone and Feel

[Emotional register, devices establishing it. Soundtrack.]

### 10. Repetition

[Repeated words, phrases, ideas.]

### 11. Quotation/Allusion

[For each significant OT citation, apply the OT Citation Triad (see `references/06-canonical-reading.md`):
- *Source context:* what the OT passage is about in its own right
- *Book usage:* whether this OT source has appeared earlier in this book/series and what it did there
- *OT-to-OT:* whether OT texts cited together in this NT passage are already in canonical conversation
- *What it adds:* the full triad's contribution to this passage

Then, for the passage as a whole (required even with zero external citations), record the Move 4 internal echo check: `Internal:` findings with direction (*answers §earlier* / *planted for later*) and confidence, or an explicit one-line nil-return ("Internal: none found; opening material checked").

For moderate-confidence allusions: Move 1 only (matching the Phase 4 significance rule). Confidence flagged throughout.]

### 12. Genre

[Type of literature, reading rules. Brief unless contested.]

### 13. Copycat

[Descriptive vs prescriptive. Character-by-character labelling for narrative. N/A for non-narrative.]

### 14. Bible Timeline

[Where on the timeline. Where the reader is. What's happened between. Note when tool isn't needed (passages about God's character).]

[For OT passages: Tanak position of the book, and one line on what it implies. Note any divergence between canonical and compositional order, with the direction-of-dependence question left open.]

### 15. Who Am I?

[Identification with characters. Christ-as-type vs human-as-example.]

### 16. So What?

[Author's intended response. Behaviour (stop/start), worldview, motivation. Four audiences. Prayer.]

---

## Extensions

### Original Language Observations

[Key Hebrew/Greek terms; grammatical/syntactical features; wordplay; recommendations for verification. Confidence flagged.]

### Textual Variants

[Variants from the catalogue that affect this passage. "No significant variants" if none. For OT passages, every Hebrew/Greek divergence reported here must be classified under the Three-Way Triage — this section carries **category 2 only** (substantive variants, with evidence, position and confidence). Translation loss belongs under Tool 7/8 or Original Language Observations; an NT-load-bearing Greek rendering belongs under Tool 11 or Biblical-Theological Themes.]

### Historical and Cultural Background

[Setting; what the original audience knew; what this changes about how we read.]

### Original Audience Reception

[Who they were; what they brought; surprises/shocks/comforts; what we bring that they didn't; **candidate Fallen Condition Focus** (shared concern — feeds `/point-purpose` them-then carry-forward → `/seven-second-sermon` Phase 1.5).]

### Biblical-Theological Themes

[1–3 major canonical themes the passage participates in.]

### Schnittjer Pass

[Torah passages only (Genesis–Deuteronomy). Run per `references/extensions/schnittjer-pass.md`. For non-Torah passages: **N/A** — not in the Torah.]

### Christological Reading

[For OT: type of connection (prophecy/typology/Christophany/trajectory/contrast); how the passage points to Christ; moralism check. For NT: typology in view, if any.]

### Difficult / Contested Verses

[Issues from the catalogue that touch this passage. May be "None significant" for some passages.]

---

## Convergent Findings

[The full list of places where multiple tools agreed. Different from Headline Findings: this is comprehensive; Headline Findings is the top 3–5.]

---

## Preaching Pitfalls

[2–5 common misreadings of this specific passage with correctives.]

---

## Open Questions / Uncertainties

[Anything flagged as uncertain — especially anything where lexicon/commentary verification would strengthen the work.]

---

## Book-Overview Tensions

[Surface — don't resolve — any places where this exegesis suggests the book-overview should be revisited. "None" if the work agrees throughout.]

---

## Text-First Declaration

**Secondary sources present in context:** [list each — commentary, transcript, prior report, book-overview — or "None"]
**Tools worked before secondary sources consulted:** [Confirmed / exceptions noted honestly]
**Passage text:** [Verified / unverified — wording-dependent findings re-checked]
**Reference files viewed:** [Core 01–07 / extensions viewed / worked example viewed — list any mandatory file *not* viewed, with reason]
**Depth floors:** [Met / any shortfall named]
**Chains verified:** [n chains, n references checked against `_texts/` — or "None claimed" / "Corpus unavailable — all chain claims tagged unverified"]
**Apparatus findings:** [n findings resting on parashoth / accents / ketiv-qere / Masorah — witness named for each, spread checked or tagged — or "None"]
**Warrant counts:** [T] n · [I] n · [S] n

[One-line health note. A report dominated by [S] findings is a reformatting of its sources, not an audit of them — if that's what the counts show, say so and name what needs re-working.]
````

---

## Filename Convention

`dig-deeper-[book]-[chapter]-[verses].odt`

Examples:
- `dig-deeper-ruth-1-1to22.odt`
- `dig-deeper-john-3-16.odt`
- `dig-deeper-romans-8-1to11.odt`

**Two-passage (Synoptic Mode):** `dig-deeper-[topic]-[bookA]-[ch]-[bookB]-[ch].odt` — e.g. `dig-deeper-decalogue-exodus-20-deuteronomy-5.odt`, `dig-deeper-hezekiah-isaiah-36-2kings-18.odt`. Named by what the pair is about, because it belongs to neither book alone.

Lower-case, hyphenated, no spaces.

---

## Quality Markers

A Dig Deeper report is excellent when it:

- **Surfaces what surprises** — including things the preacher didn't know to look for
- **Converges multi-tool evidence** — so the preacher knows which findings to trust most
- **Flags confidence honestly** — uncertain claims are marked uncertain; certain claims aren't hedged needlessly
- **Stays text-first** — every finding traceable to the passage (in Synoptic Mode, to one of the passages or to the comparison), not deduced from elsewhere
- **Adapts depth** — long where the passage warrants, short where it doesn't, N/A with reason where genuinely so
- **Hands off cleanly** — the preacher can take this report straight into `/point-purpose` and have rich material to work with
- **Surfaces difficulties** — flags pastoral, ethical, doctrinal, apologetic issues before the preacher hits them in the pulpit
- **Doesn't moralise** — keeps OT readings Christological; doesn't reduce narrative to "be like X"
- **Surfaces preaching pitfalls** — names the common misreadings before the preacher falls into them
- **Applies the OT Citation Triad fully** — every significant OT citation shows source context (Move 1), book usage (Move 2), and OT-to-OT canonical relationship (Move 3); Move 2 findings have been checked against the Positional Necessity Check; no citation treated as an isolated proof-text; **and Move 4 (internal echo) has been run for the passage as a whole — opening material checked, addressee-differentiation applied where relevant, with either tagged `Internal:` findings or an explicit nil-return**
- **Searches before it checks** — Tool 11's citation work derives candidates independently from the passage's own vocabulary before testing any candidate a secondary source already named; Move 2 is run per distinctive image in image-dense passages, not only at the theme level; where a cross-reference tool is available, it has been pointed at a systematic sweep, not only targeted point-queries
- **Declares its warrant** — the Text-First Declaration shows the report's evidence base ([T]/[I]/[S] counts, sources consulted, quote verification) rather than asserting it; and no setting/authorship/audience/use/label claim is dressed as `[T]` when the text does not state it
- **Keeps the translation work honest** — findings rest on the original languages from `_texts/`, not on an English rendering of them; Tool 8 compares the NASB95 against the declared pulpit text and runs the ancient-versions check, so the preacher is told where the text his congregation hears has already decided something for him
- **Is model-invariant** — the report meets the depth floors, follows the template verbatim, and would sit beside the worked examples without looking thinner, whichever model produced it

---

## Key Principles

- **Text-first.** The passage drives the exegesis. The book-overview is consulted, not obeyed.
- **Author's Purpose is king.** Every other tool serves it. If a finding contradicts the apparent thrust of the book, double-check.
- **Adaptive depth.** Don't pad. Don't skip. Match depth to what each tool surfaces.
- **Confidence flagging.** Mark *high*, *moderate*, *uncertain* on any claim drawing on lexicon, manuscript, or intertextual data Claude isn't fully sure of.
- **N/A is fine, but reasoned.** Every N/A needs a one-line reason.
- **Warrant honesty — the `[T]` boundary.** `[T]` means the text on the page states or shows it. Claims about authorship, date, composition, audience, occasion, cultic use, *Sitz im Leben*, or a traditional label are `[I]`/`[S]`, not `[T]` — however conservative-sounding. Split a mixed-warrant sentence and tag each part; never launder a received description or a form-critical construct (e.g. "Israel's hymnbook") into a text-observation.
- **Pure exegesis.** No TP, no PS, no sermon structure. Hand off to `/point-purpose`.
- **Surface, don't resolve, tensions with the book-overview.** Let the user decide.
- **Originals first; NASB95 as study text; pulpit text declared.** Findings come off the Hebrew or Greek in `_texts/`, quoted alongside the NASB95. The pulpit text varies by engagement — ask when a sermon is in view, never assume — and Tool 8 reports where it and the NASB95 part company. Run the ancient-versions check as well, not instead.
- **British English** throughout the report.
- **Christ-centred for OT.** Use the Christological Reading extension to provide raw material; don't allow moralistic readings of OT narrative.
- **Preacher-useful.** The report exists to help the preacher prepare — Headline Findings at the top, Preaching Pitfalls before Open Questions. Every section should pay for its place.

---

*Revision history (provenance) lives in `references/CHANGELOG.md` — not loaded during execution.*