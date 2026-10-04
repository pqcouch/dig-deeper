# Claim Audit 2: Lamentations

**Passages audited:** the whole book. The claims tested are the 14 open queue items L2–L15: nine candidates raised by the first claim audit and six raised by the whole-book sweep, counting L10 twice as both pair and design
**Date:** 4 October 2026
**Purpose:** to settle the sweep's new design claims and the audit-1 candidates before any ⭐ solo dig or sermon rests on them. Queue trigger 1 fired at 15 queued, after the sweep
**Documents under test:** `book-overview-lamentations.md` v0.2.0; `dig-deeper-lamentations-sweep.md` (3 October 2026); `dig-deeper-lamentations-claim-audit.md` (audit 1), for its new-candidate list
**Not re-tested:** L1, Jer 14 as a live source. Audit 1 settled its wording, and its direction of dependence is a question for the library, not for a lemma count

**Primary texts:**

- WLC Hebrew with the lemma index, for every count. The matcher is identical to `find.py`.
- Swete LXX, for observation.
- Rahlfs LXX Lamentations and the BHS apparatus (Logos exports), as the citation of record.
- SBLGNT is not needed: no New Testament claim was in scope.

**Every count below is a WLC lemma or phrase count unless stated.** References are in English numbering, with the Hebrew in brackets where it differs.

Warrant tags: `[T]` derivable from the text itself · `[I]` a reasonable inference from the text · `[S]` supplied by a secondary source, held provisionally · `[S: audit]` a verdict of this or the earlier audit.

---

## What this audit tested, and how

**Three blind auditors, run one after another.** None saw the overview, the sweep or the first audit. Each received only:

- a neutral brief;
- the claims, restated;
- the staged corpus;
- a shared lemma library (`alib.py`), plus `contacts.py`, the Round 7 draft density scanner.

Each was told to try to **break** its claims, not confirm them.

| Auditor | Claims | Kind |
|---|---|---|
| **A** | L10, L11, L15 | The sweep's three **design** claims, each with a chance baseline |
| **B** | L2, L3, L7, L12, L14 | Prophets: Jer 8; Nah 3; the cup at 4:21; Zech 1:6; Isa 1:7 |
| **C** | L4, L5, L6, L8, L9, L13 | Writings and lexical: Ps 77; Isa 50:6; Ezek 19; Hos 2:6 [Heb 2:8]; the verb יגה ("cause grief"); Ps 73 |

**Method for each claim.**

1. Check the wording on both sides in Hebrew, and in Greek where relevant.
2. Count how rare the shared lemma set is (`hall`).
3. Search for rival sources.
4. For design claims, run a chance baseline.
5. Score the seven Hays criteria. *History of interpretation* is "not checked" throughout, since no commentary was consulted.
6. Give a verdict and a recommended confidence.

Each auditor ran a positive control before reporting any nil or "only".

**The main session's gate.**

- **24 of 24 spot checks reproduced** from the auditors' lists, including the A1 baseline (112 of 151 windows).
- One open test was run here: the doubled-verb baseline that Auditor A named but did not run (see *Supplementary gate*).
- Auditor C was interrupted by a usage limit and resumed from its own scripts. Its report is complete.

**Length.** The three reports run to about 4,100, 5,100 and 4,200 words, over the 3,500 guide. Most of the excess is glosses and rival tables, and nothing was trimmed from the findings. They are kept in the session workspace (`auditor-A.md`, `auditor-B.md`, `auditor-C.md`, with their scripts).

---

## Summary

| # | Claim | Verdict | Recommended confidence |
|---|---|---|---|
| L2 | Jer 8:18–23 [Eng 8:18–9:1] with 2:11; 3:48 | **Confirmed with nuance** | moderate–high |
| L3 | Nah 3 as a foreign-city partner equal to Isa 47 | **Needs reframing** | moderate (chapter); two of the five stated contacts fall |
| L4 | Ps 77:8 [Eng 77:7] with 3:31 | **Confirmed with nuance** | moderate–high (3:31–32); the "densest psalm" claim reframed |
| L5 | Isa 50:6 with 3:30 | **Confirmed with nuance** | moderate; Job 16:10 is an equal partner |
| L6 | Ezek 19:4, 8 with 4:20 | **Needs reframing** | low–moderate in the Hebrew; moderate as a theme, strengthened in the Greek |
| L7 | The cup at 4:21: Hab 2:16 and Nah 3:11 the closest | **Needs reframing** | moderate (Jer 25:15–29 first, then Hab 2:16); low–moderate (Nah 3:11) |
| L8 | Hos 2:6 [Heb 2:8] with 3:9 | **Confirmed with nuance** | moderate; **Job 19:6–8 is the better partner** (moderate–high) |
| L9 | יגה ("cause grief") as a Leitwort | **Confirmed with nuance** | moderate–high, as a *verb* |
| L10 | The coda 5:19–22 "built line by line" | **Needs reframing** | pairs moderate–high (5:19, 21, 22) and low–moderate (5:20); design low–moderate, with one surviving strand |
| L11 | Ch. 3 takes up poem 1's vocabulary "item by item" | **Needs reframing** | moderate as an echo localised in 3:19–33; low as a whole-poem programme |
| L12 | Zech 1:6 with 2:17 | **Confirmed with nuance** | moderate–high (verbal contact); low–moderate ("the post-exilic generation confessing") |
| L13 | Ps 73:14, 26 with 3:22–24 | **Needs reframing** | low–moderate; Ps 119:57 leads |
| L14 | Isa 1:7 with 5:2, 18 | **Uncertain — tending to discard** | low |
| L15 | Partners "line up by poem" — a mosaic by subject | **Needs reframing** | low–moderate (mosaic); moderate–high (the individual top contacts) |

