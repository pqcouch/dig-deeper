# Claim Audit 3: Lamentations

**Passages audited:** 3:1–33 and 5:1–22, plus single contacts in chs 2 and 4. These are queue items **L16–L33** (18 claims), raised by:

- claim audit 2 (L16–L20);
- the solo dig on 3:1–33 (L21–L27);
- the solo dig on 5:1–22 (L28–L33).

**Date:** 4 October 2026
**Purpose:** to test the two solo digs' design and allusion claims before any sermon outline is written on either passage. Queue trigger 1 had fired on both limbs (19 queued; 2 digs since the last audit), and trigger 2 was armed for both passages.

**Documents under test:**

- `dig-deeper-lamentations-3-1to33.md` and `dig-deeper-lamentations-5-1to22.md` (4 October 2026);
- `dig-deeper-lamentations-claim-audit-2.md`, for its new-candidate list;
- `book-overview-lamentations.md` v0.2.1, where the claims touch it.

**Not re-tested:** L1, the direction of dependence between Lamentations and Jer 14. That is a question for the library, not for a lemma count.

**Primary texts:**

- **WLC Hebrew** with the lemma index, for every count (the matcher is identical to `find.py`).
- **Swete LXX**, for observation.
- **The Rahlfs LXX and BHS apparatus** (Logos exports), as the citation of record.

**Every count below is a WLC lemma or phrase count unless stated.** References are in English numbering, with the Hebrew in brackets where it differs.

Warrant tags: `[T]` derivable from the text itself · `[I]` a reasonable inference from the text · `[S]` supplied by a secondary source, held provisionally · `[S: audit]` a verdict of this or an earlier audit.

---

## What this audit tested, and how

**Three blind auditors, run one after another.** None of them saw:

- the digs or the overview;
- the earlier audits;
- each other's reports.

Each received a neutral brief, the claims restated, the staged corpus, the shared lemma library (`alib.py`) and the draft density scanner (`contacts.py`). Each was told to try to **break** the claims.

| Auditor | Claims | Kind |
|---|---|---|
| **A** | L25, L26, L28, L29, L33 | **Design** claims, each tested against a chance baseline. Selection effects were tested explicitly |
| **B** | L16, L20, L23, L30, L32 | Prophets: Jer 31:18–20; the cup; Isa 54:7–8; Isa 53:11 and Jer 14:20–21; Amos 8 |
| **C** | L17, L18, L19, L21, L22, L24, L27, L31 | Psalms and the Writings: Zeph 3; Ps 44; Ps 119; Ps 88; Ps 10; Ps 89 and Isa 63:7; the חֶסֶד ("lovingkindness") chiasm; Ps 125 |

**Method for each claim:**

1. Check the wording on both sides in Hebrew and Greek.
2. Count how rare the shared lemma set is, using `hall`.
3. Search for rival sources.
4. Run a chance baseline for any design claim.
5. Score the seven Hays criteria. "History of interpretation" is "not checked" throughout, because no commentary was consulted.
6. Give a verdict and a recommended confidence.

**Positive controls** were run before every nil or "only" result.

**The main session's gate.** Twenty-two spot checks from the auditors' lists were reproduced. Among them:

- Ps 102:13 alone with Lam 5:19;
- Ps 42:5, 7 with Lam 3:20 (±1 verse);
- Ps 88:9 with Lam 3:7;
- Isa 52:11 with Lam 4:15;
- Ps 119:136 with Lam 3:48;
- סבל ("bear") + עָוֹן ("iniquity");
- הפך ("turn") + אֵבֶל ("mourning") + מָחוֹל ("dance");
- זנח ("reject") + עוֹלָם ("for ever");
- חֶסֶד + רחם (the verb, "have compassion");
- Ps 89:43 with Lam 2:17;
- Ps 89:5 with Lam 5:19;
- Ps 92:3 with Lam 3:22;
- Ps 10:9 with Ps 17:12;
- the A2 baseline (Psalms 21 / 694 windows ≥4);
- the A3 selection test;
- the B1 doubled-figure baseline;
- the C3 alphabet test.

**Length.** The three reports run to about 4,100, 4,800 and 5,300 words, over the 3,500-word guide; the excess is mostly glosses and tables. Nothing has been trimmed from the findings. The reports and their scripts are kept in `/home/claude/lamaudit3/`.

---

## Summary

**The single verse contacts hold again. Every design claim made by the two solo digs comes down to low or low–moderate once a baseline is run.** The two digs' strongest *designs* turn out to be:

- **the Jer 31:18–20 cluster**, at moderate–high;
- **Ps 89**, at moderate–high — but at different points from those claimed.

