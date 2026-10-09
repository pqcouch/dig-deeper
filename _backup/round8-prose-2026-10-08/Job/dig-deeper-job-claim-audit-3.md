# Claim Audit 3: Job

**Passages audited:** twenty-five queued claims — the Sermon 4 batch from the project's `claude/claim-audit-queue.md` (Job #7, #26, #56–58, #60–79) — in three parts. A ruling on #59 is added in the Summary.

- **Part A (Torah, Chronicles and short Psalter links):**
  - A1 the witness law and the avenger of blood (Deut 19) at 16:8, 17–18 and 19:25 (#60, #68);
  - A2 David's oath of innocence (1 Chr 12:18) at 16:17, 21 (#62);
  - A3 the Song of Moses (Deut 32:22–33) behind Zophar (#72);
  - A4 Sodom (Gen 19:24; Ps 11:6) at 18:15; 20:23, 29 and 1:16 (#76);
  - A5 Ps 1 at 21:16, 18 (#74), and Ps 18:35 at 20:24 (#77).
- **Part B (the Latter Prophets):**
  - B1 Isa 59 behind Eliphaz (#56);
  - B2 Isa 14 behind Bildad (#71);
  - B3 Hezekiah's psalm at 16:19–17:16 (#57);
  - B4 the Servant pattern at 16:10, 17 (#61);
  - B5 Isa 30:8 and Jer 17:1 at 19:23–25 (#63, #64);
  - B6 Isa 44:6 and Isa 26:19–21 at 19:25 (#70, #26);
  - B7 Habakkuk at 19:2, 7, 23 (#65);
  - B8 Isa 40:14 at 21:22 (#78).
- **Part C (Lamentations, the Psalter and two design claims):**
  - C1 Lamentations 2–3 at 16:9–16 and 19:2–27 (#58);
  - C2 Lamentations 4 behind Zophar (#73);
  - C3 Ps 88, Ps 102 and Ps 69 in Job 19 (#69, #66, #67);
  - C4 Psalm 22 as a live source (#7);
  - C5 the prologue's losses inside the friends' portraits (#75);
  - C6 Job 21 as a reply to the friends (#79).

**Date:** 6–7 October 2026 (Addendum on the history of interpretation, from Logos round 6, added 7 October 2026)

**Purpose:** to test the allusion and design claims that carry weight in the three Sermon 4 digs (16:1–17:16; 19:1–29; 15:1–21:34) before the Sermon 4 backbone. Trigger 1 of the standing rule had fired: 66 candidates were queued and there had been four digs since claim audit 2. Trigger 2 was armed, because ten of these claims carry headline findings.

**Primary texts:**

- **Hebrew:** WLC with its lemma and morphology index (the observation layer); BHS with apparatus (Logos export) for Job.
- **Greek Old Testament:** Swete LXX for the whole canon. Rahlfs–Hanhart exports (Logos) for Job, Genesis, Exodus, Numbers, Deuteronomy, Kings, Isaiah, Jeremiah, the Twelve, Psalms, Proverbs and Ecclesiastes. There is no Rahlfs export for Lamentations, so Greek Lamentations is Swete only.
- **New Testament:** SBLGNT with the MorphGNT index.
- **English:** NASB95 and ESV (Logos exports).

**Study text:** NASB95 · **Pulpit text:** ESV (Sermon 4 is in view)

**Earlier audits** stand and are not re-opened. Audit 1 (28 September 2026) covered structure and the Bejon notes. Audit 2 (3 October 2026) covered the Sermon 3 set. Audit 2's verdict on Deut 32:39 at 5:18 and 10:7 is cited where the Song of Moses recurs.

---

## Method

The method is that of claim audit 2. It adds one requirement: **a null for every window rank.**

**Three independent auditors.** Each was a fresh subagent. None had access to the book overview, the sweep, the Job digs, the queue's reasoning, the earlier audits, or one another's work. Each was given its claims as proposals to break, with only the proposed rating attached. **They ran one after another, not in parallel.** Auditors A and B ran on 6 October and auditor C on 7 October, from the same briefs.

**The corpus in the cloud.** The `_texts/` corpus was staged into the session workspace, and the auditors used a shared helper library (`alib.py`, `aux.py`, `base.py`). It offers:

- in the Hebrew: lemma, co-occurrence, phrase (with a skeletal pass), ketiv and partner searches;
- in Swete and the SBLGNT: accent-insensitive searches;
- the Rahlfs and English exports;
- a chapter-window ranker over the 887 non-Job chapters of the Hebrew Bible.

Every auditor ran the positive control first (חֶסֶד ("lovingkindness") in Job: 6:14; 10:12; 37:13). Every claimed absence was preceded by a search that returned a known hit.

**Baselines.**

- **Exclusive pairs.** A Job verse has on average 1.34 content-lemma pairs that occur together in exactly one other verse of the Hebrew Bible (WLC; lemmas in at most 400 verses; 1.87 at a 700-verse cap). The rate for chapters 15–21 runs from 0.55 to 1.48 per verse. So a single exclusive pair proves little. Links were judged by clustering, rarity, verbatim phrasing, matching function and the absence of a rival.
- **The window-rank null (new in this audit).** Three Sermon 4 digs had argued from "the source window ranks Nth of 887". Each auditor re-ran the rank, then ran the same rank for 15–72 Job passages of the same length from chapters 4–14 and 22–31. This gives the top-1 score and 1st–5th gap that an *arbitrary* Job passage achieves. A proposed source counts only if its score and margin exceed that null. Selection effects were noted: a source found by scanning a ranked list is post hoc.
- **Design baselines.** Auditor C built the two design baselines the queue asked for:
  - for #75, element densities in the round-two portraits against other "fate of the wicked" portraits;
  - for #79, a ranking of the 120 friend-speech → Job-reply pairs of Job 4–27 by shared rare vocabulary.

**For every claim, each auditor:**

1. read the Job verses (WLC, BHS, Swete, Rahlfs, noting asterisked lines);
2. read the source in context;
3. verified every stated "only";
4. took frequency and chance baselines;
5. searched for the strongest rival;
6. scored the Hays criteria;
7. gave a verdict, a final rating and a line on what a preacher may safely say.

**Sources.** No commentaries and no web sources were used, so "History of interpretation" is recorded as *not checked* throughout. Library evidence already recorded from Patrick's Logos rounds is noted in the Summary where it bears on a verdict.

**Spot checks.** The main session then re-ran the evidence on which the verdicts turn (see Spot Checks).

---

## Positional Frame (Phase 0.6)

**What has the book set up that these claims serve?** Round two (15–21) begins with Eliphaz's offer of "the consolations of God" (15:11). It ends with Job's "How then will you vainly comfort me?" (21:34). Between them the friends turn from rebuking Job to describing the wicked man's end. Job turns from them to a witness in heaven (16:19), a surety (17:3) and a Redeemer (19:25). The Sermon 4 digs proposed that both voices speak in the words of other Scripture:

- Job in the words of Lamentations, Hezekiah's psalm, the Servant, Isaiah's Redeemer and the lament psalms;
- the friends in the words of Isaiah 59 and 14, the Song of Moses, Lamentations 4, Psalm 1 and the Sodom tradition.

They also proposed two designs: that the friends' portraits are built from Job's own losses in chapters 1–2, and that Job 21 answers the portraits point by point.

**Why does this matter here?** These claims would shape what the Sermon 4 backbone says about the round. They are also the kind of claim that overreaches most easily:

- "Only X and Y" pairs are common.
- Three of these claims rest on window ranks, which had never been tested against a null.
- Two are design claims built from lexical distributions.

So the question for each claim was not only "is the word-count right?" but "is this link above what chance produces, and is there a better source?"

---

## Part A: Torah, Chronicles and Short Psalter Links

### Auditor's note

**Corpus.** Hebrew: WLC text and lemma index (Strong's numbers, 23,213 verses) through `alib`. Greek: Swete (all books, LXX numbering) and the Rahlfs–Hanhart Logos exports for Job, Deuteronomy, Genesis, Kings, Isaiah and Psalms (`aux.rv`). BHS Job text and apparatus (`02-Job-BHS.txt`, `02-Job-BHS-App.txt`). English: NASB95 exports. No commentaries, web or project documents were consulted. I opened no file outside `/home/claude/audit3` except the corpus.

**Positive control.** `alib.lem('2617','Job')` returned Job 6:14, 10:12, 37:13. I ran every absence search against a verse known to hold the item and got that verse back each time: `co(['5707','6965','6030'])` returns Deut 19:16 as well as Job 16:8; `co(['1350','2555','1818'])` returns Ps 72:14; `co(['6620','7219'])` returns Deut 32:33; exact-string `'אש אלהים'` returns Job 1:16; `'עצת רשעים'` returns Ps 1:1; `'קשת נחושה'` returns Ps 18:35. Homograph letters checked: עָנָה ("answer, testify") is 6030 b (314 tokens; 6030 c "sing" and 6030 a are separate); גָּאַל ("redeem") is 1350 a (1350 b "defile" only Isa 63:4); רֹאשׁ ("poison") is 7219, kept apart from רֹאשׁ ("head") 7218; the bitter/venom words split into מְרוֹרָה 4846 (Deut 32:32; Job 13:26; 20:14, 20:25) and מְרֵרָה 4845 (Job 16:13 only). Ketiv check: no unpointed tokens in Job 16:8, 16:17, 16:21 or 1 Chr 12:18; in Job 20 only עלומו (20:11), which is irrelevant here.

**Method.** I verified each "only" by lemma (`co`, `lem`) and by exact consonants on the WLC text. The skeletal pass in `ph` is unusable for short forms (for ויוכח it returns 300+ verses), so I counted forms token by token. Rival search used `aux.partners`, `base.rank` (count of shared lemmas, maxf 150) and two weighted variants I wrote over the same `base.lems` index: IDF-weighted window scores, and a count restricted to very rare lemmas (at most 15 verses).

**Baselines computed.** (1) Exclusive pairs per verse are the brief's figures (Job 16: 0.55; Job 20: 1.03). Job 16:8, 16:17 and 16:18 have **zero** exclusive pairs at maxf 400. (2) Because two of the claims rest on exclusive *triples*, I computed exclusive content-lemma triples (each lemma in at most 700 verses) for Job 15–21: a mean of 0.39 per verse, and **18% of verses** have at least one. (3) Window-rank null for 26-verse passages (k=12, maxf 150), using 20 Job passages starting at 4:1, 5:1 … 14:1 and 22:1 … 31:1 (except 25): top-1 median **9** shared lemmas (range 7–11), 5th place median **7.5**, 1st–5th gap median **1**. IDF version: top-1 median **53.9** (maximum 67.2), 5th median 45.1, gap median 8.0. Very-rare version (lemmas in at most 15 verses): top-1 median **2** (maximum 4). (4) The same null for 12-verse passages, IDF: top-1 median **33.3**, maximum 52.1, gap median 5.8. (5) A local-cluster baseline: across all 1,068 three-verse windows in Job, I took the best non-Job two-verse window by number of shared lemmas each in at most 15 verses. 863 windows score 1, 78 score 2, and only **3** score 3 or more.

**Limits.** Lemma indexing is Strong's-based. Rare-lemma thresholds are mine and set after the fact, so a selection caveat applies to the weighted ranks. History of interpretation is not checked anywhere in this part.

---

#### A1: The witness law and the avenger of blood (Deut 19) behind Job 16:8, 17–18 and 19:25

**Claim (as tested).** (a) Job 16:8 speaks in the words of the malicious-witness law, Deut 19:16–18, through the triad עֵד ("witness") + קוּם ("rise") + עָנָה ("testify"), found in one verse only at Deut 19:16 and Job 16:8. Deut 19:16's עֵד־חָמָס ("malicious witness", literally "witness of violence") is set against Job 16:17, and Ps 35:11 is a companion. Proposed rating **moderate–high (words)**. (b) The גֹּאֵל הַדָּם ("avenger of blood", Deut 19:6, 12) and Ps 72:14 (גאל "redeem" + חָמָס "violence" + דָּם "blood") lie behind 16:18 and 19:25. Proposed rating **moderate (synthetic)**.

**Evidence**
- [T] `co(['5707','6965','6030'])` → Deut 19:16, Job 16:8 only (WLC). The triad "only" is **verified**. Pairwise, though, the words are legal stock. עֵד + עָנָה occurs in 8 verses (Exod 20:16; Deut 5:20; 19:16, 18; 31:21; Num 35:30; Prov 25:18; Job 16:8). עֵד + קוּם occurs in 6 (Deut 19:15, 16; Ps 27:12; 35:11; Ruth 4:10; Job 16:8).
- [T] Both companions carry חָמָס inside the verse, which Job does not. Ps 35:11 יְקוּמוּן עֵדֵי חָמָס ("malicious witnesses rise up"). Ps 27:12 קָמוּ־בִי עֵדֵי־שֶׁקֶר וִיפֵחַ חָמָס ("false witnesses have risen against me, and such as breathe out violence"). Ps 27:12's קָמוּ־בִי ("rose against me") is syntactically closer to Job's וַיָּקָם בִּי ("rises up against me") than Deut 19:16's יָקוּם … בְּאִישׁ ("rises … against a man").
- [T] Job's בְּפָנַי יַעֲנֶה ("testifies to my face") has a closer idiom in Hosea. עָנָה + בִּפְנֵי ("answer to the face") occurs only at Deut 25:9, Hos 5:5, Hos 7:10 and Job 16:8. Hosea also supplies the rare כַּחַשׁ ("lie, leanness"; 6 verses: Hos 7:3, 10:13, 12:1; Nah 3:1; Ps 59:13; Job 16:8).
- [I] The pun supports the forensic frame. כַחֲשִׁי means "my leanness" but also "my lie": a falsehood that "rises" and "testifies" is a false witness. Deut 19:18 עֵד־שֶׁקֶר ("false witness") is the legal category in view. Job 16:19 then counters with a true witness in heaven, עֵדִי ("my witness").
- [T] Greek: in Rahlfs, Job 16:8b (καὶ ἀνέστη ἐν ἐμοὶ τὸ ψεῦδός μου, κατὰ πρόσωπόν μου ἀνταπεκρίθη, "my falsehood rose against me, it answered to my face") is **asterisked**, so the Old Greek lacked the very clause carrying קוּם and עָנָה. Swete's Job ends the verse at καὶ ἐπελάβου μου ("and you seized me"). The hexaplaric rendering ψεῦδος ("falsehood") reads כַּחַשׁ as "lie".
- [T] Window rank, Job 16:7–18 (k=12, maxf 150): Deut 19 ranks **12th** with 4 lemmas: שֵׁן ("tooth", from 19:21 "tooth for tooth"), חָמָס, עֵד, שָׁפַךְ ("shed"). It ranks 27th by IDF. Ps 35:5–16 ranks 5th by count and **2nd** by IDF (38.6), sharing חָרַק ("gnash"), שַׂק ("sackcloth"), שֵׁן ("tooth"), חָמָס, עֵד and תְּפִלָּה ("prayer"). Lam 2:6–17 is first by far (see New candidates).
- [T] (b) `co(['1350','2555','1818'])` → Ps 72:14 only: the triad is verified. In Job, though, the three words are spread over 16:17 (חָמָס), 16:18 (דָּם) and 19:25 (גֹּאֲלִי, "my Redeemer"). גֹּאֵל הַדָּם ("avenger of blood") never occurs in Job, and Job's only uses of 1350 a are 3:5 and 19:25.
- [T] (b) Job 16:18 אֶרֶץ אַל־תְּכַסִּי דָמִי ("O earth, do not cover my blood") has better partners than Deut 19. Isa 26:21 shares אֶרֶץ ("earth"), כָּסָה ("cover"), דָּם and מָקוֹם ("place"): "the earth will reveal her bloodshed and will no longer cover her slain". It is the top `partners` hit at 13.5; ארץ + כסה + דם also occurs at Ezek 24:7 and Hab 2:17. Gen 4:10 is the only other verse with דָּם + צָעַק ("cry"), cognate with Job's זַעֲקָתִי ("my cry"). The BHS apparatus at 16:18 itself notes "cf Gn 4,10".
- [T] (b) Job 19:25's best verbal partner is Isa 44:6, an **exclusive pair** גֹּאֵל + אַחֲרוֹן ("redeemer" + "last") found only at Isa 44:6 and Job 19:25 (`excl_pairs`). Window rank for Job 19:23–27 (k=5): Isa 44:4–8 is 2nd, Deut 19:2–6 is 23rd (2 lemmas: בַּרְזֶל "iron" and גאל), and Ps 72 is 272nd.
- [I] Within Job a chain of its own does exist. 16:17–18 has no חָמָס, unburied blood and a cry; 19:7 has הֵן אֶצְעַק חָמָס ("I cry 'Violence!'"); 19:25 has גֹּאֲלִי. This supports a thematic reading (the blood cries, so a kinsman must vindicate), but it is Job-internal.

**Baseline.** Job 16:8 has no exclusive pairs at all. Its one exclusive triple is the claimed one, and 18% of verses in Job 15–21 carry at least one such triple. The triad is the kind of thing that turns up once in five verses. Its weight comes from its legal function, not from rarity.

**Rival sources.** For the witness idiom, Ps 35:11 and Ps 27:12 (each with חָמָס in-verse; Ps 35 is the stronger window). For "testify to the face", Hos 5:5 and 7:10. For 16:18, Gen 4:10 and Isa 26:21. For 19:25, Isa 44:6 and the Isaianic Redeemer (Isa 49:26 has גאל + דם + "all flesh will know").

**Hays criteria**

| Criterion | (a) witness law | (b) avenger of blood |
|---|---|---|
| Availability | Strong | Strong |
| Volume | Possible (triad unique, but stock legal words) | Weak (no shared phrase; words spread across two chapters) |
| Recurrence | Possible (witness motif in 10:17; 16:19) | Weak |
| Thematic coherence | Strong (false witness / true witness) | Possible |
| Historical plausibility | Strong | Possible |
| History of interpretation | Not checked | Not checked |
| Satisfaction | Possible | Weak |

**Verdict.** (a) **Confirmed with nuance.** (b) **Needs reframing.**

**Final rating.** (a) **Moderate (words, legal idiom).** (b) **Weak as a Deut 19 link; possible as a synthetic, Job-internal theme.**

**Reasoning.** The triad is real and exclusive, and the forensic pun on כַּחַשׁ ("lie, leanness") fits the false-witness law. But the idiom "a witness rises" is shared by Deut 19:15–18, Ps 27:12 and Ps 35:11, and Ps 35 is the stronger window. The Old Greek lacked 16:8b. Nothing in Job reproduces גֹּאֵל הַדָּם, and the textual partners of 16:18 and 19:25 lie elsewhere (Gen 4:10 and Isa 26:21; Isa 44:6).

**What a preacher may safely say.** "Job speaks in the language of the courtroom. His wasted body is like a false witness rising against him, which is exactly what Israel's law about false witnesses forbids, and so he looks for a true witness in heaven. When he asks the earth not to cover his blood, he echoes Abel's blood crying from the ground."

---

#### A2: David's oath of innocence (1 Chr 12:18) behind Job 16:17, 21

**Claim (as tested).** 1 Chr 12:18 [Eng 12:17] is echoed at Job 16:17 and 16:21. חָמָס ("violence") + כַּף ("palm") with the negative occurs only at 1 Chr 12:18 and Job 16:17; חָמָס + יָכַח ("decide") in one verse only at 1 Chr 12:18; the jussive וְיוֹכַח ("and may he decide") only at 1 Chr 12:18 and Job 16:21. Proposed rating **moderate–high (words)**.

**Evidence**
- [T] `co(['2555','3709'])` → 1 Chr 12:18, Isa 59:6, Jonah 3:8, Job 16:17. Only 1 Chr 12:18 (בְּלֹא חָמָס בְּכַפַּי, "with no violence in my palms") and Job 16:17 (לֹא־חָמָס בְּכַפָּי, "no violence in my palms") negate it. In the other two the violence *is* in their palms. **Verified.** The exact consonants לא חמס בכפי occur in these two verses only.
- [T] `co(['2555','3198'])` → 1 Chr 12:18 only. **Verified.** In Job the two words are four verses apart (16:17, 16:21). `chk_helpers.win(['2555','3709','3198'],4)` → 1 Chr 12:18 and Job 16:17 only, so the three-word set within a five-verse span is exclusive to these two places.
- [T] Forms of יָכַח (3198), counted token by token: the consonants ויוכח occur 5 times (Gen 31:42; 1 Chr 16:21; Ps 105:14; 1 Chr 12:18; Job 16:21). The first three are the wayyiqtol וַיּוֹכַח ("and he rebuked"); only 1 Chr 12:18 and Job 16:21 are the waw + jussive וְיוֹכַח. The short jussive also occurs without the waw at Hos 4:4 (×2). The claim is **verified on the pointing**, but not on the consonants.
- [T] **Strong rival for 16:17a.** Isa 53:9 עַל לֹא־חָמָס עָשָׂה וְלֹא מִרְמָה בְּפִיו ("because He had done no violence, nor was there any deceit in His mouth"). The three-word sequence עַל לֹא־חָמָס ("although no violence") occurs only at Isa 53:9 and Job 16:17 (exact consonants). Both verses then pair innocence of deed with purity of speech: "no deceit in His mouth" against Job's "my prayer is pure". So Job 16:17 shares three words with Isaiah and three with Chronicles.
- [T] **Common ancestor.** Gen 31:42: אֶת־עָנְיִי וְאֶת־יְגִיעַ כַּפַּי רָאָה אֱלֹהִים וַיּוֹכַח ("God has seen my affliction and the toil of my palms, so He rendered judgment"), alongside אֱלֹהֵי אָבִי ("the God of my father"). 1 Chr 12:18 reads like this verse recast as an oath: כַּפַּי ("my palms"), יֵרֶא אֱלֹהֵי אֲבוֹתֵינוּ ("may the God of our fathers see"), וְיוֹכַח ("and decide"). Gen 31:37 וְיוֹכִיחוּ בֵּין שְׁנֵינוּ ("that they may decide between us two") is matched by Job 9:33 לֹא יֵשׁ־בֵּינֵינוּ מוֹכִיחַ ("there is no umpire between us"). יָכַח + בֵּין ("between") occurs only at Gen 31:37, Isa 2:4, Mic 4:3 and Job 9:33. Job also knows Gen 31:42's phrase יְגִיעַ כַּפֶּיךָ ("the labour of your palms", Job 10:3; otherwise only Gen 31:42, Hag 1:11, Ps 128:2).
- [T] BHS at 16:21 notes "l c pc Mss וּבֵין" (read "and *between* a son of man and his neighbour"). That reading would sharpen the Gen 31:37 and Job 9:33 arbitration language.
- [T] Greek: 1 Chr 12:17 LXX ἴδοι ὁ θεὸς τῶν πατέρων ὑμῶν καὶ ἐλέγξαιτο ("may God see … and decide", optative) and Job 16:21 εἴη δὲ ἔλεγχος ἀνδρὶ ἔναντι κυρίου ("may there be a reproof for a man before the Lord") share the ἐλεγχ- root and the optative mood, a mild convergence. Job 16:21b is **asterisked** in Rahlfs; 16:21a, which carries the verb, is Old Greek. Isa 53:9 ἀνομίαν οὐκ ἐποίησεν ("he did no lawlessness") is not echoed in Job 16:17 (ἄδικον δὲ οὐδὲν ἦν ἐν χερσίν μου, "nothing unjust was in my hands").
- [T] Window rank for Job 16:17–21 (k=5): 1 Chr 12 ranks 46th (2 lemmas), Gen 31:40–44 ranks 11th (2), Isa 53 ranks 131st. The link is phrasal; no window stands out.
- [T] 1 Chr 12:18 has no parallel in Samuel (no Samuel verse holds חָמָס + כַּף).

**Baseline.** Job 16 has 0.55 exclusive pairs per verse, the lowest in the round, and 16:17 has none. The evidence is the matching negated phrase plus the jussive verb within five verses, which is exclusive (as shown above), and not a lemma pair.

**Rival sources.** Isa 53:9 (equal to Chronicles on 16:17a; stronger on the deed/speech pairing). Gen 31:37–42 (the probable shared source of the "see and decide" formula). Isa 59:6 and Jonah 3:8 are weak (positive "violence in their palms").

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Possible (Chronicles follows Job in the Ketuvim; a shared formula is likelier than borrowing either way) |
| Volume | Strong (negated חמס בכפי + jussive וְיוֹכַח, exclusive within a five-verse span) |
| Recurrence | Possible (Job 9:33; 10:3 draw on the same Gen 31 legal language) |
| Thematic coherence | Strong (oath of innocence, appeal for God to adjudicate) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** **Confirmed with nuance.**

**Final rating.** **Moderate (words; shared formula).**

**Reasoning.** Every stated "only" holds, the last only on the pointing. But Job 16:17 is equally close to Isa 53:9 (עַל לֹא־חָמָס, "although no violence", exclusive), and 1 Chr 12:18 itself is built on Gen 31:42. The safest frame is a shared oath-of-innocence formula ("no violence in my palms; let God see and decide") that Job and David both use. Direct dependence of Job on Chronicles is not shown.

**What a preacher may safely say.** "Job's plea, 'there is no violence in my hands … O that someone might argue my case with God', uses the same oath of innocence as David's 'there is no wrong in my hands; may God see and decide', and the same words as Isaiah's Servant, who 'had done no violence'."

---

#### A3: The Song of Moses (Deut 32:22–33) behind Zophar's speech (Job 20:4–29)

**Claim (as tested).** Zophar's portrait draws on Deut 32:22–33. פֶּתֶן ("cobra") + רֹאשׁ ("poison") occurs only at Deut 32:33 and Job 20:16. מְרֹרֹת ("bitter", Deut 32:32) matches מְרוֹרַת ("venom", Job 20:14). Further links: fire of anger (32:22 ~ 20:23, 26), אֵימָה ("terror", 32:25 ~ 20:25 אֵמִים), יְבוּל ("produce", 32:22 ~ 20:28). Deut 32:22–33 is said to rank 5th of 887. Proposed rating **moderate–high**.

**Evidence**
- [T] `co(['6620','7219'])` → Deut 32:33, Job 20:16 only. The exact phrase רֹאשׁ פְּתָנִים ("poison of cobras") occurs only at Deut 32:33 (וְרֹאשׁ פְּתָנִים אַכְזָר, "and the deadly poison of cobras") and Job 20:16 (רֹאשׁ־פְּתָנִים יִינָק, "he sucks the poison of cobras"). **Verified**, by lemma and by consonants. Positive control: Deut 32:33 is returned.
- [T] מְרוֹרָה (4846, "bitter thing, venom, gall") occurs in 4 verses only: **Deut 32:32**, Job 13:26, Job 20:14 and Job 20:25. Deut 32:32 is its only use outside Job. פֶּתֶן occurs in 6 verses (Deut 32:33; Isa 11:8; Ps 58:5; 91:13; Job 20:14, 16). רֹאשׁ "poison" (7219) occurs in 12.
- [T] **Local cluster.** Deut 32:32–33 holds מְרֹרֹת, רֹאשׁ (×2) and פְּתָנִים in two verses. Job 20:14–16 holds מְרוֹרַת פְּתָנִים ("venom of cobras") and רֹאשׁ־פְּתָנִים in three. Against the cluster baseline, only 3 of Job's 1,068 three-verse windows share three or more lemmas of at most 15 verses' frequency with a non-Job two-verse window. **Job 20:14 → Deut 32:32 is one of the three**; the other two are a single Job 28:15–16 / Isa 13:12 match.
- [T] Wider Song. Deut 32:13 וַיֵּנִקֵהוּ דְבַשׁ ("He made him suck honey") and 32:14 חֶמְאַת ("curds") against Job 20:16–17 יִינָק ("he sucks") … דְּבַשׁ וְחֶמְאָה ("honey and curds"). Israel sucks honey from the rock; the wicked man sucks cobra poison and never sees the rivers of honey and curds. דְּבַשׁ + חֶמְאָה in one verse elsewhere: 2 Sam 17:29; Isa 7:15, 7:22. Deut 32:24 אֲשַׁלַּח־בָּם ("I will send upon them") against 20:23 יְשַׁלַּח־בּוֹ ("he will send upon him"). Deut 32:22 אֵשׁ … בְאַפִּי … וַתֹּאכַל ("fire … in My anger … consumes") against 20:23 חֲרוֹן אַפּוֹ ("his burning anger") and 20:26 תְּאָכְלֵהוּ אֵשׁ ("fire will devour him"). Deut 32:41 בְּרַק ("flashing", of a sword) against 20:25 וּבָרָק ("glittering point").
- [T] The weaker items. אֵימָה (17 verses, 5 in Job) is a Job-typical word. יְבוּל occurs in 13 verses, including Lev 26:4, 20 and Deut 11:17, and BHS proposes יָבָל ("stream") at 20:28. Both add little.
- [T] **Greek.** Job 20:16 θυμὸν δὲ δρακόντων θηλάσειεν ("may he suck the wrath of serpents") renders רֹאשׁ פְּתָנִים with Deut 32:33a's θυμὸς δρακόντων ("wrath of serpents"; elsewhere only Deut 32:33 and Ode 2:33, the Song itself). The Old Greek translator of Job heard Deut 32:33 here. Job 20:14b χολὴ ἀσπίδος ("gall of an asp") recalls Deut 32:32–33 χολῆς … ἀσπίδων ("gall … asps"), but that line is **asterisked**; the Old Greek lacked it.
- [T] **Window rank reproduced.** `base.rank(span('Job',20,4,29),12,maxf=150)`: Deut 32:22–33 ranks **5th of 887** with 7 shared lemmas, tied at 7 with ranks 4–8; the top is 8 (Jer 4:18–29). The shared lemmas are מְרוֹרָה, פֶּתֶן, רֹאשׁ, יְבוּל, אֵימָה, יָנַק ("suck") and עָפָר ("dust"). By IDF it ranks **1st** (51.3), but only 1.2 ahead of Jer 4. By very-rare lemmas (at most 15 verses) it ranks **1st with 4**; no other window has more than 2.
- [T] **Null.** For 20 Job passages of 26 verses, the count top-1 median is 9 and the 5th-place median 7.5. On that metric Deut 32's 7 is ordinary 5th-place material. The IDF top-1 median is 53.9, above Deut 32's 51.3. On very rare lemmas the null top-1 median is 2, and only 1 of 20 passages reaches 4. **The rank figure as stated proves nothing; the rarity of what is shared does.** The source was proposed on the phrase, not found by scanning the list, so the selection effect is small.
- [I] Deut 32:32 names סְדֹם ("Sodom") and עֲמֹרָה ("Gomorrah"): "their vine is from the vine of Sodom … grapes of poison (רוֹשׁ), clusters bitter (מְרֹרֹת)". Zophar's venom lines thus use the Sodom-vine verse. This bears on A4.
- [T] The earlier audit's acceptance of Deut 32:39 at Job 5:18 and 10:7 was not re-tested here; I note it as recurrence only.

**Baseline.** Job 20 has 1.03 exclusive pairs per verse. Job 20:16's three exclusive pairs include פֶּתֶן + רֹאשׁ → Deut 32:33. The decisive evidence is the two-verse rare cluster (top 0.3% of Job windows), not that single pair.

**Rival sources.** Ps 58:5 (פֶּתֶן, the wicked as venomous) and Ps 140:4 share the image but not the vocabulary cluster. Jer 4:18–29, Hab 3 and Lam 4 outrank Deut 32 on raw counts only by means of common lemmas. For 20:23, Ps 78:49 is a sharper partner (see New candidates).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Strong (exclusive phrase רֹאשׁ פְּתָנִים; מְרוֹרָה otherwise only Deut 32:32) |
| Recurrence | Strong (Song already used at Job 5:18; honey/suck inversion at 20:16–17) |
| Thematic coherence | Strong (the poisoned fruit of the wicked; fire of God's anger) |
| Historical plausibility | Strong |
| History of interpretation | Not checked |
| Satisfaction | Strong |

**Verdict.** **Confirmed** (with the rank argument replaced).

**Final rating.** **High (words) for Job 20:14–17 ~ Deut 32:13–14, 32–33; moderate for the wider fire, arrow and terror items.**

**Reasoning.** Three lemmas found together in only one other place outside Job, an exclusive two-word phrase, and the Old Greek's own echo make this one of the firmest links in the round. Zophar turns the Song's language of apostate Israel's poisoned vine against Job. The "5th of 887" figure should be dropped: it is what an arbitrary Job passage's fifth window scores. The case rests on rarity and clustering.

**What a preacher may safely say.** "Zophar borrows the words of the Song of Moses. The 'poison of cobras' and 'bitter venom' are the Song's description of a people whose vine came from Sodom, and the wicked man who 'sucks' poison is the reverse of Israel, whom God made to 'suck honey from the rock'."

---

#### A4: Sodom — Gen 19:24 and Ps 11:6 — behind Job 18:15; 20:23, 29 (and 1:16)

**Claim (as tested).** Bildad's brimstone (18:15), Zophar's raining (20:23) and "portion" (20:29), and the prologue's fire from heaven (1:16) recall Gen 19:24 and Ps 11:6. The friends paint Job's losses as Sodom's fate. Proposed rating **moderate**.

**Evidence**
- [T] גָּפְרִית ("brimstone") occurs in 7 verses: Gen 19:24; Deut 29:22; Isa 30:33; 34:9; Ezek 38:22; Ps 11:6; Job 18:15. Four of the six non-Job uses are Sodom-type rained judgement or name Sodom (Gen 19:24; Deut 29:22; Ps 11:6; Ezek 38:22). The word itself carries the motif.
- [T] But Job 18:15 יְזֹרֶה עַל־נָוֵהוּ גָפְרִית ("brimstone is scattered on his habitation") has no rain and no fire, and its verb זָרָה ("scatter") never occurs with brimstone elsewhere. Window rank for Job 18:5–21 (k=12): Gen 19 is **314th** (1 lemma), Ps 11 249th, but **Deut 29:16–27 29th** (4 lemmas). Deut 29:22 has brimstone, a land that is "unsown … no grass grows", "like the overthrow of Sodom". That fits 18:15–16 (habitation, then roots dried and branch cut off) better than Gen 19:24 does.
- [T] Greek: Rahlfs **asterisks Job 18:15b** (κατασπαρήσονται τὰ εὐπρεπῆ αὐτοῦ θείῳ, "his fine things will be sown with brimstone"), together with 18:16b. The Old Greek lacked the brimstone line.
- [T] BHS at 18:15 proposes reading מַבֵּל ("fire", cf. Akkadian *nablu*) for מִבְּלִי־לוֹ ("nothing of his"). At 20:23 it proposes עָלָיו מַבֵּל חַמּוֹ ("upon him the fire of his wrath"), "cf 18,15". Either conjecture would create a "fire and brimstone" or "rain fire" collocation. They are conjectures, so they are recorded as data only.
- [T] Job 20:23 וְיַמְטֵר עָלֵימוֹ ("and will rain on him"). The exact consonants ימטר occur at Exod 9:23, Ps 78:24, 78:27 (all wayyiqtol וַיַּמְטֵר, "and he rained"), Ps 11:6 and Job 20:23. Only Ps 11:6 (יַמְטֵר עַל־רְשָׁעִים, "Upon the wicked He will rain") and Job 20:23 are the jussive. מָטַר ("rain") + רָשָׁע ("wicked") occurs in one verse only at Ps 11:6, and Job's רָשָׁע comes at 20:29.
- [T] **20:29 "portion" is a different word.** Job 20:29 has חֵלֶק ("portion"); Ps 11:6 has מְנָת כּוֹסָם ("the portion of their cup"). חֵלֶק + רָשָׁע occurs only at Job 20:29 and Job 27:13, a Job-internal refrain (`ph('חלק אדם רשע')`). The English "portion" made the link. The Greek does converge: μερίς ("portion") at Job 20:29 and Ps 10:6 LXX. That is the translator's choice.
- [T] **Stronger rival for 20:23.** Ps 78:49 יְשַׁלַּח־בָּם חֲרוֹן אַפּוֹ ("He sent upon them His burning anger"). The exact consonants ישלח ב- חרון אפו occur only at Ps 78:49 and Job 20:23. The same psalm has God "rain" (וַיַּמְטֵר) food (78:24, 27), and then "while their food was in their mouths, the anger of God rose against them" (78:30–31; cf. Num 11:33). That is Job 20:23's very sequence: filling the belly, God's anger, raining it on him while he eats.
- [T] **1:16 fails.** `ph('אש אלהים')` (exact) → 2 Kgs 1:12 and Job 1:16 only. 2 Kgs 1:12 וַתֵּרֶד אֵשׁ־אֱלֹהִים מִן־הַשָּׁמַיִם וַתֹּאכַל ("the fire of God came down from heaven and consumed") shares אֵשׁ אֱלֹהִים ("fire of God"), מִן־הַשָּׁמַיִם ("from heaven") and אָכַל ("consume") with Job 1:16. Gen 19:24 shares only "fire" and "from heaven", and it has מָטַר ("rain") and גָּפְרִית, which 1:16 lacks. אֵשׁ + שָׁמַיִם + אָכַל occurs at 2 Kgs 1:10, 12, 14; 2 Chr 7:1; Job 1:16. The Greek points the same way: Job 1:16 πῦρ ἔπεσεν ἐκ τοῦ οὐρανοῦ ("fire fell from heaven") = 1 Kgs 18:38 LXX ἔπεσεν πῦρ παρὰ κυρίου ἐκ τοῦ οὐρανοῦ (Carmel); Gen 19:24 LXX has ἔβρεξεν … θεῖον καὶ πῦρ ("rained … brimstone and fire").
- [I] The Sodom resonance in Zophar runs more securely through Deut 32:32 (the vine of Sodom; see A3) than through Gen 19:24.

**Baseline.** Job 18:15 has no exclusive pairs; Job 20:23 has one (with Gen 30:2, irrelevant); Job 1:16 has four, none with Gen 19. גָּפְרִית is rare, and that is the claim's only real asset.

**Rival sources.** Deut 29:22 (18:15–16). Ps 78:49 and 78:24–31 (20:23). 2 Kgs 1:10–14 and 1 Kgs 18:38 (1:16). Job 27:13 (20:29, internal).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Weak (one rare word at 18:15; jussive יַמְטֵר at 20:23; nothing at 1:16 or 20:29) |
| Recurrence | Possible (brimstone/rain/fire spread over two speeches) |
| Thematic coherence | Possible |
| Historical plausibility | Strong |
| History of interpretation | Not checked |
| Satisfaction | Weak |

**Verdict.** **Needs reframing.** Drop 1:16 and 20:29. Hold 18:15 as a Sodom-type motif (via Deut 29:22 as much as Gen 19:24). Read 20:23 with Ps 11:6 as a minor and Ps 78 as the major partner.

**Final rating.** **Low–moderate (motif).** 18:15 brimstone: possible. 20:23 ~ Ps 11:6: possible. 1:16 ~ Gen 19:24: discard.

**Reasoning.** "Brimstone" by itself evokes Sodom, and Ps 11:6 shares the rare jussive "He will rain" on the wicked. Beyond that, each proposed point either fails on the Hebrew (חֵלֶק is not מְנָת) or has a clearly stronger rival (2 Kgs 1:12 for "fire of God from heaven"; Ps 78:49 for "send his burning anger on him"). The Old Greek lacked the brimstone line.

**What a preacher may safely say.** "When Bildad says brimstone is scattered over the wicked man's home, he reaches for the vocabulary of Sodom-like judgement. Zophar's picture of God 'raining' anger on the wicked man while he eats echoes the psalm about Israel in the wilderness, struck while the food was still in their mouths."

---

#### A5: Two Psalter links — Ps 1 at Job 21:16, 18; Ps 18:35 at Job 20:24

**Claim (as tested).** (a) עֲצַת רְשָׁעִים ("counsel of the wicked") occurs only at Ps 1:1; Job 10:3; 21:16; 22:18. Job 21:18's chaff before the wind recalls Ps 1:4 (also Ps 35:5). A Ps 1 window ranks 178th, so the claim is about phrases, not pattern. Proposed rating **moderate–high (phrases)**. (b) קֶשֶׁת נְחוּשָׁה ("bronze bow") occurs only at Job 20:24 and Ps 18:35 [Eng 18:34]. Proposed rating **moderate**.

**Evidence**
- [T] (a) Exact `'עצת רשעים'` → Ps 1:1, Job 10:3, 21:16, 22:18. `co(['6098','7563'])` gives the same four (in-verse co-occurrence, not only the construct). **Verified.** Positive control: Ps 1:1 is returned.
- [T] (a) Within Job it is a refrain. Job 21:16b עֲצַת רְשָׁעִים רָחֲקָה מֶנִּי ("the counsel of the wicked is far from me") is word-for-word Job 22:18b, where Eliphaz throws it back at Job; 10:3 uses it of God. Ps 1:1 is the only text outside Job. BHS at 21:16 proposes מֶנּוּ ("from him"), which does not touch the phrase.
- [T] (a) Job 21:18 יִהְיוּ כְּתֶבֶן לִפְנֵי־רוּחַ וּכְמֹץ גְּנָבַתּוּ סוּפָה ("Are they as straw before the wind, and like chaff which the storm carries away?"). The best partners are not Ps 1:4. **Ps 35:5** יִהְיוּ כְּמֹץ לִפְנֵי־רוּחַ ("let them be like chaff before the wind") shares the whole frame יִהְיוּ כְּ… לִפְנֵי־רוּחַ ("they will be like … before the wind"); exact יהיו כמץ / יהיו כתבן occurs only at Ps 35:5 and Job 21:18. **Isa 17:13** is an exclusive triple, מֹץ ("chaff") + רוּחַ ("wind") + סוּפָה ("storm"), found only at Isa 17:13 and Job 21:18 (`excl_pairs` and my triple scan). Ps 1:4 כַּמֹּץ אֲשֶׁר־תִּדְּפֶנּוּ רוּחַ ("like chaff which the wind drives away") has only מֹץ + רוּחַ. גָּנַב ("steal") + סוּפָה is Job-internal (21:18; 27:20).
- [T] (a) The joint signal still holds. The window test `win(['4671','6098'],3)` → Ps 1:4 and Job 21:18 only. "Counsel of the wicked" and "chaff" within three verses of each other occur only in Ps 1 and Job 21.
- [T] (a) Job 21:17 כַּמָּה נֵר־רְשָׁעִים יִדְעָךְ ("How often is the lamp of the wicked put out?") quotes a proverb word for word: נֵר רְשָׁעִים יִדְעָךְ occurs at Prov 13:9 and 24:20 (and נֵר רְשָׁעִים at Prov 21:4). Job 21:16–18 is a run of stock two-ways sayings (Ps 1:1, Prov 24:20, Ps 35:5 / Isa 17:13, Ps 1:4) that Job lines up in order to dispute them.
- [T] (a) Rank re-run: `base.rank(span('Job',21,7,26),6)` puts Ps 1:1–6 at **101st** of 887 at maxf 150 (65th at maxf 100, 165th at maxf 200), with 3 shared lemmas: מֹץ, חָפֵץ ("delight") and עֵצָה ("counsel"). The claim's 178th was not reproduced exactly with these settings, but the conclusion (no pattern) stands. By IDF Ps 1 is 60th.
- [T] (a) Greek: the Old Greek of Job renders עֲצַת רְשָׁעִים as βουλὴ ἀσεβῶν ("counsel of the ungodly") at 10:3 and 22:18, the same as Ps 1:1 βουλῇ ἀσεβῶν. At 21:16 it has ἔργα δὲ ἀσεβῶν ("works of the ungodly"). Job 21:18 ἄχυρα … κονιορτός ("chaff … dust") does not echo Ps 1:4 χνοῦς ("chaff").
- [T] (b) **"Only these two" is false.** `co(['7198','5154'])` and exact `'קשת נחושה'` → **2 Sam 22:35**, Ps 18:35, Job 20:24. This is a parallel text: 2 Sam 22:35 וְנִחַת קֶשֶׁת־נְחוּשָׁה זְרֹעֹתָי ("and my arms bend a bow of bronze") = Ps 18:35. The phrase is limited to the Song of David and Job 20:24.
- [T] (b) The functions differ. In the Song of David the bronze bow is the king's God-given strength. In Job 20:24 (יִבְרַח מִנֵּשֶׁק בַּרְזֶל תַּחְלְפֵהוּ קֶשֶׁת נְחוּשָׁה, "He may flee from the iron weapon, but the bronze bow will pierce him") it is the weapon from which the fleeing wicked man cannot escape. That is the "flee one danger, meet another" pattern (Amos 5:19; Isa 24:18), though those texts share no lemmas here. Iron with bronze is a common pair (Lev 26:19; Isa 45:2; 48:4; Mic 4:13; Job 28:2; 40:18; 41:19). Window rank for Job 20:23–26 (k=4): 2 Sam 22:32–35 is 10th, Ps 18:32–35 26th. Ps 18:15 [Eng 18:14] בְּרָקִים ("lightnings") with חִצִּים ("arrows") is a slight extra echo of 20:25 בָּרָק ("glittering point").
- [T] (b) Greek: Job 20:24 τόξον χάλκειον against Ps 17:35 / 2 Sam 22:35 τόξον χαλκοῦν (both "bronze bow"). The adjective differs, so the translator did not echo the Psalm.

**Baseline.** Job 21 has 1.03 exclusive pairs per verse. Job 21:16 has two exclusive pairs, one of them Job-internal (with 22:18). Job 21:18's exclusive pairs and triple point to Isa 17:13 and Job 27:20, not to Ps 1. Job 20:24's two exclusive pairs point to Job 29:20 and Ezek 39:9.

**Rival sources.** (a) Ps 35:5 and Isa 17:13 for 21:18; Prov 13:9 / 24:20 for the adjacent 21:17. (b) 2 Sam 22:35 (the parallel); the flight-and-capture trope (Amos 5:19; Isa 24:18).

**Hays criteria**

| Criterion | (a) Ps 1 | (b) Ps 18:35 |
|---|---|---|
| Availability | Strong | Strong |
| Volume | Strong for 21:16 (exclusive phrase); Weak for 21:18 | Possible (exclusive two-word phrase, shared with 2 Sam 22) |
| Recurrence | Strong (10:3; 22:18; chaff in Ps 1:4) | Weak |
| Thematic coherence | Strong (two ways: fate of the wicked) | Weak (royal strength vs. the doomed fugitive) |
| Historical plausibility | Strong | Possible |
| History of interpretation | Not checked | Not checked |
| Satisfaction | Possible | Weak |

**Verdict.** (a) **Confirmed with nuance.** (b) **Needs reframing.**

**Final rating.** (a) **Moderate (phrases): high for עֲצַת רְשָׁעִים, low for the chaff line taken alone.** (b) **Weak–possible.**

**Reasoning.** "Counsel of the wicked" is a phrase Job shares with Ps 1:1 alone, and Job uses it as a refrain. The pairing with chaff three verses on is unique to Ps 1 and Job 21. But 21:18's actual wording is nearer Ps 35:5 and Isa 17:13, and 21:17 quotes Proverbs, so Ps 1 is one source in a run of stock sayings. The bronze bow is shared with the Song of David in both its copies (2 Sam 22; Ps 18), with an opposite function.

**What a preacher may safely say.** "In Job 21:16–18 Job strings together the familiar sayings of the two-ways tradition: Psalm 1's 'counsel of the wicked', Proverbs' 'the lamp of the wicked is put out', and the psalmists' 'chaff before the wind'. Then he asks how often they actually come true."

---

### New candidates surfaced

1. **Lam 2:6–17 behind Job 16:7–18** (Job's portrait of God as assailant). This is the top window by every measure: count 9 lemmas (next 6), IDF **55.2** against 38.6 for the runner-up. That beats the 12-verse null maximum (52.1) and is far above its median top-1 (33.3), with a 1st–5th gap of 22.4 (null median 5.8). Shared: חָרַק ("gnash", 5 verses), חָמַל ("pity"), שַׂק ("sackcloth"), שֵׁן ("tooth"), קֶרֶן ("horn"), צַר ("adversary"), סָגַר ("hand over"), עָפָר ("dust"), שָׁפַךְ ("pour out"). The exact שפך לארץ ("poured out on the earth") occurs only at Lam 2:11 (נִשְׁפַּךְ לָאָרֶץ כְּבֵדִי, "my liver is poured out on the earth") and Job 16:13 (יִשְׁפֹּךְ לָאָרֶץ מְרֵרָתִי, "he pours out my gall on the earth"). Job 16:9–10 חָרַק עָלַי בְּשִׁנָּיו … פָּעֲרוּ עָלַי בְּפִיהֶם ("he gnashed at me with his teeth … they gaped at me with their mouth") matches Lam 2:16 פָּצוּ עָלַיִךְ פִּיהֶם … וַיַּחַרְקוּ־שֵׁן ("they opened their mouths against you … and gnash their teeth"). The Greek has ἔβρυξεν/ἔβρυξαν … ὀδόντας ("gnashed teeth") in both. Lamentations follows Job canonically, so direction is open. Rating: **high (words)**; it should go to whichever auditor holds the Lamentations links. Ps 35:5–16 is a secondary partner (gnashing, witnesses, sackcloth).
2. **Ps 78:49 (with 78:24–31) at Job 20:23.** The exact יְשַׁלַּח־ב־ חֲרוֹן אַפּוֹ ("he sends his burning anger upon …") occurs only at Ps 78:49 and Job 20:23. The same psalm has God "rain" food and strike "while their food was in their mouths" (78:27–31). Rating: **moderate–high (words and sequence).**
3. **Isa 53:9 at Job 16:17.** The exact עַל לֹא־חָמָס ("although no violence") occurs only at these two, and both pair innocence of deed with innocence of speech. Rating: **moderate (words)**; it rivals A2.
4. **2 Kgs 1:12 at Job 1:16.** The exact אֵשׁ אֱלֹהִים ("fire of God") occurs only at these two, with מִן־הַשָּׁמַיִם ("from heaven") and אָכַל ("consume"). The Old Greek of Job 1:16 matches 1 Kgs 18:38 LXX. Rating: **moderate–high**; it replaces Gen 19:24.
5. **Prov 13:9 / 24:20 at Job 21:17.** The verbatim נֵר רְשָׁעִים יִדְעָךְ ("the lamp of the wicked is put out"). Rating: **high (phrase)**. It is cited by the speaker in order to be disputed.
6. **Gen 4:10 and Isa 26:21 at Job 16:18.** Gen 4:10: דָּם + צָעַק ("blood" + "cry"), with Job's cognate זְעָקָה ("cry"); BHS cites "cf Gn 4,10". Isa 26:21: אֶרֶץ + כָּסָה + דָּם ("earth" + "cover" + "blood"), the top `partners` hit. Rating: **moderate**.
7. **Isa 44:6 at Job 19:25.** An exclusive pair גֹּאֵל + אַחֲרוֹן ("redeemer" + "last"), with Isa 44:4–8 2nd in the window rank for 19:23–27. The words are common, so the evidence is thin. Rating: **possible**.
8. **Gen 31:37–42 behind Job 9:33 and 16:21** (and behind 1 Chr 12:18). Shared: יְגִיעַ כַּפַּי ("the toil of my palms", also Job 10:3); רָאָה … וַיּוֹכַח ("saw … and decided"); and יָכַח + בֵּין ("decide between": Gen 31:37; Isa 2:4; Mic 4:3; Job 9:33). Rating: **possible–moderate.**

### Key evidence for spot checks

1. `alib.lem('2617','Job')` → ['Job 6:14','Job 10:12','Job 37:13'] (positive control).
2. `alib.co(['5707','6965','6030'])` → ['Deut 19:16','Job 16:8']; but `co(['5707','2555'])` → Deut 19:16, Exod 23:1, Ps 27:12, Ps 35:11 (חָמָס sits in the companion verses, not Job 16:8). Rahlfs Job 16:8b is asterisked.
3. `base.rank(base.span('Job',16,7,18),12)` → Lam 2:6–17 first (9); Ps 35:5–16 5th (6); Deut 19 12th (4). The IDF version gives Lam 2 55.2, Ps 35 38.6, Deut 19 27th.
4. `alib.co(['2555','3198'])` → ['1Chr 12:18']; exact 'על לא חמס' → ['Isa 53:9','Job 16:17']; the consonants ויוכח occur as 5 tokens (Gen 31:42; 1 Chr 16:21; Ps 105:14 wayyiqtol; 1 Chr 12:18 and Job 16:21 jussive).
5. `alib.co(['6620','7219'])` → ['Deut 32:33','Job 20:16']; `alib.lem('4846')` → ['Deut 32:32','Job 13:26','Job 20:14','Job 20:25'].
6. `base.rank(base.span('Job',20,4,29),12,maxf=150,mark=('Deut',32))` → MARK rank 5 of 887, 7 lemmas; the 26-verse null (20 passages) gives top-1 median 9 and 5th median 7.5. Very-rare (at most 15 verses) ranking: Deut 32:22–33 has 4, next 2, null median 2.
7. Cluster baseline: of 1,068 three-verse Job windows, 3 share at least 3 lemmas of at most 15 verses with a non-Job two-verse window; Job 20:14 → Deut 32:32 is one. Swete/Rahlfs: θυμὸς δρακόντων occurs only at Deut 32:33 (and Ode 2:33), echoed at Job 20:16 θυμὸν δὲ δρακόντων.
8. Exact 'אש אלהים' → ['2Kgs 1:12','Job 1:16']; Job 20:29 lemma חֵלֶק 2506 a against Ps 11:6 מְנָת 4521; exact 'ישלח בם/בו חרון אפו' → ['Ps 78:49','Job 20:23'].
9. Exact 'עצת רשעים' → Ps 1:1, Job 10:3, 21:16, 22:18; exact 'יהיו כמץ/כתבן' → Ps 35:5, Job 21:18; the exclusive triple מֹץ + סוּפָה + רוּחַ → Isa 17:13 only.
10. `alib.co(['7198','5154'])` → ['2Sam 22:35','Job 20:24','Ps 18:35'] (the parallel text breaks "only these two").

---

## Part B: The Latter Prophets

### Auditor's note

**Corpus.** Hebrew: WLC text and Strong's lemma index (the observation layer), through `alib`. Greek OT: Swete (all books) and the Rahlfs–Hanhart Logos exports (Job, Isaiah, Jeremiah, Psalms, Amos, Micah, Genesis). There is no Rahlfs export for Habakkuk, so Habakkuk's Greek comes from Swete only. English: the NASB95 exports. BHS Job text and apparatus: `02-Job-BHS.txt` and `02-Job-BHS-App.txt`. No web sources and no commentaries were used. History of interpretation is **not checked** throughout.

**Positive control.** `alib.lem('2617','Job')` returned Job 6:14, 10:12, 37:13, as required. Every "only" search below returned the proposed source verse itself, so each search serves as its own known-hit control. Before reporting absences I also ran these extra known-hit checks: `lem('5842')` returned Jer 8:8, 17:1, Job 19:24, Ps 45:2 (the known stylus verses); `co(['8596','3658'])` returned Isa 5:12 and Job 21:12, both known; exact `שערי שאול` returned Isa 38:10, known; `rparse('02-Jeremiah')` returned Jer 17:5 onwards (which is how the absence of 17:1–4 was confirmed); and `sw('Job 15:26')` returned text, confirming the Swete keys.

**Method.** I searched lemmas with `lem`/`co`, plus a ±n-verse window helper (`chk_helpers.win`). Every phrase was checked by exact consonants against `alib.TX`, as well as by `ph`. The skeletal pass in `ph` over-matches badly on short words: `ph('נין')` returns more than 400 verses, and `ph('ערבני')` adds Gen 43:9. Ketiv forms were checked with `ketiv()`. The only ketiv forms in the target passages are Job 15:22 וצפו and 15:31 בשו, and neither affects a claim. I also checked for cognate and homograph splits (מְכַסֶּה 4374 vs כסה 3680; זעק 2199 vs צעק 6817; מִשְׁפָּט 4941 vs שׁפט 8199; לָעַד filed as 5707 in Isa 30:8 and as 5703 in Job 19:24) and for parallel texts (Isa 36–39 = 2 Kgs 18–20; 1 Kgs 22 = 2 Chr 18; Ps 18 = 2 Sam 22). Window ranks were run with my own quiet copy of `base.rank`. Its output is identical to `base.rank` on six spot calls (Isa 14 2nd, Isa 44 2nd, Isa 30 6th, Isa 38 27th, Lam 2 1st, Isa 5 1st). Verse partners come from `aux.partners` and window overlap from `aux.win_overlap` (maxfreq 400).

**Baselines used.** These are the brief's figures for exclusive content-lemma pairs per verse (maxf 400): Job overall 1.34, Job 15 0.94, 16 0.55, 17 1.06, 18 1.00, 19 1.48, 21 1.03. I computed `excl_pairs` for every key verse. For example, Job 19:24 alone has three exclusive pairs, two of them plainly chance pairs (with Isa 51:1 and Isa 26:4).

**Window-rank null.** I drew random contiguous Job passages, using seeded start verses in Job 4–14 and 22–31. For each I ran the same rank and recorded the scores of the 1st, 2nd and 5th windows.

| Length / k / maxf | n | top-1 median (range) | 2nd median | 5th median | gap 1st–5th median (range) |
|---|---|---|---|---|---|
| 19 / 10 / 150 (B1) | 16 | 8 (5–10) | 7 | 6 | 2 (0–5) |
| 17 / 15 / 150 (B2) | 16 | 8 (6–11) | 7.5 | 7 | 1 (0–3) |
| 20 / 9 / 150 (B3) | 16 | 8 (6–9) | 7 | 6 | 1 (0–4) |
| 12 / 12 / 150 (Lam 2 test) | 16 | 6 (4–8) | 5 | 5 | 1 (0–2) |
| 10 / 10 / 150 (Isa 5 test) | 16 | 5 (4–7) | 5 | 4 | 1 (0–2) |
| 5 / 5 / 150 (B5, B6) | 20 | 3.5 (2–5) | 3 | 3 | 1 (0–2) |
| 5 / 5 / 400 (B5, B6) | 20 | 4 (4–6) | 4 | 4 | 1 (0–2) |

**Hubness test (added).** A window rank only tells us something if the source chapter does not rank highly against *any* Job passage. So I ranked each proposed source chapter against 30 (or 40) random Job passages of the same length and k.

| Source | Test (L/k) | median rank | top-3 | top-10 |
|---|---|---|---|---|
| Isa 59 | 19/10 | 11.5 | 10/30 (1st in 5) | 14/30 |
| Isa 59 | 17/15 | 13.5 | 8/30 | 11/30 |
| Isa 33 | 19/10 | 25 | 0/30 | 8/30 |
| Isa 5 | 17/15 | 12 | 6/30 (1st in 5) | 13/30 |
| Isa 14 | 17/15 | 88.5 | 1/30 | 3/30 |
| Ps 7 | 19/10 | 212 | 0 | 0 |
| Isa 38 | 20/9 | 311.5 | 0 | 0 |
| Lam 2 / Lam 3 | 12/12 | 187.5 / 194 | 0 | — |
| Isa 44 | 5/5 (150) | 136 | 2/40 | 3/40 |
| Isa 30 | 5/5 (150) | 153 | 0/40 | 3/40 |
| Jer 17 | 5/5 (150) | 225.5 | 0/40 | 0/40 |

Isa 59 and Isa 5 are "hubs": generic lament-and-judgement chapters that sit near the top for many arbitrary Job passages. A high rank for them carries little information.

**Greek.** In the Rahlfs Job export, the asterisk sign marks hexaplaric material and the metobelus sign closes it; `†` is a Logos footnote marker. The export is inconsistent: it has 212 asterisks against 135 metobeli. At Job 19:24 there is an **orphan metobelus** after 24a with no surviving opening sign, so the status of 19:24 should be checked in Logos.

**Limits.** All counts are lemma counts in WLC unless stated otherwise. Lemma homographs and splits were checked by hand only where a claim depends on them. Selection effects: any source found by scanning a ranked list is post hoc. The new candidates below were found that way, but each was then tested at verse level and against the null.

---

#### B1: Isa 59:1–10 behind Eliphaz's portrait (Job 15:17–35)

**Claim (as tested).** Job 15:35 speaks in the words of Isa 59:4. The idiom הרה ("conceive") + עָמָל ("mischief") + ילד ("bring forth") + אָוֶן ("iniquity") occurs only in Job 15:35, Isa 59:4 and Ps 7:15. Further support is offered from רוץ ("run"), darkness and שָׁוְא ("emptiness"), and from Isa 59:1–10 ranking 2nd of 887 windows. Proposed rating: **moderate–high**.

**Evidence**
- [T] Verified (WLC): `co(['2029','5999','3205','205'])` returns Isa 59:4, Job 15:35 and Ps 7:15 only. The pairs הרה ("conceive") + עָמָל ("mischief") and הרה ("conceive") + אָוֶן ("iniquity") also occur only in these three verses. The exact string הרו עמל והוליד און ("they conceive mischief and bring forth iniquity") occurs only in Isa 59:4. So this is a three-text idiom, not a pair.
- [T] Form and order favour Isaiah over the Psalm. Job 15:35 has הָרֹה עָמָל וְיָלֹד אָוֶן ("conceiving mischief and bearing iniquity"), with two infinitives absolute. Isa 59:4 has הָרוֹ עָמָל וְהוֹלֵיד אָוֶן ("conceiving mischief and begetting iniquity"), also two infinitives absolute, in the same order עָמָל ("mischief") → אָוֶן ("iniquity"). Ps 7:15 uses finite verbs, puts אָוֶן ("iniquity") first and ends with שָׁקֶר ("falsehood").
- [T] There is an adjacent "trust in emptiness" link. Isa 59:4 has בָּטוֹחַ עַל־תֹּהוּ וְדַבֶּר־שָׁוְא ("They trust in confusion and speak lies"); Job 15:31 has אַל־יַאֲמֵן בַּשָּׁו ("Let him not trust in emptiness"; ketiv בשו, BHS: "mlt Mss בשׁוא"). The verbs differ (בטח "trust" against אמן "rely"), and שָׁוְא ("emptiness") occurs in 48 verses. `co(['7723','982'])` returns Isa 59:4 and Ps 31:7 only. The link is supportive, not decisive. [I]
- [T] The other proposed items are generic. רוץ ("run") occurs in 92 verses, and the function differs: in Isa 59:7 feet run to evil, while in Job 15:26 the wicked man charges at God. חֹשֶׁךְ ("darkness") occurs in 77 verses and כסה ("cover") in 149.
- [T] Job has its own antecedent. Eliphaz already pairs אָוֶן ("iniquity") and עָמָל ("trouble") at 4:8 (חֹרְשֵׁי אָוֶן וְזֹרְעֵי עָמָל, "those who plough iniquity and sow trouble") and at 5:6. `co(['5999','205'])` gives 11 verses. Job 15:35 adds the birth metaphor to Eliphaz's signature pair.
- [T] Window rank reproduced. `base.rank(span('Job',15,17,35),10,maxf=150)` gives Isa 33:9–18 first (8 shared rare lemmas), then **Isa 59:1–10 2nd (7; tied 2nd–3rd with Ps 55:3–12)**, with Ps 7:6–15 8th (6; tie band 4th–10th). At maxf 400, Isa 59 falls to 9th and Ps 7 is 6th. With k=19, Isa 59 is 5th (maxf 150) or 10th (maxf 400).
- [T] **The hubness test removes the force of the rank.** Against 30 random 19-verse Job passages, Isa 59 ranks in the top three ten times and first five times. It is the top window for Job 5:12–6:3, 6:21–7:9 and 26:1–27:5. Its score of 7 here equals the null median for the 2nd-placed window. Proposing it before the ranking was run does not help, because Isa 59 ranks high against almost anything in Job.
- [T] Greek. OG Job 15:35 has ἐν γαστρὶ δὲ λήμψεται ὀδύνας, ἀποβήσεται δὲ αὐτῷ κενά. This does not echo Isa 59:4 LXX (κύουσιν πόνον καὶ τίκτουσιν ἀνομίαν) or Ps 7:15 (συνέλαβεν πόνον καὶ ἔτεκεν ἀνομίαν). The κενά in 15:35 repeats 15:31's κενά (for שָׁוְא, "emptiness"), and Isa 59:4 LXX also has λαλοῦσιν κενά (for דַבֶּר־שָׁוְא, "speak lies"). This is data only. Job 15:31, 34 and 35 are not asterisked; the only asterisks in 15:17–35 are on 15:26b and 15:27b.

**Baseline.** Job 15 averages 0.94 exclusive pairs per verse. The idiom is not an exclusive pair at all (three texts). `excl_with_book` from Job 15:17–35 to Isaiah yields only chance pairs (15:23 with Isa 51:13 and 21:14; 15:31 with Isa 30:28) plus 15:34 with Isa 33:14, which is noted below. None involves Isa 59.

**Rival sources**
- **Isa 33:11–15** (new; see New candidates). Isa 33:11 has תַּהֲרוּ חֲשַׁשׁ תֵּלְדוּ קַשׁ רוּחֲכֶם אֵשׁ תֹּאכַלְכֶם ("You have conceived chaff, you will give birth to stubble; my breath will consume you like a fire"). Isa 33:14 has חֲנֵפִים ("the godless") with אֵשׁ אוֹכֵלָה ("consuming fire"), and 33:15 has שֹּׁחַד ("bribe"). Job 15:34–35 has חָנֵף ("godless"), אֵשׁ אָכְלָה ("fire consumes"), שֹׁחַד ("bribery") and הָרֹה … וְיָלֹד ("conceive … bring forth"), and 15:30 has בְּרוּחַ פִּיו ("by the breath of His mouth"). חנף ("godless") + שֹׁחַד ("bribe") within ±2 verses occurs only in Isa 33:14 and Job 15:34. הרה ("conceive") + אֵשׁ ("fire") within ±1 verse occurs only in Isa 33:11 and Job 15:35. Isa 33:9–18 is the top-ranked window.
- **Ps 7:15** remains as a third witness to the idiom, and **Ps 10:7** shares עָמָל ("mischief") + אָוֶן ("iniquity") + מִרְמָה ("deceit"; cf. 15:35b).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible (four-word idiom; closest form to Isaiah, but shared with Ps 7) |
| Recurrence | Weak (Isa 59's other contacts with Job, e.g. עַכָּבִישׁ "spider" only Isa 59:5 and Job 8:14, are not diagnostic given its hubness) |
| Thematic coherence | Possible |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Needs reframing.
**Final rating.** Low–moderate: a shared idiom, with Isa 59:4 the closest formal witness. The window-rank argument is withdrawn. Isa 33:11–15 is at least an equal co-source for 15:34–35.
**Reasoning.** The idiom is real, and Job matches Isaiah's syntax and word order more closely than Ps 7. The upgrade rested on the window rank, but Isa 59 ranks in the top three for a third of arbitrary Job passages. The remaining items are common words used differently, and for the closing verses Isa 33 supplies a tighter cluster (conceive/bear, fire consumes, godless, bribe).
**What a preacher may safely say.** "Eliphaz uses a stock phrase also found in Isaiah 59 and Psalm 7: the wicked 'conceive mischief and bring forth iniquity'."

---

#### B2: Isa 14:9–23 behind Bildad's portrait (Job 18:5–21), with echoes in Job 21:12–13, 26, 32

**Claim (as tested).** נִין ("offspring") + נֶכֶד ("posterity") occur only in Gen 21:23, Isa 14:22 and Job 18:19. A window over Isa 14 ranks 2nd of 887. Isa 14:11 (harps, Sheol, maggots) is heard at Job 21:12–13, 26, and the tomb contrast is Isa 14:19 against Job 21:32. Proposed rating: **moderate–high**.

**Evidence**
- [T] Verified (WLC): `lem('5209')` and `lem('5220')` each return Gen 21:23, Isa 14:22 and Job 18:19, so each word occurs in three verses. The exact string נין ונכד occurs only in Isa 14:22. Gen 21:23 is an oath *protecting* descendants; Isa 14:22 and Job 18:19 are both about *cutting off* a line. Isaiah matches Job's function.
- [T] The match is a cluster, not one pair. Isa 14:21–22 has תֵבֵל ("world"), שֵׁם ("name"), שְׁאָר ("remnant"), נִין ("offspring") and נֶכֶד ("posterity"). Job 18:17–19 has זֵכֶר ("memory"), שֵׁם ("name"), תֵּבֵל ("inhabited world", 18:18), נִין ("offspring"), נֶכֶד ("posterity") and שָׂרִיד ("survivor"). תֵבֵל ("world") + נִין ("offspring") within ±2 verses occurs **only** in Isa 14:21 and Job 18:18.
- [T] Isa 14:11 → Job 21:26 is hidden by a lemma split. Isa 14:11 has וּמְכַסֶּיךָ תּוֹלֵעָה ("worms are your covering"; the noun מְכַסֶּה, 4374) beside רִמָּה ("maggot"). Job 21:26 has וְרִמָּה תְּכַסֶּה עֲלֵיהֶם ("and worms cover them"; the verb כסה, 3680). `co(['7415','3680'])` returns Job 21:26 only and `co(['7415','4374'])` returns Isa 14:11 only. So רִמָּה ("maggot") + the root כסה ("cover") occurs in these two verses alone. In addition, רִמָּה ("maggot") + תּוֹלֵעָה ("worm") occurs only in Isa 14:11 and Job 25:6 (Bildad). Greek: Isa 14:11 κατακάλυμμα … σκώληξ; Job 21:26 σαπρία … ἐκάλυψεν; Job 25:6 σαπρία … σκώληξ.
- [T] The harps item does not match well. Isa 14:11 has נֵבֶל ("harp") with Sheol. Job 21:12 has תֹּף ("timbrel") + כִּנּוֹר ("lyre") + עוּגָב ("pipe"), with Sheol in 21:13. The instruments differ. The only text other than Job 21:12–13 with timbrel and lyre within ±3 verses of Sheol is **Isa 5:12, 14**.
- [T] The tomb item is common. קֶבֶר ("grave") occurs in 62 verses. Isa 14:19 "you have been cast out of your tomb" against Job 21:32 "while he is carried to the grave" is a thematic contrast only. [I]
- [T] Window rank. `base.rank(span('Job',18,5,21),15)` gives Isa 5:16–30 first (8), then **Isa 14:16–30 2nd (7; tied 2nd–4th)**. The best Isa 14 window runs past the pericope into the oracles on Assyria and Philistia: 14:29–30 שֹׁרֶשׁ ("root") supplies the match for 18:16. The proposed pericope 14:9–23 scores only 5 shared rare lemmas, and 17 chapters score more. At maxf 400 Isa 14 falls to 8th. The null for 17-verse passages has a top-2 median of 7.5, so a 7 is typical. Isa 14 is not a hub (median rank 88.5), so its placing is mildly informative, but the rank is carried by the נִין/נֶכֶד ("offspring/posterity") pair.
- [T] Greek. In Rahlfs Job 18:17b, "he has no name abroad", is **asterisked**: the OG lacked the "name" line. So is 18:16b. OG 18:19 paraphrases ("he will not be known among his people") and does not echo Isa 14:22 LXX ὄνομα καὶ κατάλειμμα καὶ σπέρμα. Job 21:32b, the watch over the tomb, is also asterisked. Job 21:12 OG has ψαλτήριον καὶ κιθάραν and Isa 5:12 LXX has κιθάρας καὶ ψαλτηρίου (data).

**Baseline.** Job 18 averages 1.00 exclusive pairs per verse. Job 18:19 has no exclusive pair at maxf 400, because the pair occurs in three verses. The case rests on the cluster (name, world, offspring, posterity, remnant~survivor) and on the matching function.

**Rival sources**
- **Isa 5:11–20 for Job 21:12–16** (new). It ranks 1st of 887 against Job 21:7–16 (k=10: 6 against 4; null top-1 median 5, range 4–7; its gap of 2 is at the top of the null range). Isa 5 is a semi-hub (median rank 26 at this length). Shared items: כִּנּוֹר ("lyre"), תֹּף ("timbrel"), Sheol; דַּעַת ("knowledge": Isa 5:13 "for lack of knowledge" ~ Job 21:14 "we do not desire the knowledge of Your ways"); and עֵצָה ("counsel": Isa 5:19 ~ 21:16).
- **Amos 2:9 for Job 18:16** (new). שֹׁרֶשׁ ("root") + מִמַּעַל ("above") + מִתַּחַת ("below") occur only in Amos 2:9 and Job 18:16.
- Prov 10:7 (זֵכֶר "memory" + שֵׁם "name" of the wicked) and Ps 109:13 for 18:17.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible (a rare pair occurring in three texts, inside a four-lemma cluster) |
| Recurrence | Possible (Isa 14:11 at Job 21:26 and 25:6) |
| Thematic coherence | Strong (extinction of the tyrant's name and line) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.
**Final rating.** Moderate for Isa 14:21–22 at Job 18:17–19, and for Isa 14:11 at Job 21:26 (and 25:6). Job 21:12–13 should be reassigned to Isa 5:11–14 (moderate). The tomb contrast at 21:32 is low.
**Reasoning.** The offspring/posterity pair sits in a tight cluster with "name", "world" and a remnant/survivor slot, and the worm-covering link survives a lemma split. Both support real contact with Isa 14's fall of the tyrant. The 2nd-of-887 rank depends on a window outside the pericope and is ordinary against the null. The music-to-Sheol line belongs with Isa 5, whose instruments match Job's exactly.
**What a preacher may safely say.** "Bildad's picture of the wicked man whose name and line are cut off uses the rare words of Isaiah's taunt over Babylon's king, 'offspring and posterity' (Isa 14:22)."

---

#### B3: Hezekiah's psalm (Isa 38:10–18) behind Job 16:19–17:16

**Claim (as tested).** The imperative of ערב ("be surety") occurs only in Ps 119:122, Isa 38:14 and Job 17:3, and Isa 38:14 and Job 17:3 share the identical form עָרְבֵנִי ("be my surety"). Further links are offered: מָרוֹם ("on high"), eyes, "gates of Sheol" and שַׁחַת ("pit"), with Isa 38 ranking 29th of 887. Proposed rating: **form exclusive — high; Hezekiah frame — moderate (synthetic)**.

**Evidence**
- [T] Verified (WLC). Of the 23 verses with ערב (6148), only three have an imperative: Ps 119:122 עֲרֹב ("be surety"), Isa 38:14 עָרְבֵנִי ("be my surety") and Job 17:3 עָרְבֵנִי ("be my surety"). The exact consonants ערבני occur only in Isa 38:14 and Job 17:3 (`ph` adds Gen 43:9 by skeletal over-match). Hezekiah's psalm (Isa 38:9–20) has no counterpart in 2 Kgs 20, so the parallel text adds no witness. 2 Kgs 18:23 = Isa 36:8 is a hitpael ("make a wager") and is irrelevant.
- [T] BHS apparatus at Job 17:3: "ᵃ prp עֵרְבֹנִי", i.e. the noun "my pledge". The exclusive form rests on MT.
- [T] Greek. OG Job 17:3a has ἔκλεψαν δέ μου τὰ ὑπάρχοντα ἀλλότριοι ("strangers stole my goods"), and 17:3b is **asterisked**. Isa 38:14 LXX has ὃς ἐξείλατό με ("who delivered me"). Neither Greek renders a surety imperative.
- [T] Heights and eyes. Isa 38:14 has דַּלּוּ עֵינַי לַמָּרוֹם ("my eyes look wistfully to the heights"); Job 16:19–20 has בַּמְּרוֹמִים ("on high") … דָּלְפָה עֵינִי ("my eye weeps"). דלל ("grow weak") and דלף ("drip") make a sound-play. [I] Isa 38:14 holds מָרוֹם ("height"), עַיִן ("eye") and ערב ("be surety") in one verse; Job spreads them from 16:19 to 17:3, across a chapter boundary. מָרוֹם ("height") occurs in 52 verses.
- [T] **The "gates of Sheol" parallel is not in the text.** Job 17:16 reads בַּדֵּי שְׁאֹל ("the bars [or limbs] of Sheol"). שַׁעֲרֵי שְׁאוֹל ("gates of Sheol") occurs only in Isa 38:10 (exact). Only שְׁאוֹל ("Sheol") is shared (64 verses). Sheol + שַׁחַת ("pit") within ±3 verses occurs in Isa 38:18, Job 17:13–16, Ps 9:18 and Ps 16:10.
- [T] Rank. With k=9 and maxf 150, Isa 38:6–14 is **27th, on a score of 4, tied 19th–57th**; the window even starts in the narrative at 38:6. With k=20 it is 31st (tie band 21st–60th), and at maxf 400 between 10th and 27th. I could not reproduce "29th" exactly. Isa 38:9–20 shares only four rare lemmas with the Job passage: מָרוֹם ("height"), ערב ("be surety"), שְׁאוֹל ("Sheol"), שַׁחַת ("pit"). The null top-1 median for this length is 8 (range 6–9). Isa 38 is not a hub (median 311.5), so a place inside a tie band at 2–6% is not nothing, but the "top 3½%" figure is not stable.

**Baseline.** Job 17 averages 1.06 exclusive pairs per verse. Job 17:3's own exclusive pairs at maxf 400 are chance pairs with מִי ("who"): Jer 30:21 and Nah 3:19. The surety link is a three-text item, sharpened only by the identical form.

**Rival sources**
- **The surety formula of Proverbs**: ערב ("be surety") + תקע ("strike [hands]") occur only in Job 17:3, Prov 6:1, 11:15, 17:18 and 22:26. Job 17:3b מִי הוּא לְיָדִי יִתָּקֵעַ ("who is there that will be my guarantor", lit. "strike my hand") is the legal formula of Proverbs.
- **Ps 119:122** (surety + עשק "oppress", like Isa 38:14 עָשְׁקָה־לִּי "I am oppressed").
- Isa 33 heads `win_overlap` for this passage (69.6), but it is semi-hub.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible (one rare, identical word) |
| Recurrence | Weak |
| Thematic coherence | Possible (a dying man appeals to God as guarantor) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance (form); the Hezekiah frame needs reframing.
**Final rating.** Form link **moderate**, not high: it depends on MT, the imperative + "me" is the natural form for anyone asking a guarantor, and the hand-striking half is Proverbs' idiom. Hezekiah frame **low–moderate**.
**Reasoning.** Job and Hezekiah do address God with the same rare imperative, and both look "to the heights" through failing eyes. That is genuine contact. But the other frame items are ordinary Sheol vocabulary, "gates of Sheol" is not in Job, and the rank sits in a wide tie band at half the null's typical top score.
**What a preacher may safely say.** "Job's cry, 'be my surety', uses the same word as Hezekiah's prayer from his sickbed (Isa 38:14); both men ask God himself to stand guarantor."

---

#### B4: The Servant pattern at Job 16:10, 17

**Claim (as tested).** Job 16:17 עַל לֹא־חָמָס ("although there is no violence") matches Isa 53:9 עַל לֹא־חָמָס עָשָׂה ("because he had done no violence"), and the phrase occurs only in these two verses. Isa 50:6 and Mic 4:14 are heard at Job 16:10 (the cheek), read with other proposed Servant links (Isa 49:4 at 9:29; Isa 53:7 at 3:1). Proposed rating: **phrase moderate; pattern moderate (synthetic)**.

**Evidence**
- [T] Verified: the exact string על לא חמס occurs only in Isa 53:9 and Job 16:17, by both exact substring and `ph`. But the "phrase" is preposition + negative + noun. **1 Chr 12:18** בְּלֹא חָמָס בְּכַפַּי ("since there is no wrong in my hands", David's words) shares the longer string לא חמס בכפי ("no violence in my hands") with Job 16:17. Exact consonants: Job 16:17 and 1 Chr 12:18 only. So Job's colon matches Isaiah in its first word and Chronicles in its last. חָמָס ("violence") + כַּף ("palm/hand") is a stock collocation: 1 Chr 12:18; Isa 59:6; Jonah 3:8; Job 16:17.
- [T] The function matches. Isa 53:9 pairs "no violence" with "nor was there any deceit in His mouth". Job 16:17 pairs "no violence in my hands" with "my prayer is pure". Both declare innocence of deed and of speech. [I]
- [T] The cheek. לְחִי ("cheek") + נכה ("strike") occurs in 9 verses (1 Kgs 22:24 = 2 Chr 18:23; Isa 50:6; Job 16:10; Judg 15:15–16; Lam 3:30; Mic 4:14; Ps 3:8). With חֶרְפָּה ("reproach") added, **only Job 16:10 and Lam 3:30**; this is an exclusive pair in `excl_pairs('Job 16:10')`. Isa 50:6 has לְחִי ("cheek") with מֹרְטִים ("those who pluck"), מַכִּים ("smiters") and כְּלִמּוֹת ("humiliation"), but no חֶרְפָּה ("reproach"). Greek: Job 16:10 OG ἔπαισέν με εἰς σιαγόνα; Lam 3:30 τῷ παίοντι αὐτὸν σιαγόνα (παίω + σιαγών in both); Isa 50:6 σιαγόνας … ῥαπίσματα; Mic 4:14 πατάξουσιν ἐπὶ σιαγόνα.
- [T] Window. Lam 2:6–17 ranks **1st of 887** against Job 16:6–17 (k=12, maxf 150), scoring 9 against 6 for the next. The null gives a top-1 median of 6 (range 4–8) and a 1st–5th gap of 1 (range 0–2). Lam 2's score and margin both exceed the null, and Lam 2 is not a hub (median rank 187.5). By the same measure Isa 50 is 62nd (3) and Isa 53 is 464th.
- [T] Other Servant links. Isa 49:4 at Job 9:29: יגע ("toil") + הֶבֶל ("vanity") is an exclusive verse pair (verified), but both words are common, and Job 19 alone averages 1.48 such pairs per verse. Isa 53:7 at Job 3:1: פתח ("open") + פֶּה ("mouth") occurs in 25 verses, so the contrast is interpretive. Isa 50:8–9 at Job 13:19 was confirmed with nuance by an earlier audit and was not re-tested.
- [T] Greek. OG Job 16:17 has ἄδικον δὲ οὐδὲν ἦν ἐν χερσίν μου; Isa 53:9 LXX has ἀνομίαν οὐκ ἐποίησεν. There is no echo. Job 16:10 and 16:17 are OG; 16:21b is asterisked.

**Baseline.** Job 16 averages 0.55 exclusive pairs per verse. Job 16:17 has none at maxf 400 or 700, so the Isaiah contact rests on a three-word string whose content words are shared with 1 Chr 12:18.

**Rival sources**
- **1 Chr 12:18** for the innocence formula.
- **Lam 3:30**, and the whole complex of **Lam 2:6–17 and 3:1–16**, for the assault on Job in 16:9–16 (new; see New candidates).
- Ps 3:8, Mic 4:14 and 1 Kgs 22:24 (striking the cheek). For the gaping mouth, Ps 22:14 and Lam 2:16 use פצה ("open wide"), not Job's פער ("gape").

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Weak (three-word string; the content words are shared with 1 Chr 12:18) |
| Recurrence | Weak (the other Servant contacts are common words or interpretive) |
| Thematic coherence | Possible (an innocent sufferer struck and shamed) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Weak |

**Verdict.** Needs reframing.
**Final rating.** Phrase **low–moderate**. Servant pattern **low** (synthetic). Lam 2–3 replaces Isa 50:6 for the assault language of 16:9–16.
**Reasoning.** The exclusive string is short and functional, and its fuller form is shared with David's protest in 1 Chr 12:18. The cheek-striking has an exclusive partner in Lam 3:30, not in Isa 50:6. Lamentations 2 is the one source that beats the null by a clear margin for this whole stretch of Job 16. A Servant reading remains a legitimate canonical reflection, but it is not a demonstrated design.
**What a preacher may safely say.** "Job's 'no violence in my hands' sounds like Isaiah's Servant who 'had done no violence' (Isa 53:9); Christians have heard the two together, but Job's words are closer still to Lamentations' sufferer struck on the cheek."

---

#### B5: Writing for the last day — Isa 30:8 behind Job 19:23–25; Jer 17:1 behind 19:24

##### (a) Isa 30:8

**Claim (as tested).** כתב ("write") + סֵפֶר ("book") + חקק ("inscribe") occur only in Isa 30:8 and Job 19:23. Isa 30:8 also has אַחֲרוֹן ("last") and לָעַד ("for ever"/"as a witness"). Isa 30:6–10 ranks 6th of 887. Proposed rating: **moderate–high**.

**Evidence**
- [T] Verified (WLC). `co(['3789','5612','2710'])` returns Isa 30:8 and Job 19:23 only. סֵפֶר ("book") + חקק ("inscribe") alone also occur only in these two verses. כתב ("write") + חקק ("inscribe") adds Isa 10:1. (חקק, סֵפֶר) is an exclusive pair in `excl_pairs('Job 19:23')`.
- [T] Feature window (added test). I took nine features of Job 19:23–25: כתב ("write"), סֵפֶר ("book"), חקק ("inscribe"), אַחֲרוֹן ("last"), consonantal לעד ("for ever"), עֵט ("stylus"), בַּרְזֶל ("iron"), צוּר ("rock"), חצב ("hew"). The best three-verse window outside Job is **Isa 30:6–8 with five of them** (write, book, inscribe, last, for ever). The next best anywhere has three: the Chronicler's formula "first and last … written in the book", Deut 31:24–26 (write, book, as a witness) and Jer 17:1 (write, stylus, iron).
- [T] The לָעַד homograph. WLC files Isa 30:8 לָעַד under 5707 עֵד ("witness") and Job 19:24 לָעַד under 5703 ("for ever"), though consonants and pointing are identical. NASB95 renders Isa 30:8 "As a witness forever". The form is common (exact לָעַד in 29 verses), so it counts only inside the cluster.
- [T] אַחֲרוֹן ("last"; 48 verses): Isa 30:8 לְיוֹם אַחֲרוֹן ("for the time to come"); Job 19:25 וְאַחֲרוֹן ("at the last").
- [T] Greek (data). In all of Swete, βιβλι- + αἰων- in one verse occurs **only in Isa 30:8** (εἰς βιβλίον … ἕως εἰς τὸν αἰῶνα) **and Job 19:23** (ἐν βιβλίῳ εἰς τὸν αἰῶνα). Job's translator moved "for ever" from 19:24 into 19:23, which produces Isaiah's collocation. Swete Job 19:24 lacks 24b (ἢ ἐν πέτραις ἐγγλυφῆναι), which Rahlfs prints; Rahlfs also has the orphan metobelus after 24a noted above.
- [T] Rank. Isa 30:6–10 is **6th (k=5, maxf 150; score 3, tied 3rd–9th)** and 2nd at maxf 400 (5). The null for 5-verse passages has a top-1 median of 3.5 (maxf 150) or 4 (maxf 400), so these scores are ordinary. Isa 30 is not a hub. The window rank re-counts the same lemmas as the verse-level search and adds nothing independent.
- [I] Function. Isa 30:8 is testimony written down for a later day against a rebellious people. Job wants his words inscribed permanently as testimony toward his vindication.

**Baseline.** Job 19 averages 1.48 exclusive pairs per verse. One pair would prove little. But a five-feature cluster in a single Isaiah verse, against a maximum of three anywhere else, is well above chance.

**Rival sources.** Hab 2:2–3 shares only כתב ("write") with 19:23. Deut 31:19–29 (writing in a book "as a witness", with אַחֲרִית הַיָּמִים "the latter days") is the Torah antecedent of Isa 30:8 itself. Within Job, compare 31:35.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Strong |
| Recurrence | Possible (Isa 44:6 in the next verse; see B6) |
| Thematic coherence | Strong |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Strong |

**Verdict.** Confirmed.
**Final rating.** Moderate–high (as proposed).
**Reasoning.** Three rare-to-moderate words are exclusive to the two verses, and the wider five-feature cluster has no rival above three. The Greek translator independently produced Isaiah's book + for-ever collocation. The rank adds nothing, but the verse-level case does not need it.
**What a preacher may safely say.** "Job's wish that his words be written in a book and inscribed for ever uses the very words of Isaiah 30:8, where the prophet writes his message down for a coming day."

##### (b) Jer 17:1

**Claim (as tested).** עֵט ("stylus") + בַּרְזֶל ("iron") occur only in Jer 17:1 and Job 19:24. Proposed rating: **moderate**.

**Evidence**
- [T] Verified: עֵט ("stylus") occurs in 4 verses (Jer 8:8; 17:1; Job 19:24; Ps 45:2). עֵט + בַּרְזֶל ("iron") occurs only in Jer 17:1 and Job 19:24, and both also have כתב ("write"): Jer 17:1 כְּתוּבָה ("written"), Job 19:23. But `excl_pairs('Job 19:24')` also returns two chance pairs, with Isa 51:1 (צוּר "rock" + חצב "hew") and Isa 26:4 (לָעַד "for ever" + צוּר "rock"). A single exclusive pair is cheap here.
- [T] BHS apparatus at Job 19:24: "prp וְצִפֹּרֶן" ("and a point") for MT וְעֹפָרֶת ("and lead"). The conjecture imports Jer 17:1's צִפֹּרֶן ("point"), so it must not be counted. MT and OG μολίβῳ ("lead") agree.
- [T] **Jer 17:1–4 is absent from the OG**: Rahlfs and Swete Jeremiah 17 both begin at v. 5. The link exists only in the Hebrew tradition.
- [I] Function is inverted: Judah's sin is indelibly engraved, Job's protest of innocence is engraved.

**Baseline.** Exclusive pair, with the shared כתב ("write") as a weak third item.
**Rival sources.** Isa 30:8 for the writing frame. Ps 45:2 and Jer 8:8 have עֵט ("pen") without iron.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible |
| Recurrence | Weak |
| Thematic coherence | Possible (inverse) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.
**Final rating.** Moderate (as proposed). The inversion reading is interpretive, and the link is Hebrew-only.
**Reasoning.** The pair is genuinely exclusive and concrete ("iron stylus"), and "write" joins it. But Job 19:24 throws up three exclusive pairs on its own, and the Greek reader of Jeremiah never met this line.
**What a preacher may safely say.** "Only here and in Jeremiah 17:1 does Scripture speak of an 'iron stylus': Jeremiah's records Judah's sin, Job wants his innocence carved in rock."

---

#### B6: The Redeemer — Isa 44:6 (with 49:26; 60:16) and Isa 26:19–21 behind Job 19:25 (and 14:12; 16:18)

##### (a) Isa 44:6 and 49:26

**Claim (as tested).** גֹּאֵל ("Redeemer") + אַחֲרוֹן ("last") occur only in Isa 44:6 and Job 19:25. גֹּאֵל + ידע ("know") + בָּשָׂר ("flesh") in one verse occurs only in Isa 49:26. Isa 44:4–8 ranks 2nd of 887. Proposed rating: **high (words); moderate (identity of the Redeemer)**.

**Evidence**
- [T] Verified: `co(['1350','314'])` returns Isa 44:6 and Job 19:25, an exclusive pair. Widening to ±1 verse adds **Ruth 3:9–10**: Ruth 3:10 הָאַחֲרוֹן ("the last [kindness]") beside the kinsman-redeemer, and Ruth 3:13 has גֹּאֵל ("redeem") + חַי ("as the LORD lives").
- [T] The function differs. Isa 44:6 אֲנִי רִאשׁוֹן וַאֲנִי אַחֲרוֹן ("I am the first and I am the last") is a divine self-predication, as in 41:4 and 48:12. In Isaiah, אַחֲרוֹן ("last") occurs only at 8:23, 30:8, 41:4, 44:6 and 48:12. Job 19:25 וְאַחֲרוֹן ("and at the last") is adverbial or predicative. The word is shared and the sense is related, not identical.
- [T] גֹּאֵל + ידע + בָּשָׂר in one verse is verified for Isa 49:26 only. Job spreads them over 19:25–26 and uses בָּשָׂר ("flesh") of his own body ("from my flesh I shall see God"), where Isa 49:26 uses it of humanity ("all flesh will know"). גֹּאֵל + ידע alone occurs in Isa 49:26, 60:16, 63:16, Job 19:25 and Ruth 4:4. Isaiah's recognition formula ("you will know that I, the LORD, am your Saviour and your Redeemer") meets Job's first-person "I know that my Redeemer lives". [I]
- [T] Rank. Isa 44:4–8 is **2nd (k=5, maxf 150; score 4, tied for 1st with Deut 32:12–16)** and 1st at maxf 400 (6). The null top-1 is 3.5 (range 2–5) at maxf 150 and 4 (range 4–6) at maxf 400. Isa 44's 6 equals the null maximum, but this target has more rare lemmas (19/25) than the null median (14/19), which inflates its scores. The extra shared lemmas have different functions: כתב ("write", 44:5), אֱלוֹהַּ ("God", 44:8) and צוּר ("Rock", 44:8). Isa 44 is not a hub.
- [T] Greek. Job 19:25 OG has ἀέναός ἐστιν ὁ ἐκλύειν με μέλλων ἐπὶ γῆς, with no "last". Isa 44:6 LXX has ὁ ῥυσάμενος … ἐγὼ μετὰ ταῦτα. There is no echo. Job 19:25 is not asterisked.

**Baseline.** Job 19 averages 1.48 exclusive pairs per verse. Job 19:25 has exactly one exclusive pair at maxf 400, and it is the Isa 44:6 pair. Its weight comes from the density of Isaiah material in Job 19:23–25 (Isa 30:8 in the verses just before) and from the rarity of "Redeemer" in Job (only here; Job 3:5 is a different verb).

**Rival sources.** Ruth 3:9–13 (the kinsman-redeemer narrative); Lam 3:58 גָּאַלְתָּ חַיָּי ("You have redeemed my life", with רִיב "plead my cause"), a legal-advocate rival; Ps 103:4.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible (exclusive pair; the senses differ) |
| Recurrence | Possible (Isa 49:26; 60:16 recognition formula) |
| Thematic coherence | Strong |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.
**Final rating.** Words **moderate–high**, not high. The identity of the Redeemer cannot be settled by this method; as a reading it stays moderate.
**Reasoning.** The verse-level pair is exclusive and sits next to the Isa 30:8 cluster, which makes deliberate contact plausible. But "last" works differently in the two texts, the "know … flesh" item is spread over two verses with different senses of "flesh", and the window rank is near the null's ceiling and re-counts the same lemmas.
**What a preacher may safely say.** "Job's 'my Redeemer … at the last' uses two words that stand together elsewhere only in Isaiah 44:6, where the Redeemer is the LORD who is 'the first and the last'."

##### (b) Isa 26:19–21

**Claim (as tested).** Isa 26:19–21 is the canonical answer to Job 14:12–14 and stands behind 19:25 and 16:18. חיה ("live") + קום ("rise") + עָפָר ("dust") in one verse occurs only in Isa 26:19 and Job 19:25. קיץ ("awake") + קום occurs only in Hab 2:7, Isa 26:19 and Job 14:12. Isa 26:21 is heard at Job 16:18. Proposed rating: **moderate (synthetic)**.

**Evidence**
- [T] חיה + קום + עָפָר holds **only at root level across a lemma split**: Isa 26:19 has the verb יִחְיוּ ("will live", 2421) and Job 19:25 has the adjective חַי ("lives", 2416). The subjects differ (the dead in Isaiah, the Redeemer in Job). קום + עָפָר alone occurs in 6 verses.
- [T] קיץ ("awake") + קום ("rise"): Hab 2:7, Isa 26:19, Job 14:12 (verified); Hab 2:7 (biters rising) is irrelevant. But **לֹא יָקִיצוּ ("they will not awake") occurs exactly only in Jer 51:39, 51:57 and Job 14:12**, and קיץ + שֵׁנָה ("sleep") only in Jer 31:26, 51:39, 51:57 and Job 14:12. Jer 51's "sleep a perpetual sleep and not wake" is the closer formal match for 14:12. Dan 12:2 (sleepers in the dust awaking to everlasting life) is the other text with קיץ + עָפָר.
- [T] Inside Job, 14:12 וְלֹא־יָקוּם ("and does not rise") → 19:25 יָקוּם ("he will take his stand") is a real echo. Exact ולא יקום ("and does not rise") also occurs at Isa 8:10, Job 8:15 and 15:29.
- [T] Isa 26:21 is Job 16:18's top verse partner (`partners`: דָּם "blood", כסה "cover", מָקוֹם "place"; 13.5). But אֶרֶץ ("earth") + כסה ("cover") + דָּם ("blood") also occurs in Ezek 24:7 and Hab 2:17. BHS cites Gen 4:10 at 16:18 (the cry of blood), and Ezek 24:7–8 (blood left uncovered to call for vengeance) is functionally close.
- [T] Greek. In Rahlfs, 14:12c (the sleep/waking colon) is **asterisked**. OG 14:12b reads "until the heaven be unstitched", so the קיץ ("awake") word is not represented. Conversely, OG 19:26 ἀναστήσαι τὸ δέρμα μου ("may he raise up my skin") and the OG appendix 42:17a ("it is written that he will rise again with those whom the Lord raises") use ἀνίστημι, as Isa 26:19 LXX does (ἀναστήσονται οἱ νεκροί). The Greek Job reads 19:25–26 as resurrection. This is reception data, not evidence of the Hebrew poet's design.

**Baseline.** Job 14:12 and 16:18 have one and zero exclusive pairs respectively at maxf 400. Each link is a three- or four-text item.
**Rival sources.** Jer 51:39, 57 (for 14:12); Dan 12:2; Ezek 24:7–8 and Gen 4:10 (for 16:18).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Weak (root-level only; spread across three Job passages) |
| Recurrence | Possible |
| Thematic coherence | Strong |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Needs reframing.
**Final rating.** Low–moderate (synthetic).
**Reasoning.** Every item is real at root level, but each has a rival as close or closer: Jeremiah 51 for "will not awake … sleep", Ezekiel 24 and Genesis 4 for uncovered blood. "Canonical answer" is a theological reading, not a demonstrable verbal design. The Greek Job does point in Isaiah's resurrection direction.
**What a preacher may safely say.** "Job asks whether a man who lies down will rise (14:12–14); Isaiah 26:19 uses the same words, 'rise', 'awake', 'dust', to promise that the dead will live. That is a canonical answer we may draw, not one Job quotes."

---

#### B7: Habakkuk's complaint (Hab 1:2–4; 2:2–3) behind Job 19:2, 7, 23

**Claim (as tested).** שׁוע ("cry for help") + חָמָס ("violence") occur only in Hab 1:2 and Job 19:7. "How long" (Hab 1:2 ~ Job 19:2), "no justice" (Hab 1:4 ~ 19:7) and "record the vision" (Hab 2:2–3 ~ 19:23) are added. Proposed rating: **moderate–high (words); shape moderate (synthetic)**.

**Evidence**
- [T] Verified: `co(['7768','2555'])` returns Hab 1:2 and Job 19:7, an exclusive pair in `excl_pairs('Job 19:7')`. The cry verb strengthens it across a by-form split: Hab 1:2 has אֶזְעַק ("I cry out"; זעק 2199) and Job 19:7 has אֶצְעַק ("I cry"; צעק 6817). With either form, the triad cry + "Violence!" + cry for help occurs only in these two verses. Jer 20:8 has אֶזְעָק חָמָס ("I cry out, 'Violence!'") without שׁוע ("cry for help").
- [T] Both describe an unanswered cry. Hab 1:2 has וְלֹא תִשְׁמָע … וְלֹא תוֹשִׁיעַ ("You will not hear … You do not save"); Job 19:7 has וְלֹא אֵעָנֶה … וְאֵין מִשְׁפָּט ("I get no answer … there is no justice").
- [T] "How long": עַד־אָנָה ("how long") occurs in 10 verses, including Bildad's Job 18:2. In 19:2 Job is answering Bildad's own question, so Habakkuk is not needed. Weak.
- [T] "No justice": וְאֵין מִשְׁפָּט ("and there is no justice") occurs exactly **only in Isa 59:8 and Job 19:7**. Hab 1:4 has a different phrase, וְלֹא־יֵצֵא לָנֶצַח מִשְׁפָּט ("justice is never upheld"). Isa 59:8 also has נְתִיבוֹת ("paths"), as Job 19:8 does.
- [T] Hab 2:2–3 shares only כתב ("write"; 212 verses) with Job 19:23. Isa 30:8 is far closer (see B5).
- [T] Rank. Hab 1 against Job 19:2–12 (k=11) is 25th (4), below Lam 3:1–11 at 14th (5). Against 19:6–8 (k=3, maxf 400), Lam 3:7–9 is 5th and Hab 1:1–3 39th.
- [T] Greek. OG Job 19:7 has ἰδοὺ γελῶ ὀνείδει … κεκράξομαι, καὶ οὐδαμοῦ κρίμα; it does not render חָמָס ("violence"). Swete Hab 1:2 has κράξομαι … βοήσομαι. κεκράξομαι occurs at Job 19:7 and Lam 3:8 (κεκράξομαι καὶ βοήσω), and in Psalms. ἕως τίνος occurs at Hab 1:2 and Job 19:2, among 18 verses.

**Baseline.** Job 19 averages 1.48 exclusive pairs per verse, and Job 19:7 has three (with Isa 33:7, Isa 58:9 and Hab 1:2). The Habakkuk pair stands out because the cognate cry verb joins it in the same verse and the function is identical.

**Rival sources**
- **Lam 3:7–9** for Job 19:7–8 (new). It has גדר ("wall up") + "and I cannot go out", then אֶזְעַק וַאֲשַׁוֵּעַ ("I cry out and call for help"; both first-person imperfects, as in Job), then נְתִיבוֹת ("paths"). גדר ("wall up") + נְתִיבָה ("path") occurs only in Hos 2:8, Isa 58:12, Job 19:8 and Lam 3:9.
- Isa 58:9 is the inverse: "you will cry for help (תְּשַׁוַּע) and He will say, 'Here I am'"; it is the top verse partner of 19:7. Ps 18:42 (a cry for help, no answer).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Strong (verse-level triad across a by-form split) |
| Recurrence | Weak (the other Habakkuk items fail) |
| Thematic coherence | Strong (an unanswered complaint about violence and justice) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.
**Final rating.** Words **moderate–high** (Hab 1:2 at Job 19:7). Shape **low–moderate**. Lam 3:7–9 is a co-witness for 19:7–8.
**Reasoning.** The single-verse match is strong and functional: cry, "Violence!", cry for help, no answer. But "how long" is answered inside Job, "no justice" is Isa 59:8's exact phrase rather than Habakkuk's, and Hab 2:2 shares one common word with 19:23. The complaint shape is better described as shared with Lamentations 3 as well.
**What a preacher may safely say.** "Job's 'I cry, Violence! but I get no answer; I shout for help' is almost word for word Habakkuk's complaint (Hab 1:2)."

---

#### B8: Isa 40:14 behind Job 21:22

**Claim (as tested).** Job 21:22 ("Can anyone teach God knowledge, in that He judges those on high?") speaks in the words of Isa 40:14, through למד ("teach") + דַּעַת ("knowledge") with God as the one who cannot be taught. Proposed rating: **moderate**.

**Evidence**
- [T] למד ("teach") + דַּעַת ("knowledge") occurs in 8 verses: Dan 1:4; Eccl 12:9; Isa 40:14; Job 21:22; Judg 3:2; Prov 30:3; Ps 94:10; 119:66. God as the one (not) taught, in a rhetorical question, occurs **only in Isa 40:14 and Job 21:22**. Ps 94:10 makes God the teacher.
- [T] The justice element survives a split. Isa 40:14 has בְּאֹרַח מִשְׁפָּט ("in the path of justice"; the noun, 4941) and Job 21:22 has יִשְׁפּוֹט ("He judges"; the verb, 8199). With the root שׁפט ("judge"), למד + דַּעַת + justice occurs only in these two verses.
- [T] למד ("teach") occurs **only once in Job** (21:22).
- [T] Job 21:22's exclusive pair at maxf 400 is (רום "high", שׁפט "judge") with Ps 75:8, a chance pair. Job 21 averages 1.03 such pairs per verse.
- [T] Greek. OG Job 21:22 has πότερον οὐχὶ ὁ κύριός ἐστιν ὁ διδάσκων σύνεσιν καὶ ἐπιστήμην; It turns the question into "God is the teacher", nearer Ps 94:10. Isa 40:14 LXX lacks διδάσκω. There is no echo, and the verse is not asterisked.

**Baseline.** Two words of moderate frequency, 8 verses together. The specificity comes from the rhetorical "who taught God?" and from justice being the third term.
**Rival sources.** Ps 94:10 (the inverse); Job 36:22–23 (Elihu: "Who is a teacher like Him? Who has appointed Him His way?"); Isa 40:13.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible |
| Recurrence | Possible (Isa 40 also proposed elsewhere in Job; not tested here) |
| Thematic coherence | Strong |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.
**Final rating.** Moderate (as proposed), with a low–moderate floor because the core words are common.
**Reasoning.** The contact is a rhetorical move ("who could teach God?") plus three words, one of which survives a noun/verb split. It is exclusive in that form. The words are common and Job's translator read the line the other way, so the link is a shared theological topos with a verbal edge rather than a quotation.
**What a preacher may safely say.** "Job's question, 'Can anyone teach God knowledge?', echoes Isaiah 40:14's 'who taught Him knowledge?' Both insist that God's justice is not learned from us."

---

### New candidates surfaced

1. **Lam 2:6–17 (with Lam 3:1–16, 30) at Job 16:6–17**. Proposed rating: **moderate–high.** It ranks 1st of 887 by a margin of 3 (9 against 6; null top-1 median 6, range 4–8; null gap 0–2), and is not a hub. Shared items:
   - חרק ("gnash") + שֵׁן ("teeth"): Lam 2:16 / Job 16:9.
   - שׁפך לָאָרֶץ ("poured out on the ground") with an organ: Lam 2:11 כְּבֵדִי ("my liver") / Job 16:13 מְרֵרָתִי ("my gall").
   - שַׂק ("sackcloth") + עָפָר ("dust"): an exclusive pair, Lam 2:10 / Job 16:15.
   - קֶרֶן ("horn") and חמל ("pity"): Lam 2:17.
   - מַטָּרָה ("target") with the bow: Lam 3:12 / Job 16:12; kidneys: Lam 3:13 / 16:13.
   - לְחִי ("cheek") + נכה ("strike") + חֶרְפָּה ("reproach"): exclusive, Lam 3:30 / Job 16:10. The Greek uses παίω + σιαγών in both.
   Direction is open: Lamentations follows Job in the canon.
2. **Isa 33:11–15 at Job 15:30–35** (moderate). It has הרה ("conceive") + ילד ("bring forth") + אֵשׁ ("fire") + אכל ("consume") + רוּחַ ("breath") (Isa 33:11), and חנף ("godless") + אֵשׁ ("fire") (33:14) with שֹׁחַד ("bribe") (33:15). חנף + שֹׁחַד within ±2 verses: only Isa 33:14 / Job 15:34. ἀσεβής + πῦρ in both Greek texts. Post hoc; Isa 33 is semi-hub, but the verse cluster carries the case.
3. **Isa 5:11–14 at Job 21:12–14** (moderate). כִּנּוֹר ("lyre") + תֹּף ("timbrel") within ±3 verses of Sheol only here; דַּעַת ("knowledge") refused (Isa 5:13 / Job 21:14). 1st of 887 against 21:7–16, at the top of the null range.
4. **Amos 2:9 at Job 18:16** (moderate). שֹׁרֶשׁ ("root") + מִמַּעַל ("above") + מִתַּחַת ("below") occur only in these two verses. Note that 18:16b is asterisked in the Greek.
5. **Lam 3:7–9 at Job 19:7–8** (moderate). Walled in, "I cry out and call for help" (first-person, as in Job), paths. גדר ("wall up") + נְתִיבָה ("path") occurs in only four verses.
6. **Jer 51:39, 57 at Job 14:12** (moderate). Exact לֹא יָקִיצוּ ("they will not awake") with שֵׁנָה ("sleep"); three texts.
7. **The surety formula of Proverbs at Job 17:3** (moderate). ערב ("be surety") + תקע ("strike hands") occurs only in Job 17:3 and Prov 6:1, 11:15, 17:18, 22:26.
8. **1 Chr 12:18 at Job 16:17** (low–moderate). The exact string לא חמס בכפי ("no violence in my hands") occurs only in these two verses.
9. **Isa 59:8 at Job 19:7** (low). Exact וְאֵין מִשְׁפָּט ("and there is no justice"), plus נְתִיבוֹת ("paths") as in 19:8.
10. **Isa 58:9 at Job 19:7** (low–moderate, as an inverse). שׁוע ("cry for help") + "Here I am" / "no answer"; it is the top verse partner.

### Key evidence for spot checks

1. `co(['2029','5999','3205','205'])` returns Isa 59:4, Job 15:35, Ps 7:15. `hub([('Isa',59)],19,10)` (my helper, which mirrors `base.rank` over 30 random Job passages) puts Isa 59 in the top three for 10 of 30 and first for 5. This decides B1.
2. `lem('5209')` and `lem('5220')` each return Gen 21:23, Isa 14:22, Job 18:19. `base.rank(span('Job',18,5,21),15)` gives "MARK rank 2 … 7 Isa 14:16-30"; the 14:9–23 window scores only 5. `chk_helpers.win(['8398','5209'],w=2)` returns Isa 14:21, Job 18:18.
3. `co(['7415','3680'])` returns Job 21:26, and `co(['7415','4374'])` returns Isa 14:11 (the lemma split). `co(['8596','3658'])` includes Isa 5:12 and Job 21:12, and these are the only two within ±3 verses of Sheol.
4. The exact consonants ערבני occur only in Isa 38:14 and Job 17:3. The BHS apparatus at 17:3 reads "ᵃ prp עֵרְבֹנִי". Job 17:16 reads בַּדֵּי שְׁאֹל ("bars of Sheol"), not "gates". `co(['6148','8628'])` returns Job 17:3 and Prov 6:1, 11:15, 17:18, 22:26.
5. The exact string 'על לא חמס' occurs in Isa 53:9 and Job 16:17; 'לא חמס בכפ' in Job 16:17 and 1 Chr 12:18. `co(['3895','5221','2781'])` returns Job 16:10 and Lam 3:30. `base.rank(span('Job',16,6,17),12)` gives "1 9 Lam 2:6-17", then 6.
6. `co(['3789','5612','2710'])` returns Isa 30:8 and Job 19:23. In Swete, `swre(r'βιβλι.*αιωνα|αιωνα.*βιβλι')` returns Isa 30:8 and Job 19:23 only.
7. `co(['5842','1270'])` returns Jer 17:1 and Job 19:24. Rahlfs and Swete Jeremiah 17 begin at v. 5. The BHS apparatus at 19:24 reads "ᵃ prp וְצִפֹּרֶן".
8. `co(['1350','314'])` returns Isa 44:6 and Job 19:25; `chk_helpers.win(['1350','314'],w=1)` adds Ruth 3:9. `base.rank(span('Job',19,23,27),5)` gives "MARK rank 2 … 4 Isa 44:4-8", tied with Deut 32:12–16, against a null top-1 median of 3.5.
9. The exact string 'לא יקיצו' occurs in Jer 51:39, 51:57 and Job 14:12. In Rahlfs, Job 14:12c (καὶ οὐκ ἐξυπνισθήσονται …) carries an asterisk.
10. `co(['7768','2555'])` returns Hab 1:2 and Job 19:7; `co(['2199','2555'])` returns Hab 1:2 and Jer 20:8; `co(['6817','2555'])` returns Job 19:7. The exact string 'ואין משפט' occurs only in Isa 59:8 and Job 19:7.

---

## Part C: Lamentations, the Psalter and Two Design Claims

### Auditor's note

**Corpus.** WLC Hebrew with its Strong's lemma index (observation layer); Swete LXX (all books); Rahlfs–Hanhart Job (Logos export, with hexaplaric asterisks); BHS Job text and apparatus (Logos export); NASB95 exports for Job, Lamentations, Psalms, Jeremiah, Deuteronomy and Habakkuk. No Rahlfs export exists for Lamentations, so Greek Lamentations is Swete only. Psalm references are WLC (Hebrew) numbering, with the English number in brackets; Swete Psalms use LXX numbering. **Swete Job 16 runs one verse ahead of the Hebrew** (Swete 16:13 = Hebrew 16:12), so Job Greek is cited by Rahlfs verse.

**Positive control.** `alib.lem('2617','Job')` returned Job 6:14, 10:12, 37:13, as it should. Before reporting absences I ran each search where a hit was known to exist. For example, `lem('5467','Lam')` returned Lam 4:6 before `lem('5467','Job')` returned nothing (Sodom). `ph('דבקה עצמי')` returned Job 19:20 as well as Ps 102:6. `co(['2555','7768'])` returned Job 19:7, the verse that prompted the search. `ph('חמרמר')` returned Job 16:16 even though the WLC leaves that word unpointed (ketiv).

**Method.** I verified every "only" by lemma (`co`, `lem`), then by exact consonants (`ph` on TX), and then by a ±1-verse window. I checked homograph letters. Job 16:16 חמרמרה ("is reddened, in ferment") is tagged 2560 c, while Lam 1:20 and 2:11 are tagged 2560 a, so `base.rank` does not count this link at all. Job 19:17 זָרָה ("is loathsome") is 2114 b, whereas Ps 69:9 and Job 19:13, 15 are 2114 a. I checked parallel texts: 2 Kgs 19:21 = Isa 37:22 for head-wagging.

**Window ranks** use `base.rank(target, k, maxf)` over 887 non-Job chapters. Each claim states its k and maxf.

**Nulls.** I drew random Job passages from chapters 4–14 and 22–31, using the same length and the same k:

| Null | Passages | Median top-1 | Top-1 range | Median gap, 1st to 5th | Gap 1st to 5th, max | Gap 1st to 2nd ≥ 2 |
|---|---|---|---|---|---|---|
| 15 verses, k=9, maxf 150 (for Job 19:6–20) | 72 | 6 | 4–9 | 1 | 2 | 2 of 54 (4%) |
| 8 verses, k=8, maxf 150 (for Job 16:9–16) | 72 | 4–5 | 3–7 | 1 | 3 | rare |
| 26 verses, k=12, maxf 150 (for Job 20:4–29) | 16* | 9 | 7–11 | 1 | 3 | — |

\*Only a few Job chapters reach 26 verses, so the 26-verse null repeats chapters.

**Exclusive-pair baselines** (brief): Job 1.34 per verse at maxf 400 (1.87 at 700).

**Purpose-built baselines.**
- C4: rare vocabulary shared by each Psalm with Job, and how often each chapter recurs in window ranks across 61 ten-verse Job passages.
- C5: counts of prologue elements in 17 "fate of the wicked" portraits, against 2,000 random windows per length.
- C6: shared rare vocabulary across all 120 pairs of the 16 speeches in Job 4–27, plus unions by round.

**Limits.** Lemma-level only; no syntax. Rahlfs is not available for Lamentations. History of interpretation was not checked. Selection effects are noted under each claim.

---

#### C1: Lamentations 2–3 as a live source in Job 16:9–16 and 19:2–27

**Claim (as tested).** Lamentations 3 (and 1–2) is a live source at Job 16:9–16 and 19:2–27. The claim cites exclusive word-pairs, a window over Lam 3:1–9 ranked 1st of 887 against Job 19:6–20, and an arc from Lam 3:36 to 3:58–59. Proposed: **high on words; moderate–high as a pattern**.

**Evidence**
- [T] מַטָּרָה ("target") and כִּלְיָה ("kidneys") fall in adjacent verses only at Job 16:12–13 and Lam 3:12–13 (WLC, ±1-verse window). Lemma 4307 also covers the "court of the guard" homograph (Jeremiah, Nehemiah). The "target" sense occurs only in 1 Sam 20:20, Job 16:12 and Lam 3:12. Greek: σκοπός ("target") stands in both Job 16:12 and Lam 3:12, and εἰς νεφρούς μου ("into my kidneys") echoes Lam 3:13's τοῖς νεφροῖς μου.
- [T] לְחִי ("cheek") and חֶרְפָּה ("reproach") co-occur only at Job 16:10 and Lam 3:30 (`co`, WLC). Both Greek texts use σιαγών ("jaw").
- [T] The reduplicated חמר ("be in ferment") occurs only at Job 16:16, Lam 1:20 and Lam 2:11 (`ph('חמרמר')`, WLC). BHS points Job 16:16 as חֳ֭מַרְמְרֻה ("is reddened"). **Verified.**
- [T] Gnashing of teeth, חרק ("gnash") with שֵׁן ("tooth"), is not exclusive: Job 16:9; Lam 2:16; Ps 35:16; 37:12; 112:10. שׁמם ("be desolate") occurs in 80 verses, which is too common to carry weight.
- [T] **The stronger Job 16 source is Lam 2, not Lam 3.** With k=8 and maxf 150, Lam 2:10–17 ranks 1st against Job 16:9–16 with 8 shared rare lemmas. The next window scores 4. Lam 3 ranks 37th. The eight lemmas are חמל ("spare"), חרק ("gnash"), שֵׁן ("tooth"), צַר ("adversary"), קֶרֶן ("horn"), עָפָר ("dust"), שַׂק ("sackcloth") and שׁפך ("pour"). Against 72 null passages the top-1 maximum was 7 and the largest 1st–5th gap was 3; Lam 2 scores 8 with a gap of 4. Widening the target to Job 16:4–16 keeps Lam 2 1st (9 against 6). The count omits חמרמר because of the homograph-letter split, so the true margin is slightly larger.
- [T] There is a phrase the claim missed: שׁפך ("pour out") + לָאָרֶץ ("to the ground") + a bodily organ occurs only at Job 16:13 ("He pours out my gall on the ground") and Lam 2:11 ("My heart [Heb. liver] is poured out on the earth"); Num 35:33 has the verb and noun with blood. Lam 2:11 is also a חמרמר verse. Greek: ἐξέχεαν εἰς τὴν γῆν (Job 16:13) and ἐξεχύθη εἰς τὴν γῆν (Lam 2:11), both "poured out on the ground". עָפָר ("dust") + שַׂק ("sackcloth") is an exclusive pair at Job 16:15 and Lam 2:10 (maxf 700).
- [T] Job 19:6–20 with k=9 and maxf 150: Lam 3:1–9 ranks **1st of 887 with 8 lemmas; the next window scores 6**. **Re-run confirmed.** It also ranks 1st at maxf 300 (10 against 8) and at k=15 (Lam 3:2–16, 9 against Lam 4's 8). The eight lemmas are עֶצֶם ("bone"), גדר ("wall up"), נְתִיבָה ("path"), נקף ("encompass"), שׁוע ("cry for help"), עוֹר ("skin"), חֹשֶׁךְ ("darkness") and הפך ("overturn"). Against the null, a top-1 of 8 or more came up in 15% of 54 Job passages, and a lead of 2 or more over 2nd place in 4%. Both together came up in about 2%. **Above chance, but in the upper tail rather than off the scale.** Against the whole of Job 19:2–27, Lam 3 drops to 8th.
- [T] גדר ("wall up") occurs in Job only at 19:8, and in Lamentations at 3:7 and 3:9 (verified). גדר + נְתִיבָה ("path") is **not** confined to these two: Hos 2:8 [Eng 2:6] and Isa 58:12 also have it. Hos 2:8 is a real rival: God walls in the way and she cannot find her paths. Lam 3:7–9 is still closer, because it is first-person, uses גדר twice, has "cannot go out" (Lam 3:7) beside "cannot pass" (Job 19:8), and darkness at Lam 3:2, 6.
- [T] נקף + עָלַי ("encompass me") occurs at Job 19:6; Lam 3:5; Ps 17:9; 88:18 [Eng 88:17]. Lam 3:5 is not exclusive.
- [T] **For Job 19:7 the better source is Hab 1:2–4.** חָמָס ("violence") + שׁוע ("cry for help") is an **exclusive pair** at Job 19:7 and Hab 1:2 (`co`). Hab 1:2 also has זעק ("cry out") and "You will not hear", and Hab 1:4 adds "justice (מִשְׁפָּט) is never upheld". Job 19:7 reads: "Behold, I cry, 'Violence!' but I get no answer; I shout for help, but there is no justice." Lam 3:8 shares זעק + שׁוע but has no חָמָס ("violence") and no מִשְׁפָּט ("justice"). Greek: κεκράξομαι ("I shall cry") is in both Job 19:7 and Lam 3:8, and κρίμα ("judgement") is in both Job 19:7 and Hab 1:4.
- [T] Skin, flesh and bone together occur at Job 10:11; 19:20; Lam 3:4; Mic 3:3, so the triad is common stock. יגה ("grieve") occurs in 8 verses, 5 of them in Lamentations; Job 19:2 has the friends as its subject.
- [I] On the arc: עות ("subvert") is in 10 verses. Job 19:6 ("God has wronged me", עִוְּתָנִי) answers Bildad's own Job 8:3 ("Does God pervert justice?", יְעַוֵּת) more directly than it answers Lam 3:36. Lam 3:58 גָּאַלְתָּ חַיָּי ("You have redeemed my life") and Job 19:25 גֹּאֲלִי חָי ("my Redeemer lives") share consonants, but the grammar differs, and גאל ("redeem") with חַי ("life, living") also occurs in Ps 103:4, Ruth and 2 Sam 14:11.
- [T] Rahlfs: no line on which the links rest is asterisked. The only asterisked lines nearby are Job 16:8b–c and 19:24, 28.

**Baseline.** Job 16 has 0.55 exclusive pairs per verse and Job 19 has 1.48. Across all of Job only 22 exclusive pairs (at maxf 700) point to Lamentations, and 2 of them fall in Job 16:10 and 16:15, slightly above the share these 51 verses would expect. The window nulls are tabulated above.

**Rival sources.** Lam 2:10–17 is a stronger match for Job 16 than Lam 3. Hab 1:2–4 is stronger for Job 19:7. Job 8:3 is stronger for the עות ("subvert") arc. Hos 2:8 is a weaker rival for גדר ("wall up").

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Possible (canonical order Job → Lam; direction open) |
| Volume | Strong (Job 16 with Lam 2–3); Possible (Job 19 with Lam 3) |
| Recurrence | Strong (Lam 1:20; 2:10–17; 3:1–13, 30 across Job 16 and 19) |
| Thematic coherence | Strong (God as assailant; besieged sufferer) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Strong for Job 16; Possible for the Job 19 arc |

**Verdict.** Confirmed with nuance.

**Final rating.** **High on words** at Job 16:9–16, where the centre of gravity is Lam 2:10–17 together with Lam 3:12–13, 30. **Moderate–high** for Lam 3:1–9 at Job 19:6–20. **Low** for the 3:36 / 3:58–59 arc. Job 19:7 should be reassigned to Hab 1:2.

**Reasoning.** Job 16 speaks in the words of Lamentations more densely than chance allows. The Lam 2 window beats every null passage, and three exclusive items cluster in it. Job 19's Lam 3 window is real but sits in the upper tail of chance. Two of its supporting items have better rivals (Hab 1:2; Job 8:3), and the target window was chosen after the event.

**What a preacher may safely say.** "In chapter 16 Job laments in the language of Lamentations: target, kidneys, cheek, gall poured on the ground. When he says God 'walled up my way' in chapter 19, he echoes Lamentations 3."

---

#### C2: Lamentations 4:3–14 behind Zophar's speech (Job 20)

**Claim (as tested).** A window over Lam 4:3–14 ranks 3rd of 887 against Job 20:4–29, supported by חֲרוֹן אַפּוֹ ("His burning anger"), רֶגַע ("moment") and Sodom. Proposed: **moderate**.

**Evidence**
- [T] With k=12 and maxf 150, Lam 4:3–14 ranks **3rd with 8 lemmas, tied with 1st and 2nd** (Jer 4:18–29; Hab 3:6–17). Four other windows score 7, including Num 24, Deut 32:22–33 and Lam 2:1–12. At maxf 300 it ranks 2nd (13, tied with Num 24). **Re-run confirmed.**
- [T] **The null kills it.** For 26-verse Job passages with the same k and maxf, the median top-1 score is **9** (range 7–11). Zophar's top window of 8 is below what an arbitrary Job passage of that length achieves. Lam 4 has no margin at all.
- [T] The eight shared lemmas are scattered and differ in function. Lam 4:4 has the infant's tongue (לָשׁוֹן) cleaving to the palate (חֵךְ) for thirst and the sucking child (ינק). Job 20:12–16 has evil kept under the tongue and in the palate, and the wicked man sucking poison. ינק ("suck") + לָשׁוֹן ("tongue") is an exclusive pair at maxf 700, but the images do not match.
- [T] חֲרוֹן אַף ("burning anger") occurs in 34 verses, including Lam 1:12, Exod 32:12 and Jer 4:8, 26. It does not distinguish anything.
- [T] רֶגַע ("moment") occurs in 22 verses, four of them in Job. Lam 4:6 joins it to הפך ("overthrow"). Job 20:5 (רֶגַע) and 20:14 (נֶהְפָּךְ, "is turned") lie nine verses apart, with different subjects.
- [T] **Sodom is absent from Job 20.** `lem('5467','Job')` returns nothing; the positive control `lem('5467','Lam')` returns Lam 4:6.
- [T] **Rival: Deut 32:32–33.** רֹאשׁ פְּתָנִים ("poison of cobras") is **exclusive** to Deut 32:33 and Job 20:16. מְרוֹרָה ("bitter thing, venom", 4846) occurs only in Deut 32:32 and Job 13:26; 20:14, 25. Deut 32:32 names **Sodom** and Gomorrah in the same breath: "their vine is from the vine of Sodom … their clusters, bitter". So the Sodom association near Job 20:14–16 comes through Deut 32, not Lam 4:6. Deut 32:22–33 scores 7 in the Job 20 rank.
- [T] Rahlfs: in Job 20, lines 9b, 11b, 12b, 13b, 14b, 20b–21a and 25c are asterisked. **The tongue/palate lines 20:12b–13b and the "venom of cobras" line 20:14b were absent from the Old Greek.** 20:23b's θυμὸν ὀργῆς ("wrath of anger") is Old Greek and matches Lam 4:11 (Swete), but that is a stock LXX phrase.
- [T] Exclusive pairs (maxf 700) from Job 20 to Lamentations: 20:14 → Lam 1:20 (הפך "turn" + מֵעִים "bowels" / קֶרֶב "inward part") and 20:16 → Lam 4:4. From Job 20 to Deuteronomy: 20:16 → Deut 32:33.

**Baseline.** Job 20 has 1.03 exclusive pairs per verse at maxf 400. The 26-verse window null is given above (median top-1 of 9).

**Rival sources.** Deut 32:32–33 (exclusive phrase, Sodom, venom). Jer 4:18–29 and Hab 3:6–17 tie with Lam 4 in the rank.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Possible |
| Volume | Weak |
| Recurrence | Weak |
| Thematic coherence | Possible (divine anger, sudden overthrow) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Weak |

**Verdict.** Discard (as a source-window claim).

**Final rating.** **Low.** The "Lamentations in the friends' voice" extension is not supported. Where the vocabulary does carry the Sodom and venom associations, it points to Deut 32:32–33.

**Reasoning.** A 3rd-place tie on a score below the null median is noise. The named contacts are either common (חֲרוֹן אַף, "burning anger") or split across verses (רֶגַע, "moment" / הפך, "overturn"), and Sodom is not in the Job text. The one striking cluster in Job 20:14–16 has a better, exclusive rival.

**What a preacher may safely say.** "Zophar's picture of the wicked man swallowing cobra venom echoes the Song of Moses (Deut 32:32–33)."

---

#### C3: Three lament psalms in Job 19 (Ps 88, Ps 102, Ps 69)

**Claim (as tested).**
- (a) Ps 88:9, 18–19 [Eng 88:8, 17–18] at Job 19:6–19; proposed **moderate–high**.
- (b) Ps 102:6 [Eng 102:5] at Job 19:20, with Ps 102:4 [Eng 102:3] at Job 30:30; proposed **high (words)**.
- (c) Ps 69:9 [Eng 69:8] at Job 19:13–17, with no distinctive pattern for the abandonment psalms as a set; proposed **moderate (phrase); no pattern**.

**Evidence: (a) Ps 88**
- [T] רחק ("remove far") + the consonants מידע ("acquaintance") in one verse occur only at Ps 88:9 and 88:19 (`co`, `ph`). With a ±1-verse window, only Ps 88 and Job 19:13–14 qualify: Job 19:13 has הִרְחִיק ("He has removed far") and 19:14 has מְיֻדָּעַי ("my intimate friends"). Job 19:13 itself has יֹדְעַי ("my acquaintances", Qal), not מְיֻדָּע, so **the claim's "Job 19:13" should read 19:13–14.** Ps 31:12 [Eng 31:11] and 55:14 also have מְיֻדָּע.
- [T] Job 19:13 reads: "He has removed my brothers far from me, And my acquaintances are completely estranged from me." Ps 88:9 [Eng 88:8] reads: "You have removed my acquaintances far from me; You have made me an object of loathing to them." In both, God is the agent. BHS app. 19:13ᵃ ("prb l c Ms G S קוּ—"; G and S are the sigla for the Greek and the Syriac) proposes the plural, and Rahlfs has the brothers as subject (ἀδελφοί μου ἀπέστησαν, "my brothers departed"). **The God-as-agent match is a feature of the MT only.**
- [T] נקף + עָלַי + יַחַד ("encompass me altogether") occurs only at Ps 88:18 [Eng 88:17]. Job splits it: 19:6 has נקף + עָלַי ("closed … around me"), and יַחַד + עָלַי ("together against me") occurs at 19:12 and 16:10, as well as Ps 31:14; 35:26; 41:8; Hos 11:8. This is weak. Greek: ἐκύκλωσάν με ("they surrounded me") occurs in both Ps 87:18 and Job 19:12.
- [T] Ps 88:9 has the noun תּוֹעֵבוֹת ("loathing"); Job 19:19 has the verb תעב ("abhor"), which occurs in 20 verses, four in Job. This is weak. Greek: βδέλυγμα ("abomination", Ps 87:9) sits beside ἐβδελύξαντο ("they abhorred", Job 19:19).
- [T] With k=9 and maxf 150, Ps 88:11–19 ranks **14th of 887 (top 1.6%)** against Job 19:6–20 with 5 lemmas. **Re-run confirmed.** But 5 is below the null's median top-1 (6), and every Job passage has some window in its top 2%. **This is not evidence.** The window also misses the best link, because ידע ("know") is too frequent for maxf.

**Evidence: (b) Ps 102**
- [T] דָּבְקָה עַצְמִי ("my bone clings") is **verbatim and only** at Job 19:20 and Ps 102:6 (`ph`). דבק ("cling") + עֶצֶם ("bone") + בָּשָׂר ("flesh") occurs only in these two (`co`). Job 19:20: "My bone clings to my skin and my flesh". Ps 102:6 [Eng 102:5]: "My bones cling to my flesh". **Verified.** BHS app. 19:20ᵃ proposes reading בעור־בשרי ("in the skin of my flesh"), which does not affect the phrase. The Greek does not echo: Ps 101:6 has ἐκολλήθη ("clung"), Job 19:20 has ἔχεται ("is held").
- [T] **Additional link:** אֲנָחָה ("sighing, groaning") + לֶחֶם ("bread") within one verse of each other occurs **only** at Job 3:24 and Ps 102:5–6 [Eng 102:4–5]. Ps 102:6 is the same verse used at Job 19:20. So two Job laments draw on one psalm verse. Ps 102:4–5: "I forget to eat my bread. Because of the loudness of my groaning…". Job 3:24: "For my groaning comes at the sight of my food".
- [T] עֶצֶם ("bone") + חרר ("burn") occurs in three verses: Ezek 24:10; Ps 102:4; Job 30:30. It is not exclusive. **There is a rival for Job 30:30:** Lam 4:8 has עוֹר ("skin") + עֶצֶם ("bone") + the root שׁחר ("black"). This contact is exclusive at the root level, but the Strong's numbers are split (7835 in Job 30:30, 7815 in Lam 4:8). Lam 4:8: "blacker than soot … Their skin is shriveled on their bones". Ps 102:1–12 against Job 30:16–31 ranks only 47th (k=12), while Lam 4 ranks 11th.

**Evidence: (c) Ps 69**
- [T] אָח ("brother") + זוּר ("be estranged") + נָכְרִי ("foreigner") in one verse occurs **only at Ps 69:9** (`co`, both homographs). Job spreads the three words: אַחַי ("my brothers") + זָרוּ ("are estranged") at 19:13, and לְזָר ("a stranger") + נָכְרִי הָיִיתִי ("I am a foreigner") at 19:15. The consonants נכרי הייתי ("I am a foreigner") occur only in Job 19:15 (`ph`). The Ps 69:9 structure לִבְנֵי אִמִּי ("to my mother's sons") is mirrored by לִבְנֵי בִטְנִי ("to my own brothers", literally "sons of my womb") at Job 19:17, but Job 19:17's זָרָה ("is loathsome") is the other homograph (2114 b).
- [T] נוד ("show sympathy") + נחם ("comfort") occurs at Isa 51:19; Nah 3:7; Ps 69:21 [Eng 69:20]; Job 2:11; 42:11. This is not distinctive, and Isa 51:19 and Nah 3:7 share Ps 69's "none to comfort" form.
- [T] Windows against Job 19:13–19 (k=7, maxf 150): Ps 69 ranks 89th, Ps 88 94th, Ps 31 17th. **Confirmed: there is no pattern.**

**Baseline.** Job 19 has 1.48 exclusive pairs per verse. Its exclusive pairs at maxf 700 point to Pss 13, 140, 58, 31, 119, 102 and 63, so a single exclusive pair with some psalm is routine. What lifts Ps 102 is a verbatim phrase reused twice.

**Rival sources.** For (a), Ps 31:12 [Eng 31:11] (מְיֻדָּע "acquaintance", reproach, neighbours). For (b) at Job 30:30, Lam 4:8. For (c) at 2:11, Isa 51:19 and Nah 3:7.

**Hays criteria**

| Criterion | (a) Ps 88 | (b) Ps 102 | (c) Ps 69 |
|---|---|---|---|
| Availability | Possible | Possible | Possible |
| Volume | Possible | Strong | Possible |
| Recurrence | Weak | Strong (Job 3:24; 19:20) | Weak |
| Thematic coherence | Strong | Strong | Strong |
| Historical plausibility | Possible | Possible | Possible |
| History of interpretation | Not checked | Not checked | Not checked |
| Satisfaction | Possible | Strong | Possible |

**Verdict.** (a) Confirmed with nuance. (b) Confirmed. (c) Confirmed (as modestly framed).

**Final rating.** (a) **Moderate**: one real two-verse contact (19:13–14 with Ps 88:9, 19), and the rest is weak. (b) **High (words)** at 19:20, and **moderate–high** for "Ps 102 is live in Job" (adding 3:24). The contact with Job 30:30 is **possible**, with Lam 4:8 as a rival. (c) **Moderate (phrase)**; **low** for the Job 2:11 / 42:11 contact.

**Reasoning.** Only Ps 102 offers verbatim, exclusive wording, and it does so twice in two Job laments. Ps 88 gives one MT-only, two-verse contact, and its top-2% rank is an artefact of ranking. Ps 69:9's three words are scattered across three Job verses.

**What a preacher may safely say.** "'My bone clings to my skin and my flesh' is the very wording of Psalm 102:5 [Eng], and Job 3:24 also echoes that psalm's groaning over bread. Job's lament about friends removed far from him resembles Psalm 88."

---

#### C4: Psalm 22 as a live source in Job (2:8; 3:11, 24; 16:4)

**Claim (as tested).** Four contacts show that Ps 22 is used repeatedly. Proposed: **moderate–high (synthetic)**. The test is whether the four together exceed chance.

**Evidence**
- [T] **Ps 22:2 [Eng 22:1] and Job 3:24.** שְׁאָגָה ("roaring, groaning") occurs in 7 verses, and with a first-person suffix in Ps 22:2, Ps 32:3 and Job 3:24. Ps 32:3 is an equal rival: "my body wasted away Through my groaning". Ps 102:5–6 [Eng 102:4–5] is a stronger rival, because it gives Job 3:24's other pair, אֲנָחָה ("sighing") + לֶחֶם ("bread"), exclusively (see C3b). Ps 22:15 [Eng 22:14], "poured out like water", resembles Job 3:24b ("pour out like water"), but the verbs differ: שׁפך ("pour") against נתך ("pour forth"). In the Old Greek, Ps 21:2 has παραπτωμάτων ("transgressions") and no "groaning", so the Greek offers no echo.
- [T] **Ps 22:11 [Eng 22:10] and Job 3:11.** רֶחֶם ("womb") + בֶּטֶן ("belly") occurs at Jer 1:5; Job 3:11; 31:15; Ps 22:11; 58:4. **Rival: Jer 20:18.** "Why did I ever come forth from the womb" is לָמָּה + רֶחֶם + יצא ("why" + "womb" + "come forth"), which is Job 3:11's own syntax: "Why did I not die at birth, Come forth from the womb". It sits in the cursing-of-birth genre that Job 3 belongs to. Ps 22:11 uses the womb as grounds for trust, which runs the opposite way to Job.
- [T] **Ps 22:16 [Eng 22:15] and Job 2:8.** חֶרֶשׂ ("potsherd") occurs in 16 verses. In Ps 22:16 it is a simile ("My strength is dried up like a potsherd"); in Job 2:8 it is an implement. Ps 22:16 has עָפָר ("dust"); Job 2:8 has אֵפֶר ("ashes"). חֶרֶשׂ + עָפָר together occur only at Ps 22:16 and Num 5:17. This is weak. The Greek ὄστρακον ("potsherd") is the standard rendering.
- [T] **Ps 22:8 [Eng 22:7] and Job 16:4.** נוע + רֹאשׁ ("shake the head") occurs in 6 verses: 2 Kgs 19:21 = Isa 37:22 (a parallel text), Lam 2:15, Ps 22:8, Ps 109:25 and Job 16:4. It is an idiom. **Lam 2:15–16 is the better-clustered rival:** head-shaking, then open mouths and gnashing of teeth, which reappear at Job 16:9–10, and Lam 2:10–17 ranks 1st against Job 16 (C1). In Job 16:4 Job is the one who would shake his head, hypothetically.
- [T] **Joint test 1: shared rare vocabulary.** Ps 22 shares 14 lemmas of frequency ≤ 20 with Job. The median for the 36 Psalms of 20–45 verses is 7. Ps 22 ranks **6th of 36**. Pss 55, 68, 69, 104 and 107 equal or exceed it. Counting verse pairs that share at least two rare lemmas (≤150) gives Ps 22 8, the median 3, and a rank of 7th of 36.
- [T] **Joint test 2: recurrence in window ranks.** Across 61 ten-verse Job passages (Job 3–31; k=10, maxf 150), Ps 22 enters a top 10 five times: Job 3:11–20, 19:11–20, 20:11–20, 30:1–10 and 30:11–20. That makes it the **23rd most recurrent chapter**, behind Isa 59, Deut 32 and Isa 5 (10–11 times each). The windows are always Ps 22:6–17, and the shared words are generic: bone, dust, pour, strength, encompass.
- [T] Rahlfs: no asterisk at Job 2:8, 3:11, 3:24 or 16:4.

**Baseline.** Four single-lemma or idiom contacts at frequency ≤ 20 are fewer than the seven such lemmas a median psalm of this length shares with Job. **Four contacts do not exceed chance as a count.** Their only claim to weight would be matching function, and each has either a rival with closer function (Jer 20:18; Ps 102:5–6; Lam 2:15) or an inverted function (womb as trust; potsherd as simile).

**Rival sources.** Jer 20:14–18 (Job 3:11). Ps 102:5–6 and Ps 32:3 (Job 3:24). Lam 2:15–16 (Job 16:4).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Possible |
| Volume | Weak |
| Recurrence | Possible (Ps 22:6–17 recurs in windows, generically) |
| Thematic coherence | Possible |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Weak |

**Verdict.** Needs reframing.

**Final rating.** **Low** for the four claimed contacts as a proof of use. **Low–moderate** for the weaker claim that Ps 22 belongs to the lament stock that Job's speeches share. It is above median, but no more distinctive than Pss 55, 69 or 107.

**Reasoning.** Each contact is either a common idiom or rare word with a closer rival, or a reversal of function, and together they fall short of what an average psalm of that length shares with Job. The Ps 22 resonance a reader feels is real at the level of genre, but the corpus does not single it out.

**What a preacher may safely say.** "Job's laments belong to the same world of complaint as Psalm 22, with its mockers, encircling enemies and bones laid bare. His curse on his birth is closest to Jeremiah 20, not to the psalm."

---

#### C5: The prologue's losses inside the friends' portraits (design claim)

**Claim (as tested).** The round-two portraits (Job 15:20–35; 18:5–21; 20:5–29) are built from Job's losses in the prologue: fire, sword, house and tent, survivor, children, skin, and בלע ("swallow"). Proposed: **links verified; design moderate (untested)**.

**Evidence**
- [T] **The links verify as vocabulary.**
  - Fire with אכל ("devour") links 1:16 to 15:34 and 20:26.
  - חֶרֶב ("sword") links 1:15, 17 to 15:22.
  - Tent and house appear at 15:28, 34; 18:6, 14–15; 20:19, 26, 28.
  - Children appear at 18:19 (נִין וָנֶכֶד, "offspring or posterity") and 20:10.
  - עוֹר ("skin") links 2:4 to 18:13.
  - בלע ("swallow") links 2:3 to 20:15, 18.
- [T] There is one correction. The prologue's escapee verb is מלט ("escape"): "I alone have escaped" (1:15–19). שָׂרִיד ("survivor", 18:19; 20:21, 26) is a different lemma. Zophar does use מלט at 20:20 (לֹא יְמַלֵּט, "He does not retain"), which is the closer verbal contact.
- [T] Greek data: 1:16 πῦρ … κατέφαγεν ("fire … devoured") matches 20:26 κατέδεται αὐτὸν πῦρ ("fire will devour him"). The prologue's σωθεὶς ἐγὼ μόνος ("I alone saved") matches 18:19 οὐδὲ σεσῳσμένος … ὁ οἶκος αὐτοῦ ("nor his house saved") and 20:20 οὐκ ἔστιν αὐτοῦ σωτηρία ("there is no safety for him"). 20:15 has ἄγγελος ("messenger") dragging the man from his house. Rahlfs asterisks: 18:15b (brimstone) and 22:20b (fire consumes the remnant) were absent from the Old Greek.
- [T] **Baseline A, using the claim's own 7 elements.**

| Portrait | Verses | Elements present (of 7) |
|---|---|---|
| Job 15:20–35 | 16 | 3 (fire, sword, house/tent) |
| Job 18:5–21 | 17 | 5 |
| Job 20:5–29 | 25 | 5 |
| Job 5:2–7 (Eliphaz r1) | 6 | 1 |
| Job 8:11–19 (Bildad r1) | 9 | 2 |
| Job 22:15–20 | 6 | 2 |
| **Job 27:13–23** | 11 | **4** |
| Ps 37 | 40 | 2 |
| Ps 73:3–20 | 18 | 1 |
| Ps 109:6–20 | 15 | 1 |
| Ps 49 | 21 | 2 |
| Prov 1:10–19 | 10 | 3 |
| Isa 14:4–21 | 18 | 3 |

  Random windows (2,000 per length, drawn from poetic Hebrew Bible books and from Job 3–41 outside the prologue and round two):
  - 16 verses with at least 3 elements: 12–24%.
  - 17 verses with at least 5: 0.4–0.9%.
  - 25 verses with at least 5: 1.6–1.8%.
  - 11 verses with at least 4: about 3%.

  So under this list, Job 18 and 20 are above chance, Job 15 is not, and **Job 27:13–23 is as dense as either.**
- [T] **Baseline B, using a list derived from the prologue rather than from the portraits.** This list has 10 elements: fire, sword, house/tent, escape, children/servants, skin, livestock, bone/flesh, boils, wind/storm. Round two scores 4, 5 and 5. The random-window probabilities become P(≥4 | 16 verses) ≈ 0.17, P(≥5 | 17 verses) ≈ 0.07–0.11 and P(≥5 | 25 verses) ≈ 0.15–0.17, all **within chance**. Job 27:13–23 again scores highest (5 in 11 verses).
- [I] **Selection effect.** Elements such as skin and בלע ("swallow") were put on the list because they appear in the portraits. When the list is built from the prologue alone, the signal disappears.

**Baseline.** Tabulated above. Round-one portraits are sparse (1–2 elements). Other Hebrew Bible portraits score 1–3. Job's own 27:13–23 is the densest.

**Rival sources.** The genre itself: the fate of the wicked in Job 27, Prov 1 and Isa 14 carries house, sword and children routinely. 18:15's brimstone on the dwelling points as much to Sodom (Gen 19:24) as to 1:16.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong (same book) |
| Volume | Possible |
| Recurrence | Possible (15, 18, 20; but also 27) |
| Thematic coherence | Strong (dramatic irony is apt) |
| Historical plausibility | Strong |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Needs reframing.

**Final rating.** **Links verified. The design is not demonstrated (low–moderate).** Bildad and Zophar are above chance only on a list that is itself post hoc. On an independent list they are ordinary, and Job 27 matches them.

**Reasoning.** The irony is plain to a reader, since the friends describe what has already happened to Job. But the vocabulary density does not show that the portraits were built from the prologue rather than from stock imagery. The finding is better stated as a reader-level resonance, strongest in 18:13, 18:19 and 20:26, than as a compositional design.

**What a preacher may safely say.** "The friends' portrait of the wicked man, with fire, the tent, no survivor, children gone and skin devoured, sounds uncomfortably like what we watched happen to Job in chapters 1–2. Whether or not they mean it, the reader hears it."

---

#### C6: Job 21 answers the friends clause by clause (design claim)

**Claim (as tested).** Job 21 is a point-by-point reply to the round-two portraits, supported by twelve verified links. A chance baseline is required. Proposed: **links verified; design moderate**.

**Evidence**
- [T] **Links checked, all WLC:**
  - פַּחַד ("dread") + שָׁלוֹם ("peace"): Jer 30:5; Job 15:21; 21:9; 25:2. Rare, but not exclusive.
  - The lamp: 21:17 נֵר רְשָׁעִים יִדְעָךְ ("the lamp of the wicked is put out") is **verbatim Prov 13:9 and Prov 24:20**, and 18:5–6 has אוֹר רְשָׁעִים יִדְעָךְ ("the light of the wicked goes out") and נֵרוֹ … יִדְעָךְ ("his lamp goes out"). Job is quoting the proverb that Bildad used. The Old Greek echoes it: λύχνος … σβεσθήσεται ("the lamp … will be quenched") in both 18:6 and 21:17.
  - שׁמם ("be appalled") + אחז ("seize") is in one verse only at 18:20. At 21:5–6 it is split across two verses.
  - 21:28 אֹהֶל מִשְׁכְּנוֹת רְשָׁעִים ("the tent, the dwelling places of the wicked") **conflates Bildad's 8:22 (אֹהֶל רְשָׁעִים, "tent of the wicked") and 18:21 (מִשְׁכְּנוֹת עַוָּל, "dwellings of the wicked")**, and it is introduced by כִּי תֹאמְרוּ ("For you say"). But **21:28b is asterisked in Rahlfs**, so the Old Greek lacked the line.
  - עַל עָפָר + שׁכב ("lie on the dust") occurs only at Job 7:21; 20:11; 21:26.
  - מתק ("be sweet") occurs at Exod 15:25; Job 20:12; 21:33; Prov 9:17; Ps 55:15. The Old Greek has γλυκαίνω ("make sweet") in both 20:12a and 21:33a, and both lines are Old Greek.
  - שָׁלֵו ("at ease") occurs in Job only at 16:12; 20:20; 21:23, but 21:23b is asterisked.
  - רֶגַע ("moment") links 20:5 and 21:13. צפן ("store up") links 15:20 and 21:19; 21:19 has no "You say" in the Hebrew, where NASB95 supplies it.
- [T] **Pointed answers the claim missed:**
  - The **opening**: 15:11 תַּנְחֻמוֹת ("consolations") against 21:2 תַּנְחוּמֹתֵיכֶם ("your consolation"). The noun occurs in 5 verses of the Hebrew Bible, 2 of them in Job. The Old Greek of 15:11 lacks it.
  - 21:7 גָּבְרוּ חָיִל ("become very powerful") combines 15:25 (גבר, "conduct himself arrogantly") with 15:29 (חַיִל, "wealth").
  - אֵיד ("calamity") links 18:12 to 21:17, 30.
  - אַיֵּה ("where?") links 15:23 to 21:28.
- [T] **Baseline: all 120 pairs of the 16 speeches in Job 4–27**, with each speech's opening formula verse dropped. "cos" means shared rare lemmas divided by √(size × size).

| Pair | Rank by HB-rare count (≤150) | Rank by HB-rare cos (≤150) | Rank by HB-rare cos (≤400) | Rank by Job-rare cos (≤6 Job verses) |
|---|---|---|---|---|
| 15 → 21 | 50 | 40 | 16 | 26 |
| 18 → 21 | 70 | 57 | 77 | 12 |
| 20 → 21 | 88 | 95 | 94 | 46 |
| 18 → 19 (control) | 86 | 73 | 78 | 68 |

  Zophar 20 is the speech with the most claimed links, yet it is the weakest pair, at or below the median.
- [T] **Union by round**: round two (15 + 18 + 20) set against each of Job's eight speeches.

| Metric | Job 21's place | Ahead of Job 21 |
|---|---|---|
| HB-rare cos, maxf 150 | 2nd | Job 12–14 (0.226 against 0.200) |
| HB-rare cos, maxf 400 | 3rd | Job 12–14; Job 26–27 |
| Job-rare cos (≤6 Job verses) | 1st (0.138) | Job 12–14 close behind at 0.132 |

  **The control undercuts the Job-rare result.** Round three (22 + 25) also puts Job 21 first on the Job-rare measure (0.137), and the single pair 21 ↔ 22 is the top friend–Job pair (0.121). Eliphaz 22:18 repeats 21:16 verbatim ("the counsel of the wicked is far from me"). Job 21 is lexically central both backwards and forwards. Its link to round two is above average but not saturated.

**Baseline.** Tabulated above. It agrees with the earlier finding that adjacent speech pairs are not saturated (18 → 19 ranks 68th–86th here).

**Rival sources.** Proverbs (13:9; 24:20) for the lamp. Job 7:21 for lying in the dust. Eliphaz 22 as the other partner of Job 21's vocabulary.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible (pairwise middling; union above average) |
| Recurrence | Strong (openings, closes, quotation formula) |
| Thematic coherence | Strong (prosperity of the wicked against their swift ruin) |
| Historical plausibility | Strong |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.

**Final rating.** **Links verified. Design moderate** as "pointed answers". **Not supported** as "clause by clause".

**Reasoning.** Job 21's overall vocabulary overlap with round two is not exceptional, and Zophar 20, the speech supposedly answered most closely, is the weakest pair. The case therefore rests on marked rejoinders: the opening (consolations), the quoted proverb about the lamp, "for you say" with a conflation of Bildad's two phrases, "lie in the dust", and "sweet". Several of these lines were absent from the Old Greek (21:23b, 21:28b), which is worth recording.

**What a preacher may safely say.** "Job 21 deliberately throws the friends' own lines back at them. 'How often is the lamp of the wicked put out?' quotes Bildad and the proverb he leaned on, and 'For you say, "Where is the tent of the wicked?"' cites them outright."

---

### New candidates surfaced

1. **Lam 2:10–17 in Job 16:4–16.** Window rank 1st (k=8, maxf 150): 8 against 4 for Job 16:9–16, and 9 against 6 for Job 16:4–16. This beats every one of 72 null passages, where the maximum was 7 and the largest gap 3. The exclusive items are שׁפך + לָאָרֶץ + organ ("poured on the ground", Job 16:13; Lam 2:11), עָפָר + שַׂק ("dust" + "sackcloth", Job 16:15; Lam 2:10) and חמרמר ("in ferment", Job 16:16; Lam 2:11). Lam 2:15–16 adds head-wagging, open mouths and gnashing teeth (Job 16:4, 9–10), and the Greek "poured out on the ground" matches. **Rating: high.**
2. **Hab 1:2–4 in Job 19:7.** חָמָס ("violence") + שׁוע ("cry for help") is exclusive (Hab 1:2; Job 19:7). The cry goes unheard or unanswered, and "no justice" (מִשְׁפָּט, Hab 1:4) appears; Greek κρίμα ("judgement") is in both. **Rating: moderate–high.**
3. **Ps 102:5–6 [Eng 102:4–5] in Job 3:24.** אֲנָחָה ("sighing") + לֶחֶם ("bread") within one verse of each other is exclusive. The same psalm verse feeds Job 19:20. **Rating: moderate–high.**
4. **Deut 32:32–33 in Job 20:14–16.** רֹאשׁ פְּתָנִים ("poison of cobras") is exclusive. מְרוֹרָה ("venom") occurs only in Deut 32:32 and Job. Sodom stands in Deut 32:32. **Rating: moderate–high.** It displaces C2.
5. **Lam 5:16 in Job 19:9.** עֲטֶרֶת רֹאשׁ ("crown of the head") with a verb of loss (סור "remove" / נפל "fall") occurs only in these two verses; the other eight verses with the phrase set a crown on a head. **Rating: possible (moderate).**
6. **Lam 4:8 in Job 30:30.** עוֹר ("skin") + עֶצֶם ("bone") + the root שׁחר ("black") occurs only here, across the Strong's split 7835/7815. **Rating: possible.** It is a rival to Ps 102:4.
7. **Within Job: 15:11 → 21:2** (תַּנְחוּמוֹת, "consolations": 5 Hebrew Bible verses, 2 in Job), and **8:3 → 19:6** (עות, "pervert, wrong": Job answers Bildad's question with his own verb). **Rating: moderate–high** as pointed answers.
8. **Job 20:14 → Lam 1:20.** הפך ("turn") + מֵעִים ("bowels") / קֶרֶב ("inward part") is an exclusive pair, but the function differs: food turning in the stomach against a heart overturned. **Rating: weak.**

### Key evidence for spot checks

1. `base.rank(base.span('Job',16,9,16), 8, maxf=150)` gives 1st place to Lam 2:10–17 with 8; the next windows score 4. In the null (72 eight-verse Job passages, k=8) the top-1 maximum is 7 and the 1st–5th gap maximum is 3.
2. `base.rank(base.span('Job',19,6,20), 9, maxf=150)` gives 1st place to Lam 3:1–9 with 8; the next scores 6. In the null (54 fifteen-verse passages) top-1 ≥ 8 occurs 15% of the time, a lead ≥ 2 occurs 4%, and both together about 2%.
3. `co(['2555','7768'])` returns ['Hab 1:2', 'Job 19:7'].
4. `base.rank(base.span('Job',20,4,29), 12, maxf=150)` gives Jer 4:18–29, Hab 3:6–17 and Lam 4:3–14 all with 8. The null median top-1 is 9 (range 7–11).
5. `co(['6620','7219'])` returns ['Deut 32:33', 'Job 20:16']. `lem('5467','Job')` returns [], and `lem('5467','Lam')` returns ['Lam 4:6'].
6. `ph('דבקה עצמי')` returns ['Job 19:20', 'Ps 102:6']. `lem('585')` within ±1 verse of `lem('3899')` gives only ['Job 3:24', 'Ps 102:6'].
7. `[r for r in V if 'מידע' in TX[r] and has(r,'7368')]` returns ['Ps 88:9', 'Ps 88:19']. On a ±1-verse window it adds Job 19:14 (רחק "remove far" is at 19:13). The Rahlfs and BHS apparatus at 19:13 read the plural, with the brothers as subject.
8. C4: Ps 22 shares 14 lemmas of frequency ≤ 20 with Job; the median for 20–45-verse psalms is 7, and Ps 22 ranks 6th of 36. Across 61 Job passages Ps 22 enters a top 10 five times and is the 23rd most recurrent chapter. `co(['7358','3318'])` includes Jer 20:18.
9. C5: claim list. Job 18:5–21 and 20:5–29 have 5 of 7 elements, with P(≥5) of 0.4–0.9% (17 verses) and about 2% (25 verses). Job 27:13–23 has 4 of 7 in 11 verses (about 3%). On the prologue-derived list of 10, round two's P is 0.07–0.17.
10. C6: of 120 speech pairs, 20 → 21 ranks 46th–95th. The round-two union puts Job 21 2nd, 3rd or 1st depending on metric, and the round-three union also puts Job 21 1st on the Job-rare measure. `ph('נר רשעים ידעך')` returns ['Job 21:17', 'Prov 13:9', 'Prov 24:20']. Rahlfs 21:23b and 21:28b are asterisked.

---

## Spot Checks

The main session re-ran the evidence on which each verdict turns. It used the same corpus, outside the auditors' sessions. **All 24 checks reproduced the auditors' results.** There is one note on method.

| # | Claim | Check (edition) | Result |
|---|---|---|---|
| 1 | all | Positive control: חֶסֶד in Job | 6:14; 10:12; 37:13 (WLC) — reproduced |
| 2 | A1 | עֵד + קום + ענה in one verse | Deut 19:16; Job 16:8 only (WLC) — reproduced |
| 3 | A1 | עֵד + חָמָס | Deut 19:16; Exod 23:1; Ps 27:12; Ps 35:11 — not Job 16:8 (WLC) — reproduced |
| 4 | A2 | חָמָס + יכח in one verse | 1 Chr 12:18 only (WLC) — reproduced |
| 5 | A3 | פֶּתֶן + רֹאשׁ | Deut 32:33; Job 20:16 only (WLC) — reproduced |
| 6 | A3 | מְרוֹרָה (4846) | Deut 32:32; Job 13:26; 20:14; 20:25 (WLC) — reproduced |
| 7 | A3 / C2 | Window rank against Job 20:4–29, k = 12 | Jer 4:18–29, Hab 3:6–17, Lam 4:3–14 tied at 8; Deut 32 not in the top three (WLC) — reproduced |
| 8 | A5 | עֲצַת רְשָׁעִים | Ps 1:1; Job 10:3; 21:16; 22:18 (WLC) — reproduced |
| 9 | A5 | קֶשֶׁת + נְחוּשָׁה | **2 Sam 22:35**; Job 20:24; Ps 18:35 — the parallel text breaks "only these two" (WLC) — reproduced |
| 10 | B1 | הרה + עָמָל + ילד + אָוֶן | Isa 59:4; Job 15:35; Ps 7:15 (WLC) — reproduced |
| 11 | B2 | נִין (5209) and נֶכֶד (5220) | Each Gen 21:23; Isa 14:22; Job 18:19 (WLC) — reproduced |
| 12 | B2 | Window rank against Job 18:5–21, k = 15 | 1st Isa 5:16–30 (8); 2nd Isa 14:16–30 (7) — the Isa 14 window is not the pericope 14:9–23 (WLC) — reproduced |
| 13 | B3 | ערבני, exact consonants | Isa 38:14; Job 17:3 only (WLC) — reproduced; see the note on method |
| 14 | B4 | עַל לֹא־חָמָס, exact | Isa 53:9; Job 16:17 only (WLC) — reproduced |
| 15 | B5 | כתב + סֵפֶר + חקק | Isa 30:8; Job 19:23 only (WLC) — reproduced |
| 16 | B5 | עֵט + בַּרְזֶל | Jer 17:1; Job 19:24 only (WLC) — reproduced |
| 17 | B6 | גֹּאֵל + אַחֲרוֹן | Isa 44:6; Job 19:25 only (WLC) — reproduced |
| 18 | B7 | שׁוע + חָמָס | Hab 1:2; Job 19:7 only (WLC) — reproduced |
| 19 | C1 | Window rank against Job 16:9–16, k = 8 | 1st Lam 2:10–17 (8); next windows 4 (WLC) — reproduced |
| 20 | C1 | Null for check 19: 24 random eight-verse Job passages (chapters 4–14, 22–31) | Top-1 scores 3–7 (median 4.5); 1st–5th gap 0–3. Lam 2:10–17's 8 with a gap of 4 exceeds every null passage — reproduced |
| 21 | C1 | Window rank against Job 19:6–20, k = 9 | 1st Lam 3:1–9 (8); next 6 (WLC) — reproduced |
| 22 | C2 | סְדֹם (5467) | In Job: none; in Lamentations: 4:6 (WLC; the control returned Lam 4:6) — reproduced |
| 23 | C3 | דבקה עצמי, exact | Ps 102:6; Job 19:20 only (WLC) — reproduced |
| 24 | C6 | נֵר רְשָׁעִים יִדְעָךְ | Prov 13:9; Prov 24:20; Job 21:17 (WLC) — reproduced |

**Note on method.** The helper's phrase search runs a second, *skeletal* pass, with waw, yod and final *he* removed, so that a defective spelling cannot hide a verse. On short words that pass over-matches. For check 13 it returned Gen 43:9 (אֶעֶרְבֶנּוּ, "I will be surety for him") as well. That form is a first-person singular imperfect with an object suffix, not the imperative "be surety for me". The exact consonants return only Isa 38:14 and Job 17:3, as auditor B reported. No verdict depends on a skeletal-only hit.

---

## Summary

### Verdict count

| Verdict | Count | Claims |
|---|---|---|
| Confirmed | 4 | A3 Deut 32 (#72; rank argument dropped); B5a Isa 30:8 (#63); C3b Ps 102 (#66); C3c Ps 69 (#67; as modestly framed) |
| Confirmed with nuance | 12 | A1a Deut 19 witness law (#60); A2 1 Chr 12:18 (#62); A5a Ps 1 (#74); B2 Isa 14 (#71); B3 Isa 38 form (#57; the Hezekiah frame needs reframing); B5b Jer 17:1 (#64); B6a Isa 44:6 (#70); B7 Habakkuk (#65); B8 Isa 40:14 (#78); C1 Lamentations (#58); C3a Ps 88 (#69); C6 Job 21 (#79) |
| Needs reframing | 8 | A1b the avenger of blood (#68); A4 Sodom (#76); A5b Ps 18:35 (#77); B1 Isa 59 (#56); B4 the Servant pattern (#61); B6b Isa 26:19–21 (#26); C4 Psalm 22 (#7); C5 the prologue's losses (#75) |
| Uncertain — flag for research | 0 | — |
| Discard | 1 | C2 Lamentations 4 behind Zophar (#73) |

**#59 (Bildad's reply picks up Job 16–17).** This item was baselined in the 19:1–29 dig (5 October). There, 16–17 → 18 ranked 99th and 18 → 19 ranked 75th of 120 speech pairs. Auditor C's independent speech-pair baseline for C6 used the same frame and agrees that pair-level overlap in this round is unremarkable. The 19 dig's ruling stands: **a pointed reply, moderate; no lexical design.** It is closed with this audit.

### Verdicts in brief

| # | Claim | Proposed | Verdict | Final rating | What a preacher may safely say |
|---|---|---|---|---|---|
| 60 | Deut 19:16–18 at 16:8 | moderate–high | Confirmed with nuance | **Moderate** (words; legal idiom shared with Ps 27:12; 35:11). Rahlfs 16:8b asterisked | "His wasted body is like a false witness rising against him — what Israel's law about false witnesses forbids." |
| 68 | The avenger of blood (Deut 19:6, 12; Ps 72:14) at 16:18; 19:25 | moderate (synthetic) | Needs reframing | **Weak** as a Deut 19 link; the partners of 16:18 are Gen 4:10 and Isa 26:21 | "When he asks the earth not to cover his blood, he echoes Abel's blood crying from the ground." |
| 62 | 1 Chr 12:18 at 16:17, 21 | moderate–high | Confirmed with nuance | **Moderate** — a shared oath-of-innocence formula (with Gen 31:42 behind Chronicles, and Isa 53:9 as close to 16:17) | "Job uses the same oath of innocence as David: no wrong in my hands; may God see and decide." |
| 72 | Deut 32:22–33 behind Zophar | moderate–high | Confirmed | **High (words)** for 20:14–17 ~ Deut 32:13–14, 32–33; moderate for fire, arrow and terror. Drop "5th of 887" | "Zophar borrows the Song of Moses: the poison of cobras, the vine of Sodom, the honey from the rock reversed." |
| 76 | Sodom (Gen 19:24; Ps 11:6) at 18:15; 20:23, 29; 1:16 | moderate | Needs reframing | **Low–moderate (motif).** 18:15 brimstone possible (Deut 29:22 as much as Gen 19:24); 20:23 → Ps 78:49 (major) and Ps 11:6 (minor); drop 1:16 (→ 2 Kgs 1:12) and 20:29 | "Bildad reaches for the vocabulary of Sodom-like judgement; Zophar's God 'rains' anger on the wicked as on Israel in the wilderness (Ps 78)." |
| 74 | Ps 1:1, 4 at 21:16, 18 | moderate–high | Confirmed with nuance | **Moderate**: high for עֲצַת רְשָׁעִים ("counsel of the wicked"), low for the chaff line alone (Ps 35:5; Isa 17:13) | "Job strings together the two-ways sayings — Psalm 1, Proverbs' lamp, the chaff — and asks how often they come true." |
| 77 | Ps 18:35 at 20:24 | moderate | Needs reframing | **Weak–possible**: also 2 Sam 22:35 (parallel text), and the function is opposite | — |
| 56 | Isa 59:1–10 behind Eliphaz | moderate–high (raised by the 15–21 dig) | Needs reframing | **Low–moderate**: a shared idiom (Isa 59:4; Ps 7:15) with Isa 33:11–15 an equal co-source for 15:34–35. The window rank is withdrawn: Isa 59 is in the top three for a third of arbitrary Job passages | "Eliphaz uses a stock phrase also found in Isaiah 59 and Psalm 7: the wicked 'conceive mischief and bring forth iniquity'." |
| 71 | Isa 14:9–23 behind Bildad; 21:12–13, 26, 32 | moderate–high | Confirmed with nuance | **Moderate** for Isa 14:21–22 at 18:17–19 and Isa 14:11 at 21:26. 21:12–13 → Isa 5:11–14 (moderate). Tomb contrast low. Rank dropped | "Bildad's wicked man, whose name and line are cut off, is described in the rare words of Isaiah's taunt over Babylon's king: 'offspring and posterity'." |
| 57 | Isa 38:10–18 at 16:19–17:16 | form high; frame moderate | Confirmed with nuance (form); frame needs reframing | Form **moderate** (MT-dependent; the natural form for asking a guarantor; Proverbs' surety idiom alongside). Hezekiah frame **low–moderate**; Job 17:16 has "bars", not "gates", of Sheol | "Job's 'be my surety' uses the same word as Hezekiah's sickbed prayer (Isa 38:14); both ask God himself to stand guarantor." |
| 61 | The Servant pattern at 16:10, 17 | moderate | Needs reframing | Phrase **low–moderate** (Isa 53:9); pattern **low**. Lam 3:30, not Isa 50:6, for the cheek | "Christians have heard Job's 'no violence in my hands' with the Servant who 'had done no violence' — but Job's words are closer still to Lamentations." |
| 63 | Isa 30:8 at 19:23–25 | moderate–high | Confirmed | **Moderate–high**; the Greek has Isaiah's book + for-ever collocation independently | "Job's wish that his words be written in a book for ever uses the very words of Isaiah 30:8." |
| 64 | Jer 17:1 at 19:24 | moderate | Confirmed with nuance | **Moderate**; Hebrew-only (the Greek Jeremiah lacks 17:1–4); the inversion is interpretive | "Only here and in Jeremiah 17:1 is there an 'iron stylus': Jeremiah's records Judah's sin; Job wants his innocence carved in rock." |
| 70 | Isa 44:6 (49:26; 60:16) at 19:25 | high (words); moderate (identity) | Confirmed with nuance | Words **moderate–high**; the identity of the Redeemer is a reading (moderate), not a result | "Job's 'my Redeemer … at the last' uses two words that stand together elsewhere only in Isaiah 44:6, where the Redeemer is the LORD, 'the first and the last'." |
| 26 | Isa 26:19–21 as the canonical answer to 14:12–14; 16:18; 19:25 | moderate | Needs reframing | **Low–moderate (synthetic)**: rivals Jer 51:39, 57 (14:12) and Gen 4:10; Ezek 24:7–8 (16:18) | "Isaiah 26:19 uses the same words — rise, awake, dust — to promise that the dead will live: a canonical answer we may draw, not one Job quotes." |
| 65 | Hab 1:2–4; 2:2–3 at 19:2, 7, 23 | moderate–high (words) | Confirmed with nuance | Words **moderate–high** (Hab 1:2 at 19:7); shape **low–moderate**; "no justice" is Isa 59:8's phrase; Lam 3:7–9 co-witness | "Job's 'I cry, Violence! but I get no answer' is almost word for word Habakkuk's complaint." |
| 78 | Isa 40:14 at 21:22 | moderate | Confirmed with nuance | **Moderate** (low–moderate floor: common words; a shared topos) | "Job's 'Can anyone teach God knowledge?' echoes Isaiah's 'who taught Him knowledge?'" |
| 58 | Lamentations 2–3 at 16:9–16 and 19:2–27 | high (words); moderate–high (pattern) | Confirmed with nuance | **High** at Job 16, but the main source is **Lam 2:10–17** (with Lam 3:12–13, 30). **Moderate–high** for Lam 3:1–9 at 19:6–20 (post hoc; upper tail of chance, about 2%). The Lam 3:36, 58–59 arc **low**. 19:7 → Hab 1:2; 19:6 answers Bildad's 8:3 | "In chapter 16 Job laments in the language of Lamentations; when he says God 'walled up my way' (19:8), he echoes Lamentations 3." |
| 73 | Lam 4:3–14 behind Zophar | moderate | **Discard** | **Low**: a tie at 8 against a null median of 9; Sodom is not in Job 20; the better source is Deut 32:32–33 | — |
| 69 | Ps 88 at 19:6–19 (overview row to be raised) | moderate–high | Confirmed with nuance | **Moderate** — not raised. One MT-only, two-verse contact (19:13–14); the top-2% rank is an artefact | "Job's lament about friends removed far from him resembles Psalm 88." |
| 66 | Ps 102:6 at 19:20 (with 102:4 at 30:30) | high (words) | Confirmed | **High (words)**; with a new exclusive contact at 3:24 (Ps 102:5–6), "Ps 102 is live in Job" is **moderate–high**. 30:30 possible (rival Lam 4:8) | "'My bone clings to my skin and my flesh' is the very wording of Psalm 102:5 [Eng]." |
| 67 | Ps 69:9 at 19:13–17; 69:21 at 2:11; 42:11 | moderate (phrase); no pattern | Confirmed | **Moderate (phrase)**; 2:11 / 42:11 **low**; no pattern across the abandonment psalms | — |
| 7 | Psalm 22 as a live source (2:8; 3:11, 24; 16:4) | moderate–high (synthetic) | Needs reframing | **Low**: Ps 22 is 6th of 36 comparable psalms; each contact has a closer rival (Jer 20:18; Ps 102:5–6; Ps 32:3; Lam 2:15) | "Job's laments belong to the same world of complaint as Psalm 22; his curse on his birth is closest to Jeremiah 20." |
| 75 | The prologue's losses in the friends' portraits (design) | links verified; design moderate (untested) | Needs reframing | **Links verified; design not demonstrated.** Above chance only on the claim's own list; within chance on a prologue-derived list; Job 27:13–23 is as dense. A reader-level resonance, strongest at 18:13, 18:19 and 20:26 | "The friends' portrait sounds uncomfortably like what we watched happen to Job in chapters 1–2. Whether or not they mean it, the reader hears it." |
| 79 | Job 21 answers the friends clause by clause (design) | links verified; design moderate | Confirmed with nuance | **Pointed answers, moderate**; not "clause by clause". 20 → 21 ranks 46th–95th of 120 pairs; round two taken together puts 21 near the top, but round three does too. The case rests on 15:11 → 21:2, the lamp proverb, "for you say", the dust and the sweetness | "Job 21 throws the friends' own lines back at them: 'How often is the lamp of the wicked put out?'" |

### The finding all three auditors reached independently

**Lamentations 2:6–17 behind Job 16:4–18.** Each auditor raised it, blind to the other two. Auditor A found it from the witness-law rival search, B from the Servant pattern's, and C from the Lamentations claim. It is the strongest source result in the round:

- **Window rank.** The window ranks 1st of 887 against Job 16, by 8 or 9 shared rare lemmas against 4–6 for the next. It beats every one of 72 arbitrary Job passages of the same length (null maximum 7; largest gap 3); spot checks 19–20 reproduce this.
- **Exclusive items.**
  - שׁפך + לָאָרֶץ + a bodily organ ("poured out on the ground"): Lam 2:11 כְּבֵדִי ("my liver"); Job 16:13 מְרֵרָתִי ("my gall").
  - עָפָר + שַׂק ("dust" + "sackcloth"): Lam 2:10; Job 16:15.
  - The reduplicated חמרמר ("in ferment"): Lam 1:20; 2:11; Job 16:16. The lemma index files Job's form under a different homograph letter, so the ranker under-counts it.
- **Lam 2:15–16 in Job 16:4, 9–10.** Head-shaking, open mouths and gnashing teeth (חרק + שֵׁן). The Greek has ἔβρυξαν … ὀδόντας ("gnashed teeth") in both.
- **Lam 3:12–13, 30 complete it:** target and kidneys (16:12–13); cheek struck in reproach (16:10).

**Rating: high (words).** Lamentations stands after Job in the Ketuvim, so the direction of dependence is open. It replaces Isa 50:6 (#61) and Ps 22:8 (#7) as the partner for the assault language of 16:4–16. It is recorded as **confirmed by audit 3** rather than queued.

### What the audit changes, in one paragraph

**The source claims split cleanly by how they were found.**

- **What survives.** The claims that stand on exclusive, verbatim and clustered wording in one or two verses all survive:
  - Deut 32:32–33;
  - Isa 30:8;
  - Ps 102:6;
  - Hab 1:2;
  - Isa 44:6;
  - Isa 14:22;
  - Lam 2 at Job 16.
- **What falls.** The claims that rested on a window rank fall: Isa 59, Lam 4, the Isa 14 rank, the Deut 32 rank and Ps 88's top 2%. The null shows that the top windows of arbitrary Job passages score just as high. **The window-rank argument is withdrawn as evidence for any source in this round**, except where a source beats the null by a clear margin (Lam 2 at Job 16; Lam 3:1–9 at Job 19, in the upper tail).
- **The two design claims shrink** to what a reader hears (#75) and to marked rejoinders (#79).
- **The two Christological frames** (the Servant, #61; Isa 26 as canonical answer, #26) stand as **canonical reflection, not demonstrated design**, which is how the backbone may use them.

### Confidence Change Propagation

The book overview (v0.1.1) has not yet received the Sermon 4 rows. The 15–21 dig proposed them as Book-Overview Tensions. The table shows what each proposed or existing row should carry.

| Allusion | Previous (proposed) confidence | New confidence | Sections to update |
|---|---|---|---|
| Lam 2:10–17 (with 3:12–13, 30) at 16:4–16 | — (Lam 2–3 as #58) | **High (words)** | Intertextual Map (Lamentations row, now live at 16 and 19); Echo Table N/A; 16–17 dig Headline 3 |
| Lam 3:1–9 at 19:6–20 | high pattern / ranked 1st | **Moderate–high** (post hoc; upper tail) | Intertextual Map; 19 dig Headline 4 |
| Lam 3:36, 58–59 arc at 19:6, 25–27 | moderate–high | **Low** | 19 dig Headline 4 |
| Lam 4:3–14 at 20 | moderate | **Discard** | 15–21 dig Headline 5; drop the proposed overview row; drop "Lamentations live in both voices" |
| Deut 32:13–14, 32–33 at 20:14–17 | moderate–high | **High (words)** | Intertextual Map (Deut 32 live source: 5:18; 10:7; 20:14–17); 15–21 dig Headline 5 (drop "5th of 887") |
| Isa 59:1–10 at 15:17–35 | moderate–high (raised) | **Low–moderate (idiom)**; Isa 33:11–15 co-source | 15–21 dig Headline 5; queue #56 reverts |
| Isa 14:21–22 at 18:17–19; 14:11 at 21:26 | moderate–high | **Moderate** | Intertextual Map; 15–21 dig Headline 5 (drop rank) |
| Isa 5:11–14 at 21:12–14 | — | **Moderate (new)** | Intertextual Map; 15–21 dig Tool 11 (replaces Isa 14 at 21:12–13) |
| Ps 1:1 at 21:16 | moderate–high | **Moderate** (high for the phrase) | Intertextual Map; 15–21 dig |
| Ps 18:35 at 20:24 | moderate | **Weak–possible** (two words; opposite function) | 15–21 dig Headline 5 and Tool 11 (the dig already listed 2 Sam 22:35; the queue's summary did not) |
| Ps 11:6 / Gen 19:24 (Sodom) | moderate | **Low–moderate (motif)**; 1:16 → 2 Kgs 1:12; 20:23 → Ps 78:49 | 15–21 dig Headline 2 and 5; Echo Table (1:16) |
| Isa 40:14 at 21:22 | moderate | **Moderate** (unchanged) | — |
| Isa 38:14 at 17:3 | high (form) | **Moderate (form)**; frame **low–moderate** | 16–17 dig Headline 4 |
| Deut 19:16 at 16:8 | moderate–high | **Moderate** | 16–17 dig Headline 1 |
| 1 Chr 12:18 at 16:17, 21 | moderate–high | **Moderate** (shared formula) | 16–17 dig |
| The Servant at 16:10, 17 | moderate | **Low** (pattern); Isa 53:9 phrase low–moderate | 16–17 dig Christological Reading; Christological trajectory |
| Isa 30:8 at 19:23 | moderate–high | **Moderate–high** (confirmed) | — |
| Jer 17:1 at 19:24 | moderate | **Moderate** (confirmed) | — |
| Isa 44:6 at 19:25 | high (words) | **Moderate–high (words)**; identity moderate (reading) | 19 dig Headline 2; Christological trajectory |
| Isa 26:19–21 at 14:12; 16:18; 19:25 | moderate | **Low–moderate (synthetic)** | 19 dig Headline 2; Christological trajectory |
| The avenger of blood (Deut 19:6, 12; Ps 72:14) | moderate (synthetic) | **Weak** | 19 dig |
| Hab 1:2 at 19:7 | moderate–high | **Moderate–high** (words); shape low–moderate | Intertextual Map |
| Ps 88 at 19:6–19 | moderate (row to be raised) | **Moderate — do not raise** | Intertextual Map (keep the row at moderate) |
| Ps 102:6 at 19:20 (with 102:5–6 at 3:24) | high (words) | **High (words)**; Ps 102 live, moderate–high | Intertextual Map (new row) |
| Ps 69:9 at 19:13–17 | moderate | **Moderate** (unchanged) | — |
| Ps 22 as a live source | moderate–high (synthetic) | **Low** | Intertextual Map (Ps 22 row); Job 3 and 16–17 digs |
| Prologue losses in the portraits (#75) | design moderate | **Reader-level resonance; design not shown** | 15–21 dig Headline 2; Echo Table rows 1:16 → 15:34; 20:26 kept as echoes, not design |
| Job 21 as reply (#79) | design moderate | **Pointed answers, moderate** | 15–21 dig Headline 4 |

### Recommended book-overview revisions

1. **Intertextual Map.** Add or adjust the Sermon 4 rows as in the table above.
   - **Lamentations** becomes a live source at Job 16 (high) and 19 (moderate–high), and is no longer claimed in the friends' voice.
   - **The Song of Moses** is live in both voices: Deut 32:39 at 5:18 and 10:7 (audit 2), and Deut 32:32–33 at 20:14–16 (high).
   - **Ps 102** is live at 3:24 and 19:20.
   - **Ps 22** drops to low.
   - **Ps 88** stays at moderate.
2. **A method note in the colophon.** Window ranks are not evidence for a source unless they beat a Job-passage null; the null medians are recorded in this audit (eight-verse windows: top-1 median about 4–5; twelve- to fifteen-verse: about 6; 26-verse: 9).
3. **Christological trajectory.** Keep 16:19 → 17:3 → 19:25 as the Job-internal line. Present Isa 44:6 (moderate–high words), Isa 53:9 (low–moderate) and Isa 26:19 (low–moderate) as **canonical reflection a reader may draw**, not as allusions Job makes.
4. **Echo Table.** Keep 1:16 → 15:34; 20:26 (fire) and 1:15–19 → 18:19; 20:21, 26 (survivor) as echoes the reader hears, flagged as reader-level, not design. Add 8:3 → 19:6 (עות, "pervert, wrong"), 15:11 → 21:2 (consolations) and 18:5–6 → 21:17 (the lamp), all moderate–high as pointed answers.

### Recommended dig revisions

**16:1–17:16 (Sermon 4 solo dig).**

- **Headline 1:** Deut 19:16 is **moderate**, a legal idiom shared with Ps 27:12; 35:11. Note that Rahlfs asterisks 16:8b.
- **Headline 3:** re-attribute the main source to **Lam 2:10–17** (high), with Lam 3:12–13, 30 completing it.
- **Headline 4:** the surety form is **moderate**; the Hezekiah frame is **low–moderate**. Correct "gates of Sheol" to "bars of Sheol" (17:16 בַּדֵּי שְׁאֹל) wherever the frame cites Isa 38:10.
- **1 Chr 12:18:** moderate, as a shared formula (with Gen 31:42; Isa 53:9 equally close at 16:17).
- **Christological Reading:** the Servant pattern is low; keep it as canonical reflection.
- **Ps 22:8 at 16:4:** add Lam 2:15 as the closer partner.

**19:1–29 (Sermon 4 solo dig).**

- **Headline 2:**
  - Isa 44:6 is moderate–high on words, and the Redeemer's identity is a reading;
  - Isa 26:19 is low–moderate (synthetic);
  - drop the avenger-of-blood thread (weak).
- **Headline 3:** Isa 30:8 is confirmed at moderate–high and Jer 17:1 at moderate. Note that the Greek Jeremiah lacks 17:1.
- **Headline 4:**
  - Lam 3:1–9 is moderate–high (post hoc; upper tail of chance);
  - the Lam 3:36, 58–59 arc is low;
  - assign 19:7 to Hab 1:2 (moderate–high);
  - add 8:3 → 19:6 (Job answers Bildad's verb);
  - add Lam 5:16 at 19:9 (possible).
- **Ps 88:** moderate (do not raise). **Ps 102:** high, with 3:24.

**15:1–21:34 (consolidation dig).**

- **Headline 2:** restate as a reader-level resonance, not a design:
  - drop 1:16 ~ Gen 19:24 (→ 2 Kgs 1:12);
  - drop 20:29 ~ Ps 11:6 (חֵלֶק is not מְנָת, "portion");
  - read 20:23 with Ps 78:49.
- **Headline 4:** "pointed answers", not "clause by clause"; Zophar 20 → 21 is the weakest pair.
- **Headline 5:**
  - withdraw every window rank;
  - Isa 59 is low–moderate (idiom), with Isa 33:11–15;
  - Isa 14 is moderate (14:21–22; 14:11), with 21:12–13 → Isa 5:11–14;
  - Deut 32:32–33 is **high** (words);
  - discard Lam 4;
  - Ps 18:35 is weak–possible (two words, opposite function; the dig had already listed 2 Sam 22:35);
  - drop "Lamentations is live in both voices".
- **Convergent Findings:** "Both sides draw on the same Scripture" stands only for the Song of Moses (Deut 32:39 / 32:32–33) and, more loosely, Isaiah. Lamentations is Job's alone.

### New links surfaced by the audit

**Confirmed and not queued:**

- **Lam 2:10–17 at Job 16:4–16** — high; reached by all three auditors (above).

**Queued for a later audit** (numbered in the queue as #80–#90):

| Queue | Link | Evidence | Rating |
|---|---|---|---|
| 80 | Isa 33:11–15 at 15:30–35 | הרה + ילד + אֵשׁ + אכל + רוּחַ (33:11); חנף + שֹׁחַד within ±2 verses only Isa 33:14 / Job 15:34; ἀσεβής + πῦρ in both Greek texts | moderate (post hoc) |
| 81 | Isa 5:11–14 at 21:12–14 | כִּנּוֹר + תֹּף within ±3 verses of Sheol only here; knowledge refused (Isa 5:13 / 21:14); 1st of 887 against 21:7–16, at the top of the null range | moderate |
| 82 | Amos 2:9 at 18:16 | שֹׁרֶשׁ + מִמַּעַל + מִתַּחַת only these two verses; 18:16b asterisked in Rahlfs | moderate |
| 83 | The Proverbs surety formula at 17:3 | ערב + תקע only Job 17:3; Prov 6:1; 11:15; 17:18; 22:26 | moderate |
| 84 | Ps 78:49 (with 78:24–31) at 20:23 | יְשַׁלַּח־ב־ חֲרוֹן אַפּוֹ exact only Ps 78:49 / Job 20:23; God "rains" food and strikes "while their food was in their mouths" | moderate–high |
| 85 | 2 Kgs 1:12 at 1:16 | אֵשׁ אֱלֹהִים exact only these two, with "from heaven" and "consume"; the Old Greek of Job 1:16 matches 1 Kgs 18:38 | moderate–high |
| 86 | Gen 31:37–42 at 9:33; 16:21 (and behind 1 Chr 12:18) | יְגִיעַ כַּפַּי (also 10:3); "saw … and decided"; יכח + בֵּין (Gen 31:37; Isa 2:4; Mic 4:3; Job 9:33) | possible–moderate |
| 87 | Ps 102:5–6 at 3:24 | אֲנָחָה + לֶחֶם within one verse exclusive; the same psalm verse feeds 19:20 | moderate–high |
| 88 | Lam 5:16 at 19:9 | עֲטֶרֶת רֹאשׁ with a verb of loss only these two | possible (moderate) |
| 89 | Lam 4:8 at 30:30 | עוֹר + עֶצֶם + שׁחר across the 7835/7815 split | possible |
| 90 | Isa 59:8; 58:9 at 19:7 | וְאֵין מִשְׁפָּט exact only Isa 59:8 / Job 19:7; שׁוע with "no answer" inverting Isa 58:9 | low–moderate |

**Not queued** — verified lexical chains: 8:3 → 19:6 (עות); 15:11 → 21:2 (תַּנְחוּמִים / תַּנְחוּמוֹת); 18:5–6 → 21:17. These go to the Echo Table.

---

## Critical Assessment

1. **History of interpretation was not checked.** Every Hays table records it as *not checked*. Patrick's Logos rounds have already supplied some evidence:
   - Delitzsch on 16:20 with Isa 38:14 (round 4), relevant to #57;
   - Davison (HDB) listing Isa 59:4 ~ 15:35 (round 2), relevant to #56;
   - BHS's own "cf Gn 4,10" at 16:18.

   None of these reverses a verdict. Davison's listing confirms that #56 is a known parallel, not that it is a source. A Logos round on the links now rated high or moderate–high is the obvious next check before they enter the overview: Lam 2 at Job 16; Deut 32:32–33 at Job 20; Isa 30:8; Ps 102:6; Hab 1:2; Ps 78:49; 2 Kgs 1:12.
2. **The auditors shared one helper library.** Their searches are independent, but a fault in `alib` or `base` would be common to all three. The spot checks used the same library. Exact-consonant checks outside it (checks 13, 23 and the Hebrew gate) reduce this risk but do not remove it.
3. **The null is a Job-passage null.** It measures what a Job passage scores against the canon. It does not measure what a non-Job passage would score. That is the right question for "is this source above chance for this passage?" It is not a test of whether Job as a book is unusually allusive.
4. **Selection effects remain.** Lam 2 at Job 16 was found post hoc by every auditor. The null answers the question of chance, but not the question of choice. It is still the strongest result in the round because three blind routes reached it.
5. **MT-only links.** Several surviving links depend on the Masoretic consonants or pointing (the surety imperative at 17:3; Ps 88 at 19:13–14; Jer 17:1, which the Greek Jeremiah lacks). Where Rahlfs asterisks a Job line (16:8b; 18:16b; 21:23b; 21:28b), the Old Greek reader did not have it. These are facts about the witnesses, not verdicts against the links.
6. **One error was the queue's, not the dig's** *(corrected 7 October 2026)*. The 15–21 dig listed קֶשֶׁת נְחוּשָׁה ("bronze bow") at 2 Sam 22:35, Ps 18:35 and Job 20:24. The queue's one-line summary (#77) shortened that to "only these two". Auditor A, given the queue's wording, rightly broke it with the parallel text. The verdict stands on the opposite function and the two-word overlap. The lesson is for the queue: a claim summary must carry the dig's own count. Parallel texts remain a standing check in the gate (2 Sam 22 = Ps 18; Isa 36–39 = 2 Kgs 18–20; Ps 14 = 53; Ps 40:14–18 = 70).

---

## Queue and Triggers

**Audited and closed:** #7, #26, #56, #57, #58, #60–79 (25 items), with #59 closed on the 19 dig's baseline. **Added:** #80–90 (11 items) from this audit. **Job queue after audit 3: 51** — the 40 not audited (#1–6, 8–12, 17–22, 25, 27–29, 31–34, 40–53, 55) plus the 11 new.

**Triggers.**

1. Count limb still armed by the backlog (51), with digs since last audit reset to 0. The next audit is best batched with the Sermon 5 material (22:1–31:40) or the Finalise pass, whichever comes first.
2. **Satisfied for the Sermon 4 backbone.** Every allusion and design claim carrying a Sermon 4 headline has now been audited. The backbone takes the verdicts as `[S: audit 3]`. The three Sermon 4 digs should be patched to carry the verdicts (recommended above) before or alongside the backbone. #21 (Ezek 14:22–23 ↔ 42:11) remains armed before the 42:7–17 dig.
3. Unchanged. Finalise is not yet planned.

---

## Addendum: History of Interpretation (Logos Round 6)

*Added 7 October 2026.* Patrick put the round 6 questions to his Logos library. The answers, corpus-checked, are assessed in the project doc `claude/job-logos-answers-round-6-assessment.md`. They fill the "History of interpretation" row that this audit left *not checked*, for these claims:

| # | Claim | History found | Rating after round 6 |
|---|---|---|---|
| 58 | Lam 2:10–17 at Job 16 | Delitzsch compares 16:13 with Lam 2:11, and 16:16 with Lam 1:20; 2:11 | **High** (unchanged); history present |
| 58 | Lam 3 at Job 19 | **Schnittjer**, *Old Testament Use of Old Testament* (2021), 557–558: Lam 3:6–9 ~ Job 19:6–12. He argues that Lamentations is the donor and Job the receptor (Job's ironic use; alterations like the friends' allusions) | **High for Lam 3:7–9 ~ 19:7–8**; the window moderate–high; the direction argued, still recorded as open |
| 63 | Isa 30:8 at 19:23–24 | Barnes; TLOT (חקק with כתב at Isa 10:1; 30:8; Job 19:23) | **High (words)** |
| 70 | Isa 44:6 at 19:25 | Delitzsch reads אַחֲרוֹן "according to Isa 44:6, 48:12, comp. 41:4" — the divine title | **Moderate–high**; high on the titular reading |
| 57 | Isa 38:14 at 17:3 | Delitzsch: "a word of entreaty" shared with Isa 38:14 and Ps 119:122; Prov 6:1 for the hand-striking | **Moderate** (confirmed) |
| 60 | Deut 19:16 at 16:8 | HALOT: כַּחַשׁ "leanness" or "lie" (Greek, Aquila, Vulgate); elsewhere the word always means "lie" | Deut 19:16 **moderate**; the forensic reading (a lying witness) **moderate–high** |
| 66 | Ps 102:6 at 19:20 | Longman (TOTC, *Psalms*, 353); HCSB cross-references for 3:24 | **High**; history present |
| 75 | The prologue's losses in the portraits | Konkel–Longman; Zuck; Andersen read the portraits as the friends' veiled description of Job | **The friends' insinuation, moderate–high** `[S]`; authorial design still not shown |
| 79 | Job 21 as reply | JFB, Lawson, Zuck: 21:17 quotes Bildad (18:5–6) to question it | **Pointed rejoinders, moderate** (confirmed); a new one, **5:26 → 21:32** (גָּדִישׁ), found |
| 84 | Ps 78:49 at 20:23 | None. HALOT reads לְחוּם as "flesh, body" (ESV "into his body") | Phrase **moderate–high**; the "eating" sequence **moderate** |
| 72 | Deut 32:32–33 at 20:14–16 | Delitzsch cites Deut 32:33 only to gloss רֹאשׁ ("poison") | **High (words)**; history weak |
| 65, 71 | Hab 1:2; Isa 14:22 | None found | Unchanged |
| 81 | Isa 5:11–14 at 21:12–14 | *Treasury of Scripture Knowledge* cross-reference only | **Moderate** (unchanged) |
| 76 | Sodom at 18:15 | Watson: "a manifest allusion" to Sodom. No ancient practice of scattering sulphur found. BHS conjectures "fire" (מַבֵּל) at 18:15 and 20:23, and the NIV84 adopts it at 18:15 | **Low–moderate (motif)** (unchanged) |

**New candidate:** #91 — Lam 3:51 (the poel of עלל, "deal severely") at Job 16:15. Delitzsch makes the comparison; the WLC files the two under different homographs (5953 d / a). *Possible–moderate.*

---

## Colophon

- **Report:** `Job/dig-deeper-job-claim-audit-3.{md,odt,html}`.
- **Auditors:** three blind general-purpose subagents, run one after another. A and B ran on 6 October 2026 and C on 7 October 2026. Their working parts are reproduced unaltered above, with headings demoted one level.
- **Briefs:** a common brief plus three claims files, written before the auditors ran and held in the session workspace.
- **Corpus:** WLC with lemma and morphology index; BHS with apparatus (Job); Swete; Rahlfs (as listed); SBLGNT; NASB95 and ESV exports.
- **Spot checks:** 24, all reproduced.
- **Verdicts:** 4 Confirmed; 12 Confirmed with nuance; 8 Needs reframing; 0 Uncertain; 1 Discard.
- **Warrant:** every count names its edition; every "only" was checked by lemma and, for phrases, by exact consonants; every absence was preceded by a passing positive control. History of interpretation was not checked.