| Verdict | Count |
|---|---|
| Confirmed | 0 |
| Confirmed with nuance | 7 (L2, L4, L5, L8, L9, L12, and the verb-level part of L10) |
| Needs reframing | 7 (L3, L6, L7, L10 design, L11, L13, L15) |
| Uncertain | 1 (L14) |
| Discard | 0 as a whole claim. **Two sub-contacts are discarded:** Nah 3:7 ~ 2:13 and the Lam 3 partnership for Ps 73's "portion + fail" |

**In one sentence:** the single verse contacts mostly stand, often with a better rival beside them, but **every design claim the sweep made falls back to moderate or below once a chance baseline is run**. The exception is one localised signal: poem 1's vocabulary clusters in 3:19–33, the turn and the centre.

---

## Claims Audited

### L10 — the coda 5:19–22 "built line by line from other prayers" (Auditor A)

**Source:** the sweep, Unit 7 finding 3 (*synthetic*), and Solo-Dig Priority 2.

**Wording.**

| Line | Partner the sweep named | What the audit found |
|---|---|---|
| **5:19** | Ps 102:13 [Eng 102:12] | **Near-verbatim.** But the sweep's lemma set (YHWH + לְעוֹלָם, "forever" + ישׁב, "sit") is in **11 verses**, so it is not rare. The rarity lies in דּוֹר וָדוֹר ("generation to generation") and the word order. |
| | Ps 89:5 [Eng 89:4] | כִּסֵּא ("throne") + דּוֹר ("generation"): **2 verses**. |
| | *Rival:* **Ps 9:8 [Eng 9:7]** | YHWH + עוֹלָם + ישׁב + כִּסֵּא: **2 verses** (Ps 9:8; Lam 5:19). As exclusive as the named partners. |
| **5:20** | Isa 49:14 (שׁכח, "forget" + עזב, "forsake") | The pair is in **4 verses**: idiom. |
| | *Rival:* **Ps 44:24–25 [Eng 44:23–24]** | לָמָּה ("why") + נֶצַח ("forever") + שׁכח within one verse occurs only there and at Lam 5:20. **The better partner.** |
| **5:21** | Jer 31:18 | Doubled שׁוב (hiphil + qal; "restore … return"): **2 verses**. **Ketiv** וְנָשׁוּב, qere וְנָשׁוּבָה ("that we may return"). Ps 80:4, 8, 20 [Eng 80:3, 7, 19] have the exact form הֲשִׁיבֵנוּ ("restore us"). |
| **5:22** | Jer 14:19 | Infinitive absolute + finite מאס ("utterly reject"): **2 verses**. **Jer 14:19 is a question**; Lam 5:22 is a כִּי אִם ("unless") clause. |
| | *Rival for 5:22b:* **Isa 64:8 [Eng 64:9]** | קצף ("be angry") + עַד ("to") + מְאֹד ("very"): **2 verses**. |

**Baseline.** The sweep's test was that every line has its own exclusive or near-exclusive partner (at most four Hebrew Bible verses).

- **112 of 151** sliding four-verse blocks of Lamentations pass that test (74 %).
- Chance alone predicts 72 %.
- Eight control books range from 57 % to 100 %.

**So the test does not single out the coda.** On a weighted measure of rarity the coda ranks 31st of 151 blocks: in the top fifth, but not exceptional. `[T]`

**What the baseline cannot see — and what survives.** The doubled-verb figures of 5:21 and 5:22 are invisible to a lemma-set count. See the *Supplementary gate*: of the doubled-verb figures in Lamentations, **only 5:21 and 5:22 have an exclusive partner, and both partners are in Jeremiah (31:18; 14:19)**. That is a real, if small, design signal.

**Greek.**

- The Greek keeps the Ps 102 link and tightens it: σὺ δέ ("but you") = וְאַתָּה, as BHS notes.
- It keeps Jer 31:18 (ἐπίστρεψον, "restore").
- It **loses the Jer 14:19 wording** (ἀπωθούμενος ἀπώσω against ἀποδοκιμάζων ἀπεδοκίμασας, two different verbs for "reject"). Only the doubled figure survives.

**Hays.**

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Possible | Direction open; none of the partners is datable against Lamentations from the text |
| Volume | Strong (5:19, 21, 22) · Possible (5:20) | Three exclusive figures; 5:20 rests on a common pair |
| Recurrence | Possible | Jer 31 and Jer 14 recur elsewhere in the book |
| Thematic coherence | Strong | A communal-lament coda |
| Historical plausibility | Possible | |
| History of interpretation | not checked | |
| Satisfaction | Possible | The "line by line" programme over-reads a book where most blocks look like this |

