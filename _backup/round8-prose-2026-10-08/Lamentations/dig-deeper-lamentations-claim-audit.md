# Claim Audit: Lamentations

**Passages audited:** the eleven queued claims from `book-overview-lamentations.md` v0.1.0 (queue #1–11) — Lam 1:1, 3, 5, 9, 10, 13, 16; 2:2, 7, 10, 13, 15, 17–19, 20; 3:1–30; 4:10, 15–22; 5:1, 16, 18–22 — and the book's proposed structure
**Date:** 3 October 2026
**Purpose:** to test the overview's allusion, structure and handoff claims before the sweep leans on them. Two triggers had fired at the overview's first build: eleven candidates queued (trigger 1), and eight of them entered the overview above *moderate* unaudited (trigger 2)
**Primary texts:** WLC Hebrew and lemma index (`_texts/hebrew-wlc/`); Swete LXX; the Rahlfs Lamentations and BHS-apparatus exports from `_texts/logos-exports/`; SBLGNT/MorphGNT
**Study text:** NASB95 · **Pulpit text:** ESV is declared for this book, but no sermon is in view, so no pulpit divergence is assessed here
**Book-overview context:** `Lamentations/book-overview-lamentations.md` v0.1.0 (Draft, 3 October 2026)

Warrant tags: `[T]` observable on the page · `[I]` inference from the text · `[S]` supplied by a secondary source or by tradition. Every count below is a **WLC lemma count** unless it names another edition; "verses in the Hebrew Bible" means verses of the WLC (23,213). References are in English numbering, with the Hebrew in brackets where it differs.

---

## What this audit tested, and how

**Method — the house audit method of the Mark, Matthew and Job audits.** Three fresh auditors were run **one after another**, each **blind** to the overview and to each other. Each was given the claims as neutral propositions, without the overview's ratings or reasoning, and told to *break* them from the primary texts. The corpus was staged from `_texts/` into the session workspace. A shared library reproduced `find.py`'s lemma matcher exactly and was validated before use: חֶסֶד ("lovingkindness") returned Ruth 1:8; 2:20; 3:10, and שָׁכַן ("to dwell") was found at Exod 40:35 and correctly failed at 40:34. No commentaries were consulted and no web search was made.

| Auditor | Claims | Area |
|---|---|---|
| **A** | A1–A4 = queue #5, #6, #10, #11 | Torah, structure, the Daniel handoff |
| **B** | B1–B4 = queue #1, #2, #7, #9 | Latter Prophets |
| **C** | C1–C3 = queue #3, #4, #8 | Writings and New Testament |

**Tests applied to every claim.**

1. **Wording** on both sides, from the Hebrew (and the Greek where relevant).
2. **Rarity:** how many verses in the Hebrew Bible contain the shared lemma set. A pair shared by 200 verses is idiom; one shared by two is distinctive.
3. **Rival sources:** the texts that share the same wording as strongly or more strongly.
4. **A chance baseline** for every *design* claim (a "live source", a structure, a superlative). The density of rare contacts was compared with control texts and with every same-sized window of the Psalter (2,514 windows) or of the Latter Prophets and Psalms (5,231 windows).
5. **The Greek:** whether Swete, and for Lamentations the Rahlfs export, keeps or loses the link.
6. **Hays's seven criteria.** History of interpretation is recorded throughout as *not checked*, since no commentaries were consulted.
7. **Direction of dependence open throughout**, with Isaiah treated as one book.

**Checks by the main session.** Fifty-six of the auditors' decisive findings were re-run independently: 47 lemma and phrase results, four Greek results, the שׁוב ("return") construction search and four of the baseline scripts. **All 56 reproduced exactly.** The main session also ran a supplementary gate on wording claims in the overview that were *not* in the queue (see the section *Supplementary gate*).

---

## Summary

| # | Claim | Verdict | Overview rating | Recommended |
|---|---|---|---|---|
| A1 | Deuteronomy 28 live at six places | **Confirmed with nuance** | high | moderate–high for 4:16 and 1:3; low–moderate as a structuring source |
| A2 | Lev 13:45–46: "the holy city becomes the leper" | **Needs reframing** | high (4:15); moderate (1:1) | moderate (4:15 echo); low (1:1) |
| A3 | Concentric frame: 1 ↔ 5, 2 ↔ 4, 3 at the centre | **Needs reframing** | moderate–high | low–moderate (concentric); moderate (2 ↔ 4 phrase pairing) |
| A4 | Daniel 9 as the canonical handoff | **Needs reframing** | moderate–high | low (lexical); moderate (thematic juxtaposition) |
| B1 | Isa 47: "every one of Zion's humiliations is Babylon's" | **Confirmed with nuance** | high (1:9); moderate–high (pattern) | moderate–high (1:9); moderate (chapter); low ("every one") |
| B2 | Isa 51:17–23 "the densest answer in the canon" | **Needs reframing** | high | moderate–high (link); low (superlative) |
| B3 | Jer 31:18 behind Lam 5:21 (with 1:16; 2:18) | **Confirmed with nuance** | high (5:21) | moderate–high (5:21); moderate (1:16); low (2:18) |
| B4 | Ezekiel's net for the king at Lam 1:13 | **Needs reframing** | moderate–high | low as worded; moderate for Lam 4:20 ~ Ezek 19:4, 8 |
| C1 | Ps 89:38–51 behind the shape of Lam 4–5 | **Needs reframing** | high | low–moderate as worded; **moderate–high moved to Lam 2** |
| C2 | Job behind Lam 3 ("in the images of Job") | **Confirmed with nuance** | high (3:9, 12–13); moderate–high (set) | moderate–high (three pairs); moderate overall |
| C3 | Lam 2:15 LXX supplies the "passers-by" of Matt 27:39 // Mark 15:29 | **Needs reframing** | moderate–high | low–moderate |

| Verdict | Count |
|---|---|
| Confirmed | 0 |
| Confirmed with nuance | 4 |
| Needs reframing | 7 |
| Uncertain — flag for research | 0 |
| Discard | 0 |

**The pattern is the one every previous audit in this project has found.**

- **The single, exclusive verbal links held.** Lam 4:16 ~ Deut 28:50 (four lemmas, two verses in the Hebrew Bible); Lam 1:9 ~ Isa 47:7; Lam 5:21 ~ Jer 31:18; Lam 3:12–13 ~ Job 16:12–13.
- **Every design claim came down:** a "live source" at six places, a concentric structure, a handoff, "the densest answer in the canon", "every one of Zion's humiliations".
- **No stated "only" in the overview was false.**
- **Three factual errors** were found in the overview's wording, and are listed under *Recommended book-overview revisions*.
- **The overview missed its densest partner altogether: Jeremiah 14.**

---

## Claims Audited

### Claim A1: Deuteronomy 28 as a live source (queue #5)

**Source:** Intertextual Map (Torah) and Canonical Position (*Presupposes*); overview rating **high**.
**Claim:** Deut 28 is used at Lam 1:3 (28:65), 1:5 (28:13, 44), 2:20 and 4:10 (28:53, 57), 4:16 (28:50) and 4:19 (28:49), with Lev 26:29 as a parallel curse list.

**Findings.**

- **Lam 4:16 ~ Deut 28:50 is the strongest link in the set.** פְּנֵי כֹהֲנִים לֹא נָשָׂאוּ זְקֵנִים לֹא חָנָנוּ ("they did not honour the priests; they did not favour the elders"; זקנים is a ketiv, but its lemma survives) against לֹא־יִשָּׂא פָנִים לְזָקֵן וְנַעַר לֹא יָחֹן ("who will have no respect for the old, nor show favour to the young"). The four lemmas נשׂא ("lift"), פָּנִים ("face"), זָקֵן ("old") and חנן ("show favour") stand together **only in these two verses**; even זָקֵן + חנן alone occurs only there. `[T]` The Rahlfs export keeps πρεσβύτας ("elders"); **Swete reads προφήτας ("prophets") and loses the link.**
- **Lam 1:3 ~ Deut 28:65 is strong.** מָנוֹחַ ("rest") + גּוֹיִם ("nations") stand together only in these two verses. The overview missed a second hit in the same verse: 1:3b כָּל־רֹדְפֶיהָ הִשִּׂיגוּהָ ("all her pursuers have overtaken her") with 28:45 וּרְדָפוּךָ וְהִשִּׂיגוּךָ ("they shall pursue you and overtake you"). This pair is commoner (14 verses, including 2 Kgs 25:5 and the capture of Zedekiah), but it makes 1:3 a two-hit verse. `[T]`
- **Lam 1:5 is possible only.** It shares רֹאשׁ ("head") with 28:44, but **Lamentations has no זָנָב ("tail")**. "Head and tail" in the overview is therefore an overstatement. The semantic reversal (the foe becomes head) is real. `[T]`
- **Lam 2:20 belongs to a pooled family.** אכל ("eat") + פְּרִי ("fruit") of offspring links it to 28:53. Siege cannibalism is a family of texts: Lev 26:29; Deut 28:53; Jer 19:9 (which reproduces Deut 28:53's בְּמָצוֹר וּבְמָצוֹק, "in the siege and in the distress"); Ezek 5:10. `[T]`
- **Lam 4:10 is a factual error in the overview.** **פְּרִי does not occur at 4:10** — in Lamentations it occurs only at 2:20. The closer parallel to 4:10 בִּשְּׁלוּ יַלְדֵיהֶן ("they boiled their children") is **2 Kgs 6:29** וַנְּבַשֵּׁל אֶת־בְּנִי ("so we boiled my son"): women, a siege, boiling a child. `[T]`
- **Lam 4:19 is better read with Jeremiah.** It shares only נֶשֶׁר ("eagle", 26 verses) with Deut 28:49. Its formula, "swifter than eagles" (קַלִּים … מִנִּשְׁרֵי, "swifter … than the eagles"), matches **Jer 4:13** קַלּוּ מִנְּשָׁרִים סוּסָיו ("his horses are swifter than eagles") and 2 Sam 1:23. The Greek agrees: κοῦφοι … ὑπὲρ ἀετούς ("swifter than eagles") ≈ Jer 4:13 κουφότεροι ἀετῶν ("swifter than eagles"), not Deut 28:49's ὅρμημα ἀετοῦ ("the swoop of an eagle"). `[T]`
- **Missed by the overview.** Lam 4:14 נָעוּ עִוְרִים ("they wandered, blind") ~ Deut 28:29 (the blind man groping). Lam 1:14 עֹל … עַל־צַוָּארִי ("yoke … on my neck") ~ Deut 28:48 — though עֹל + צַוָּאר ("yoke" + "neck") occurs in ten verses and is dense in Jer 27–28.

**Chance baseline.**

- **The overall density is ordinary.** 4.5 % of Lamentations' verses have a rare link (a lemma pair found in ten verses or fewer) to Deut 28. The control texts give: Jer 8–12, 4.4 %; Micah, 5.7 %; Ezek 5–7, 5.2 %; Joel, 4.1 %; Jer 14–15, 11.6 %.
- **Seen from the source side, Deut 28 is inside the judgement band but well below the leaders.** Deut 28 has 10.1 links per 100 verses. Jer 6 has 36.7 and Isa 1 has 35.5; Jer 6:11 alone touches Lam 2:11, 19, 21; 4:1; 5:14.

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | direction open |
| Volume | Strong (4:16; 1:3); Weak elsewhere | two exclusive clusters; the rest is one word or a theme |
| Recurrence | Possible | two or three strong points, not six |
| Thematic coherence | Strong | covenant curse ↔ curse realised; 2:17 says "He has accomplished His word Which He commanded from days of old" |
| Historical plausibility | Possible | the curse idiom is also pooled in Jeremiah (19:9; 4:13) |
| History of interpretation | not checked | no commentaries consulted |
| Satisfaction | Possible | 4:16 and 1:3 illuminate; 4:10 and 4:19 read better against 2 Kgs 6 and Jer 4:13 |

**Verdict:** **Confirmed with nuance.** Deut 28 is live by the two-use test, through two links of real quality. It is not live at six places, and the number of contacts is ordinary for a judgement text.
**Book-overview action required:**

- Delete 4:10 and 4:19 from the Deut 28 row.
- Remove פְּרִי from 4:10.
- Name 2 Kgs 6:28–29 (for 4:10), Jer 4:13 and 2 Sam 1:23 (for 4:19), and Jer 19:9 (beside Lev 26:29).
- Add Deut 28:45 at 1:3.
- Recast 1:5 as "the foe becomes head".
- Re-rate the row: **moderate–high** for 4:16 and 1:3; **low–moderate** for Deut 28 as a structuring source.

---

### Claim A2: Lev 13:45–46 — "the holy city becomes the leper" (queue #6)

**Source:** Intertextual Map (Torah); Canonical Position. Overview rating: **high** (4:15); **moderate** (1:1).
**Claim:** Lam 4:15 echoes the leper's cry, וְטָמֵא טָמֵא יִקְרָא ("and he shall cry, 'Unclean! Unclean!'", Lev 13:45). Lam 1:1, יָשְׁבָה בָדָד ("she sits alone"), echoes בָּדָד יֵשֵׁב ("he shall live alone", Lev 13:46).

**Findings.**

- **The cry is genuinely rare.** In the sense "cry 'Unclean!'", טָמֵא + קרא ("unclean" + "cry") occurs **only at Lev 13:45 and Lam 4:15**; Isa 35:8 has the pair in a different, passive sense. `[T]`
- **But Isa 52:11 is the stronger verbal partner.** סוּרוּ סוּרוּ … טָמֵא אַל־תִּגָּעוּ ("depart, depart … touch nothing unclean") matches four elements of 4:15 in the same order. סור ("depart") + טָמֵא ("unclean") + נגע ("touch") occurs only at Isa 52:11 and Lam 4:15, and the Greek is near-verbatim (ἀπόστητε ἀπόστητε … μὴ ἅπτεσθε, "depart, depart … do not touch"). `[T]`
- **The word that carries the Leviticus link is textually suspect.** BHS marks קָרְאוּ לָמוֹ ("they cried to them") at 4:15 *sed prb dl* ("but probably to be deleted"). `[T]` for the apparatus note; `[unchecked — apparatus spread]`.
- **The subject is not the city.** In 4:13–15 those cried at as "Unclean!" are the prophets and priests who shed blood, נְגֹאֲלוּ בַּדָּם ("defiled with blood", 4:14). They are blood-defiled, not leprous. Poem 1's impurity vocabulary is **menstrual**: נִידָה ("impurity", 1:8), טֻמְאָתָהּ בְּשׁוּלֶיהָ ("her uncleanness was in her skirts", 1:9), נִדָּה ("an unclean thing", 1:17). "The holy city becomes the leper" merges two subjects and two impurity systems. `[T]`
- **Lam 1:1 is idiom.** ישׁב ("sit") + בָּדָד ("alone") occurs in six verses (Lev 13:46; Jer 15:17; 49:31; Ps 4:9 [Eng 4:8]; Lam 1:1; 3:28). A *city* that is בָּדָד ("solitary") appears only at Isa 27:10 and Lam 1:1, a better rival. The Greek loses the Leviticus link: μόνη ("alone", Lam 1:1) against κεχωρισμένος ("separated", Lev 13:46).

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | direction open |
| Volume | Possible (4:15); Weak (1:1) | two lemmas at 4:15, one of them textually queried; 1:1 is idiom |
| Recurrence | Weak | no other leprosy vocabulary in Lamentations — no צָרַעַת ("skin disease"), no נֶגַע ("mark") |
| Thematic coherence | Possible | the exclusion of the unclean fits; leprosy specifically does not |
| Historical plausibility | Possible | — |
| History of interpretation | not checked | — |
| Satisfaction | Weak–Possible | Isa 52:11 explains more of 4:15 |

**Verdict:** **Needs reframing.** Lev 13:45 is a real echo at 4:15, but of the priests and prophets driven out with the leper's cry. It does not show that the city becomes a leper, and Isa 52:11 is the closer text.
**Book-overview action required:**

- Restate the row as follows: at 4:15 the defiled priests and prophets are driven out with the leper's cry (Lev 13:45), in words closest to Isa 52:11.
- Move the Isa 52:11 row up beside it.
- Drop the 1:1 leg, or demote it to *low*, naming Isa 27:10 and Jer 15:17.
- Note that poem 1's impurity is menstrual.
- Flag the BHS deletion proposal at 4:15.
- Re-rate: **moderate** for 4:15; **low** for 1:1.

---

### Claim A3: The concentric frame — 1 ↔ 5, 2 ↔ 4, 3 at the centre (queue #10)

**Source:** Structural Arc Map, "The binding device". Overview rating: **moderate–high**.
**Claim:** Poems 2 and 4 answer each other (אֵיכָה, "How!"; children and food; prophets and priests; poured-out wrath; "at the head of every street"). Poems 1 and 5 answer each other (אַלְמָנָה, "widow"; "See, O LORD" / "look and see"; "rest"). Poem 3 stands at the centre.

**Findings on the evidence offered.**

- **אֵיכָה ("How!") does not pair 2 with 4.** It stands at 1:1, 2:1, 4:1 *and 4:2*, so it links poems 1, 2 and 4. `[T]`
- **"See, O LORD" does not pair 1 with 5.** רְאֵה יְהוָה וְהַבִּיטָה ("See, O LORD, and look") at **2:20 is word for word 1:11**. נבט ("look") + ראה ("see") occurs at 1:11, 1:12, 2:20 and 5:1. `[T]`
- **The overview mis-cites the prophets.** It gives them at 4:16; 4:16 has priests and elders, and the prophets are at **4:13**. `[T]`
- **Three items do hold, exclusive within Lamentations to poems 2 and 4.** נָבִיא ("prophet": 2:9, 14, 20; 4:13); שׁפך ("pour out") + חֵמָה ("wrath": 2:4; 4:11); בְּרֹאשׁ כָּל־חוּצוֹת ("at the head of every street": 2:19; 4:1). Children and bread are *not* exclusive to 2 and 4: עוֹלָל ("child") is at 1:5; לֶחֶם ("bread") at 1:11; 5:6, 9. `[T]`
- **One item holds for 1 and 5.** אַלְמָנָה ("widow") occurs only at 1:1 and 5:3. מָנוֹחַ ("rest", 1:3) and הוּנַח ("was given rest", 5:5) are cognates and a soft echo. `[T]`
- **The counts are correct.** The WLC lemma-index word counts are 376 / 381 / 381 / 259 / 145. **Counting space-separated words instead gives 330 / 333 / 347 / 231 / 136, so the unit must be named.** The verse midpoint does fall between 3:33 and 3:34 (verses 77 and 78 of 154). **The word midpoint (771 of 1,542) falls at 3:3**, so "the centre" depends on the unit counted. `[T]`

**Chance baseline.** The test reshuffled Lamentations' verses 2,000 times into five pseudo-poems with the real poems' word counts. It counted the content lemmas each pair of poems shares exclusively, and the rare verse-to-verse links per 10⁴ word-pairs.

| Pair | Exclusive lemmas: observed ÷ expected (p) | Rare verse-links (per 10⁴ word-pairs) |
|---|---|---|
| 1–2 | 0.78 (0.87) | **0.98** |
| 1–3 | 0.85 (0.77) | 0.21 |
| 1–4 | 0.71 (0.87) | 0.00 |
| **1–5** | **1.40 (0.27)** | 0.37 |
| 2–3 | 1.09 (0.38) | 0.34 |
| **2–4** | **1.00 (0.56)** | **0.91** |
| 2–5 | 0.93 (0.62) | 0.72 |
| 3–4 | 0.70 (0.88) | 0.20 |
| 3–5 | 1.39 (0.28) | 0.00 |
| 4–5 | 1.09 (0.52) | 0.00 |

**Reading the table.**

- On whole vocabulary, 2–4 is exactly at chance.
- At phrase level 2–4 is strong (0.91), but 1–2 is stronger (0.98).
- 1–5 is the only pair above expectation on vocabulary, and not significantly so.
- 1–4 has no rare links at all.

**The data fit poem 2 as a hub — tied to poem 1 and to poem 4 — better than a mirror.** Poem 3 is lexically the most isolated poem, which fits a distinct centre but is equally explained by its individual first-person voice.

| Hays (design claim) | Score | Reasoning |
|---|---|---|
| Volume | Possible (2–4); Weak (1–5) | 2–4 has distinctive phrases; 1–5 rests on אַלְמָנָה alone |
| Recurrence | Possible | — |
| Chance baseline | Weak | neither pair beats chance on vocabulary; 1–2 equals 2–4 at phrase level |
| Thematic coherence | Possible | 2 and 4 share siege and wrath scenes |
| History of interpretation | not checked | — |
| Satisfaction | Possible | the formal centre is real; the lexical symmetry is not demonstrated |

**Verdict:** **Needs reframing.** The formal facts stand:

- four acrostics, with poem 3 a triple acrostic;
- poem 5 has 22 verses but no acrostic;
- the last two poems shrink;
- the verse midpoint falls at 3:33 | 34.

The lexical concentric design is **not** shown above chance. 2 ↔ 4 is a real phrase pairing, but no stronger than 1 ↔ 2, and 1 ↔ 5 rests on one word.

**Book-overview action required:**

- Replace "a concentric frame" with **"a formally centred book: the triple acrostic at its centre, poem 2 as a lexical hub tied to both 1 and 4, and the volume falling away in 4–5"**.
- Remove אֵיכָה and "See, O LORD" from the evidence.
- Correct 4:16 → 4:13.
- Name the count unit, and note that the word midpoint is 3:3.
- Re-rate: **low–moderate** (concentric); **moderate** (2 ↔ 4 phrases).
- The word-count table and the 3:31–33 centre stand, as verse-based facts.

---

### Claim A4: Daniel 9 as the canonical handoff (queue #11)

**Source:** Canonical Position, *Handoff*. Overview rating: **moderate–high**.
**Claim:** Daniel's prayer takes up Lamentations' language. The items offered are "we have sinned" (Dan 9:5); חֶרְפָּה ("reproach") with Jerusalem (9:16); the root שׁמם ("be desolate"); "open your eyes and see" (9:18); and רַחֲמִים ("compassion", 9:18).

**Findings.**

- **Every shared item is a formula.** חָטָאנוּ ("we have sinned") occurs in 23 verses; רַחֲמִים ("compassion") in 44. `[T]`
- **Dan 9:18's formula belongs elsewhere.** פְּקַח עֵינֶיךָ וּרְאֵה ("open your eyes and see") is **Hezekiah's prayer** (2 Kgs 19:16 = Isa 37:17). Lam 5:1's הַבֵּט וּרְאֵה ("look and see") matches **Isa 63:15 and Ps 80:15 [Eng 80:14]**. `[T]`
- **The pairing at Lam 5:1 is not in Daniel 9.** זכר ("remember") + חֶרְפָּה ("reproach") occurs at Ps 74:22; Ps 89:51 [Eng 89:50]; Isa 54:4; Jer 15:15 and Lam 5:1 — not in Dan 9. `[T]`
- **Different words on each side.** The two sides use different lemmas of the root שׁמם (Dan 9:17 שָׁמֵם, an adjective; 9:18 שְׁמָמוֹת, a noun; Lam 5:18, a verb). The Lamentations side of the claim is assembled from four verses in two poems. `[T]`
- **On neutral measures Daniel 9 ranks near the bottom of the confession family.** Rare links to Lamentations per 100 words:

| Prayer | Rare links to Lamentations per 100 words |
|---|---|
| Ps 89:39–53 [Eng 89:38–52] | 5.45 |
| Jer 14:1–15:4 | 3.94 (17 Lamentations verses linked) |
| Ps 74 | 3.59 |
| Isa 63:7–64:11 [Eng 63:7–64:12] | 2.68 |
| **Dan 9:4–19** | **1.47** |
| Ezra 9 | 1.00 |
| Prov 1–2 (control) | 0.79 |

  Daniel 9 ranked first only on a feature list drawn from Daniel 9 itself, which is circular. **Isa 63–64 has every feature the claim cites from Daniel 9, with closer wording at Lam 5:1** (Isa 63:15 הַבֵּט … וּרְאֵה, "look … and see"; Isa 64:8 [Eng 64:9] זכר + נבט, "remember" + "look"; Isa 64:9 [Eng 64:10] "Zion a wilderness … Jerusalem a desolation").
- **The Greek gives a neat frame, but Ps 89 is closer still.** Theodotion's Dan 9:18 ἴδε τὸν ἀφανισμὸν ἡμῶν ("see our desolation") and Lam 5:1 ἴδε τὸν ὀνειδισμὸν ἡμῶν ("see our reproach") frame each other well. Ps 88:51 Swete [Eng 89:50] μνήσθητι … τοῦ ὀνειδισμοῦ ("remember … the reproach") is closer still.

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | — |
| Volume | Weak | formulaic; no exclusive cluster |
| Recurrence | Weak | the Lamentations items are scattered |
| Thematic coherence | Strong | confession over a desolate Jerusalem |
| Historical plausibility | Possible | Dan 9:2 names Jeremiah's seventy years, not Lamentations |
| History of interpretation | not checked | — |
| Satisfaction | Possible as canonical juxtaposition; Weak as a lexical handoff | — |

**Verdict:** **Needs reframing.** Daniel 9 is one member of a pooled family of communal confessions, and not a distinctive partner.
**Book-overview action required:**

- Recast the *Handoff* field: Daniel 9 stands as one of the confessional prayers that, in canonical order, follow Lamentations' unanswered question. Its link is thematic. Lexically, Lamentations' closest partners are Isa 63–64, Ps 74, Ps 89 and Jer 14.
- Correct the Dan 9:18 formula's true parallel (2 Kgs 19:16 = Isa 37:17).
- Re-rate: **moderate** (thematic and canonical); **low** (lexical).

---

### Claim B1: Isaiah 47 — "every one of Zion's humiliations is Babylon's" (queue #1)

**Source:** Intertextual Map (Isaiah). Overview rating: **high** for 1:9, **moderate–high** for the pattern.
**Claim:** Isa 47:1, 3, 7, 8 and 15 are matched at Lam 2:10; 1:8; 1:9; 1:1; 4:17.

**Findings, contact by contact.**

- **Lam 1:9 ~ Isa 47:7 — exclusive and near-verbatim.** לֹא זָכְרָה אַחֲרִיתָהּ ("she did not consider her future") against לֹא זָכַרְתְּ אַחֲרִיתָהּ ("you did not remember the outcome of it"). זכר ("remember") + אַחֲרִית ("end") occurs **only in these two verses**, and the Greek keeps it: οὐκ ἐμνήσθη ἔσχατα αὐτῆς ("she did not remember her last things") against οὐδὲ ἐμνήσθης τὰ ἔσχατα ("nor did you remember the last things"). Deut 32:29 is not a rival: it has בין ("understand"), not זכר. `[T]`
- **Lam 2:10 ~ Isa 47:1 — exclusive cluster, scattered syntax.** ישׁב ("sit") + עָפָר ("dust") + בְּתוּלָה ("virgin") + בַּת ("daughter") occurs only in these two verses. In Lamentations, however, the elders sit, the dust goes on their heads, and the virgins have their own clause. The dust-on-the-head rite has its own phrase (Josh 7:6; Ezek 27:30; Job 2:12–13), and Isa 47:1 LXX has no "dust". `[T]`
- **Lam 1:1 ~ Isa 47:8 — rare.** אַלְמָנָה ("widow") + ישׁב ("sit") occurs in four verses, and only these two picture a **city** sitting as a widow. Both also set the city's former rank against her fall (Isa 47:5 גְּבֶרֶת מַמְלָכוֹת, "the queen of kingdoms"; Lam 1:1 שָׂרָתִי בַּמְּדִינוֹת, "a princess among the provinces"). `[T]`
- **Lam 1:8 — not Isa 47.** עֶרְוָה ("nakedness") + ראה ("see") occurs in ten verses. Ezek 16:37 (lovers seeing her nakedness) is closer than Isa 47:3, and the Greek loses the Isaiah link. `[T]`
- **Lam 4:17 — idiom.** "No one to save" occurs in 21 verses. Isa 45:20 אֵל לֹא יוֹשִׁיעַ ("a god who cannot save") is nearer in form than 47:15. `[T]`
- **The skirts of Lam 1:9 are not Isa 47's.** בְּשׁוּלֶיהָ ("in her skirts") matches Jer 13:22, 26 and Nah 3:5; Isa 47:2 uses a different word (שֹׁבֶל, "train"). `[T]`

**Chance baseline.**

- Against Lam 1–2, Isa 47 ranks **3rd of 219 Latter-Prophets chapters** by density (0.733 rare contacts per verse). It stands behind **Jer 14** (1.045) and level with **Nah 3** (0.737), the second foreign-city humiliation chapter.
- Against Lam 3–5 it falls to 58th.
- So it is a genuine partner of the city-poems — in the top 2 % of chapters — but not a unique one.

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | direction open |
| Volume | Strong (1:9; 2:10, scattered); Possible (1:1); Weak (1:8; 4:17) | — |
| Recurrence | Strong | three independent contacts in Lam 1–2 |
| Thematic coherence | Strong | a queenly city brought to the dust and to widowhood |
| Historical plausibility | Possible | — |
| History of interpretation | not checked | — |
| Satisfaction | Possible | illuminates 1:1 and 1:9; does not reach "every one" |

**Verdict:** **Confirmed with nuance.** Isa 47 is a real partner of Lam 1–2 through 1:9, 2:10 and 1:1. "Every one of Zion's humiliations" is **false as worded**, and Nah 3 is an equal partner.
**Book-overview action required:**

- Drop "every one".
- Remove 1:8 and 4:17 from the row, or mark them as shared idiom, naming Ezek 16:37 and Isa 45:20.
- Assign the skirts to Jer 13:22, 26 and Nah 3:5.
- Add **Nah 3** beside Isa 47.
- Note that Isa 52:2 and 54:4 reverse Isa 47's images within Isaiah.
- Re-rate: **moderate–high** (1:9); **moderate** (Isa 47 as a chapter); **low** ("every one").

---

### Claim B2: Isaiah 51:17–23 — "the densest single answer to Lamentations anywhere in the canon" (queue #2)

**Source:** Intertextual Map (Isaiah); Christological Trajectory (the cup). Overview rating: **high**.
**Claim:** The cup (51:17, 22 ~ Lam 4:21–22); "who will comfort you?" with ruin, famine and sword (51:19 ~ 2:13; 4:9); sons lying "at the head of every street" (51:20 ~ 2:19, 21; 4:1); the cup removed and given to the tormentors (51:22–23 ~ 4:21–22).

**Findings.**

- **Lam 2:13 ~ Isa 51:19 is exclusive.** נחם ("comfort") + שֶׁבֶר ("ruin") occurs only in these two verses. `[T]` Nah 3:7 shares מִי ("who?") + נחם with both.
- **The Greek strengthens the link.** LXX Lam 2:13 reads τίς σώσει καὶ παρακαλέσει σε … ὅτι ἐμεγαλύνθη **ποτήριον** συντριβῆς σου ("who will save and comfort you … for the **cup** of your ruin has been made great"). BHS records that the translator read מִי יוֹשִׁיעַ לָךְ וְנִחַמְךָ ("who will save you and comfort you") and כּוֹס ("cup") where the Hebrew has כַּיָּם ("like the sea"). **In Greek, Lam 2:13 holds all three elements of Isa 51:17–19 — the cup, the ruin, and "who will comfort you?".** `[T]` for Swete and the BHS note. Whether the translator was reading Lamentations through Isaiah is an open textual question. This is triage category 2: a substantive Greek reading, weighed rather than defaulted.
- **"At the head of every street" is shared with Nahum.** The phrase occurs at Isa 51:20; Nah 3:10; Lam 2:19; 4:1. **Nah 3:10 is closer to Lam 2:19**: עוֹלָל ("infant") + רֹאשׁ ("head") + חוּצוֹת ("streets") occurs only at Nah 3:10 and Lam 2:19. `[T]`
- **The cup that passes to Edom has closer partners than Isaiah.** Hab 2:16 (כּוֹס, "cup" + גַּם, "also": only Hab 2:16 and Lam 4:21); Nah 3:11 (תִּשְׁכְּרִי, "you will be drunk": only Nah 3:11 and Lam 4:21); Jer 49:12 (the cup addressed to Edom). Isa 51:22–23 supplies the *pattern of reversal*, not the wording. `[T]`
- **A contact the overview missed.** The root יגה ("cause grief, torment") occurs in eight verses, five of them in Lamentations (1:4, 5, 12; 3:32, 33). יגה + עבר ("pass by") occurs only at Isa 51:23 and Lam 1:12. `[T]`

**Chance baseline.** Rare shared lemma pairs per verse against the whole of Lamentations (pairs found in five verses or fewer):

| Passage | Rare pairs per verse |
|---|---|
| Isa 51:17–23 | 0.57 |
| **Isa 51:17–52:2, as one unit** | **1.33** |
| Isa 52:1–12 | 1.25 |
| Jer 30:12–17 | 1.00 |
| Jer 31:15–22 | 1.00 |
| Isa 49:14–21 | 0.50 |
| Isa 54:1–11 | 0.18 |
| Isa 40:1–2 | 0 |
| *Control:* Jer 14:17–22 | 4.00 |
| *Control:* Jer 8:18–23 | 2.17 |

Across every 7-verse window of the Latter Prophets and Psalms, the window beginning at Isa 51:17 ranks **395th of 5,231**.

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | direction open |
| Volume | Strong (51:19 ~ 2:13); Possible (51:20); Weak (the cup in the Hebrew), Strong in the Greek of 2:13 | — |
| Recurrence | Strong | 2:13, 19, 21; 4:1, 21–22; 1:12 through יגה |
| Thematic coherence | Strong | Isaiah asks and answers Lamentations' own question |
| Historical plausibility | Possible | — |
| History of interpretation | not checked | — |
| Satisfaction | Strong | — |

**Verdict:** **Needs reframing.** The connection is real and strong, but the superlative fails. Taken alone, 51:17–23 is not the densest of the "answer" passages. **Taken as Isa 51:17–52:2, it leads them.** Jer 14 and Jer 8 outrank everything, but as fellow laments, not answers.
**Book-overview action required:**

- Redefine the unit as **Isa 51:17–52:2**.
- Replace "the densest single answer anywhere in the canon" with **"the densest of the reversal passages"**.
- Name Nah 3:10 for 2:19, and Hab 2:16, Nah 3:11 and Jer 49:12 for the Edom cup at 4:21.
- Add the יגה contact and the LXX reading at 2:13 (כּוֹס).
- Re-rate: **moderate–high** for the link.

---

### Claim B3: Jeremiah 31:15–18 behind Lam 5:21, 1:16 and 2:18 (queue #7)

**Source:** Intertextual Map (Jeremiah); Echo Table. Overview rating: **high** for 5:21.
**Claim:** הֲשִׁיבֵנוּ … וְנָשׁוּבָה ("restore us … that we may be restored", Lam 5:21) is Ephraim's prayer, הֲשִׁבֵנִי וְאָשׁוּבָה ("bring me back that I may be restored", Jer 31:18). Rachel's weeping (31:15) and tears (31:16) stand behind Lam 1:16 and 2:18.

**Findings.**

- **Lam 5:21 ~ Jer 31:18 is a unique construction.** Of the 28 verses in the Hebrew Bible with both a hiphil and a qal of שׁוב ("return"), **only Jer 31:18 and Lam 5:21** have a hiphil imperative with a first-person object followed by a first-person qal. `[T]`
  - Ps 80:4, 8, 20 [Eng 80:3, 7, 19] and Jer 17:14 share the *pattern* (imperative followed by a result), but not the doubled שׁוב. Jer 15:19 has the reverse order.
  - Lam 5:21 has the ketiv ונשוב; the qere וְנָשׁוּבָה (many manuscripts, per BHS) is a **cohortative**, exactly as Jer 31:18's וְאָשׁוּבָה. The qere makes the match closer still. `[T]`; `[unchecked — apparatus spread]` for the qere's extent.
  - In Greek the link survives: ἐπίστρεψόν με καὶ ἐπιστρέψω ("turn me, and I will turn", Swete Jer 38:18) against ἐπίστρεψον ἡμᾶς … καὶ ἐπιστραφησόμεθα ("turn us … and we will be turned"). But the first half is also the Greek refrain of Ps 79 and 84 [Eng 80 and 85], so only the second verb is distinctive there.
- **Lam 1:16 ~ Jer 31:15 — a genuine trio.** בכה ("weep") + נחם ("comfort") occurs in four verses (Gen 37:35; Jer 31:15; Lam 1:2, 16); add בֵּן ("son") and it is three. The root of the "refused to be comforted" idiom is Gen 37:35 (Jacob over Joseph). `[T]`
- **Lam 2:18 belongs to Jer 14:17, not Jer 31.** ירד ("run down") + דִּמְעָה ("tears") + יוֹמָם ("by day") + לַיְלָה ("night") occurs **only at Jer 14:17 and Lam 2:18**. `[T]`

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | direction open |
| Volume | Strong (5:21); Possible (1:16); Weak (2:18 for Jer 31) | — |
| Recurrence | Possible | 1:16; 5:21 |
| Thematic coherence | Strong | grief moving to a plea for return |
| Historical plausibility | Possible | — |
| History of interpretation | not checked | — |
| Satisfaction | Strong (5:21) | — |

**Verdict:** **Confirmed with nuance.**
**Book-overview action required:**

- State the exclusivity (2 of 28 verses) and the qere.
- Note that in Greek the half-line is also the Ps 80 refrain.
- Reassign 2:18 to Jer 14:17.
- Name Gen 37:35 as the root of the comfort-refused idiom.
- Re-rate: **moderate–high** (5:21); **moderate** (1:16); **low** (2:18 as a Jer 31 contact).

---

### Claim B4: Ezekiel's net for the king at Lam 1:13 (queue #9)

**Source:** Intertextual Map (Ezekiel). Overview rating: **moderate–high**.
**Claim:** פָּרַשׂ רֶשֶׁת לְרַגְלַי ("He has spread a net for my feet", Lam 1:13) takes up "I will spread My net over him" (Ezek 12:13; 17:20; 19:8; Hos 7:12): the net spread for the king is spread for Zion.

**Findings.**

- **The pair is uncommon but idiomatic.** פרשׂ ("spread") + רֶשֶׁת ("net") occurs in nine verses (Ezek 12:13; 17:20; 19:8; 32:3; Hos 5:1; 7:12; Ps 140:6; Prov 29:5; Lam 1:13). Lam 1:13's distinctive element, the net set *for the feet*, places it with Ps 9:16; 25:15; 57:7 and Prov 29:5, not with Ezekiel's עָלָיו ("over him"). There is nothing royal, nothing of capture and nothing of Babylon in Lam 1:13. The Greek compounds differ (διεπέτασεν, "spread out", against ἐκπετάσω, "I will spread out"). `[T]`
- **The real royal contact is at Lam 4:20.** מְשִׁיחַ יְהוָה נִלְכַּד בִּשְׁחִיתוֹתָם … בַגּוֹיִם ("the LORD's anointed was captured in their pits … among the nations") meets Ezek 19:4, 8 גּוֹיִם … בְּשַׁחְתָּם נִתְפָּשׂ ("nations … he was caught in their pit"), said of Judah's royal lion.
  - The Hebrew lemmas differ (שְׁחִית against שַׁחַת, both "pit"; לכד against תפשׂ, both "catch").
  - The Greek is near-identical: συνελήμφθη ἐν ταῖς διαφθοραῖς αὐτῶν ("he was caught in their pits") against ἐν τῇ διαφθορᾷ αὐτῶν συνελήμφθη. Apart from these, the combination occurs only in Ps 9:16.
  - Ezek 19:8 also contains the spread net. `[T]`

| Hays (as claimed) | Score | Reasoning |
|---|---|---|
| Volume | Possible | nine verses; formula and object differ |
| Recurrence | Possible | only if 4:20 ~ Ezek 19 is counted |
| Thematic coherence | Possible | — |
| History of interpretation | not checked | — |
| Satisfaction | Weak | the royal application is not in 1:13 |

**Verdict:** **Needs reframing.**
**Book-overview action required:**

- Move the row to **Lam 4:20 ~ Ezek 19:4, 8 (the king caught in the pit)**, rated **moderate**.
- Keep 1:13 only as the shared hunting idiom (Ps 9:16; 57:7; Prov 29:5), rated **low**.
- Add Ezek 19 to the Christological Trajectory's "anointed taken" paragraph, where the overview already cites συνελήμφθη ("was seized").

---

### Claim C1: Psalm 89:38–51 [Heb 89:39–52] behind the shape of Lam 4–5 (queue #3)

**Source:** Intertextual Map (Writings). Overview rating: **high**, "live (six places)".
**Claim:** Ps 89:38–51 is "the closest parallel to the shape of Lam 4–5". The overview cites contacts at 4:20, 2:7, 3:31, 5:22, 2:2, 5:16, 1:12, 2:15 and 5:1.

**Findings.**

- **Lam 4–5 is the wrong target.** Measured strictly (lemma pairs found in five verses or fewer), Lam 4–5 and Ps 89:39–52 [Eng 89:38–51] share one rare pair, at 5:1. Across 2,514 fourteen-verse windows of the Psalter, that ranks 81st, and 21 % of windows score as much. `[T]`
- **The real cluster is in Lam 2, and it is exclusive.**
  - **נאר ("spurn")** occurs **only at Ps 89:40 [Eng 89:39] and Lam 2:7** in the whole Hebrew Bible. With זנח ("reject") beside it, it occurs in these two places only. The overview missed it.
  - **Lam 2:17 ~ Ps 89:43 [Eng 89:42].** God raises (רום) the foe (צַר) and makes the enemy (אוֹיֵב) rejoice (שׂמח). The four lemmas stand together **only in these two verses**. Lam 2:17 inverts Ps 89:18, 25 [Eng 89:17, 24], where it is the king's horn that is raised. The overview missed it.
  - **Lam 2:2 ~ Ps 89:40–41 [Eng 89:39–40].** חלל ("profane") + לָאָרֶץ ("to the ground"), with מִבְצָר ("stronghold") beside it, occurs only there.
  - **"All who pass along the way"** (כָּל־עֹבְרֵי דֶרֶךְ) occurs in four verses: Ps 80:13 [Eng 80:12]; 89:42 [Eng 89:41]; Lam 1:12; 2:15.
  - These Lam 2 contacts follow roughly the order of Ps 89:39–43 [Eng 89:38–42]. Against Lam 2, Ps 89:39–52 ranks **4th of 2,514** windows (top 0.8 %). `[T]`
- **Most of the overview's Lam 3–5 contacts have closer rivals.**
  - **3:31 ~ Ps 77:8 [Eng 77:7].** זנח ("reject") + עוֹלָם ("forever") + אֲדֹנָי ("Lord") stand together only there and at Lam 3:31, and Lamentations answers the psalm's question.
  - **5:22 ~ Jer 14:19.** The doubled מָאֹס מָאַסְתָּ ("you have utterly rejected") occurs only at Jer 14:19 and Lam 5:22. **Lamentations never pairs זנח with מאס** (that pair is Ps 89:39 [Eng 89:38] alone).
  - **5:1** is shared equally with Ps 74:22.
  - **5:16** has no word in common with Ps 89: נֵזֶר ("crown") is not עֲטֶרֶת ("crown"). Its exclusive partner is **Job 19:9** עֲטֶרֶת רֹאשִׁי ("the crown from my head").
  - **4:20** מְשִׁיחַ יְהוָה ("the LORD's anointed") is idiom, in 22 verses.
  - **One further Ps 89 contact:** כִּסְאֲךָ ("your throne") + לְדֹר וָדוֹר ("to all generations") occurs only at **Ps 89:5 [Eng 89:4]** and Lam 5:19. `[T]`
- **The Greek keeps the Lam 2 links:** ἐβεβήλωσεν … εἰς τὴν γῆν … ὀχυρώματα ("he profaned … to the ground … strongholds", 2:2); ηὔφρανεν … ἐχθρόν, ὕψωσεν ("he made the enemy rejoice; he raised", 2:17). It loses נאר.

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | direction open |
| Volume | Weak (Lam 4–5); Strong (Lam 2) | — |
| Recurrence | Weak (Lam 4–5); Strong (Lam 2: four verses meet five consecutive verses of the psalm) | — |
| Thematic coherence | Strong | the rejected anointed, the profaned crown, the mocking passers-by |
| Historical plausibility | Possible | shared liturgical idiom explains as well as borrowing |
| History of interpretation | not checked | — |
| Satisfaction | Possible (Lam 4–5); Strong (Lam 2:17 as an inversion of Ps 89) | — |

**Verdict:** **Needs reframing.** Ps 89 is not distinctive for Lam 4–5, where it is one voice among Ps 74, 79, 80 and Jer 14. **It is distinctive for Lam 2**, at a level the baseline does not explain.
**Book-overview action required:**

- Move the row from Lam 4–5 to **Lam 2:2, 7, 15, 17**, rated **moderate–high**.
- Add נאר and Lam 2:17 ~ Ps 89:43.
- Drop 5:16, giving it to Job 19:9.
- Give 3:31 to Ps 77:8, 5:22 to Jer 14:19, and 5:1 jointly to Ps 74:22.
- Keep 4:20 as thematic only, and add Ps 89:5 ~ 5:19.
- In the Christological Trajectory, "Lamentations echoes Ps 89 six times" must be withdrawn. The Davidic thread rests on Lam 2 and 4:20, not on six contacts.

---

### Claim C2: Job behind Lam 3 — "the man of Lam 3 suffers in the images of Job" (queue #4)

**Source:** Intertextual Map (Writings); Canonical Position. Overview rating: **high** for 3:9 and 3:12–13; **moderate–high** for the set.
**Claim:** Job 3:23; 9:18; 16:10, 12–13; 19:8; 30:9; and 1:1 (Uz) are matched at Lam 3:1, 7, 9, 12–15, 30, 43–44, 63 and 4:21.

**Findings.**

- **Three exclusive pairs.**
  - **Lam 3:12–13 ~ Job 16:12–13.** מַטָּרָא/מַטָּרָה ("target") with כִּלְיוֹת ("kidneys") occurs only in these two places, in the same order.
  - **Lam 3:30 ~ Job 16:10.** לְחִי ("cheek") + חֶרְפָּה ("reproach") occurs only in these two verses.
  - **Lam 3:14 ~ Job 30:9.** "I have become their taunt-song" (נְגִינָתָם, "their taunt-song", + היה, "become") occurs only in these two verses. `[T]`
- **Each exclusive pair has an equally exclusive rival.**
  - Lam 3:30 also meets **Isa 50:6**. נתן ("give") + נכה ("smite") + לְחִי ("cheek") occurs only at Isa 50:6 and Lam 3:30: "I gave … my cheeks to those who pluck out the beard".
  - Lam 3:14a meets **Jer 20:7**. שְׂחוֹק ("laughingstock") + כָּל־הַיּוֹם ("all the day") occurs only at Jer 20:7 and Lam 3:14.
  - So 3:14 joins Jeremiah (first half) to Job (second half). `[T]`
- **Lam 3:7–9 ~ Job 19:8 is moderate.** גדר ("wall up") + נְתִיבָה ("path") occurs in four verses. **Hos 2:6 [Heb 2:8]** shares three words with 3:9 (גדר, דֶּרֶךְ "way", נְתִיבָה), and גדר + דֶּרֶךְ occurs only at Hos 2:8 [Heb] and Lam 3:9. Job 19:8 fits 3:7's "I cannot go out" better. `[T]`
- **Two factual errors in the overview's wording.**
  - Job 9:18 has מַמְּרֹרִים ("bitterness"), a different noun from Lam 3:15's מְרוֹרִים ("bitterness"); the link is at root level only.
  - The סכך ("cover") of Lam 3:43–44, "you have covered yourself", is a different word-sense from Job 3:23's "hedged in". The hedged-in man survives as a motif, through Lam 3:7 with Job 3:23 and 1:10. `[T]`
- **Uz (4:21) fits Jer 25:20 better than Job 1:1.** Jeremiah's cup oracle (25:15–29) names Edom and has the cup. Swete's Lamentations drops Uz altogether. `[T]`
- **Missed Job contacts.**
  - Lam 3:8 ~ Job 19:7 (crying out, unheard).
  - **Lam 5:16 ~ Job 19:9.** עֲטֶרֶת רֹאשׁ ("crown of the head") occurs in these two verses only.
  - Lam 2:16 ~ Job 16:9 (gnashing the teeth).
  - **Lam 2:11 ~ Job 16:13.** The inner organ "poured out on the ground" occurs only at 2 Sam 20:10; Job 16:13; Lam 2:11.
  - So Job 16 and 19 touch Lam 2, 3 and 5, not Lam 3 alone. `[T]`

**Chance baseline.**

| Comparator | Rare contacts (≤5 verses) per 100 comparator verses |
|---|---|
| Job, whole book | 2.15 |
| Job 3–20 | 3.10 |
| Job 21–42 | 1.54 |
| **Isa 49–54** | **6.73** |
| **Jer 11–20** | **4.67** |
| Ps 22–41 | 3.61 |
| Ps 69–88 | 2.99 |

- **By density, Job is not distinctive for Lam 3.**
- Job also touches Lam 1, 2 and 4 at least as densely as Lam 3 (contacts per 100 words: Lam 1, 7.45; Lam 2, 6.82; Lam 3, 6.04; Lam 4, 8.49).
- What *is* distinctive is the concentration of exclusive pairs in Lam 3:7–30. But Lam 3 has equally exclusive matches with Jer 20:7, Isa 50:6, Ps 143:3, Ps 77:8 and Ps 88:7.
- **Lam 3 is a mosaic of exclusive contacts with several lament corpora. Job is one of its larger pieces, not its frame.** `[I]`

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Possible | relative dating open |
| Volume | Strong (3:12–13; 3:14b; 3:30); Moderate (3:7–9; 3:15); Weak (3:1, 43–44; 4:21) | — |
| Recurrence | Strong | Job 16:10–13 alone meets Lam 3:12, 13, 30 and 2:11, 16 |
| Thematic coherence | Strong | God as archer, the walled-in sufferer, the mocked man |
| Historical plausibility | Possible | pooled lament language explains equally |
| History of interpretation | not checked | — |
| Satisfaction | Possible | "in the images of Job" overstates the case |

**Verdict:** **Confirmed with nuance.** The pairs are real and exclusive; the frame is overstated.
**Book-overview action required:**

- Replace "in the images of Job" with **"Lam 3 is a mosaic: Job 16, 19 and 30 supply three exclusive images, alongside Jer 20:7, Isa 50:6 and Pss 77, 88, 143"**.
- Correct Job 9:18's noun.
- Drop סכך at 3:43–44.
- Name the rivals at each point (Isa 50:6 for 3:30; Jer 20:7 for 3:14; Hos 2:6 [Heb 2:8] for 3:9).
- Attach Uz to Jer 25:20 rather than Job 1:1.
- Add Job 19:9 ~ Lam 5:16, Job 19:7 ~ 3:8 and Job 16:9, 13 ~ 2:16, 11.
- Re-rate: **moderate–high** for the three pairs; **moderate** for Job overall.
- **For the Job overview:** its Lam 3 row holds on 3:12 and 3:30, and only partly on 3:7, 9.

---

### Claim C3: Lam 2:15 LXX supplies the "passers-by" of Matt 27:39 // Mark 15:29 (queue #8)

**Source:** Intertextual Map (New Testament); Christological Trajectory, point 4. Overview rating: **moderate–high**.
**Claim:** Ps 22:7 [Heb 22:8] supplies the head-wagging, "but only Lamentations (in the Greek) supplies the passers-by".

**Findings.**

- **The claim holds in its narrowest form.** Lam 2:15 is the only verse in Swete that combines παραπορεύομαι ("pass by") with κινέω … κεφαλήν ("shake the head"). `[T]`
- **Jer 18:16 gives the same image with a sister verb.** It reads πάντες οἱ **διαπορευόμενοι** αὐτῆς … **κινήσουσιν τὴν κεφαλὴν αὐτῶν** ("all who pass through it … will shake their head"), with "their head" exactly as in Lam 2:15. `[T]`
- **Jer 18:16 is also the only rival in the Hebrew.** Only Jer 18:16 and Lam 2:15 combine עבר ("pass by") with a head-shaking verb (נוד/נוע, "shake") in adjacent verses. `[T]`
- **The participle itself is not unique to Lamentations.** οἱ παραπορευόμενοι ("those passing by") also occurs at Ps 79:13 [Eng 80:12] and Jer 19:8. `[T]`
- **The Gospels lack ὁδόν ("way").** `[T]`
- **Ps 22 frames the whole crucifixion scene** (Matt 27:35, 39, 43, 46). Mark's Οὐά ("Aha!") and the temple saying have no match in Lamentations. `[T]`

| Hays | Score | Reasoning |
|---|---|---|
| Availability | Strong | the Greek Lamentations was available |
| Volume | Possible | two items shared; both natural roadside vocabulary; ὁδόν absent |
| Recurrence | Weak | no other Lamentations echo in the Passion scene |
| Thematic coherence | Possible | mocked Jerusalem beside the temple taunt; Jer 18:16 and 19:8 share it |
| History of interpretation | not checked | — |
| Satisfaction | Possible | — |

**Verdict:** **Needs reframing.**
**Book-overview action required:**

- Replace "only Lamentations supplies the passers-by" with **"the participle and the head-wagging coincide only in Lam 2:15 LXX; Jer 18:16 LXX gives the same image with διαπορευόμενοι ('those passing through'); Ps 22 governs the scene"**.
- Re-rate: **low–moderate**.
- In the Christological Trajectory (point 4), soften "the passers-by of Lam 2:15 reappear" accordingly.

---

## Supplementary gate on the overview's other wording claims

These rows were not in the queue, so the main session checked their wording rather than their design. They are wording corrections, not audit verdicts.

| Overview statement | What the corpus shows | Correction |
|---|---|---|
| Ps 143:3 at Lam 3:6 — "identical", "verbatim, four lemmas" | The four words are identical, but **the first two are reversed**: הוֹשִׁיבַנִי בְמַחֲשַׁכִּים ("he has made me dwell in dark places") in the psalm, בְּמַחֲשַׁכִּים הוֹשִׁיבַנִי in Lam 3:6. כְּמֵתֵי עוֹלָם ("like those who have long been dead") is found only in these two verses. The Greek is reordered in the same way | Say "verbatim, with the first two words reversed". The rating stays high |
| Amos 5:18, 20 at Lam 3:2 — חֹשֶׁךְ וְלֹא־אוֹר ("darkness and not light"), "phrase" | The phrase stands at **Amos 5:18, Job 12:25 and Lam 3:2**. Amos 5:20 has the two words, but not as the phrase | Add Job 12:25 as a rival; cite Amos 5:18 for the phrase |
| 1 Kgs 9:8 at Lam 2:15 — Jer 19:8 and 49:17 "share both verbs" | עבר ("pass by") + שׁרק ("hiss") occurs in six verses: 1 Kgs 9:8; Jer 19:8; 49:17; **50:13**; **Zeph 2:15**; Lam 2:15 | Add Jer 50:13 and Zeph 2:15. Pooled; moderate rather than high |
| Hos 2:11 [Heb 2:13] at Lam 2:6 — מוֹעֵד ("appointed feast") + שַׁבָּת ("sabbath"), moderate–high | The pair occurs in nine verses | Re-rate moderate |
| Zeph 2:2–3 at Lam 2:22 — יוֹם אַף־יְהוָה ("the day of the LORD's anger"), "the same phrase" | Confirmed: Zeph 2:2, 3 and Lam 2:22 only | Stands |
| Ps 88:6 [Heb 88:7]; Ps 102:12 [Heb 102:13]; Isa 24:17; Ezek 27:3; Jer 8:11, 21 | All confirmed as stated. בּוֹר תַּחְתִּיּוֹת ("the lowest pit") has a different preposition in Lamentations. Ps 102:12 is near-verbatim, with כִּסְאֲךָ ("your throne") for זִכְרְךָ ("your name") | Stand |

---

## What the audit adds that the overview missed

The auditors were told to report any partner more distinctive than the claims in front of them. The most important finding of the audit is here. **Every row below is verified wording; none has yet been audited as design.**

1. **Jeremiah 14 is Lamentations' densest partner in the Latter Prophets, and the overview does not have it as a live source.**
   - Against Lam 1–2 it is the **top chapter of 219** (1.045 rare contacts per verse).
   - Its 7-verse window is the top window of 5,231.
   - **Jer 14:17 alone is the exclusive partner of three Lamentations verses:** 2:18 (tears running down day and night); 2:13 (שֶׁבֶר + גָּדוֹל + בְּתוּלָה, "a great ruin … the virgin"); 3:48 (eyes running down over the ruin).
   - Jer 14:19 is the exclusive partner of Lam 5:22 (מָאֹס מָאַסְתָּ, "you have utterly rejected").
   - Jer 14 is also the densest confession in the Daniel 9 comparison (17 Lamentations verses linked).
   - **Jer 8:18–23 [Eng 8:18–9:1]** is second.
   - *Recommended:* **live, high on words.**
2. **Nahum 3 equals Isaiah 47 as a foreign-city partner.** Its contacts are exclusive:
   - Nah 3:10 ~ Lam 1:5 (infants going into captivity);
   - Nah 3:10 ~ Lam 2:19 (infants at the head of every street);
   - Nah 3:11 ~ Lam 4:21 (תִּשְׁכְּרִי, "you will be drunk");
   - Nah 3:7 ~ Lam 2:13 ("who will grieve … comforters");
   - Nah 3:5 ~ Lam 1:9 (the skirts).
3. **Ps 77.** 3:31 answers Ps 77:8 [Eng 77:7] exclusively ("Will the Lord reject forever?" — "the Lord will not reject forever"). In the window scan, the densest 14-verse windows of the whole Psalter against Lam 1–3 are those covering Ps 77 (windows beginning Ps 76:12–77:3, Hebrew numbering). *Unaudited; queued.*
4. **Ps 89 for Lam 2** — נאר ("spurn"); Lam 2:17 ~ Ps 89:43 [Eng 89:42]; Ps 89:5 [Eng 89:4] ~ Lam 5:19 (see C1).
5. **Isa 50:6 for Lam 3:30**, as exclusive as Job 16:10. It bears directly on the Christological Trajectory's "man under the rod".
6. **Ezek 19:4, 8 for Lam 4:20** (see B4), with Ps 9:16 as the only other Greek match.
7. **Hab 2:16 and Nah 3:11 for the cup at Lam 4:21**, closer in wording than Isa 51.
8. **Job 19:9 for Lam 5:16** (עֲטֶרֶת רֹאשׁ, "the crown of the head"). **Job 19:7 for Lam 3:8.** **Job 16:9, 13 for Lam 2:16, 11.**
9. **The root יגה ("cause grief")** — five of its eight occurrences in the Hebrew Bible are in Lamentations, and Isa 51:23 ~ Lam 1:12 is exclusive. A candidate Leitwort for the sweep.
10. **LXX Lam 2:13 reads ποτήριον ("cup", = כּוֹס) and "who will save you"**, which brings Isa 51:17–19 into the Greek. This is an additional row for *The Greek Text of Lamentations*.
11. **Hos 2:6 [Heb 2:8] for Lam 3:9** (גדר + דֶּרֶךְ, "wall up" + "way", exclusive).

---

## Confidence Change Propagation

Every section of the overview where each change must be applied:

| Allusion / claim | Previous | New | Sections to update |
|---|---|---|---|
| Deut 28 (whole) | high, "six places" | moderate–high (4:16; 1:3); low–moderate (structuring) | Intertextual Map (Torah); Canonical Position — *Presupposes*; colophon live-source list; health note |
| Deut 28 at 4:10; 4:19 | listed | removed (2 Kgs 6:29; Jer 4:13) | Intertextual Map; *Presupposes* |
| Lev 13:45–46 | high / moderate | moderate (4:15); low (1:1) | Intertextual Map; *Presupposes* |
| Concentric frame | moderate–high | low–moderate; 2 ↔ 4 phrases moderate | Structural Arc Map — *binding device*; Microscript test (no change needed); health note |
| Daniel 9 handoff | moderate–high | moderate (thematic); low (lexical) | Canonical Position — *Handoff* |
| Isa 47 | high (1:9); moderate–high (pattern) | moderate–high (1:9); moderate (chapter); "every one" withdrawn | Intertextual Map (Isaiah); live-source list |
| Isa 51:17–23 | high, "densest … in the canon" | moderate–high, as Isa 51:17–52:2, "densest of the reversal passages" | Intertextual Map (Isaiah); Christological Trajectory (the cup); Greek section (add 2:13 ποτήριον, "cup") |
| Jer 31:18 at 5:21 | high | moderate–high; 2:18 → Jer 14:17 | Intertextual Map (Jeremiah); Echo Table — no change (internal rows stand) |
| Ezek net at 1:13 | moderate–high | low (1:13); moderate (4:20 ~ Ezek 19:4, 8) | Intertextual Map (Ezekiel); Christological Trajectory (point 3) |
| Ps 89 | high, Lam 4–5, "six places" | moderate–high for **Lam 2**; low–moderate for Lam 4–5 | Intertextual Map (Writings); Christological Trajectory (point 3 "six times"); live-source list; colophon |
| Job | high / moderate–high | moderate–high (three pairs); moderate overall | Intertextual Map (Writings); Canonical Position — final paragraph; live-source list |
| Matt 27:39 // Mark 15:29 | moderate–high | low–moderate | Intertextual Map (NT); Christological Trajectory (point 4) |
| Hos 2:11 [Heb 2:13] at 2:6 | moderate–high | moderate | Intertextual Map (Twelve) |
| 1 Kgs 9:8 at 2:15 | high | moderate (pooled) | Intertextual Map (Former Prophets) |
| **Jer 14** | absent | **live; high on words** | Intertextual Map (Jeremiah); live-source list; Preaching Traps 5 (the Jeremian vocabulary) |
| **Nah 3** | absent | moderate–high (exclusive contacts) | Intertextual Map (Twelve) |

---

## Recommended book-overview revisions

The audit supports a **v0.2.0 interim upgrade**, in the pattern of the Job and Matthew overviews. Nothing here is a Finalise pass; the digs have not yet run.

1. **Correct the three factual errors.**
   - פְּרִי ("fruit") is at 2:20 only, not 4:10.
   - Job 9:18's noun is מַמְּרֹרִים ("bitterness"), not מְרֹרִים.
   - Prophets are at 4:13, not 4:16.
2. **Correct the wording of two stated parallels:** Ps 143:3 is reordered, not identical; and Amos 5:18 shares the phrase with Job 12:25.
3. **Rewrite the binding device** as a formally centred book with poem 2 as a lexical hub. Keep the word-count table, the verse midpoint and the 3:31–33 centre, naming the counting unit.
4. **Rebuild the live-source list.** Strike "Psalms 22, 74 and 89" in that form, Deuteronomy 28 as a six-place source, and "Job behind Lam 3" as a frame. The new list:
   - **Jeremiah**, with Jer 14 and 8 leading, then 20 and 31;
   - **Isaiah 47 and 51:17–52:2**;
   - **Nahum 3**;
   - **Ps 89 (for Lam 2)**;
   - **Job 16 and 19 (for Lam 2, 3 and 5)**;
   - **Deut 28 (4:16; 1:3)**.
   - Move Ps 22, 74 and 77 to the pooled lament family.
5. **Recast the *Handoff*** as thematic and canonical juxtaposition with the confessional prayers, Dan 9 among them.
6. **Christological Trajectory.** Point 3 rests on Lam 4:20 with Ezek 19:4, 8, and on Lam 2 with Ps 89 — not on "six times". Point 4 adds Isa 50:6 beside Job 16:10 at 3:30. The passers-by of Matt 27:39 become a low–moderate touch.
7. **Add LXX 2:13** (ποτήριον, "cup"; "who will save you") to *The Greek Text of Lamentations*.
8. **Re-rate the rows** as listed in the propagation table.

**The Preaching Traps, the Pulpit Notes, the Echo Table (internal, lemma-gated) and the Preaching Units stand unchanged.** None rested on an audited claim except trap 5's "Jeremian vocabulary", which the audit strengthens.

---

## New candidates for the queue

These were surfaced by the audit and are not yet audited as design: Jer 14 as a live source (14:17, 19); Jer 8:18–23; Nah 3 (3:5, 7, 10, 11); Ps 77 (3:31 and the Lam 1–3 window); Isa 50:6 at 3:30; Ezek 19:4, 8 at 4:20; Hab 2:16 and Nah 3:11 at 4:21; Hos 2:6 [Heb 2:8] at 3:9; the root יגה ("cause grief") as a Leitwort.

---

## Critical assessment — the gaps in this audit

1. **No history of interpretation.** No commentary was consulted. Every Hays row for that criterion is empty, and the Logos pass recommended at the overview's colophon is still owed. A Research Assistant round on Jer 14 and Lamentations, Ps 89 and Lam 2, and LXX 2:13 would fill the largest gap.
2. **The baselines measure lemma co-occurrence, not syntax or sound.** They under-weight single rare words and miss pairs that straddle verse boundaries (Lam 3:12–13 had to be hand-tested). They say how dense a partner is, never that one text used another.
3. **Size sensitivity.** Rates per comparator verse penalise large books (Job is 1,070 verses). The auditors used several normalisations (per comparator verse, per Lamentations word, windowed), and Job comes out mid-band on all of them. But no single normalisation is neutral.
4. **The direction of dependence is open throughout.** "Shares the wording of" is all any row may say. In particular, the Isaiah and Jeremiah results do not tell us which text is answering which.
5. **Apparatus spread was not checked.** That applies to the BHS deletion proposal at 4:15, the qere at 5:21, and the LXX *Vorlage* at 2:13. Each is tagged `[unchecked — apparatus spread]`, and none may carry a sermon headline until a library pass has been made.
6. **The rival search was lexical.** Conceptual parallels with no shared vocabulary would not be found by it.
7. **The auditors over-ran the length guide** (about 4,300–4,500 words each, against 3,500), largely in their tables. Nothing was trimmed from their findings.

---

## Text-First Declaration

**Secondary sources present in context:** the book overview under audit (withheld from the auditors); the earlier Job overview (named to Auditor C as a claim to test, not relied on). No commentaries.
**Auditors blind:** confirmed. Each worked from neutral claim statements, without the overview's ratings or reasoning, and was barred from the Lamentations folder and from the other auditors' files.
**Passage text:** verified from the WLC throughout; every Hebrew quotation above was taken from the corpus.
**Chains verified:** about 140 lemma and phrase searches across the three auditors. **56 decisive findings were re-run by the main session, and all 56 reproduced exactly.** Positive controls ran in every session (Ruth חֶסֶד; Exod 40:35 שָׁכַן; Lam 4:15 טָמֵא; Lam 1:9 אַחֲרִית; Isa 51:19 נחם; the Lam 5:21 morphology), and every "only" result in this report sits beside one.
**Apparatus findings:** three — the 4:15 deletion proposal, the 5:21 qere and the LXX *Vorlage* at 2:13. Each is cited as BHS prints it, and each is tagged `[unchecked — apparatus spread]`.
**Warrant:** every verdict rests on `[T]` corpus observations; design judgements are `[I]`. No `[S]` finding carries a verdict.

**Health note.** The overview's single verbal links were sound; its design claims were not. That is the same result as the Mark, Matthew and Job audits. Its biggest miss is Jeremiah 14, which this audit puts at the top of Lamentations' intertextual map. The v0.2.0 upgrade should be made before the sweep.
