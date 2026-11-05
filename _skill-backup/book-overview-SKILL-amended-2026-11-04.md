---
name: book-overview
description: "Produce a whole-book orientation document for a book of the Bible — the planning layer that /dig-deeper consumes at its Phase 0.5 and that /point-purpose and /sermon-review lean on. Always trigger when the user says \"book overview\", \"overview of [book]\", \"orient me to [book]\", \"map the whole book\", \"presenting situation\", \"arc map\", \"microscript\", \"intertextual map\", \"preaching traps\", or wants the big picture of a biblical book before working individual passages or planning a series. Also trigger in Finalise/Upgrade mode — revising an existing overview in light of completed dig-deeper runs, a claim audit, or a macro-synthesis (\"update the overview\", \"finalise the overview\", \"the digs found X — fix the overview\"). Complements dig-deeper (downstream passage exegesis) and point-purpose (downstream sermon backbone). Works from the original languages (the _texts/ corpus) as substrate, with NASB95 as the English study text. House output: .md, .odt, .html.\n"
metadata:
  version: "0.1.0"
  author: "Patrick Couch"
---

# Book Overview

Produce a **whole-book orientation document** for a book of the Bible: the planning layer that sits *above* passage-level work. The overview is the substrate `/dig-deeper` front-loads at its Phase 0.5, and the orientation `/point-purpose` and `/sermon-review` assume. Its job is to make every downstream passage dig sharper and faster — never to pre-decide their findings.

This skill produces **orientation, not exegesis**. It does not run the sixteen tools on any passage (that is `/dig-deeper`) and does not produce a Teaching Point or sermon structure (that is `/point-purpose`). It maps the terrain so the detailed work lands well.

**The overview is a planning document, and it is meant to be revised.** It orients the digs; the digs then test and correct it (Finalise/Upgrade mode). An overview treated as fixed truth the digs must conform to has failed. Surface its provisional claims honestly and let the passage work overturn them.

---

## Text-First Discipline

The substrate is the **biblical text in its original language**, never a commentary, study guide, prior overview, or English version. Reach your own conclusions from the book itself — read it cover to cover first — and only then consult secondary sources to confirm, nuance, or resist what you found.

**A translation cannot carry the evidence this document is built from.** A repeated root, a Leitwort, the count of a formula, a name-pun, the paragraph markers — none of them survives into English. An overview assembled from an English text cannot see them and must not claim them. See Phase 0.2.

Tag every non-trivial claim by warrant, exactly as `/dig-deeper` does:

- `[T]` — derivable from the text itself
- `[I]` — a reasonable inference from the text, not stated by it
- `[S]` — supplied by a secondary source, held provisionally until checked

