# Toolkit amendments — Round 7: the claims the chain gate cannot see

**Date:** 3 October 2026 · **Letters:** AB, AC, AD — continuing from Round 6's Z and AA
**Skills touched:** `book-overview` (`SKILL.md`, `references/deliverables.md`), plus one new corpus tool, `_texts/tools/contacts.py`
**Status:** DRAFTED, not applied. The find/replace pairs below are ready for a `.skill` package. The draft tool is in `_skill-backup/round-7-draft/contacts.py`.
**Occasion:** the Lamentations book overview (v0.1.0) and its claim audit, both of 3 October 2026.

---

## Summary

The book-overview gate (Phase 10.5) asks one question of an allusion: **are the claimed words present in the claimed verses?** The Lamentations overview passed that test. About 128 lemma claims were checked, and the claim audit found **no stated "only" that was false**. Yet seven of the eleven audited claims came back *Needs reframing*. The overview also missed the book's densest partner altogether, and five of its wording statements were wrong.

None of these failures was a missing word. They were failures of four other kinds, none of which the gate looks at:

1. **Rivals.** The words were present, but another text shared them as closely or more closely. Isa 52:11 is closer than Lev 13:45 at Lam 4:15; Jer 14:19 is closer than Ps 89 at 5:22; Jer 18:16 rivals Lam 2:15 behind Matt 27:39.
2. **Shape.** The words were present but not as claimed. The overview called Ps 143:3 "identical" to Lam 3:6; the first two words are reversed. It counted Job 9:18 as sharing a noun that is in fact a different noun. And it listed a lemma (פְּרִי, "fruit") at two verses of a row when it stands at only one.
3. **Design.** "Live at six places", "concentric", "the densest answer in the canon", "every one of Zion's humiliations", "the handoff". Each is a claim about a *pattern*, and each fell to a chance baseline that the overview never ran.
4. **Omission.** The map was built by sweeping the book for what the drafter already knew to look for. A mechanical scan of the whole canon puts **Jeremiah 14** first of 858 chapters for Lam 1–2, and it was not in the map at all.

This round adds three gate items and one tool:

- **AB — rival search and a density scan.** Before any allusion enters the map above *moderate*, count how many verses share its words and name the closest rivals. Before the map is finalised, scan the whole canon for the book's densest partners, and account for every chapter in the top ten.
- **AC — wording shape.** "Identical", "verbatim", "the same phrase" and "only" must pass an *ordered* phrase test. A row citing several verses must be verified **verse by verse**, not as a set.
- **AD — design claims and superlatives.** A design claim — a live source, a structure, a handoff — is capped at *moderate* until a chance baseline has been run. A superlative is barred unless it was measured. This brings the overview into line with the sweep rule `dig-deeper` already has (Sweep Mode item 5).
- **The tool:** `contacts.py`, so that AB and AC take one command each.

**What the round does not do.** It does not replace the claim audit. AB–AD catch the *mechanical* failures before an overview is written. Whether an allusion is deliberate is still a judgement, and still the audit's job.

---

## The evidence

### What the gate checked and what failed

| Claim (overview v0.1.0) | Passed the chain gate? | What failed | Would have been caught by |
|---|---|---|---|
| Deut 28 live at six places | yes | design: two strong links, not six; Lamentations' Deut 28 density is ordinary for a judgement text (4.5 %, against 2.3–11.6 % in the controls) | AD (baseline); AB (rivals: 2 Kgs 6:29, Jer 4:13) |
| Deut 28 row: פְּרִי at 2:20 *and 4:10* | yes — checked as a set | row-level: פְּרִי is at 2:20 only | AC (verse-by-verse) |
| Lev 13:45–46 behind 4:15; 1:1 | yes | rival: Isa 52:11 shares four elements in order; Lev 13:45 shares two | AB |
| Concentric frame 1↔5, 2↔4 | yes | design: 2–4 is exactly at chance on vocabulary (observed ÷ expected = 1.00); 1–2 is as strong at phrase level | AD |
| Dan 9 as handoff | yes | design and rivals: Dan 9 ranks near the bottom of the confession family; Isa 63–64 matches Lam 5:1 more closely | AB; AD |
| Isa 47: "every one of Zion's humiliations" | yes | superlative: two of the five contacts are idiom with closer rivals | AD; AB |
| Isa 51:17–23 "densest answer in the canon" | yes | superlative: 395th of 5,231 windows; it leads only as 51:17–52:2 | AD |
| Ezek net at 1:13 | yes | rival and idiom: the pair occurs in nine verses, and the "net for the feet" belongs with Ps 9; 57; Prov 29 | AB |
| Ps 89 "six places" in Lam 4–5 | yes | wrong target: Ps 89 is distinctive for Lam 2 (4th of 2,514 windows), not Lam 4–5 (81st) | AB (scan); AD |
| Job "behind Lam 3" | yes | design: Job is mid-band by density; Jer 11–20 and Isa 49–54 run higher | AD; AB |
| Matt 27:39 "only Lamentations supplies" | yes | rival: Jer 18:16 LXX has the same image with a sister verb | AB |
| Ps 143:3 "identical" at Lam 3:6 | yes | shape: the first two words are reversed | AC |
| Job 9:18 "שׂבע + מְרֹרִים" | yes — checked by root | shape: Job has a different noun (מַמְּרֹרִים) | AC |
| Amos 5:18, 20 "phrase" at 3:2 | yes | shape and rival: the phrase is at Amos 5:18 and Job 12:25, not at 5:20 | AC; AB |
| **Jer 14 — absent from the map** | n/a | **omission: first of 858 chapters by rare-contact density for Lam 1–2** | AB (scan) |

