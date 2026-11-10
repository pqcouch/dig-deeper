# Toolkit Amendments, Round 10

**Date:** 9 November 2026\
**Status:** **Accepted 9 November 2026; packaged for installation.** AH is adopted on trial (withdraw if the next three claim audits raise no new design claim). Packages and the pre-round backup are in `_skill-backup/`: `dig-deeper-round-10-2026-11-09.skill`, `book-overview-0.3.3-round-10-2026-11-09.plugin`, `backup-pre-round-10-2026-11-09.tgz`; point-purpose by proposal card. **Installed and verified 9 November 2026, 10:05:** the installed dig-deeper folder is byte-identical to the package; book-overview 0.3.3 (the copy in use, and the copy the skill loader reads) is identical to the package; point-purpose matches the proposal card (the loader quotes the `name` field, a formatting difference only). The old 0.3.2 folder remains in the sync cache, unused.\
**Source run:** the Colossians Finalise pass of 4 November 2026 (overview v1.2; macro-synthesis v1.1), with claim audit 5 and its dig patches\
**Lettering:** AF–AH. AD and AE are each used twice already (round 8's document and the round-9 CHANGELOG entry), so this round starts at AF to avoid a third collision.\
**Files affected:** `dig-deeper/SKILL.md`; `dig-deeper/references/claim-audit-format.md`; `dig-deeper/references/CHANGELOG.md`; `book-overview/references/modes-and-interfaces.md`; `point-purpose/SKILL.md`. Checked against the installed copies on 9 November 2026, not against earlier notes.

---

## Summary

| | What fails now | Amendment | Evidence |
|---|---|---|---|
| **AF** | A claim audit "reproduces" an *only*, *identical* or *exactly* by lemma, so a changed or reordered phrase passes | Shape words need an ordered phrase search, in the dig gate and in every audit spot check | Two shape errors survived claim audits 3 and 5 |
| **AG** | Audit patches go into a table at the foot of a dig, and the headline above keeps the superseded wording, which point-purpose reads first | Headline-level changes are rewritten in place; Finalise lists any stale headline; point-purpose reads governing sections first | Eight digs patched this way on 4 November |
| **AH** | An audit introduces a new *design* claim and propagates it straight into a dig, without the baseline it requires of every other design claim | New design claims raised by an audit are queued, not propagated, and capped at moderate | Audit 5's "distance echo is the letter's real linking device" |

All three come from errors found in one run. AF rests on two independent errors of the same kind, and is the firmest. AG and AH each rest on one pass, but their faults are mechanical, not interpretive.

---

## The evidence

### AF — two shape claims that survived the audits

1. **"ὃ ἐὰν ποιῆτε ('whatever you do'), NT only Col 3:17 and 3:23."** This stood in the 3:18–4:1 dig, in claim audit 3 (C41), in the overview's Echo 64, and in claim audit 5, where Auditor B listed it among the confirmed "only"s and the main session "reproduced" it. The two verses do not read the same: NA28 and SBLGNT print καὶ πᾶν ὅ τι ἐὰν ποιῆτε at 3:17 and ὃ ἐὰν ποιῆτε at 3:23. What is exclusive is a relative pronoun with ἐὰν ποιῆτε; John 13:17 and 15:14 have ἐὰν ποιῆτε as a condition. The NA28 apparatus shows the majority text (D¹ K L 𝔪) assimilating 3:23 to 3:17, καὶ πᾶν ὅ τι, so the scribes heard the link too. **The link holds; the shape claim did not.**
2. **"Luke 1:79 repeats Ps 106:10 exactly"** (claim audit 5, C61, Auditor A). Ps 106:10 LXX reads καθημένους ἐν σκότει καὶ σκιᾷ θανάτου; Luke 1:79 reads τοῖς ἐν σκότει καὶ σκιᾷ θανάτου καθημένοις. The words are the same, but the participle has moved to the end and is dative, not accusative.

**Why the checks missed them.** Both were checked by lemma. A lemma check confirms that the words are present, and is blind to order and form. The book-overview gate already has the rule that would have caught them (round 8, AC, Phase 10.5 (a): *identical*, *verbatim*, *the same phrase* and *only* are shape claims, licensed only by an ordered phrase search). **The dig-deeper gate and the claim-audit spot checks do not**, and the audit's reproduction step is where both errors were passed as confirmed.

### AG — patches that leave the headline behind

Claim audit 5 was applied to eight digs on 4 November by appending a section headed "Claim audit 5 (vN)" whose first line says it "governs the paragraphs above where they differ". The headlines above were left as they were. In the 1:1–14 dig, Headline 4 still reads the "you" → "us" shift as *moderate–high* design; the table below lowers that to *low–moderate*. The point-purpose skill's Phase 1, row 1 tells it to read **Headline Findings, So What, candidate FCF, Christological Reading and Preaching Pitfalls** — not the governing table at the foot. Run as written, point-purpose on 1:1–14 would build its Teaching Point from the superseded headline.

The Finalise pass found the tables and checked them against the propagation table, but its procedure gave it no step for noticing that a headline had gone stale.

### AH — a design claim introduced by an audit

Claim audit 5 discarded the "welded seams" as a design, rightly, on a 20,000-cut baseline. In the same verdict it described **distance echo as "the letter's real linking device"**, and that sentence went into the 2:6–15 dig's patch. Distance echo as a *device* is itself a design claim, and no baseline was run on it. The Finalise pass capped it at *moderate*, but only because it noticed. A second, smaller case: the audit grouped σύνδεσμος ("bond", 2:19 → 3:14) with ταπεινοφροσύνη as "re-valued", though audit 2 had called that link a continuation. It went to the queue (C78), which is the right place, so no harm followed.

The rule that a design claim is capped at *moderate* until baselined is written for the claims an audit *tests*. It says nothing about the claims an audit *makes*.

---

## Amendment AF — shape words need an ordered phrase search

### AF1 · `dig-deeper/SKILL.md`, Phase 10.5, gate item (e3)

**Find** (inside item (e3)):

> (קְדוֹשׁ יִשְׂרָאֵל is 25 verses of Isaiah, not the 24 a plene-only search returns: 49:7 spells it קְדֹשׁ);

**Replace with:**

> (קְדוֹשׁ יִשְׂרָאֵל is 25 verses of Isaiah, not the 24 a plene-only search returns: 49:7 spells it קְדֹשׁ); **and the words *identical*, *verbatim*, *exactly*, *the same phrase*, and any *only* that rests on a phrase rather than a word, are claims about shape, which a lemma check cannot verify: they are licensed only by an ordered phrase search on the surface text (Hebrew normalised as above, plain and skeletal; Greek accent-stripped), and where the lemmas match but the order or the forms differ the report says *reordered*, *partial* or *in a different form* — "ὃ ἐὰν ποιῆτε, NT only Col 3:17, 23" passed three checks by lemma while 3:17 reads ὅ τι ἐὰν ποιῆτε (round 10, AF)**;

### AF2 · `dig-deeper/references/claim-audit-format.md`, after the paragraph beginning "**Spot checks and positive controls are written as prose**"

**Insert:**

> **A verdict that confirms a shape word is reproduced by an ordered phrase search, not by lemma.** Where an auditor's finding says *only*, *identical*, *verbatim*, *exactly* or *the same phrase*, the main session's spot check runs the phrase in order on the surface text and quotes both places as they stand. A lemma reproduction confirms that the words are present and cannot see a reordered or altered form. Colossians claim audit 5 "reproduced" two shape claims this way, and both were wrong in shape: ὃ ἐὰν ποιῆτε at Col 3:17, 23 (3:17 has ὅ τι), and Luke 1:79 "exactly" Ps 106:10 (the participle moved and changed case).

**Also add to the auditors' brief** (the claims-file preamble the main session writes for each blind auditor): *"Where you report that a phrase is identical, verbatim, exact or found only in certain places, quote each occurrence in full as the text prints it."*

---

## Amendment AG — a headline is rewritten, not governed from below

### AG1 · `dig-deeper/references/claim-audit-format.md`, section "Confidence Change Propagation", after its first paragraph

**Insert:**

> **Patching a dig.** When a verdict changes what a dig's **Headline Findings**, **So What** or **candidate FCF** says or rates, the patch rewrites that paragraph in place and marks it (*"v1.3 — claim audit 5: …"*), keeping the earlier wording only if the change needs it to be understood. A table appended at the foot that "governs the paragraphs above" is acceptable for body sections (the tools, Open Questions, Book-Overview Tensions), never for these three, because they are what `point-purpose` lifts. The propagation table gets a column, **Headline touched?**, answered yes or no for each dig, so the patch list cannot omit one.

### AG2 · `book-overview/references/modes-and-interfaces.md`, Finalise / Upgrade procedure, new step 7

**Insert after step 6:**

> 7. **List stale headlines.** For each dig whose later sections (an audit table, a "What Changed" section) govern earlier ones, check its Headline Findings, So What and candidate FCF against the governing wording. List any that now disagree in the colophon under **Stale headlines**, and either patch them in the same pass or name them as owed before `point-purpose` runs on that unit. A finalised overview resting on digs whose own headlines contradict their patches is not ready to hand on.

### AG3 · `point-purpose/SKILL.md`, Phase 1, row 1

**Find:**

> | 1 | **Locate the exegesis.** Prefer a `dig-deeper` report; read its Headline Findings, So What, candidate FCF, Christological Reading, and Preaching Pitfalls. |

**Replace with:**

> | 1 | **Locate the exegesis.** Prefer a `dig-deeper` report. **First read any section that governs earlier ones** — headed "Claim audit N", "What Changed in vN" or "Revision vN" — then read its Headline Findings, So What, candidate FCF, Christological Reading, and Preaching Pitfalls. Where a governing section changes a headline's rating or wording, build from the governing version, and say so in the backbone. |

AG3 is a safeguard for the reports already patched the old way. AG1 stops new ones.

---

## Amendment AH — an audit's own design claims go to the queue

### AH1 · `dig-deeper/references/claim-audit-format.md`, section "Summary", new paragraph after "Recommended book-overview revisions"

**Insert:**

> ### New claims raised by the audit
>
> An audit often proposes something while testing something else. **A new single contact** is queued with a suggested rating, as now. **A new design claim** — a device, a pattern, a structure, a "real" explanation offered in place of one discarded — is queued too, capped at *moderate* until its own chance baseline has run, and **is not written into the propagation table or into any dig's patch**. The rule that holds design claims to a baseline applies to the claims an audit makes, not only to those it tests. Colossians claim audit 5 discarded the "welded seams" on a 20,000-cut baseline and in the same verdict called distance echo "the letter's real linking device", with no baseline, and that sentence reached a dig.

---

## CHANGELOG entry (for `dig-deeper/references/CHANGELOG.md`, at the top)

> *Revised November 2026, round 10 (shape words in audits; headlines left behind by patches; an audit's own design claims), from the Colossians Finalise pass of 4 November 2026.* **(AF)** Gate item (e3) gains the shape-word rule the book-overview gate has had since round 8 (AC); `claim-audit-format.md` requires shape verdicts to be reproduced by ordered phrase search, and auditors to quote each occurrence. Evidence: ὃ ἐὰν ποιῆτε at Col 3:17, 23 (3:17 has ὅ τι) and Luke 1:79 against Ps 106:10 (participle moved, case changed) both passed audit checks by lemma. **(AG)** Headline Findings, So What and candidate FCF are patched in place; the propagation table records whether a headline was touched; Finalise lists stale headlines; `point-purpose` reads governing sections first. Evidence: eight Colossians digs patched by appended tables, with the 1:1–14 Headline 4 left at its superseded rating. **(AH)** Design claims raised by an audit are queued, capped at moderate and kept out of patches. Evidence: "distance echo is the letter's real linking device" (audit 5) reached the 2:6–15 dig without a baseline.

---

## How it would be installed

The route learned on 7 September still applies: a proposal card replaces `SKILL.md` only, so the reference-file edits need packages.

- **dig-deeper:** one `.skill` package carrying `SKILL.md` (AF1), `claim-audit-format.md` (AF2, AG1, AH1) and `CHANGELOG.md`. Backup of the installed folder first, in `_skill-backup/`.
- **book-overview:** a `.plugin` package (version 0.3.2 → 0.3.3) carrying `modes-and-interfaces.md` (AG2).
- **point-purpose:** AG3 is a `SKILL.md`-only edit, so a proposal card can carry it.

After installation, check the installed files directly, not this document's status line (the round-1 lesson).

---

## What this round does not change

- **The house converters.** The fix for lists running into the paragraph above them was applied on 9 November 2026 to `_house-style/make_odt.py` and `make_html.py` (pandoc option `+lists_without_preceding_blankline`). That is house tooling, not a skill, and is recorded here only so the two are not confused.
- **The Colossians files themselves.** Claim audit 5 still says "exactly" and "only these two"; three digs still carry the ποιῆτε claim; the 1:1–14 headlines still need rewriting under AG1. That is the tidying pass, which follows this round.
- **The seven amendments proposed by the Daniel claim audit (1 November).** Not reviewed here; they are still unapplied.

---

## Critical assessment

- **AF is well founded:** two independent errors of one kind, and the rule already exists one skill over. The cost is a phrase search per shape claim.
- **AG3 makes point-purpose read more,** and a report with several governing sections (the 1:15–20 dig has eight revisions) could become hard to read in order. AG1 is the real fix; AG3 can be withdrawn once the existing digs have had their headlines rewritten.
- **AH rests on one sentence in one audit.** It is cheap, since it only moves new design claims from the patch to the queue, but it is not yet shown to be needed often. It could be marked *adopted on trial* and withdrawn if the next three audits raise no new design claim.
- **None of this was tested on a live run.** Rounds 2 and 5 adopted rules on trial for that reason; AH is the one this round would mark so.