**The `[T]` boundary — do not stamp reconstruction as text.** `[T]` is for what the book *on the page* states or directly shows (a superscription's attribution, a word that is present, a structural seam you can point to). It is **not** for claims about the book's **authorship, date, composition history, audience, occasion, liturgical or cultic use, *Sitz im Leben*, or its traditional title/label** — these are reconstructions or received descriptions, and are `[I]` at best, usually `[S]`, however venerable or conservative-sounding they are. *Sniff test:* could this be known only by someone standing **outside** the text — a historian, a form critic, church tradition? If yes, it is not `[T]`. Beware especially the **imported scholarly construct wearing conservative clothing**: e.g. "the Psalter was Israel's hymnbook" reads like a plain fact but is a Second-Temple, form-critical (Gunkel-Mowinckel) description — `[S]`, not `[T]`, and in tension with a canonical-shape reading. What the text attests (a superscription; a temple-singer guild named in a narrative) and what tradition supplies about the *collection's* use are different warrants and must be tagged apart — **even within a single sentence**. When a claim straddles categories, split it and tag each part rather than averaging to one comfortable tag. This bites hardest in the **Presenting Situation** (author, audience, occasion): tag it honestly.

**Self-check before writing:** *Could this overview have been written by someone who read a commentary but never read the book?* If yes, re-work it from the text. An overview dominated by `[S]` is a reformatting of its sources, not an orientation to the book.

---

## Required Input

| Required | Notes |
|----------|-------|
| **Book reference** | E.g. "Philippians", "Ruth", "Jonah". A portion ("Philippians 1–2") is acceptable but flag the overview as partial. |

If the book is not given, ask.

## Optional Inputs (auto-detect from conversation)

| If present | How to use it |
|------------|---------------|
| Completed `/dig-deeper` reports on the book's passages | **Finalise/Upgrade mode** — harvest their Convergent Findings, Book-Overview Tensions, internal echoes, and Christological readings to correct and enrich the draft. |
| A `/dig-deeper` claim audit (`dig-deeper-[book]-claim-audit.md`) | Treat its verdicts as settled checking-stage input; do not re-derive. |
| A macro-synthesis (`[book]-dig-deeper-macro-synthesis.md`) | Fold its cross-pericope macro-arguments into the arc map and Christological trajectory. |
| A series brief / sermon calendar | Shape the preaching-units section around it. |

---

## Mode Selection (choose first)

- **Draft mode (default)** — build the overview fresh from the book's text. Use when no dig-deeper runs exist yet, or when starting series planning from scratch.
- **Finalise/Upgrade mode** — revise an existing overview (or build a definitive one) using completed dig-deeper runs, a claim audit, or a macro-synthesis. Use when the sweep is done and the overview should now reflect what the passages actually demonstrated.

State the mode in the report header. In Finalise mode, work the text-derived draft *first*, then reconcile against the runs — do not simply transcribe the runs.

---

## The Deliverable Contract

Every overview must produce these seven threads. They are the contract `/dig-deeper` depends on — its Phase 0.5 extracts the starred four directly, and Moves 2 and 4 are fuelled by the intertextual map and the echo table. Full specifications and formats: **`references/deliverables.md`**.

1. **Presenting situation** ★ — author, audience, occasion, and the concrete pressure the book answers.
2. **Structural arc map** — the book's movements (aim for 3–7), the device binding them (linear, bookends, chiasm, panels), and each movement's function.
3. **Microscript** — the book's whole argument or storyline compressed to 1–3 sentences; the spine everything hangs on.
4. **Intertextual map** ★ — the OT (or earlier) sources the book draws on, *where* each is used, what each use does, and which are **live sources** (used two or more times). This is the fuel for dig-deeper's Tool 11 Move 2; build it by systematic sweep, not memory.
5. **Christological trajectory** ★ — how the book points to Christ (prophecy / type / trajectory / contrast), and the moralism trap to avoid.
6. **Preaching traps** ★ — book-level misreadings with their likely passage-level manifestations.
7. **Early↔late echo table** — internal anticipations and resolutions (a boast answered, a question resolved, an image replanted). This is the fuel for dig-deeper's Move 4; hold the opening chapters open against the whole book.
8. **Canonical position** ★ — where the book stands in the Tanak, as five fields, with *Presupposes* carrying checked references. `dig-deeper` extracts this at Phase 0.5 rather than re-deriving it at 0.55.

Two supporting sections complete the document:

- **Preaching units** — a proposed pericope division for a series, each weighted **⭐ HIGH** (needs a full solo dig before the pulpit) or **Standard**.
- **Colophon / provenance** — version, date, mode, sources consulted, and warrant counts, so later Upgrade passes can see what has changed.

---

## Workflow

Work in this order. Follow the phases literally; if one does not apply, say so in a line rather than omitting it.

| Phase | What you do |
|-------|-------------|
| 0 | **Choose the mode** (Draft / Finalise). Note any dig-deeper runs, claim audit, or macro-synthesis in conversation. |
| **0.2** | **Load the substrate.** Locate `_texts/` in the connected prep folder and read its README before using it. Take the book from the corpus — Hebrew from `hebrew-wlc/`, Greek OT from `greek-lxx-swete/`, Greek NT from `greek-nt-sblgnt/` — not from memory and not from a search. Every count, chain and repetition claim in the overview is made against the corpus and **names its edition** (WLC, Swete, SBLGNT), because a count is edition-specific. Where a finding turns on a particular reading rather than on the wording generally — a variant, an apparatus question, a Rahlfs-vs-Swete divergence, an NA28 decision — the corpus is not enough: go to Logos and cite that; the user's own exports are in `_texts/logos-exports/`. **Do not ask a search engine what a verse says.** And know what the corpus cannot show you: it holds **one** Hebrew manuscript tradition, so it can verify wording, counts and chains, and can never report how widely an *apparatus* feature is attested. **If the corpus is unreachable, say so in the colophon before proceeding rather than falling back silently** — and an overview that never saw the original language may not report a count, a repetition, or a Leitwort as `[T]`. |
| 1 | **Read the whole book in its original language first, then in the NASB95**, ideally in one sitting each. Identify the genre. Note first impressions of situation, repeated words and structure before analysing — **the repeated-words observation is made in the original, because it cannot be made in a translation.** |
| 2 | **Detective pass — presenting situation.** Who writes/narrates, to whom, when, why? What pressure does the book answer? Text-first; tag warrants. **Author, date, audience, occasion, and any traditional title/label (e.g. "Israel's hymnbook") are `[I]`/`[S]`, not `[T]`, unless the book states them on the page — split mixed-warrant sentences and tag each part (the `[T]` boundary).** |
| 2a | **Fix the canonical position.** State where the book stands in the Tanak — Torah, Nevi'im (Former or Latter), or Ketuvim — in the BHS order, as the five fields in `references/deliverables.md` § 8. Ruth stands among the Megilloth, not after Judges; Daniel is in the Writings; Chronicles closes the canon. Where canonical and compositional order diverge, report both and resolve neither. For NT books give the equivalent: position in the collection, what it presupposes, what it hands on. |
| 3 | **Map the arc.** Strip chapter/verse marks; find the real seams (repeated phrases, scene/voice changes, argument stages). Name 3–7 movements and the binding device. |
| 4 | **Distil the microscript.** One to three sentences capturing the whole. Test it against every movement — if a movement does not serve it, the microscript is wrong. |
| 5 | **Build the intertextual map.** Sweep the book for quotations, distinctive verbal echoes, and conceptual/name/number allusions. Record source → location(s) → what each use does. Mark live sources (≥2 uses). Note explicitly when the book is OT-citation-light and carried mainly by internal repetition (a finding dig-deeper needs). **Then run the density scan** — `python3 _texts/tools/contacts.py scan <Book>`, and once per major block (`<Book>:1-2`) — which ranks every chapter of the Hebrew Bible by rare shared vocabulary with the book. **Every chapter in the top ten must be accounted for:** either it enters the map, or the map says in one line why it does not (common subject matter, a list, a genealogy). A map that has been swept only for what the drafter already knew to look for will miss its densest partner — the Lamentations overview of 3 October 2026 omitted Jeremiah 14, which the scan ranks first of 858 chapters. **Run the scan a second time with the chapter floor lowered to five verses (`--min 5`), and account for any chapter that enters the top ten only there.** The default floor of ten verses excludes short chapters by construction: Obadiah's second-densest partner, Joel 3, has five verses. Density is noisy at that size, so read the matched words before the row enters the map. **A rare-pair scan also works verse against verse and divides by chapter length, so it understates a tight cluster spread over adjoining verses.** After the scan, score five-verse windows across the canon on the book's rarer words: Num 24:17–21 against Obadiah ranks 66th of 922 chapters but 13th of about 19,500 windows by raw count (95th by rarity-weighted count, so quote the measure with the rank). **Exclusive sets drawn from scattered verses of the book are candidates, not evidence.** In the Obadiah audit, 14.2 % of the verses of the Hebrew Bible held a three-word set from Obadiah's vocabulary found in no other verse, and three claims built that way (Gen 27:41, Deut 32:35, Prov 27:10) came down. A contact needs shape: an ordered phrase, a shared construction, or a tight cluster in the source. *(Added 4 November 2026.)* **For NT books, run the New Testament mode against Swete's LXX:** `python3 _texts/tools/contacts.py ntscan <Book>` — and once per major block (`<Book>:1-2`) — with the book label as the SBLGNT index has it (`Col`, `1Cor`, `Heb`). It gives six runs (whole chapters, 8-verse and 16-verse windows; all words and rarer words) and a stability table. **Account for every chapter in the top ten of the stability table**, quote a partner's rank only where it holds across the runs, and run `--check "<chapter>"` on every partner the map names, reading the matched words for sense (Phase 10.5 (a)). Where a row rests on the LXX wording, cite it from the Rahlfs export in `logos-exports/`, not from Swete. *(NT mode added 19 October 2026; positive controls: Heb 1:1–14 ranks Ps 44 LXX first, Col 1:15–20 ranks Ps 88 LXX first in all six runs.)* |
| 6 | **Trace the Christological trajectory.** For OT books, run the type/trajectory/contrast categories; always include the moralism check. For NT books, name how Christ is the ground and pattern. |
| 7 | **Name the preaching traps.** Book-level misreadings, cliché sermons, tribe blind spots, pastoral landmines — each with its likely passage-level form. |
| 8 | **Build the early↔late echo table.** Hold the opening unit(s) open against the whole book; apply addressee-differentiation where the book opens by naming distinct parties. |
| 9 | **Propose preaching units** with HIGH/Standard weightings. |
| 10 | **Checking stage.** *Only now* consult commentaries or, in Finalise mode, the dig-deeper runs / claim audit / macro-synthesis. Reconcile: confirm, nuance, or resist the text-first draft; re-tag warrants honestly ([S] for anything that originated in a source). Surface — do not silently absorb — tensions between the draft and the runs. |
| 10.5 | **Pre-output gate — a gate, not a review.** Fix any failure before writing the file. **(a) Every claim that a word, root or formula recurs across two or more places is verified against the corpus lemma index — by lemma, never by pointed surface form or English gloss — and each claimed reference confirmed to contain it.** Where a phrase search is unavoidable, normalise maqqef, paseq and sof pasuq to spaces as well as NFD-stripping combining marks; run a second *skeletal* pass with waw, yod and word-final *he* deleted, since a defective spelling drops a verse silently and an undercount is indistinguishable from a count; and **treat any unpointed word in the window as a ketiv the pattern cannot match — confirm the chain by lemma before trusting the result.** About one verse in twenty of the Hebrew Bible carries an unpointed form, and in the densest books about one in five (Daniel 22.4 %, Ezra 10.4 %); the ketiv at Neh 9:17, וְרַב־וחסד, hid that verse's citation of Exod 34:6 from a whole-Bible search that was otherwise correctly normalised. **Chains are checked with `_texts/tools/find.py`** (`lemma` to list, `verify` to gate, which exits non-zero on a failed reference); a bespoke matcher is validated against it on a known-positive lemma before its output is used, since the lemma field's homograph suffixes (`2617 a`, `6965 b`) make a naive equality test return a silent zero. **And a nil or surprisingly short return is never reported as an absence until a positive control has passed** — run the identical search against one reference the item is *known* to contain and see it returned; if the control fails the search is broken, not the text. **The two faults likeliest to survive every other check are a tool whose answer goes to a channel the script is not reading, and a scan that counts the corpus's own markup — the bare ס and פ paragraph markers — as text.** **In the Greek OT the fault runs the other way.** Swete has no lemma index, so its counts are made on word-beginnings, and a stem can credit a *different* word — καταλλαγή ("exchange", Isa 9:5) under καταλλάσσω ("to reconcile"), εἴκοσι ("twenty") under εἰκών ("image"), ὁρᾶτε ("see!") under ὁρατός ("visible"). That is a false positive, which no positive control catches. **Read the word behind every stem hit before it is counted** (the scan tool's sense-check listing prints them); drop a hit in another sense, and name a cognate in another sense as such. *(Added 19 October 2026.)* *(Positive control adopted on trial, Round 5; two cause-classes added Round 6.)* A reference that fails is removed from the chain or the chain restated — never hedged and left standing. **A row that cites a lemma at several verses is verified at each verse separately, never as a set:** the Lamentations overview cited פְּרִי ("fruit") at 2:20 and 4:10 when it stands at 2:20 only. **And the words *identical*, *verbatim*, *the same phrase* and *only* are claims about shape, which a lemma check cannot verify.** They are licensed only by an *ordered* phrase search, run plain and skeletal (`contacts.py phrase "<words>"`). Where the lemmas match but the phrase does not, the row says *reordered* or *partial*. Where two words share a root but not a lemma (מְרוֹרִים against מַמְּרֹרִים, "bitterness"), the row says *cognate*. Ps 143:3 is not "identical" to Lam 3:6: its first two words are reversed. (b) Every count names its edition. (c) Every finding resting on a feature of the **apparatus** rather than the wording — *parashoth*, accentuation, ketiv/qere, Masorah — names its witness rather than the tradition ("as BHS prints it", never "the Masoretic text" unqualified), and says where the feature is a reading tradition rather than authorial. (d) Every allusion in the intertextual map and every row of the echo table carries a confidence flag. (e) Where the corpus was unavailable, every chain claim is tagged `[unverified — chain not checked]`, capped at moderate confidence, and **may not be handed to a dig as though it were established**. **(f) Every allusion rated above *moderate* carries a rarity count and a rival search.** Count how many verses of the Hebrew Bible contain its shared lemma set (`contacts.py all <lemmas>`; `--window 1` for a pair that straddles two verses), and name every text that shares the set as closely as the claimed source, or more closely. The row states the count ("two verses in the Hebrew Bible", "nine verses") and names the rivals. **An allusion whose wording occurs in more than about ten verses is idiom, and may not be rated above *moderate* on wording alone.** An allusion with an equal or closer rival is rated against the rival, not in isolation. **(g) A design claim is capped at *moderate* until a chance baseline has been run, and a superlative is barred unless it was measured.** A design claim is any claim about a *pattern* rather than a reference: a "live source", a structure (chiasm, concentric frame, panels, inclusio built from vocabulary), a "handoff", a programme of allusion. The baseline asks whether the pattern occurs more often than it would by chance: for example, by comparing the claimed pairing of two sections against every other pairing; by reshuffling verses into pseudo-sections of the same size; or by ranking the claimed partner against every chapter or window of comparable size (`contacts.py scan`). **Superlatives** — *the densest*, *the closest*, *every one*, *the only*, *anywhere in the canon* — state a measurement. They may be used only when the measurement was made, and the row gives it ("first of 858 chapters"). A design claim that has not been baselined is stated as a proposal, tagged `[I]`, and named in the colophon as a first target for the claim audit. In the Lamentations audit, all seven design claims needed reframing while every exclusive single link held. **(h) Every search is stated in words** — the original-language words in their own script with a gloss, the edition and the result — with no search command, routine or script name, word-index number or parameter symbol anywhere in the overview (the rule of `dig-deeper` gate item (j)). Record the results in the colophon. **This is where the overview's highest-risk claims are made:** the intertextual map and the echo table are cross-passage chains built at speed across a whole book, and this project's audits agree across three books that such synthetic claims fail at a much higher rate than passage-level ones. An unverified chain in an overview is not a local defect — it is a defect with a delivery mechanism. |
| 11 | **Write the report and render three formats** (.md, .odt house style, .html two-pane house style). See Output Format. |
| 12 | **Present** the files (`present_files` in Cowork; report the path in Claude Code). |

