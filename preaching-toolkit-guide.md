# The Preaching Toolkit: Workflow Quick Reference

**Four skills, one system:** `book-overview` · `dig-deeper` · `point-purpose` · `sermon-review`
**Substrate:** the original languages, from `_texts/` · **Study text:** NASB95 (1995, not the 2020 revision) · **Pulpit text:** declared per engagement
**House output:** `.md` (canonical) · `.odt` · `.html`

*Rewritten 13 September 2026, at the close of the September process review. The version it replaces dated from 23 July and predated the whole of it.*

---

## The order at a glance

Book overview → make it visible to the project → book sweep → solo passage digs → finalise the overview → point-purpose → sermon-review.

The overview is **first in and last out**: it orients everything downstream, and the completed passage work flows back to finalise it. Treat it as a planning document to be *tested*, not fixed truth.

---

## Before anything: the substrate

Every run — overview, sweep, dig, claim audit — begins from the primary texts, never from an English version.

| Layer | What it is | Right for | Not for |
|---|---|---|---|
| `_texts/hebrew-wlc/` | Westminster Leningrad Codex | Reading, counting, roots, Leitwort work | Citing *BHS* as such |
| `_texts/greek-lxx-swete/` | Swete's LXX | Reading and searching the Greek OT | Citing *Rahlfs* |
| `_texts/greek-nt-sblgnt/` | SBLGNT with parsing | Reading, counting, lemma work in the NT | Citing *NA28* |
| `_texts/logos-exports/` | Your own exports, filed book-first | **Citation of record** where a reading is load-bearing | Whole-canon searching |

**Observe versus cite.** The first three are *proxies*: right for finding, counting and checking; wrong for citing where a finding turns on a particular reading. A variant, an apparatus question, a Rahlfs-vs-Swete divergence, an NA28 decision — those go to Logos, and the finding cites that.

Three rules that follow, and they are not negotiable:

- **Every count and chain names its edition.** A count is edition-specific; "seven times" without "in the WLC" is not a finding.
- **Do not ask a search engine what a verse says.**
- **If the corpus is unreachable, say so before proceeding** rather than falling back silently.

Read `_texts/README.md` at the start. It states what each layer is and, more usefully, what each is *not*.

---

## Step by step

**1. Book overview (its own skill).** Run first, before any passage work. Produces the **canonical position** (Tanak section, reading implication, presupposes, handoff, neighbours), presenting situation, arc map, microscript, intertextual map, Christological trajectory, preaching traps, an early↔late echo table, and a weighted series plan.

> "Give me a book overview of Philippians."

**2. Make it visible to the project.** For the downstream skills to *use* the overview automatically, it must be somewhere they can see it — a connected folder or the same conversation. A skill cannot consume an overview it cannot see. The same is true of `_texts/`: if the folder is not connected, the corpus is not loaded, and the run must say so.

**3. Book sweep (a dig-deeper mode).** A lighter, proportional-depth pass across the whole book — for auditing the overview and seeing the cross-passage network. This is planning, not pulpit prep. **A sweep's book-level claims are provisional until audited**, because proportional depth cuts the checking first.

> "Using the Philippians book overview, run a dig-deeper sweep across the whole book."

**4. Solo passage digs.** For each passage you will preach — especially the ⭐ HIGH ones the overview flagged — run a full solo dig. `dig-deeper` has four modes and chooses first:

| Mode | When |
|---|---|
| **Fresh Exegesis** | The default: a full report on one passage |
| **Claim Audit** | "Is this overview / commentary / article right?" |
| **Macro-Synthesis** | "What do all these runs add up to?" — needs a finished sweep |
| **Synoptic** | The passage is told twice in the canon and the differences are part of the question |

> "Dig deeper into Philippians 2:1–11, using the book overview."
> "Dig deeper into Isaiah 36–39 // 2 Kings 18–20." *(synoptic)*

**5. Finalise the overview (the loop closes).** Feed the completed runs back so the overview reflects what the passages actually demonstrated. Optionally ask for the cross-pericope synthesis.

> "Finalise the Philippians book overview using the completed digs."
> "Pull the threads together — give me a macro-synthesis of the Philippians digs."

**6. Per sermon: point-purpose, then sermon-review.**