**Verdict: Needs reframing.** Drop "built line by line" and "each line its own partner". Say instead:

- the coda is dense in communal-lament idiom;
- 5:19 is near-verbatim Ps 102:13, with Ps 9:8 and Ps 89:5 for the throne;
- 5:20's best partner is Ps 44:24–25;
- **5:21 and 5:22 end the book in two rare Jeremian figures (31:18; 14:19)**, the one strand of design that survives;
- 5:22b matches Isa 64:8.

**Confidence:** pairs moderate–high (5:19, 21, 22) and low–moderate (5:20); the design as a whole low–moderate; the Jeremian pair at 5:21–22 moderate.

### L11 — chapter 3 takes up poem 1's vocabulary "item by item" (Auditor A)

**Source:** the sweep's Convergent 1 and Headline 1; Solo-Dig Priority 1.

**Wording.**

| Item | Poem 1 | Poem 3 | Check |
|---|---|---|---|
| יגה ("cause grief") | 1:4, 5, 12 | 3:32, 33 | ✓. BHS reads 1:4 with the Greek as נְהוּגוֹת ("led away") |
| בָּדָד ("alone") + ישׁב ("sit") | 1:1 | 3:28 | ✓ (5 verses in the Hebrew Bible) |
| עֹל ("yoke") | 1:14 | 3:27 | MT ✓. **BHS marks 1:14a as doubtful ("dub")**: many manuscripts and the Greek read נִשְׁקַד עַל ("bound … upon"), not "yoke". The yoke there rests on the Lucianic Greek and Symmachus |
| עֳנִי ("affliction") + מָרוּד ("wandering") | 1:7 | 3:19 | ✓. **Exclusive in the Hebrew Bible (2 verses)** |
| "See, O LORD" | 1:9, 11, 20 | 3:59–60 | **Wrong as a 1 → 3 item.** Ch. 3 has the perfect ("you have seen"). The imperative recurs at 2:20 and 5:1 |
| **Missed:** יגה + רֹב ("abundance") | 1:5 | 3:32 | **Exclusive in the Hebrew Bible (2 verses).** "Afflicted her **for the multitude** of her transgressions" → "according to **the abundance** of His lovingkindness". The Greek keeps it. **The strongest single link** |

**Baseline (poem against poem).** The count is lemmas occurring at most three times in Lamentations and shared by both poems, as a ratio to chance.

| Pairing | Shared | Ratio |
|---|---|---|
| 1–3 | 20 | 0.78 |
| 1–2 | 19 | 0.74 |
| 2–3 | 21 | 0.81 |
| 1–5 | — | the highest after size adjustment |

**Poems 1 and 3 share no more rare vocabulary than the other pairings.** `[T]`

**The real signal.** The poem-1 items that ch. 3 does share **cluster in 3:19–33**:

- 62 %, 41 % or 33 % of them, depending on the rarity cut-off;
- against an expected 23 % (3:19–33 is that share of ch. 3);
- p ≈ 0.02–0.10.

Poem 2's shared items do **not** cluster there (20–25 %). `[T]` for the counts; `[I]` for the reading.

**Hays:** Volume Strong for 1:5/3:32 and 1:7/3:19, Weak for the yoke and "See"; Recurrence Possible; Thematic coherence Strong; Satisfaction Strong for the centre, Weak for "item by item".

**Verdict: Needs reframing.** Restate it as follows: **the turn and the centre (3:19–33) answer poem 1 in its own words.** The evidence is:

- עֳנִי + מָרוּד (1:7 → 3:19);
- יגה + רֹב (1:5 → 3:32);
- בָּדָד (1:1 → 3:28);
- the verb יגה (1:5, 12 → 3:32–33).

Ch. 3 does not take up poem 1 as a whole. Drop "See, O LORD" from the list, and footnote the yoke as textually doubtful at 1:14.

**Confidence:** moderate (localised); low (whole-poem).

### L15 — the partners "line up by poem": a mosaic by subject (Auditor A)

**Source:** the sweep's Convergent 5.

**Density scans, poem by poem, against all chapters of the Hebrew Bible.**