---

## Original languages — script and gloss

**Give the original word in its own script, with an English gloss in brackets immediately after — every occurrence, not only the first.** חֶסֶד ("covenant-kindness"), גֹּאֵל ("kinsman-redeemer"), κοινωνία ("partnership"), φρονέω ("to think, to be minded").

The gloss is the NASB95 rendering where the word is being discussed as it stands in a particular verse, and a lexical gloss where it is being discussed as a word.

**Transliteration is kept only where the sound is the point** — paronomasia, assonance, a name-pun — and then give all three: נְחֹשڶׁת ("bronze", *nĕḥōšet*) against נָחָשׁ ("serpent", *nāḥāš*). An overview that transliterates by default makes the reader's Hebrew harder to learn, not easier.

The `.odt` and `.html` converters render both scripts correctly and set Hebrew three points above the surrounding English; nothing special is needed in the Markdown.

---

## Consistency Contract

This skill must produce overviews of the same shape and discipline whatever model runs it.

1. Follow the phase table in order; do not merge or silently skip phases.
2. Produce all seven deliverable threads plus preaching units and colophon — every time, even when a thread ends up brief (state "sparse" with a reason rather than omitting).
3. Keep it text-first **and original-language-first**: reach findings from the book, in its own language, before opening any source; warrant-tag throughout; run the Phase 10.5 gate before writing.
4. Match the worked examples in `examples/` for depth, register, and flagging density — `philippians-worked.md` (NT epistle) and `ruth-worked.md` (OT narrative) are the calibration anchors.
5. Build the intertextual map by systematic sweep, not recall; flag confidence on every allusion (*high / moderate / uncertain*).
6. Never let a secondary source or a dig-deeper run become the substrate; the overview reports the book, checked against sources — not the sources reformatted.
7. Where a judgement is genuinely contested (a structural seam, a disputed occasion), show the options and flag confidence rather than asserting one.
8. **Never state a pattern, a superlative or a "live source" more confidently than its baseline allows** (Phase 10.5 (f)–(g)). Single exclusive links are where an overview is reliable; synthetic claims are where it is not, and the colophon names them as the claim audit's first targets.

