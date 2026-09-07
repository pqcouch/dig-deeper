# Transliteration and Greek Chain Audit

**Mode:** Claim Audit — pass 2, completing the folder
**Date:** 4 September 2026
**Scope:** all 131 documents — the 124 Old Testament documents plus the John, Philippians, Acts, Matthew, Luke, 1 Peter and 2–3 John sets
**Substrate:** `_texts/hebrew-wlc/` (WLC with lemma index), `_texts/greek-nt-sblgnt/` (SBLGNT with MorphGNT parsing)
**Bridge:** TBESH — Tyndale Brief Lexicon of Extended Strongs for Hebrew (CC BY) — mapping transliteration to Strong's numbers
**Follows:** `dig-deeper-ot-chain-audit` (2 September), which covered Hebrew-script claims only

---

## Headline findings

**1. One real error, and it carries a "verified" tag.** The John gathering-thread statistic — *"συνάγω 4× / σκορπίζω 3× in John"* — is wrong on both counts. συνάγω occurs **7** times; σκορπίζω occurs **2**. The claim stands in two documents, and in one of them it is marked as verified.

**2. Two load-bearing claims verified exactly, independently.** Isaiah's "Holy One of Israel splits 12/13 across chapters 1–39 and 40–66" is precisely right: 25 occurrences of the construct phrase, 12 before chapter 40 and 13 after. John's σημεῖον count of 17 is exactly right, and its δαιμόνιον list — six occurrences at 7:20; 8:48, 49, 52; 10:20, 21, every one an accusation — is right to the verse.

**3. No error at all in the Greek documents' presence claims.** All 38 Greek-script failures were artefacts of the checker: reference pairing, inflected form against lexical form, compound against simplex, and one case where `κατ᾽ ὄνομα` was cut at the apostrophe. The John, 1 Peter and 2–3 John documents come out clean.

**4. No new error in the Torah.** This pass was commissioned because the Torah's lexical work is transliterated and pass 1 could not reach it. It reached it, and found nothing. That is a genuine result, but a qualified one — see the limitations below, which matter more here than anywhere else in this report.

**5. Counting claims proved far more productive than presence claims.** Every real finding in this pass came from checking a *number*, not from checking whether a word sits at a verse. Presence claims in transliteration are hard to check and mostly came back either weak or falsely failed. **A stated count is the most auditable thing a report can contain**, and the method should lean on that.

---

## What was checked

| | |
|---|---|
| Documents in scope | 131 |
| Documents yielding claims | 109 |
| Claims extracted | 2,531 |
| — transliterated Hebrew | 1,821 |
| — Hebrew script | 432 |
| — Greek script | 278 |
| Word-to-reference checks | 3,141 |
| Verified present | 627 |
| Verified, but the quoted form is ambiguous enough that the hit proves little | 1,702 |
| Verified at a neighbouring verse, consistent with English/Hebrew versification | 133 |
| Near miss, not explained by versification | 103 |
| Cross-testament (a Hebrew word cited at a New Testament reference, or the reverse) — out of scope | 347 |
| Failed | 194 |
| Unresolvable to any lemma | 13 |
| **Failures examined by hand** | **51 — all 38 Greek, all 3 tight transliteration, 10 sampled fuzzy** |
| **Real errors found among them** | **0** |
| **Real errors found by count-checking** | **1** |

---

## The error

### John: the gathering thread's statistics

> `book-overview-john.md` — "Develops — **συνάγω 4×, σκορπίζω 3×**, εἰς ἕν at 11:52; 17:21, 23 | high"
>
> `dig-deeper-john-10-1to21.md` — "συνάγω 4× / σκορπίζω 3× **in John** (verified `[S…`"

**Counted against the SBLGNT:**

| Lemma | Claimed | Actual | Where |
|---|---|---|---|
| συνάγω | 4× | **7×** | 4:36; 6:12; 6:13; 11:47; 11:52; 15:6; 18:2 |
| σκορπίζω | 3× | **2×** | 10:12; 16:32 |
| διασκορπίζω | — | 1× | 11:52 |

Two distinct faults. **συνάγω** is undercounted: four is the number of occurrences *inside the thread being traced*, not the number in the Gospel, but the claim says "in John". **σκορπίζω** is overcounted because 11:52's scattering is **διασκορπίζω**, a compound with its own lemma — the simplex and the compound have been added together.

The thread itself is untouched. 6:12 → 10:12, 16 → 11:52 → 16:32 → 17:21–23 is a real and well-observed sequence, and 11:52 genuinely holds both a gathering and a scattering. What fails is the statistic offered as its warrant, in a table cell whose confidence column reads "high" and whose sibling document calls it verified.

**Fix:** either restate as "συνάγω 7× in John, four of them in this thread; σκορπίζω 2×, with διασκορπίζω at 11:52", or drop the numbers and keep the verse sequence, which was never in doubt.

**One trivial companion.** παροιμία is given as "3× at 10:6; 16:25, 29". The verses are right; the occurrences are four, because 16:25 carries it twice. A verse count offered as an occurrence count.