| # | Claim | Verdict | Recommended confidence |
|---|---|---|---|
| L16 | Jer 31:18–20 behind 3:20 and 5:21 (the doubled-verb figures) | **Confirmed with nuance** | moderate–high |
| L17 | Zeph 3 the densest partner of Lam 4 | **Confirmed with nuance** (as a ranking only) | moderate for the rank; low–moderate for any borrowing |
| L18 | Ps 44:24–25 behind 5:20 | **Needs reframing** | low–moderate |
| L19 | Ps 119:49–57 behind 3:19–24 (same letters) | **Needs reframing — broaden** | moderate–high that the two acrostics are related, through exact phrases at the same letters (ח 3:24; פ 3:48; ר 3:58) |
| L20 | Jer 25:15–29 leads the cup at 4:21 | **Needs reframing** | moderate (Jer 25); low–moderate (Hab 2:16); **add Isa 51:22–23** |
| L21 | Ps 88 a multi-contact partner of Lam 3 | **Confirmed with nuance — strengthened** | moderate–high |
| L22 | Ps 10:9 behind 3:10 | **Confirmed with nuance** | moderate (a composite image) |
| L23 | Isa 54:7–8 behind 3:31–32 | **Needs reframing** | low–moderate; **Ps 77:8–10 is closer** |
| L24 | Ps 89:2 (or Isa 63:7) behind 3:22 | **Needs reframing** | moderate (Isa 63:7); low–moderate (Ps 89:2); Ps 92:3 an equal rival |
| L25 | **Design:** 3:1–16 built from the enemy's images | **Needs reframing** | links high; design low–moderate |
| L26 | **Design:** 3:17–33 answers the "reject for ever?" psalms | **Needs reframing** | moderate–high (3:31 ~ Ps 77:8); low (the four-psalm cluster) |
| L27 | (a) Ps 44 behind 3:17–20; (b) חֶסֶד chiasm 3:22 ↔ 3:32 | **Needs reframing** | (a) low — **Ps 42–43 is the partner** (moderate–high); (b) keep as an observation, drop as design (low–moderate) |
| L28 | **Design:** Isa 54:4–9 answers Lam 5 (seven roots) | **Needs reframing** | low (design); moderate (Isa 54 as a thematic counterpart) |
| L29 | **Design:** Lam 5 prays Jer 31 in reverse, in order | **Needs reframing** | moderate–high (the pairing); low ("in order") |
| L30 | Isa 53:11 behind 5:7; Jer 14:20–21 behind 5:1, 7, 16, 19 | **Split** | Isa 53:11: **Uncertain — low**. Jer 14:19–21: **Confirmed with nuance** — moderate–high |
| L31 | Ps 125:1 behind 5:18–19 | **Needs reframing** | low (Ps 125); **high that Ps 102:13 is the closest wording** |
| L32 | Amos 8:7–13 the threat fulfilled in 5:14–17 | **Needs reframing** | low–moderate |
| L33 | Ps 89 heard at three points | **Confirmed with nuance** | moderate–high, at **2:7, 2:17, 5:1, 5:19**; low–moderate at 3:22 |

| Verdict | Count |
|---|---|
| Confirmed | 0 |
| Confirmed with nuance | 6 (L16, L17, L21, L22, L33, and the Jer 14 half of L30) |
| Needs reframing | 12 (L18, L19, L20, L23, L24, L25, L26, L27, L28, L29, L31, L32) |
| Uncertain | 1 (the Isa 53:11 half of L30) |
| Discard | 0 as whole claims. **Withdrawn as arguments:** the seven-root "only other passage" (L28); "in Jer 31's order" (L29); the four-psalm cluster (L26); the חֶסֶד chiasm as design (L27b); Ps 125's "transfer" as allusion (L31) |

---

## Claims Audited

### Design claims (Auditor A)

#### L25 — 3:1–16 "built from the enemy's images, now applied to God"

**What holds.**

- God is the implied subject of 24 finite verbs in 3:2–16, and YHWH is first named at 3:18.
- Two exclusive contacts:
  - 3:10 ~ Ps 10:9 (ארב, "lie in wait" + אַרְיֵה, "lion" + מִסְתָּר, "hiding place");
  - 3:6 ~ Ps 143:3 (verbatim, with the first two words reversed). `[T]`
- **Missed:** Ps 17:12 is a third partner for 3:10 with a wicked subject. אַרְיֵה + מִסְתָּר occurs in Ps 10:9, Ps 17:12 and Lam 3:10.

**Baseline.** Each block's rare-partner images were classified by the partner's agent. The auditor's classification list is in `a1_classification.txt`.

| Block | Partners whose agent is the enemy or the wicked |
|---|---|
| Lam 3:1–16 | 2 of 7 |
| Lam 2:1–8 | 6 of 28 |
| Job 16:7–17 | 2 of 3 |
| Lam 1:12–16 | 0 of 10 |
| Ps 88 | 0 of 4 |

**Describing God in images belonging to an enemy is ordinary in these laments, not distinctive of Lam 3.** Lam 3's own rare partners split evenly with passages in which God is the agent. Job 19:6–12 is the closest overall rival (13 shared content words). `[T]` for the counts; the classification is the auditor's and should be re-checked.

**Verdict: Needs reframing.** Keep the two contacts (high) and add Ps 17:12. Drop "the assault is *composed from* the enemy's images" as a design claim (low–moderate). Preach it as what the man *says*: he uses of God the words the psalms use of the wicked. Do not claim that the poet built the stanza that way.