| Poem | Supported | Not supported |
|---|---|---|
| 1–2 | Jer 14 (1st), Nah 3 and Isa 47 (2nd–3rd) | **Ps 89 ranks 307th** (its exclusive contacts are verse-level, not density) |
| 3 | Ps 143 (1st); at the looser setting Ps 77, Job 16, Jer 20 and Ps 88 reach the top 20 | Job 19, Job 30, Isa 50 weak |
| 4 | Isa 52 (2nd) | Deut 28, Ezek 19 and every cup text weak or absent. **Zeph 3 is poem 4's top partner** — missed |
| 5 | Isa 64 (1st), Jer 31 (5th) | Ps 102, Isa 49 and Isa 63 weak (Ps 102's contact is a verbatim line the scan cannot see) |

- **Jer 14 cuts across the poems.** It ranks 1st, 2nd and 3rd against poems 1–2, 3 and 4. It is the book's pervasive partner, not a partner for the city.
- **Baseline.** The two halves of the *same* poem (3:1–33 against 3:34–66) share only 1–4 of their top-20 partner chapters. Different poems share 0–6. Distinct top lists per poem are what noise produces.

**Verdict: Needs reframing.** Report the supported contacts poem by poem as observations, not as an alignment. Move Jer 14 out of the "city" column. Label the unsupported rows "verse-level only". Add Zeph 3 for poem 4 (unaudited).

**Confidence:** mosaic low–moderate; individual top contacts moderate–high.

### L2 — Jer 8:18–23 [Eng 8:18–9:1] (Auditor B)

- שֶׁבֶר בַּת־עַמִּי ("the ruin of the daughter of my people") occurs **only in Jeremiah and Lamentations**: 5 verses by phrase, 6 by lemma with Jer 14:17.
- **Missed, and decisive:** לִבִּי דַוָּי ("my heart is faint") occurs only at **Jer 8:18 and Lam 1:22**. דַּוָּי itself is in 3 verses (Isa 1:5; Jer 8:18; Lam 1:22).
- **Rival:** Jer 14:17–19 is stronger for 2:18, 3:48–49 and 5:22. It ranks 1st of 858 chapters; Jer 8 ranks 7th.

**Verdict: Confirmed with nuance — moderate–high.** Jer 8:18–23 is a real partner, second to Jer 14. Add 1:22 to its rows.

### L3 — Nahum 3 equal to Isa 47 (Auditor B)

| Contact | Result |
|---|---|
| Nah 3:10 ~ 1:5 (עוֹלָל, "infant" + הלך, "go" + שְׁבִי, "captivity") | **Exclusive (2 verses).** But the wording needs correcting: in Nahum the *city* goes into captivity and the infants are dashed to pieces |
| Nah 3:10 ~ 2:19 ("at the head of every street") | The phrase is in 4 verses, with **Isa 51:20** an equal rival. BHS marks part of 2:19 as an addition ("c–c add"); which words is unchecked |
| Nah 3:11 ~ 4:21 (תִּשְׁכְּרִי, "you will be drunk") | **Exclusive (2 verses)**; the Greek keeps it |
| **Nah 3:7 ~ 2:13 ("who will grieve … comforters")** | **Discard.** Lam 2:13 has no נוד ("grieve"); the lemma never occurs in Lamentations (control: `hhas('Nah 3:7','5110')` True). The partner of 2:13 is Isa 51:19 |
| Nah 3:5 ~ 1:9 (skirts) | **Not exclusive.** Jer 13:22, 26 share the image; Jer 13:26 is almost identical to Nah 3:5 |

- **Density:** Nah 3 ranks 5th and Isa 47 3rd of 858 chapters in this auditor's scan (both above most foreign-city oracles). 6 of Nahum's 15 rare pairs come from the single verse 3:10.

**Verdict: Needs reframing — moderate** for the chapter as a comparable partner, resting on 3:10 and 3:11. Strike the 3:7 contact. Demote 3:5 to shared idiom with Jer 13. Correct the 1:5 wording.

### L7 — the cup at 4:21 (Auditor B)

- **Missed:** "the land of Uz" (עוּץ + אֶרֶץ) occurs in only **3 verses**: Job 1:1, **Jer 25:20** and Lam 4:21.
- **Jer 25:15–29** brings together the cup, drunkenness, Edom and Uz, and shares the most lemmas with 4:21 (7). **It ranks first.**
- **Hab 2:16** is the closest in syntax: the cup coming "to you", plus גַּם ("also"); the set גַּם + כּוֹס is exclusive (2 verses). The Greek strengthens it, since both read "the cup of the Lord" — `[unchecked]` against Rahlfs for Lam 4:21.
- **Nah 3:11 has no cup at all**; it shares only the verb.

**Verdict: Needs reframing.** Order the partners as Jer 25:15–29 → Hab 2:15–16 → Jer 49:12 / Isa 51:17–22 → Nah 3:11 (verb only). **Confidence:** moderate; low–moderate for Nah 3:11.

### L12 — Zech 1:6 with 2:17 (Auditor B)

- The four-verse lemma set (זמם, "purpose" + עשׂה, "do" + יהוה) is correct. In **Gen 11:6** it is the people who purpose, not God.
- **Missed:** צוה ("command") occurs in both verses. With it, the set is **exclusive to Zech 1:6 and Lam 2:17**. That makes the contact stronger than the sweep claimed.
- **Rivals:** Jer 51:12 is close. Zech 8:14 pairs instead with Jer 4:28 (exclusive).
- **Zechariah is otherwise not a dense partner** of Lamentations (Zech 1, 7 and 8 rank 297th, 445th and 124th).
- **Who confesses in Zech 1:6b is not settled by the text**: the nearest antecedent is "your fathers" (1:4–6).

**Verdict: Confirmed with nuance.** Moderate–high for the verbal contact. Low–moderate for the sweep's gloss "the post-exilic generation confessing in Lamentations' own idiom". Reword it as "a returnee-era prophetic text that uses the same confession of a word purposed, commanded and done".

### L14 — Isa 1:7 with 5:2, 18 (Auditor B)

- The scan finds **no rare contact** between Isa 1 and Lam 5. Isa 1:4–9 shares only 2 distinctive lemmas with Lam 5, and the claim's three words are 16 verses apart in Lamentations.
- Jer 2:12–25, Ps 79 and **Isa 63:15–64:11 [Eng 63:15–64:12]** each share 6–7. Isa 64 ranks first against Lam 5.
- Only the Greek converges a little: ἀλλότριοι ("strangers") plus a verb of overturning.

**Verdict: Uncertain, tending to discard — low.** Isa 1:7 belongs to the shared vocabulary of a land devoured by strangers. If Lam 5 needs a prophetic partner, it is Isa 63:15–64:11.

### L4 — Ps 77:8 [Eng 77:7] with 3:31 (Auditor C)

- זנח ("reject") + עוֹלָם ("forever"): **exclusive (2 verses)**. Positive control passed.
- **Stronger than the claim:** זנח + חֶסֶד ("lovingkindness") + רחם ("compassion") within ±4 verses also occurs only in Ps 77:8–10 and Lam 3:31–32. **Lam 3:31–32 answers Ps 77:8–10 point by point.**
- **Greek:** Swete keeps the link and tightens it (εἰς τὸν αἰῶνα ἀπώσεται κύριος, "the Lord will cast off forever").
- **"Densest psalm against Lam 1–3" needs reframing.** Ps 77 is first among psalms only at one rarity setting (density 0.476, about 4.4 standard deviations), and that density comes from Lam 1–2. Against Lam 3 alone it has one contact and ranks 8th among psalms. **Ps 143:3 ~ 3:6 is the better Lam 3 partner.**

**Verdict: Confirmed with nuance — moderate–high** for 3:31–32 ~ Ps 77:8–10. Drop the window superlative.

### L5 — Isa 50:6 with 3:30 (Auditor C)

- נתן ("give") + נכה ("smite") + לְחִי ("cheek"): **exclusive (2 verses)**. The construction is the same: "give … to the one who smites".
- **Job 16:10** (לְחִי + נכה + חֶרְפָּה, "reproach") is **equally exclusive**.
- **The rest of Isa 50:4–9 shares no rare contact with Lam 3.**
- **Greek:** δίδωμι ("give") and σιαγών ("cheek") survive; the word for striking does not.

**Verdict: Confirmed with nuance — moderate.** It is a verse-level contact, not a Servant-passage source for Lam 3. It may carry Christological point 4 only as a shared posture ("type and contrast"), never as dependence.

### L6 — Ezek 19:4, 8 with 4:20 (Auditor C)

- **No shared verb or noun.**
  - The verbs for "caught" differ: Ezekiel has תפשׂ, Lamentations לכד.
  - The nouns for "pit" differ: Ezekiel has שַׁחַת, Lamentations שְׁחִית.
- **What is exclusive is the frame**, "caught in *their* pit/pits".
- **Correction to v0.2.0:** its rarity cell, "גּוֹי ('nation') + שַׁחַת ('pit'): 3 verses (Ezek 19:4, 8; Ps 9:16)", does **not include Lam 4:20**, which has שְׁחִיתוֹת. Checked: `hall(['1471','7825'])` returns Lam 4:20 alone.
- **Rival:** Ps 9:16 [Eng 9:15] uses Lamentations' own verb (לכד, "be caught").
- **Greek:** the translators make the two read almost alike ("he was caught in their corruption"). That shows how early readers heard them, not dependence.
- Ezek 19 is itself called a קִינָה ("lament", 19:1, 14), which supports a shared royal-lament theme.

**Verdict: Needs reframing.** Low–moderate as a link in the Hebrew. **Moderate as a shared theme of the captured royal lion**, strengthened in the Greek. Christological point 3 should rest on 4:20's own words and the Davidic covenant, with Ezek 19 as a parallel lament.

### L8 — Hos 2:6 [Heb 2:8] with 3:9 (Auditor C)

- גדר ("wall up") + דֶּרֶךְ ("way"): **exclusive (2 verses)**. The Greek keeps it strongly.
- **Missed, and stronger:** **Job 19:6–8**. It shares five rare words with Lam 3:1–9 — wall up, surround, cry for help, path, darkness — and the same form נְתִיבוֹתַי ("my paths"). In a sliding-window scan of the whole Hebrew Bible, Job 19 ranks **joint 1st**; Hos 2 ranks about 230th.

**Verdict: Confirmed with nuance — moderate** for Hos 2:6. **Job 19:6–8 is the better parallel for 3:1–9 (moderate–high).** This revises audit 1's C2, where Job 19:8 was weighed against 3:7 only.

### L9 — יגה ("cause grief") as a Leitwort (Auditor C)

- The verb occurs in **8 verses; 5 are in Lamentations** (1:4, 5, 12; 3:32, 33).
- **Baseline.** Only two words in a book under 400 verses reach 60 % concentration, Aramaic aside: יגה here, and עמל ("toil") in Ecclesiastes (8 of 11).
- At 1:5, 1:12 and 3:32–33 **the subject is the LORD**, and 3:32–33 answers the earlier verses (L11's יגה + רֹב strengthens this).
- **It is the verb, not the root:** the nouns of the same root (יָגוֹן, "grief"; תּוּגָה, "sorrow") do not occur in Lamentations.
- **Text:** BHS proposes נְהוּגוֹת ("led away") at 1:4 with the Greek, so the secure count may be **4 of 7**.
- Isa 51:23 ~ 1:12 (יגה + עבר, "pass by"): **exclusive**; the Greek keeps it.
- **Greek:** ταπεινόω ("humble") is used at 1:5, 12; 3:32, 33. It is the stock Greek word for "afflict", so the distinct root disappears in translation.

**Verdict: Confirmed with nuance — moderate–high.** Call it "the verb יגה", note the variant at 1:4, and note that the Greek levels it.

### L13 — Ps 73:14, 26 with 3:22–24 (Auditor C)

- **Factual error in the sweep.** "Portion + fail in one verse (Ps 73:26; Job 17:5)" does not include Lamentations, which has the two words **two verses apart** (3:22 and 3:24).
- **The exact parallel is Ps 119:57**: חֶלְקִי יְהוָה ("the LORD is my portion"), plus אָמַרְתִּי ("I have said"), matching 3:24's אָמְרָה נַפְשִׁי ("my soul says"). **Both are the ח (Heth) stanza of an acrostic**, which partly explains why the word is shared.
- **Rare three-word combinations within nearby verses:** Ps 119 has 24, Jer 9 has 9, Ps 73 has 4.
- **Greek:** 3:22–24 is absent from the Old Greek, so the Greek cannot carry the link.

**Verdict: Needs reframing — low–moderate** for Ps 73 as a specific partner. Moderate that 3:19–24 draws on a shared Psalter idiom of affliction, hope, portion and mercy, with **Ps 119:49–57 leading**.

---

## Supplementary gate on the open test

Auditor A named one test it did not run: **how often do doubled-verb figures occur across Lamentations, and do others also have exclusive partners?**

That covers the infinitive absolute with a finite verb of the same root, and the doubled שׁוב of 5:21. The main session ran it (WLC morphology):

| Verse | Figure | Hebrew Bible verses with the same figure | Partner in Jeremiah |
|---|---|---|---|
| 1:2 | בָּכוֹ תִבְכֶּה ("she weeps bitterly") | 6 | Jer 22:10 (among 5 others) |
| 1:20 | מָרוֹ מָרִיתִי ("I have greatly rebelled") | 1 (Lam only) | — |
| 3:20 | זָכוֹר תִּזְכּוֹר ("remembers well") | 3 (Deut 7:18; **Jer 31:20**; Lam 3:20) | **Jer 31:20** |
| 3:52 | צוֹד צָדוּנִי ("hunted me down") | 1 (Lam only) | — |
| **5:21** | doubled שׁוב ("restore … return") | **2** | **Jer 31:18** |
| **5:22** | מָאֹס מְאַסְתָּנוּ ("utterly rejected us") | **2** | **Jer 14:19** |

**Result.** Of the six doubled figures:

- two have no partner at all (1:20; 3:52);
- one is common (1:2);
- **three meet a partner in Jeremiah**: 3:20, 5:21 and 5:22.

**Only 5:21 and 5:22 are exclusive.** **Jer 31:18–20 supplies two of the three** (3:20 and 5:21), within three verses of each other.

The coda's Jeremian ending is therefore not random noise. It sits in a small, real pattern linking Lamentations' turn (3:20) and its close (5:21) to Ephraim's lament and God's reply in Jer 31:18–20 (`[T]` for the counts; `[I]` for the pattern). **Confidence: moderate. Newly queued (L16).**

**Main-session spot checks reproduced (24 of 24).** Among them:

- Ps 9:8 / Lam 5:19;
- Ps 44:24–25 / 5:20;
- Isa 64:8 / 5:22;
- יגה + רֹב (1:5; 3:32);
- עֳנִי + מָרוּד (1:7; 3:19);
- the A1 baseline (82/151, 99/151 and 112/151 at ≤ 2, 3 and 4 verses);
- לִבִּי דַוָּי (Jer 8:18; 1:22);
- Nah 3:10 / 1:5;
- תִּשְׁכְּרִי (Nah 3:11 / 4:21);
- גַּם + כּוֹס (Hab 2:16 / 4:21);
- Uz (3 verses);
- נוד absent from Lamentations;
- זמם + צוה (Zech 1:6 / 2:17);
- זנח + עוֹלָם (Ps 77:8 / 3:31);
- נתן + נכה + לְחִי (Isa 50:6 / 3:30);
- גדר + דֶּרֶךְ (Hos 2:8 / 3:9);
- לכד at Ps 9:16 and Lam 4:20, not Ezek 19:4;
- חֵלֶק + כלה (Ps 73:26; Job 17:5);
- קצף + עַד + מְאֹד (Isa 64:8 / 5:22);
- the BHS "dub" at 1:14.

---

## What the audit adds that the overview and the sweep missed

Every row is verified wording. None is yet audited as design.

1. **יגה + רֹב (1:5 → 3:32)**, exclusive in the Hebrew Bible. "For the **multitude** of her transgressions" is answered by "the **abundance** of His lovingkindness". The single strongest link between poem 1 and the centre.
2. **Job 19:6–8 for 3:1–9.** It is the joint-densest window in the Hebrew Bible against Lam 3:1–9, and it shares "my paths".
3. **Jer 31:18–20 for 3:20 and 5:21**: two of the book's three Jeremian doubled figures.
4. **לִבִּי דַוָּי ("my heart is faint"): Jer 8:18 and Lam 1:22 only.**
5. **Ps 44:24–25 [Eng 44:23–24] for 5:20**, and **Isa 64:8 [Eng 64:9] for 5:22b**.
6. **Ps 9:8 [Eng 9:7] for 5:19**, alongside Ps 102:13 and Ps 89:5.
7. **Jer 25:15–29 (with Uz, 25:20) leads the cup partners at 4:21.**
8. **Ps 119:49–57 for 3:21–24**: the ח (Heth) slot, "my portion", "I said".
9. **Ps 143:3 for 3:6** leads Lam 3's psalm partners (already in v0.2.0 as a wording row).
10. **Zeph 3 is poem 4's densest partner.** Unaudited.

---

## Confidence Change Propagation

**Into the book overview (v0.2.0 → v0.3.0 at Finalise, or a v0.2.1 patch):**

| Allusion / claim | v0.2.0 | New | Sections to update |
|---|---|---|---|
| Nah 3 | live, moderate–high; "2nd of 858"; contacts at 1:5, 9; 2:13, 19; 4:21 | **moderate**. Contacts at 1:5 and 4:21 exclusive; **2:13 struck**; 1:9 shared with Jer 13:26; 2:19 shared with Isa 51:20. Rank is scan-dependent (2nd–5th) | Intertextual Map (Twelve); live-source list; *What Changed* |
| Ezek 19:4, 8 at 4:20 | moderate; "גּוֹי + שַׁחַת: 3 verses" | **low–moderate (Hebrew); moderate as a theme** (Greek). **Correct the rarity cell**: Lam 4:20 has שְׁחִית, not שַׁחַת | Intertextual Map (Ezekiel); Christological Trajectory point 3 |
| Hos 2:6 [Heb 2:8] at 3:9 | moderate | moderate. **Add Job 19:6–8 (moderate–high) for 3:1–9** | Intertextual Map (Twelve; Writings — Job row) |
| Isa 50:6 at 3:30 | 2 verses, exclusive | moderate; verse-level only; Job 16:10 equal | Intertextual Map (Isaiah); Christological point 4 ("type and contrast" kept) |
| Ps 77 at 3:31 | exclusive; "densest window" | **moderate–high for 3:31–32 ~ 77:8–10**; window claim withdrawn | Intertextual Map (Writings) |
| Cup partners at 4:21 | Hab 2:16; Nah 3:11; Jer 49:12; Jer 25 with Uz | **Jer 25:15–29 first**, Hab 2:16 second; Nah 3:11 verb only | Intertextual Map; Christological Trajectory (the cup) |
| Jer 8 | Jer 14 and 8 leading | moderate–high; **add 1:22 ~ 8:18 (לִבִּי דַוָּי)** | Intertextual Map (Jeremiah); Echo Table note |
| יגה | Echo Table (sweep proposal) | **moderate–high, as "the verb"**; 1:4 variant noted | Echo Table; Key Words |

**Into the sweep (corrections to make in place, as a v1.1 of the sweep file):**

| Location | Current | Corrected |
|---|---|---|
| Headline 1 | יגה "root"; 5 of 8 | "verb"; 5 of 8 (4 of 7 if 1:4 follows the Greek); **add יגה + רֹב 1:5 → 3:32 (exclusive)**. Confidence unchanged (chain high; design moderate–high) |
| Unit 7, finding 3 and Tool 11 | "each line of the coda has its own exclusive partner"; 5:20 Isa 49:14 | Reframe as L10 above: Ps 102:13 + Ps 9:8 + Ps 89:5; **Ps 44:24–25** for 5:20; Jer 31:18 and Jer 14:19 (the doubled figures); Isa 64:8 for 5:22b. Design low–moderate; the Jeremian pair moderate |
| Unit 3, finding 5 and Tool 11 | Ps 73:26 has fail + portion "in one verse" alongside Lam | **Correct**: Lam's pair is 2 verses apart. Ps 73 low–moderate; **Ps 119:49–57 leads** |
| Unit 3 Tool 11 | Job 19:8 at 3:7, Hos 2:6 at 3:9 | **Job 19:6–8 for 3:1–9 (moderate–high)** |
| Unit 2 finding 3 | Zech 1:6, set of 4 verses | **Exclusive with צוה (2 verses)**; gloss reworded (antecedent "your fathers") |
| Unit 6 Tool 11 | Ezek 19, moderate; cup partners order | Ezek 19 low–moderate in Hebrew, moderate as theme; **Jer 25:15–29 first** |
| Unit 7 Tool 11 | Isa 1:7, new candidate | **Drop** (low); Isa 63:15–64:11 leads |
| Convergent 1 | "Ch. 3 takes up poem 1, item by item" | **"The turn and centre (3:19–33) answer poem 1 in its own words"** (moderate). Drop "See, O LORD"; yoke textually doubtful at 1:14 |
| Convergent 5 | the mosaic table | **Observations, not alignment** (low–moderate). Jer 14 pervasive; Ps 89 verse-level; add Zeph 3 (unaudited) |
| Solo-Dig Priorities | audit targets 1–6 | Done; carry forward L16 (Jer 31:18–20) and Zeph 3 |

---

## Recommended revisions

1. **Patch the sweep now (v1.1)**, per the propagation table. The changes are small, but two are factual: the Ps 73 "one verse" claim and "See, O LORD" as a 1 → 3 item.
2. **Patch the overview's two factual cells now, or at Finalise:**
   - the Ezek 19 rarity cell;
   - the Nah 3:7 ~ 2:13 contact.
   Re-rate the rows above at Finalise.
3. **For the solo digs:**
   - **3:1–33** should build on 1:5 → 3:32 (יגה + רֹב), 1:7 → 3:19, Ps 77:8–10 → 3:31–32, Job 19:6–8 → 3:1–9 and Ps 119:57 → 3:24. It should not build on Ps 73.
   - **5:1–22** should present the coda as dense communal-lament idiom ending in two Jeremian figures, not as a line-by-line programme.
4. **Nothing in this audit touches the Preaching Traps or the pastoral notes.**

---

## New candidates for the queue

- **L16** — Jer 31:18–20 for 3:20 and 5:21, the doubled figures. Moderate.
- **L17** — Zeph 3 as poem 4's densest partner. Unaudited; verse-level contacts not yet read.
- **L18** — Ps 44:24–25 [Eng 44:23–24] for 5:20. Verse-exclusive; moderate–high.
- **L19** — Ps 119:49–57 for 3:21–24 (the ח slot). Moderate.
- **L20** — Jer 25:15–29 (with Uz) as the lead cup partner at 4:21. Moderate.

**Closed by this audit:** L2–L15. Open: L1 (direction only) and L16–L20.

---

## Critical assessment — the gaps in this audit

1. **No history of interpretation.** No commentary was consulted, so every Hays row for that criterion is empty. A Logos round is still owed on three questions: Jer 14 / Jer 31 and Lamentations (direction); the coda's doubled figures; and the BHS notes at 1:4, 1:14 and 2:19.
2. **The baselines measure lemma co-occurrence.** They are blind to word order, morphology and sound. A1's baseline could not see the doubled figures, which is why the supplementary gate was needed. That gate is itself small (six figures), so its p-value is not meaningful. It shows a pattern, not a proof.
3. **Size and setting sensitivity.** The density ranks move with the rarity cut-off: Nah 3 came 2nd in audit 1's scan and 5th here; Ps 77 is first among psalms at only one setting. **Rank claims are reported as ranges, never as single superlatives.**
4. **Direction of dependence is open throughout.** "Shares the wording of" is all any row may say.
5. **Apparatus spread was not checked.** That covers 1:4 (נְהוּגוֹת), 1:14 ("dub"), 2:19 ("c–c add") and the qere at 5:21. Each is cited as BHS prints it, `[unchecked — apparatus spread]`.
6. **The rival search was lexical.** Conceptual parallels with no shared vocabulary are not found by it.
7. **Auditor C was interrupted** by a usage limit and resumed from its own scripts. Its findings were spot-checked like the others'. The interruption is recorded so a reader can weigh it.
8. **The auditors over-ran the length guide.** Nothing was trimmed.

---

## Text-First Declaration

**Secondary sources present in context:**

- the book overview v0.2.0;
- the sweep;
- claim audit 1.

These were the objects under test. The auditors were blind to all three.

**No commentary, transcript or lexicon** beyond the BHS apparatus (Logos export).

**Primary texts opened:**

- WLC (reading text and lemma index), in full for Lamentations and canon-wide for the scans;
- Swete LXX, for every Greek row;
- the Rahlfs Lamentations export (5:19–22; 3:22–24);
- the BHS apparatus for Lamentations.

**Chains and counts verified:** 24 decisive spot checks reproduced by the main session, plus the doubled-figure baseline run here. Positive controls were recorded by each auditor before every nil or "only".

**Warrant use:** verdicts are `[S: audit]` for downstream use. Counts are `[T]`; readings of design are `[I]`.

**Health note.** The single contacts mostly hold, often beside a better rival. The design claims all came down. What survived is narrow:

- a localised echo of poem 1 in 3:19–33;
- a Jeremian close in 5:21–22, linked to 3:20 through Jer 31:18–20.

**That is enough to preach the centre and the ending with confidence, but not to preach an architecture.**
