# The Preaching Toolkit — skill amendments, Round 4

**Date:** 13 September 2026 · **Status: partly applied — see *As applied* at the foot.**
**Scope: four skills, not one** — `book-overview`, `dig-deeper`, `point-purpose`, `sermon-review`.
**Lettering.** Round 1 used A–E (F1–F7 for consequential edits); Round 2, G–J; Round 3, K–N. Round 4 continues at **O**.

**Why the name changed.** Rounds 1–3 were filed as `dig-deeper-skill-amendments*.md` because they amended one skill. This round amends the toolkit, so the name says so. It continues the same series.

---

## The finding this round rests on

The September review has upgraded **one skill of four**. The other three have not been opened, and they now contradict both `dig-deeper` and the project instructions. Measured, not remembered:

| Skill | Last modified | What it still says |
|---|---|---|
| `dig-deeper` | 12 Sep 2026 | current through Round 3 |
| `book-overview` | **31 Jul 2026** | *"Read the whole book in ESV"* · *"British English; ESV default"* · no `_texts/`, no corpus, no NASB95, no pulpit-text variable, no Tanak order, no chain gate |
| `point-purpose` | 2 Sep 2026 | *"Default translation: ESV"* · *"British English; ESV default"* |
| `sermon-review` | 2 Sep 2026 | *"Usually the English Standard Version"* · **A4 page, Georgia 13 pt, 1.5 spacing**, built with the `docx` npm library and delivered as `.docx` |

`book-overview` is the one that matters most, and not because it is the most wrong. It is **step 1**: its output is what `dig-deeper` front-loads at Phase 0.5 as the thread-set orienting every tool. An overview built by reading the book in English — no Hebrew opened, no count made against the corpus, Christian canonical order — enters a corpus-disciplined dig as a secondary source. The dig will then note agreement with it, and **that agreement will look like confirmation**. It is the project's own named failure mode, one level up: *a process that re-reads a source can only agree with it.*

### The measurement that decides how this round is applied

The gloss convention (Amendment S below) cannot be installed by editing `SKILL.md` files. Both skills' Consistency Contracts instruct a run to **match the worked example** for depth, register and flagging density. So the examples are the operative instruction. They were counted:

| Worked example | Hebrew characters | Greek characters | Transliteration marks |
|---|---|---|---|
| `dig-deeper/examples/psalm-33-worked.md` | **0** | 0 | 49 |
| `dig-deeper/examples/romans-8-31to39-worked.md` | **0** | 35 | 22 |
| `book-overview/examples/ruth-worked.md` | **0** | 0 | 19 |
| `book-overview/examples/philippians-worked.md` | **0** | 0 | 12 |

**Not one Hebrew character in any of the four.** Psalm 33 and Ruth are the OT anchors, and both teach transliteration exclusively. A rule in `SKILL.md` saying "use the Hebrew script" against four examples that never do would be a rule the examples overrule — which is exactly the shape of failure Round 3 recorded (*grep the whole file for the assumption, not just the paragraph that argues it*), now at tree level rather than file level.

**Consequence:** Round 4 requires rebuilt artefacts, not proposal cards alone. See *How each amendment is applied*.

---

## `book-overview` — four amendments

### Amendment O — Load the substrate

**Current text (Phase 1):**

> **Read the whole book** in ESV, ideally in one sitting. Identify the genre. Note first impressions of situation, repeated words, and structure before analysing.

This is the sentence that makes every other problem possible. A book read only in English cannot see a repeated root, a Leitwort, a formula's count, or a name-pun — and "note first impressions of **repeated words**" is precisely the observation English cannot support.

**Proposed: a new Phase 0.2, mirroring `dig-deeper`'s, and Phase 1 rewritten.**

> **0.2 — Load the substrate.** Locate `_texts/` in the connected prep folder and read its README before using it. Take the book's Hebrew or Greek from the corpus — `hebrew-wlc/`, `greek-lxx-swete/`, `greek-nt-sblgnt/` — not from memory and not from a search. Every count, chain and repetition claim in the overview is made against the corpus and **names its edition**. Where a finding turns on a particular reading rather than on the wording generally (a variant, an apparatus question, a Rahlfs-vs-Swete divergence, an NA28 decision), the corpus is not enough: go to Logos and cite that; your own exports are in `_texts/logos-exports/`. **Do not ask a search engine what a verse says.** And know what the corpus cannot show you: it holds **one** Hebrew manuscript tradition, so it can verify wording, counts and chains, and it can never report how widely an apparatus feature is attested. If the corpus is unreachable, say so in the colophon before proceeding rather than falling back silently — and an overview that never saw the original language may not report a count, a repetition, or a Leitwort as `[T]`.