### This is the fourth audit to find the same pattern

| Audit | Single exclusive links | Design / synthetic claims |
|---|---|---|
| Mark, 29 Sep | the 74 lexical chains all passed their gate | only 5 of 21 allusions survived as rated |
| Matthew audit 2, 2 Oct | 30 of 41 confirmed | a "Sermon ↔ passion" pattern was no more frequent than chance |
| Job audit 2, 3 Oct | the verbatim and rare links held | "every design claim built from ordinary pairs came down" |
| **Lamentations, 3 Oct** | **every exclusive link held** | **all seven design claims needed reframing** |

**The chain gate is doing exactly what it was built to do. It was never built to test these claims.**

---

## Amendment AB — rival search and a canon-wide density scan

### AB1 — `book-overview/SKILL.md`, Phase 5 row

**Find:**

> | 5 | **Build the intertextual map.** Sweep the book for quotations, distinctive verbal echoes, and conceptual/name/number allusions. Record source → location(s) → what each use does. Mark live sources (≥2 uses). Note explicitly when the book is OT-citation-light and carried mainly by internal repetition (a finding dig-deeper needs). |

**Replace with:**

> | 5 | **Build the intertextual map.** Sweep the book for quotations, distinctive verbal echoes, and conceptual/name/number allusions. Record source → location(s) → what each use does. Mark live sources (≥2 uses). Note explicitly when the book is OT-citation-light and carried mainly by internal repetition (a finding dig-deeper needs). **Then run the density scan** — `python3 _texts/tools/contacts.py scan <Book>`, and once per major block (`<Book>:1-2`) — which ranks every chapter of the Hebrew Bible by rare shared vocabulary with the book. **Every chapter in the top ten must be accounted for:** either it enters the map, or the map says in one line why it does not (common subject matter, a list, a genealogy). A map that has been swept only for what the drafter already knew to look for will miss its densest partner — the Lamentations overview of 3 October 2026 omitted Jeremiah 14, which the scan ranks first of 858 chapters. *(OT books. For NT books the scan is not yet built; say so in the colophon.)* |

### AB2 — `book-overview/SKILL.md`, Phase 10.5, a new item (f)

**Find:**

> Record the results in the colophon. **This is where the overview's highest-risk claims are made:**

**Replace with:**

> **(f) Every allusion rated above *moderate* carries a rarity count and a rival search.** Count how many verses of the Hebrew Bible contain its shared lemma set (`contacts.py all <lemmas>`; `--window 1` for a pair that straddles two verses), and name every text that shares the set as closely as the claimed source, or more closely. The row states the count ("two verses in the Hebrew Bible", "nine verses") and names the rivals. **An allusion whose wording occurs in more than about ten verses is idiom, and may not be rated above *moderate* on wording alone.** An allusion with an equal or closer rival is rated against the rival, not in isolation. Record the results in the colophon. **This is where the overview's highest-risk claims are made:**

### AB3 — `book-overview/references/deliverables.md`, §4, after point 5 of the sweep list

**Find:**

> 5. Mark **live sources** — any source used **two or more times**; dig-deeper gives further echoes from a live source an elevated prior.

**Replace with:**

> 5. Mark **live sources** — any source used **two or more times**; dig-deeper gives further echoes from a live source an elevated prior. **A use counts towards "live" only if it survives the rival search** (Phase 10.5 (f)). Two uses that are each pooled idiom do not make a live source.
> 6. **Run the density scan and account for its top ten** (Phase 5). Add a column to the table, or a line under it, giving each row's **rarity count** (verses in the Hebrew Bible sharing the lemma set) and its **closest rival**.

