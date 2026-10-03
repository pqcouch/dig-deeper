# Claim Audit 2: Job

**Passages audited:** eleven claims — the Sermon 3 load-bearing set from the project's `claude/claim-audit-queue.md` (Job #13–16, #23–24, #35–39), in three parts:

- **Part A (Torah, Former Prophets and Psalm 39):** A1 Exod 33:19–34:7 (#13); A2 the Sinai–Horeb revelation texts behind Eliphaz's vision (#35); A3 Deut 32:23–25, 39 and 28:29 (#37); A4 Psalm 39 (#16).
- **Part B (the Latter Prophets):** B1 Isa 44:24 and Job's two creation hymns (#14); B2 Isa 50:6–9 (#23); B3 Hosea as a live source (#36); B4 Amos's doxologies (#15).
- **Part C (the Writings and a canonical dialogue):** C1 Psalm 44, with the Romans 8 convergence (#24); C2 Ps 107:40–42 divided between Eliphaz and Job (#38); C3 the canon's reply to Job 4:7 (#39).

**Date:** 3 October 2026

**Purpose:** to test the cross-passage allusion and pattern claims that carry weight in the Sermon 3 digs (Job 9:1–10:22; 13:1–14:22; 4:1–5:27) before the 4:1–14:22 unit dig and the Sermon 3 backbone. Both limbs of trigger 1 of the standing rule had fired (41 candidates queued; four digs since the last audit), and trigger 2 was armed: four of these claims carry headline findings.

**Primary texts:**

- **Hebrew:** WLC with its lemma and morphology index (the observation layer). BHS (Logos export) for Job where a reading mattered.
- **Greek Old Testament:** Swete LXX for the whole canon; Rahlfs–Hanhart exports (Logos) for Job, Genesis, Exodus, Numbers, Deuteronomy, Kings, Isaiah, Jeremiah, Hosea, Amos, Micah, Psalms, Proverbs and Ecclesiastes.
- **New Testament:** SBLGNT with the MorphGNT index.
- **English:** NASB95 and ESV (Logos exports).

**Study text:** NASB95 · **Pulpit text:** ESV (Sermon 3 is in view).

**Versification:** references follow the Hebrew (WLC) numbering. Where the English differs, the English number is added where it is quoted (e.g. Ps 39:14 = Eng 39:13; Ps 44:23–25 = Eng 44:22–24; Ps 107 is the same in both).

**Earlier audit:** `Job/dig-deeper-job-claim-audit.md` (28 September 2026: the structure claims and the Bejon notes) stands and is not re-opened here. Its verdict on the שׁוֹט / שׁוּט sound-play (9:23) is cited where relevant.

---

## Method

The method is the Mark audit's (29 September 2026), as refined in the two Matthew audits, with one addition — an explicit **chance baseline for every "only" claim**.

**Three independent auditors.** Each was a fresh subagent with no access to the book overview, the sweep, the Job digs, the queue's reasoning, the earlier audit, or one another's work. Each was given the claims as proposals to break, with only the proposed rating attached. They ran **one after another, not in parallel**.

**The corpus in the cloud.** The `_texts/` corpus (WLC text and lemma index, Swete, SBLGNT and the needed Logos exports) was staged into the session workspace, and the auditors worked through a shared helper library (`/home/claude/jobaudit/alib.py`) offering lemma, co-occurrence, phrase (with a skeletal pass) and ketiv searches in the Hebrew; accent-insensitive searches in Swete and the SBLGNT; and the Rahlfs and English exports. Every auditor ran the positive control first (חֶסֶד in Job: 6:14; 10:12; 37:13), and every claimed absence was preceded by a search returning a known hit.

**The chance baseline.** Before the audit, the main session measured how ordinary an "only X and Y" pair is. In Job 4 a verse has on average **about two content-lemma pairs that occur together in exactly one other verse** of the Hebrew Bible (WLC; lemmas in at most 400 verses); across the whole book the figure is 1.34 (1.87 at a 700-verse cap). So a single exclusive pair proves little. The auditors were told to judge links by **clustering, rarity, verbatim phrasing, matching function and the absence of a rival**, and to build a chance baseline for every pattern or design claim. They used three kinds:

- **exclusive-pair counts** for each Job verse, and how many point to the proposed source;
- **window tests** (how often several Job verses converge by chance on one short source window);
- **control-book rates** (for "live source" claims: Job's exclusive pairs and shared rare lemmas per 1,000 verses of comparable books) and, for the Ps 107 design claim, a **permutation test**.

**Each auditor did seven things for every claim:** read the Job verses (WLC, Swete, Rahlfs); read the source with its context; verified every stated "only"; took frequency and chance baselines; searched for the strongest rival; scored the Hays criteria; and gave a verdict, a final rating and a line on what a preacher may safely say.

**Sources.** No commentaries and no web sources were used, so "History of Interpretation" is recorded as *not checked* throughout. Where the Greek translators' renderings bear on a link, they are reported as data within the corpus.

**Spot checks.** The main session then re-ran the evidence on which the verdicts turn (see Spot Checks).

---

## Positional Frame (Phase 0.6)

**What has the book set up that these claims serve?** Job opens with God's verdict on "My servant Job" (1:8; 2:3) and three friends who come to comfort him (2:11). Round one of the dialogue (4–14) is where the friends' doctrine is first stated and Job first turns from the friends to God. The digs on 4–5, 9–10 and 13–14 proposed that both sides speak in the words of other Scripture — the Torah's revelations and curses, the prophets' hymns and Servant, the Psalter's laments — and that the book stages a contest over shared texts.

**Why does this matter here?** These are exactly the claims that most easily overreach. A dig working at speed across a whole speech finds many "only X and Y" pairs, and the baseline shows that such pairs are common. The question for each claim was therefore not only "is the word-count right?" but "is this link above what chance produces, and is there a better source?"

---

## Part A: Torah, Former Prophets and Psalm 39

### Auditor's note

**Corpus.** WLC Hebrew with its lemma index (Strong's numbers), Swete's LXX, Rahlfs–Hanhart exports (Job, Exodus, Numbers, Deuteronomy, Kings, Psalms), all read through `alib.py`. Every count below names its edition. Unless stated otherwise, a count is a number of **verses** in the WLC.

**Positive control.** `lem('2617','Job')` returned Job 6:14, 10:12, 37:13, as required. Each absence claimed below was preceded by a search that returned a known hit: `ph('בטרם אלך')` returned Ps 39:14 before the variant spellings were tested; `lem('5352','Exod')` returned Exod 34:7 before the co-occurrence tests; `lem('4272')` returned Deut 32:39 before the מחץ + רפא test; and the Swete searches returned Deut 4:12 and 1 Kgs 19:12 before the Job tests.

**Method.** For each claim I (1) read the Job verses and the source in the WLC, Swete and Rahlfs; (2) tested every "only" claim by lemma, and by consonantal phrase where one was stated (`ph` also runs a skeletal pass, and I checked the ketiv); (3) took lemma frequencies; (4) counted exclusive content-lemma pairs (`excl_pairs`, at maxfreq 400 and 700) for each Job verse and compared them with the chapter baseline; (5) looked for rivals in three ways: the verse-level partners each Job verse shares most with, weighted by rarity; windows of verses scored on the claim's own lemma set (biased towards the proposed source, and labelled as such); and windows scored on *all* the rarer lemmas of the Job passage (unbiased).

**Baselines (WLC).** Exclusive pairs per verse: Job overall 1.34 (maxfreq 400) and 1.87 (700); Job 4: 2.10 / 2.48; Job 5: 1.52 / 2.04; Job 7: 1.10 / 1.95; Job 9: 0.89; Job 10: 0.91; Job 13: 1.07. Across the book, 4% of Job verses have five or more exclusive pairs at maxfreq 400, and 8% at 700.

**Limits.** These are lemma statistics on a proxy text, not BHS. Strong's numbering merges some homographs and splits some cognates; for example, the verb חדל (2308) and the adjective חָדֵל (2310) carry different numbers. The pair method cannot see phrase-level or cross-verse links, so I tested those separately. History of Interpretation: **not checked** (no commentaries, no web). Where the LXX translator's own rendering bears on a link I report it as data inside the corpus, not as interpretive history.

Tags: [T] = on the page; [I] = inference.

---

### A1: Exodus 33:19–34:7 (the passing-by and the proclamation of the Name) behind Job 7, 9, 10, 13

**Source:** #13 · 9:1–10:22 dig (Tool 11; Tool 7 on נקה and חנן) and 13:1–14:22 dig (Tool 11 on 13:21–24)

**Claim (as tested).** Job's laments draw on the Sinai theophany and the Name-formula: God "passing by" unseen (9:11), נקה (acquit) with עָוֹן (iniquity) (10:14) next to חֶסֶד (steadfast love) (10:12), חנן (be gracious) (9:15), נשׂא + פֶּשַׁע + עָוֹן (7:21), the sin triad (13:23), and God's hand and hidden face (13:21, 24). Proposed rating: moderate–high, synthetic.

**Evidence**
- [T] Every stated "only" list verified (WLC): נקה + עָוֹן = Exod 34:7; Num 5:31; 14:18; Job 10:14. With חֶסֶד as well = Exod 34:7; Num 14:18. נשׂא + פֶּשַׁע + עָוֹן = Exod 34:7; Num 14:18; Mic 7:18; Ps 32:5; Job 7:21. עָוֹן + פֶּשַׁע + חַטָּאת = Exod 34:7; Lev 16:21; Ps 32:5; Isa 59:12; Ezek 21:29; Dan 9:24; Job 13:23. **None failed.**
- [T] Job uses negated piel נקה twice with God as subject: 9:28 and 10:14, both לֹא תְנַקֵּנִי (you will not acquit me). The 9:28 parallel to the formula's וְנַקֵּה לֹא יְנַקֶּה (he will by no means acquit) is as close as 10:14's, and the claim leaves it out. The same idiom is also at Exod 20:7 / Deut 5:11; Nah 1:3; Jer 30:11; 46:28.
- [T] **Cross-verse test.** Searching for נקה within ±2 verses of both חֶסֶד and עָוֹן returns Exod 34:7; Num 14:18; Job 10:14, and also **Exod 20:7 / Deut 5:11** (the Decalogue: "visiting iniquity … showing חֶסֶד … will not acquit") and Prov 16:5. So the 10:12–14 cluster matches the formula *tradition*, which has two Torah loci, not Exod 34 alone.
- [T] **Job 9:11 עבר.** עבר occurs in 492 verses. With God as subject: Exod 12:12, 23; 33:19, 22; 34:6; 1 Kgs 19:11 (וְהִנֵּה יְהוָה עֹבֵר, "and behold, the LORD passed by"); Amos 5:17; 7:8; 8:2. So it is not exclusive. Job 9:11 pairs it with חלף, and חלף is the verb of Eliphaz's spirit in **Job 4:15** (וְרוּחַ עַל־פָּנַי יַחֲלֹף, "a spirit passed before my face").
- [T] **Greek check, Job 9:11.** Swete and Rahlfs read ἐὰν ὑπερβῇ με … καὶ ἐὰν παρέλθῃ με. So παρέλθῃ renders **יַחֲלֹף**, not יַעֲבֹר, and the match with Exod 34:6 παρῆλθεν is Greek only. It does not map onto the Hebrew word the claim names.
- [T] **Job 9:15 חנן.** The hithpael אֶתְחַנָּן (I implore mercy) appears at Deut 3:23 (Moses), Job 9:15; 19:16; Ps 30:9; 142:2. Exod 33:19 has qal חָנַן with God as subject. The stem, subject and sense all differ.
- [T] **Job 13:21, 24.** סור + כַּף (remove + hand) occurs only at Exod 33:23 and Ps 81:7. Job 13:21 uses רחק (put far), not סור. The hidden face (סתר + פָּנִים, 37 verses) **does not occur in Exod 33**, which uses ראה (see). It is the lament idiom (Ps 13:2; 22:25; 27:9; 44:25; 88:15; 102:3; 143:7) and also Deut 31:17–18; 32:20. On this point the link **fails lexically**.
- [T] **Exclusive pairs (maxfreq 400).** 9:11: 0; 9:15: 1 (Deut 19:18); 10:12: 2 (Job 6:4; Hos 9:7); 10:14: 1 (Jer 2:35); 7:21: 0; 13:21: 0; 13:23: 0; 13:24: 1 (Ps 55:13). **None of the six points to Exod 33–34.** The Exodus links are triples of moderately common sin-words (עָוֹן in 215 verses, פֶּשַׁע in 90, חַטָּאת in 270, נשׂא in 609), each shared with 4–7 verses.

**Baseline.** Using the claim's own lemma set (biased), Exod 33:19–34:7 holds 9 of 10 features against 6 for the next windows (Num 14; Mic 7; Ps 25; Ps 31–32; Ps 50–51). That is expected, since the set was drawn from Exodus. Using *all* the rarer lemmas of the Job verses (unbiased, 12-verse windows), Exod 33:23–34:11 scores 11, level with or behind Isa 43:16–27 (12), Mic 6:16–7:11 (12), Ps 51:2–13 (12), 1 Sam 25 (11), 2 Sam 12 (11) and Ps 31:16–32:2 (11). [I] The pattern does not stand out above what the general vocabulary of sin and pardon produces.

**Rival sources**
- **Mic 7:18** for Job 7:21. It shares four lemmas (נשׂא, עָוֹן, עבר, פֶּשַׁע), including the עבר that Exod 34:7 lacks, and Mic 7:18 also has חֶסֶד. It is itself a reworking of the formula.
- **Ps 32:5** for 13:23 (and 7:21). It shares עָוֹן + פֶּשַׁע + חַטָּאת + hiphil ידע (אוֹדִיעֲךָ ~ הֹדִיעֵנִי, "make me know") + נשׂא, in a first-person lament about sin. It outranks Exod 34:7 on shared lemmas, as does Isa 59:12.
- **2 Sam 24:10; Zech 3:4** for the idiom הֶעֱבִיר עָוֹן (take away iniquity) in 7:21.
- **Ps 130:3** for 10:14: אִם + שׁמר + עָוֹן ("If you should mark iniquities"), with חֶסֶד at 130:7. Its function is closer than Exod 34:7.
- **1 Kgs 19:11 and Job 4:15** for God "passing by".

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | Both are canonical Torah texts; compositional order is open. The formula was widely reused (Num 14:18; Joel 2:13; Jonah 4:2; Ps 86:15; 103:8; 145:8; Neh 9:17; Nah 1:3; Mic 7:18) |
| Volume | Weak–Possible | No exclusive pairs; the triples are shared with 4–7 verses; the only rare-ish lemma is נקה (33 verses) |
| Recurrence | Possible | Formula vocabulary recurs in 7:21; 9:28; 10:12–14; 13:23 |
| Thematic coherence | Possible | Job inverts the "forgiving/not acquitting" God. The theophany elements (passing, hand, face) do not cohere lexically |
| Historical plausibility | Possible | Use of the formula tradition is plausible; direction left open |
| History of interpretation | Not checked | — |
| Satisfaction | Weak–Possible | "Formula tradition" explains the data; "Exod 33–34 specifically" adds little |

**Verdict.** Needs reframing.

**Final rating.** Moderate for Job's engagement with the Exod 34:6–7 forgiveness formula *tradition*. Low for a specific link to the Exod 33 theophany (passing by, hand, face, חנן).

**Reasoning.** The "only" statements are true, but they rest on combinations of common sin-words. Closer rivals exist for individual verses: Mic 7:18 for 7:21, Ps 32:5 and Isa 59:12 for 13:23, Ps 130:3 for 10:14. The Decalogue (Exod 20:5–7) is an equal Torah locus for the 10:12–14 cluster. The theophany strand fails or is weak: the hidden face is absent from Exod 33, חנן differs in stem, and the Greek "passing" verb renders a different Hebrew word. Job 9:11 is better read alongside Job 4:15 and 1 Kgs 19:11.

**What a preacher may safely say.** "Job keeps throwing the language of Israel's great confession of the Name (Exod 34:6–7: the God who forgives iniquity, transgression and sin, yet will by no means clear the guilty) back at God. It is a confession he knows, and he cannot square it with what is happening to him." (The confession is paraphrased here, not quoted from NASB95.)

**Book-overview action.** The overview's map has no Exodus row. At the Finalise pass add **Exod 34:6–7 (formula tradition) → 7:21; 9:28; 10:12–14; 13:23**, moderate, with Exod 20:5–7, Mic 7:18, Ps 32:5 and Ps 130:3 named; record the Exod 33 theophany reading of 9:11 and 13:21–24 as low.

---

### A2: The Sinai–Horeb revelation texts behind Eliphaz's night vision (Job 4:12–18)

**Source:** #35 · 4:1–5:27 dig, Headline 2 and Tool 11

**Claim (as tested).** Job 4:16 contains three pairs, each exclusive to one revelation text: מַרְאֶה + תְּמוּנָה (appearance + form) → Num 12:8; תְּמוּנָה + קוֹל (form + voice) → Deut 4:12; דְּמָמָה + קוֹל (silence + voice) → 1 Kgs 19:12. There are supporting links in 4:13 and 4:15. The vision is told in the vocabulary of the canon's great revelations, and its message (4:17–18) contradicts God's "My servant" (1:8; 2:3). Proposed rating: high on words, moderate–high on design.

**Evidence**
- [T] All three exclusive pairs verified (WLC): מַרְאֶה + תְּמוּנָה = Num 12:8; Job 4:16 only. תְּמוּנָה + קוֹל = Deut 4:12; Job 4:16 only. דְּמָמָה + קוֹל = 1 Kgs 19:12; Job 4:16 only. **None failed.**
- [T] Rarity: תְּמוּנָה occurs in **10 verses** (Exod 20:4; Num 12:8; Deut 4:12, 15, 16, 23, 25; 5:8; Ps 17:15; Job 4:16), seven of them in the Sinai/Horeb prohibition texts. דְּמָמָה occurs in **3 verses** (1 Kgs 19:12; Ps 107:29; Job 4:16). Two of its three uses sit next to קוֹל: קוֹל דְּמָמָה דַקָּה (1 Kgs 19:12) and דְּמָמָה וָקוֹל (Job 4:16, same words in reversed order).
- [T] **Sequence match with 1 Kgs 19:11–12:** a רוּחַ (wind/spirit) passes, a figure or person stands (עמד), then silence and voice. Job 4:15–16 has רוּחַ … יַחֲלֹף (passes), יַעֲמֹד (it stood), then דְּמָמָה וָקוֹל. רוּחַ + עמד on its own is ordinary (15 verses), but the ordered sequence is not.
- [T] **Num 12:6–8 is a two-verse cluster, stronger than claimed:** 4:16 ~ 12:8 (מַרְאֶה + תְּמוּנָה), and 4:18 "in His servants (עֲבָדָיו) He puts no trust (יַאֲמִין)" ~ 12:7 "My servant (עַבְדִּי) Moses … he is faithful (נֶאֱמָן)". עבד + אמן is not exclusive (13 verses), but it falls in the adjacent verse of the same source and is semantically inverted [I].
- [T] **Servant language.** עֶבֶד in Job: 1:8; 2:3; 4:18; 42:7, 8 (and five non-divine uses). [I] Eliphaz's "He puts no trust in His servants" sits between God's two "My servant Job" sayings in the prologue and the four in 42:7–8, where God rebukes Eliphaz for not speaking rightly "as My servant Job". Num 12:8 ends "why were you not afraid to speak against My servant Moses?" and the chapter closes with Moses interceding (12:13), as Job does for Eliphaz (42:8). This is a structural observation, not a lexical proof.
- [T] תַּרְדֵּמָה (deep sleep) + נפל (fall) = Gen 2:21; 15:12; 1 Sam 26:12; Prov 19:15; Job 4:13; 33:15. Gen 15:12 alone adds dread falling on the recipient (אֵימָה … נֹפֶלֶת) at a night revelation, matching 4:13–14 in function. **Job 33:15 repeats 4:13b verbatim** (בִּנְפֹל תַּרְדֵּמָה עַל־אֲנָשִׁים, "when deep sleep falls on men"). Elihu reprises Eliphaz's line.
- [T] סמר + בָּשָׂר (bristle + flesh) = Job 4:15; Ps 119:120 only (verified). Ps 119:120 also has פַּחַד (dread), as Job 4:14 does: a three-lemma tie, but in a fear-of-judgement idiom, not a revelation scene.
- [T] **Greek (Swete = Rahlfs here).** 4:16 reads καὶ οὐκ ἦν μορφὴ πρὸ ὀφθαλμῶν μου, ἀλλ᾽ ἢ αὔραν καὶ φωνὴν ἤκουον ("there was no form before my eyes, only a breeze and a voice I heard"). The translator **negated** the Hebrew ("a form was before my eyes"). The construction "no [form] … only … voice" (ἀλλ᾽ ἢ … φωνη-) occurs in Swete only at Deut 4:12 (ὁμοίωμα οὐκ εἴδετε ἀλλ᾽ ἢ φωνήν, "you saw no likeness, only a voice") and Job 4:16. [I] The Greek translator heard Deut 4:12 here. αὔρα occurs in Swete only at 1 Kgs 19:12 and Job 4:16. But Rahlfs also has it at Ps 106:29 (= MT 107:29 דְּמָמָה), so αὔρα is the translators' **stock equivalent** for דְּמָמָה and not independent evidence.
- [T] Swete and Rahlfs 4:17 read ἄμεμπτος, as in 1:1, 1:8 and 2:3: **confirmed**. But Greek Job uses ἄμεμπτος 11 times (Swete: 1:1, 8; 2:3; 4:17; 9:20; 11:4; 12:4; 15:14; 22:3, 19; 33:9), and here it renders Hebrew יִטְהַר (be pure), not תָּם (blameless). It is a Greek-level echo of the prologue, not a Hebrew one.

**Baseline.** Job 4:16 has 3 exclusive pairs at maxfreq 400 (Num 12:8; Dan 8:15; Gen 31:32) and **5** at 700 (adding 1 Kgs 19:12 and Deut 4:12, because קוֹל occurs in 436 verses). That puts it in the top 8% of Job verses. **Four of the five point to vision or revelation texts**; the fifth (Gen 31:32, נכר + נֶגֶד) is noise. By contrast, the exclusive pairs of Job 4:14 go to Ps 53:6, Isa 33:14 and Jer 13:22, with no coherent pattern. [I] The coherence of 4:16's pairs is well above chance. In a window search on all the rarer lemmas of 4:12–16, though, the generic terror vocabulary dominates: Deut 28:62–68 ranks first, 1 Kgs 19:8–14 fifth, Dan 8:15–21 eleventh, and Num 12 and Deut 4 do not appear, because each rests on one very rare word. The links are **distributed across three sources and anchored in rare words**, not concentrated in one passage.

**Rival sources**
- **Dan 8:15–18.** עמד + נֶגֶד + מַרְאֶה is exclusive to Dan 8:15 and Job 4:16 (a figure "standing before me with the appearance of a man"). It continues with a voice (8:16), deep sleep (נִרְדַּמְתִּי, root רדם, 8:18) and falling on the face. This equals Num 12:8 in volume for the "standing figure" element, but it lacks the rare anchors (תְּמוּנָה, דְּמָמָה) and the Torah theology of "form versus voice". Direction is open; Daniel is usually taken as late, so this may be reception of Job or shared vision-genre idiom.
- **Gen 15:12** for 4:13–14. It is a better match than Gen 2:21 (night revelation, deep sleep plus dread).
- **Ps 119:120** for 4:14–15 (fear idiom).
- No single rival outranks the combination of Num 12 + Deut 4 + 1 Kgs 19.

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Strong | Torah and Former Prophets; order of composition open |
| Volume | Strong | Three exclusive pairs in one verse, two anchored in words of 10 and 3 occurrences; a near-verbatim reversed collocation with 1 Kgs 19:12 |
| Recurrence | Possible | 4:18 ~ Num 12:7; 4:13 reprised at 33:15; the servant motif runs through 1:8 / 2:3 / 42:7–8 |
| Thematic coherence | Strong | "A form I could not make out; silence and a voice" inverts Moses' "form of the LORD" and sits close to Horeb's "no form, only a voice" |
| Historical plausibility | Possible–Strong | Plausible either way; the LXX translator already read 4:16 through Deut 4:12 |
| History of interpretation | Not checked | (LXX rendering noted as a corpus datum) |
| Satisfaction | Strong | Explains the oddities of 4:16 better than generic vision language does |

**Verdict.** Confirmed with nuance.

**Final rating.** High on the words; moderate–high on the design.

**Reasoning.** The three exclusive pairs are real, rare-anchored, packed into a single verse, and coherent in a way chance pairs are not, and the Greek translator seems to have heard Deut 4:12. The nuance: the vocabulary is spread across three sources rather than drawn from one; Dan 8:15 is an equal rival for the "standing figure"; and the 4:13–15 support (תַּרְדֵּמָה, סמר) is shared with non-revelation texts. The "servant" contradiction is an inference strengthened by Num 12:7–8 and Job 42:7–8, not a lexical datum.

**What a preacher may safely say.** "Eliphaz describes his night vision in words that recall how God spoke to Moses and to Elijah. Yet what his voice tells him — 'He puts no trust even in His servants' (4:18) — is the very thing God contradicts when He calls Job 'My servant'."

**Book-overview action.** Add **Num 12:6–8 + Deut 4:12 + 1 Kgs 19:11–12 → 4:12–18**: high on words, moderate–high on design; note Num 12:7 ~ 4:18 and Dan 8:15 as a rival for the standing figure.

---

### A3: Deuteronomy 32:23–25, 39 and 28:29 behind Eliphaz (Job 5) and Job's reply (6:4)

**Source:** #37 · 4:1–5:27 dig, Headline 3 (its Deuteronomy half) and Tool 11

**Claim (as tested).** מחץ + רפא only Deut 32:39 / Job 5:18; רֶשֶׁף (Resheph, "flame/plague") 5:7 ~ Deut 32:24, with famine and teeth; משׁשׁ + צָהֳרַיִם (grope + noon) only Deut 28:29 / Job 5:14; Job 6:4 arrows and poison ~ Deut 32:23–24; משׁשׁ + חֹשֶׁךְ (grope + darkness) only Exod 10:21; Job 5:14; 12:25. Proposed rating: high on words for 32:39 and 28:29; moderate for the 32:23–25 cluster.

**Evidence**
- [T] Verified (WLC): מחץ + רפא = Deut 32:39; Job 5:18 only (מחץ occurs in 14 verses). משׁשׁ + צָהֳרַיִם = Deut 28:29; Job 5:14 only. משׁשׁ + חֹשֶׁךְ = Exod 10:21; Job 5:14; 12:25 only (משׁשׁ occurs in 8 verses). **None failed.** Job 5:18 contains a ketiv (וידו, qere וְיָדָיו "his hands"); it does not affect the lemma test.
- [T] **Job 5:18 has a second parent in form.** Hos 6:1 "He has torn and will heal (רפא) us; He has struck and will bind us up (חבשׁ)" gives the same double wound/bind and strike/heal frame. חבשׁ + רפא = Ezek 34:4; Hos 6:1; Isa 30:26; Ps 147:3; Job 5:18. [I] Job 5:18 combines Deut 32:39's verbs with the frame of Hos 6:1.
- [T] **Additional link not in the claim.** Job 10:7 וְאֵין מִיָּדְךָ מַצִּיל ("and there is none to deliver from Your hand") transposes Deut 32:39 וְאֵין מִיָּדִי מַצִּיל into the second person. The phrase מידי מציל occurs only at Deut 32:39 and Isa 43:13. Job's reply turns Eliphaz's Deut 32:39 against him. Isa 43:13 is a co-rival; its מִי יְשִׁיבֶנָּה (who can turn it back?) has a counterpart in Job 9:12.
- [T] **Greek, Job 5:14.** ψηλαφ- + μεσημβρ- (grope + noon) occurs in Swete at Deut 28:29, **Isa 59:10** and Job 5:14. Isa 59:10 (Hebrew גשׁשׁ, a different verb, + צָהֳרַיִם + עִוְרִים "the blind") reuses Deut 28:29, so the image had currency beyond Deuteronomy. The Hebrew exclusivity with Deut 28:29 stands.
- [T] **Job 5:7 רֶשֶׁף** occurs in 6 verses: Deut 32:24 (plague); Hab 3:5 (with דֶּבֶר, pestilence); Ps 76:4 (flashes of the bow, i.e. arrows); 78:48 (lightning); Song 8:6 (flames); Job 5:7. "Sparks fly upward" fits the flame/flash sense of Song 8:6 and Ps 76:4, not Deut 32:24's plague. רֶשֶׁף + רָעָב (famine) is in one verse only at Deut 32:24; Job splits them across 5:7 and 5:20, 13 verses apart. Swete Job 5:7 reads νεοσσοὶ γυπός ("young of the vulture"): the translator saw no Resheph.
- [T] **Job 6:4.** חֵץ + חֵמָה (arrow + venom/wrath) in one verse occurs only at Job 6:4. Within ±2 verses: Deut 32:23–24; Ezek 5:15–16; **Ps 38:2–3**. חֵמָה means "venom" at Deut 32:24, 33; Ps 58:5; 140:4, and 6:4's "my spirit drinks their poison" fits that sense, which favours Deut 32. But "drinking the חֵמָה of Shaddai" recurs at **Job 21:20**, and Isa 51:17, 22 has the cup of wrath. Swete reads θυμός (wrath).
- [T] **Teeth and beasts.** Job 4:10 שִׁנֵּי כְפִירִים (teeth of young lions): its exclusive pair goes to **Ps 58:7** (שִׁנֵּימוֹ … כְּפִירִים), not to Deut 32:24 (שֶׁן־בְּהֵמוֹת, "teeth of beasts"). Job 5:22–23 (beasts of the field, covenant, at peace): בְּרִית + חַיָּה + שָׂדֶה = Hos 2:20; Job 5:23 only. Famine, sword and beast together = Ezek 5:17; 14:21.

**Baseline.** Exclusive pairs at maxfreq 700: 4:10 → 3 (Ps 58:7; Prov 26:13; Joel 1:6); 5:7 → 2 (Hos 9:11; Ps 90:10); 5:14 → 4 (**Deut 28:29**; Job 24:16; Isa 58:10; Isa 16:3); 5:18 → 1 (**Deut 32:39**); 5:20 → 2 (Hos 13:14; Jer 18:21); 6:4 → 7 (none to Deut 32). That is **2 of 19 to Deuteronomy**, both in the strong single links. The 32:23–25 cluster is invisible at verse level. At window level (all rarer lemmas of 4:10, 5:7, 5:14, 5:18, 5:20, 5:22, 6:4; 17-verse windows; unbiased), **Deut 32:23–39 ranks second** (10 lemmas) behind Ps 55:5–21 (12, generic day/night/fear words) and ahead of **Ps 91** (9). On the claim's own feature set it leads with 10 of 13, ahead of Ps 58:4–59:8 (7). [I] There is a real, though diffuse, cross-verse affinity with Deut 32, above most windows but not unique.

**Rival sources**
- **Hos 6:1** for the form of 5:18.
- **Ps 91** for Eliphaz's promises in 5:19–23: terror by night, arrow by day, noon, the lion (שַׁחַל) and young lion (כְּפִיר) as in 4:10, and "you will not fear" (לֹא תִירָא) as in 5:21–22.
- **Ps 58:5–8** for venom, teeth of young lions and arrows (4:10 + 6:4).
- **Ps 38:2–3** (first-person "Your arrows have sunk into me", with חֵמָה) for 6:4. It matches 6:4 in register, as Deut 32 matches in sense.
- **Hos 2:20** for the covenant with the beasts (5:23).
- **Isa 59:10** as a second witness to the groping-at-noon image.
- **Isa 43:13** as a co-source for 10:7.
- None outranks Deut 32:39 for 5:18 or Deut 28:29 for 5:14.

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Strong | Deuteronomy's Song and curses; order of composition open |
| Volume | Strong (32:39; 28:29) / Weak (32:23–25) | Two exclusive pairs on rare lemmas (מחץ 14 verses, משׁשׁ 8); the cluster rests on single common words or cross-verse spreads |
| Recurrence | Possible–Strong | 32:39 recurs in Job 10:7 (phrase); 28:29 is backed by 12:25 (משׁשׁ + חֹשֶׁךְ) |
| Thematic coherence | Strong | Eliphaz quotes the "I wound and I heal" God; Job answers that the arrows and poison are in him and that none delivers from God's hand |
| Historical plausibility | Possible–Strong | Plausible; Isa 59:10 shows Deut 28:29 already being reused |
| History of interpretation | Not checked | — |
| Satisfaction | Strong / Weak | Strong for 5:18, 5:14 and 10:7; weak for 5:7 רֶשֶׁף and the teeth |

**Verdict.** Confirmed with nuance. Strong for Deut 32:39 → 5:18 (and 10:7) and Deut 28:29 → 5:14. The 32:23–25 cluster needs reframing as diffuse affinity, with Ps 91, Ps 58 and Ps 38 as live rivals.

**Final rating.** High for 32:39 and 28:29; low–moderate for the 32:23–25 cluster. Overall: moderate–high.

**Reasoning.** Both exclusive links are verified and rest on rare verbs in matching contexts, and Job's own 10:7 confirms that Deut 32:39 is being used, which the claim did not notice. The רֶשֶׁף link fails on sense (flame, not plague), the teeth link prefers Ps 58:7, and 6:4 is split between Deut 32 (sense of "venom") and Ps 38 (register of the sufferer). The verse-level exclusive pairs do not support the cluster.

**What a preacher may safely say.** "Eliphaz uses the Song of Moses: God wounds and God heals (Deut 32:39; Job 5:18). Job answers that 'the arrows of the Almighty are within me' (6:4) and, in the same Song's words, 'there is no deliverance from Your hand' (10:7)."

**Book-overview action.** Add **Deut 32:39 → 5:18; 10:7** as a **live** source (high) and **Deut 28:29 → 5:14** (high); record רֶשֶׁף at 5:7 as a non-link to Deut 32:24; the 32:23–25 cluster low–moderate.

---

### A4: Psalm 39 as a "live source" in Job 7, 9, 10 and 14

**Source:** #16 · 9:1–10:22 dig (Tool 11; Tool 10) and 13:1–14:22 dig (14:6)

**Claim (as tested).** בְּטֶרֶם אֵלֵךְ (before I go) only Ps 39:14 / Job 10:21; וְאַבְלִיגָה (that I may be cheerful) only Job 9:27; 10:20; Ps 39:14; plus הוֹדִיעֵנִי (make me know), סור + מֵעָלַי (remove from me), שׁמר + חטא (keep + sin), הֶבֶל (breath), שׁעה + מִן (look away from), חדל (cease). Proposed rating: high; a live source.

**Evidence**
- [T] **בְּטֶרֶם אֵלֵךְ:** verified by phrase and by skeletal pass: Job 10:21; Ps 39:14 only (WLC). Variants tested: בטרם אלכה → 0; טרם אלך → the same two. By lemma, טֶרֶם + הלך (3212) also returns **Gen 45:28** (אֵלְכָה … בְּטֶרֶם אָמוּת, "I will go … before I die"), a different construction. The phrase claim holds; a bare lemma claim would not.
- [T] **וְאַבְלִיגָה:** verified: Job 9:27; 10:20; Ps 39:14 only (WLC phrase and skeletal). The root בלג (1082) occurs in **4 verses** in all (the others are Amos 5:9, a different sense; Jer 8:18 מַבְלִיגִיתִי is a separate lemma). No ketiv issue: the ketiv in Job 10:20 is יחדל ישית (qere חֲדַל וְשִׁית), not the בלג form.
- [T] **Ps 39:14 ↔ Job 10:20–21 is an ordered sequence:** an imperative of turning away + מִמֶּנִּי (from me) + וְאַבְלִיגָה + בְּטֶרֶם אֵלֵךְ + a negated future (Ps וְאֵינֶנִּי "and am no more"; Job וְלֹא אָשׁוּב "and shall not return"). Job substitutes שִׁית (turn) for הָשַׁע (look away) and adds מְעַט (a little). [I] This is near-quotation.
- [T] **Ps 39:14's elements recur across Job:** שׁעה + מִן = Isa 22:4; Job 7:19 (תִשְׁעֶה מִמֶּנִּי); Ps 39:14 (שׁעה occurs in 15 verses), plus Job 14:6 שְׁעֵה מֵעָלָיו; וְאַבְלִיגָה at 9:27; וְאֵינֶנִּי at 7:21 and 7:8 (common: 80 verses). Isa 22:4 ("look away from me, let me weep") is a real but non-addressee rival.
- [T] **Weaker sub-links.** הוֹדִיעֵנִי occurs in 26 verses (including Exod 33:13; Ps 25:4; 143:8; and Job 38:3; 40:7; 42:4, spoken by God), and its content differs (Ps 39:5 "my end"; Job 10:2 "why You contend"; 13:23 "my sins"): weak. סר + מֵעָלַי: 27 verses (skeletal): weak lexically, though Ps 39:11 (remove Your stroke, the blow of Your hand) fits Job 9:34 and 13:21 in function. שׁמר + חטא = 2 Kgs 10:31; Job 10:14; Ps 39:2, but the subject is inverted (the psalmist guards himself; God watches Job). Ps 130:3 is a closer functional rival. הֶבֶל + יָמִים (breath + days): Eccl ×5; Jer 16:19; Ps 39:6; 78:33; **144:4**; Job 7:16, so not distinctive. **חדל fails as stated:** Ps 39:5 has the adjective חָדֵל (2310, "fleeting"), while Job 7:16, 10:20 and 14:6 have the verb (2308, "cease, leave off"). They share a root but differ in sense.
- [T] **Moth (עָשׁ)**, an extra link the claim did not list: Ps 39:12 ~ Job 13:28 (and 4:19). The noun occurs in about 7 Hebrew verses; the Strong's 6211 total of 12 includes Aramaic homographs in Dan 4–5.
- [T] **Greek.** Rahlfs/Swete Ps 38:14 πρὸ τοῦ με ἀπελθεῖν ~ Job 10:21 πρὸ τοῦ με πορευθῆναι (partial). Greek Job 9:27 drops "be cheerful", and 10:20 ἀναπαύσασθαι differs from Ps 38:14 ἀναψύξω. The Greek translators did not reproduce the link verbatim.

**Baseline.** Exclusive pairs in Job 10:20–22 (maxfreq 400/700): 10:20 → 0; 10:21 → 1 (Jer 13:16, טֶרֶם + צַלְמָוֶת "deep darkness"); 10:22 → 1 (Job 28:3). **0 of 2 point to Ps 39.** This is a blind spot of the method: in 10:20 בלג pairs only with function words, and the טֶרֶם + הלך pair falls above the frequency cap (הלך occurs in 936 verses) and is not exclusive (Gen 45:28). The link is phrasal and cross-verse, which the pair statistic cannot see. Measured directly, the co-occurrence of בלג (4 verses) and the phrase בְּטֶרֶם אֵלֵךְ (2 verses) within two verses happens **only** at Ps 39:14 and Job 10:20–21. On a bag-of-lemmas comparison with Job 7; 9:25–35; 10; 14, Ps 39 ranks only about tenth among psalms per verse (behind Ps 13, 6, 90, 23, 101, 141, 53, 143, 14). Its distinctiveness lies entirely in the rare lemmas (בלג, שׁעה) and the exact phrasing.

**Rival sources**
- **Ps 6** has more rare lemmas in common (ערשׂ "couch", עשׁשׁ "waste away", עתק "grow old" and others) but no phrase identity.
- **Ps 90** (90:10 עָמָל + "fly away" ~ Job 5:7, which is not a Job 7–14 link) and **Ps 88** (darkness, the land of the dead, the hidden face) are thematic rivals.
- **Ps 144:4** for הֶבֶל + days; **Ps 130:3** for "marking" sin; **Isa 22:4** for "look away from me".
- **None outranks Ps 39** for the 9:27 / 10:20–21 / 7:19 / 14:6 complex.

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible–Strong | Psalm with a Davidic superscription; relative date unknown, direction open |
| Volume | Strong | Exact phrase (2 occurrences) + a rare verb form (3 occurrences, root 4) in the same order as the psalm |
| Recurrence | Strong | Ps 39:14's elements recur at 7:19; 7:21; 9:27; 10:20–21; 14:6; moth at 13:28 |
| Thematic coherence | Strong | Brevity of life, a plea for God to look away, death as no return; Job also voices what Ps 39:2–3, 10 keeps silent [I] |
| Historical plausibility | Possible | Either direction is possible; the near-quotation shows dependence, not who borrowed |
| History of interpretation | Not checked | — |
| Satisfaction | Strong (39:14) / Weak (others) | Ps 39:14 explains 10:20–21 better than any rival; several listed sub-links add nothing |

**Verdict.** Confirmed with nuance.

**Final rating.** High for Ps 39:14 behind Job 10:20–21 and 9:27, with recurrence at 7:19 and 14:6. Moderate–high for "live source" as a description of the whole psalm.

**Reasoning.** The two exact-phrase links are robust across spelling variants, the skeletal pass and the ketiv check, and Job 10:20–21 reproduces Ps 39:14's sequence in order. It is the strongest verbal link in Part A. Its weight sits on one verse of the psalm. Of the other proposed links, three are weak (הוֹדִיעֵנִי, סור מֵעָלַי, שׁמר + חטא), one is common (הֶבֶל), and one fails as stated (חדל: adjective against verb). The exclusive-pair statistic misses the link entirely, which is a warning about relying on that statistic for phrasal allusion.

**What a preacher may safely say.** "When Job begs God, 'Withdraw from me that I may have a little cheer before I go — and I shall not return' (10:20–21), he is praying the closing words of Psalm 39 ('Turn Your gaze away from me, that I may smile again before I depart and am no more', Ps 39:13 Eng) almost word for word, and taking them further than the psalmist dared."

**Book-overview action.** Add **Ps 39:14 → 9:27; 10:20–21** (high), live with 7:19; 14:6 and the moth at 13:28; add Ps 39 to the live-sources sentence; strike חדל as a link.

---

## Part B: The Latter Prophets

### Auditor's note

**Corpus.** Hebrew: Westminster Leningrad Codex (WLC) with the Strong's lemma index in `alib.py`. Greek OT: Swete (LXX numbering). Rahlfs–Hanhart: Logos exports for Job, Isaiah, Hosea and Amos. Every count below names the edition it was taken from. Nothing was cited from BHS or NA28; any finding that ends up load-bearing still needs checking against BHS and Rahlfs in Logos.

**Control.** `lem('2617','Job')` returned Job 6:14; 10:12; 37:13, as required. Each search behind a claimed absence or exclusivity was first run on a known hit: for example, `co(['5186','8064'])` returns all 20 verses where נטה (stretch out) and שָׁמַיִם (heavens) occur together before `co(['5186','8064','905'])` narrows them to two. Phrase searches (`ph`) were checked on pointed forms where it mattered. Isa 44:24 ends with a ketiv (מי אתי); it does not affect any lemma used here.

**Method.** I verified every "only" claim by lemma. I took verse frequencies with `lemfreq` and exclusive-pair counts with `excl_pairs`. Two baselines of my own were added, both from the WLC:
- **Window test.** Across all 1,060 eleven-verse windows in Job, I counted how many *distinct* Job verses have exclusive pairs pointing into a single three-verse window of one other book.
- **Control-book rates.** For each book, I counted (a) Job's exclusive pairs pointing to it and (b) rare lemmas (found in five verses or fewer) that it shares with Job, each normalised per 1,000 verses of that book.

**Limits.**
- `alib` folds homograph letters together (2790 covers both חרשׁ "plough" and חרשׁ "be silent"), so a few exclusive pairs are artefacts. I flag them where they matter.
- History of Interpretation was not checked (no commentaries, no web).
- Tags: [T] = on the page; [I] = inference.

---

### B1: Isaiah 44:24 behind Job's two creation hymns (9:5–10; 10:8–12)

**Source:** #14 · 9:1–10:22 dig, Tool 11 and the support for Headline 3

**Claim (as tested).** נטה + שָׁמַיִם + לְבַד ("who alone stretches out the heavens") occur together only in Isa 44:24 and Job 9:8. Isa 44:24's "who formed you from the womb" supplies the second hymn (Job 10:8–12). On this reading Job's two hymns are the two halves of Isa 44:24, whose speaker is "your Redeemer" (גֹּאֵל; cf. Job 19:25).

**Evidence**
- [T] WLC: נטה + שָׁמַיִם + לְבַד occur together only in **Isa 44:24 and Job 9:8**. The claim is **verified**. Even נטה + לְבַד alone is exclusive to this pair. Swete agrees: τὸν οὐρανὸν μόνος appears only in Job 9:8 (ὁ τανύσας) and Isa 44:24 (ἐξέτεινα), and Rahlfs is the same. The verbs differ in the Greek.
- [T] The formula itself is common. WLC has נטה + שָׁמַיִם in 20 verses. The bare participle נֹטֶה שָׁמַיִם, as in Job, appears in Isa 44:24; 51:13; Ps 104:2; Zech 12:1. Related forms are in Isa 40:22; 42:5; 45:12; Jer 10:12 = 51:15. The only distinguishing element is לְבַד (alone): first person in Isaiah (לְבַדִּי), third person in Job (לְבַדּוֹ).
- [T] Supporting data outside 9:8:
  - The Poel יְהוֹלֵל ("makes fools of") occurs only in Isa 44:25, Job 12:17 and Eccl 7:7 (WLC, pointed search). In both Isaiah and Job it sits inside a participial hymn.
  - Isa 44:27 הָאֹמֵר לַצּוּלָה ("who says to the deep") resembles Job 9:7 הָאֹמֵר לַחֶרֶס ("who speaks to the sun").
- [T] Job 9:8 is a **composite verse**. Line 8a matches Isa 44:24. Line 8b (וְדוֹרֵךְ עַל־בָּמֳתֵי יָם, "and treads on the heights of the sea") matches Amos 4:13 (וְדֹרֵךְ עַל־בָּמֳתֵי אָרֶץ, "… of the earth") word for word apart from the final noun. See B4.
- [T] **The "second half" fails lexically.**
  - יצר ("form", Isa 44:24's verb) **never occurs in Job** (WLC: zero).
  - Job 10:8–12 uses עצב (fashion), עשה (make), חֹמֶר (clay), סכך (weave), לבשׁ (clothe), but not בֶּטֶן (womb).
  - בֶּטֶן in 10:19 is "from the womb to the grave", which is about death, not formation.
  - יצר + בֶּטֶן occur in Isa 44:2, 24; 49:5; Jer 1:5, none of them in Job.
  - Job's only formation-in-the-womb verse is 31:15 (עשה + בֶּטֶן). That pair is shared with Isa 44:2 and 44:24, but also with Eccl 11:5 and Hos 9:16.
- [T] **גֹּאֵל is not distinctive.** Isaiah uses lemma 1350 in 24 verses (35:9–63:16), and the divine title recurs in 41:14; 43:14; 44:6; 47:4; 48:17; 49:7, 26; 54:5, 8; 59:20; 60:16. Job 19:25 stands nine chapters away from 9–10.

**Baseline.** Job 9:5–10 + 10:8–12 (11 verses) contain 14 exclusive pairs in the WLC (maxfreq 400). One of them points to Isa 44:24, which is about what chance predicts (Job 9–10 average is 0.89 per verse). The window test finds no three-verse source receiving links from more than one of these verses. The phrase stands on a three-lemma exclusive clause supported by the Greek, not on a cluster.

**Rival sources**
- For the "Maker of heavens and of man" pairing: Zech 12:1 (נֹטֶה שָׁמַיִם … וְיֹצֵר רוּחַ־אָדָם, "stretches out the heavens … forms the human spirit"; Swete has πλάσσων, as in Isa 44:24), Isa 42:5, 45:12 ("my hands stretched out the heavens", with אָדָם, man) and 51:13. The pairing is **formulaic**.
- For Job 10:8–12:
  - **Ps 119:73** יָדֶיךָ עָשׂוּנִי ("your hands made me"). In the WLC, יָדֶיךָ + עשה + 1cs is shared only with Job 10:8, and Swete Ps 118:73 αἱ χεῖρές σου ἔπλασάν με agrees with Swete Job 10:8 in its first clause (the second verbs differ: ἡτοίμασάν / ἐποίησάν; see Spot Checks, 16).
  - **Ps 139:13** (סכך + בֶּטֶן; cf. Job 10:11 תְּסֹכְכֵנִי, "you knit me").
  - Gen 2:7; 3:19 for clay and dust (10:9).

  Each of these outranks Isa 44:24 for 10:8–12.

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | Relative dates of Job and Isa 40–55 are disputed; direction open |
| Volume | Possible | Three-lemma exclusive clause, but inside a 20-verse formula; one distinguishing word |
| Recurrence | Possible | יְהוֹלֵל (Isa 44:25 ~ Job 12:17) and הָאֹמֵר ל־ suggest acquaintance with Isa 44:24–28 |
| Thematic Coherence | Possible | Sole-Creator theme fits 9:5–10; the "two halves" design is not supported |
| Historical Plausibility | Possible | Both draw on shared hymnic stock |
| History of Interpretation | not checked | — |
| Satisfaction | Weak (design) / Possible (phrase) | Ps 119/139 explain 10:8–12 better |

**Verdict.** Needs reframing. The phrase link is confirmed; the "two halves" design is discarded.

**Final rating.** Phrase (9:8a ~ Isa 44:24): **moderate–high**. Two-hymn design: **low**.

**Reasoning.** The "alone" clause is genuinely exclusive in both the WLC and Swete. Together with the Poel יְהוֹלֵל, it makes acquaintance with Isa 44:24–28 plausible. But 9:8 is a mosaic: its second line is Amos 4:13. The womb-formation hymn has no Hebrew tie to Isa 44:24 and much closer ones to Ps 119:73 and Ps 139:13. The Redeemer bridge rests on a title Isaiah uses everywhere.

**What a preacher may safely say.** "Job's 'who alone stretches out the heavens' (9:8) uses the very words of Isaiah's confession of the one Creator, 'stretching out the heavens by Myself' (Isa 44:24)." Do not claim that Job's two hymns are built on that verse's two halves.

**Book-overview action.** Add **Isa 44:24 → 9:8a** (moderate–high) in one row with Amos 4:13; 5:8 → 9:8b–9, as the mosaic of 9:5–10. Record the "two halves of Isa 44:24" design as a non-link; 10:8–12 goes with Ps 119:73 and Ps 139:13.

---

### B2: Isaiah 50:6–9 (the third Servant Song) behind Job 13:18–28

**Source:** #23 · 13:1–14:22 dig, Headline 2

**Claim (as tested).** Job 13:18–28 is linked to Isa 50:6–9 by:
- the "who will contend?" question;
- the moth-and-garment clause;
- Isa 50:8's four court words (מִי, רִיב, צדק, מִשְׁפָּט);
- "I know … vindicated";
- hiding the face;
- the Greek, which keeps these links.

The claimed inversion: the Servant's accusers wear out, while Job himself wears out.

**Evidence**
- [T] WLC: מִי + רִיב occur together only in **Isa 50:8 and Job 13:19** (verified). The phrasing is almost identical: מִי־הוּא יָרִיב עִמָּדִי (Job) and מִי־יָרִיב אִתִּי (Isa), both meaning "who will contend with me?"
- [T] WLC: בלה + בֶּגֶד + עָשׁ occur together only in **Isa 50:9 and Job 13:28** (verified). Adding אכל ("eat") gives four shared lemmas in one clause, still exclusive. בֶּגֶד + עָשׁ alone: Isa 50:9; 51:8; Job 13:28 (verified). בלה + בֶּגֶד: Isa 50:9; 51:6; Job 13:28; Ps 102:27.
- [T] WLC: Isa 50:8 is the **only verse in the Hebrew Bible** with רִיב + צדק + מִשְׁפָּט. Job 13:18–19 spreads the same four across two verses (verified).
- [T] "I know … vindicated":
  - Job 13:18 יָדַעְתִּי כִּי־אֲנִי אֶצְדָּק ("I know that I will be vindicated") parallels Isa 50:7 וָאֵדַע כִּי־לֹא אֵבוֹשׁ ("I know that I will not be put to shame") plus 50:8 מַצְדִּיקִי ("he who vindicates me").
  - In one verse, ידע + צדק occur only in Gen 38:26; Job 9:2; 13:18, so the construction is also Job's own.
- [T] **Job's own idiom.** Job 23:6 repeats יָרִיב עִמָּדִי. Job 9:20 has צדק with יַרְשִׁיעֵנִי ("would condemn me"), the very form in Isa 50:9. מִי־הוּא appears in Job 4:7; 9:24; 13:19; 17:3; 41:2. The court lexicon is native to Job 9–13.
- [T] **Hiding the face** (סתר + פָּנִים) occurs in 37 WLC verses and is non-distinctive.
- [T] Wider Servant-Song resonance:
  - נכה + לְחִי ("strike the cheek"): Isa 50:6 and Job 16:10 (9 verses in all).
  - רֹק ("spit") occurs in three verses only: Isa 50:6; Job 7:19; 30:10.
- [T] **Greek** (Swete; Rahlfs is the same in substance):
  - τίς … ὁ κρινόμενός μοι (Isa 50:8) and τίς … ὁ κριθησόμενός μοι (Job 13:19): each phrase appears only in its own verse.
  - Job 13:28 ἱμάτιον σητόβρωτον, παλαιοῦται ("a moth-eaten garment, wears out") answers Isa 50:9 ὡς ἱμάτιον παλαιωθήσεσθε … σής ("you will wear out like a garment … moth").
  - [I] OG Job 13:18 reads ἐγγύς εἰμι τοῦ κρίματός μου ("I am near my judgement"); the MT has "I have set out my case". This may assimilate Isa 50:8 ἐγγίζει ὁ δικαιώσας με ("he who vindicates me draws near"). If so, the translator heard the link.
- [T] **Inversion.** In Isa 50:7, 9 the Servant has God as helper (עזר) and his accusers (כֻּלָּם) wear out. In Job 13:28 the subject וְהוּא ("and he") wears out. Read with 14:1, that is Job as mortal man. Job never says "I have no helper" in ch. 13, so that half of the contrast is [I], though it is a reasonable reading.

**Baseline**
- Job 13:18–28 contains 17 exclusive pairs (WLC, maxfreq 400). Two of them, from two different Job verses (13:19, 13:28), point to Isa 50:8–9.
- Window test: two distinct Job verses converging on one three-verse source window happens in **6.1%** of eleven-verse windows in Job, and three never does. The cluster is in the top decile, not off the scale.
- On raw counts, Lev 26:36 has three exclusive pairs with Job 13:25 (driven leaf, pursue), but all from one verse.
- What lifts Isa 50 above chance is quality, not count: a four-lemma clause, a near-verbatim question, the only verse holding all the court words, and agreement in the Greek.

**Rival sources**
- For 13:28:
  - Isa 51:6–8 (the same Isaianic complex; together the three verses hold all four lemmas).
  - Ps 102:27 (כֻּלָּם כַּבֶּגֶד יִבְלוּ, "they will all wear out like a garment", nearly verbatim with Isa 50:9, but **no moth**).
  - Hos 5:12 (רָקָב + עָשׁ, rot + moth, exclusive with 13:28's first half).

  Isa 50:9 remains the closest single verse.
- For the court words: Isa 41:1, 21; 43:26; 54:17; Mic 6:1–2; Jer 2:9; Hos 4:1. Each has ריב or משפט, but none has מִי + ריב + צדק + משפט.

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | Dating unresolved; direction open |
| Volume | Strong | Four-lemma exclusive clause; near-verbatim question; Greek agrees |
| Recurrence | Possible–Strong | Isa 50:6 echoes at Job 16:10; רֹק (3×) at 7:19; 30:10 |
| Thematic Coherence | Strong | Both are first-person trial speeches by an innocent sufferer before God |
| Historical Plausibility | Possible | Shared legal register; either could depend on the other |
| History of Interpretation | not checked | — |
| Satisfaction | Strong | The inversion gives a coherent reading of 13:28 |

**Verdict.** Confirmed with nuance.

**Final rating.** **Moderate–high.** The words are high; the deliberate link is moderate–high; direction of dependence is open.

**Reasoning.** This is the strongest of the four claims. The convergence is of a kind the baseline rarely produces: two independent exclusive links in one speech to two adjacent verses, one of them four lemmas long, both kept in the Greek. The nuance: Job's court vocabulary is his own (9:2–3, 20; 23:6), so the claim should rest on 13:19 and 13:28, not on the generic legal words or the hiding of the face.

**What a preacher may safely say.** "Job asks the Servant's question, 'Who will contend with me?' (Isa 50:8). But where the Servant's accusers wear out like a moth-eaten garment, Job says it is he who wears out (13:28)." Treat which text came first as an open question.

**Book-overview action.** Add **Isa 50:8–9 → 13:19, 28** (moderate–high; direction open), with 16:10 and the רֹק links as recurrence.

---

### B3: Hosea as a "live source" in Job (mainly Eliphaz, Job 4–5)

**Source:** #36 · 4:1–5:27 dig, Headline 3 (its Hosea half) and Tool 11

**Claim (as tested).** Eliphaz speaks Hosea's covenant language of judgement and healing. The proposed links:
- plough/reap (4:8 ~ Hos 10:13);
- lions (4:10 ~ Hos 5:14);
- "none to deliver" (5:4);
- bind/heal (5:18 ~ Hos 6:1);
- covenant with the beasts (5:23 ~ Hos 2:20);
- rot/moth (13:28 ~ Hos 5:12);
- the lion that hunts (10:16).

**Evidence (all WLC unless stated)**
- [T] חרשׁ + קצר (plough + reap): 1 Sam 8:12; Amos 9:13; Hos 10:13; Job 4:8. Verified as stated. "Moral sense only" is a semantic filter, not a lemma fact.
- [T] שַׁחַל + כְּפִיר (two lion words): Hos 5:14; Ps 91:13; Job 4:10. Verified. וְאֵין מַצִּיל ("none to deliver") is in 11 verses (verified).
- [T] חבשׁ + רפא (bind + heal): Isa 30:26; Ezek 34:4; Hos 6:1; Ps 147:3; Job 5:18. Verified. **מחץ + רפא (strike + heal) occurs only in Deut 32:39 and Job 5:18** (verified). Syntax:
  - Job 5:18 כִּי הוּא יַכְאִיב וְיֶחְבָּשׁ ("for he wounds and binds up");
  - Hos 6:1 כִּי הוּא טָרָף וְיִרְפָּאֵנוּ ("for he has torn, and he will heal us");
  - Deut 32:39 has מָחַצְתִּי וַאֲנִי אֶרְפָּא … וְאֵין מִיָּדִי מַצִּיל ("I strike and I heal … none delivers from my hand").
- [T] בְּרִית + חַיַּת הַשָּׂדֶה (covenant + beasts of the field) occur together only in **Hos 2:20 and Job 5:23** (verified). חֶרֶב + מִלְחָמָה (sword + war, Hos 2:20 ~ Job 5:20) occur together in 21 verses, so that part is common.
- [T] רָקָב + עָשׁ (rot + moth) occur together only in **Hos 5:12 and Job 13:28** (verified).
- [T] שַׁחַל is in 7 verses. God is the שַׁחַל in Hos 5:14 and 13:7. In Job 10:16 the lion is ambiguous ("if it lifts itself, like a lion you hunt me"). **OG Job 10:16 makes Job the hunted lion** (ἀγρεύομαι … ὥσπερ λέων, "I am hunted like a lion").
- [T] **A link not in the claim:** פדה + מָוֶת (+ יד), "ransom from death (from the hand)", occurs only in **Hos 13:14 and Job 5:20**. Swete agrees: ῥύομαι + ἐκ θανάτου + ἐκ χειρός in both.
- [T] **Greek.**
  - Job 5:4 καὶ οὐκ ἔσται ὁ ἐξαιρούμενος ("and there will be none to rescue") is **verbatim** Hos 5:14. Only these two verses have the full phrase in Swete; Rahlfs agrees.
  - But the Greek loses the rest: Hos 10:13 reads παρεσιωπήσατε (the translator took חרשׁ as "be silent"); Hos 5:12 has no moth; OG Job 5:23 lacks the covenant clause (Rahlfs too).

**Baseline (control books)**
- **Exclusive pairs** from the whole of Job (WLC, maxfreq 400), per 1,000 verses of the target book:

  | Hosea | Joel | Zephaniah | Amos | Jonah | Nahum | Micah | Habakkuk |
  |---|---|---|---|---|---|---|---|
  | 71 (14 pairs) | 68 | 75 | 82 | 104 | 149 | 181 | 196 |

  Hosea sits at or below the Minor-Prophet median.
- In Job 3–14: Hosea 35.5, Joel 41, Mal 54, Micah 57, Habakkuk 107. In Job 4–5, Hosea gets 2 pairs (4:3; 5:20), the same as Micah, Habakkuk and Jonah.
- **Rare lemmas** (≤5 verses) shared with Job: Hosea 6 (30.5 per 1,000), Amos 54.8, Micah 57, Nahum 106, Zephaniah 151.
- Window test on Job 4–5: the largest cluster points to Isa 35:3 (weak hands and knees, 4:3–4), not to Hosea.
- Several of the proposed links are not exclusive pairs at all: they involve lemmas in more than 400 verses, or pairs found in three to five verses.
- **Hosea is not statistically elevated in Job.**

**Rival sources**
- **Deut 32:39** for 5:18 and 5:4 (exclusive מחץ + רפא, plus "none delivers from my hand"). Hos 5:14–6:1 itself echoes Deut 32:39 (tearing, healing, אֵין מַצִּיל), so Deut 32 is the common ancestor [I].
- **Proverbs.**
  - Prov 22:8 has two exclusive pairs with Job 4:8 (זרע + קצר + אָוֶן, sow + reap + iniquity, found only in Prov 22:8 and Job 4:8). Hosea has none.
  - Prov 3:11–12 (מוּסַר … אַל־תִּמְאָס, "do not despise the discipline"; יוֹכִיחַ, "he reproves") is nearly verbatim with Job 5:17.
  - Prov 22:22 (דכא + שַׁעַר, "crush in the gate") is exclusive with Job 5:4.
  - Prov 26:13 (שַׁחַל + אַרְיֵה, two lion words) is exclusive with Job 4:10.
- **Ps 91** shares 11 content lemmas with Job 4:8–11 + 5:4 + 5:17–26: lions, protection, "you will not fear".
- **Lev 26:6 / Ezek 34:25** for the beasts and peace (בְּרִית שָׁלוֹם, "covenant of peace", חַיָּה רָעָה, "evil beast"). Job 11:19 וְאֵין מַחֲרִיד ("none will make you afraid") is Lev 26:6's phrase.

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | Direction open |
| Volume | Possible | Two clean exclusives (2:20 ~ 5:23; 13:14 ~ 5:20) and one in 13:28; the rest are shared stock |
| Recurrence | Possible | Several Hosea contacts, but no more than chance relative to Micah, Habakkuk or Nahum |
| Thematic Coherence | Possible | Wound-and-heal and covenant-peace fit Eliphaz, but equally fit Deut 32, Lev 26 and Proverbs |
| Historical Plausibility | Possible | Covenant-blessing stock was widely shared |
| History of Interpretation | not checked | — |
| Satisfaction | Weak (as "pattern") | Proverbs and Deut 32 explain Eliphaz's idiom at least as well |

**Verdict.** Needs reframing.

**Final rating.** Individual echoes (Hos 2:20 ~ Job 5:23; Hos 13:14 ~ Job 5:20; Hos 5:12 ~ Job 13:28): **moderate**. "Hosea as a live source" pattern: **low–moderate**.

**Reasoning.** The stated "only" claims all check out, and one extra exclusive (Hos 13:14 ~ Job 5:20) strengthens the individual case. But the control-book baseline shows Job meets Hosea no more often than it meets Micah, Habakkuk or Nahum. For several of the key verses (4:8, 5:4, 5:17, 5:18) the stronger exclusive links go to Proverbs and Deut 32. Eliphaz speaks a pooled covenant-and-wisdom idiom of which Hosea is one voice, not *the* source.

**What a preacher may safely say.** "Eliphaz uses the language of Israel's covenant hope (a covenant with the beasts of the field, ransom from death, a God who wounds and heals) that we also hear in Hosea and in the Song of Moses." Do not say Eliphaz is quoting Hosea.

**Book-overview action.** **Hosea is not a live source.** Record its three single echoes (2:20 ~ 5:23; 13:14 ~ 5:20; 5:12 ~ 13:28) at moderate, and add Prov 3:11–12 (already in the map), Prov 22:8, 22 and Ps 91 as Eliphaz's idiom.

---

### B4: Amos's doxologies (4:13; 5:8–9; 9:5–6) as a "live source" in Job

**Source:** #15 · 9:1–10:22 dig (Tool 11; Tool 5)

**Claim (as tested).** Job 3:4–9, 9:5–10, 9:27 and 10:20–22 draw on Amos's doxologies, through:
- עֵיפָה ("gloom", occurring twice);
- treading the heights;
- the constellations;
- בלג ("flash" / "be cheerful");
- shared participial-hymn form.

**Evidence (WLC unless stated)**
- [T] עֵיפָה is **lemma 5890 in both** verses: Amos 4:13 עֵיפָה and Job 10:22 עֵיפָתָה (same noun with a ה ending). There are only two verses, so the claim is **verified**. But the root is wider: עוף II ("be dark") appears at Job 11:17 (תָּעֻפָה כַּבֹּקֶר תִּהְיֶה, "darkness will be like morning"), and מוּעָף / מָעוּף at Isa 8:22–23.
- [T] דרך + בָּמָה (tread + heights): Amos 4:13; Mic 1:3; Deut 33:29; Hab 3:19; Job 9:8. Adding יָם (sea) leaves Job alone (verified). Amos 4:13 is the closest form: participle + עַל־בָּמֳתֵי + noun, inside a hymn.
- [T] כִּימָה (Pleiades) occurs only in Amos 5:8; Job 9:9; 38:31. כְּסִיל (Orion) adds Isa 13:10 (verified). **עשה + כִּימָה ("maker of the Pleiades") occurs only in Amos 5:8 and Job 9:9**: עֹשֶׂה … כְּסִיל וְכִימָה in Job, עֹשֵׂה כִימָה וּכְסִיל in Amos.
- [T] Overlap with Job 9:5–10 (content lemmas shared): Amos 5:8, 7 (including כִּימָה, כְּסִיל, הפך "turn", יָם); Amos 4:13, 6 (including דרך, בָּמָה, הָרִים "mountains"); Isa 44:24, 6; Isa 40:22, 4; Jer 10:12, 4; Ps 104:2, 2.
- [T] בלג occurs in four verses: Amos 5:9; Job 9:27; 10:20; Ps 39:14 (verified). But **Ps 39:14 is nearly verbatim with Job 10:20–21**: both have וְאַבְלִיגָה ("that I may brighten up") and בְּטֶרֶם אֵלֵךְ ("before I go"), and that second phrase occurs only in Ps 39:14 and Job 10:21. Amos 5:9 uses the Hiphil participle in a different sense ("makes destruction flash").
- [T] Job 3:4–9: **Jer 13:16** shares חשׁך (darken) + נֶשֶׁף (twilight) + קוה (hope) + אוֹר (light) with Job 3:9, found only in those two verses, and adds צַלְמָוֶת (deep darkness). Amos 5:8 shares only common lemmas there. צַלְמָוֶת occurs in 17 verses, 9 of them in Job; it is Job's own word.
- [T] **A link not in the claim:** בֹּקֶר + צַלְמָוֶת (morning + deep darkness) occur together only in **Amos 5:8 and Job 24:17**. In Job, morning *is* deep darkness to the wicked: an inversion of Amos's "turns deep darkness into morning" [I].
- [T] **Greek.**
  - OG Amos 5:8 has **no constellations** (ὁ ποιῶν πάντα καὶ μετασκευάζων, "who makes all things and transforms them"; Swete and Rahlfs).
  - Amos 4:13 renders עֵיפָה ὁμίχλην ("mist"), while OG Job 10:21–22 has σκοτεινὴν καὶ γνοφεράν ("dark and gloomy"). The Greek preserves neither link.
  - Rahlfs Amos 5:8 εἰς τὸ πρωὶ σκιὰν θανάτου ("into the morning, the shadow of death") matches Job 24:17 τὸ πρωὶ σκιὰ θανάτου. Swete's Amos has only σκιάν.
- [T] **Participial hymn as a general form.** Isa 40:22–23; 44:24–28; Ps 104:2–4; Job 12:17–25; 26:7–13 all use the same form.

**Baseline**
- **Exclusive pairs** from the whole of Job to Amos (WLC, maxfreq 400): 12, or 82 per 1,000 Amos verses. That is mid-table, below Micah (181), Habakkuk (196) and Nahum (149).
- **Rare shared lemmas** (≤5 verses): Amos 8 (54.8 per 1,000), Micah 57, Habakkuk 54, Nahum 106, Zephaniah 151.
- **Concentration** is the real signal: 4 of Amos's 8 rare shared lemmas sit in the doxologies (4:13; 5:8–9). That concentration is not unique, though. Zephaniah 1 has 4 rare shared lemmas, and Habakkuk 3 has 9 (at ≤8 verses). Their Job contacts, however, are scattered, not concentrated in one Job passage.

**Rival sources**
- **Ps 39:14** for 9:27 and 10:20–21; it outranks Amos.
- **Jer 13:16** (and Amos 8:9) for 3:4–9; it outranks Amos 5:8.
- **Isa 44:24** for 9:8a.
- For 9:8b–9, Amos 4:13 and 5:8 have **no stronger rival**.

**Hays criteria**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | Direction open |
| Volume | Strong (9:8b–9) / Weak (3:4–9; 9:27; 10:20) | Rare-lemma and near-verbatim matches in 9:8b–9; rivals elsewhere |
| Recurrence | Possible–Strong | 9:8b, 9:9, 10:22 and 24:17 each touch the doxologies |
| Thematic Coherence | Strong (9:5–10) | God as cosmic Maker and Overturner in participles, in both texts |
| Historical Plausibility | Possible | Shared doxological stock |
| History of Interpretation | not checked | — |
| Satisfaction | Possible | Explains 9:8b–9 well; over-reaches for chs. 3 and 10 |

**Verdict.** Confirmed with nuance for Job 9:8b–9 (plus עֵיפָה at 10:22 and Job 24:17). Needs reframing for the wider design: drop 3:4–9 and 9:27/10:20.

**Final rating.** Job 9:8b–9 ~ Amos 4:13; 5:8: **moderate–high**. "Amos as a live source" across 3:4–10:22: **moderate**.

**Reasoning.** Job 9:8b–9 shares with Amos's doxologies a near-verbatim participial clause ("treads on the heights of …") and the unique "maker of the Pleiades and Orion". No rival comes close for those lines. עֵיפָה and Job 24:17 add rare, independent contacts. But Ps 39:14 owns Job 10:20–21, Jer 13:16 owns Job 3:9, and Amos's overall rate in Job is ordinary. So the claim holds for the hymn of ch. 9, not for a design running from Job 3 to 10.

**What a preacher may safely say.** "Job's hymn to the God who 'tramples down the waves of the sea' and 'makes the Bear, Orion and the Pleiades' (9:8–9) speaks in the words of Amos's doxologies (Amos 4:13; 5:8). And Job's 'Withdraw from me that I may have a little cheer before I go' (10:20–21) is Psalm 39's prayer."

**Book-overview action.** Add **Amos 4:13; 5:8 → 9:8b–9** (moderate–high), with 10:22 (עֵיפָה) and 24:17; drop 3:4–9 (Jer 13:16 owns it) and 9:27 / 10:20 (Ps 39:14 owns them).

---

**Cross-claim observation [I].** Job 9:5–10 is woven from a shared prophetic-doxological stock:
- 9:8a matches Isa 44:24;
- 9:8b matches Amos 4:13;
- 9:9 matches Amos 5:8.

B1 and B4 are better presented together, as one claim about the hymn's mosaic, than as two competing "sources".

---

## Part C: The Writings and a Canonical Dialogue

### Auditor's note

**Corpus.** WLC Hebrew (Open Scriptures/morphhb, lemma-indexed by Strong's number); Swete's LXX (Vaticanus-based; LXX numbering, so Ps 43 = MT Ps 44 and Ps 106 = MT Ps 107; Swete's Ecclesiastes runs one verse ahead in ch. 7, so Swete Eccl 7:16 = MT 7:15); Rahlfs–Hanhart exports for Job, Psalms, Isaiah, Micah and Ecclesiastes; SBLGNT for Romans. All Hebrew counts below are **WLC** verse counts unless stated otherwise. Greek readings are labelled Swete or Rahlfs.

**Positive control.** `lem('2617','Job')` returned Job 6:14, 10:12, 37:13 as required. Before each claimed absence I checked that the same search returned the Job verse itself (e.g. the יָשָׁר + אבד search returns Job 4:7, and the phrase search for לָמָּה פָנֶיךָ תַסְתִּיר returns Job 13:24). No ketiv tokens were found in Job 5:16, 13:24 or 14:12, so the phrase searches there can be relied on.

**Method.** Each claim was tested for (a) verse-level lemma co-occurrence, (b) consonantal phrase matches (plain and skeletal), (c) multi-verse windows where a link spans neighbouring verses, (d) a frequency baseline for each lemma, and (e) the exclusive-pair baseline: in Job 4 a verse has on average **2.1** content-lemma pairs that occur together in exactly one other verse (maxfreq 400). For C2's design claim I built three explicit chance baselines (see C2). Rivals were looked for by lemma and by phrase.

**Limits.** The corpus is an observation layer, not a citation layer. BHS/apparatus questions were not checked. History of Interpretation was **not checked** (no commentaries, no web). I leave the direction of dependence open throughout unless the evidence decides it, which it never does here.

Tags: **[T]** = on the page; **[I]** = inference.

---

### C1: Psalm 44 behind Job 13:24 and 14:12 (with 13:9 and Zophar's 11:6), and a convergence with Romans 8

**Source:** #24 · 13:1–14:22 dig (Tool 11; Christological reading)

**Claim (as tested).** Psalm 44:22–27 is a source for Job 13:24 and 14:12, with lesser echoes in Job 13:9 and Zophar's 11:6. Psalm 44 is the lament of a faithful, innocent community, and this register suits Job. Romans 8:33–36 quotes Ps 44:23 and draws on Isa 50:8–9, and Job 13:18–24 draws on both.

**Evidence.**
- [T] **Job 13:24 = Ps 44:25a, word for word.** לָמָּה־פָנֶיךָ תַסְתִּיר ("Why do You hide Your face?"). The phrase occurs only in Job 13:24 and Ps 44:25 (WLC, plain and skeletal phrase search). Verified.
- [T] The lemma triad מָה + סתר + פָּנִים occurs only in Deut 32:20, Job 13:24, Ps 44:25 and Ps 88:15 (WLC). **Verified as stated.** סתר + מָה without פָּנִים adds Isa 40:27 and Ps 89:47.
- [T] **New, and stronger than proposed.** Job 13:24b continues "and count me (וְתַחְשְׁבֵנִי) as Your enemy". Ps 44:23 has "we are counted (נֶחְשַׁבְנוּ) as sheep for slaughter". The set חשׁב + סתר + פָּנִים within a three-verse window occurs only at Job 13:22–24 and Ps 44:23–25 (WLC). So Job 13:24 takes up two adjacent verses of the psalm (vv. 23 and 25), not just one.
- [T] **Job 14:12 ~ Ps 44:24.** עור ("arouse") + קיץ ("awake") + a sleep lemma in one verse: only Job 14:12 and Ps 44:24 (WLC). This holds even when the sleep lemmas are pooled (ישׁן verb 3462 / adjective 3463 / שֵׁנָה 8142) and both "awake" lemmas (6974/3364) are allowed. **Verified, with one nuance:** the psalm has the verb תִישַׁן, while Job has the noun מִשְּׁנָתָם. The pair עור + קיץ also occurs in Hab 2:19 and Ps 35:23 and 73:20. The prayer "Arouse/awake, Lord" is a lament topos: Ps 7:7; 35:23; 44:24; 59:5–6.
- [T] **Ps 44:22 ~ Job 13:9.** חקר ("search out") is shared, with God as subject in a rhetorical question in both. But חקר occurs in 26 verses (WLC), six of them in Job. This is weak on its own.
- [T] **תַּעֲלֻמוֹת ("secrets") occurs only in Job 11:6, Job 28:11 and Ps 44:22 (WLC). Verified.** [T] Zophar's next lines add more: Job 11:11 כִּי־הוּא יָדַע ("for He knows") ≈ Ps 44:22 כִּי־הוּא יֹדֵעַ. That trigram occurs only in Job 11:11, Job 28:23, Ps 44:22 and Ps 103:14. Zophar's 11:6 + 11:11 therefore gives a small two-point echo of Ps 44:22 [I].
- [T] **Dust and rise (Ps 44:26–27 ~ Job 14:8, 12, 19).** This is generic. עָפָר + קוּם in one verse occurs in 1 Sam 2:8; Isa 2:19; 26:19; 52:2; Job 19:25; Ps 113:7 (WLC). No Job 14 verse is among them. Weak.
- [T] **Register.** Ps 44:18–22 protests covenant loyalty: "we have not forgotten You (וְלֹא שְׁכַחֲנוּךָ)… if we had… would not God search this out?" This matches Job 13:18, 23 ("I know that I will be vindicated… make me know my transgression"). Thematic fit is strong.
- [T] **Greek.** Rom 8:36 (SBLGNT) = Swete and Rahlfs Ps 43:23 word for word, except that SBLGNT has Ἕνεκεν where Swete and Rahlfs have ἕνεκα. **Verified.** The LXX of Job does **not** carry the Ps 44 links into Greek. Job 13:24 has διὰ τί ἀπ᾽ ἐμοῦ κρύπτῃ, where Ps 43:25 has ἵνα τί τὸ πρόσωπόν σου ἀποστρέφεις. And Rahlfs **asterisks** Job 14:12c (καὶ οὐκ ἐξυπνισθήσονται ἐξ ὕπνου αὐτῶν). That colon, the one nearest to Ps 44:24, is therefore a hexaplaric supplement and absent from the Old Greek [T]. The link belongs to the Hebrew.
- [T] **Isa 50:8–9 ~ Job 13:18–28 (convergence check). This link is stronger than proposed.**
  - ריב + צדק within two verses occurs only at Isa 50:7–8, Job 9:2, Job 13:18–19 and Job 33:12.
  - ריב + צדק + עָשׁ ("moth") within an eleven-verse window occurs only in Isa 50 and Job 13:18–28.
  - בלה ("wear out") + עָשׁ occurs only in Isa 50:9 and Job 13:28.
  - בֶּגֶד + עָשׁ + אכל occurs only in Isa 50:9, Isa 51:8 and Job 13:28 (all WLC).
  - The wording is close too: Job 13:19 מִי־הוּא יָרִיב עִמָּדִי sits beside Isa 50:8 מִי־יָרִיב אִתִּי and Isa 50:9 מִי־הוּא יַרְשִׁיעֵנִי. In the LXX (Swete/Rahlfs), Job 13:19 τίς… ὁ κριθησόμενός μοι matches Isa 50:8 τίς ὁ κρινόμενός μοι.
- [T] Rom 8:33–34 (θεὸς ὁ δικαιῶν· τίς ὁ κατακρινῶν) echoes Isa 50:8–9 LXX. It shares no distinctive vocabulary with LXX Job 13 beyond the τίς-plus-judging-verb pattern.

**Baseline.**
- Exclusive-pair counts for the Job verses are low: 13:24 = 1 (to Ps 55:13), 14:12 = 1 (to Zech 4:1), 13:9 = 0 (maxfreq 400). All are below the Job 4 mean of 2.1.
- At pair level, Job shares only one exclusive pair with all of Ps 44 (Job 38:15–Ps 44:4). The Ps 44 links therefore do **not** come from ordinary pair noise. They are a verbatim phrase, a unique triad, and a unique three-verse window.
- Lemma frequencies (WLC verses): תַּעֲלֻמוֹת 3; קיץ 22; ישׁן 21; שֵׁנָה 23; עור 65; סתר 80; חשׁב 122; חקר 26.
- In a scan of skeletal trigrams, Job has 195 verse-pairs that share a trigram attested at most twice outside Job, and most of these are function-word strings. A content trigram with a single partner is uncommon, so the cluster is well above chance.

**Rival sources.**
- **For 13:24: Ps 88:15** (לָמָה יְהוָה תִּזְנַח נַפְשִׁי תַּסְתִּיר פָּנֶיךָ מִמֶּנִּי). It shares the interrogative, סתר + פָּנִים and חשׁב (Ps 88:5, נֶחְשַׁבְתִּי), and its register (an individual near Sheol, 88:11 "will the shades rise (יָקוּמוּ)?") is arguably closer to Job 14. But it is not verbatim, and it has no "awake/sleep" cluster. The other "hide your face" texts (Ps 13:2; 27:9; 69:18; 102:3; 143:7) are imperatives or "how long", not "why", and Ps 10:1 uses עלם. **Ps 88 is a real secondary rival, not an equal one.**
- **For 14:12:** Jer 51:39, 57 shares the phrase לֹא יָקִיצוּ ("they will not wake"; the phrase also occurs in 1 Sam 12:17, Eccl 11:4 and Isa 59:1 in other senses), plus שְׁנַת (sleep) and ישׁן, in a death-as-endless-sleep sense that is **closer in meaning** to Job 14:12 than Ps 44:24 is. Zech 4:1 shares the exact clause יֵעוֹר מִשְּׁנָתוֹ ~ Job's יֵעֹרוּ מִשְּׁנָתָם (the only two hits, WLC), though as an ordinary simile. Isa 26:19 (קום + קיץ + dust) and Dan 12:2 (sleepers in dust shall awake) are the canonical **antitheses**, not sources.
- [I] The best description is that Job 14:12 inverts Ps 44:24's call to God ("Arouse… awake") into human death-sleep ("will not awake… nor be aroused"), using a death-sleep idiom it shares with Jer 51.

**Hays criteria.**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | Both are canonical; their relative dates are unknown; direction left open |
| Volume | Strong | Unique three-word verbatim phrase (13:24); unique עור + קיץ + sleep triad (14:12); unique חשׁב + סתר + פנים window |
| Recurrence | Strong | Ps 44:22, 23, 24, 25 all recur, across Job 11 (Zophar) and Job 13–14 (Job) |
| Thematic coherence | Strong | The protest of the innocent (Ps 44:18–22) answers Job 13:18–23 |
| Historical plausibility | Possible | Use of the Psalter's lament language in a wisdom dialogue is plausible; nothing decides direction |
| History of interpretation | Not checked | — |
| Satisfaction | Strong | The community's "Awake, Lord!" becomes "man will not awake"; "counted as sheep" becomes "counted as Your enemy" |

**Verdict.** Confirmed with nuance.

**Final rating.** High on the words. Moderate–high for Ps 44 as a source. The Romans convergence is moderate at most, and only as a synthetic observation.

**Reasoning.** The Ps 44 link is better than proposed: Job 13:22–24 takes up Ps 44:23 *and* 44:25, and 14:12 inverts 44:24. Two parts of the claim need trimming. The dust/rise and חקר links are weak, and 14:12 shares its death-sleep sense with Jer 51:39, 57. The link also does not survive into the Old Greek: 13:24 is rendered differently, and 14:12c is a hexaplaric plus. On the convergence, Job 13 provably uses both Ps 44 and Isa 50:8–9 (the Isa 50 cluster is strong), and Paul provably uses both. Nothing shows that Paul had Job in view, so the "triangle" is the reader's construction.

**What a preacher may safely say.** "Job borrows the very words of Psalm 44, the lament of God's faithful people suffering though they had not forgotten Him: 'Why do You hide Your face?' Paul quotes the same psalm in Romans 8:36."

**Book-overview action.** Add **Ps 44:23–25 → 13:24; 14:12** (high words; moderate–high source), with Zophar's 11:6, 11 as a minor echo; state the Romans 8 convergence as the reader's synthesis, not as Job's design.

---

### C2: Psalm 107:40–42 divided between Eliphaz and Job

**Source:** #38 · 4:1–5:27 dig, Tool 11 (and the 9:1–10:22 dig on 12:21, 24 by anticipation)

**Claim (as tested).** Job 5:16b reproduces Ps 107:42b. Ps 107:41 lies behind Job 5:11 and 5:15. Job 12:21a and 12:24b quote Ps 107:40 word for word. Two speakers thus take adjacent verses of one psalm, as with Deut 32:39 (Eliphaz 5:18 / Job 10:7), and this is proposed as a design.

**Evidence.**
- [T] **Job 12:21a = Ps 107:40a** (שׁוֹפֵךְ בּוּז עַל־נְדִיבִים, "He pours contempt on nobles"). The only difference is plene שׁוֹפֵךְ against defective שֹׁפֵךְ. **Job 12:24b = Ps 107:40b** (וַיַּתְעֵם בְּתֹהוּ לֹא־דָרֶךְ, "and makes them wander in a pathless waste"), letter for letter. **Verified.** Job splits *one* psalm verse across two cola three verses apart. Job 12:21 alone carries three exclusive pairs to Ps 107:40 (WLC), among the eight strongest verse-to-verse links between Job and any other book.
- [T] **Job 5:16b ≈ Ps 107:42b.** עַוְלָה + קפץ + פֶּה occurs only in Job 5:16 and Ps 107:42 (WLC). **Verified.** קפץ + פֶּה adds Isa 52:15. Job has the by-form וְעֹלָתָה and lacks כָּל. In the Greek (Swete = Rahlfs) the verb is the same: Job 5:16 ἀδίκου δὲ στόμα ἐμφραχθείη, Ps 106:42 ἀνομία ἐμφράξει τὸ στόμα αὐτῆς. Here the link survives into the LXX.
- [T] **Job 5:11 ~ Ps 107:41.** שׂגב + אֶבְיוֹן in one verse occurs only in Ps 107:41. **No Job verse contains both**: Job distributes them over 5:11 (שָׂגְבוּ) and 5:15 (אֶבְיוֹן). The stated co-occurrence therefore holds only as a cross-verse correspondence. A better verse-level link exists, which the claim missed: **שׂגב + שׂים occurs only in Job 5:11 and Ps 107:41** (WLC). Job 5:11 has לָשׂוּם… שָׂגְבוּ, and Ps 107:41 has וַיְשַׂגֵּב… וַיָּשֶׂם. Frequencies: שׂגב 20 verses, אֶבְיוֹן 58.
- [T] **Not in the claim: a further Eliphaz echo.** Job 22:19 יִרְאוּ צַדִּיקִים וְיִשְׂמָחוּ ("the righteous see and are glad") ≈ Ps 107:42a יִרְאוּ יְשָׁרִים וְיִשְׂמָחוּ. Ps 69:33 is a looser parallel. So Eliphaz uses **both halves** of Ps 107:42 (5:16 and 22:19) [I, moderate].
- [T] Job 12:22–25 has further, weaker contacts with Ps 107: צַלְמָוֶת ("deep darkness"; Ps 107:10, 14), חֹשֶׁךְ and כַּשִּׁכּוֹר ("like a drunkard"; Ps 107:27). Isa 19:14 is the only verse besides Job 12:25 that pairs תעה with שִׁכּוֹר.
- [T] **The proposed parallel pattern.** מחץ + רפא occurs only in Deut 32:39 and Job 5:18 (Eliphaz). Job 10:7 וְאֵין מִיָּדְךָ מַצִּיל ≈ Deut 32:39 וְאֵין מִיָּדִי מַצִּיל, which Isa 43:13 also shares. **Verified.**

**Baseline (design claim).**
1. **Single exclusive pairs (maxfreq 400).** Job shares 162 exclusive pairs with 78 different psalms. In **16 of those 78 psalms**, two different speakers (narrator excluded) hit verses no more than two apart. A permutation test that shuffled Job verses among the links (2,000 runs) gave a mean of 13.3, with P(≥16) ≈ 0.13. At maxfreq 700 the figures were 23 of 91, mean 19.7, P ≈ 0.12. **At this level the "adjacent verses split between speakers" pattern is ordinary.**
2. **Strong links (≥2 exclusive pairs to the same verse).** There are 43 such Job-verse/target-verse links across the whole Hebrew Bible, and **none** forms a cross-speaker adjacent split. (Job 5:16 enters through a triad, not two pairs.)
3. **Rare verbatim trigrams (attested at most twice outside Job).** There are 6 cross-speaker adjacent splits. Only two are substantive:
   - Ps 8:5 (Eliphaz 15:14 / Job 7:17, the same verse)
   - Ps 107:40–42 itself.

   Ps 40:13 (Eliphaz 5:9 / Job 9:10) is really Job repeating Eliphaz, and the others are function-word strings.

So what is distinctive about Ps 107 is that **both sides are verbatim**, not that they are adjacent. The phenomenon of rival speakers handling the same text recurs (Deut 32:39; Ps 8:5; Ps 107), but adjacency is not its defining feature.

**Rival sources.** 1 Sam 2:7–8 and Ps 113:7–8 share with Job 5:9–16 only דַּל + אֶבְיוֹן, a stock pair found in 9 verses (WLC). They have no שׂגב and no verbatim wording, though 1 Sam 2:7 (מַשְׁפִּיל אַף־מְרוֹמֵם) is thematically close to 5:11. For the wording of 5:11a (שְׁפָלִים לְמָרוֹם), **Isa 57:15** is the lexical rival: שׁפל + מָרוֹם occurs only in Isa 57:15 and Job 5:11. **Neither rival outranks Ps 107**, which alone gives a verbatim cola match plus שׂגב + שׂים.

**Hays criteria.**

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | Both are canonical; their relative dates are unknown; direction open |
| Volume | Strong | Two verbatim cola (12:21a, 24b); a unique triad (5:16b); a unique pair (5:11) |
| Recurrence | Strong | Ps 107:40, 41, 42 (twice, counting 22:19), plus weaker contacts in Job 12:22–25 |
| Thematic coherence | Strong | Eliphaz takes the psalm's comfort for the poor; Job takes its overthrow of rulers, and omits the comfort |
| Historical plausibility | Possible | Plausible, but undecidable |
| History of interpretation | Not checked | — |
| Satisfaction | Strong for the words; Possible for the "design" | The contested reading is illuminating; the adjacency design does not beat chance as a type |

**Verdict.** Confirmed with nuance on the words. The design claim needs reframing.

**Final rating.** High on the words. The pattern is downgraded from moderate–high to **moderate**.

**Reasoning.** Every verbal link holds. Job 12:21a/24b and 5:16b are among the strongest verbatim contacts between Job and the Psalter. 5:11 is better grounded in שׂגב + שׂים than in the claimed שׂגב + אֶבְיוֹן, which are never in the same Job verse. As a type, "two speakers hit nearby verses of one text" happens by chance in about a fifth of psalms linked to Job. The pattern is meaningful here only because both uses are verbatim. It is better framed as "the friends and Job contest the same tradition" (cf. Deut 32:39; Ps 8:5) than as a planned adjacency design.

**What a preacher may safely say.** "Eliphaz and Job both use Psalm 107. Eliphaz takes its comfort ('unrighteousness must shut its mouth', 5:16; Ps 107:42), and Job takes its judgement on rulers ('He pours contempt on nobles', 12:21; Ps 107:40). Each hears in the same psalm what fits his case."

**Book-overview action.** Extend the existing **Ps 107:40** row to **Ps 107:40–42**: Eliphaz 5:11, 5:16; 22:19 · Job 12:21, 24 (high on words). Carry the adjacency design at moderate, under "the friends and Job contest the same texts".

---

### C3: The canon's reply to Eliphaz's "Who ever perished being innocent?" (Job 4:7)

**Source:** #39 · 4:1–5:27 dig, Headline 4

**Claim (as tested).** Eliphaz's doctrine has canonical partners (צַדִּיק + אבד, where the wicked perish), and other texts contradict it: Isa 57:1, Mic 7:2 (יָשָׁר + אבד, shared only with Job 4:7) and Eccl 7:15. Eccl 7:15 is proposed as a handoff, because both Eliphaz and Qohelet appeal to רָאִיתִי ("I have seen"). נָקִי + אבד is proposed as unique to Job 4:7 and Jonah 1:14. This is offered as a canonical dialogue, not an allusion.

**Evidence.**
- [T] צַדִּיק + אבד occurs in exactly six verses: Ps 1:6; Prov 10:28; 11:10; 28:28; Isa 57:1; Eccl 7:15 (WLC). **Verified.** In the first four the *wicked* perish; in Isa 57:1 and Eccl 7:15 the *righteous* perish. **Job 4:7 itself does not contain צַדִּיק.** It has נָקִי and יְשָׁרִים.
- [T] יָשָׁר + אבד occurs only in Job 4:7 and Mic 7:2 (WLC). **Verified, but not significant.** At maxfreq 700, Job 4:7 has seven exclusive pairs, going to Mic 7:2, Jonah 1:14 (two), Mic 3:9, Ps 83:5, Isa 49:21 and Gen 37:16. That is above the Job 4 mean of about 2, and Mic 7:2 is one ordinary pair among them. Mic 7:2's subject is חָסִיד, which never occurs with אבד in Job, and its context is social collapse, not theodicy. Rahlfs has εὐλαβής where Swete has εὐσεβής: an edition divergence, not load-bearing.
- [T] נָקִי + אבד occurs only in Job 4:7 and Jonah 1:14 (WLC). **Verified, but irrelevant.** In Jonah the word means "innocent blood" (דָּם נָקִיא), and the sailors fear perishing *for* shedding it. The sense is different, so the link should be discarded as a dialogue partner.
- [T] **"I have seen."** In Job, the first-person perfect of ראה (רָאִיתִי) occurs only in Eliphaz's first speech, at 4:8 and 5:3 (WLC). That is a genuine mark of his speech. Across the Hebrew Bible it is a sapiential commonplace: Eccl 18 verses; Ps 37:25, 35; Prov 24:32. It is Qohelet's signature form, so it cannot point specifically to Eccl 7:15.
- [T] **Psalm 37 is closer to Eliphaz than Eccl 7:15 is.**
  - Ps 37:25 "I have not seen (לֹא רָאִיתִי) the righteous forsaken" restates Eliphaz's thesis.
  - Ps 37:35–36 "I have seen (רָאִיתִי) a wicked, violent man spreading like a luxuriant tree… and he was no more" matches Job 5:3 "I have seen (רָאִיתִי) the fool taking root (מַשְׁרִישׁ), and suddenly I cursed his dwelling" in structure.
  - Ps 37:37 pairs תָּם ("blameless") with יָשָׁר and the verb ראה, as Eliphaz pairs תֹם (4:6) with יְשָׁרִים (4:7). (תָּם + יָשָׁר: Job 1:1, 8; 2:3; Ps 37:37; Prov 29:10.)
  - But Ps 37 has **no exclusive lemma pair** with Job 4–5. It is a partner in genre and function, not a lexical source.
- [T] **Isaiah 57 is the strongest counter-voice lexically, and the claim underplays it.** Besides 57:1 (הַצַּדִּיק אָבָד), Isa 57:15 has two exclusive pairs with Eliphaz's first speech: דכא + שׁכן (only Isa 57:15 and Job 4:19) and שׁפל + מָרוֹם (only Isa 57:15 and Job 5:11). The LXX sharpens the contrast: Isa 57:1 Ἴδετε ὡς ὁ δίκαιος ἀπώλετο ("See how the righteous perished"; δίκαιος ἀπώλετο occurs only here in Swete) against Job 4:7 τίς καθαρὸς ὢν ἀπώλετο. Isaiah's "See!" answers Eliphaz's "I have seen" [I, Greek only].
- [T] **Eccl 7:15** (אֶת־הַכֹּל רָאִיתִי… יֵשׁ צַדִּיק אֹבֵד בְּצִדְקוֹ) shares with Job 4:7–8 only אבד and the common רָאִיתִי. It shares no exclusive pair with Job 4–5. Its "righteous who perishes" is the plainest canonical negation of Eliphaz's thesis.

**Baseline.**
- Job 4:7's seven exclusive pairs (maxfreq 700) make any single "only" pair from it unremarkable.
- Lemma frequencies (WLC verses): אבד 174; צַדִּיק 197; יָשָׁר 119; נָקִי 42; ראה 1,205. These are common words.
- The counter-voice texts do not cluster on Job 4:7 itself. The one cluster that does exceed chance is Isa 57:1 + 57:15 against Job 4:7, 4:19 and 5:11: three points of contact with one speech from one short chapter.

**Rival sources.**
- For the Eliphaz side of the "dialogue", Ps 37 (wisdom psalm; "I have seen"; תָּם/יָשָׁר) is a closer partner than Ps 1 or Proverbs.
- For the counter-voice, Isa 57:1, 15 outranks both Mic 7:2 and Eccl 7:15 on lexical evidence. Eccl 7:15 remains the clearest on thesis.

**Hays criteria** (scored as if for an allusion, to test whether that framing could be justified).

| Criterion | Score | Reason |
|---|---|---|
| Availability | Possible | All are canonical; dates uncertain; direction open |
| Volume | Weak | Common lemmas only; יָשָׁר + אבד is at the chance level; no verbatim phrase with Mic, Eccl or Jonah |
| Recurrence | Weak (Possible for Isa 57) | Only Isa 57 recurs (vv. 1, 15) |
| Thematic coherence | Strong | The thesis "the innocent never perish" is explicitly contradicted by Isa 57:1 and Eccl 7:15 |
| Historical plausibility | Weak (as a handoff) | Nothing on the page links Ecclesiastes to Job 4 specifically |
| History of interpretation | Not checked | — |
| Satisfaction | Strong as a reader's dialogue; Weak as an authorial allusion | — |

**Verdict.** Needs reframing.

**Final rating.** Moderate for a canonical dialogue that the reader builds. High that the canon contains both voices. **Low–moderate** for Eccl 7:15 as a handoff. Discard Jonah 1:14.

**Reasoning.** All the counts are correct, but they do not carry the weight placed on them. יָשָׁר + אבד is one of seven chance-level exclusive pairs in Job 4:7. נָקִי + אבד in Jonah has a different sense. רָאִיתִי is a wisdom commonplace and is Qohelet's own signature. On the Eliphaz side, Ps 37 is the closer partner. On the counter side, Isa 57 is the only text with a lexical cluster against Eliphaz's speech. The dialogue should be described as thematic and reader-constructed, with Isa 57:1 and Eccl 7:15 as its two clearest counter-voices, not as an allusion or a handoff.

**What a preacher may safely say.** "Eliphaz asks, 'Who ever perished being innocent?' (4:7). Scripture itself answers. Isaiah says, 'The righteous man perishes, and no man takes it to heart' (Isa 57:1), and the Preacher says, 'there is a righteous man who perishes in his righteousness' (Eccl 7:15)."

**Book-overview action.** No map row (this is a reader's canonical dialogue, not an allusion). If the trap or Christology sections cite it, lead with **Isa 57:1, 15**; Eccl 7:15 as thesis only; Ps 37 as Eliphaz's partner; Jonah 1:14 discarded.

---

## Spot Checks

The main session re-ran the evidence on which each verdict turns, from the same corpus but outside the auditors' sessions. **Twenty-three of the 24 checks reproduced the auditors' results exactly; the twenty-fourth (check 16) corrects one word of auditor B's and changes no verdict.** A note on method follows the table.

| # | Claim | Check (edition) | Result |
|---|---|---|---|
| 1 | A1 | The hidden face (סתר + פָּנִים) in Exodus | None in Exod 33; Exodus has only 3:6 (Moses hides *his own* face) (WLC) — reproduced |
| 2 | A1 | Job 9:11 in the Greek | παρέλθῃ stands in the line with יַחֲלֹף (Swete, Rahlfs) — reproduced |
| 3 | A1 | נקה ± 2 verses of חֶסֶד and עָוֹן | Includes Exod 20:5–7 and Deut 5:9–11 as well as Exod 34:7 / Num 14:18 (WLC) — reproduced |
| 4 | A1 | Ps 130:3 against Job 10:14 | אִם + שׁמר + עָוֹן in both (WLC) — reproduced |
| 5 | A2 | Exclusive pairs at Job 4:16 | 3 at maxfreq 400; 5 at 700, four of them to Num 12:8, Deut 4:12, 1 Kgs 19:12, Dan 8:15 (WLC) — reproduced |
| 6 | A2 | Dan 8:15 | עמד + נֶגֶד + מַרְאֶה only Dan 8:15 and Job 4:16 (WLC) — reproduced |
| 7 | A2 | "No … only a voice" in the Greek | ἀλλ᾽ ἢ … φωνη- only Deut 4:12 and Job 4:16 (Swete) — reproduced |
| 8 | A2 | αὔρα | Swete only 1 Kgs 19:12 and Job 4:16; **Rahlfs also Ps 106:29** (= MT 107:29 דְּמָמָה) — reproduced |
| 9 | A2 | Num 12:7 ~ Job 4:18 | עֶבֶד + אמן in adjacent source verses (WLC) — reproduced |
| 10 | A3 | מִיָּדִי / מִיָּדְךָ מַצִּיל | Deut 32:39; Isa 43:13; Job 10:7 (second person) (WLC) — reproduced |
| 11 | A3 | Job 4:10 teeth | Exclusive pair to Ps 58:7, not Deut 32:24 (WLC) — reproduced |
| 12 | A4 | בלג | Four verses: Amos 5:9; Job 9:27; 10:20; Ps 39:14 (WLC) — reproduced |
| 13 | A4 | חָדֵל (2310) against חדל (2308) | Ps 39:5 adjective; Job 7:16; 10:20; 14:6 verb (WLC) — reproduced |
| 14 | B1 | יצר in Job | Zero verses (WLC; positive control Isa 44:24 returned) — reproduced |
| 15 | B1 | יְהוֹלֵל | Isa 44:25; Job 12:17; Eccl 7:7 only (WLC, exact consonants) — reproduced |
| 16 | B1 | Ps 119:73 ~ Job 10:8 in the Greek | **Correction:** Swete Ps 118:73 reads Αἱ χεῖρές σου ἔπλασάν με καὶ ἡτοίμασάν με; Job 10:8 reads αἱ χεῖρές σου ἔπλασάν με καὶ ἐποίησάν με. The first clause agrees word for word, the second verb does not, so the agreement is partial, not "verbatim" as auditor B wrote. The Hebrew exclusivity stands |
| 17 | B3 | פדה + מָוֶת | Hos 13:14; Job 5:20 only (WLC) — reproduced |
| 18 | B3 | Swete Job 5:4 | καὶ οὐκ ἔσται ὁ ἐξαιρούμενος = Hos 5:14 word for word (Swete; Rahlfs agrees) — reproduced |
| 19 | B3 | Control-book rates | Hosea 71, Micah 181, Habakkuk 196 exclusive pairs per 1,000 verses (WLC) — reproduced |
| 20 | B4 | בֹּקֶר + צַלְמָוֶת; עשה + כִּימָה | Each only Amos 5:8 and one Job verse (24:17; 9:9) (WLC) — reproduced |
| 21 | B4 | Jer 13:16 against Job 3:9 | Four lemmas shared, exclusive to the pair (WLC) — reproduced |
| 22 | C1 | חשׁב + סתר + פָּנִים, three-verse window | Only Job 13:22–24 and Ps 44:23–25 (WLC) — reproduced; Rahlfs Job 14:12c marks καὶ οὐκ ἐξυπνισθήσονται ἐξ ὕπνου αὐτῶν with the hexaplaric asterisk — reproduced |
| 23 | C2 | שׂגב + שׂים; Job 22:19 | Only Job 5:11 and Ps 107:41; Job 22:19 ≈ Ps 107:42a (WLC) — reproduced |
| 24 | C3 | דכא + שׁכן; שׁפל + מָרוֹם | Each only Isa 57:15 and one Eliphaz verse (4:19; 5:11) (WLC) — reproduced |

**Note on method.** The helper's phrase search runs a second, *skeletal* pass (waw, yod and final *he* removed) so that a defective spelling cannot hide a verse. On two- and three-letter words that pass over-matches, so short exact phrases (check 15) were confirmed by exact consonants instead. No verdict depends on a skeletal-only hit.

---

## Summary

### Verdict count

| Verdict | Count | Claims |
|---|---|---|
| Confirmed | 0 | — |
| Confirmed with nuance | 6 | A2, A3, A4, B2, C1, C2 (words) |
| Needs reframing | 5 | A1, B1, B3, C3, B4 (design) |
| Discard | 0 | (sub-links discarded within claims: Jonah 1:14; רֶשֶׁף; the חדל link; the "two halves" design) |

**Counting convention.** B4 and C2 received split verdicts. Each is counted once, by the verdict on the part a sermon would lean on: C2 under "Confirmed with nuance" (the words carry the finding; the adjacency design is reframed), B4 under "Needs reframing" (the queue item claimed Amos as a live source across Job 3–10, and that is what is reframed; the 9:8b–9 link itself is confirmed with nuance). Read with their halves, the eleven claims hold thirteen sub-verdicts: eight confirmed with nuance and five needing reframing.

**The pattern.** No claim failed outright and no stated "only" proved false. Every claim that rests on **one or two verbatim or rare-anchored links** survived (Deut 32:39; Deut 28:29; Ps 39:14; Isa 50:8–9; Ps 44:23–25; Ps 107:40–42; the three revelation texts at 4:16). Every claim that rests on a **pattern or design** built from many ordinary pairs was reframed downwards (Hosea; Exod 33; Isa 44:24's two halves; Amos across 3–10; the adjacency of Ps 107; the canon's reply). This is the same result as the Matthew and Mark audits: synthetic, cross-passage claims fail at a far higher rate than single links.

### Confidence Change Propagation

| Claim (dig and place) | Previous | Revised | What changes downstream |
|---|---|---|---|
| Hosea as a live source behind Eliphaz (4–5 dig, Headline 3) | moderate–high (pattern) | **low–moderate** (pattern); moderate (three single echoes) | Headline 3 rewritten: Deuteronomy's Song and curses lead; Eliphaz speaks a pooled covenant-and-wisdom idiom (Deut 32; Lev 26; Prov 3 and 22; Ps 91), of which Hosea is one voice |
| The canon's reply to 4:7 (4–5 dig, Headline 4) | high | **moderate** (reader's canonical dialogue) | Headline 4 kept, but framed as "Scripture answers" for the reader, not as an allusion; Isa 57:1, 15 leads; Jonah 1:14 and Mic 7:2 drop out as evidence |
| Eccl 7:15 as a handoff (4–5 dig) | moderate–high | **low–moderate** | Use Eccl 7:15 as a thesis-level counter-voice only |
| Exod 33:19–34:7 behind 7–13 (9–10 and 13–14 digs) | moderate–high | **moderate** (Exod 34:6–7 formula tradition); **low** (Exod 33 theophany) | Drop the hidden-face and "passing by" theophany strand; 9:11 goes with 4:15 and 1 Kgs 19:11 |
| Isa 44:24 behind both creation hymns (9–10 dig, Tool 11 and Headline 3) | moderate | **low** (design); moderate–high (9:8a phrase) | Headline 3 stands on its own markers; the "two halves of Isa 44:24" sentence is withdrawn |
| Amos's doxologies as a live source, 3–10 (9–10 dig) | moderate–high | **moderate**; moderate–high for 9:8b–9 | Drop 3:4–9 and 9:27 / 10:20 from the Amos list; add 10:22 and 24:17 |
| Ps 107:40–42 divided as a design (4–5 dig) | moderate–high | **moderate** | Present as both sides contesting a shared text, not as planned adjacency |
| Ps 39 as a live source (9–10 dig) | high | **moderate–high** (whole psalm); high (39:14 → 10:20–21; 9:27) | Rest the finding on Ps 39:14; drop חדל, הוֹדִיעֵנִי and שׁמר + חטא as supporting links; add the moth (39:12 ~ 13:28) |
| Deut 32:23–25 cluster (4–5 dig) | moderate | **low–moderate** | Drop רֶשֶׁף; 6:4 shared with Ps 38:2–3; 4:10 goes with Ps 58:7 |
| Isa 50:6–9 (13–14 dig, Headline 2) | moderate–high | **moderate–high** (unchanged) | Ground the headline on 13:19 and 13:28; the "no helper" half of the inversion is [I] |
| Ps 44 (13–14 dig) | moderate–high | **moderate–high** source; high words (unchanged; strengthened) | Add Ps 44:23 ~ 13:24b; Romans 8 triangle stated as the reader's synthesis |
| Sinai–Horeb texts behind 4:12–18 (4–5 dig, Headline 2) | high / moderate–high | **unchanged** | Add Num 12:7 ~ 4:18; name Dan 8:15 as a rival for the standing figure |

### Recommended book-overview revisions

The overview's intertextual map was drafted before the Sermon 3 digs and holds none of these sources except Ps 107:40. These revisions are for the **Finalise pass**, not for an interim edit:

1. **Add rows (each with its audited rating):** Deut 32:39 → 5:18; 10:7 (**live**, high); Deut 28:29 → 5:14 (high); Num 12:6–8 + Deut 4:12 + 1 Kgs 19:11–12 → 4:12–18 (high words; moderate–high design); Ps 39:14 → 9:27; 10:20–21 (high; **live** with 7:19; 14:6; 13:28); Ps 44:23–25 → 13:24; 14:12 (high words); Isa 50:8–9 → 13:19, 28 (moderate–high); Isa 44:24 → 9:8a and Amos 4:13; 5:8 → 9:8b–9 (presented together as **the mosaic of 9:5–10**); Exod 34:6–7 formula tradition → 7:21; 9:28; 10:12–14; 13:23 (moderate).
2. **Extend the Ps 107 row** from 107:40 to 107:40–42: Eliphaz at 5:11, 5:16; 22:19; Job at 12:21, 24.
3. **Record as non-links or low:** Isa 44:24 as the design of both hymns; Exod 33 as the theophany behind 9:11 and 13:24; Hosea as a live source; Eccl 7:15 as a handoff; Jonah 1:14 as a partner to 4:7; Deut 32:24 רֶשֶׁף behind 5:7.
4. **Live-sources sentence:** add Deut 32, Ps 39 and Ps 44 to the list of live sources; add Prov 22 and Ps 91 as Eliphaz's idiom.
5. **A macro-pattern to carry forward at moderate confidence:** **the friends and Job contest the same texts** — Deut 32:39 (Eliphaz 5:18; Job 10:7), Ps 107:40–42 (Eliphaz 5:11, 16; 22:19; Job 12:21, 24), Ps 8:5 (Job 7:17; Eliphaz 15:14). It is the one design-level claim this audit leaves stronger than it found it, because each instance is verbatim. Test it again at the macro-synthesis.

### Recommended dig revisions

**4:1–5:27 dig.**

- **Headline 3** is the one headline this audit cannot let stand as written. Recast it: "Eliphaz lays the Song of Moses and the covenant curses over a man outside Israel who has not broken covenant" — Deut 32:39 and 28:29 high; the wider idiom pooled (Lev 26; Prov 3:11–12; 22:8, 22; Ps 91), with Hosea's three echoes (2:20; 13:14; 5:12) named as moderate and no longer as a source.
- **Headline 4:** keep the canonical dialogue but tag it [I], reader-constructed; lead with Isa 57:1 and add Isa 57:15 (the cluster against 4:19 and 5:11); add Ps 37 as Eliphaz's partner; drop Jonah 1:14 and Mic 7:2.
- **Headline 2:** stands; add Num 12:7 ~ 4:18 and the Dan 8:15 rival.
- **Tool 11:** replace שׂגב + אֶבְיוֹן with שׂגב + שׂים; add Job 22:19 ≈ Ps 107:42a and Hos 13:14 ~ 5:20; add Prov 26:13 for 4:10; mark the 32:23–25 cluster low–moderate.

**9:1–10:22 dig.**

- **Headline 3:** keep the two creation panels on their own structural markers; withdraw "the two halves of Isa 44:24"; add Ps 119:73 and Ps 139:13 for 10:8–12.
- **Tool 11:** reframe Exod 33–34 as the formula tradition (with Exod 20:5–7, Mic 7:18, Ps 32:5, Ps 130:3 as rivals); strike חדל from the Ps 39 list; trim the Amos list to 9:8b–9 plus 10:22 (and 24:17 outside the unit); add Job 10:7 ~ Deut 32:39.

**13:1–14:22 dig.**

- **Headline 2:** stands; ground it on 13:19 and 13:28; mark "he has no helper" as [I].
- **Tool 11:** add Ps 44:23 ~ 13:24b; name Jer 51:39, 57 and Zech 4:1 as rivals at 14:12, and record that 14:12c is a hexaplaric plus in the Greek; drop the Exod 33 hidden-face reading of 13:24.

**These are recommendations, not edits.** The three digs are left as delivered; the 4:1–14:22 unit dig will take these verdicts as `[S: audit]` input and say where it departs from the dig wording.

### New links surfaced by the audit

The auditors surfaced ten links the digs had not claimed. All are WLC-verified. Three were tested inside the eleven claims and count as audited (Job 22:19 under C2; Isa 57:15 under C3, which also closes that part of queue #41; Ps 44:23 under C1). The other seven have not been tested for rivals at the same depth: six enter the queue at the rating shown (#42–47), Ps 119:73 is filed with #17 (Ps 139:13–16), and the macro-pattern "the friends and Job contest the same texts" is queued as #48 for the macro-synthesis.

| Link | Evidence | Rating |
|---|---|---|
| Num 12:7 ~ Job 4:18 | עֶבֶד + אמן in the verse next to Num 12:8 | moderate |
| Deut 32:39 ~ Job 10:7 | וְאֵין מִיָּדְךָ מַצִּיל transposes וְאֵין מִיָּדִי מַצִּיל (also Isa 43:13) | high |
| Hos 13:14 ~ Job 5:20 | פדה + מָוֶת, only these two | moderate |
| Amos 5:8 ~ Job 24:17 | בֹּקֶר + צַלְמָוֶת, only these two; an inversion | moderate–high |
| Jer 13:16 ~ Job 3:9 | four lemmas, exclusive | moderate–high |
| Ps 119:73 ~ Job 10:8 | יָדֶיךָ + עשה + first person, exclusive; Greek partial | moderate–high |
| Isa 44:25 ~ Job 12:17 | Poel יְהוֹלֵל (also Eccl 7:7) | moderate |
| Ps 107:42a ~ Job 22:19 | "the righteous see and are glad" | moderate |
| Isa 57:15 ~ Job 4:19; 5:11 | דכא + שׁכן; שׁפל + מָרוֹם, each only these two | moderate–high (as counter-voice) |
| Ps 44:23 ~ Job 13:24b | חשׁב + סתר + פָּנִים in one three-verse window | high |

---

## Critical Assessment

The verdicts are sturdier than the digs' first ratings, but the audit has gaps of its own that a preacher should know.

**1. No history of interpretation.** Every Hays table records it as *not checked*. A link that the Targum, the rabbis or the Fathers already heard (or never heard) would move several ratings. For the Sermon 3 headlines that matter most (Isa 50; Ps 44; the Sinai–Horeb vision) one targeted check in Logos would be worth doing before the backbone.

**2. Direction of dependence is open everywhere.** No claim's evidence decides who borrowed from whom. The digs' wording "Job uses …", "Eliphaz quotes …" is therefore stronger than the audit can carry; "Job speaks in the words of …" is the safe form. Where the direction matters theologically (Isa 50 and the Servant; Ps 44 and Romans 8), the sermon should say "the same words" and not "Job quotes Isaiah".

**3. The baselines are lemma statistics on a proxy text.** They are WLC with a Strong's index, not BHS, and they cannot see phrasal or cross-verse links — the strongest link in the audit (Ps 39:14 → 10:20–21) scored zero on the pair statistic. A low baseline score is therefore not evidence against a phrase link; a high one is not evidence for a design.

**4. Rival searches are wide but not exhaustive.** The auditors searched by lemma and by phrase, with windows and control books, but they could not search by image or concept. A rival with different words for the same picture would not appear.

**5. The control-book method compares books of very different size and genre.** Micah's and Habakkuk's high rates partly reflect their brevity. The Hosea verdict does not hang on the rank alone (the rival exclusives at 4:8, 5:4, 5:17 and 5:18 carry it), but the rank should not be quoted on its own.

**6. One macro-claim is strengthened, and it has only three instances.** "The friends and Job contest the same texts" rests on Deut 32:39, Ps 107 and Ps 8:5. Three verbatim instances is suggestive, not a design. It should go to the macro-synthesis as a candidate, not into a sermon as a thesis.

---

## Queue and Triggers

**Queue updated.** The eleven audited items (#13–16, #23–24, #35–39) are marked with their verdicts in `claude/claim-audit-queue.md`. Item #30 (Hos 5:12 at 13:28) was tested inside B3 and is closed at moderate. Six new links are added as #42–47 and the macro-pattern as #48. Last audit: 3 October 2026; digs since: 0.

**Still queued (Job):** #1–12, #17–22, #25–29, #31–34, #40–41 and the new #42–48 — **36 items.** None of them carries a Sermon 3 headline.

**Triggers.**

- **Trigger 1 (about ten candidates, or three to four digs since the last audit):** the count limb is armed again by the backlog (36), but the digs-since limb is reset to 0. Recommendation: run the next audit after the 15:1–21:34 digs, or at the Finalise pass, whichever comes first, and give it the backlog by sermon.
- **Trigger 2 (a load-bearing allusion):** **satisfied for Sermon 3.** Every allusion carried by a Sermon 3 headline has now been audited. The backbone can take the verdicts as `[S: audit]`.
- **Trigger 3 (a Finalise pass):** not yet. The recommended overview revisions above are held for it.

---

## Colophon

**Audit:** Job claim audit 2 (the Sermon 3 set). **Date:** 3 October 2026. **Auditors:** three blind subagents, run in turn; spot checks by the main session.

**Corpus:** WLC (lemma-indexed) and BHS (Logos export) for Job; Swete LXX; Rahlfs–Hanhart (Logos exports, fourteen books); SBLGNT; NASB95 and ESV (Logos exports). Every count names its edition. Positive control (חֶסֶד in Job: 6:14; 10:12; 37:13) passed in all four sessions.

**Secondary sources:** none. History of interpretation not checked.

**Earlier audit:** `dig-deeper-job-claim-audit.md` (28 September 2026), not re-opened.

**Next:** the Job 4:1–14:22 unit dig, then the Sermon 3 backbone.