---

## Output Format

Produce the overview as **three files in the house style**, matching the wider toolkit:

1. **`.md`** — the working document (template in `references/deliverables.md`).
2. **`.odt`** — LibreOffice, A5 portrait, Liberation Serif, margins top 15 mm / bottom 10 mm / sides 10 mm; body 12 pt (line 1.15, space below 2 mm); title 18 pt; headings 14 pt bold; footnotes 10 pt. English (UK).
3. **`.html`** — the two-pane reading layout (sticky Contents sidebar + main column), sidebar built from the H1 title plus every H2, `lang="en-GB"`, generated from the `.md`.

**Filename convention:** `book-overview-[book].{md,odt,html}` (lower-case, hyphenated) — e.g. `book-overview-philippians.odt`, `book-overview-ruth.html`.

Build both rendered formats with the canonical house converters in the connected prep folder — `_house-style/make_odt.py` and `_house-style/make_html.py`. They apply the house style, declare the house font as an ODF font face (without which LibreOffice silently renders Hebrew in its default complex-script font), set the complex-script size three points above the western size, normalise bare `---` rules so pandoc cannot swallow a section, and refuse to write a file that has lost a section.

Work the content first as Markdown; render only once the content is complete. Before presenting, verify the `.odt` opens as A5 with Liberation Serif, that any Hebrew is in that face rather than a fallback, and that every `.html` nav anchor resolves.