#### L26 — 3:17–33 "replies to the 'reject for ever?' psalms (44, 74, 77, 88)"

**What holds.** **3:31 is a near-verbatim answer to Ps 77:8 [Eng 77:7].** זנח ("reject") + עוֹלָם ("for ever") occurs only in these two verses, and the Greek is near-identical: μὴ εἰς τοὺς αἰῶνας ἀπώσεται κύριος / οὐκ εἰς τὸν αἰῶνα ἀπώσεται κύριος ("will the Lord cast off for ever?" / "the Lord will not cast off for ever"). *Moderate–high.* `[T]`

**What fails.**

- **The cluster.** Lam 3:17–33 shares only 3 rare word-pairs with the four psalms.
  - Across the Hebrew Bible this is unusual: 1.26 % of 17-verse windows reach 3.
  - Within Lamentations it is not: 17 of 74 windows reach 3, and **Lam 1:1–17 scores 5**.
  - In the Psalter, 21 of 694 windows reach 4.
  - **Lamentations as a whole is dense in this psalm-family; 3:17–33 is not singular.**
- **Errors in the claim as worded:**
  - 3:8 (the Ps 88:14 contact) lies outside the block.
  - 3:18 נִצְחִי means "my endurance", not "for ever"; so the זנח + לָנֶצַח ("reject … for ever") window at 3:17–18 is a homonym hit.
- **Missed: Ps 42–43** (see L27a).

**Verdict: Needs reframing.** 3:31 ~ Ps 77:8 is moderate–high; the four-psalm "dialogue" is low.

#### L28 — "Isa 54:4–9 answers Lam 5: the only other passage with all seven roots of address"

**Reproduced.** With roots grouped (אַלְמָנָה / אַלְמָנוּת, "widow / widowhood"; קצף / קֶצֶף, "be angry / anger"):

- Isa 54:4–9 holds all seven;
- no other six-verse window holds ≥ 5;
- at 22 verses, only Isa 54 and Lam 5 hold ≥ 5.

**Selection effect.** The seven roots were chosen *from* Lam 5, after the two texts had been read together. The choice was principled (the words of address to God), but it was still made after the fact.

Auditor A took the 40 content roots of Lam 5 that fall in the same frequency band as the seven:

- **Fourteen six-verse windows outside Lam 5, in 7 chapters, hold ≥ 7 of them.** Jer 14:16–21, Hos 4:5–10 and Lam 2:16–21 hold 8.
- By plain lemma (without the grouping), Isa 54:4–9 holds only 6, and is not the best.
- **Control poems behave the same way:**

  | Control poem | Six-verse windows elsewhere holding ≥ 7 of its band roots |
  |---|---|
  | Ps 74 | 51 windows in 23 chapters |
  | Isa 63:15–64:11 | 16 windows in 7 chapters |
  | Ps 79 | 7 windows in 2 chapters |

- **Randomly drawn seven-root sets almost never match:** 0 of 1,000 reach ≥ 6 roots.
- **So the uniqueness is produced by choosing the roots after looking.** `[T]`

**Further points.**

- **Subject.** In Isa 54:4 it is the woman who forgets and does not remember her shame. God is not the subject, which is the reverse of Lam 5:1 and 5:20.
- **Greek.** Five of the seven roots survive in Greek; מאס ("reject") and קצף ("be angry") are rendered differently.
- **Sharper partners for 5:20–22:**
  - **Isa 64:8 [Eng 64:9]** — קצף + עַד + מְאֹד ("be exceedingly angry") is exclusive with Lam 5:22, and Isa 64 ranks 1st of 858 chapters against Lam 5;
  - **Jer 14:19** — the doubled מאס ("utterly reject") is exclusive with Lam 5:22;
  - Isa 54 ranks 24th.

**What Isa 54 still holds.**

- **Isa 54:8 ~ Lam 3:32** — חֶסֶד + רחם (verb) + עוֹלָם within a one-verse window; exclusive. *Moderate.*
- Isa 54:1 שׁוֹמֵמָה ("desolate one") and Isa 54:11 לֹא נֻחָמָה ("not comforted") touch Lamentations' vocabulary.

**Verdict: Needs reframing.** Withdraw "the only other passage" as evidence of design. Keep Isa 54 as a thematic counterpart (moderate), with one exclusive tie at 3:32. Name Isa 64:8 and Jer 14:19–21 as Lam 5's closest verbal partners.

#### L29 — "Lam 5 prays Jer 31 in reverse, in Jer 31's order"

**The pairing is strong.**

- **Jer 31 is the only chapter of 858 with ≥ 5 rare word-pairs shared with Lam 5.** The mean is 0.13.
- **Two contacts are exclusive:**
  - **5:15 ~ 31:13** — הפך ("turn") + אֵבֶל ("mourning") + מָחוֹל ("dance");
  - **5:21 ~ 31:18** — the doubled שׁוב ("restore … return").
- Jer 31:13 also shares virgins, young men and old men with Lam 5:11–14. `[T]`

**The order argument fails.** Only 3 of the 5 contacts run in sequence, which happens by chance about 65 % of the time.