> "Turn the dig-deeper report on Philippians 2:1–11 into a sermon backbone." *(point-purpose)*
> "Here's my sermon draft — review it and produce a final manuscript." *(sermon-review)*

---

## The gates

Each stage refuses to ship work that fails its own checks. Knowing what they are tells you what a run is protecting you from — and what to ask for if it goes quiet.

| Gate | Where | What it refuses |
|---|---|---|
| **Chain verification** | overview Phase 10.5 · dig Phase 10.5 (e3) | A claim that a word recurs across verses, unverified by lemma. A failing reference is *removed*, never hedged |
| **Apparatus spread** | dig (e4) | A finding resting on *parashoth*, accents, ketiv/qere or Masorah that names "the Masoretic text" rather than its witness |
| **The OT Citation Triad** | dig Tool 11 | A citation treated as a proof-text, without source context, book usage and OT-to-OT |
| **Anti-moralism** | point-purpose Phase 8 | A Teaching Point whose payoff is "be like X" |
| **Pulpit-text check** | point-purpose 8.5 · sermon-review criterion 10 | A point resting on wording the congregation's version does not carry |
| **Section count** | both converters | An `.odt` or `.html` that has silently lost a section to a stray `---` |

**The chain gate is the one to understand.** A *passage-level* claim rests on one verified stretch of text. A *synthetic* claim — a chain, an arc, a count across a book — is assembled across passages, and this project's audits agree across three books that synthetic claims fail at a much higher rate. The intertextual map and the echo table in a book overview are exactly that: synthetic claims, built at speed, and then handed downstream as settled input. An unverified chain in an overview is not a local defect; it is a defect with a delivery mechanism.

---

## Two texts, and which is which

| | What it is | Who declares it |
|---|---|---|
| **Study text** | NASB95 — the 1995 edition, not the 2020 revision | Fixed. Quoted as the English reference alongside the original |
| **Pulpit text** | The version the congregation will hear — ESV (Anglicised) at your own church, NIV84 or another elsewhere | **Declared per engagement. Asked for, never assumed.** |

A **book overview has no pulpit text** — no sermon is in view, and one should not be invented; the field reads "N/A". A **dig** has one only if a sermon is in view. **point-purpose and sermon-review always have one**, and both now check it: where the pulpit text and the NASB95 diverge in a way that bears on a finding, the run says so and says what the congregation will actually hear. That gap is a note to the preacher, not a verdict on a translation.

---

## Hebrew and Greek in the documents

**Script first, English gloss in brackets, every occurrence** — חֶסֶד ("lovingkindness"), λόγος ("word"), φρονέω ("to think, to be minded"). Not transliteration, and not "first occurrence only".

**Transliteration is kept only where the sound is the argument** — paronomasia, assonance, alliteration, a name-pun — and then all three are given: נְחֹשֶׁת ("bronze", *nĕḥōšet*) against נָחָשׁ ("serpent", *nāḥāš*).

**A sermon manuscript inverts the order, and only a manuscript does.** Those pages are read aloud, so the English leads and the original follows in brackets: *"not visit, not pass through, but settle down and stay (שָׁכַן)."* Never put an original-language word where the preacher must read it aloud to complete the sentence.

Hebrew is set three points above the surrounding English in every house format. The converters handle it; nothing special is needed in the Markdown.

---

## It's a loop, not a line

```
book-overview ──Phase 0.5──► dig-deeper ──findings──► point-purpose ──► sermon-review
      ▲                           │                        │                 │
      └────── runs feed back ──────┘        pulpit text ────┴─────────────────┘
              (Finalise / macro-synthesis)
```

The first pass of the overview is a Draft, written to be corrected. Each dig tests it; the finalise pass rewrites it with what the sweep proved. The pulpit text enters at the sermon end and is checked twice on the way to the pulpit.

---

## Where to keep the files

Keep everything for a book **together in one folder per book**, inside a single prep folder connected to the project. This is what makes the loop automatic: dig-deeper picks up the overview at Phase 0.5, reconciles each passage against its *neighbouring* reports (especially the opening chapter) at its checking stage, and the finalise/macro-synthesis passes read the whole set.

**Keep the `.md` as the canonical copy.** The skills read and generate from Markdown; the `.odt` and `.html` are derived views and can be regenerated at any time.