> **1 — Read the whole book in its original language first, then in English**, ideally in one sitting each. Identify the genre. Note first impressions of situation, repeated words and structure before analysing — **the repeated-words observation is made in the original, because it cannot be made in a translation.**

### Amendment P — Canonical position becomes a produced thread

**The gap.** `dig-deeper` gained Phase 0.55 in Round 1, which states the Tanak position of the book as five fields — Section · Reading implication · Presupposes · Handoff · Neighbours — and says *"at book level state it as five fields"*. **At book level.** But the skill that works at book level does not produce it, so every dig recomputes it from scratch, and the overview — the natural home for a book-level fact — is silent on where the book stands.

The pattern is not hypothetical. It was harvested from four imported overviews into `canon-position-pattern.md` on 4 September precisely so it could be carried forward, and `ruth-worked.md` already carries a hand-written version of it (*"in the Hebrew canon Ruth sits in the Writings (Megilloth)…"*) — the practice exists in the example and is absent from the contract.

**Proposed: an eighth deliverable thread, and a new Phase 2a.**

> **8. Canonical position** ★ — where the book stands in the Tanak (Torah / Nevi'im Former or Latter / Ketuvim), in the BHS order, stated as five fields: **Section · Reading implication · Presupposes · Handoff · Neighbours**, of which **Presupposes carries the testable claims and must be filled with checked references**. Ruth stands among the Megilloth, not after Judges; Daniel is in the Writings; Chronicles closes the canon. **Where canonical order and compositional order diverge — Isa 36–39 ‖ 2 Kgs 18–20 is the paradigm — report both and resolve neither by default**, leaving the direction of dependence as a named open question. For NT books, give the equivalent: position in the collection, what it presupposes, what it hands on.

Starred, because `dig-deeper` should extract it at Phase 0.5 rather than re-derive it at 0.55.

### Amendment Q — The chain gate belongs where chains are made

**The structural error.** `dig-deeper`'s gate item (e3) ends: *an unverified chain "may not enter a book overview"*. The Synthetic Claims section repeats it. But **the prohibition lives in the wrong skill.** It stops a dig exporting an unverified chain *into* an overview; it says nothing about the chains an overview builds natively — and Phase 5 instructs the overview to *"sweep the book for quotations, distinctive verbal echoes, and conceptual/name/number allusions"* and Phase 8 to build an early↔late echo table. Those two threads are described in this skill's own words as **the load-bearing outputs**. They are also, precisely, manufactured synthetic claims: cross-passage chains, built at speed, across a whole book.

The audits agree across three books that synthetic claims fail at a much higher rate than passage-level ones. The overview is where they are made, and it has no gate at all.

**Proposed: a new Phase 10.5, before the write-up.**

> **10.5 — Pre-output gate (a gate, not a review).** Fix any failure before writing the file. (a) **Every claim that a word, root or formula recurs across two or more places is verified against the corpus lemma index — by lemma, never by pointed surface form or English gloss — and each claimed reference confirmed to contain it.** Where a phrase search is unavoidable, normalise maqqef, paseq and sof pasuq to spaces and NFD-strip combining marks, and run a second skeletal pass with waw, yod and word-final *he* deleted, since a defective spelling drops a verse silently. A reference that fails is removed from the chain or the chain restated — never hedged and left standing. (b) Every count names its edition. (c) Every finding resting on a feature of the **apparatus** rather than the wording — *parashoth*, accentuation, ketiv/qere, Masorah — names its witness rather than the tradition ("as BHS prints it", never "the Masoretic text" unqualified), and says where the feature is a reading tradition rather than authorial. (d) Every live source in the intertextual map carries a confidence flag. (e) Where the corpus was unavailable, every chain claim is tagged `[unverified — chain not checked]`, capped at moderate confidence, and **may not be handed to a dig as though it were established**. Record the results in the colophon.

*The last clause matters more than it looks: an overview's whole purpose is to be consumed downstream, so an unverified chain in an overview is not a local defect. It is a defect with a delivery mechanism.*

### Amendment R — Study text, and the absence of a pulpit text

**Current:** *"Default translation: ESV"* (description), *"British English; ESV default"* (Key Principles), *"**Translation:** ESV"* (the template header in `references/deliverables.md` and both worked examples).

**Proposed:**

> **The study text is the NASB95** — the 1995 edition specifically, not the 2020 revision, which is a substantially different text. Quote it as the overview's English reference, alongside the Hebrew or Greek the findings rest on.
>
> **A book overview declares no pulpit text.** No sermon is in view; a pulpit text is a fact about an engagement, not about a book, and one should not be invented. The header field reads **"Pulpit text: N/A — no sermon in view"**. Where the overview proposes preaching units, that is a plan, not an engagement.

*This is a small precision worth stating: `dig-deeper` already says a pulpit text should not be invented where no sermon is in view, and a book overview is the clearest instance of that case.*

---

## Amendment S — the gloss convention (all four skills)

**The request, in the user's words:** the original-language word in its own letters, with an English translation in brackets after it, **every time**.

**Why it is a house convention and not a `dig-deeper` convention.** A book overview names Hebrew terms in its intertextual map and echo table; `point-purpose` carries them into the sermon plan; `sermon-review` quotes them in a manuscript read from a pulpit. If only one skill adopts the rule, the outputs of a single series disagree with each other.

**Proposed, for all four skills:**

> **Original languages appear in their own script, with an English gloss in brackets immediately after — every occurrence, not only the first.** שָׁכַן ("to dwell"), λόγος ("word"), קְדוֹשׁ יִשְׂרָאֵל ("the Holy One of Israel"). The gloss is the NASB95 rendering where the word is being discussed as it stands in a particular verse, and a lexical gloss where the word is being discussed as a word. **Transliteration is kept only where the sound is the point** — paronomasia, assonance, a name-pun — in which case give the script, the gloss, and the transliteration together: נְחֹשֶׁת ("bronze", *nĕḥōšet*) against נָחָשׁ ("serpent", *nāḥāš*). A report that transliterates by default has made the reader's Hebrew harder to learn, not easier.

**What this requires beyond `SKILL.md`.** All four worked examples teach the opposite (see the measurement above). Each must be revised so that the anchor and the rule agree. This is the bulk of the work in Round 4 and it cannot be skipped: the Consistency Contract tells a run to match the example, so an unrevised example silently repeals the rule.

**Rendering is already handled.** The `.odt` converter sets Liberation Serif as the complex-script face and Hebrew three points above the body size; the house HTML scales Hebrew by 125% through a `unicode-range` font declaration. Both were fixed and verified on 12 September — Hebrew and Greek were confirmed present and correctly drawn in a PDF rendered from the house `.odt`.

---

## `point-purpose` — Amendment T

**Current:** *"Default translation: ESV"* (description); *"**British English; ESV default** unless the exegesis specifies another translation — the exegesis's wording transfers directly into the plan."*

The instinct in the second half is right — the wording should transfer from the exegesis — but the default is wrong, and `point-purpose` is the one downstream skill where a pulpit text genuinely *is* in view.

**Proposed:**

> **British English. The study text is the NASB95**, inherited from the dig-deeper report the plan is built on; its wording transfers directly into the plan. **`point-purpose` is sermon-facing, so the pulpit text is live: ask which version the engagement uses if it has not been stated, and never assume the ESV.** Where the pulpit text and the NASB95 diverge in a way that bears on the Teaching Point or the Purpose Statement, say so and say what the congregation will actually hear — that gap is a note to the preacher, not a translation verdict.

---

## `sermon-review` — Amendments U and V

### Amendment U — house style and output format

**Current:** a full `.docx` specification — A4, Georgia 13 pt, 1.5 line spacing, Arial headings in #2E4057, built with the `docx` npm library.

**This is superseded in three separate ways** by settled preference: the house style is **A5 portrait, Liberation Serif**; sermon outputs are **LibreOffice-native `.odt`**, not `.docx`; and the house `.odt` is built by `_house-style/make_odt.py`, which also handles the complex-script font and size that Amendment S now requires.

**Proposed:**

> Produce the manuscript as a **LibreOffice Writer document (`.odt`)** in the house style: A5 portrait; margins top 15 mm, bottom 10 mm, sides 10 mm; Liberation Serif — title 18 pt, headings 14 pt bold with no line below, body 12 pt at 1.15 line spacing with 0 above and 2 mm below, footnotes 10 pt with a 0.6 cm hanging indent; English (UK); widow/orphan control at two lines. Build it from Markdown with `_house-style/make_odt.py`, which applies the house style, declares the complex-script font, and sets Hebrew three points above the body size. **Do not build sermon manuscripts with the `docx` library.**
>
> Scripture quotations are indented and italic at body size. The closing "Amen." and any repeated opening question keep their emphasis through weight and centring rather than a second typeface — the house style uses one family.

*Worth flagging honestly: the existing spec encodes real design decisions — the colour accents, the bordered headings, the centred Amen. Some will not survive a single-family A5 house style, and that is a loss as well as a correction. This amendment should be reviewed against an actual rendered manuscript rather than accepted on paper.*

### Amendment V — the version footer follows the declared pulpit text

**Current:** *"Bible version: Usually the English Standard Version (ESV)… Always include an ESV attribution footer (or the relevant version)."*

A sermon manuscript quotes the version the congregation will hear, which varies by engagement.

**Proposed:**

> **Bible version: the declared pulpit text for this engagement.** Ask which version applies if it has not been stated; do not default to the ESV. The attribution footer names that version. Where the manuscript discusses a word in the original, the study text (NASB95) may be cited alongside to show what the pulpit text has decided — but what is read aloud is the pulpit text.

---

## How each amendment is applied

| Amendment | Skill | Reaches it how |
|---|---|---|
| O, P, Q, R | `book-overview` | **Plugin skill** — changes go through the plugin mechanism, not a proposal card |
| S | all four | `SKILL.md` edits **plus** four revised worked examples → plugin rebuild *and* a rebuilt `.skill` package |
| T | `point-purpose` | Account skill — proposal card |
| U, V | `sermon-review` | Account skill — proposal card |

Two carried obligations:

- **The Round 3 entry in `references/CHANGELOG.md`** is still outstanding. It goes in with the `dig-deeper` package this round requires.
- **Any `.skill` package must be built from the installed, post-Round-3 `SKILL.md`**, or installing it silently reverts Round 3.

## Recommended order

1. **T** — one line, no dependencies, removes a live contradiction.
2. **O and R** — `book-overview`'s substrate and study text. These stop the worst thing the toolkit currently does, which is to let an English-only overview enter a corpus-disciplined dig wearing the authority of a checked source.
3. **Q** — the chain gate. Prevents defects rather than improving findings, and the overview is where the highest-risk claims are manufactured.
4. **P** — canonical position. Improves the contract and saves every downstream dig a re-derivation.
5. **U and V** — `sermon-review`. Review against a rendered manuscript, not on paper.
6. **S** — the gloss convention, last, because it touches all four skills and four worked examples, and because doing it last means each example is revised once, against the finished rules.

## What is deliberately not proposed

- **No change to the seven existing deliverable threads**, their order, or the phase structure of `book-overview`. They are working; this round adds to them.
- **No change to `sailhamer-analysis`, `song-assessment`, `whisper-transcript` or `logos-research`.** None of them asserts a translation default or a house style that now conflicts. `logos-research` mentions an NASB rail shortcut, which is a description of the Logos interface, not a study-text claim.
- **No attempt to make `book-overview` run the sixteen tools.** The division of labour between orientation and exegesis is sound and this round does not touch it.

## As applied, 13 September 2026

### The converter question, settled first

`_house-style/make_odt.py` is now the **canonical** house `.odt` converter and carries
`HOUSE_ODT_VERSION`. A skill that cannot rely on the prep folder being connected takes a
**generated, hash-stamped copy** rather than a hand-maintained one, produced by the new
`_house-style/bundle_converter.py`:

```
python3 _house-style/bundle_converter.py <destination.py>     # write a stamped copy
python3 _house-style/bundle_converter.py --check <file.py>    # report drift
```

The check distinguishes **two** failures, because they need different answers and the
first version of it caught neither:

- **EDITED BY HAND** — the copy's body no longer matches the stamp it carries. Someone
  fixed the copy instead of the original. Move the change to the canonical file, bump the
  version, regenerate.
- **STALE** — the stamp no longer matches the canonical file. The original moved on and
  the copy did not.

*Both were tested by causing them.* The first implementation compared only the stamp with
the canonical hash, so editing a copy by hand still reported `CURRENT` — which is exactly
the silent divergence the mechanism exists to prevent.

### `sermon-review` — U, V and S applied

Delivered as a proposal card. It is a single-file skill, so nothing needed packaging.
Alongside U and V, one deliberate departure from Amendment S:

**S is inverted for a sermon manuscript, and only for a manuscript.** Elsewhere the rule
is script first, gloss in brackets. A manuscript is read aloud, so the running text
carries the **English** and the original follows in brackets in its own script:

> "The word is *dwell* — not visit, not pass through, but settle down and stay
> (שָׁכַן)."

A preacher cannot read pointed Hebrew aloud from a script under pressure, and a sentence
that opens with unvocalised script invites a stumble in the pulpit. The skill states the
principle so it is visible and editable: *never put an original-language word where the
preacher must read it aloud to complete the sentence.* Transliteration is kept where the
sound is the point, which in preaching is more often than in a report.

Two further changes the amendment did not anticipate, found by reading the file end to
end rather than patching the paragraphs the spec named:

- **A tenth review criterion — the pulpit text.** Amendment V made the pulpit text a
  variable; nothing then *checked* it. Stage 1 now asks whether the declared pulpit text
  actually carries the wording the sermon's argument turns on. A point that works in the
  NASB95 and vanishes in the congregation's version is a problem to solve before Sunday.
- **A step 2 in the process flow**, confirming the pulpit text before the review begins,
  because criterion 10 cannot run without it.

*What this costs, stated plainly:* the old specification's colour accents, bordered Arial
headings and 15 pt centred "Amen." do not survive a single-family A5 house style. Emphasis
now comes from weight, centring and space. That is a real loss as well as a correction,
and it should be judged against a rendered manuscript rather than this paragraph.

### `book-overview` — O, P, Q, R and S applied (plugin v0.2.0)

Delivered as a rebuilt plugin. Phase 0.2 loads the corpus; Phase 1 reads the original language first; Phase 2a and a new **eighth starred thread** produce the canonical position; Phase 10.5 is the chain gate, now living where chains are made rather than where they arrive. `references/deliverables.md` gains § 8 and a rebuilt template header and colophon.

**The two worked examples went from zero Hebrew and zero Greek to 300 and 150 characters**, every word checked against the corpus rather than written from memory. Two results:

- **Ruth's echo table carried a real error.** It recorded Naomi's "rest" at 1:9 and 3:1 as a repeated word. The Hebrew has מְנוּחָה at 1:9 and מָנוֹחַ at 3:1 — cognate nouns from נוח, not one lexeme. The echo stands; "the same word recurs" would not have. **The NASB95 reads "rest" in both places, so no English text could have exposed it.** The correction is now written into the example as the worked justification for the gate.
- **Philippians' claims all held and are now verifiable:** χαρά/χαίρω/συγχαίρω exactly 16 occurrences across 12 verses; φρονέω in 7 verses spanning every movement; στήκω at 1:27 and 4:1 only; συναθλέω at 1:27 and 4:3 **and nowhere else in the New Testament** — that last asserted by the old example, now checked canon-wide.

### `point-purpose` — T and S applied, and the mechanism was wrong

This document predicted `point-purpose` would need a package, because a proposal card cannot reach `scripts/render_odt.py`. **Reading the file end to end showed a card is enough**, because the right fix is not to repair the bundled renderer but to stop using it: `SKILL.md` now points at the canonical `_house-style/make_odt.py` and **supersedes the bundled script explicitly, naming its four defects**, with the same fallback `sermon-review` uses when the prep folder is not connected.

*The residue, stated plainly:* the superseded file is still physically present in the skill. A card cannot delete it. It is inert as long as `SKILL.md` is followed, and removing it is a tidying job for whenever the skill next needs a package for another reason.

Two additions the amendment did not anticipate, again found by reading rather than patching:

- **A Phase 8.5 pulpit-text check.** T made the pulpit text live for this skill; nothing then tested it. A Teaching Point resting on a repeated root the pulpit text levels into synonyms, or on a connective it drops, is a plan that works on paper and dies in the pulpit — and it is far cheaper to find here than on Sunday.
- **The gloss order is house-standard here, and the skill says why.** A plan is studied, not spoken, so script leads and the gloss follows. The document states that the manuscript stage inverts it, so the order is not carried across by habit.

## Check before applying

Round 3's lesson, unchanged: **grep the whole file for the assumption, not just the paragraph that argues it.** Applying Round 3 to its own stated scope would have left five contradictions elsewhere in the file. This round spans four skills and two reference trees, so that check is correspondingly larger — and the assessment above rests on targeted greps plus one full read of `book-overview/SKILL.md`. Each file should be read end to end at application time, not trusted from this document.