**Two further problems:**

- **5:7 ~ 31:29** shares only "father". Jer 14:20 and Ezek 18:20 are stronger partners for 5:7.
- **3:20 ~ 31:20** belongs to Lam 3, not Lam 5, and Deut 7:18 has the same doubled form.

**Verdict: Needs reframing.** "Lam 5 is the negative image of Jer 31:13 and 31:18" is moderate–high. "In order" is low and is withdrawn.

#### L33 — "Ps 89 heard at three points"

**The links.**

- The three wording claims are confirmed, but **the strongest points are not the ones claimed**.
- Ps 89 has **three exclusive multi-lemma ties** with Lamentations:

  | Ps 89 | Lamentations | Exclusive set |
  |---|---|---|
  | 89:39–40 | **2:7** | נאר ("spurn"), and זנח + נאר ("reject … spurn") within one verse |
  | **89:43** [Eng 89:42] | **2:17** | רום ("raise") + צַר ("adversary") + שׂמח ("make glad") + אוֹיֵב ("enemy") |
  | **89:5** [Eng 89:4] | **5:19** | כִּסֵּא ("throne") + דּוֹר וָדוֹר ("generation and generation") + עוֹלָם ("for ever") — David's throne in the psalm, the LORD's in Lamentations |

- Lam 5:1 ~ Ps 89:51 ("remember … reproach") is closer in Greek than in Hebrew: Μνήσθητι, κύριε … ὀνειδισμοῦ ("remember, Lord … reproach").

**Baseline.**

- **On exclusive ties only, two of 150 psalms reach three points: Ps 89 and Ps 55.** Among long psalms, Ps 78 has 1, and Ps 18, 22 and 106 have none.
- On looser criteria, three points is ordinary (29 of 150 psalms); Ps 89 ranks 3rd.

**3:22 demoted.** Isa 63:7 and **Ps 92:3 [Eng 92:2]** are equal rivals at 3:22. Ps 92:3 is the only other verse with חֶסֶד ("lovingkindness") + אֱמוּנָה ("faithfulness") + בֹּקֶר ("morning") within one verse. And 3:22–24 is absent from the Greek.

**Verdict: Confirmed with nuance.** Ps 89 is a live source for **Lam 2 (2:7, 2:17) and Lam 5 (5:1, 5:19)**, moderate–high. The 3:22 point is low–moderate.

### Prophets (Auditor B)

#### L16 — Jer 31:18–20 behind 3:20 and 5:21

- **The two contacts:**
  - the doubled שׁוב ("restore … return") is exclusive to Jer 31:18 and Lam 5:21;
  - the doubled זכר ("remember") occurs at Deut 7:18, Jer 31:20 and Lam 3:20.
- **Lamentations has seven doubled-verb figures.** Four have same-figure partners elsewhere, and **all four have a partner in Jeremiah**.
- **Jer 31:18–20 is the only three-verse window in the Hebrew Bible holding two of them.** It is also the densest doubled-verb window of all: five figures in three verses.

**Caveats.**

- The 3:20 link depends on whose remembering is meant. The *tiqqun soferim* reading (God as subject) matches Jer 31:20 better.
- The Greek keeps 5:21 and loses 3:20.
- The very next line, 5:22, partners Jer 14:19, not Jer 31.

**Verdict: Confirmed with nuance — moderate–high.**

#### L20 — the cup at 4:21

- **Uz.** עוּץ ("Uz") + אֶרֶץ ("land") occurs in only 3 verses (Job 1:1; Jer 25:20; Lam 4:21). But Jer 25:20 lists Uz *apart from* Edom, while Lamentations places Edom *in* Uz. **The Uz contact is weaker than claimed.**
- **Hab 2:16's** גַּם ("also") + כּוֹס ("cup") is no more than chance.
- **Missed: Isa 51:22–23** — the only other place where the cup passes from Zion to her enemies "no more"; the Greek wording matches Lam 4:22.
- **Also to be named:** Jer 49:12 (the cup to Edom) and **Ps 137:7** (Edom + ערה, "strip bare": 2 verses).

**Verdict: Needs reframing.** Jer 25 moderate; Hab 2:16 low–moderate; **Isa 51:22–23 moderate–high for 4:21–22**.

#### L23 — Isa 54:7–8 behind 3:31–32

- חֶסֶד + רחם (verb) occurs in only 3 verses: Isa 54:8, Isa 54:10 and Lam 3:32.
- With the noun "compassion", or in a one-verse window, it is ordinary covenant language.
- Isa 54:7's "brief moment" has no counterpart in Lamentations.
- **Ps 77:8 [Eng 77:7] is the closer partner:** 3:31 answers its question in its own words.

**Verdict: Needs reframing — low–moderate.** Auditor A rates the 54:8 ~ 3:32 tie moderate; Auditor B rates it low–moderate. **The audit adopts low–moderate to moderate**, and Ps 77:8–10 as the primary partner.

#### L30 — Isa 53:11 at 5:7; Jer 14:20–21 at 5:1, 7, 16, 19

**Isa 53:11.**