---

## Claims verified exactly

Worth recording, because a claim audit that reports only faults gives a false picture of the work.

| Claim | Source | Verified |
|---|---|---|
| "Holy One of Israel splits 12/13 across chs 1–39 and 40–66" | Isaiah overview | **Exact.** 25 occurrences of קְדוֹשׁ יִשְׂרָאֵל; 12 in chs 1–39, 13 in chs 40–66 |
| σημεῖον occurs 17 times in John | John overview | **Exact** |
| δαιμόνιον occurs 6 times, every one an accusation against Jesus (7:20; 8:48, 49, 52; 10:20, 21) | John overview | **Exact, to the verse** |
| παραβολή occurs 0 times; μετανοέω occurs 0 times | John overview | **Exact** |
| Sheol: "five occurrences" across Proverbs 1–9 (1:12; 2:18 *rĕpāʾîm*; 5:5; 7:27; 9:18 *rĕpāʾîm*) | Proverbs 1–9 dig | **Right as scoped.** Note that שְׁאוֹל occurs 9× in the whole book, so the sentence reads as a book-level count unless the section scope is held in view |

The Isaiah result deserves a note. That claim is load-bearing for the whole Isaiah overview and is tagged `[T]`. It was made by a run working from supplied BHS exports, and it survives an independent machine count of the construct phrase without a single verse of drift.

---

## Limitations — and they are larger here than in pass 1

**The bridge under-confirms.** Transliteration is lossy in ways Hebrew script is not. SBL writes a mater lectionis as a vowel mark (*bəʿênāyw*) where the lexicon writes the consonant (*a.yin*); aleph and ayin are dropped by the lexicon's own scheme; construct endings, verbal prefixes and pronominal suffixes all have to be peeled by guesswork. Each fallback widens the candidate set, so **1,702 of 3,141 checks came back "weak"** — the word was found, but among so many candidate lemmas that finding it proves little.

**Therefore the failures are dominated by artefacts, and absence of a finding is not proof of correctness.** Of 51 failures examined by hand, 51 were faults in the checker. That is reassuring about the reports and damning about the checker's precision, and it means this pass **cannot certify the Torah clean**. It can say only that it surfaced nothing — which is weaker, and is what the headline says.

**Known checker faults, recorded so a future pass starts ahead of this one:**

| Fault | Example |
|---|---|
| Nearest-reference pairing still mis-assigns in dense clauses | "*mĕzimmâ* (1:4)→*zāmĕmâ* (31:16)" — the second word drew the first reference |
| Inflected forms not matched to lexical entries | συναγαγεῖν against lemma συνάγω; ἑλκύω against SBLGNT's ἕλκω |
| Compounds not related to simplexes | διασκορπίζω against σκορπίζω |
| Apostrophes cut tokens | `κατ᾽ ὄνομα` became `κατ` |
| "MT" read as an abbreviation for Matthew | "= MT 17:5's" in the Jeremiah sweep resolved to Matt 17:5 |
| Greek transliterations treated as Hebrew | *hilastērion*, *typos* looked for in the Hebrew text |
| Waw-prefixed verbs missed after the waw is normalised to b | *wayyaḥšĕbehā* at Gen 15:6 — present, reported absent |

**Negative claims read as positive.** A report saying a word is *distinct from*, or *against*, or *not at* a verse is making the opposite claim to the one tested. Several failures were reports being careful.

---

## What this changes

**Nothing about re-running the digs.** Pass 1 found four errors, all in one document. This pass found one, in a different document, and it is a corrigible sentence rather than a flawed argument. Two audits across 131 documents have produced five errors, none of which requires a re-run.

**Something about the method, though.** The most auditable claim a report can make is a **count** — and counts are exactly where both this pass's real finding and pass 1's cleanest finding came from. Amendment C in `dig-deeper-skill-amendments.md` requires chains to be verified; on this evidence it should also require that **every stated count name its edition and be reproducible**, since a count is the one claim a later reader can check in a single command.

The corollary is uncomfortable and worth stating: **the word "verified" in a report is not itself evidence.** The John statistic carries it, and is wrong.

---

## Reproducing this

```
python3 _texts/tools/translit.py          # rebuild the bridge
python3 _audit/extract_verify_v2.py       # extract and verify
```

| File | Contents |
|---|---|
| `_texts/_bridge/translit-to-strongs.tsv` | 3,558 skeletons mapped to Strong's numbers |
| `_texts/_bridge/strongs-info.tsv` | Strong's, Hebrew, transliteration, gloss |
| `_audit/04-claims-v2.tsv` | 2,531 extracted claims with context |
| `_audit/05-verdicts-v2.tsv` | 3,141 checks with verdicts |

---

*Prepared with the Dig Deeper toolkit in Claim Audit Mode, 4 September 2026. Every failure reported as an error was read in its own context and counted against the primary text. Confirmation by the originating run was not accepted as evidence.*