---

## Interfaces to the Rest of the Toolkit

- **→ `/dig-deeper` (Phase 0.5):** the four starred threads (presenting situation, intertextual map, Christological trajectory, preaching traps) are extracted and held in peripheral vision; the intertextual map feeds Move 2, the echo table feeds Move 4.
- **→ `/point-purpose`:** the microscript and Christological trajectory orient the Teaching Point and Purpose Statement; the preaching units set series scope.
- **← from the sweep (Finalise/Upgrade):** completed dig-deeper runs, a claim audit, and a macro-synthesis flow *back* to correct and finalise the overview.

Full interface detail, the Finalise/Upgrade procedure, and the colophon/provenance convention: **`references/modes-and-interfaces.md`**.

---

## Key Principles

- **The book drives the overview; sources are consulted, not obeyed.**
- **Orientation, not exegesis or sermon.** Map the terrain; hand the detail to dig-deeper and point-purpose.
- **The intertextual map and echo table are the load-bearing outputs** — they are what make downstream Moves 2 and 4 possible. Do them by sweep, not memory.
- **Adaptive depth.** Rich where the book warrants; brief-with-reason where a thread is sparse; never omit a thread.
- **Confidence flagging and warrant tags throughout.**
- **The `[T]` boundary.** `[T]` means the book states or shows it. Authorship, date, audience, occasion, cultic use, *Sitz im Leben*, and traditional labels are `[I]`/`[S]`, not `[T]` — however conservative-sounding; never launder a received description or a form-critical construct (e.g. "Israel's hymnbook") into a text-observation.
- **Christ-centred for OT books;** run the moralism check.
- **British English.** The substrate is the original language from `_texts/`; the **NASB95** (1995 edition, not the 2020 revision) is the English study text, quoted alongside it.
- **No pulpit text.** A book overview has no sermon in view, and a pulpit text is a fact about an engagement rather than about a book — do not invent one. The header field reads "N/A — no sermon in view". Proposing preaching units is a plan, not an engagement.
- **Originals in their own script, with the English in brackets** — every occurrence; transliteration only where the sound is the point.
- **The chain gate is not optional.** The intertextual map and the echo table are this document's highest-risk claims, and they are handed downstream as though settled.
- **Built to be revised.** Draft orients the digs; the digs finalise the overview.