- סבל ("bear") + עָוֹן ("iniquity") occurs only at Isa 53:11 and Lam 5:7.
- **But** סבל is a rare synonym within a common idiom: נשׂא ("carry") + עָוֹן occurs in **37 verses**.
- The Greek loses the link (ὑπέσχομεν, "we underwent" / ἀνοίσει, "he will bear").
- The theology runs the other way (complaint / vicarious bearing).

**Verdict: Uncertain — low as an allusion.** It may still be used as **canonical reflection**: "the only other place this verb takes 'iniquities'". But it must not be called an echo.

**Jer 14:19–22.**

- The counts are confirmed:
  - עָוֹן + אָב + חטא ("iniquity + father + sin") occurs in 3 verses;
  - כִּי חָטָאנוּ ("for we have sinned") in 5.
- Jer 14:19 is the sole partner of 5:22.
- Jer 14:19–22 ranks 13th of 20,288 four-verse windows against Lam 5. Isa 64:4–8 ranks higher.
- **Ezek 18:19–20 and Jer 31:29–30** are the texts that *answer* 5:7.

**Verdict: Confirmed with nuance — moderate–high.**

#### L32 — Amos 8 as the threat fulfilled

- הפך ("turn") + אֵבֶל ("mourning") occurs in 4 verses.
- **Jer 31:13 is the closer partner of 5:15** (exclusive with מָחוֹל, "dance").
- **Lam 5:20 inverts Amos 8:7, and so cannot be its fulfilment.** In Amos God swears that he will *not* forget their deeds; in Lamentations the people complain that he *does* forget them.
- Amos 8 ranks 13th–15th of 858 chapters against Lam 5.

**Verdict: Needs reframing — low–moderate.**

### Psalms and Writings (Auditor C)

**One finding cuts across three claims.** Lam 3:22–24 and 3:29 are absent from both Swete and Rahlfs. So 3:24's "my portion is the LORD" (L19), all of L24, and half of L27b have **no Greek witness**. `[T]`

#### L17 — Zeph 3 and Lam 4

- Zeph 3 ranks top at every threshold.
- But **4 of its 8 rare pairs come from one verse pair, Lam 4:11 ~ Zeph 3:8.** Without that pair it falls level with Amos 9.
- Zeph 3 is densely linked to many chapters; its own top partner is Ezek 22.
- **Missed:** Isa 52:11's סוּרוּ סוּרוּ ("depart, depart") is exclusive with Lam 4:15. This is Lam 4's strongest single parallel and is already in the overview `[S: audit]`.

**Verdict: Confirmed as a ranking — moderate; low–moderate as a source.**

#### L18 — Ps 44:24–25 at 5:20

- The count holds.
- But the words straddle two verses in Ps 44, and Ps 44 ranks only 57th of 150 psalms against Lam 5.
- **Stronger partners:**
  - Ps 13:2 (the same verb form);
  - Ps 74 (Zion destroyed);
  - **Isa 49:14** (שׁכח, "forget" + עזב, "forsake", with Zion speaking).

**Verdict: Needs reframing — low–moderate.**

#### L19 — Ps 119 and Lam 3

**The alphabet test.**

- The same-letter excess is largely forced by the alphabet.
- Same-letter against off-letter shared content lemmas: **1.59 against 0.82**.
- **That falls to 0.68 against 0.60** once each line's forced first word is removed.

**What survives is a set of exact phrases found only in these two poems, at several letters:**

| Ps 119 | Lam 3 | Phrase | Rarity |
|---|---|---|---|
| **119:57** | **3:24** | חֶלְקִי יְהוָה ("my portion is the LORD") | **only these two verses** |
| **119:136** | **3:48** | פַּלְגֵי־מַיִם תֵּרַד עֵינִי ("streams of water my eye runs down") | **only these two verses** |
| 119:154 | 3:58 | ריב ("plead my cause") + גאל ("redeem") | 4 verses |

**Verdict: Needs reframing — broaden.** The two great alphabetic poems share exact phrases at several letters. That relation is moderate–high. The ז–ח "slot" correspondence on its own is withdrawn.

#### L21 — Ps 88 and Lam 3

- **Ps 88 ranks 2nd of 150 psalms per verse against Lam 3.**
- **Missed contacts:**
  - **Ps 88:9 [Eng 88:8] ~ Lam 3:7** — וְלֹא אֵצֵא ("and I cannot go out"): only these two verses;
  - Ps 88:6 ~ Lam 3:54 — "cut off".
- **3:6 belongs to Ps 143:3**, which is verbatim. Ps 88:7 shares only מַחֲשַׁכִּים ("dark places").

**Verdict: Confirmed with nuance, strengthened — moderate–high** for 3:7, 3:8, 3:17, 3:54–55.

#### L22 — Ps 10:9 at 3:10

- The triple is exclusive.
- But 3:10 is a **composite**: Ps 17:12 has the same plural "hiding places", and Hos 13:7–8 makes God the predator. The bear is not in Ps 10.

**Verdict: Confirmed with nuance — moderate.**

#### L24 — Ps 89:2 or Isa 63:7 at 3:22