---

## Amendment AC — wording shape, and rows verified verse by verse

### AC1 — `book-overview/SKILL.md`, Phase 10.5 item (a)

This edit **appends** a sentence to item (a), after its last sentence. It does not touch the ketiv sentence that Round 6's **Z3** corrects, so the two rounds can be applied in either order.

**Find:**

> A reference that fails is removed from the chain or the chain restated — never hedged and left standing. (b) Every count names its edition.

**Replace with:**

> A reference that fails is removed from the chain or the chain restated — never hedged and left standing. **A row that cites a lemma at several verses is verified at each verse separately, never as a set:** the Lamentations overview cited פְּרִי ("fruit") at 2:20 and 4:10 when it stands at 2:20 only. **And the words *identical*, *verbatim*, *the same phrase* and *only* are claims about shape, which a lemma check cannot verify.** They are licensed only by an *ordered* phrase search, run plain and skeletal (`contacts.py phrase "<words>"`). Where the lemmas match but the phrase does not, the row says *reordered* or *partial*. Where two words share a root but not a lemma (מְרוֹרִים against מַמְּרֹרִים, "bitterness"), the row says *cognate*. Ps 143:3 is not "identical" to Lam 3:6: its first two words are reversed. (b) Every count names its edition.

---

## Amendment AD — design claims and superlatives

### AD1 — `book-overview/SKILL.md`, Phase 10.5, a new item (g)

Insert immediately after the new item (f).

> **(g) A design claim is capped at *moderate* until a chance baseline has been run, and a superlative is barred unless it was measured.** A design claim is any claim about a *pattern* rather than a reference: a "live source", a structure (chiasm, concentric frame, panels, inclusio built from vocabulary), a "handoff", a programme of allusion. The baseline asks whether the pattern occurs more often than it would by chance: for example, by comparing the claimed pairing of two sections against every other pairing; by reshuffling verses into pseudo-sections of the same size; or by ranking the claimed partner against every chapter or window of comparable size (`contacts.py scan`). **Superlatives** — *the densest*, *the closest*, *every one*, *the only*, *anywhere in the canon* — state a measurement. They may be used only when the measurement was made, and the row gives it ("first of 858 chapters"). A design claim that has not been baselined is stated as a proposal, tagged `[I]`, and named in the colophon as a first target for the claim audit. In the Lamentations audit, all seven design claims needed reframing while every exclusive single link held.

### AD2 — `book-overview/SKILL.md`, Consistency Contract

**Find:**

> 7. Where a judgement is genuinely contested (a structural seam, a disputed occasion), show the options and flag confidence rather than asserting one.

**Replace with:**

> 7. Where a judgement is genuinely contested (a structural seam, a disputed occasion), show the options and flag confidence rather than asserting one.
> 8. **Never state a pattern, a superlative or a "live source" more confidently than its baseline allows** (Phase 10.5 (f)–(g)). Single exclusive links are where an overview is reliable; synthetic claims are where it is not, and the colophon names them as the claim audit's first targets.

### AD3 — `book-overview/references/deliverables.md`, §2 (the binding device) and §8 (the handoff)

**Find (§2):**

> - Name the **binding device**: linear build, bookends (inclusio), sandwich, chiasm (centre = point), or thematic panels.

**Replace with:**

> - Name the **binding device**: linear build, bookends (inclusio), sandwich, chiasm (centre = point), or thematic panels. **Keep formal evidence and lexical evidence apart.** Formal evidence — acrostic order, verse counts, refrains, superscriptions — is `[T]`. A lexical symmetry ("sections 2 and 4 answer each other") is a design claim, capped at *moderate* until it beats a baseline (Phase 10.5 (g)). Evidence offered for a pairing must be **exclusive to that pairing**: אֵיכָה ("How!") at Lam 1:1, 2:1 and 4:1 cannot pair poems 2 and 4 against poem 1.

**Find (§8, the *Handoff* row):**

> | **Handoff** | what it passes to what follows |

**Replace with:**

> | **Handoff** | what it passes to what follows — **thematic unless shown otherwise**. A *lexical* handoff ("book X takes up this book's language") is a design claim and needs its rivals named. A book is not a lexical partner if other texts share as much with it. |

---

## The new tool: `_texts/tools/contacts.py`