```
dig-deeper/
├── README.md
├── preaching-toolkit-guide.md          this file
├── _texts/                             THE SUBSTRATE — read its README first
│   ├── hebrew-wlc/  greek-lxx-swete/  greek-nt-sblgnt/
│   ├── logos-exports/                  your exports, filed book-first in Tanak order
│   └── tools/find.py                   lemma search and chain verification
├── _house-style/
│   ├── make_odt.py                     canonical .odt converter (versioned)
│   ├── make_html.py                    the two-pane reading layout
│   └── bundle_converter.py             stamps and checks bundled copies
├── _audit/                             claim-extraction checkpoints
├── Philippians/
│   ├── book-overview-philippians.md
│   ├── dig-deeper-philippians-sweep.md
│   ├── dig-deeper-philippians-2-1to11.md
│   └── philippians-dig-deeper-macro-synthesis.md    (if produced)
├── Isaiah/
│   ├── book-overview-isaiah.md
│   └── dig-deeper-hezekiah-isaiah-36-2kings-18.md   two-passage report, hosted here
├── Kings/
│   └── dig-deeper-hezekiah-pointer.md               one line: where the real file lives
└── The Twelve/
    └── Habakkuk/ …
```

Per-book folders matter because the skills reconcile a passage against its *neighbours*. Folder case doesn't matter to the skills; co-location does.

**A two-passage report is filed once.** Where both books share a parent (Exodus // Deuteronomy under `Torah/`), it goes at the level above both. Where they share no parent — which is most pairs — the real file goes in **one** book's folder, chosen by where the *unique* material sits, with a one-line pointer page in the other's. Never two copies: they drift, and the index lists the report twice.

**Source texts are not reports.** They live in `_texts/logos-exports/`, filed book-first in the Tanak sections and named `NN-Book-VERSION.txt` — the convention is in `_texts/README.md`, not here.

---

## Filename conventions

Use these exact patterns (lower-case, hyphenated) so the skills recognise related files as a set:

| Output | Filename pattern | Example |
|--------|------------------|---------|
| Book overview | `book-overview-[book].md` | `book-overview-ruth.md` |
| Passage dig | `dig-deeper-[book]-[chapter]-[verses].md` | `dig-deeper-philippians-4-1to9.md` |
| **Two-passage dig (Synoptic)** | `dig-deeper-[topic]-[bookA]-[ch]-[bookB]-[ch].md` | `dig-deeper-hezekiah-isaiah-36-2kings-18.md` |
| Book sweep | `dig-deeper-[book]-sweep.md` | `dig-deeper-philippians-sweep.md` |
| Claim audit | `dig-deeper-[book]-claim-audit.md` | `dig-deeper-jonah-claim-audit.md` |
| Macro-synthesis | `[book]-dig-deeper-macro-synthesis.md` | `ruth-dig-deeper-macro-synthesis.md` |
| Sermon plan | `point-purpose-[book]-[chapter]-[verses].odt` | `point-purpose-john-6.odt` |
| **Library-wide audit** | `dig-deeper-[scope]-audit.md`, at the root | `dig-deeper-ot-chain-audit.md` |

Verse ranges use `to` (e.g. `4-1to9`); single verses drop the range (e.g. `dig-deeper-john-3-16.md`). A two-passage report is named by what the pair is *about*, because it belongs to neither book alone — and the name stays the same wherever it is hosted.

---

## Rendering

Build both derived formats with the canonical converters in `_house-style/`:

```
python3 _house-style/make_odt.py  report.md report.odt
python3 _house-style/make_html.py report.md report.html
```

They apply the A5 / Liberation Serif house style, declare the house font as an ODF font face (without which LibreOffice silently renders Hebrew in its default complex-script font), set Hebrew three points above the western size, normalise bare `---` rules so pandoc cannot swallow a section as YAML metadata, and **refuse to write a file that has lost a section**.

**One converter, not several.** A skill that cannot rely on the prep folder being connected takes a hash-stamped copy produced by `bundle_converter.py`, never a hand-maintained one. `--check` reports the two ways a copy goes wrong: *edited by hand* (its body no longer matches its own stamp) and *stale* (the canonical file moved on). Two converters existed once in this toolkit, and they diverged silently.

---

*Keep this guide in the prep folder as a reminder of the sequence. When in doubt: the corpus first, overview before passages, every chain verified, and the overview finalised last.*