- **Isa 63:7 is the better partner.** It covers both 3:22 and 3:32, and matches the qere.
- חֶסֶד + אֱמוּנָה ("lovingkindness + faithfulness") is ordinary Psalter idiom: 11 verses, all in the Psalms.
- Ps 92:3 is an equal rival (A5).

**Verdict: Needs reframing.** Isa 63:7 moderate; Ps 89:2 low–moderate.

#### L27 — (a) Ps 44 at 3:17–20; (b) the חֶסֶד chiasm

**(a) Ps 44.**

- **The "exclusive" נֶפֶשׁ ("soul") + שׁוח ("sink") pair is an artefact of the lexicon.** The index files the closely related verb שׁחח ("be bowed down") under a different number (7817). Read that way, the partner is **Ps 42–43**:
  - **Ps 42:7 [Eng 42:6]:** עָלַי נַפְשִׁי תִשְׁתּוֹחָח עַל־כֵּן אֶזְכָּרְךָ ("my soul is bowed down within me; therefore I remember you").
  - **Lam 3:20–21:** ותשיח עָלַי נַפְשִׁי … עַל־כֵּן אוֹחִיל ("my soul is bowed down within me … therefore I hope").
  - **Ps 42:6, 12; 43:5:** הוֹחִילִי ("hope!").
- **The counts.**
  - זכר ("remember") + נֶפֶשׁ + יחל ("hope") within ±1 verse occurs **only at Ps 42:5, 42:7 and Lam 3:20**.
  - עָלַי נַפְשִׁי ("within me my soul") occurs in 5 verses.
- **The ketiv and the Greek** (καταδολεσχήσει, "will muse") point instead to Ps 77:4, 7.

**Verdict on (a): Needs reframing.** Ps 44 is low. **Ps 42–43 is moderate–high on the qere**; Ps 77 is moderate on the ketiv and the Greek.

**(b) The chiasm.**

- 21 verses contain both חֶסֶד and רַחֲמִים: 11 in one order, 10 in the other (the Exod 34:6 order).
- The same reversal within 10 verses occurs in 5 other places (Isa 54, Mic 7, Ps 40, Ps 103).

**Verdict on (b): keep as an observation; drop as design — low–moderate.**

#### L31 — Ps 125:1 at 5:18–19

- **Ps 102:13 [Eng 102:12] is the closest wording.** יְהוָה + עוֹלָם + ישׁב ("sit, abide") + דּוֹר ("generation") occurs **only at Ps 102:13 and Lam 5:19**. *High.*
- **Joel 4:20 [Eng 3:20]** carries the "abide for ever / generation and generation" pair of a *place* — "Judah shall abide for ever, and Jerusalem to generation and generation". It is a closer source for the mountain-to-LORD idea than Ps 125.
- The "transfer" from mountain to LORD is a reading of the sequence 5:18 → 5:19, not an allusion to Ps 125.

**Verdict: Needs reframing.** Ps 125 low; Ps 102:13 high; Joel 4:20 moderate.

---

## Supplementary gate

No open test was left by the auditors. Every decisive figure in the summary table was re-run in the main session — the 22 spot checks listed above. Two of them corrected the claims:

- **The Ps 44:26 "exclusive" is a lexicon artefact.**
  - שׁחח ("be bowed down", 7817) + נֶפֶשׁ occurs at Ps 42:6, 42:7, 42:12 and 43:5.
  - זכר + נֶפֶשׁ + שׁחח occurs at Ps 42:7 alone.
  - Lam 3:20's verb is filed as שׁוח (7743).
  - **The two lemma numbers divide one word-family.** Future chains on this root must search both. `[T]`
- **"Remember + soul + hope"** returns nothing at window 0 and **Ps 42:5, 42:7 and Lam 3:20** at window ±1. The claim needs its window stated.

---

## What the audit adds

Every row is verified wording; none is yet audited as design.

1. **Ps 42–43 behind 3:20–24.** "My soul is bowed down within me; therefore …" (Ps 42:7 ~ Lam 3:20–21), with "hope" as the refrain (Ps 42:6, 12; 43:5 ~ Lam 3:21, 24, 26). This is the closest model for the turn. *Moderate–high.*
2. **Ps 88:9 ~ Lam 3:7** — "and I cannot go out", exclusive. With 3:8, 3:17 and 3:54–55, Ps 88 is the leading psalm partner of Lam 3 after Ps 143.
3. **Ps 119:136 ~ Lam 3:48** — "streams of water my eye runs down", exclusive. **Ps 119 and Lam 3 share exact phrases at three letters — ח (3:24), פ (3:48), ר (3:58) — each time in the same letter-slot of both poems.** Each phrase begins with the line's alphabet-forced first word (חֶלְקִי, "my portion"; פַּלְגֵי, "streams"; רִיב, "plead"), but what follows is not forced, and the two-to-four-word phrases occur nowhere else. That is the measure of the relation; the alphabet test alone does not show it.
4. **Ps 89:43 ~ Lam 2:17 and Ps 89:5 ~ Lam 5:19** — exclusive. Ps 89 is a live source for Lam 2 and Lam 5.
5. **Ps 92:3 ~ Lam 3:22–23** — חֶסֶד + אֱמוּנָה + בֹּקֶר ("lovingkindness, faithfulness, morning"), exclusive in a one-verse window.
6. **Isa 51:22–23 ~ Lam 4:21–22** — the cup passed from Zion to her tormentors "no more"; the Greek matches 4:22.
7. **Ps 17:12 ~ Lam 3:10** — "lion … in hiding places".
8. **Joel 4:20 ~ Lam 5:19** — "abide for ever … generation and generation".
9. **Ps 137:7 ~ Lam 4:21** — Edom + "strip bare", exclusive.
10. **Ps 55** reaches three exclusive ties with Lamentations, like Ps 89. Unread; queue.