`find.py` answers one question: *is the word there?* `contacts.py` answers the three questions this round adds. It uses `find.py`'s lemma matcher unchanged.

| Command | Question | Example (WLC) |
|---|---|---|
| `contacts.py all <lemmas> [--window n]` | How rare is this set? Which verses contain all of it? | `all 5375 6440 2205 2603` → Deut 28:50, Lam 4:16 (2 verses) |
| `contacts.py phrase "<words>"` | Is it really verbatim, in this order? Plain and skeletal passes | `phrase "במחשכים הושיבני"` → Lam 3:6 only — **Ps 143:3 has the words reversed** |
| `contacts.py scan <Book>[:ch-ch] [--k 5] [--top 20]` | Which chapters of the Hebrew Bible share the most rare vocabulary with this book or block? | `scan Lam:1-2` → 1. **Jer 14** (1.045), 2. Nah 3, 3. Isa 47, 4. Isa 52, … 8. Jer 8, 9. Jer 6, 10. Isa 51 — of 858 chapters, in about a second |

**Definition.** A *rare contact* is a pair of content lemmas that occurs in a verse of the target and in a verse of the comparison chapter, and in no more than *K* verses of the whole Hebrew Bible (default K = 5). The 24 commonest lemmas (each found in more than 1,500 verses) are excluded. Density is rare pairs per verse of the comparison chapter.

**What it cannot do — and the tool's docstring says so:**

- it cannot see a pair that straddles two verses (use `all --window 1`);
- it does not score a single rare word;
- it does not score syntax or sound;
- it measures shared vocabulary, not borrowing;
- it is Hebrew only — an NT scan against Swete is a candidate for a later round.

**Validation on this draft.**

- `all` reproduces `find.py` on the Ruth חֶסֶד ("lovingkindness") control (1:8; 2:20; 3:10) and on Exod 40:34/35.
- `scan Lam:1-2` reproduces, independently, the Latter-Prophets ranking the Lamentations audit's Auditor B built with a separate script: Jer 14 1.045, Nah 3 0.737, Isa 47 0.733.
- `all 4307 3629 --window 1` reproduces the Job 16:12 ~ Lam 3:12 pair, which straddles two verses on each side.

---

## How the rounds fit together

- **Round 6 (Z, AA) is drafted but not installed.** The installed `book-overview/SKILL.md` still quotes the old ketiv figures ("one verse in six"; "Ezra, 52.9 %"). AC1 appends to item (a) *after* that sentence, so Z3 and AC1 apply cleanly in either order. **Both rounds can go into one `.skill` package.**
- **`dig-deeper` already has the design rule for sweeps** (Multi-Passage Sweep Mode, item 5: "a design claim built on a lexical distribution needs a chance baseline before it can be a headline"). AD gives the overview the same rule. No `dig-deeper` edit is needed this round. A one-line pointer to `contacts.py` in `dig-deeper`'s Phase 10.5 (e3) would be natural, but it is left for a later round so that this one stays small.
- **The positive-control rule (Round 5, Y) is on trial**, and this run supports keeping it: every nil and "only" in the audit carried a control, and none failed.

---

## Trial and withdrawal

**Adopt AB, AC and AD on trial for the next two book overviews.** Withdraw an item if its checks add work to two overviews without changing a single rating or row in either. **AC is the least likely to be withdrawn**: it would have changed three rows of the Lamentations overview at a cost of about one command each.

---

## Verification done on this spec

- **Every find string was matched against the installed files on 3 October 2026:** `book-overview/SKILL.md` (Phase 5 row; Phase 10.5 item (a) and its closing sentence; Consistency Contract item 7) and `references/deliverables.md` (§2 binding-device bullet; §4 point 5; §8 *Handoff* row).
- **Every figure quoted is from the Lamentations claim audit or was re-run for this draft:** 858 chapters; Jer 14 1.045; the Ps 143:3 order; the four-lemma Deut 28:50 set.
- **Not done:** the `.skill` package has not been built, and nothing is installed. Per the standing check, after installing, diff the installed `SKILL.md` against the intended text before treating the round as finished.

---

## Consequential edits outside the skills

1. **Copy `contacts.py` into `_texts/tools/`** and add three lines to `_texts/README.md` § *Using it*.
2. **Lamentations overview v0.2.0** — apply the claim audit's propagation table. That already does, by hand, what AB–AD would have done mechanically.
3. **Job overview** — its Lam 3 row holds on 3:12 and 3:30, but only partly on 3:7–9 (Hos 2:6 [Heb 2:8] rivals). Add a note at its next upgrade.