---

## Confidence Change Propagation

### Into the 3:1–33 dig (v1.0 → v1.1, when patched)

| Location | Current | Corrected |
|---|---|---|
| Headline 2 | "wears the Psalter's pictures of the enemy" (design moderate–high) | **Two exclusive contacts (Ps 10:9; Ps 143:3), plus Ps 17:12. The design claim is withdrawn** (low–moderate): God in enemy imagery is ordinary in these laments. Preach as the man's words |
| Headline 3 | the "reject for ever?" dialogue (moderate–high) | **3:31 ~ Ps 77:8–10 (moderate–high). The turn's closest model is Ps 42–43** (3:20–21, 24). The four-psalm cluster is low. Remove the 3:18 "for ever" reading (נִצְחִי means "my endurance") |
| Headline 4 | חֶסֶד chiasm (moderate–high) | **An observation, not a design** (low–moderate). The pair's order varies freely. The 1:5 → 3:32 tie and the 3:21 ↔ 3:33 "heart" frame stand |
| Tool 11 | Ps 89:2 at 3:22 (moderate); Isa 54:7–8 (moderate–high); Ps 44:24–26; Ps 119 same-slot | Isa 63:7 and Ps 92:3 lead at 3:22; Ps 89:2 low–moderate. Isa 54:8 ~ 3:32 low–moderate to moderate. **Ps 44 replaced by Ps 42–43.** Ps 119: exact phrases at 3:24, 3:48, 3:58. **Add Ps 88:9 ~ 3:7** |
| Positional Necessity (revisited) | "Ps 89 used in both directions" | **Withdraw.** Ps 89 is heard in Lam 2 and Lam 5, not at 3:22 |
| Repetition / Vocabulary | נֶפֶשׁ + שׁוח "only Ps 44:26" | **Lexicon artefact.** Ps 42:6–7, 12; 43:5 (שׁחח) |

### Into the 5:1–22 dig (v1.0 → v1.1, when patched)

| Location | Current | Corrected |
|---|---|---|
| Headline 1 | Isa 54:4–9 the only other passage with all seven roots (moderate–high, "baseline run") | **Withdrawn as design** (selection effect; low). Isa 54 is a thematic counterpart (moderate). **Isa 64:8 and Jer 14:19–21 are the closest verbal partners of 5:20–22** |
| Headline 2 | Jer 31 prayed in reverse, in order | **The pairing stands** (moderate–high: Jer 31 is the only chapter with ≥ 5 rare pairs; 31:13 and 31:18 exclusive). **"In order" is withdrawn.** The 31:29 link is weak (Jer 14:20; Ezek 18:20 stronger) |
| Headline 3 | 5:7 ~ Isa 53:11 "one other home" (high wording) | **Uncertain — low as an allusion** (סבל is a rare synonym; נשׂא + עָוֹן occurs in 37 verses; the Greek loses it). Use as canonical reflection only. Jer 14:19–21 stands (moderate–high) |
| Headline 4 | Ps 125:1 "transfer" (moderate–high) | **Ps 102:13 is the exclusive partner of 5:19** (high). The transfer is a reading of 5:18 → 5:19 (`[I]`), not an allusion. Joel 4:20 is the "place abides for ever" parallel (moderate) |
| Tool 11 | Amos 8 "threat fulfilled" (moderate–high); Ps 44 at 5:20 (moderate–high) | Amos 8 low–moderate (5:20 *inverts* 8:7). Ps 44 low–moderate; **Isa 49:14 and Ps 13:2** for 5:20. **Ps 89:5 ~ 5:19** (exclusive) and Ps 89:51 at 5:1 confirmed |
| Christological Reading | "the bearer of iniquities (5:7 → Isa 53:11) … high on the canonical connection" | **Lower to moderate, as canonical reflection.** The Christological route runs more securely through Jer 31 (5:21 → 31:31–34) |

### Into the overview (v0.2.1 → Finalise)

| Row | Current | New |
|---|---|---|
| Ps 89 | "for Lam 2", moderate–high | **Lam 2 (2:7, 2:17) and Lam 5 (5:1, 5:19)**, moderate–high |
| Psalms for Lam 3 | Pss 77, 88, 143 | **Ps 143 (3:6); Ps 88 (3:7, 8, 17, 54–55); Ps 77 (3:31); Ps 42–43 (3:20–24); Ps 119 (3:24, 48, 58); Ps 10/17 (3:10)** |
| Lam 5 partners | Isa 63–64; Jer 31:18; Jer 14:19; Pss 102, 89, 44 | **Isa 64 (1st); Jer 31 (31:13, 18); Jer 14:19–21; Ps 102:13; Ps 89:5, 51; Isa 49:14**; Ps 44 demoted |
| The cup at 4:21–22 | Jer 25 first (audit 2) | **Isa 51:22–23 and Jer 25:15–29**, with Ps 137:7 for Edom |
| Isa 54 | not in the map | **Isa 54:8 ~ Lam 3:32** (low–moderate to moderate); thematic counterpart to Lam 5 |

---

## Recommended revisions

1. **Patch both solo digs to v1.1** per the propagation tables. The changes are confined to Headlines 2–4 (3:1–33), Headlines 1, 3 and 4 (5:1–22), and their Tool 11 rows. Both digs' pulpit notes, pastoral notes and internal-echo findings are untouched.
2. **For point-purpose on either passage**, build only on:
   - **3:1–33:** the ענה ("afflict") bracket; the exodus-formula inversion; the man's words for God (Ps 10:9; Ps 143:3, *as his words*); "this I bring back to my heart" with Ps 42–43; 3:31 answering Ps 77; 1:5 → 3:32; MT "we are not consumed".
   - **5:1–22:** the address frame; the two confessions (Jer 14:20); Jer 31:13 and 31:18; Ps 102:13 at 5:19; the reversal of poem 2 (2:1, 6 → 5:1, 20); 3:33 → 5:11; 5:22 with Jer 14:19.
3. **The Christological line for 5:1–22** runs best through Jer 31:31–34 (from 5:21) and the throne (5:19; Ps 102; Heb 1:8–12, which quotes Ps 102). Isa 53:11 is reflection, not echo.

**A pattern to note for the toolkit.** Across Matthew, Job and now three Lamentations audits, the single-verse contacts hold and the design claims fail. Both solo digs here produced design headlines that did not survive a baseline. Round 7's AD item (a pre-headline baseline) would have caught L25, L26, L28 and L29 *in the dig*.

---

## New candidates for the queue

- **L34** — Ps 42–43 behind 3:20–24 (moderate–high)
- **L35** — Ps 119 and Lam 3: exact phrases at 3:24, 3:48, 3:58 — a relation of the two acrostics (moderate–high)
- **L36** — Isa 51:22–23 behind 4:21–22 (moderate–high)
- **L37** — Ps 55, three exclusive ties with Lamentations (unread)
- **L38** — Joel 4:20 behind 5:19 (moderate)
- **L39** — Ps 92:3 behind 3:22–23 (moderate)

**Closed by this audit:** L16–L33. **Open:** L1 (direction only), L34–L39.

---

## Critical assessment — the gaps in this audit

1. **No history of interpretation.** No commentary was consulted. A Logos round would test the Ps 42–43 and Ps 77 readings of 3:20–31, and the כִּי אִם ("unless") of 5:22.
2. **Manual classification in L25.** The enemy-or-God coding of rare partners is the auditor's own and should be re-checked from `a1_classification.txt`.
3. **The baselines measure lemma co-occurrence.** They miss sound, syntax and word order. L28's selection-effect test is itself one design of baseline; a stricter test (pre-registering the roots) is impossible after the fact.
4. **Lexicon artefacts.** The שׁוח / שׁחח split (7743 / 7817) shows that the index can divide a word-family. Chains that turn on rare verbs should search the cognate numbers too.
5. **Ketiv and qere dependence.** Results at 3:10, 3:20, 3:32 and 5:21 change with the reading chosen. Each row says which.
6. **Greek absence.** 3:22–24 and 3:29 have no Old Greek, so findings there cannot be checked in the Greek tradition.
7. **Direction of dependence** is open throughout.
8. **Apparatus spread** is unchecked for every ketiv, *tiqqun* and paragraph marker cited.
9. **The auditors over-ran the length guide.** Nothing was trimmed.

---

## Text-First Declaration

**Secondary sources present in context** (the objects under test):

- the 3:1–33 and 5:1–22 digs;
- claim audit 2;
- overview v0.2.1.

The auditors were blind to all of them. No commentary or lexicon beyond the BHS apparatus was used.

**Primary texts opened:**

- WLC (reading text and lemma index; canon-wide for scans and baselines);
- Swete LXX, for every Greek row;
- the Rahlfs Lamentations export;
- the BHS apparatus for Lamentations.

**Chains and counts verified:**

- the three auditors' baselines (A1, A2, A3, A4, A5; B1, B2, B4; C1, C3, C7b);
- 22 decisive spot checks reproduced by the main session;
- positive controls recorded by each auditor before every nil or "only".

**Warrant use:** verdicts are `[S: audit]` for downstream use. Counts are `[T]`; readings of design are `[I]`.

**Health note.** For the third time running, the design claims fell and the exclusive contacts held. Both digs remain preachable on their verified contacts and internal chains. **Their design headlines should be patched before point-purpose.**
