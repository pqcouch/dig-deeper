# Claim Audit 4: Job

**Passages audited:** the Sermon 5 batch (Job 22:1–28:28): seventeen claims in three parts, with twenty rulings where a claim divides. They are the ten queued claims from the project's `claude/claim-audit-queue.md` (Job #45, #55, #92–99), plus seven claims the Sermon 5 material rests on. Those seven come from the book overview's contested judgements on the third cycle, the sweep's self-quotation table and the 28:1–28 dig's headlines.

- **Part A (Torah, the Prophets and the Psalter in Job 22–28):**
  - A1 Deuteronomy 8 with Ps 78 and Isa 48:21 behind the miner's strophe, 28:1–11 (#93);
  - A2 Isa 40:12–13 at 28:25 (#98);
  - A3 Isa 33:6 at 28:28 (#96);
  - A4 Amos 5:8 at 24:17 (#45);
  - A5 Isa 51:9 and 27:1 at 26:12–13 (#55);
  - A6 Deut 24:17 at 24:3 (sweep).
- **Part B (Proverbs, the motto and the gem list):**
  - B1 Prov 2:1–6 behind 28:20–28 (#92);
  - B2 Prov 8 and 3:13–20 behind 28:12–27, with the "circle" of 22:14 and 26:10 (overview);
  - B3 Ezekiel 28 and Exodus 28, the gem field at 28:15–19 (#97);
  - B4 the motto at 28:28 (Prov 1:7; 9:10; 15:33; Ps 111:10; Prov 3:7; 14:16; 16:6) (overview).
- **Part C (design and structure in Job 22–28):**
  - C1 the miner doing God's acts in miniature (#94);
  - C2 the ear and the eye (#95), and Eliphaz's "fear" (28 dig);
  - C3 the internal window test binding 28 to 22, 26 and 38 (28 dig);
  - C4 who speaks chapter 28, and the frame (#99);
  - C5 whether 24:18–25 and 27:13–23 are Job's words (overview);
  - C6 the third cycle's breakdown (overview);
  - C7 Eliphaz turning Job's words (21:14–16 → 22:17–18) and Job's answer (22:22 → 23:12) (sweep).

**Date:** 8 October 2026

**Revised:** 8 October 2026, v1.1. Every search is now stated in words: the original-language words in their own script with a gloss, the edition searched, and the result. The working shorthand of the earlier text (search-routine names, word-index numbers and script file names) has been removed. No verdict, count, rank or rating has changed (toolkit amendments round 8).

**Purpose:** to test the allusion, design and structure claims that would carry weight in the Sermon 5 unit dig and backbone, before they are used. The project plan required "the third-cycle claim audit first" for Sermon 5. Trigger 2 of the standing rule was armed by the 28:1–28 dig, four of whose seven headlines rest on unaudited claims (#92–95), with the speaker question (#99) belonging with 27:13–23.

**Primary texts:**

- **Hebrew:** WLC with its lemma and morphology index (the observation layer); BHS with apparatus (Logos export) for Job, which is what every paragraphing and apparatus finding below cites.
- **Greek Old Testament:** Swete LXX for the whole canon. Rahlfs–Hanhart exports (Logos) for Job, Genesis, Exodus, Numbers, Deuteronomy, Kings, Isaiah, Jeremiah, the Twelve, Psalms, Proverbs and Ecclesiastes.
- **New Testament:** SBLGNT with the MorphGNT index.
- **English:** NASB95 and ESV (Logos exports); NIV84 for Job. There is no English export for Ezekiel, so Ezekiel is paraphrased.

**Study text:** NASB95 · **Pulpit text:** ESV (Sermon 5 is in view)

**Warrant tags** in the auditors' parts: `[T]` derivable from the text; `[I]` a reasonable inference from it. History of interpretation was not checked (no commentaries were opened).

---

## Method

The method is that of claim audit 3: three blind auditors, a positive control, exclusive-pair baselines, rival searches, and **a Job-passage null for every window rank**. Two things are new.

**A faster ranker with a built-in null.** The 28:1–28 dig introduced a window ranker that ranks the 887 non-Job chapters of the Hebrew Bible by their best window against a Job passage and, for each candidate, counts how many other Job passages of the same length rank that chapter as high or higher. The auditors used it with stated window lengths (in verses) and frequency ceilings (the most verses a word may occur in and still count as rare), and re-ran each proposed rank under other settings to test its stability.

**Design and attribution tests.** Auditor C built chance baselines for every design claim and tested the attribution claims against the text's own markers: BHS paragraphing, speech formulas, person and address, a vocabulary profile, and the Greek with its asterisks.

**Three independent auditors.** Each was a fresh subagent. None had access to the book overview, the sweep, the Job digs (including the 28:1–28 dig whose claims were under test), the queue's reasoning, the earlier audits, or one another's work. Each was given its claims as proposals to break, with only the proposed rating attached. **They ran one after another, not in parallel.** Auditors A and B ran first; auditor C was interrupted by a session break before it wrote anything and was run again from the same brief, with its predecessor's scratch code available but every result re-run.

**The corpus in the cloud.** The `_texts/` corpus was staged into the session workspace. The auditors shared the search routines of claim audit 3, with the window ranker, a reader for the BHS text of Job and a reader for the English exports. Every auditor ran the positive control first (חֶסֶד ("lovingkindness") in Job: 6:14; 10:12; 37:13), and every claimed absence was preceded by a search that returned a known hit.

**Baselines.**

- **Exclusive pairs.** A Job verse has on average 1.34 content-lemma pairs that occur together in exactly one other verse of the Hebrew Bible (WLC; lemmas in at most 400 verses; 1.87 at a 700-verse cap). For chapters 22–28 the rate runs from 0.71 (ch. 23) to 1.96 (ch. 27); at the 700 cap from 1.40 to 3.00. A single exclusive pair proves little.
- **The window-rank null.** A proposed source counts only if its rank survives the null and small changes of window length and frequency ceiling. Where the shared words are a rare semantic field that no other Job passage uses (gems; rock and water), the null is weak, and the auditors said so.
- **Design baselines.** Auditor C compared Job 28 with other Job passages of the same length for each design claim (the miner's pairs with Job's hymns; the internal window test for every chapter; the distribution of nouns of similar frequency across Eliphaz's speeches; trigram repetition at every speech junction).

**For every claim, each auditor:** read the Job verses (WLC, BHS, Swete, Rahlfs, noting asterisks); read the source in context; verified every stated "only"; took baselines; searched for the strongest rival; scored the Hays criteria (or, for structure claims, a table of markers); and gave a verdict, a final rating and a line on what a preacher may safely say.

**Apparatus sigla.** Where the BHS apparatus is quoted, its Fraktur sigla are given in roman to keep the house fonts: G = the Greek, S = the Syriac, V = the Vulgate.

**Spot checks and independent rebuilds.** The main session re-ran the evidence on which the verdicts turn (26 checks), and rebuilt the two verdicts that change the 28:1–28 dig most (C3 and C4) with its own code (see Spot Checks).

---

## Positional Frame (Phase 0.6)

**What has the book set up that these claims serve?** The third round (22–27) begins with Eliphaz's harshest speech: he accuses Job of specific sins (22:5–9), turns Job's own words against him (22:17–18), and offers restoration if Job will lay his gold in the dust and take the Almighty as his gold (22:22–25). Job answers that he cannot find God (23:3, 8–9), describes the oppression the wicked commit unpunished (24), and hears a six-verse Bildad (25). Zophar does not speak. Job "takes up his discourse" again (27:1), swears his innocence, describes the wicked man's portion in words that open with Zophar's line (27:13 = 20:29), and then, with no paragraph break as BHS prints it, the wisdom poem begins (28).

The Sermon 5 claims under test say:

- that the third round is a breakdown the text itself registers, and that the passages that sound like the friends (24:18–25; 27:13–23) are, as the text stands, Job's;
- that chapter 28 lies within Job's discourse;
- that Job 24 speaks in the words of Deuteronomy's social law, Job 26 in the words of the sea-battle hymns, and Job 28 in the words of Israel's wilderness memory, Isaiah 40, Isaiah 33, Proverbs 2, 3 and 8, and the gem inventories;
- and that Job 28 is designed — the miner doing God's acts, the ear-to-eye line, Eliphaz's "fear" answered, and the poem as the meeting point of 22, 26 and 38.

**Why does this matter here?** These claims would shape what the Sermon 5 unit dig and backbone say. Several rest on window ranks or design patterns, the kinds of claim earlier audits found most prone to overreach. And four are headlines of a dig written in this same session, which makes a blind test more necessary, not less.

---

## Part A: Torah, the Prophets and the Psalter in Job 22–28

### Auditor's note

**Corpus.** Hebrew: WLC text and lemma index; BHS Job text and apparatus (the Logos exports), read directly. Greek OT: Swete (all books, LXX numbering) and the Rahlfs–Hanhart Logos exports for Job, Deuteronomy, Isaiah, Amos and Psalms. NT: SBLGNT. English: NASB95 exports (Job, Deuteronomy, Isaiah, Jeremiah, Proverbs, Amos; Psalms read directly from the export, English numbering). No web, no commentaries, no project or memory documents; no other part file opened.

**Rahlfs signs in the Job export.** In this export the dagger (†) is a colon divider (1,135 occurrences), not a metobelus. The asterisk opens a hexaplaric stretch and a separate metobelus sign closes it (212 asterisks, 135 metobeli); e.g. Job 1:6 "asterisk παραστῆναι ἐναντίον τοῦ κυρίου. metobelus". Not every colon inside a long stretch carries its own asterisk, so where an unmarked colon sits just before the metobelus I treat it as probably hexaplaric, and say so.

**Positive controls (run before every absence claim).**
- חֶסֶד ("covenant-kindness") in Job (WLC) returned 6:14; 10:12; 37:13 (required result).
- חַלָּמִישׁ ("flint") in Deuteronomy returned Deut 8:15; 32:13 (known hits) before testing חַלָּמִישׁ ("flint") elsewhere.
- The phrase נָחָשׁ בָּרִחַ / בָּרִיחַ ("fleeing serpent"), searched in both spellings, returned Isa 27:1 and Job 26:13 each time: the consonant search finds the defective spelling (Isa) and the plene spelling (Job).
- The two entries under which the WLC index files רַהַב ("Rahab") returned the two halves of the split (Isa 30:7; Job 9:13; 26:12 / Isa 51:9; Ps 87:4; 89:11), confirming the bridge is needed.
- Regex search for יִרְאַת + divine name was tested on Job 28:28 itself (returned) before being used for the "only" claim.

**Method.** For each claim: exact lemma co-occurrence (in one verse, within one verse either side, and with a root-bridged search that accepts any of the words sharing a root in each slot); consonantal confirmation where a phrase is claimed; exclusive-pair counts (words in at most 400 and 700 verses) for the key Job verses; window ranks against all 887 non-Job chapters, with the Job-passage null, at a stated window length and frequency ceiling; rival search by the window ranker on the Job passage and by targeted lemma searches; Greek read in Swete and Rahlfs for both Job and the proposed source.

**Baselines used.** The brief's figures (exclusive pairs of content words per verse, words in at most 400 [700] verses): Job 1.34 [1.87]; Job 24: 1.32 [2.28]; 26: 1.50 [2.07]; 28: 1.64 [2.36]. Exclusive pairs I computed for the key verses (words in at most 400 verses): Job 28:2 = 0; 28:9 = 1 (with Ps 114:8); 28:10 = 0; 28:25 = 1 (with Lev 19:35); 28:28 = 2 (Isa 29:14; Isa 10:13); 26:12 = 2 (Isa 50:2; 1 Kgs 5:9); 26:13 = 3 (Isa 27:1; Judg 13:25, a homograph artefact; Prov 30:19); 24:3 = 1 (Deut 24:17); 24:17 = 3 (Isa 17:14; Ruth 3:14; Amos 5:8). So every claimed exclusive pair here is at or below the chance level for its chapter. What decides each case is clustering, a matching function and the absence of rivals.

**Limits.** The window ranker uses exact lemma numbers, so it cannot see root-level links across a lemma split (נְחֹשֶׁת / נְחוּשָׁה; מָדַד / מִדָּה; שָׁקַל / מִשְׁקָל; רַהַב 7293 / 7294; סוג / נשׂג). Where this matters I add root-bridged searches. Ugaritic parallels are mentioned once, from my own knowledge, flagged [I] and not checked in the corpus. History of interpretation: Not checked throughout.

---

#### A1: Deuteronomy 8:6–15 (with Ps 78:7–20 and Isa 48:21) behind the miner's strophe, Job 28:1–11

**Claim (as tested).** The vocabulary of Israel's wilderness memory (Deut 8:9, 13–15; Ps 78:15–20; Isa 48:21) stands behind 28:1–11, with man the miner as the one acting. Proposed rating: wilderness rock-and-water tradition **moderate**; Deut 8 as a specific source **low–moderate**.

**Evidence**
- [T] Reproduced the reported ranks exactly (WLC, 10-verse windows): counting words in up to 800 verses, Deut 8:6–15 ranks 2nd of 887 against 28:1–11 (1 of 76 nulls as high), with Isa 30:21–30 1st (0 of 76). At a 150-verse ceiling, Ps 78:7–16 ranks 1st (0 of 76) and Deut 8:6 ranks 3rd (1 of 76). Against the whole of Job 28 (800-verse ceiling), Deut 8 ranks 9th (0 of 16) and Ps 78 4th (0 of 16).
- [T] What the Deut 8 window shares (words in at most 800 verses, WLC): חַלָּמִישׁ ("flint"), בַּרְזֶל ("iron"), צוּר ("rock"), שׁכח ("forget"), נַחַל ("wadi"), אֶבֶן ("stone"), לֶחֶם ("bread"), זָהָב ("gold"), כֶּסֶף ("silver"), הַר ("mountain"). Copper is *not* counted, because Job's נְחוּשָׁה and Deut's נְחֹשֶׁת (both "copper, bronze") are filed apart. What the Isa 30:21–30 window shares is spread across unrelated topics: idols of silver and gold, hailstones, fire, the "Rock of Israel", binding up wounds (חבשׁ). That window ranks highly because of common words, which confirms the claim's "diffuse".
- [T] Copper is a matter of Job's own usage. נְחוּשָׁה ("copper/bronze") occurs 10 times in the WLC, 4 of them in Job (20:24; 28:2; 40:18; 41:19). Job never uses נְחֹשֶׁת (0 hits). So the lemma difference is the book's habit and is no evidence against the link. But it also follows that iron + copper is stock vocabulary in Job: בַּרְזֶל ("iron") + נְחוּשָׁה in one verse occurs at Isa 45:2; 48:4; Lev 26:19; Mic 4:13; Job 20:24; 28:2; 40:18; 41:19.
- [T] The rivals for iron + copper (בַּרְזֶל + נְחֹשֶׁת in one verse, WLC) are 23 verses, among them Gen 4:22; Num 31:22; Deut 8:9; 28:23; 33:25; Josh 6:19, 24; Isa 60:17; Jer 6:28; Ezek 22:18, 20; 1 Chr 22:3, 14, 16; 29:2, 7. Add stone and only five verses remain: 1 Chr 22:14; 29:2; 2 Chr 2:13; Isa 60:17; Deut 8:9. The other four are inventories or exchanges. **Deut 8:9 is the only one in which stones yield iron and hills yield copper, that is, a statement about extraction from the earth.** It is also the only verse with אֶרֶץ ("land") + לֶחֶם ("bread") + אֶבֶן ("stone") (Deut 8:9 alone, WLC), and Job 28:5–6 has all three: "The earth, from it comes food … Its rocks are the source of sapphires." The suffixed form אֲבָנֶיהָ ("its stones") occurs in both Deut 8:9 and Job 28:6.
- [T] חַלָּמִישׁ ("flint") occurs in exactly 5 verses: Deut 8:15; 32:13; Isa 50:7; Job 28:9; Ps 114:8 (confirmed). **The only exclusive pair of Job 28:9 (words in at most 400 verses) is with Ps 114:8, not Deut 8:15.** חַלָּמִישׁ + הפך ("overturn") occur together only at Job 28:9 ("He overturns the mountains") and Ps 114:8 ("Who turned the rock into a pool of water, the flint into a fountain of water"). Ps 114:4, 6 also has mountains (הָרִים). The claim missed this.
- [T] בקע ("split") + צוּר ("rock") in one verse: only Isa 48:21, Job 28:10, Ps 78:15 (confirmed, and the same at ±1). Ps 78:16 has נְהָרוֹת ("rivers"), as does Job 28:11. Ps 78:20 has נְחָלִים ("streams") and לֶחֶם, and Job 28:4–5 has נַחַל and לֶחֶם.
- [T] The functions differ. In every wilderness text God splits the rock so that water comes out. In Job 28:10–11 *man* cuts channels (יְאֹרִים) in rock and "dams up the streams" to look for ore. The vocabulary is shared and the action is reversed.
- [T] שׁכח ("forget") is not a matching function. Job 28:4 הַנִּשְׁכָּחִים מִנִּי־רָגֶל means "forgotten by the foot" (NASB95), a remote shaft. Deut 8:11, 14, 19 means forgetting the LORD.
- [I, tested] Deut 8:6 ends וּלְיִרְאָה אֹתוֹ ("and to fear Him"), before the list of the land's riches. Job 28 ends with יִרְאַת אֲדֹנָי ("the fear of the Lord", 28:28) after its list of the earth's riches. Both chapters run from the earth's wealth to the fear of God, in mirror order. This is a thematic observation only; the lemmas differ (יָרֵא verb in Deut, יִרְאָה noun in Job).
- [T] Greek: Job 28:2 is unmarked in Rahlfs (Old Greek): σίδηρος μὲν γὰρ ἐκ γῆς γίνεται, χαλκὸς δὲ ἴσα λίθῳ λατομεῖται. Rahlfs Deut 8:9 reads γῆ, ἧς οἱ λίθοι σίδηρος … μεταλλεύσεις χαλκόν. The shared terms are γῆ, λίθος, σίδηρος and χαλκός. ἀκρότομος ("flint") occurs in Swete at Deut 8:15; Josh 5:2–3; 3 Kgdms 6:12; Ps 113:8 [114:8]; Job 28:9; 40:15; Sir 40:15; 48:17; Wis 11:4. **But in Rahlfs Job 28:9a (ἐν ἀκροτόμῳ ἐξέτεινεν χεῖρα αὐτοῦ) sits inside the asterisked stretch that opens at 28:5b and closes with the metobelus after 9a.** So the Old Greek probably lacked the flint line, and the ἀκρότομος echo is hexaplaric. The Old Greek 28:4b (unmarked) reads οἱ δὲ ἐπιλανθανόμενοι ὁδὸν δικαίαν ("those who forget the righteous way"): the Greek turns "forgotten" into a moral forgetting, which comes closer to Deut 8:11, 14 (ἐπιλάθῃ Κυρίου). I report this as data on reception in the Greek.

**Baseline.** Job 28:2 and 28:10 have no exclusive pairs (words in at most 400 verses). 28:9 has one, with Ps 114:8. The null is weak for this field: within Job, minerals and rock-and-water vocabulary occur almost only in chapter 28 (with a little in 22:24–25: gold, dust, rock, wadis, Ophir, silver). So the 0–1 of 76 null scores show that Deut 8 and Ps 78 *share Job 28's field*, not that either is the source. A fairer comparison is with other texts that use the field. Against 28:1–11 at an 800-verse ceiling, Deut 8 (2nd) beats Isa 60 (4th), Exod 17 (14th), Josh 6 (18th), Ps 105 (38th), Neh 9 (43rd), Ezek 28 (83rd), 1 Chr 29 (97th) and Num 20 (409th).

**Rival sources.** Ps 114:8 for 28:9 (flint + "turn"); Ps 78:15–16 and Isa 48:21 for 28:10–11 (split rock, rivers); Isa 60:17 and 1 Chr 22; 29 for the metals (inventories, no extraction); Job 22:24–25 inside the book (gold among the rocks of the wadis).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong (Torah and Psalter precede in canonical order) |
| Volume | Possible (no verbatim phrase; distinctive lemma cluster; copper by root only) |
| Recurrence | Possible (the wilderness-water texts recur in Ps 78, 105, 114; Isa 48) |
| Thematic coherence | Possible (riches of the earth set against fear of God; actions reversed) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.

**Final rating.** Wilderness rock-and-water tradition behind 28:9–11: **moderate**, with Ps 78:15–16, Ps 114:8 and Isa 48:21 the closest wording and Deut 8:15 one member of the group. Deut 8:9 behind 28:2, 5–6 (land, bread, stones, iron, copper): **low–moderate**. Its extraction framing is unique; the copper link is by root only.

**Reasoning.** The rare lemmas (flint; split + rock) really are concentrated in the wilderness-water tradition. But the tradition is spread over several texts, and for the flint line Ps 114:8 is closer than Deut 8:15. Deut 8:9 alone pictures metals dug out of the land, and that is the best argument for it as a specific source for 28:2. The null cannot separate "source" from "shared field", because no other Job passage talks about mining.

**What a preacher may safely say.** "Job 28 describes the miner in words Israel used for its wilderness memory: flint, split rock, streams, iron and copper from the land's stones. But here it is man who splits the rock, and what he cannot dig out is wisdom."

---

#### A2: Isaiah 40:12–13 at Job 28:25 (with Rom 11:33–35)

**Claim (as tested).** Job 28:25 ("When He imparted weight to the wind and meted out the waters by measure") speaks in the words of Isa 40:12–13 ("Who has measured the waters … marked off the heavens … weighed the mountains … Who has directed the Spirit of the LORD?"). Five roots are shared: מדד, מים, תכן, שׁקל, רוח. Proposed rating: **moderate**.

**Evidence**
- [T] תכן ("measure, regulate") occurs in 13 verses. תכן + רוּחַ ("wind/spirit") in one verse: Isa 40:13; Job 28:25; Prov 16:2 (confirmed). תכן + מַיִם ("water") in one verse: Isa 40:12 and Job 28:25 only. With all three within ±1: Isa 40:12–13 and Job 28:25 only.
- [T] Root-bridged search, because the lemmas are split (WLC): any weighing lemma (שָׁקַל 8254 / מִשְׁקָל 4948) + any measuring lemma (מָדַד 4058 / מִדָּה 4060 / מֵמַד 4461) in one verse gives Isa 40:12, Job 28:25 and Lev 19:35 (honest weights). Add מַיִם within ±1 and only **Isa 40:12 and Job 28:25** remain. Wind + water + any measuring or weighing root in a single verse: Job 28:25 alone, because Isa spreads them over vv. 12–13. The five-root count holds once the roots are bridged.
- [T] מִשְׁקָל and מִדָּה each occur only here in Job.
- [T] Function: in Isa 40:12–14 the rhetorical questions establish that no one measured alongside God or taught him (vv. 13–14 use דַּעַת "knowledge", תְּבוּנוֹת "understanding", דֶּרֶךְ "way"). Job 28:23–27 claims that God alone "understands its way" (הֵבִין דַּרְכָּהּ, 28:23) and shows it by his measuring of wind and water. So the same divine monopoly on measuring knowledge is at work in both.
- [T] Window rank (WLC, words in at most 150 verses): against 28:20–28 (9-verse windows) Isa 40 ranks **83rd** with 2 shared rare lemmas, and **18 of 46** nulls rank it as high. Against 28:23–27 (5-verse windows) it is 153rd (17 of 48). This fails the null. My parameters differ from the reported 52nd and 13 of 46, but the outcome is the same. The method cannot see this link, because the shared words are frequent (מַיִם, רוּחַ) or split across lemmas.
- [T] Greek: Job 28:25 is unmarked in Rahlfs (Old Greek): ἀνέμων σταθμὸν ὕδατός τε μέτρα. Isa 40:12 (Rahlfs/Swete): τίς ἐμέτρησεν τῇ χειρὶ τὸ ὕδωρ … τίς ἔστησεν τὰ ὄρη σταθμῷ. The two Greek texts share σταθμός ("weight, balance"), μετρ- ("measure") and ὕδωρ ("water").
- [T] Rom 11:34 reproduces Isa 40:13 LXX almost word for word (τίς … ἔγνω νοῦν κυρίου … σύμβουλος … ἐγένετο). Rom 11:35 (τίς προέδωκεν αὐτῷ, καὶ ἀνταποδοθήσεται αὐτῷ;) follows the *Hebrew* of Job 41:3 [Eng 41:11] (מִי הִקְדִּימַנִי וַאֲשַׁלֵּם, "who has given to Me that I should repay him?"), not the Greek of Job (Swete 41:2 / Rahlfs 41:3 τίς ἀντιστήσεταί μοι καὶ ὑπομενεῖ;). ἀνεξιχνίαστος occurs in Swete only at Job 5:9; 9:10; 34:24 and in Swete's Odes (8:6), and in the NT at Rom 11:33 and Eph 3:8 (confirmed). The Old Greek of Job 28:27 has the cognate ἐξιχνίασεν ("searched it out"), inside an asterisked stretch. Paul's doxology pairs Isa 40 with Job 41, not with Job 28. It is canonical reception that sets Isaiah 40 and Job side by side, not evidence for 28:25 in particular.

**Baseline.** Job 28:25 has one exclusive pair, words in at most 400 verses (מִדָּה + מִשְׁקָל with Lev 19:35), below the chapter's 1.64. The case rests on a four-root cluster that is unique (weigh + measure + water + תכן) and that no exclusive-pair or window measure can capture.

**Rival sources.**
- Prov 8:27–29 ranks **7th** against 28:20–28 (1 of 46 nulls). It shares a construction with Job 28:26: בַּעֲשֹׂתוֹ לַמָּטָר חֹק ("when He set a limit for the rain"), and Prov 8:29 בְּשׂוּמוֹ לַיָּם חֻקּוֹ ("when He set for the sea its boundary"). Both are ב + infinitive with suffix + ל + element + חֹק ("decree, limit"), and the regex search finds only Job 28:26, Prov 8:29 and one unrelated hit (1 Kgs 2:3). Job 28:27 הֱכִינָהּ ("He established it") also matches Prov 8:27 בַּהֲכִינוֹ.
- Jer 10:12–13 = 51:15–16 has wisdom, understanding, waters, wind and rain (rank 91; 10 of 46).
- Prov 30:4 has who-questions with wind and waters (rank 38; 7 of 46).
- So Isa 40:12 explains 28:25 (the measuring of wind and water) and Prov 8:27–29 explains 28:26–27 (decrees and establishing).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Strong (four to five roots in one to two verses, cluster unique to these places) |
| Recurrence | Possible (Isa 40 is in view again in Job 38:4–5: measurements, line) |
| Thematic coherence | Strong (God alone measures, so God alone knows) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible (one verse carries it) |

**Verdict.** Confirmed with nuance.

**Final rating.** **Moderate.** The root cluster is unique to these two places; the window method is blind to it.

**Reasoning.** The root-bridged search turns "five roots in two verses" into a cluster found nowhere else in the Hebrew Bible, and the function matches. The link is still one verse wide, and Prov 8:27–29 is the better parallel for 28:26–27. The direction of dependence is open; "speaks in the words of" is the right register.

**What a preacher may safely say.** "Job 28:25 uses Isaiah 40's language of God measuring the waters and weighing the wind. Both passages make the same point: the One who measures creation is the only one who knows where wisdom is."

---

#### A3: Isaiah 33:6 at Job 28:28 (syntax and treasure)

**Claim (as tested).** יִרְאַת יְהוָה הִיא אוֹצָרוֹ ("the fear of the LORD is his treasure", Isa 33:6) is the only other verse with יִרְאַת + divine name + הִיא + predicate, matching Job 28:28 יִרְאַת אֲדֹנָי הִיא חָכְמָה ("the fear of the Lord, that is wisdom"). Isa 33:6 also has חָכְמַת וָדַעַת ("wisdom and knowledge"), and its treasure motif matches Job's price strophe. Proposed rating: **moderate**.

**Evidence**
- [T] יִרְאַת followed directly by a divine name occurs in 27 verses (WLC normalised text). Followed by an independent pronoun as copula: only Isa 33:6, Job 28:28 and Prov 31:30. In Prov 31:30 יִרְאַת is the adjective 3373 ("a woman who fears the LORD"), a different construction. The syntactic claim is **confirmed**. The pronoun + חָכְמָה ("wisdom") sequence occurs only at Job 28:28.
- [T] BHS apparatus at 28:28: "ᶜ mlt Mss יהוה; pc Mss pr יהוה; > 2 Mss". Many manuscripts read יהוה for אֲדֹנָי. **אֲדֹנָי ("the Lord") occurs nowhere else in Job** (WLC: 28:28 only). If the יהוה reading were adopted, 28:28 would open יִרְאַת יְהוָה הִיא, identical to Isa 33:6 for three words. The apparatus also notes לָאָדָם ("to man") omitted in one manuscript, and הֵן ("behold") omitted in one manuscript and the Syriac.
- [T] יִרְאָה ("fear") + חָכְמָה in one verse: Isa 11:2; 33:6; Job 28:28; Prov 1:7; 9:10; 15:33; Ps 111:10 (seven, confirmed). Four of these say what Job 28:28 says: the fear of the LORD *is* the beginning, or the instruction, of wisdom (Prov 1:7; 9:10; 15:33; Ps 111:10). Isa 33:6 is the only one with Job's syntax, but its predicate is "his treasure", not wisdom.
- [T] Job 28:28b (וְסוּר מֵרָע בִּינָה, "and to depart from evil is understanding"): fear + turn + evil in one verse occurs at Job 1:1, 8; 2:3; 28:28; Prov 3:7; 14:16; 16:6; 1 Sam 12:20; Zeph 3:15. The strongest tie of the second half is inside Job, back to the prologue.
- [T] The treasure motif is conceptual only. Job 28 never uses אוֹצָר ("treasure"); its only Job occurrence is 38:22 (storehouses of snow). יִרְאָה + אוֹצָר in one verse: Isa 33:6 and **Prov 15:16** ("Better is a little with the fear of the LORD than great treasure"). Prov 15:16 has exactly the comparative logic of Job 28:15–19 (wisdom set above gold).
- [T] Window (WLC, words in at most 150 verses, 10-verse windows, against 28:12–28): Isa 33 ranks 5th but **8 of 41** nulls rank it as high. Its shared lemmas are שׁקל, בִּינָה, רַע, ספר, אָז, and are diffuse. Prov 8:10–19 ranks 2nd (0 of 41), Prov 3:14–23 8th (1 of 41) and Lam 4 9th (1 of 41): the price-and-wisdom texts beat Isa 33 under the null.
- [T] Greek: Job 28:28 is unmarked (Old Greek): ἡ θεοσέβειά ἐστιν σοφία, τὸ δὲ ἀπέχεσθαι ἀπὸ κακῶν ἐστιν ἐπιστήμη. θεοσέβεια ties back to Job 1:1 θεοσεβής. Rahlfs Isa 33:6: ἐκεῖ σοφία καὶ ἐπιστήμη καὶ εὐσέβεια πρὸς τὸν κύριον, οὗτοί εἰσιν θησαυροὶ δικαιοσύνης. The Greek of both verses shares the triad σοφία, ἐπιστήμη and -σέβεια, but the Greek of Isaiah has no "fear … is" identification. I report this as data.

**Baseline.** Job 28:28 has 2 exclusive pairs counting words in up to 400 verses (with Isa 29:14 and Isa 10:13) and 6 counting up to 700, which is about chapter level. A single construction shared by two verses, out of 27 verses with יִרְאַת + divine name, is a thin syntactic link. It is suggestive, not decisive.

**Rival sources.** For the formula: Prov 1:7; 9:10; 15:33; Ps 111:10. For the second half: Job 1:1, 8; 2:3; Prov 3:7; 16:6. For treasure: Prov 15:16; 2:4–5 ("seek her as silver … as hidden treasures; then you will discern the fear of the LORD"); Prov 3:14–15; 8:10–11, 19.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Possible (three-word identity only if the יהוה variant is read; predicate differs) |
| Recurrence | Weak (no other Isa 33 contact in Job 28) |
| Thematic coherence | Possible (fear of the LORD as the true valuable) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Weak (the wisdom formula and the prologue explain 28:28 more fully) |

**Verdict.** Needs reframing.

**Final rating.** Isa 33:6 as a specific source: **low–moderate**. "The fear of the LORD is wisdom" as the wisdom tradition's formula (Prov 1:7; 9:10; Ps 111:10) tied back to Job 1:1: **strong** as tradition.

**Reasoning.** The clause type is shared by Isa 33:6 and Job 28:28 alone, and the manuscript variant יהוה would sharpen it. But the content of 28:28 belongs to Proverbs' formula and to Job's own prologue, and every treasure parallel is closer in Proverbs (15:16; 2:4–5) than in Isaiah. Isa 33:6 is best treated as a syntactic companion, not a source.

**What a preacher may safely say.** "Job 28:28 brings us back to what Job was in chapter 1, a man who feared God and turned from evil, and to Proverbs' motto that the fear of the LORD is where wisdom begins. Isaiah, too, calls the fear of the LORD a treasure."

---

#### A4: Amos 5:8 at Job 24:17

**Claim (as tested).** בֹּקֶר ("morning") + צַלְמָוֶת ("deep darkness") occur together only at Amos 5:8 ("changes deep darkness into morning") and Job 24:17 ("the morning is the same to him as thick darkness"), as an inversion. Proposed rating: **moderate–high**.

**Evidence**
- [T] Confirmed: בֹּקֶר ("morning") + צַלְמָוֶת ("deep darkness") in one verse: Amos 5:8 and Job 24:17 (WLC), and the same within one verse either side. צַלְמָוֶת occurs in 17 verses, 10 of them in Job.
- [T] It is one of **three** exclusive pairs in Job 24:17 (words in at most 400 verses): בַּלָּהָה ("terror") + בֹּקֶר with Isa 17:14 ("At evening time, behold, there is terror! Before morning they are no more"); בֹּקֶר + נכר ("recognise") with Ruth 3:14; and בֹּקֶר + צַלְמָוֶת with Amos 5:8. Isa 17:14 is as exclusive as Amos 5:8 and closer in subject (terror, night predators gone by morning). Three pairs per verse is above the Job 24 average of 1.32, but each pair on its own is ordinary.
- [T] Window (WLC, words in at most 150 verses, 5-verse windows, against 24:13–17): Amos 5 ranks **45th** (6 of 48 nulls) with two shared lemmas (צַלְמָוֶת, אֶבְיוֹן). Rivals beat it. Isa 59:6–10 is 1st (1 of 48): נֶשֶׁף ("twilight"), נְתִיבָה ("path"), חֹשֶׁךְ ("darkness") and אוֹר ("light"); compare Isa 59:8–10 "the way of peace they do not know … their paths crooked … we hope for light, but behold, darkness … we stumble at midday as in the twilight" with Job 24:13, 15–16. Jer 13:12–16 is 2nd (0 of 48): נֶשֶׁף, צַלְמָוֶת, אוֹר. Isa 9:1 is 3rd (0 of 48).
- [T] Inside Job, the idea of God turning deep darkness to light is at 12:22 (וַיֹּצֵא לָאוֹר צַלְמָוֶת, "brings the deep darkness into light"). צַלְמָוֶת + אוֹר in one verse: Isa 9:1; Jer 13:16; Job 12:22. An "inversion" in 24:17 could as well invert Job 12:22. The commonplace that night-workers treat morning as their darkness is enough to explain the line without a source.
- [T] The Amos doxologies are present in Job, but at chapter 9. כִּימָה ("Pleiades") + כְּסִיל ("Orion") occur only at Amos 5:8; Job 9:9; 38:31. דֹּרֵךְ עַל־בָּמֳתֵי ("treads on the high places") occurs at Amos 4:13; Mic 1:3; Job 9:8 (plus Deut 33:29; Hab 3:19). הפך ("overturn") is in Job 9:5 and Amos 5:8. Window against Job 9:5–10 (6-verse windows, words in at most 150 verses): Amos 4 ranks 6th and Amos 5 7th, each with **0 of 51** nulls; Mic 1 ranks 44th (0 of 51). Amos 9 is weak (271st). Job 26 (tested under A5) and Job 38:31 are further contacts.
- [T] Greek: Rahlfs places Job 24:17 inside the asterisked stretch from 24:14b to 18a (asterisks at 14b, 15b, 15c, 16b, 16c, 17b; metobelus after 18a). **The Old Greek probably lacked 24:17.** The hexaplaric line ὅτι ὁμοθυμαδὸν τὸ πρωὶ αὐτοῖς σκιὰ θανάτου matches Rahlfs Amos 5:8 εἰς τὸ πρωὶ σκιὰν θανάτου (Swete Amos has only σκιάν). The Greek overlap belongs to the revision, not the Old Greek.

**Baseline.** Job 24 averages 1.32 exclusive pairs per verse (words in at most 400 verses), and 24:17 has three. The Amos pair is no more remarkable than the Isa 17:14 pair, and the window test fails the null.

**Rival sources.** Isa 59:8–10 and Jer 13:16 for the light/darkness/twilight complex of 24:13–17; Isa 17:14 for terror and morning; Job 12:22 internally. Job 38:12–15 (God commands the morning to shake out the wicked and withholds their light) is the book's own answer to 24:13–17.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Weak (two common-to-moderate words; no phrase) |
| Recurrence | Possible (Amos doxologies recur in Job 9:5–9 and 38:31) |
| Thematic coherence | Possible (inversion of a divine act into the habits of the wicked) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Weak (idiom, Isa 59 and Job 12:22 explain the line as well) |

**Verdict.** Needs reframing.

**Final rating.** Amos 5:8 at Job 24:17: **low** (possible echo). The Amos doxologies at Job 9:5–10: **moderate** (see New candidates).

**Reasoning.** The pair is real but sits at the chance level, the window test fails, and Isa 59:8–10 and Jer 13:16 are closer to the whole of 24:13–17. The Old Greek did not have the verse. Amos's hymn does stand behind Job, but the evidence for it is at Job 9:8–9, not 24:17.

**What a preacher may safely say.** "The Lord is the one who 'turns deep darkness into morning' (Amos 5:8; Job 12:22). Those who love the night turn that around and treat morning as their darkness (Job 24:17)." Present this as a contrast the preacher draws, not as a quotation in the text.

---

#### A5: Isaiah 51:9 and 27:1 at Job 26:12–13 (the sea monster)

**Claim (as tested).** (a) רַהַב ("Rahab") + חלל ("pierce") occur only at Isa 51:9 and Job 26:12–13, after bridging the 7293/7294 split. Proposed rating: **moderate–high (words)**. (b) נָחָשׁ בָּרִחַ ("fleeing serpent") occurs only at Isa 27:1 and Job 26:13. Proposed rating: **high**.

**Evidence**
- [T] (a) The split is confirmed: 7293 = Isa 30:7; Job 9:13; 26:12, and 7294 = Isa 51:9; Ps 87:4; 89:11. Bridged, Rahab + חלל 2490 in one verse gives Isa 51:9 only. **Job does not qualify "within one verse"**: Rahab is at 26:12 and חֹלֲלָה at 26:13. At ±1 the pair is Isa 51:9 and Job 26:12.
- [T] (a) The "only" fails at root level. Ps 89:11 [Eng 89:10] reads דִכִּאתָ כֶחָלָל רָהַב ("You Yourself crushed Rahab like one who is slain"), and חָלָל is the noun of the same root ("pierced, slain"), in the same verse as Rahab. Ps 89:10 [Eng 89:9] also has the sea ("You rule the swelling of the sea"). So three texts join sea + Rahab + the root חלל: Isa 51:9–10, Ps 89:10–11 and Job 26:12–13.
- [T] (a) The verbs differ. Job 26:12 מָחַץ ("shattered", 4272) + Rahab occurs only at Job 26:12. Isa 51:9 has הַמַּחְצֶבֶת ("who hewed", 2672), a different root.
- [T] Additional wording that strengthens Isaiah 51 but is not exclusive to it: רֹגַע הַיָּם ("stirs up the sea") in one verse is only Isa 51:15, Jer 31:35, Job 26:12. **The exact sequence בְּכֹחוֹ … וּבִתְבוּנָתוֹ ("by His power … by His understanding") occurs only at Jer 10:12, Jer 51:15 and Job 26:12** (Ps 147:5 has the two nouns unsuffixed). Jer 10:12 also has נָטָה ("stretched out") the heavens, and Job 26:7 has נֹטֶה צָפוֹן ("stretches out the north"). The BHS apparatus at Job 26:12 notes the ketiv ובתובנתו as a scribal error, with qere וּבִתְבוּנָתוֹ.
- [T] (b) Confirmed: נָחָשׁ ("serpent") + בָּרִיחַ ("fleeing") in one verse: Isa 27:1 and Job 26:13 (WLC). Consonant search finds both the plene spelling (Job בָּרִיחַ) and the defective one (Isa בָּרִחַ). Neither verse has an unpointed ketiv form. The other occurrence of בָּרִיחַ, Isa 43:14, means fugitives or bars. Job 26:13's exclusive pair (words in at most 400 verses) is with Isa 27:1.
- [I] (b) The Ugaritic Baal cycle names Lotan as *btn brḥ* … *btn ʿqltn* ("fleeing serpent … twisting serpent"), matching Isa 27:1's pair of epithets. This is from my own knowledge and not checked in the corpus. If correct, נָחָשׁ בָּרִיחַ is an inherited epithet, and two Hebrew texts sharing it need not depend on each other.
- [T] Windows (WLC, words in at most 150 verses): against 26:5–14 (10-verse windows), Isa 51 ranks 48th (9 of 44), Isa 27 158th (13 of 44), Ps 89 22nd (4 of 44), Jer 31 14th (2 of 44), Ps 104 24th (2 of 44). Against 26:10–13 (4-verse windows), **Jer 31:33–36 ranks 1st (0 of 41)**, sharing רגע ("stir"), אוֹר ("light") and חֹק ("decree": Job 26:10 חֹק־חָג; Jer 31:36 הַחֻקִּים). Isa 27 ranks 17th (1 of 41), Isa 51 135th (19 of 41), Ps 89 211th. The lemma splits handicap Isa 51 and Ps 89 here.
- [T] Greek: Job 26:12–13 is unmarked in Rahlfs (Old Greek; the metobelus closes after 26:11): ἐπιστήμῃ δὲ ἔτρωσε τὸ κῆτος ("by knowledge he wounded the sea-monster") … ἐθανάτωσεν δράκοντα ἀποστάτην ("he slew the rebel dragon"). Isa 27:1 (Rahlfs) has τὸν δράκοντα ὄφιν φεύγοντα: δράκων is shared, but Job's Greek does not render "fleeing" as Isaiah's Greek does. The Greek of Isa 51:9–10 (Swete) has no Rahab/dragon clause at all (οὐ σὺ εἶ ἡ ἐρημοῦσα θάλασσαν). So the Greek tradition gives no support to a textual link.

**Baseline.** Job 26 averages 1.50 exclusive pairs per verse. Job 26:13 has 3, one of them a homograph artefact (חלל "begin" in Judg 13:25), which shows how homographs produce exclusive pairs. The נָחָשׁ בָּרִיחַ pair is the exception: it is a two-word phrase, not two scattered lemmas.

**Rival sources.** Ps 89:10–11 (sea, Rahab, root חלל); Ps 74:13–14 (sea, dragons, Leviathan); Jer 10:12 = 51:15 (by His power … by His understanding); Jer 31:35 (stirs up the sea); Job 9:13 inside the book ("the helpers of Rahab").

**Hays criteria**

| Criterion | (a) Rahab pierced | (b) Fleeing serpent |
|---|---|---|
| Availability | Strong | Strong |
| Volume | Possible (root shared with Ps 89:11 too) | Strong (two-word phrase, only two places) |
| Recurrence | Strong (Rahab also Job 9:13; sea monster Job 3:8; 7:12; 40:25) | Possible |
| Thematic coherence | Strong (creation as victory over the sea) | Strong |
| Historical plausibility | Possible | Possible (shared epithet likely) |
| History of interpretation | Not checked | Not checked |
| Satisfaction | Possible | Possible |

**Verdict.** (a) Needs reframing. (b) Confirmed with nuance.

**Final rating.** (a) Job 26:12–13 shares a hymnic sea-battle idiom with Isa 51:9–15 and Ps 89:10–11, with phrasing also shared with Jer 10:12 and Jer 31:35: **moderate**, as idiom rather than text. (b) Lexical identity with Isa 27:1: **high**. As evidence of dependence on Isa 27:1 rather than a shared epithet: **moderate**.

**Reasoning.** Bridging the Rahab split is legitimate, but bridging roots also brings in Ps 89:11. Isa 51 then becomes one of three hymns that join sea, Rahab and piercing, and Job 26:12's opening "by His power … by His understanding" belongs to Jeremiah's doxology. "Fleeing serpent" is truly unique to Isa 27:1 and Job 26:13. Because it is most likely an inherited mythic epithet, it shows a shared stock of imagery more than borrowing.

**What a preacher may safely say.** "Job 26 praises God in the words Israel's hymns used for his victory over the sea: He shattered Rahab and pierced 'the fleeing serpent', Isaiah's name for Leviathan (Isa 27:1). Job is drawing on the same store of imagery as Isaiah and the Psalms."

---

#### A6: Deuteronomy 24:17 at Job 24:3

**Claim (as tested).** "Nor take a widow's garment in pledge" (לֹא תַחֲבֹל, Deut 24:17) lies behind "They take the widow's ox for a pledge" (יַחְבְּלוּ, Job 24:3). אַלְמָנָה ("widow") + חבל ("take in pledge") in one verse: only these two. Job 24:2–12 reads as a list of Deuteronomy's laws broken, and the landmark of 24:2 is conceptual only. Proposed rating: **moderate**.

**Evidence**
- [T] Confirmed: אַלְמָנָה ("widow") + חבל ("take in pledge") in one verse: Deut 24:17 and Job 24:3 (WLC), and the same within one verse either side. Including the Ezekiel noun חֲבֹלָה ("pledge") adds nothing.
- [T] **The link is a four-lemma cluster, not a single pair.** Deut 24:17 has נטה ("pervert"), יָתוֹם ("orphan"), חבל ("pledge") and אַלְמָנָה ("widow"). Job 24:3–4 has יְתוֹמִים, יַחְבְּלוּ, אַלְמָנָה and then יַטּוּ ("they push aside", 24:4). All four within ±1: **only Deut 24:17 and Job 24:3**. Without the pledge verb, orphan + widow + נטה gives Deut 24:17; 27:19; Isa 9:16; 10:2; Mal 3:5.
- [T] Window (WLC, words in at most 150 verses, 11-verse windows, against 24:2–12): **Deut 24:11–21 ranks 1st of 887** with 8 shared rare lemmas, and only 1 of 76 nulls ranks it as high. The shared lemmas are עֹמֶר ("sheaf": Deut 24:19 / Job 24:10), חבל (24:17 / 24:3, 9), קָצִיר ("harvest": 24:19 / 24:6), יָתוֹם (24:17, 19–21 / 24:3, 9), אַלְמָנָה (24:17, 19–21 / 24:3), אֶבְיוֹן ("needy": 24:14 / 24:4), עָנִי ("poor": 24:12, 14–15 / 24:9) and כֶּרֶם ("vineyard": 24:21 / 24:6). Against 24:2–4 (3-verse windows), Deut 24 is 4th (0 of 41). This is a full block of Deuteronomy's social law, not one verse.
- [T] Companion and rivals: Exod 22:19–29 [Eng 22:20–30] ranks 2nd (1 of 76): widow and orphan (22:21, 23), the pledged cloak (22:25), ox (22:29), poor (22:24), and כְּסוּת ("covering", 22:26 / Job 24:7). Ezek 18 ranks 12th (1 of 76). Job 24:9's only exclusive pair is with Ezek 18:16: robbing (גזל) + pledging (חבל). Ezek 18:7, 16 also has the hungry and the naked (cf. Job 24:10). Isa 10:1–2 is 22nd (4 of 76).
- [T] **The landmark of 24:2 is verbal, not merely conceptual.** The WLC files Job 24:2 יַשִּׂיגוּ under 5381 (נשׂג "overtake"), but the ketiv is ישיגו, the śin spelling of הִסִּיג ("move back", סוג 5253). With the boundary noun, the passages are Deut 19:14; 27:17; Hos 5:10; Prov 22:28; 23:10; Job 24:2. Landmark + orphan within ±1: **only Job 24:2–3 and Prov 23:10** ("Do not move the ancient boundary or go into the fields of the fatherless"). Landmark + widow within ±3: Deut 27:17 (with 27:19 widow and orphan), Job 24:2–3 and Prov 15:25. The claim understated 24:2.
- [T] On the homograph: 2254a covers "take in pledge" (Exod 22:25; Deut 24:6, 17; Amos 2:8; Ezek 18:16; Prov 20:16; 27:13; Job 22:6; 24:3, 9) and also "act corruptly / ruin" (Neh 1:7; Job 34:31; Isa 13:5; 32:7; 54:16; Mic 2:10; Song 2:15). In Job 24:3 the object (ox) and in 24:9 the preposition עַל ("against the poor") settle the sense as pledge.
- [T] Inside the book, Job 22:6–9 is Eliphaz's charge against Job. It uses the same field: תַחְבֹּל ("you have taken pledges"), garments, the naked, widows, orphans. Pledge + garment (חבל + בֶּגֶד) in one verse: Deut 24:17; Job 22:6; Amos 2:8; Ezek 18:16; Prov 20:16; 27:13. In ch. 24 Job describes others doing what Eliphaz accused him of.
- [T] Greek: Job 24:3 is unmarked (Old Greek): ὑποζύγιον ὀρφανῶν ἀπήγαγον καὶ βοῦν χήρας ἠνεχύρασαν. Job 24:4 has ἐξέκλιναν ἀδυνάτους. Rahlfs Deut 24:17: Οὐκ ἐκκλινεῖς κρίσιν προσηλύτου καὶ ὀρφανοῦ καὶ χήρας καὶ οὐκ ἐνεχυράσεις ἱμάτιον χήρας. The Greek of both shares ἐκκλίνω, ὀρφανός, χήρα and ἐνεχυράζω. Swete's Deut 24:17 lacks the pledge clause altogether, a manuscript difference to note when citing the LXX.

**Baseline.** Job 24:3 has exactly one exclusive pair (counting words in up to 400 or 700 verses), the one with Deut 24:17, against a chapter average of 1.32 [2.28]. On its own that would prove little. The window rank (1st, with 1 of 76 nulls) and the four-lemma cluster are what lift it.

**Rival sources.** Exod 22:20–26 (companion law); Ezek 18:7, 16 (for 24:9–10); Prov 23:10 (for 24:2–3a); Deut 27:17–19 (landmark and widow/orphan curses together).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong |
| Volume | Strong (four-lemma cluster in one to two verses, unique to the pair) |
| Recurrence | Strong (Deut 24:10–21 block; also Deut 19:14 / 27:17 at 24:2; Job 22:6–9) |
| Thematic coherence | Strong (catalogue of protected persons wronged) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Strong |

**Verdict.** Confirmed with nuance. The link is stronger than proposed, and the source is the law of the vulnerable rather than one verse.

**Final rating.** **Moderate–high** for Job 24:2–12 speaking in the words of Deuteronomy's social law (Deut 24:10–21, with 19:14 / 27:17 at 24:2), with Exod 22:20–26 as companion. Deut 24:17 at 24:3 specifically: **moderate–high**.

**Reasoning.** What first looked like a single exclusive pair turns out to be a four-lemma cluster, and the whole Deut 24 block ranks first of 887 chapters and beats the null. The landmark verb is the same as Deuteronomy's once the śin spelling is recognised. Exod 22 and Ezek 18 share parts of the field, so "the law of the vulnerable" is the safest description of the source.

**What a preacher may safely say.** "Job 24 reads like Deuteronomy 24 broken line by line: boundaries moved, the orphan's donkey driven off, the widow's ox taken in pledge, the needy pushed off the road. These are the very people the law told Israel to protect."

---

### New candidates surfaced

1. **Job 9:5–10 and the Amos doxologies (Amos 4:13; 5:8).** כִּימָה + כְּסִיל ("Pleiades + Orion") occur only at Amos 5:8; Job 9:9; 38:31. דֹּרֵךְ עַל־בָּמֳתֵי ("treads on the high places") at Amos 4:13; Mic 1:3; Job 9:8 (and Deut 33:29; Hab 3:19). הפך in Job 9:5 and Amos 5:8. Windows against Job 9:5–10 (6-verse windows, words in at most 150 verses): Amos 4 6th and Amos 5 7th, each with 0 of 51 nulls. Rating: **moderate**. This is where the "Amos doxology in Job" evidence actually lies.
2. **Jer 10:12 = 51:15 at Job 26:12 (and 26:7).** בְּכֹחוֹ … וּבִתְבוּנָתוֹ ("by His power … by His understanding") occurs only in these three verses. נטה ("stretch out") with the heavens or the north follows in both. Rating: **moderate**, as doxological idiom.
3. **Jer 31:35–36 at Job 26:10–12.** רֹגַע הַיָּם ("stirs up the sea"; only Isa 51:15, Jer 31:35, Job 26:12) with חֹק ("decree") and light and darkness. Window against 26:10–13 (4-verse windows): 1st, with 0 of 41 nulls. Rating: **low–moderate**.
4. **Ps 114:8 at Job 28:9.** חַלָּמִישׁ + הפך ("flint" + "turn/overturn") occur only in these two verses, and it is Job 28:9's only exclusive pair (words in at most 400 verses). Rating: **low–moderate**, as part of the A1 tradition.
5. **Prov 8:27–29 at Job 28:26–27.** ב + infinitive with suffix + ל + element + חֹק occurs only at Job 28:26 and Prov 8:29 (plus 1 Kgs 2:3, unrelated). הֵכִין ("establish") is in Job 28:27 and Prov 8:27. Window against 28:20–28: 7th (1 of 46). Rating: **moderate**. Refer to the Proverbs auditor.
6. **Prov 15:16 and 2:4–5 for the treasure motif of 28:15–28.** Fear of the LORD + אוֹצָר ("treasure") occurs only at Isa 33:6 and Prov 15:16, the latter as a "better than" comparison. Prov 2:4–5 has silver, hidden treasures and the fear of the LORD. Rating: **moderate** as a rival to Isa 33:6.
7. **Prov 23:10 at Job 24:2–3.** Landmark + orphan within ±1 occur only here and at Job 24:2–3, once the śin spelling of הִסִּיג is recognised. Rating: **moderate**.
8. **Isa 59:8–10 at Job 24:13–16.** "They do not know" the way, paths (נְתִיבוֹת), darkness for light, twilight (נֶשֶׁף). Window against 24:13–17: 1st (1 of 48). Rating: **low–moderate**.

### Key evidence for spot checks

1. Positive control: חֶסֶד ("covenant-kindness") in Job returns 6:14; 10:12; 37:13 (WLC).
2. חַלָּמִישׁ ("flint") + הפך ("turn"): Job 28:9 and Ps 114:8, and this is Job 28:9's one exclusive pair: flint + "turn" is shared with Ps 114:8, not Deut 8:15.
3. בַּרְזֶל ("iron") + נְחֹשֶׁת ("copper") + אֶבֶן ("stone"): 1 Chr 22:14; 29:2; 2 Chr 2:13; Deut 8:9; Isa 60:17. אֶרֶץ ("land") + לֶחֶם ("bread") + אֶבֶן: Deut 8:9 alone. נְחֹשֶׁת never occurs in Job; נְחוּשָׁה occurs at 20:24; 28:2; 40:18; 41:19.
4. Window rank against Job 28:1–11 (10-verse windows, words in at most 800 verses): Deut 8 2nd, its best window opening at 8:6 with 10 shared words, 1 of 76 nulls as high; Isa 30 1st, 0 of 76. At a 150-verse ceiling: Ps 78 1st, its window opening at 78:7 with 7 shared words, 0 of 76. Rahlfs Job 28:5b–9a is asterisked, with the metobelus after ἐν ἀκροτόμῳ ἐξέτεινεν χεῖρα αὐτοῦ.
5. Root-bridged search: "weigh" (שָׁקַל or מִשְׁקָל) + "measure" (מָדַד, מִדָּה or מֵמַד) + מַיִם ("water") within one verse either side: Isa 40:12 and Job 28:25. Window rank against Job 28:20–28 (9-verse windows): Isa 40 83rd with 2 shared words, 18 of 46 nulls; Prov 8 7th with 4, 1 of 46.
6. יִרְאַת ("fear of") + any divine name + הִיא / הוּא ("it is"), in the WLC text: Isa 33:6, Job 28:28, Prov 31:30 (the last parsed as the adjective יָרֵא, "fearing"). BHS apparatus Job 28:28 reads "ᶜ mlt Mss יהוה". אֲדֹנָי ("the Lord") occurs in Job only at 28:28.
7. Job 24:17 has three exclusive pairs (Isa 17:14; Ruth 3:14; Amos 5:8). Window rank against Job 24:13–17 (5-verse windows): Amos 5 45th, 6 of 48 nulls; Isa 59 1st, 1 of 48; Jer 13 2nd, 0 of 48. Rahlfs asterisks Job 24:14b–18a.
8. כִּימָה ("Pleiades") occurs at Amos 5:8; Job 9:9; 38:31, in each case with כְּסִיל ("Orion"). Window rank against Job 9:5–10 (6-verse windows): Amos 4 6th and Amos 5 7th, each 0 of 51 nulls.
9. Rahab + חלל: bridged, gives Isa 51:9 only in one verse, and Isa 51:9 with Job 26:12 at ±1. Ps 89:11 has רָהַב + כֶחָלָל ("like one slain", same root). נָחָשׁ ("serpent") + בָּרִיחַ ("fleeing"): Isa 27:1 and Job 26:13. כֹּחַ ("power") + תְּבוּנָה ("understanding"): Jer 10:12; 51:15; Job 26:12; Ps 147:5, with the exact suffixed pair only in the first three.
10. יָתוֹם ("orphan") + חבל ("take in pledge") + אַלְמָנָה ("widow") + נטה ("turn aside"), within one verse either side: Deut 24:17 and Job 24:3. Window rank against Job 24:2–12 (11-verse windows): Deut 24 1st, its window opening at 24:11 with 8 shared words, 1 of 76 nulls. The ketiv of Job 24:2 is גבלות ישיגו, the śin spelling of the landmark verb in Deut 19:14; 27:17.

---

## Part B: Proverbs, the motto and the gem list

### Auditor's note

**Corpus.** WLC Hebrew with its Strong's lemma index (observation layer); BHS Job and BHS apparatus (Logos exports) for Job 28:28; Swete LXX (all books); Rahlfs–Hanhart Job (Logos export); NASB95 exports for English quotation. There is no Ezekiel English export, so Ezekiel is paraphrased. Every count below names its edition. Hebrew references follow WLC versification; Psalms are given in Hebrew numbering with the English number in brackets.

**Positive control.** A search for חֶסֶד ("covenant-kindness") in Job (WLC) returned 6:14; 10:12; 37:13, as required. Before each reported absence I ran the same search on a verse known to contain the item:
- פְּנִינִים ("jewels, corals") returned Job 28:18 and Prov 8:11 before I ran the claimed exclusive co-occurrence with חָכְמָה ("wisdom").
- רַע ("evil") returns 623 verses when its homograph entries are searched together, against 234 and 101 for two of the entries alone, so the "fear + turn from evil" searches cover every רַע.
- The phrase סוּר מֵרָע ("turn from evil") returned all four Job verses (1:1, 1:8, 2:3, 28:28) before I used it on the rest of the Hebrew Bible.
- An exact-text search of the WLC for יִרְאַת אֲדֹנָי ("fear of the Lord") returned Job 28:28. The skeletal phrase search also gave 2 Sam 19:21 and 24:3, which are false hits (over-matching).

**Method.** (1) I re-ran every reported rank with the window ranker, using the stated window length and frequency ceiling. I then varied the window (3, 5, 7, 9 verses) and the ceiling (150, 400, 800 verses), because a rank 1 that does not survive these changes is fragile. (2) I listed the shared lemmas behind every top window. (3) I wrote a window scorer that merges cognates, because the WLC index splits several pairs that matter here: סלא / סלה ("weigh, value"), מָדַד / מִדָּה ("measure"), שָׁקַל / מִשְׁקָל ("weigh / weight"), קָצֶה / קָצָה ("end"), חֹק / חָקַק ("decree / inscribe"), and חוּג / חוּג ("circle", noun and verb). (4) I searched for rivals by verse partners, by window scores and by targeted lemma searches, in one verse and across neighbouring verses. (5) I read the Greek of Job in Swete and Rahlfs, and the Greek of the proposed sources in Swete.

**Baselines.** I used the brief's exclusive-pair rates (WLC, lemmas in up to 400 verses): Job overall 1.34 per verse; Job 28, 1.64. My spot checks: Job 28:16 has 4 exclusive pairs (two with Ezek 28:13, one with Ps 45:10, one with 28:19); Job 28:18 has 2 (Prov 8:11; Eccl 9:15); Job 28:28 has 2 (Isa 29:14; Isa 10:13), neither of them with Proverbs. A single exclusive pair is therefore at or below the chance rate.

**Limits.** I did not consult commentaries and did not check the history of interpretation. Window ranks count shared lemmas without weighting. The Job-passage null is weak wherever the shared vocabulary is a field that no other Job passage uses (gems; the wisdom refrain of 28:12/20). The Rahlfs Job export has 212 asterisks but only 135 metobeli, so some asterisked runs are ambiguous; this is noted where it matters.

---

#### B1: Proverbs 2:1–6 behind Job 28:20–28 (and 28:1–13)

**Claim (as tested).** Prov 2:4–6 (silver, hidden treasures, אָז "then", בין "discern", יִרְאַת יְהוָה "fear of the LORD", מצא "find", YHWH gives wisdom) lies behind Job 28:20–28 and also 28:1–13. Proposed rating: **moderate–high; direction open.**

**Evidence**
- [T] Rank reproduced (WLC, words in at most 150 verses, 5-verse windows): Prov 2:1 window ranks 1st of 887 against Job 28:20–28, and 0 of 46 Job nulls rank Prov 2 as high. But the top score is a **three-way tie at 4 shared lemmas**: Prov 2:1–5, Prov 8:10–14 and 1 Chr 22:10–14. The order within the tie is only dictionary order.
- [T] The four shared lemmas in Prov 2:1–5 are בִּינָה ("understanding", 38 verses), יִרְאָה ("fear", 42), אָז ("then", 114) and חָכְמָה ("wisdom", 141). All four are ordinary wisdom-school vocabulary. Silver, כֶּסֶף, occurs in 343 verses, so it does not enter the score at a 150-verse ceiling.
- [T] The rank is fragile (WLC):
  - 3-verse windows: Prov 2 ranks 9th.
  - 7-verse windows: 2nd.
  - 9-verse windows: 6th.
  - 400-verse ceiling, 5-verse windows: 5th, and **Deut 4:6** goes to 1st.
  - 800-verse ceiling, 5-verse windows: 10th; Jer 10:10 is 1st.
- [T] The extension fails. Against Job 28:1–13 (150-verse ceiling, 5-verse windows), Prov 2 ranks **223rd**. Against the whole of chapter 28 it ranks 63rd (5-verse windows) and 52nd (9-verse windows).
- [T] The image words do not match. Prov 2:4's מַטְמוֹנִים ("hidden treasures") occurs in only five verses (Gen 43:23; Isa 45:3; Jer 41:8; **Job 3:21**; Prov 2:4) and is absent from Job 28. Job 28 uses תַּעֲלֻמָה ("hidden thing", 28:11). Prov 2:4's search verbs בקשׁ ("seek") and חפשׂ ("search") are absent from Job 28, whose verb is חקר ("search out", 28:3, 27).
- [T] Job 28:28 has וַיֹּאמֶר ("and He said"), not נָתַן ("give"). The claim's "God giving the word to man" paraphrases 28:28. The only נתן in Job 28 is 28:15 לֹא יֻתַּן ("[gold] cannot be given").
- [T] The "then" works differently. In Prov 2:5, 9 אָז ("then") is the reward of the human seeker: "Then you will discern the fear of the LORD". In Job 28:27 it is God's: "Then He saw it and declared it".
- [T] Feature windows on the bundle silver + find + discern + fear + wisdom + give (WLC): Prov 1:31–2:5 comes top, but Prov 8:3–14 is within one feature. The features were taken from Prov 2, so this is post hoc.
- [T] Greek. Job 28:12, 20 (Swete, Rahlfs) "ἡ δὲ σοφία πόθεν εὑρέθη" ("but wisdom, where was it found?") and Prov 2:5 "ἐπίγνωσιν θεοῦ εὑρήσεις" ("you will find knowledge of God") share εὑρίσκω ("find") and συν- forms ("understanding"). Job 28:28's θεοσέβεια ("godliness") is not Prov 2:5's φόβον Κυρίου ("fear of the Lord"). In Rahlfs, Job 28:27a ("then He saw it") falls inside an asterisked run beginning at 26b, if the run ends at the metobelus in v. 27. On that reading the Old Greek lacked the אָז line.
- [I] Thematic contrast. Both texts make wisdom God's possession and give the fear of the LORD as its human face. Prov 2 uses the treasure-search as an image of diligence rewarded; Job 28 shows the miner finding everything except wisdom. This contrast is real, but it is carried by ideas, not by shared rare words.

**Baseline.** The window's whole score comes from four lemmas that are characteristic of Proverbs generally. Prov 8 ties, and 1 Chr 22:12–13 shares the pattern "YHWH give you understanding (בִּינָה) … then (אָז)". The 0-of-46 null is weak because the shared words are the refrain vocabulary of 28:12/20/28, which no other nine-verse Job passage concentrates.

**Rival sources.** Prov 8:10–14 (tied; it carries the motto-like 8:13). Deut 4:5–10 (1st at a 400-verse ceiling; see B4 and New candidates). 1 Chr 22:10–14 (tied). Job-internal: Zophar's Job 11:6–9 shares the rarer words תַּעֲלֻמָה and תַּכְלִית (see New candidates).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Possible |
| Volume | Weak |
| Recurrence | Weak |
| Thematic coherence | Possible |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Needs reframing.

**Final rating.** Low–moderate as a link. It holds as a conceptual comparison only. The 28:1–13 extension is **discarded**.

**Reasoning.** The rank 1 is a tie built from four common wisdom words. It does not survive small changes in window length or frequency ceiling, and it disappears entirely for 28:1–13. Prov 2's distinctive image words (treasures, seek, search) are absent from Job 28. What remains is a shared theological pattern (wisdom is God's; fear of the LORD is its human form), which Prov 8, Deut 4 and 1 Chr 22 also share.

**What a preacher may safely say.** "Proverbs 2 pictures wisdom as treasure that the earnest seeker will find; Job 28 uses mining to show that human searching, however skilled, does not reach it. Both end at the same place: wisdom is God's, and the fear of the Lord is where man meets it."

---

#### B2: Proverbs 8:10–31 and 3:13–20 behind Job 28:12–27 (with the "circle" of 22:14; 26:10)

**Claim (as tested).** Wisdom's speech in Prov 8 and the wisdom poem of Prov 3:13–20 share Job 28's valuables and creation vocabulary. The proposal also holds that the חוּג ("circle") of Job 22:14 and 26:10 shows Job's hymns sharing Wisdom's cosmology. Proposed rating: **high on words; moderate–high on use; direction open.** The brief also asks for a test of the "better than gold" rivals and of whether the null means anything for a valuables field.

**Evidence**
- [T] Verified (WLC): פְּנִינִים 6443 + חָכְמָה 2451 in one verse occur **only** at Job 28:18 and Prov 8:11. פְּנִינִים occurs in six verses in all: Job 28:18; Prov 3:15; 8:11; 20:15; 31:10; Lam 4:7. פָּז 6337 ("fine gold") occurs in nine: Isa 13:12; Job 28:17; Lam 4:2; Prov 8:19; Ps 19:11[10]; 21:4[3]; 119:127; Song 5:11, 15. The other shared words are common (WLC verse counts): כֶּסֶף 343, דֶּרֶךְ 626, כון about 210, חֹק 124, יָם 339, מַיִם 522, תְּהוֹם 35, בקע 50.
- [T] Correction to the lemma list. Prov 8:27's בְּחוּקוֹ is חָקַק 2710 ("when He inscribed"), not חֹק. Only 8:29's חֻקּוֹ ("its boundary") is the noun 2706.
- [T] Ranks reproduced (WLC, words in at most 150 verses, 5-verse windows): Prov 8 ranks 2nd against 28:20–28 (0 of 46 nulls); 9th against 28:12–19 (0 of 55); Prov 3:11 ranks 8th against 28:12–19 (2 of 55).
- [T] **What drives the Prov 8 rank against 28:20–28.** The scoring window is Prov 8:10–14, and the shared lemmas are חָכְמָה, יִרְאָה, רַע ("evil"), בִּינָה. That is Prov 8:13, "The fear of the LORD is to hate evil", plus 8:14. It is motto vocabulary, not the creation section.
- [T] The creation section does not stand out (WLC). Prov 8:27–29 against Job 28:23–27 (3-verse windows) ranks 255th at a 150-verse ceiling (9 of 48 nulls as high) and 24th at 400 (1 of 48). At the 400-verse ceiling the top windows are **Isa 40:12**, Isa 66:1, **Jer 10:11**, **Jer 51:14** (each 0 of 48 nulls).
- [T] A syntactic match the lemma counts miss: Prov 8:29 בְּשׂוּמוֹ לַיָּם חֻקּוֹ ("when He set for the sea its boundary") and Job 28:26 בַּעֲשֹׂתוֹ לַמָּטָר חֹק ("when He set a limit for the rain"). Both use infinitive construct + suffix + לְ + element + חֹק inside a series of "when He…" clauses (Prov 8:27–29; Job 28:25–26). However, a decree laid on an element of nature recurs elsewhere: חֹק + יָם ("sea") at Jer 5:22 and Prov 8:29; Job 38:10 (sea); Jer 31:35. The idiom is shared, not owned.
- [T] An inversion. Prov 3:19 says YHWH "by understanding established (כּוֹנֵן) the heavens" by wisdom; Job 28:27 says הֱכִינָהּ, "He established *it*", that is, wisdom itself. כון + חָכְמָה in one verse occurs at Jer 10:12; 51:15; Prov 3:19; 24:3. Within one verse either side, Ezek 28:12–13 and Job 28:27 are added.
- [T] **The circle.** חוּג 2329 (noun) occurs only at Isa 40:22; Job 22:14; Prov 8:27. The verb חוּג 2328 occurs only at Job 26:10. Job 26:10 חֹק־חָג עַל־פְּנֵי־מָיִם ("He has inscribed a circle on the surface of the waters") against Prov 8:27 בְּחוּקוֹ חוּג עַל־פְּנֵי תְהוֹם ("when He inscribed a circle on the face of the deep") gives four matching elements in order: חקק/חֹק + חוּג + עַל־פְּנֵי + waters/deep. They are the **only** two verses with חוּג (either form) + פְּנֵי. This is the strongest verbal contact in the claim, but it lies in Job 26, not Job 28. Strong's splits (2706/2710, 2328/2329) hide it from lemma tools.
- [T] Job 22:14 "He walks on the vault (חוּג) of heaven" is closer to Isa 40:22 "the circle (חוּג) of the earth" than to Prov 8:27. **Job 22:14b is asterisked in Rahlfs**, so the Old Greek lacked the חוּג line. Job 26:10a is Old Greek: "πρόσταγμα ἐγύρωσεν ἐπὶ πρόσωπον ὕδατος" ("He circled a decree on the face of the water"). Greek Prov 8:27 has no circle ("ὅτε ἀφώριζεν τὸν ἑαυτοῦ θρόνον ἐπ᾽ ἀνέμων", "when He marked out His throne on the winds").
- [T] Reception datum (Swete, flagged for the main session): Sir 24:5 "γῦρον οὐρανοῦ ἐκύκλωσα μόνη" ("I alone encircled the vault of heaven"). There Wisdom walks the circuit of heaven, using the wording of Greek Job 22:14 "γῦρον οὐρανοῦ διαπορεύεται" ("He walks the vault of heaven").
- [T] Greek of the valuables line. The only line linking פְּנִינִים with wisdom, **Job 28:18b, is asterisked in Rahlfs**, so the Old Greek lacked it. The hexaplaric Greek renders it "ἕλκυσον σοφίαν ὑπὲρ τὰ ἐσώτατα" ("draw wisdom above the innermost things"). Greek Prov 8:11 and 3:15 have λίθων πολυτελῶν ("costly stones"). There is no Greek echo.
- [T] "Better than gold" rivals. Prov 16:16 (חָכְמָה + חָרוּץ "gold" + בִּינָה + כֶּסֶף); Prov 20:15 (זָהָב "gold" + פְּנִינִים + "lips of knowledge", without חָכְמָה); Ps 19:11[10] and 119:127 (זָהָב + פָּז, but of the law or commandments); Ps 119:72 (gold and silver). Only Prov 3:14–15, 8:10–11, 19 and 16:16 compare *wisdom* with valuables. The incomparability formula is shared in sense, not in wording: Prov 3:15 = 8:11 וְכָל־חֲפָצִים לֹא יִשְׁווּ־בָהּ ("all desirable things cannot compare with her"), against Job 28:17, 19 לֹא־יַעַרְכֶנָּה ("cannot equal it").

**Baseline.** The 0-of-55 null for 28:12–19 means little: no other Job passage lists valuables, so no null passage can score in that field. In my cognate-merged ranking against 28:15–19 (7-verse windows), Prov 8 falls to 36th and Prov 3 to 9th. Lam 4, Ezek 28 and Exod 28 all outrank them (see B3).

**Rival sources.** For the creation lines (28:23–27): Isa 40:12–14 shares מַיִם + תִּכֵּן ("mete out"); the measure and weigh cognates (מָדַד/מִדָּה, שָׁקַל/מִשְׁקָל); רוּחַ ("wind/Spirit", 40:13); בין and דֶּרֶךְ (40:14). It also has חוּג at 40:22. תכן in the sense "measure out" occurs only at Isa 40:12, 13 and Job 28:25. Jer 10:12–13 (= 51:15–16; compare Ps 135:7) shares כון + חָכְמָה, לַמָּטָר ("for the rain") + עשׂה, רוּחַ, and קְצֵה הָאָרֶץ ("end of the earth"; Job 28:24 has the cognate קְצוֹת). For the valuables: Lam 4:1–7 (B3).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Possible |
| Volume | Possible (Strong for the 28:18/8:11 pair and the 26:10/8:27 pair; Weak for the rest) |
| Recurrence | Possible |
| Thematic coherence | Strong |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Needs reframing.

**Final rating.** Moderate on words, moderate on use; direction open. Job 26:10 / Prov 8:27 is moderate–high on its own.

**Reasoning.** Two verbal contacts are genuine and specific: פְּנִינִים + חָכְמָה (Job 28:18 / Prov 8:11) and the inscribed circle on the face of the waters (Job 26:10 / Prov 8:27). The infinitive "when He set … a decree" series is a real shared idiom. But Prov 8's high rank against 28:20–28 comes from 8:13's motto words, not from the creation poem. Job 28:23–27 has at least as much in common with Isa 40:12–14 and Jer 10:12–13. "Behind Job 28:12–27" overstates a shared wisdom-and-creation idiom.

**What a preacher may safely say.** "Job 28 speaks in the language of Proverbs' wisdom poems: wisdom is worth more than pearls, and God laid down decrees for sea and rain. Job 26:10 uses the very picture of Proverbs 8:27, God inscribing a circle on the face of the waters. But where Proverbs says God made the world by wisdom, Job 28 says God established wisdom itself."

---

#### B3: Ezekiel 28:2–13 and Exodus 28:17–20, the gem field at Job 28:15–19

**Claim (as tested).** The rarest words in the gem list are shared with the high priest's breastpiece (Exod 28:17–20) and with the king of Tyre's covering in Eden (Ezek 28:13). Contrast: Ezekiel's king won gold by wisdom, while in Job 28 no gold can buy wisdom. Proposed rating: **field moderate; source low.** Test Lam 4:1–7 and Song 5:11–14.

**Evidence**
- [T] Lemma counts all verified (WLC):
  - פִּטְדָה 6357 ("topaz"): only Exod 28:17; 39:10; Ezek 28:13; Job 28:19.
  - שֹׁהַם 7718 ("onyx"): 11 verses, including Gen 2:12 and Ezek 28:13.
  - סַפִּיר 5601 ("sapphire/lapis"): 11, including Ezek 28:13 and Job 28:6, 16.
  - רָאמוֹת 7215 ("coral"): only Ezek 27:16 and Job 28:18.
  - גָּבִישׁ 1378 ("crystal") and זְכוֹכִית 2137 ("glass"): only in Job.
- [T] Rank reproduced (WLC, words in at most 150 verses, 5-verse windows): Ezek 28:9 window ranks 1st against 28:12–19 (5 shared: חָכְמָה, יָקָר "precious", סַפִּיר, פִּטְדָה, שֹׁהַם; 0 of 55 nulls). As the claim itself notes, the null is uninformative because no other Job passage lists gems.
- [T] The breastpiece link is thin. Job shares 3 of the 12 breastpiece stones (פִּטְדָה, סַפִּיר, שֹׁהַם) and lacks the other nine. Ezek 28:13's stones all come from the breastpiece list, and Job's three are in both. On stones alone, Job cannot be assigned to Exod 28 rather than Ezek 28. Job's own distinctive items (גָּבִישׁ, זְכוֹכִית, רָאמוֹת, פְּנִינִים, כֶּתֶם "gold", פָּז) are in neither.
- [T] **Lam 4:1–7 is the strongest rival on words.** Lam 4:2 הַמְסֻלָּאִים בַּפָּז ("weighed against fine gold") uses סלא. Job 28:16, 19 לֹא תְסֻלֶּה ("cannot be valued") uses the by-form סלה, which the WLC index files separately. Those three verses are the **only** places in the Hebrew Bible where this "weigh, value against gold" verb occurs. The split numbering hides the match. Lam 4:1–7 also has כֶּתֶם (4:1; Job 28:16, 19, with טוֹב "good" / טָהוֹר "pure"), פָּז, פְּנִינִים (4:7), סַפִּיר (4:7), יָקָר (4:2), זָהָב ("gold"), and אַבְנֵי ("stones", 4:1).
- [T] Cognate-merged ranking against Job 28:15–19 (WLC, 7-verse windows):
  - 150-verse ceiling: Lam 4:1 is 1st with 6; Ezek 28:7 2nd with 5; Exod 28:14 3rd with 4; Isa 13:6 7th; Prov 3:9 9th; Song 5:8 10th.
  - 400-verse ceiling: Lam 4 is again 1st (7), ahead of Ezek 28 (6).
  - Against Job 28:1–19: Lam 4 1st, Ezek 28 9th.
- [T] Other rivals:
  - Isa 13:12 (אֱנוֹשׁ "man" + פָּז + אָדָם + כֶּתֶם אוֹפִיר "gold of Ophir"). It is the only verse with אֱנוֹשׁ + פָּז. Job 28:13 has אֱנוֹשׁ, 28:16 כֶּתֶם אוֹפִיר, 28:17 פָּז, 28:28 אָדָם.
  - The phrase כֶּתֶם אוֹפִיר occurs only at Isa 13:12, Job 28:16 and Ps 45:10[9].
  - Song 5:11, 14–15 shares כֶּתֶם, פָּז, סַפִּיר and זָהָב, without wisdom.
  - Within Job: 22:24–25 (Ophir gold, silver) and 31:24 (זָהָב, כֶּתֶם).
- [T] Support for the thematic contrast: Ezek 28:4 "by your wisdom and understanding you have made wealth, gold and silver in your treasuries" (paraphrased). It is the **only** verse in the Hebrew Bible where זָהָב and חָכְמָה meet. חָכְמָה + כֶּסֶף meet only at Eccl 7:12, Ezek 28:4 and Prov 16:16. Ezek 28:12 also has מָלֵא חָכְמָה ("full of wisdom"), and 28:13 ends כּוֹנָנוּ ("were established"); Job 28:27 has הֱכִינָהּ ("He established it").
- [T] Greek (Rahlfs Job). The onyx-and-sapphire line, 28:16b, is asterisked, so the Old Greek lacked it. The Old Greek keeps τοπάζιον Αἰθιοπίας ("topaz of Ethiopia", 28:19a) and σαπφείρου ("of sapphire", 28:6a). It transliterates גָּבִישׁ as γαβις and renders רָאמוֹת as μετέωρα ("lofty things"). So most of the Ezek 28:13 overlap is not in the Old Greek.
- [I] Edenic colouring: Gen 2:11–13 combines gold, שֹׁהַם and כּוּשׁ ("Cush"); Job 28:19 has פִּטְדַת כּוּשׁ ("topaz of Cush"). The merged score is only 2–4, so this is colour, not a source.

**Baseline.** The field null is uninformative. Among non-Job texts, Ezek 28 does not stand clear of Lam 4 or Exod 28, and falls behind Lam 4 once the cognate split is merged. Job 28:16 has 4 exclusive pairs, against a chapter rate of 1.64; two of them are with Ezek 28:13.

**Rival sources.** Lam 4:1–7 (strongest on words and on the valuation verb). Isa 13:12 (Ophir phrase; man against gold). Exod 28 / 39 (the same stones as Ezek 28:13). Song 5:11–15. 1 Kgs 10 / 2 Chr 9: Solomon's wisdom with Ophir gold and precious stones (4 shared, with 7-verse windows).

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Possible |
| Volume | Possible (field); Weak (Ezek 28 as a single source) |
| Recurrence | Weak |
| Thematic coherence | Possible (Ezek 28:4's wisdom-to-wealth contrast) |
| Historical plausibility | Possible |
| History of interpretation | Not checked |
| Satisfaction | Possible |

**Verdict.** Confirmed with nuance.

**Final rating.** Field moderate. Ezek 28 as source low, with the wisdom-to-wealth contrast possible. Lam 4:1–7 as rival low–moderate.

**Reasoning.** The lemma facts are all correct, and Job 28's list does sit in the rare vocabulary of priestly, royal and lament inventories of precious things. Ezek 28 alone adds wisdom to that field, which makes the contrast attractive. On words, though, Lam 4:1–7 is as close or closer: it has the unique "weigh against gold" verb and four of Job's valuables. The breastpiece supplies only the three stones Ezek 28:13 also has. The field is shared; no single source is shown.

**What a preacher may safely say.** "Job 28 names the rarest treasures of the ancient world, the stones of the priest's breastpiece and of the king of Tyre's robe, and declares that none can buy wisdom. Ezekiel's king thought his wisdom had won him gold; Job 28 says gold cannot win wisdom."

---

#### B4: The motto (Prov 1:7; 9:10; 15:33; Ps 111:10, with Prov 3:7; 14:16; 16:6) at Job 28:28

**Claim (as tested).**
- (a) יִרְאָה ("fear") + חָכְמָה ("wisdom") meet in seven verses. Three of them (Isa 11:2, Prov 9:10, Job 28:28) add בִּינָה. Job 28:28 alone has אֲדֹנָי ("Lord"), and many manuscripts read יהוה.
- (b) "Fear" + סוּר מֵרָע ("turn from evil") occur in one verse only at Job 1:1, 1:8, 2:3, 28:28 and Prov 3:7; 14:16; 16:6.
- (c) In Job, סוּר + רַע occur only at those four verses, with θεοσεβ- ("godly") + ἀπέχομαι ἀπό ("keep away from") at the same four in Greek.
- (d) In canonical order the motto is tested (Job) before it is taught (Proverbs).

Proposed rating: **high.** The brief asks whether 28:28 depends on Proverbs or shares a formula, and whether the Proverbs "turn from evil" verses are closer to 1:1 or to 28:28.

**Evidence**
- [T] (a) Verified (WLC). יִרְאָה ("fear") + חָכְמָה ("wisdom") in one verse: Isa 11:2; 33:6; Job 28:28; Prov 1:7; 9:10; 15:33; Ps 111:10. Adding בִּינָה ("understanding") leaves Isa 11:2, Job 28:28, Prov 9:10. אֲדֹנָי ("the Lord") occurs in Job only at 28:28. The exact phrase יראת אדני occurs only at Job 28:28 in the Hebrew Bible.
- [T] (a) BHS apparatus, Job 28:28: "ᶜ mlt Mss יהוה; pc Mss pr יהוה; > 2 Mss". Many manuscripts read יהוה, a few put יהוה before it, and two omit it. The claim is accurate. The Greek "ἡ θεοσέβειά" has no divine name, so it does not decide the reading.
- [T] (b) Verified exactly (WLC):
  - Verb 3372: 1 Sam 12:20; Prov 3:7; Zeph 3:15. The 1 Samuel and Zephaniah verses use the lemmas in other senses ("do not fear … do not turn aside from following the LORD"; "He has turned away your judgements … you will fear evil no more").
  - Adjective 3373: Job 1:1, 1:8, 2:3; Prov 14:16.
  - Noun 3374: Job 28:28; Prov 16:6.
- [T] (c) Verified (WLC): 5493 + 7451 in Job only at 1:1, 1:8, 2:3, 28:28. In Greek Job (Swete), θεοσεβ- occurs only at 1:1, 1:8, 2:3 and 28:28. ἀπεχ- occurs at those four and at 13:21, where it means "withdraw (your hand)". Rahlfs: none of the four lines is asterisked, so the Old Greek had all of them, including 28:28.
- [T] **Form test: formula or dependence?** None of the Proverbs or Psalter motto forms matches Job 28:28's syntax. Those forms are רֵאשִׁית ("beginning", Prov 1:7; Ps 111:10), תְּחִלַּת ("beginning", Prov 9:10) and מוּסַר ("instruction", Prov 15:33). Job 28:28 is an identity clause, "X הִיא חָכְמָה … בִּינָה" ("X, that is wisdom … understanding"). Its only matches are:
  - חָכְמָה + בִּינָה + הִיא in one verse: only **Deut 4:6** (כִּי הִוא חָכְמַתְכֶם וּבִינַתְכֶם, "for that is your wisdom and your understanding") and Job 28:28.
  - יִרְאָה + הִיא in one verse: only **Isa 33:6** (יִרְאַת יְהוָה הִיא אוֹצָרוֹ, "the fear of the LORD is his treasure", in a verse that also has חָכְמַת וָדַעַת, "wisdom and knowledge") and Job 28:28.

  So Job 28:28 shares the motto's content, but its wording is closer to Deut 4:6 and Isa 33:6 than to any Proverbs verse. Deut 4:6 also equates *doing* with wisdom and understanding, as 28:28b equates turning from evil with understanding.
- [T] **Are the Proverbs "turn from evil" verses closer to 1:1 or to 28:28?** They split by grammar:
  - **Prov 14:16** חָכָם יָרֵא וְסָר מֵרָע ("a wise man is cautious and turns away from evil") uses the same adjective + participle forms as Job 1:1 וִירֵא אֱלֹהִים וְסָר מֵרָע ("fearing God and turning away from evil"). It is closest to the frame.
  - **Prov 16:6** וּבְיִרְאַת יְהוָה סוּר מֵרָע ("by the fear of the LORD one keeps away from evil") uses noun + infinitive, matching Job 28:28 יִרְאַת אֲדֹנָי … וְסוּר מֵרָע. It is closest to 28:28.
  - **Prov 3:7** uses imperatives with "do not be wise in your own eyes", a wisdom-and-fear pairing between the two.
- [T] Rival passages for "fear + turn from evil": **Ps 34:12[11]** "I will teach you the fear of the LORD" and **34:15[14]** "Depart (סוּר) from evil and do good", three verses apart. **Prov 8:13** "The fear of the LORD is to hate evil". The phrase סוּר מֵרָע alone occurs in 12 verses: Job ×4; Prov 3:7; 13:19; 14:16; 16:6; 16:17; Ps 34:15[14]; 37:27; Isa 59:15.
- [T] Greek. Job's θεοσέβεια / θεοσεβής is the rendering of "fear of God" at Gen 20:11 and Exod 18:21 (Swete). Greek Proverbs and Psalms use φόβος κυρίου ("fear of the Lord") + ἐκκλίνω ("turn aside"): Prov 3:7; 14:16; 15:27a (= MT 16:6); 16:17; Ps 33:15[34:14]. Greek Job thus binds 28:28 to 1:1 rather than to Greek Proverbs. One overlap: Job 2:3 "ἀπὸ παντὸς κακοῦ" ("from every evil") is also in Greek Prov 3:7 (and 1:33).
- [T] **(d) does not hold as stated.** In the Tanak (BHS) order, the Ketuvim run Psalms, Job, Proverbs. So the reader meets "the fear of the LORD is the beginning of wisdom" in **Ps 111:10**, and "fear of the LORD" with "turn from evil" in **Ps 34:12, 15[11, 14]**, before Job. Isa 11:2 and 33:6 come earlier still, in the Latter Prophets, and Deut 4:6, 10 in the Torah. Only the Proverbs formulations come after Job.

**Baseline.** Job 28:28 has no exclusive content pair with Proverbs (words in at most 400 verses). The motto words are frequent enough to recur. The frame link inside Job (1:1, 1:8, 2:3 with 28:28) is exclusive within the book in both Hebrew and Greek, which is significant against Job's rate of 1.34 pairs per verse.

**Rival sources.** Deut 4:5–10 (identity form; "learn to fear Me", 4:10; 1st of 887 against 28:20–28 at a 400-verse ceiling with 5-verse windows, with 1 of 46 nulls as high). Isa 33:6 (identity form + treasure). Ps 34:12–15[11–14]. Prov 8:13.

**Markers** (attribution and design: does 28:28 depend on Proverbs, and does the canonical sequence hold?)

| Marker | Score |
|---|---|
| Formula (shared fear–wisdom–evil content) | Strong |
| Paragraphing (BHS ס after 28:28; the line closes the poem) | Strong |
| Vocabulary profile (unique אֲדֹנָי in Job; identity syntax shared with Deut 4:6 / Isa 33:6, not Proverbs) | Possible |
| Greek (θεοσεβ- / ἀπέχομαι ties 28:28 to 1:1, not to Greek Proverbs) | Strong for the frame; Weak for dependence |
| Verbal architecture (1:1 / 1:8 / 2:3 / 28:28 exclusive in Job) | Strong |

**Verdict.** Confirmed with nuance.

**Final rating.** High for (a)–(c), that is, the shared formula and the 1:1 / 28:28 frame. Low for dependence on any single Proverbs verse. (d) needs reframing.

**Reasoning.** Every lemma statement in (a)–(c) is accurate, and the frame link from 28:28 back to 1:1 is exclusive within Job in both Hebrew and Greek. Job 28:28 shares the wisdom tradition's formula, but its identity syntax is matched only by Deut 4:6 and Isa 33:6. Among the Proverbs sayings, 14:16 echoes Job 1:1 and 16:6 echoes Job 28:28, which points to a shared formula rather than a borrowing in either direction. In Tanak order, Ps 34 and Ps 111 teach the motto before Job tests it.

**What a preacher may safely say.** "Job 28 ends with the confession the whole wisdom tradition shares, the fear of the Lord as wisdom and turning from evil as understanding, and in doing so it names Job himself as he was described in chapter 1. The Psalms have already taught this; Job puts it under the severest test before Proverbs sets it out for daily life."

---

### New candidates surfaced

1. **Job 11:6–9 ↔ Job 28:3, 11–14, 25 (internal).** Zophar's "secrets of wisdom" (תַּעֲלֻמוֹת חָכְמָה, 11:6), "can you discover (תִּמְצָא) … the limit (תַּכְלִית) of the Almighty" (11:7), deeper than Sheol and "broader than the sea (יָם)" (11:9). The shared words include two of the rarest in Job 28 (WLC): תַּעֲלֻמָה occurs in three verses (Job 11:6; 28:11; Ps 44:22[21]); תַּכְלִית in five (Job 11:7; 26:10; 28:3; Neh 3:21; Ps 139:22). There are also the cognates חֵקֶר / חקר ("depth / search out") and מִדָּה ("measure"). In 28:3, 11 the miner reaches every limit and brings the hidden thing to light, yet wisdom is not found (28:12–14). **Rating: moderate–high (Job-internal).**
2. **Isa 40:12–14, 22 ↔ Job 28:23–27 and 22:14.** Shares מַיִם + תִּכֵּן ("mete out"), which in the sense "measure" occurs only at Isa 40:12, 13 and Job 28:25. Also the measure and weigh cognates, רוּחַ, בין, דֶּרֶךְ, and חוּג (40:22). Isa 40:12 ranks 1st against 28:23–27 (WLC, 400-verse ceiling, 3-verse windows), with 0 of 48 nulls as high. Greek Isa 40:12 ἐμέτρησεν … ὕδωρ … σταθμῷ ("measured … water … with a weight") against Job 28:25 ἀνέμων σταθμὸν ὕδατός τε μέτρα ("a weight for the winds and measures of water"). **Rating: moderate.**
3. **Jer 10:12–13 (= 51:15–16; compare Ps 135:7) ↔ Job 28:24–27.** Shares כון + חָכְמָה, לַמָּטָר + עשׂה, רוּחַ, and "end of the earth" (across the split between קָצֶה and קָצָה). It ranks 3rd and 4th against 28:23–27 (400-verse ceiling, 3-verse windows), with 0 of 48 nulls. **Rating: low–moderate.**
4. **Lam 4:1–7 ↔ Job 28:15–19.** Shares the unique "value against gold" verb (סלא / סלה: Lam 4:2; Job 28:16, 19 only), כֶּתֶם, פָּז, פְּנִינִים, סַפִּיר, יָקָר. It ranks 1st on the cognate-merged ranking. **Rating: low–moderate as a source; strong as a field companion.**
5. **Deut 4:5–10 ↔ Job 28:28.** The only other verse with חָכְמָה + בִּינָה + הִיא in identity form (4:6). Doing equals wisdom; "learn to fear Me" (4:10); statutes (חֻקִּים, compare 28:26). It ranks 1st against 28:20–28 at a 400-verse ceiling with 5-verse windows, with 1 of 46 nulls. **Rating: low–moderate.**
6. **Isa 33:6 ↔ Job 28:28.** The only other verse with יִרְאַת X הִיא ("the fear of X is"), alongside חָכְמָה and אוֹצָר ("treasure"), which echoes the valuables of 28:15–19. **Rating: low–moderate.**
7. **Job 3:21 ↔ Prov 2:4.** מַטְמוֹנִים ("hidden treasures") occurs in five verses in the Hebrew Bible. Job digs for death more than for treasure; Proverbs seeks wisdom as treasure. The Greek shares ὡς / ὥσπερ θησαυρούς ("as treasures"). It is a single rare word, but with mirrored function. **Rating: low–moderate.**
8. **Isa 13:12 ↔ Job 28:13, 16–17.** The only verse with אֱנוֹשׁ + פָּז; it shares כֶּתֶם אוֹפִיר (with Ps 45:10[9]; three verses in all). "Man made scarcer than gold" against "wisdom beyond gold". **Rating: low.**
9. **Sir 24:5 (Greek) as reception of Job 22:14.** "γῦρον οὐρανοῦ" ("the vault of heaven"), the circuit God walks in Job 22:14, is walked by Wisdom in Sirach. This bears on B2's circle and is passed to the main session for library checking. **Not rated (reception).**

### Key evidence for spot checks

1. Window rank against Job 28:20–28 (5-verse windows): Prov 2:1 1st, Prov 8:10 2nd, 1 Chr 22:10 3rd, **all at 4**; 0 of 46 nulls each. The shared words for Prov 2:1–5 are בִּינָה ("understanding"), יִרְאָה ("fear"), אָז ("then") and חָכְמָה ("wisdom").
2. Sensitivity: Prov 2 ranks 9th (3-verse windows), 5th (400-verse ceiling, 5-verse windows; Deut 4:6 is 1st), 10th (800-verse ceiling, 5-verse windows). Against Job 28:1–13 it ranks **223rd**.
3. The shared words for Prov 8:10 against 28:20–28 are חָכְמָה ("wisdom"), יִרְאָה ("fear"), רַע ("evil") and בִּינָה ("understanding"), the motto words of Prov 8:13. Prov 8:27 against 28:23–27 (3-verse windows): 255th at a 150-verse ceiling, 24th at 400.
4. פְּנִינִים ("jewels") + חָכְמָה ("wisdom"): Job 28:18 and Prov 8:11. Job 28:18b is asterisked in Rahlfs.
5. The noun חוּג ("circle") occurs at Isa 40:22, Job 22:14 and Prov 8:27; the verb חוּג ("draw a circle") only at Job 26:10. With פָּנִים ("face"), the noun gives Prov 8:27 alone and the verb Job 26:10 alone. Prov 8:27's בְּחוּקוֹ is the verb חקק ("inscribe"), not the noun חֹק ("decree").
6. סלא ("weigh") occurs only at Lam 4:2; its by-form סלה ("value") at Job 28:16, 19. In the cognate-merged ranking against Job 28:15–19 (7-verse windows), Lam 4:1 is 1st (6) and Ezek 28:7 2nd (5).
7. פִּטְדָה ("topaz") occurs at Exod 28:17; 39:10; Ezek 28:13; Job 28:19. זָהָב ("gold") + חָכְמָה ("wisdom") in one verse: Ezek 28:4 only.
8. יִרְאָה ("fear") + חָכְמָה ("wisdom") gives seven verses (Isa 11:2; 33:6; Job 28:28; Prov 1:7; 9:10; 15:33; Ps 111:10). The adjective יְרֵא ("fearing") + סור ("turn") + רַע ("evil") gives Job 1:1, 1:8, 2:3, Prov 14:16; the noun יִרְאָה with the same gives Job 28:28, Prov 16:6; the verb ירא with the same gives 1 Sam 12:20, Prov 3:7, Zeph 3:15.
9. חָכְמָה ("wisdom") + בִּינָה ("understanding") + הִיא / הוּא ("it is"): Deut 4:6 and Job 28:28. יִרְאָה ("fear") + הִיא / הוּא: Isa 33:6 and Job 28:28.
10. θεοσεβ- ("godly, godliness") in Swete: in Job only 1:1, 1:8, 2:3, 28:28; elsewhere Gen 20:11, Exod 18:21 and later books. BHS apparatus at Job 28:28: "ᶜ mlt Mss יהוה; pc Mss pr יהוה; > 2 Mss".

---

## Part C: design and structure in Job 22–28

### Auditor's note

**Corpus.** WLC with its lemma index (observation layer), the BHS Job export and its apparatus (Logos), Swete LXX, the Rahlfs–Hanhart Job export (Logos), and the NASB95, ESV and NIV84 Job exports, all from the `_texts/` corpus. English is quoted from NASB95 unless stated. Every count names its edition (WLC unless stated).

**Positive control.** A search for חֶסֶד ("covenant-kindness") in Job (WLC) returned 6:14; 10:12; 37:13, as required. Before reporting absences I ran known-hit searches: the phrase וַיַּעַן צֹפַר ("then Zophar answered") finds both Zophar formulas (11:1, 20:1); שְׁמוּעָה ("report") returns 1 Kgs 2:28 and others, so its absence from Job is real; תּוֹרָה ("instruction") returns 1 Chr 16:40 and others before its single Job hit; יִרְאָה ("fear") without a book returns Prov 1:7 among others; the lemma search and the consonant search for שֵׁמֶץ ("whisper") agree (Job 4:12, 26:14). Parallel texts and lemma splits were checked: the consonants of לְשֵׁמַע אֹזֶן ("by the hearing of the ear") catch 2 Sam 22:45 (infinitive), which the lemma search misses. Skeletal over-matches were rejected: the phrase יִרְאַת אֲדֹנָי also returns 2 Sam 19:21 and 24:3 (לִקְרַאת אֲדֹנִי), and אִמְרֵי פִי ("the words of my mouth") returns dozens of false hits; only exact matches in the WLC text are reported.

**Method.** Each claim was rebuilt from scratch. The interrupted earlier run left working searches; I reused them after reading them, corrected the files they drew on, and re-ran every result reported here. The map of who speaks where was checked against every speech formula in Job before use.

**Baselines computed.** (1) C1: Job-exclusive lemma pairs shared with the hymns, for all 432 sliding 11-verse windows of Job poetry, counting words in up to 400, 700 and 1,100 verses. (2) C2: distribution of Job lemmas of 4–7 verses across the three Eliphaz speeches, with a random-placement simulation; eye/see density by chapter. (3) C3: the internal five-verse window test re-run, with a whole-chapter null (36 chapters) and two topic controls (38:1–28; 26:5–14). (4) C4/C5: BHS paragraph markers for the whole book against every speech formula and every within-speech chapter break; a speaker vocabulary profile tested on 25 passages of known speaker; a friends'-portrait profile with sliding windows from Job's undisputed speeches and the friends' other speeches, plus Job 21 as topic control. (5) C6: verbatim trigram and four-word repetition from earlier speeches, for every speech in the book. (6) C7: verbatim trigrams, content bigrams and exclusive pairs for every pair of speeches in 3–27, adjacent and non-adjacent.

**Greek conventions.** In the Rahlfs Job export an asterisk opens each hexaplaric stich and a metobelus closes the group; the dagger sign that also appears is an apparatus cue and was ignored. Lines inside an asterisked group without their own asterisk were treated with caution and are named only where the reading is clear.

**Limits.** No morphological index: verb stems (e.g. the hiphil of יצא at 28:11) are judged from the pointed form. Sliding windows overlap, so window percentages are not independent; chapter counts are given alongside. Vocabulary profiling failed its controls at speaker level and was used only to show that it cannot decide. History of interpretation was not checked; the "disorder" view (C5, C6) is recalled, not consulted. The BHS export lacks the ס that the WLC prints at 19:29; this does not touch chapters 22–31.

#### C1: The miner does on a small scale what Job's speeches say God does (design, Job 28:3–11)

**Claim (as tested).** Four exclusive pairs tie the acts in 28:3–11 to God's acts elsewhere: (i) תַּכְלִית ("limit") + חֹשֶׁךְ ("darkness"), Job 26:10 and 28:3; (ii) הפך ("overturn") + הַר ("mountain"), 9:5 and 28:9; (iii) יצא hiphil ("bring out") + אוֹר ("light"), in Job only 12:22 and 28:11; (iv) בקע ("split") + צוּר ("rock"), Job 28:10, Ps 78:15, Isa 48:21. חקר ("search") brackets the poem (28:3 man, 28:27 God). Proposed: pairs high; design moderate–high.

**Evidence**

- [T] All four pairs verify by lemma (WLC). תַּכְלִית ("limit") + חֹשֶׁךְ ("darkness"): Job 26:10, 28:3 (exclusive in the Hebrew Bible). הפך ("overturn") + הַר ("mountain"): Job 9:5, 28:9 (exclusive in the Hebrew Bible). יצא ("bring out") + אוֹר ("light"): Hos 6:5, Isa 13:10, 51:4, Job 12:22, 28:11, Mic 7:9, Ps 37:6: exclusive **within Job only**; יצא is one of the commonest verbs (991 WLC verses). בקע ("split") + צוּר ("rock"): Isa 48:21, Job 28:10, Ps 78:15. Cognate check: בקע + סֶלַע ("crag") only 2 Chr 25:12, so no hidden rival there.
- [T] תַּכְלִית ("limit") occurs in five WLC verses: Job 11:7, 26:10, 28:3, Neh 3:21, Ps 139:22. In 26:10 it is "the boundary of light and darkness" which God drew; in 28:3 it is the extremity the searcher reaches ("to the farthest limit he searches out"). The shared word has a different function in each line.
- [T] 12:22 is closer to 28:3–11 than the pair alone shows: "He reveals mysteries from the darkness (חֹשֶׁךְ) And brings (וַיֹּצֵא) the deep darkness (צַלְמָוֶת) into light (לָאוֹר)". Job 28:3 has חֹשֶׁךְ and צַלְמָוֶת ("deep shadow"), and 28:11 "what is hidden he brings out (יֹצִא) to the light (אוֹר)". חֹשֶׁךְ + צַלְמָוֶת in one verse in Job: 3:5, 10:21, 12:22, 28:3, 34:22 (WLC), so that pair is a formula, but four lemmas of 12:22 recur across 28:3–11.
- [T] חקר: the verb ("search out") in Job at 5:27, 13:9, 28:3, 28:27, 29:16, 32:11 (WLC); in chapter 28 only 28:3 (חוֹקֵר, "searches out") and 28:27 (חֲקָרָהּ, "searched it out"). The bracket is real. The noun חֵקֶר ("searching") is lemmatised separately (Job 5:9, 8:8, 9:10, 11:7, 34:24, 36:26, 38:16) and hides a rival (below).
- [T] The subject of 28:3–11 is unexpressed in Hebrew: 28:3 opens קֵץ שָׂם ("he set an end") with no noun; NASB95 supplies "Man". The design reading (a human miner) is the natural one after 28:1–2, but it is an inference; a reader who takes God as the subject of 28:9–11 turns the "small-scale mirror" into simple repetition of hymn language.
- [I] Greek (data). Rahlfs asterisks 28:3b ("and every limit he searches out", καὶ πᾶν πέρας αὐτὸς ἐξακριβάζεται) and 26:10b (μέχρι συντελείας φωτὸς μετὰ σκότους): the Old Greek lacked **both** תַּכְלִית lines of pair (i). 28:9b κατέστρεψεν … ὄρη ("he overturned … mountains") echoes 9:5 ὁ καταστρέφων … ὄρη. 28:11 βάθη δὲ ποταμῶν ἀνεκάλυψεν … εἰς φῶς ("he uncovered the depths of rivers … into light") echoes 12:22 ἀνακαλύπτων βαθέα ἐκ σκότους … εἰς φῶς: ἀνακαλύπτω + βάθ- occurs only in Dan 2:22, Job 12:22 and 28:11 (Swete). The translator heard 12:22 in 28:11. 28:10b ("my eye saw") is not asterisked.

**Baseline.** I counted, for every 11-verse sliding window of Job poetry (432 windows, excluding chapter 28 and any window overlapping the hymns 5:9–16; 9:4–13; 12:13–25; 26:5–14; 36:26–37:24; 38:2–41:26), the Job-exclusive content-lemma pairs whose other verse lies in those hymns. Results:

| Frequency ceiling (WLC verses) | 28:1–11 | null mean (SD) | null max | windows reaching 28:1–11 | chapters reaching it |
|---|---|---|---|---|---|
| 400 | 3 | 0.55 (0.85) | 5 | 12 (2.8%) | 5 of 31 (3, 11, 12, 24, 36) |
| 700 | 4 | 1.14 (1.23) | 5 | 26 (6.0%) | 7 of 31 |
| 1100 | 6 | 1.73 (1.42) | 7 | 5 (1.2%) | 2 of 31 (24, 14) |

The 28:1–11 count includes pairs with no design value (28:4 with 39:15, the ostrich's "foot" and "forget"), as the null windows do. The passage sits in the top 1–6% of Job windows, but Job 3, 14 and 24 do as well or better: the hymns' vocabulary (light, darkness, mountains, waters) is shared by any passage on the same subjects. Pair (iii) enters only when lemmas in up to 1100 verses are admitted.

**Rival sources**

- [T] **Zophar, 11:6–8.** תַּעֲלֻמָה ("hidden thing") occurs in WLC only Job 11:6 ("the secrets of wisdom", תַּעֲלֻמוֹת חָכְמָה), 28:11 ("what is hidden he brings out to the light") and Ps 44:22 [Eng 44:21]. 11:7 is the only verse joining חֵקֶר ("searching") and תַּכְלִית: "Can you discover the depths (חֵקֶר) of God? Can you discover the limits (תַּכְלִית) of the Almighty?"; 28:3 has the verb חקר with תַּכְלִית. Zophar's lines, with the verb מצא ("find") twice, stand behind the poem's hinge, "where can wisdom be found?" (28:12). The miner reaches "every limit" and brings "the hidden thing" to light; Zophar said no one reaches God's limit. This is at least as strong as pair (i) and makes 28:3–11 an answer to Zophar as well as a mirror of the hymns.
- [T] **Ps 114:8** for 28:9–10: "Who turned (הַהֹפְכִי) the rock (הַצּוּר) into a pool of water, The flint (חַלָּמִישׁ) into a fountain of water." חַלָּמִישׁ ("flint") occurs in five WLC verses (Deut 8:15; 32:13; Isa 50:7; Job 28:9; Ps 114:8); הפך + חַלָּמִישׁ only Job 28:9 and Ps 114:8; הפך + צוּר only Ps 114:8. Job 28:9–10 has הפך, חַלָּמִישׁ, צוּר, בקע and water-channels (יְאֹרִים) in two lines. Deut 8:15 ("He brought water for you out of the rock of flint") and Ps 78:15 ("He split the rocks in the wilderness") complete a wilderness-rock cluster. Pair (iv) is one strand of it, not the whole.

**Hays criteria**

| Criterion | Score |
|---|---|
| Availability | Strong (internal to Job; Ps 78, 114, Isa 48 canonical) |
| Volume | Possible (two HB-exclusive pairs; one pair only Job-exclusive, built on a very common verb) |
| Recurrence | Strong (9:5, 12:22, 26:10 in three different hymns) |
| Thematic coherence | Strong (searching, light out of darkness, mountains overturned) |
| Historical plausibility | Strong |
| History of interpretation | Not checked |
| Satisfaction | Possible (the mirror holds if the subject is human; Zophar 11:6–7 is an equally good key) |

**Verdict.** Confirmed with nuance.

**Final rating.** Pairs: (i), (ii), (iv) high; (iii) moderate (in-Job exclusive only). Design: moderate.

**Reasoning.** Every pair is real and three of four are rare, and the Greek translator himself heard 9:5 and 12:22 in 28:9–11. But the cluster is matched by Job 3, 14 and 24 against the same hymns, so it does not by itself prove deliberate design; it is the vocabulary of the subject. The stronger point is that 28:3–11 gathers words used of God (and Zophar's "limit", "search" and "hidden things") and gives them to a human searcher who still cannot find wisdom.

**What a preacher may safely say.** "The miner in Job 28 does, in his tunnels, things Job's speeches say God does: he overturns mountains, reaches the limit of darkness, and brings hidden things to light; and yet he cannot find wisdom."

#### C2: The ear and the eye, and Eliphaz's "fear" (two design lines into and out of Job 28)

**Claim (as tested).** (a) שֵׁמֶץ ("whisper") only Job 4:12 and 26:14; 28:22 "with our ears (בְּאָזְנֵינוּ) we have heard (שָׁמַעְנוּ) a report of it (שִׁמְעָהּ)"; the seeing pattern in 28; 42:5 "I have heard of You by the hearing of the ear; But now my eye sees You". אֹזֶן + שָׁמַע + שֵׁמַע in one verse only Job 28:22, 42:5, Ps 18:45; in Job the noun שֵׁמַע only 28:22, 42:5. Proposed: words high, line moderate–high. (b) יִרְאָה ("fear") in Job only 4:6, 6:14, 15:4, 22:4, 28:28, once in each Eliphaz speech, with 28:28 defining it in the frame's terms (1:1, 8; 2:3). Proposed: words high, design moderate–high.

**Evidence**

- [T] שֵׁמֶץ ("whisper") occurs only at Job 4:12, 26:14 (WLC); the consonant search returns the same two, so no ketiv or variant spelling is hidden. 4:12: "my ear (אָזְנִי) received a whisper of it"; 26:14: "how faint a word (שֵׁמֶץ דָּבָר) we hear (נִשְׁמַע) of Him". Eliphaz's night-word and Job's "faint word" are tied by an HB-exclusive noun.
- [T] אֹזֶן ("ear") + the verb שׁמע ("hear") + the noun שֵׁמַע ("hearing") in one verse: Job 28:22, 42:5, Ps 18:45 [Eng 18:44] (WLC). Parallel-text check: 2 Sam 22:45 reads לִשְׁמוֹעַ אֹזֶן (the infinitive of the verb), so the lemma search misses it; the consonants of לְשֵׁמַע אֹזֶן return 2 Sam 22:45, Job 42:5, Ps 18:45. The **phrase** לְשֵׁמַע אֹזֶן ("by the hearing of the ear") is therefore 42:5 plus the royal psalm and its parallel; 28:22 does not have the phrase, only the three lemmas. The noun שֵׁמַע ("hearing") in Job: 28:22, 42:5 only (17 HB verses). Control: שְׁמוּעָה ("report") returns 1 Kgs 2:28 and others, and nothing in Job, so no cognate is hiding.
- [T] Ear-and-eye together is a Job idiom, not a 28/42 peculiarity: אֹזֶן ("ear") + שׁמע ("hear") + עַיִן ("eye") + ראה ("see") in one verse of Job: 13:1 ("my eye has seen all this, my ear has heard"), 29:11, 42:5. 42:5 answers 13:1 and 29:11 as much as 28:22.
- [T] Seeing in 28: עַיִן ("eye") 28:7, 10, 21; ראה ("see") 28:10, 24, 27 (WLC). Chapter 28 has the second-highest density of eye/see verses in Job (0.179 of verses; Job mean 0.080; chapter 17 is 0.188, chapter 31 is 0.175). The poem moves from the hawk's eye that has not seen the path (28:7) and the miner's eye that sees every precious thing (28:10), to wisdom hidden "from the eyes of all living" (28:21), to Abaddon who has only heard (28:22), to God who "sees everything under the heavens" (28:24) and "saw it" (28:27). That is a real hear-versus-see progression inside 28.
- [I] Greek: Rahlfs asterisks 26:14b, so the Old Greek lacked the שֵׁמֶץ line of 26:14. 28:22b in Greek, Ἀκηκόαμεν δὲ αὐτῆς τὸ κλέος ("we have heard its fame"), has no "ears"; 42:5 ἀκοὴν μὲν ὠτὸς ἤκουόν σου ("by hearing of the ear I heard you") keeps them.
- [T] (b) יִרְאָה ("fear") in Job: 4:6, 6:14, 15:4, 22:4, 28:28: verified (control: the same search across the Hebrew Bible returns Prov 1:7 among others). Speakers: Eliphaz 1 (4:6), Job (6:14), Eliphaz 2 (15:4), Eliphaz 3 (22:4), poem (28:28). The exact phrase יִרְאַת אֲדֹנָי ("the fear of the Lord") is Job 28:28 only; the skeletal phrase search also returns 2 Sam 19:21 and 24:3, but these are skeletal over-matches of לִקְרַאת אֲדֹנִי ("to meet my lord").
- [T] The frame tie is stronger than the Eliphaz series: סור + רַע ("turn from evil") in Job only 1:1, 1:8, 2:3, 28:28 (WLC), and the adjective יְרֵא ("fearing") only 1:1, 1:8, 2:3. [I] The Greek makes the same tie: θεοσεβ- in Job only 1:1, 1:8, 2:3 (θεοσεβής) and 28:28 (θεοσέβεια), each with ἀπέχεσθαι ἀπὸ … κακ- ("to keep away from evil").
- [T] NASB95 hides the Eliphaz series: 4:6 "your fear of God", but 15:4 "you do away with reverence" and 22:4 "because of your reverence". The Greek also breaks it: 22:4 has no φόβος ("fear").

**Baseline.** (a) No numerical null was possible for a "line" of motifs; the controls above show that ear-and-eye pairing recurs in Job (13:1, 29:11) and that eye/see density in 28 is high but matched by chapters 17 and 31. (b) Of 222 Job lemmas occurring in 4–7 verses (WLC), 2 fall in all three Eliphaz speeches (יִרְאָה and כחד, "hide"); placing such lemmas at random in the speech verses gives an expected 0.70 (by simulation; for a five-verse lemma P = 0.0025). One such lemma is what a scan of all lemmas would turn up by chance; the distribution is suggestive only because of what the word means, not because it is improbable.

**Rival sources.** For (a), Job 13:1 and 29:11 are rival antecedents to 42:5 (same four lemmas). Ps 18:45 [Eng 18:44] "as soon as they hear, they obey me" is the only verbatim sharer of לְשֵׁמַע אֹזֶן; it is a royal-submission line and adds nothing to Job's sense. For (b), 1:9 "Does Job fear (יָרֵא) God for nothing?" is the frame's own question, which 28:28 answers no less than Eliphaz's.

**Markers** (design claim)

| Marker | Score |
|---|---|
| Formula | Strong for (b): 28:28 repeats the frame's pair "fear" + "turn from evil" (1:1, 8; 2:3) in Hebrew and Greek |
| Paragraphing | Possible: 28:28 closes with ס; 42:5 lies inside 42:2–6 |
| Vocabulary profile | Strong (שֵׁמֶץ HB-exclusive; שֵׁמַע only 28:22, 42:5 in Job; יִרְאָה five verses) |
| Greek | Possible (supports the frame tie; omits 26:14b and the ears in 28:22; no "fear" at 22:4) |
| Verbal architecture | Possible for (a) (hear-then-see inside 28 is real; ear-and-eye is common in Job); Possible for (b) (the one-per-speech spread is within chance expectation) |

**Verdict.** (a) Confirmed with nuance. (b) Confirmed with nuance: the frame tie is strong; the "one per Eliphaz speech" pattern is real but not beyond chance.

**Final rating.** (a) Words high; the 4:12 → 26:14 → 28:22 → 42:5 line moderate. (b) Words high; 28:28 → 1:1, 8; 2:3 high; Eliphaz series moderate.

**Reasoning.** Every lexical statement verifies. But hearing-then-seeing is a Job idiom (13:1, 29:11), and an exclusive noun shared by 28:22 and 42:5 within a 42-chapter book is a modest datum. The fear line is strongest where it ties 28:28 to the narrator's and the LORD's description of Job, a tie the Greek translator also made.

**What a preacher may safely say.** "Job 28 ends with the very words the book used of Job at the start: fearing God and turning from evil. Eliphaz kept raising Job's 'fear' in each speech; the poem says what that fear actually is."

#### C3: Job 28 bound to 22:24–28, 26:6–14 and 38:24–28 (internal window test), with 23:3, 10

**Claim (as tested).** Job 28 has 86 rare lemmas (in up to 150 WLC verses); across 878 five-verse windows elsewhere in Job the mean overlap is 1.55 (SD 1.29); three windows tie at the top with six: 22:24–28, 26:6–10, 38:24–28. Specific answers: 26:14 יִתְבּוֹנָן ("understand") → 28:23 הֵבִין; קָצָה ("end, fringe") in Job only 26:14, 28:24; 28:26b = 38:25b; אוֹפִיר ("Ophir") in Job only 22:24, 28:16; ידע + מצא ("know" + "find") in Job only 23:3, 28:13; דֶּרֶךְ + עִמָּדִי only 23:10, with עִמָּדִי at 28:14. Proposed: moderate–high.

**Evidence**

- [T] The window test reproduces exactly (WLC, 5-verse windows within Job, chapter 28 excluded, words in at most 150 verses): 86 rare lemmas, 878 windows, mean 1.55, SD 1.29; top three at 6: 22:24–28 (אוֹפִיר "Ophir", אוֹר "light", אָז "then", נַחַל "torrent", עָפָר "dust", צוּר "rock"), 26:6–10 (אֲבַדּוֹן "Abaddon", בקע "split", אוֹר, חֹק "limit", חֹשֶׁךְ "darkness", תַּכְלִית "limit"), 38:24–28 (אוֹר, חֲזִיז "thunderbolt", אֵי "where", יֵשׁ "there is", מוֹצָא "source", מָטָר "rain"). Three of the eighteen are function words (אָז, אֵי, יֵשׁ). Next come 14:4–8 and 14:7–11 at 5 (tree, root, dust, water), a passage nobody proposes as a partner.
- [T] **Null, whole chapters.** Running the same test on each other Job chapter as target (its own chapter excluded) gives top-window z-scores from 3.13 to 5.91. Job 28's top window is z = (6 – 1.55)/1.29 = 3.46; **26 of 36** comparable chapters have a more prominent top neighbour. Job 28's best internal neighbours are less prominent than most chapters' are.
- [T] **Topic control** (as the claim asked). 38:1–28: 85 rare lemmas, mean 1.88, SD 1.40, top 8 (3:5–9, and 40:6–10), z = 4.37. 26:5–14: 42 rare, mean 0.66, SD 0.86, top 4 (17:9–13; 37:7–11), z = 3.88. Both comparison poems have more prominent neighbours than Job 28 does, and 38's top partner is chapter 3 (light and darkness). The top windows reflect shared cosmological and mineral vocabulary.
- [T] Specific links, each verified (WLC): the consonants of וְדֶרֶךְ לַחֲזִיז קֹלוֹת occur at Job 28:26, 38:25 only: "And a course for the thunderbolt" / "Or a way for the thunderbolt". חֲזִיז ("thunderbolt") HB: 28:26, 38:25, Zech 10:1. This three-word verbatim half-line is the strongest single tie in the claim. אוֹפִיר ("Ophir") in Job: 22:24, 28:16 (12 HB verses). קָצָה ("end, fringe") in Job: 26:14 ("the fringes (קְצוֹת) of His ways"), 28:24 ("the ends (לִקְצוֹת) of the earth"); 30 HB verses; the cognate קָצֶה has no Job hit, so nothing is hidden; קֵץ ("end") is 28:3. The referents differ (His ways; the earth). בִּין ("understand") occurs in 23 Job verses: 26:14 → 28:23 is weak. ידע ("know") + מצא ("find") in one verse of Job: 23:3, 28:13; the two verbs share 24 HB verses (874 and 425 verses each): weak. דֶּרֶךְ ("way") + עִמָּד ("with me") in one verse: Gen 28:20, 35:3, Job 23:10, Ps 101:6, so "only 23:10" holds only within Job; עִמָּדִי ("with me") occurs in 14 Job verses: the 28:14 link is negligible.
- [T] A better form of the 23:10 link: ידע + דֶּרֶךְ ("know" + "way") in Job only 23:10 ("He knows the way I take") and 28:23 ("God understands its way, And He knows its place"); 47 HB verses, so exclusive within Job only. BHS apparatus at 28:13: "G ὁδὸν αὐτῆς, prp דַּרְכָּהּ" (the Greek reads "its way" for עֶרְכָּהּ, "its value"). [I] In the Greek, 23:10 οἶδεν … ὁδόν μου, 28:13 οὐκ οἶδεν βροτὸς ὁδὸν αὐτῆς, 28:23 οἶδεν … τὴν ὁδόν: a know-the-way line that the Greek makes explicit.
- [T] 22:24–25 and 28 share a cluster within one semantic field: gold of Ophir, dust (עָפָר), rock (צוּר), torrents (נַחַל), silver (כֶּסֶף, 22:25; 28:1, 15). Eliphaz: "the Almighty will be your gold" (22:25); the poem: "It cannot be valued in the gold of Ophir" (28:16). The function contrast is apt; the overlap is that of the subject.
- [I] Greek: Rahlfs asterisks 22:24b (the Ophir line), 26:14b (the שֵׁמֶץ line) and 28:26b ("and a way in the shaking of voices"); 38:25b (ὁδὸν δὲ κυδοιμῶν) is Old Greek. So the Old Greek lacked the Ophir line of 22:24 and the 28:26b half of the verbatim tie; the Greek reader did not have these links.

**Baseline.** Stated above: Job-internal five-verse windows, words in at most 150 verses, with a whole-chapter null (36 chapters) and two topic controls. The window result does not beat the null.

**Rival sources.** Zophar 11:6–9 (see C1): תַּעֲלֻמָה ("hidden thing", Job only 11:6 and 28:11), חָכְמָה ("wisdom"), תַּכְלִית; window 11:5–9 shares 3 rare lemmas with 28 but they are among the rarest in the set. Chapter 14 (tree, root, dust, water) matches 26:6–10 almost as closely, which shows the window ranks are topic-driven.

**Markers** (design claim)

| Marker | Score |
|---|---|
| Formula | Strong for 28:26b = 38:25b only |
| Paragraphing | Weak (no marker evidence either way) |
| Vocabulary profile | Weak (window prominence below the Job-chapter null; topic controls higher) |
| Greek | Weak (Old Greek lacked 22:24b, 26:14b and 28:26b) |
| Verbal architecture | Possible (Ophir/gold contrast; know-the-way 23:10 / 28:23) |

**Verdict.** Needs reframing.

**Final rating.** Window test: does not support design. Specific links: 28:26b = 38:25b high; Ophir 22:24–25 / 28:16 moderate; ידע + דֶּרֶךְ 23:10 / 28:23 moderate; קָצָה 26:14 / 28:24 low–moderate; בִּין, ידע + מצא, עִמָּדִי low. Overall "meeting point" claim: low–moderate.

**Reasoning.** The numbers reproduce, but a top overlap of 6 on a mean of 1.55 is less prominent than the top neighbour of most Job chapters, and two other cosmological poems do better on the same test. The poem's relation to 22, 26 and 38 has to rest on particular lines, of which the verbatim thunderbolt half-line and the gold-of-Ophir contrast carry weight; the 23:3 and 28:14 links are too common to bear it.

**What a preacher may safely say.** "Eliphaz told Job that if he put away his gold of Ophir, the Almighty would be his gold; the poem says wisdom cannot be bought with gold of Ophir. And the poem's line about God making 'a course for the thunderbolt' comes back word for word when God speaks from the storm."

#### C4: Who speaks chapter 28, and the frame (structure / attribution)

**Claim (as tested).** As the text stands the poem lies within Job's discourse, in a voice above the dispute. Markers: (i) וַיֹּסֶף אִיּוֹב שְׂאֵת מְשָׁלוֹ ("And Job again took up his discourse") only 27:1, 29:1, Greek identical; (ii) 27:1 follows Job's own 26:1–14, so 29:1 cannot show another voice spoke 28; (iii) BHS has no marker in 27 (last ס after 26:14), פ after 28:11 and 28:19, ס after 28:28; (iv) 28:1 opens with כִּי and silver; כֶּסֶף + עָפָר only 27:16 and Zech 9:3; מָקוֹם 27:21, 23 → 28:1, 6, 12, 20, 23; (v) no first or second person in the poem outside quoted speech; (vi) Greek 28:10 "my eye saw"; (vii) 28:28 opens with a wayyiqtol and names אֲדֹנָי, its only occurrence in Job in BHS. Option B (narrator) possible; Option C (Zophar) no marker. Proposed: within Job's discourse, moderate.

**Evidence**

- [T] (i) The consonants of וַיֹּסֶף אִיּוֹב שְׂאֵת מְשָׁלוֹ ("Then Job continued his discourse") occur at Job 27:1, 29:1 only (WLC). נשׂא + מָשָׁל ("take up a discourse") elsewhere: Num 23:7, 18; 24:3, 15, 20, 21, 23 (Balaam); Isa 14:4; Mic 2:4; Hab 2:6: the idiom of an oracle or taunt-song, not of dialogue. [I] Swete and Rahlfs 27:1 and 29:1 are identical: Ἔτι δὲ προσθεὶς Ἰὼβ εἶπεν τῷ προοιμίῳ ("And Job, continuing, spoke in his discourse").
- [T] (ii) Verified: 26:14 ends with ס, then 27:1. The reintroduction of a speaker with no intervening voice is a pattern in the book: Elihu is reintroduced at 34:1 (after his own 33:33), 35:1 (after 34:37) and 36:1, וַיֹּסֶף אֱלִיהוּא ("And Elihu continued"), after 35:16. So 29:1, like 27:1 and 36:1, can mark a resumed discourse; it cannot by itself show that someone else spoke 28.
- [T] (iii) BHS paragraph markers, whole book (the BHS export, 38 markers): in 22–31 they fall at 22:30 פ, 24:25 ס, 25:6 פ, 26:14 ס, 28:11 פ, 28:19 פ, 28:28 ס, 31:7 פ, 31:40 פ. Nothing in 23, 27, 29 or 30. **Every one of the 28 speech-introduction formulas in Job (3:2 … 42:1) is preceded by a BHS marker**; there is no unmarked change of speaker anywhere in the book. All 14 chapter ends that fall inside a speech (4:21, 6:30, 9:35, 12:25, 13:28, 16:22, 23:17, 27:23, 29:25, 30:31, 32:22, 36:33, 38:41, 40:32) are unmarked, and 27:23 is one of them. The Masoretic layout treats 27:23 → 28:1 as a boundary inside one discourse. (The WLC has an extra ס at 19:29 not shown in the BHS export; it does not affect 22–31.)
- [T] Speech-internal markers in the poetry are rare: 28:11, 28:19 and 31:7 only. Two of the three fall inside 28, before each refrain ("But where can wisdom be found?", 28:12; 28:20). The layout marks the poem as a structured unit, but not as a new speaker.
- [T] (iv) כֶּסֶף ("silver") + עָפָר ("dust") in one verse: Job 27:16, Zech 9:3 (exclusive in the Hebrew Bible); 28:1 has כֶּסֶף ("silver"), 28:2 עָפָר ("dust"). מָקוֹם ("place") in Job 26–29 = 27:21, 23; 28:1, 6, 12, 20, 23 (WLC). 28:1 is the only chapter-initial כִּי in Job. But the syntax כִּי יֵשׁ לְ- ("for there is … for") has an exact parallel inside Job's own speech: 14:7 כִּי יֵשׁ לָעֵץ תִּקְוָה ("For there is hope for a tree"), opening a new stanza in mid-speech; 28:1 כִּי יֵשׁ לַכֶּסֶף מוֹצָא ("Surely there is a mine for silver"). [I] Rahlfs asterisks 27:21b and 27:23b, the two "place" lines of 27: the Old Greek lacked them.
- [T] (v) Reading every verse of 28 (WLC): first-person forms occur only inside quoted speech (28:14 בִי "in me", עִמָּדִי "with me", spoken by the Deep and the Sea; 28:22 בְּאָזְנֵינוּ שָׁמַעְנוּ "with our ears we have heard", Abaddon and Death); there is no second person. But 27 is not uniform: 27:2–12 has first and second person ("I will instruct you", 27:11; "you have all seen it", 27:12), while 27:13–23 is entirely third person, as 28 is. The person shift occurs at 27:13, not at 28:1, so this marker does not separate 28 from what precedes.
- [I] (vi) Swete 28:10 πᾶν δὲ ἔντιμον ἴδεν μου ὁ ὀφθαλμός, Rahlfs εἶδέν μου ὁ ὀφθαλμός ("my eye saw every precious thing"); not asterisked, so Old Greek. The BHS apparatus has **no note at 28:10** (its Job 28 notes are at 2, 12, 13, 15, 23, 28). "Reading עֵינִי for עֵינוֹ" is a plausible inference (yod/waw), not a recorded variant. The Old Greek reader nonetheless met a first-person speaker in 28, and the only speaker in view is Job.
- [T] (vii) אֲדֹנָי ("the Lord") in Job: 28:28 only (WLC). BHS apparatus 28:28: "ᶜ mlt Mss יהוה; pc Mss pr יהוה; > 2 Mss": many manuscripts read יהוה for אֲדֹנָי. Elsewhere in the poetic dialogue יהוה occurs only at 12:9 (Job). So "only אֲדֹנָי in Job" is true of the Leningrad text, not of the tradition. Wayyiqtol forms introducing speech inside poetry: 11:4, 22:29, 28:28, 29:18, 33:24, 33:27, 36:10, 38:11. The closest is 38:11, God recalling creation: וָאֹמַר ("And I said, 'Thus far you shall come …'") after setting the sea's bounds (38:10). 28:28 follows the same creation sequence (28:25–27: "When He set a limit for the rain … Then He saw it … and searched it out"), so וַיֹּאמֶר is the next step of that narrative, not a narrator's frame breaking in.
- [T] Option C (Zophar): no formula, no marker, no apparatus note at 27:13 or 28:1, and the Greek has the same structure. One relevant note elsewhere: at 25:1 BHS records "ᵃ–ᵃ Ms אִיּוֹב", one manuscript reading "And Job answered" for "Bildad the Shuhite". That is a single manuscript, and it moves in the opposite direction (more Job, not more friends).
- [T] Vocabulary profile: I built a speaker profile (share of a target's rare lemmas found in repeated 15-verse samples of each speaker's corpus, target excluded) and ran it on 25 passages of known speaker (14 of Job, 3 Eliphaz, 2 Bildad, 2 Zophar, 2 Elihu, 2 YHWH). It named the right speaker in only **8 of 25** (Job's speeches 2 of 14; Zophar 0 of 2). Rare vocabulary in Job follows topic, not speaker, so it cannot attribute 28 at all; the poem's result (Zophar and YHWH tied, 6.4%; Job 5.3%) means nothing.

**Markers**

| Marker | Score |
|---|---|
| Formula | Strong (27:1 and 29:1 frame 27–28 as Job's resumed discourse; continuation formulas elsewhere need no intervening voice) |
| Paragraphing | Strong (every speaker change in Job is marked; 27:23 → 28:1 is unmarked like every other within-speech chapter break) |
| Vocabulary profile | Weak (the method fails its controls; it decides nothing) |
| Greek | Possible (Old Greek 28:10 "my eye" puts a first-person speaker in the poem; no Greek marker of a new voice) |
| Verbal architecture | Possible (silver + dust 27:16 → 28:1–2; "place" 27:21, 23 → 28; כִּי יֵשׁ as at 14:7) |

**Verdict.** Confirmed with nuance.

**Final rating.** Within Job's discourse as the text stands: moderate–high. "A voice above the dispute": moderate (a tone judgement, supported by the third person and the internal markers, but not a marker of a different speaker). Option B possible but unmarked; Option C has no textual support.

**Reasoning.** The paragraphing test is stronger than the claim stated it: the Masoretic tradition marks every change of speaker in Job, and it marks none at 28:1. Two of the claim's markers need correcting: the person shift is at 27:13, not 28:1, and the אֲדֹנָי of 28:28 is יהוה in many manuscripts. The wayyiqtol at 28:28 belongs to the creation narrative of 28:25–27, as at 38:11, and is no sign of a narrator.

**What a preacher may safely say.** "As the Hebrew text stands, chapter 28 is part of Job's continuing discourse; no new speaker is introduced, and the old scribes marked no break. But the tone changes: Job stops arguing and speaks about wisdom in a voice above the quarrel."

#### C5: Are 24:18–25 and 27:13–23 Job's words? (the "disorder" question)

**Claim (as tested).** These passages "sound like the friends' doctrine in Job's mouth". 27:13 opens with Zophar's closing words זֶה חֵלֶק־אָדָם רָשָׁע ("This is the portion of a wicked man"), the four-word phrase only at 20:29 and 27:13, the rest of each verse different. Option A: disorder (parts of 24–27 belong to Bildad and Zophar). Option B: the breakdown is the point (Job takes up the friends' lines, to parody or to concede the doctrine while denying its application). ESV inserts "You say," at 24:18; NASB95 and NIV84 print the passage as Job's. The MT attributes 26–31 to Job. Proposed: contested; the text attributes both to Job; disorder not demonstrated.

**Evidence**

- [T] The consonants of זֶה חֵלֶק־אָדָם רָשָׁע ("This is the portion of a wicked man") occur at Job 20:29, 27:13 only (WLC). The overlap is larger than stated: both b-lines also open with וְנַחֲלַת ("and the heritage of") and both end with a divine name governed by מִן (20:29 מֵאֵל "from God"; 27:13 מִשַּׁדַּי "from the Almighty"); the a-lines differ only in מֵאֱלֹהִים / עִם־אֵל. חֵלֶק + נַחֲלָה in one verse in Job: 20:29, 27:13, 31:2 (18 HB verses). [I] The Greek a-lines are verbatim: αὕτη ἡ μερὶς ἀνθρώπου ἀσεβοῦς παρὰ κυρίου ("This is the portion of an ungodly man from the Lord") at 20:29 and 27:13 (Swete, Rahlfs). 20:29 closes Zophar's second speech (BHS פ).
- [T] (i) **Vocabulary profile against the friends' portraits** (15:20–35; 18:5–21; 20:5–29), WLC rare lemmas, sliding windows of the same length:

| Target | Frequency ceiling | shared with portraits | Job's undisputed speeches: windows reaching it | friends' other speeches: windows reaching it |
|---|---|---|---|---|
| 24:18–25 (8 vv.) | 150 | 3 | 256 of 312 (82%) | 155 of 195 (79%) |
| 24:18–25 | 400 | 3 | 307 of 312 (98%) | 194 of 195 (99%) |
| 27:13–23 (11 vv.) | 150 | 9 | 46 of 258 (18%) | 17 of 162 (10%) |
| 27:13–23 | 400 | 20 | 0 of 258 (max 19) | 0 of 162 (max 17) |

24:18–25 has **no** friends'-portrait profile: it shares less with those portraits than most of Job's own windows do. 27:13–23 does stand out at a 400-verse ceiling, but the topic control explains it: Job's own chapter 21 (on the fate of the wicked) reaches 19 in an 11-verse window (21:16–26), within one of 27:13–23. The 20 shared items include בַּלָּהוֹת ("terrors"), חֶרֶב ("sword"), מָוֶת ("death"), עָפָר ("dust"), מָקוֹם ("place"), שָׂרִיד ("survivor"), עָרִיץ ("tyrant"), חֵלֶק ("portion") and נַחֲלָה ("heritage"): the vocabulary of the subject. So 27:13–23 talks about what the friends talked about, as Job does in 21; vocabulary cannot say who is talking. The general speaker profile (C4) failed its controls (8 of 25) and is no help here.
- [T] (ii) **Signs of quotation.** 24:18–25 has no verb of saying, no second person and no imperative to the friends, and it ends in Job's first person: "Now if it is not so, who can prove me a liar, And make my speech (מִלָּתִי) worthless?" (24:25), which claims what precedes as his own speech. 27:13 follows directly on 27:11–12, addressed to the friends in the second person plural: "I will instruct you (אוֹרֶה אֶתְכֶם) in the power of God … Behold, all of you have seen it; Why then do you act foolishly (הֶבֶל תֶּהְבָּלוּ)?" 27:13–23 can be read as the content of that instruction or as the friends' own doctrine handed back ("you have all seen it"); the text does not mark which.
- [T] **A precedent for unmarked quotation in Job's mouth.** 21:19 has no verb of saying in Hebrew (אֱלוֹהַּ יִצְפֹּן־לְבָנָיו אוֹנוֹ "God stores away his iniquity for his sons"), yet NASB95 supplies "You say", ESV "You say" and NIV84 "It is said"; two verses later Job says so outright, כִּי תֹאמְרוּ ("For you say", 21:28). So Job does cite the friends' doctrine without a marker, and all three versions recognise it at 21:19. At 24:18 only the ESV supplies "You say"; NASB95 ("They are insignificant on the surface of the water") and NIV84 ("Yet they are foam on the surface of the water") do not. The ESV's choice has a textual analogy but no word in the Hebrew; for a congregation hearing the ESV, the attribution is the translator's.
- [I] (iii) **Greek.** Rahlfs asterisks 24:14b, 15b–c, 16b–c, 17b and 24:18a, closing with the metobelus after 24:18a: the Old Greek lacked most of 24:14b–18a, including the line that the ESV prefixes with "You say". 24:18b–24 is Old Greek and is rendered as **wishes**: καταραθείη ἡ μερὶς αὐτῶν ("may their portion be cursed"), ἀναφανείη ("may [their plants] appear [dry]"), ἀποδοθείη ("may it be repaid to him"), συντριβείη ("may every unrighteous one be broken"). The translator read 24:18–24 as Job's own imprecation on the wicked, not as a quotation of the friends. In 27:13–23 Rahlfs asterisks only the b-lines of 27:19, 21, 22 and 23; the a-lines are Old Greek, with no change of speaker.
- [T] Masoretic markers: no paragraph marker within 24 (the next is ס at 24:25) or 27 (none). Apparatus for 24 and 27 has only word-level notes (e.g. 24:24 "G ὥσπερ μολόχη = כְּמַלּוּחַ"; 27:18, 27:19); no note proposes a speaker change. The only speaker-level note in 22–28 is at 25:1 ("Ms אִיּוֹב", one manuscript reading Job for Bildad).

**Baseline.** Stated in the table: Job's undisputed speeches (excluding 27 and 24:13–25) and the friends' other speeches, sliding windows of equal length, at two rarity thresholds, with Job 21 as a topic control.

**Rival sources.** For 27:13, Zophar's 20:29 is the only verbal source, and it is close (a-line nearly verbatim, b-line parallel). For 24:18–25 there is no special tie to the friends' portraits.

**Markers**

| Marker | Score |
|---|---|
| Formula | Strong for the text as it stands (26:1, 27:1, 29:1 give 26–31 to Job; no counter-formula); 27:13 = 20:29a is a quoted formula |
| Paragraphing | Strong (no marker in 24 before 24:25, none in 27; every speaker change elsewhere is marked) |
| Vocabulary profile | Weak (24:18–25 has no friends' profile; 27:13–23's overlap is matched by Job 21) |
| Greek | Possible (the Old Greek renders 24:18–24 as Job's own wishes; lacks 24:18a; no speaker change in 27) |
| Verbal architecture | Possible (27:11–12 address frames 27:13–23 as instruction or rebuttal; 24:25 claims 24:18–24 as Job's speech) |

**Verdict.** Confirmed with nuance.

**Final rating.** The text as it stands attributes both passages to Job: high. Disorder (Option A): not demonstrated; no textual marker supports it. Option B (Job takes up the friends' lines): possible for 27:13–23 (the 20:29 citation, the address in 27:11–12, the precedent of 21:19 and 21:28); weak for 24:18–25, whose vocabulary is not the friends' and which Job claims as his own (24:25).

**Reasoning.** The claim is right that the text cannot demonstrate disorder, and the markers lean further toward Job than the claim states. The two passages should be separated: 27:13 visibly cites Zophar's last line, and Job elsewhere quotes the friends without a marker, so a citation reading of 27:13–23 has textual grounds; 24:18–25 has none, and its oldest Greek reading makes it Job's prayer against the wicked.

**What a preacher may safely say.** "In 27:13 Job picks up, almost word for word, the line with which Zophar ended his last speech. Whether he is quoting them in order to answer them, or agreeing that God judges the wicked while denying that this explains his own case, he is still speaking in his own voice."

#### C6: The third cycle breaks down, and the breakdown is the point

**Claim (as tested).** Bildad's last speech is six verses (25:1–6) and 25:4 repeats 9:2 exactly (וּמַה־יִּצְדַּק אֱנוֹשׁ עִם־אֵל, "how can a man be just with God?"); Zophar has no third speech (וַיַּעַן צֹפַר only 11:1, 20:1); 32:1–5 narrates the friends' silence. The shortening is design: the human debate exhausts itself before 28 and before God speaks. Proposed: breakdown as the text stands high; as design moderate–high.

**Evidence**

- [T] The consonants of וּמַה־יִּצְדַּק אֱנוֹשׁ עִם־אֵל occur at Job 9:2, 25:4 only (WLC). Correction: the repetition is of a **half-line**, 9:2b = 25:4a ("But how can a man be in the right before God?"); 9:2a (אָמְנָם יָדַעְתִּי כִי־כֵן, "In truth I know that this is so") is not repeated.
- [T] The rest of 25:4–6 is built from Eliphaz. 25:4b וּמַה־יִּזְכֶּה יְלוּד אִשָּׁה ("Or how can he be clean who is born of woman?") answers 15:14 מָה־אֱנוֹשׁ כִּי־יִזְכֶּה וְכִי־יִצְדַּק יְלוּד אִשָּׁה; צדק + זכה + יָלוּד in one verse only 15:14 and 25:4 (WLC). 25:5 לֹא־זַכּוּ בְעֵינָיו ("are not pure in His sight") = 15:15b verbatim (the consonant search returns 15:15, 25:5 only). The sequence הֵן … לֹא … אַף כִּי ("Behold … not … how much less") at 25:5–6 is that of 15:15–16 and 4:18–19. So 25:4–6 combines a line of Job (9:2b) with Eliphaz's argument from the heavens to the worm (4:17–19; 15:14–16).
- [T] **Baseline for repetition.** For each speech in the book, I counted the consonantal word trigrams and four-word sequences that already occur in an earlier speech (WLC). Bildad's third speech: 4 of 29 trigrams (13.8%), 2 of 24 four-word sequences (8.3%), in 2 of 5 verses. Every other speech in Job: at most 1.7% (trigrams) and 1.0% (four-word). Bildad 25 is about eight times as derivative as any other speech in the book. "Bildad has nothing new to say" is measurable.
- [T] Speech lengths (verses of speech, formula excluded; WLC): Round 1: Eliphaz 47, Bildad 21, Zophar 19 (Job 50, 56, 74). Round 2: Eliphaz 34, Bildad 20, Zophar 28 (Job 37, 28, 33). Round 3: Eliphaz 29, **Bildad 5**, **Zophar none** (Job 41 in 23–24, 13 in 26, 22 in 27, then 28 and 29–31). The friends' totals fall from 87 to 82 to 34 verses.
- [T] The phrase וַיַּעַן צֹפַר ("then Zophar answered") occurs at 11:1, 20:1 only (positive control: the same search finds both earlier formulas). No third Zophar formula.
- [T] **A formula marker the claim missed.** The speech formula in the dialogue is וַיַּעַן X וַיֹּאמַר ("And X answered and said"). The last friend's formula is 25:1; Job's last "answer" in the dialogue is 26:1. Job's next two speeches are introduced differently: וַיֹּסֶף אִיּוֹב שְׂאֵת מְשָׁלוֹ ("And Job again took up his discourse", 27:1; 29:1). Job no longer "answers", because no one has spoken. וַיַּעַן with Job returns only when the LORD has spoken (40:3; 42:1).
- [T] 32:1–5 names the end in the vocabulary of the formula: וַיִּשְׁבְּתוּ … מֵעֲנוֹת אֶת־אִיּוֹב ("these three men ceased answering Job", 32:1; שׁבת "cease" occurs only here in Job); לֹא־מָצְאוּ מַעֲנֶה ("they had found no answer", 32:3); אֵין מַעֲנֶה ("there was no answer", 32:5); מַעֲנֶה ("answer") occurs in Job only at 32:3, 5. Elihu repeats it: "they no longer answer (לֹא־עָנוּ עוֹד)" (32:15, 16). The echo is to the verb of the speech formulas, not to particular words of the third round.
- [T] **Signals of displacement.** Paragraphing: 24:25 ס, 25:6 פ, 26:14 ס, normal speech-end markers, none inside 25–27. BHS apparatus for 24–27: word-level notes only, except at 25:1: "ᵃ–ᵃ Ms אִיּוֹב" (one manuscript reads "And Job answered" for "And Bildad the Shuhite answered"). That single manuscript would remove Bildad's third speech altogether, the opposite of a reconstruction that gives 26 or 27 to the friends. [I] Greek: 25:1, 26:1, 27:1 have the same speaker formulas (Ὑπολαβὼν δὲ Βαλδαδ ὁ Σαυχίτης λέγει; Ὑπολαβὼν δὲ Ιωβ λέγει; Ἔτι δὲ προσθεὶς Ιωβ…); no Greek witness here supplies a Zophar speech. Rahlfs asterisks many b-lines in 26:5–14, so the Old Greek's 26 was shorter, but its speaker was the same.

**Baseline.** Repetition: all 25 speeches in Job as the comparison set (stated above). Lengths: the three rounds as data, without a probability claim.

**Rival sources.** No rival source; the rival is an explanation: the scholarly view (recalled, not checked here) that the third cycle is damaged. The text supplies no positive evidence for that view in the Masoretic layout, the apparatus or the Greek; it can neither exclude it nor show it.

**Markers**

| Marker | Score |
|---|---|
| Formula | Strong (no third Zophar formula; the "answer" formula stops after 26:1 and Job "continues his discourse" at 27:1, 29:1) |
| Paragraphing | Strong (normal speech-end markers at 24:25, 25:6, 26:14; nothing suggests displacement) |
| Vocabulary profile | Strong (Bildad 25 is by far the most derivative speech in the book: 13.8% repeated trigrams against at most 1.7% elsewhere) |
| Greek | Possible (same speaker structure; no evidence of a lost speech) |
| Verbal architecture | Strong (32:1–5 names the cessation with the formula verb ענה) |

**Verdict.** Confirmed with nuance (25:4 repeats a half-line, not the whole of 9:2).

**Final rating.** Breakdown as the text stands: high. As design: moderate–high; the text marks the breakdown in three independent ways (Bildad's borrowed lines, the change of formula, the narrated silence), though no text can prove intention against a theory of accidental damage.

**Reasoning.** The claim's data verify and the formula change and the repetition count strengthen it: the book itself registers that the friends have run out of words, and says so in 32:1–5. The only manuscript evidence touching a speaker in this section points away from a redistribution to the friends. Design is the best reading of the text as it stands, but it is an inference from the text's own markers, not a demonstration.

**What a preacher may safely say.** "By the third round the friends have run dry: Bildad's last speech is five verses, and half of it is borrowed from Job and from Eliphaz; Zophar does not speak at all. The narrator says it plainly: 'these three men ceased answering Job.'"

#### C7: Eliphaz quotes Job back at him (21:14–16 → 22:17–18), and Job answers Eliphaz (22:22 → 23:12)

**Claim (as tested).** (a) "They say to God, 'Depart from us! …' … The counsel of the wicked is far from me" (21:14, 16) is put back into Job's mouth by Eliphaz (22:17–18). Proposed: high (self-quotation). (b) Eliphaz: "Please receive instruction (תּוֹרָה) from His mouth And establish His words (אֲמָרָיו) in your heart" (22:22); Job: "I have treasured the words of His mouth (אִמְרֵי־פִיו) more than my necessary food" (23:12). תּוֹרָה only here in Job. Proposed: high. Test whether these make the third round a set of pointed rejoinders.

**Evidence**

- [T] (a) Exact wording (WLC): 21:14 וַיֹּאמְרוּ לָאֵל סוּר מִמֶּנּוּ ("They say to God, 'Depart from us!'") / 22:17 הָאֹמְרִים לָאֵל סוּר מִמֶּנּוּ ("They said to God, 'Depart from us!'"); The consonants of לָאֵל סוּר מִמֶּנּוּ occur at 21:14, 22:17 only. 21:16b עֲצַת רְשָׁעִים רָחֲקָה מֶנִּי = 22:18b verbatim; The consonants of עֲצַת רְשָׁעִים רָחֲקָה מֶנִּי occur at 21:16, 22:18 only. Around them: 21:15 מַה־שַׁדַּי ("What is the Almighty …?") / 22:17b וּמַה־יִּפְעַל שַׁדַּי ("What can the Almighty do …?"); 21:16a טוּבָם ("their prosperity") / 22:18a "He filled their houses (בָּתֵּיהֶם) with good things (טוֹב)"; בָּתֵּיהֶם ("their houses") in Job only 3:15, 21:9 ("Their houses are safe from fear"), 22:18. So 22:17–18 recomposes 21:9, 14–16: two verbatim strings and three further echoes in two verses.
- [T] **Who is speaking "far from me".** In 21:16 the "me" is Job, disowning the wicked. In 22:18 the "me" is Eliphaz: he repeats Job's disavowal as his own, after aligning Job with "the ancient path Which wicked men have trod" (22:15). Eliphaz does not put the words back into Job's mouth; he quotes the wicked as Job reported them and then takes Job's own disclaimer for himself. That is pointed (by implication: far from me, not from you), but it is appropriation, not "self-quotation" by Job.
- [T] BHS apparatus 22:17: "ᵃ prp לָנוּ cf G S": the Greek and Syriac read "What will the Almighty do to us?", which would continue the wicked's own speech as in 21:15. [I] The Greek does not carry the verbatim tie: 21:14 Ἀπόστα ἀπʼ ἐμοῦ ("Depart from me"), while 22:17 lacks the "Depart" clause (οἱ λέγοντες Κύριος τί ποιήσει ἡμῖν;); 21:16b ἔργα δὲ ἀσεβῶν οὐκ ἐφορᾷ ("he does not oversee the works of the ungodly") against 22:18b βουλὴ δὲ ἀσεβῶν πόρρω ἀπʼ αὐτοῦ ("the counsel of the ungodly is far from him"). Neither line is asterisked. The repetition is a feature of the Hebrew.
- [T] (b) תּוֹרָה ("instruction") in Job: 22:22 only (WLC; control: the same search across the Hebrew Bible returns 1 Chr 16:40 and others). מִצְוָה ("command") in Job only 23:12. פֶּה + אֵמֶר ("mouth" + "words") in one verse in Job: 8:2 (Bildad: "the words of your mouth (אִמְרֵי־פִיךָ) be a mighty wind"), 22:22, 23:12. The function matches: Eliphaz urges Job to receive God's words and lay them up; Job replies that he has already kept God's command and treasured His words (23:11–12, "I have kept His way and not turned aside. I have not departed from the command of His lips").
- [T] **A shared source of the idiom.** אֵמֶר + צפן + מִצְוָה ("words" + "treasure" + "commandments") in one verse only Job 23:12, Prov 2:1, Prov 7:1 (WLC); Prov 2:1 adds לקח ("receive"), which is Eliphaz's קַח (22:22): "My son, if you will receive my words And treasure my commandments within you" (Prov 2:1). Eliphaz's demand and Job's reply between them speak in the words of the Proverbs instruction formula, divided between two speakers. תּוֹרָה + מִצְוָה are a common pair (22 HB verses, including Prov 3:1; 6:20, 23; 7:2).
- [T] BHS apparatus 23:12: "ᵇ l frt בְּחֵקִי cf G V" (for מֵחֻקִּי, "more than my portion"); [I] Swete and Rahlfs ἐν δὲ κόλπῳ μου ἔκρυψα ῥήματα αὐτοῦ ("in my bosom I hid his words"). On the Greek reading, Job's line comes closer still to Eliphaz's "establish His words in your heart"; the Greek also has τὰ ῥήματα αὐτοῦ ("his words") in both 22:22 and 23:12.
- [T] **Baseline: are third-round junctions pointed rejoinders?** For every pair of speeches in the dialogue (3–27), I counted verbatim consonantal trigrams, content bigrams, and in-Job exclusive lemma pairs (words in at most 700 verses) shared between them, per 1000 verse-pairs. Adjacent junctions in rounds 1–2 (12 pairs): **no verbatim trigram at any of them**; content bigrams 0.10 per 1000. Third-round adjacent junctions: Job 21 → Eliphaz 22 has two verbatim trigrams (the two strings above), 4 content bigrams and 3 exclusive pairs, the only verbatim rejoinder at any adjacent junction in the book. Eliphaz 22 → Job 23–24: no verbatim trigram, 2 exclusive pairs (22:9/24:3 "widows" + "orphans"; 22:11/23:17 "darkness" + "cover"); 22:22 → 23:12 is lemma-level only. Job 23–24 → Bildad 25 and Bildad 25 → Job 26: nothing. The third round's other verbatim repetitions are not adjacent: Bildad 25 from Job 9:2 and Eliphaz 15:14–15; Job 27:13 from Zophar 20:29.

**Rival sources.** For (a), none: 21:14–16 is the only source. For (b), Prov 2:1 and 7:1 share a rarer triple with 23:12 than 22:22 does, and 8:2 shares פֶּה + אֵמֶר; so 22:22 → 23:12 is a reply in common instruction idiom, not an exclusive verbal link.

**Hays criteria** (for (a) and (b) together)

| Criterion | Score |
|---|---|
| Availability | Strong (adjacent speeches) |
| Volume | Strong for (a) (two verbatim strings, HB-exclusive); Possible for (b) (lemma-level; common idiom) |
| Recurrence | Possible (the third round also recycles 9:2, 15:14–15 and 20:29, but not at adjacent junctions) |
| Thematic coherence | Strong (the wicked's speech and Job's disavowal; receiving and keeping God's words) |
| Historical plausibility | Strong |
| History of interpretation | Not checked |
| Satisfaction | Strong for (a) as Eliphaz's appropriation of Job's words; Possible for (b) |

**Verdict.** (a) Confirmed with nuance (not self-quotation: Eliphaz repeats the wicked's words as Job reported them and claims Job's disavowal for himself). (b) Confirmed with nuance (a real reply, in shared instruction idiom). The generalisation "the third round is a set of pointed rejoinders": Needs reframing.

**Final rating.** (a) Verbal link high; "quotes Job back at him" moderate as characterised, high as "Eliphaz turns Job's own words". (b) Moderate. Third round as rejoinders: low as a pattern; the 21 → 22 junction is unique in the book.

**Reasoning.** The two verbatim strings in 22:17–18 are exclusive and are the only verbatim rejoinder at any adjacent junction in Job, so (a) is a real and deliberate-looking repetition; but the speaker of "far from me" in 22:18 is Eliphaz. The 22:22 → 23:12 reply is real in function but uses instruction language also found in Prov 2:1 and 7:1. The rest of the third round recycles earlier speeches rather than answering the one before.

**What a preacher may safely say.** "Eliphaz takes Job's own words, 'Depart from us' and 'the counsel of the wicked is far from me', and turns them: he says those words as if Job were the wicked man. Job answers that he has already done what Eliphaz demands: he has treasured the words of God's mouth."

### New candidates surfaced

1. **Zophar 11:6–7 → Job 28:3, 11–13** (answer to Zophar). תַּעֲלֻמָה ("hidden thing") occurs in WLC only Job 11:6 (תַּעֲלֻמוֹת חָכְמָה, "the secrets of wisdom"), 28:11 ("what is hidden he brings out to the light") and Ps 44:22 [Eng 44:21]. 11:7 is the only verse joining חֵקֶר ("searching") and תַּכְלִית ("limit"); 28:3 joins the verb חקר with תַּכְלִית; 11:7 asks twice "can you find (תִּמְצָא)", and 28:12–13 asks where wisdom "can be found (תִּמָּצֵא)". Zophar said no one reaches the limit of the Almighty; the poem's miner reaches "every limit", brings the hidden thing to light, and still cannot find wisdom. Rating: **moderate–high** (two rare ties plus matching function; Greek of 11:6–7 does not echo).
2. **Ps 114:8 and Deut 8:15 → Job 28:9–10** (the wilderness rock). הפך + חַלָּמִישׁ ("overturn" + "flint") only Job 28:9 and Ps 114:8; הפך + צוּר ("rock") only Ps 114:8 ("Who turned the rock into a pool of water, The flint into a fountain of water"); צוּר + חַלָּמִישׁ Deut 8:15; 32:13; Ps 114:8. Job 28:9–10 has הפך, חַלָּמִישׁ, צוּר, בקע ("split") and water-channels in two lines; C1's pair (iv) (Ps 78:15; Isa 48:21) is one strand of this cluster. Rating: **moderate** (direction open; the miner's acts in words used of God's wilderness provision).
3. **Job 12:22 → 28:3, 11** (beyond C1's pair). 12:22 has חֹשֶׁךְ, צַלְמָוֶת, יצא hiphil and אוֹר, all four found across 28:3–11. [I] The Greek translator heard it: ἀνακαλύπτω + βάθ- occurs only in Dan 2:22, Job 12:22 and 28:11 (Swete), and βάθ- in Job only at those two verses. Rating: **moderate** (Hebrew lemmas individually common; the Greek is reception evidence).
4. **Bildad 25:4b–6 built from Eliphaz 15:14–16 and 4:17–19.** 25:5b לֹא־זַכּוּ בְעֵינָיו = 15:15b (only these two, by consonants); צדק + זכה + יָלוּד only 15:14 and 25:4; the sequence הֵן … לֹא … אַף כִּי of 25:5–6 = 15:15–16 and 4:18–19. With 25:4a = 9:2b, half of Bildad's last speech is borrowed. Rating: **high**.
5. **The change of formula after 26:1 as a marker of the breakdown.** The dialogue's formula וַיַּעַן X וַיֹּאמַר ("X answered and said") is last used for Job at 26:1; 27:1 and 29:1 use וַיֹּסֶף אִיּוֹב שְׂאֵת מְשָׁלוֹ ("Job again took up his discourse"); "answered" returns for Job only after the LORD speaks (40:3; 42:1); 32:1, 3, 5 then narrate that the friends ceased "answering" (מֵעֲנוֹת; מַעֲנֶה only 32:3, 5 in Job). Rating: **high** (structural).
6. **ידע + דֶּרֶךְ ("know" + "way") 23:10 → 28:23.** In Job only 23:10 ("He knows the way I take") and 28:23 ("God understands its way, And He knows its place"); 47 HB verses. BHS at 28:13 records the Greek ὁδὸν αὐτῆς ("its way", proposing דַּרְכָּהּ). Job says God knows his way; the poem says God alone knows wisdom's way. Rating: **moderate** (replaces C3's weak עִמָּדִי link).
7. **Prov 2:1 and 7:1 behind 22:22 / 23:12.** אֵמֶר + צפן + מִצְוָה only Job 23:12, Prov 2:1, 7:1; Prov 2:1 adds לקח (Eliphaz's קַח, 22:22): "My son, if you will receive my words And treasure my commandments within you". Eliphaz and Job divide the instruction formula between them. Rating: **moderate** (shared idiom; direction open).
8. **Job 28:28 וַיֹּאמֶר and 38:11 וָאֹמַר: divine speech at creation inside poetry.** Both follow the setting of bounds at creation (28:25–27; 38:8–10). This reframes C4 (vii): the wayyiqtol continues the creation narrative, it does not signal a narrator. Rating: **moderate** (structural parallel; two cases).
9. **Job 14:7 כִּי יֵשׁ לָעֵץ תִּקְוָה → 28:1 כִּי יֵשׁ לַכֶּסֶף מוֹצָא.** The same opening (כִּי יֵשׁ לְ- + noun + noun) begins a new stanza inside Job's speech at 14:7, as 28:1 does after 27:23. Rating: **low–moderate** (supports C4; one parallel).

### Key evidence for spot checks

1. Positive control: חֶסֶד ("covenant-kindness") in Job returns 6:14; 10:12; 37:13 (WLC).
2. תַּכְלִית ("limit") + חֹשֶׁךְ ("darkness"): Job 26:10, 28:3; יצא ("bring out") + אוֹר ("light"): Hos 6:5, Isa 13:10, 51:4, Job 12:22, 28:11, Mic 7:9, Ps 37:6 (C1 pair (iii) is exclusive only within Job).
3. תַּעֲלֻמָה ("hidden thing") occurs at Job 11:6, 28:11, Ps 44:22; הפך ("turn") + חַלָּמִישׁ ("flint"): Job 28:9 and Ps 114:8 (new candidates 1 and 2).
4. Counting words in up to 700 verses, 28:1–11 has 4 Job-exclusive pairs with the hymns; 26 of 432 sliding 11-verse windows (6.0%) reach it, and 7 of 31 chapters (including 3, 7, 14, 24 at 5).
5. The internal window test for Job 28: 86 rare words, 878 windows, mean 1.55, SD 1.29, top score 6 (22:24–28, 26:6–10, 38:24–28). The whole-chapter null: Job 28 z = 3.46; 26 of 36 other chapters have a higher top-window z; 38:1–28 z = 4.37; 26:5–14 z = 3.88.
6. The consonants of וְדֶרֶךְ לַחֲזִיז קֹלוֹת ("and a course for the thunderbolt"): Job 28:26 and 38:25; Rahlfs 28:26b is asterisked, 38:25b is not.
7. Every one of the 28 speech formulas in Job is preceded by a BHS פ or ס; chapter 27 has no marker; BHS apparatus 28:28 "ᶜ mlt Mss יהוה"; no apparatus entry at 28:10.
8. The speaker vocabulary profile names the right speaker for 8 of 25 known passages (vocabulary cannot attribute 28, 24:18–25 or 27:13–23).
9. Counting words in up to 400 verses, 27:13–23 shares 20 rare lemmas with 15:20–35, 18:5–21, 20:5–29; Job 21's best 11-verse window (21:16–26) shares 19; 24:18–25 shares 3, reached by 307 of 312 Job windows.
10. Bildad 25:2–6 repeats 4 of 29 three-word strings (13.8%) from earlier speeches, against at most 1.7% for every other speech; the consonants of לָאֵל סוּר מִמֶּנּוּ occur at Job 21:14 and 22:17, and those of עֲצַת רְשָׁעִים רָחֲקָה מֶנִּי at Job 21:16 and 22:18; no verbatim three-word string occurs at any adjacent junction of rounds 1–2.

---

## Spot Checks

The main session re-ran the evidence on which each verdict turns. It used the same corpus, outside the auditors' sessions. **All 26 checks reproduced the auditors' results.** It then rebuilt the two verdicts that change the 28:1–28 dig most with searches written afresh: **one reproduced and one did not**, and the second is corrected below.

| # | Claim | Check (edition) | Result |
|---|---|---|---|
| 1 | all | Positive control: חֶסֶד in Job | 6:14; 10:12; 37:13 (WLC) — reproduced |
| 2 | A1 | חַלָּמִישׁ ("flint") + הפך ("overturn") in one verse | Job 28:9; Ps 114:8 only (WLC) — reproduced |
| 3 | A1 | בַּרְזֶל ("iron") + נְחֹשֶׁת ("copper") + אֶבֶן ("stone") | 1 Chr 22:14; 29:2; 2 Chr 2:13; Deut 8:9; Isa 60:17 (WLC) — reproduced |
| 4 | A1 | אֶרֶץ + לֶחֶם + אֶבֶן in one verse | Deut 8:9 only (WLC) — reproduced |
| 5 | A1 | נְחֹשֶׁת ("copper") in Job | none — Job uses נְחוּשָׁה (WLC) — reproduced |
| 6 | A5 | נָחָשׁ + בָּרִחַ ("fleeing serpent") | Isa 27:1; Job 26:13 only (WLC) — reproduced |
| 7 | A3 / C4 | אֲדֹנָי ("the Lord") in Job | 28:28 only (WLC; BHS prints the same, with "ᶜ mlt Mss יהוה") — reproduced |
| 8 | B4 | יִרְאָה + חָכְמָה in one verse | Isa 11:2; 33:6; Job 28:28; Prov 1:7; 9:10; 15:33; Ps 111:10 (WLC) — reproduced |
| 9 | B4 | יָרֵא (adj.) + סוּר + רַע | Job 1:1; 1:8; 2:3; Prov 14:16 (WLC) — reproduced |
| 10 | B4 | יִרְאָה (noun) + סוּר + רַע | Job 28:28; Prov 16:6 (WLC) — reproduced |
| 11 | B4 | ירא (verb) + סוּר + רַע | 1 Sam 12:20; Prov 3:7; Zeph 3:15 (WLC) — reproduced |
| 12 | B2 | פְּנִינִים + חָכְמָה in one verse | Job 28:18; Prov 8:11 only (WLC) — reproduced |
| 13 | B2 | חוּג ("circle", the noun) | Isa 40:22; Job 22:14; Prov 8:27 (WLC) — reproduced |
| 14 | B2 | חוּג ("inscribe a circle", the verb) | Job 26:10 only (WLC) — reproduced |
| 15 | B3 | פִּטְדָה ("topaz") | Exod 28:17; 39:10; Ezek 28:13; Job 28:19 (WLC) — reproduced |
| 16 | B3 | זָהָב + חָכְמָה in one verse | Ezek 28:4 only (WLC) — reproduced |
| 17 | C1 | תַּכְלִית + חֹשֶׁךְ in one verse | Job 26:10; 28:3 only (WLC) — reproduced |
| 18 | C1 | יצא + אוֹר in one verse, whole Hebrew Bible | Hos 6:5; Isa 13:10; 51:4; Job 12:22; 28:11; Mic 7:9; Ps 37:6 — exclusive only within Job (WLC) — reproduced |
| 19 | C (new) | תַּעֲלֻמָה ("hidden thing") | Job 11:6; 28:11; Ps 44:22 [Eng 44:21] (WLC) — reproduced |
| 20 | C3 | וְדֶרֶךְ לַחֲזִיז קֹלוֹת, exact | Job 28:26; 38:25 only (WLC) — reproduced |
| 21 | C7 | לָאֵל סוּר מִמֶּנּוּ, exact | Job 21:14; 22:17 only (WLC) — reproduced |
| 22 | C7 | עֲצַת רְשָׁעִים רָחֲקָה מֶנִּי, exact | Job 21:16; 22:18 only (WLC) — reproduced |
| 23 | C5 | זֶה חֵלֶק־אָדָם רָשָׁע, exact | Job 20:29; 27:13 only (WLC) — reproduced |
| 24 | B1 | Window rank against Job 28:20–28, 5-verse windows, words in at most 150 verses | Prov 2:1, Prov 8:10 and 1 Chr 22:10 **tied at 4** (WLC) — reproduced |
| 25 | A1 | Deut 8 rank against Job 28:1–11, 10-verse windows, words in at most 800 verses | 2nd of 887 (WLC) — reproduced |
| 26 | B1 | Prov 2 rank against Job 28:1–13, 5-verse windows, words in at most 150 verses | 223rd (WLC) — reproduced |

**Independent rebuild 1 — C3, the internal window test (reproduced in verdict).** For every chapter of Job, the main session scored each five-verse window elsewhere in the book by the rare lemmas (in up to 150 verses, WLC) it shares with that chapter, and expressed the top window as a z-score. Job 28: top 6, mean 1.55, SD 1.29, **z = 3.46**, exactly as auditor C found. **31 of the other 41 chapters** have a higher top-window z (auditor C, working on a slightly different chapter set, found 26 of 36). Job 26 reaches z = 4.64 and Job 38 z = 4.30. The verdict stands: the window test does not single chapter 28 out, and its relation to 22, 26 and 38 has to rest on particular lines.

**Independent rebuild 2 — C4, the paragraphing test (corrected).** Auditor C reported that "every one of the 28 speech formulas in Job is preceded by a BHS פ or ס", and on that basis raised "within Job's discourse" to moderate–high. Its script read the markers from the **WLC transcription** of Leningrad, not from the BHS export. The two differ at one point that matters: the WLC has a setumah after 19:29, and **BHS has none** (confirmed by Patrick on screen, 5 October; the BHS export agrees). So **as BHS prints it, one change of speaker in the dialogue — Job → Zophar at 20:1 — is not preceded by a marker.** (The two other unmarked formulas found by the rebuild, 1:9 and 2:4, are dialogue inside the prose prologue, where individual speeches are not marked.) The absence of a marker before 28:1 is therefore consistent with Job's speaking on, but it is not decisive. The main session holds the rating at **moderate**, as the 28:1–28 dig had it. On the WLC transcription alone, moderate–high would be justified. This is the standing rule — check every "as BHS prints it" claim against the BHS export — doing its work.

---

## Summary

### Verdict count

Seventeen claims; twenty rulings where a claim divides (A5 a/b; C2 a/b; C7 a/b, with C7's generalisation ruled separately below).

| Verdict | Count | Rulings |
|---|---|---|
| Confirmed | 0 | — |
| Confirmed with nuance | 14 | A1, A2, A5b, A6, B3, B4, C1, C2a, C2b, C4, C5, C6, C7a, C7b |
| Needs reframing | 6 | A3, A4, A5a, B1, B2, C3 |
| Uncertain | 0 | — |
| Discard | 0 | (the extension of B1 to 28:1–13 is discarded as a sub-claim) |

### Verdicts in brief

| # | Claim | Queue / source | Verdict | Final rating |
|---|---|---|---|---|
| A1 | Wilderness rock-and-water tradition (Deut 8:15; Ps 78:15–16; Ps 114:8; Isa 48:21) behind 28:9–11; Deut 8:9 behind 28:2, 5–6 | #93 | Confirmed with nuance | Tradition **moderate** (Ps 114:8 closest for the flint line); Deut 8:9 **low–moderate** |
| A2 | Isa 40:12–13 at 28:25 | #98 | Confirmed with nuance | **Moderate**; the root cluster (weigh + measure + water) is unique to these two places; Prov 8:27–29 the better parallel for 28:26–27 |
| A3 | Isa 33:6 at 28:28 | #96 | Needs reframing | **Low–moderate**; a syntactic companion, not a source; the treasure is closer in Prov 15:16; 2:4–5 |
| A4 | Amos 5:8 at 24:17 | #45 | Needs reframing | **Low**; the pair is at chance level and the Old Greek lacked the verse; the Amos doxologies stand behind 9:5–10 instead (moderate) |
| A5 | (a) Isa 51:9 at 26:12–13; (b) Isa 27:1 "fleeing serpent" at 26:13 | #55 | (a) Needs reframing; (b) Confirmed with nuance | (a) **moderate** as a shared sea-battle idiom (with Ps 89:10–11; Jer 10:12; 31:35); (b) lexical identity **high**, dependence **moderate** |
| A6 | Deut 24:17 at 24:3 | sweep | Confirmed with nuance | **Moderate–high**, and wider: Job 24:2–12 speaks in the words of Deuteronomy's law of the vulnerable (Deut 24:10–21; 19:14; 27:17), with Exod 22:20–26 |
| B1 | Prov 2:1–6 behind 28:20–28 (and 28:1–13) | #92 | Needs reframing | **Low–moderate**, a conceptual comparison only; the rank 1 is a three-way tie on four common wisdom words and does not survive small changes; the 28:1–13 extension discarded |
| B2 | Prov 8 and 3:13–20 behind 28:12–27; the circle | overview | Needs reframing | **Moderate** on words and use; Job 26:10 / Prov 8:27 (the inscribed circle) **moderate–high** |
| B3 | Ezek 28 and Exod 28, the gem field | #97 | Confirmed with nuance | Field **moderate**; Ezek 28 as source **low**; Lam 4:1–7 a field companion (low–moderate) |
| B4 | The motto at 28:28 | overview | Confirmed with nuance | **High** for the shared formula and the 1:1 / 28:28 frame; **low** for dependence on any single Proverbs verse; "tested before taught" reframed |
| C1 | The miner doing God's acts | #94 | Confirmed with nuance | Pairs (i) 26:10, (ii) 9:5, (iv) Ps 78:15 / Isa 48:21 **high**; (iii) 12:22 **moderate** (exclusive only within Job); design **moderate** |
| C2a | The ear and the eye (4:12; 26:14 → 28:22 → 42:5) | #95 | Confirmed with nuance | Words **high**; the line **moderate** (hearing-then-seeing is a Job idiom: 13:1; 29:11) |
| C2b | Eliphaz's "fear" (4:6; 15:4; 22:4 → 28:28) | 28 dig | Confirmed with nuance | 28:28 → 1:1, 8; 2:3 **high** (Hebrew and Greek); the one-per-speech series **moderate** (chance gives about one) |
| C3 | Internal window test: 28 bound to 22, 26, 38 | 28 dig | Needs reframing | Window test **does not support design**; specific links: 28:26b = 38:25b high; Ophir moderate; ידע + דֶּרֶךְ 23:10 / 28:23 moderate; קָצָה 26:14 / 28:24 low–moderate; the rest low; "meeting point" **low–moderate** |
| C4 | Who speaks 28; the frame | #99 | Confirmed with nuance | Within Job's discourse **moderate** (main-session correction of the auditor's moderate–high; see Spot Checks); "a voice above the dispute" moderate; Option C (Zophar) no support |
| C5 | 24:18–25 and 27:13–23 | overview | Confirmed with nuance | The text attributes both to Job **high**; disorder not demonstrated; Job taking up the friends' lines possible for 27:13–23, weak for 24:18–25 |
| C6 | The breakdown of the third cycle | overview | Confirmed with nuance | As the text stands **high**; as design **moderate–high** (25:4 repeats a half-line, 9:2b) |
| C7a | 21:14–16 → 22:17–18 | sweep | Confirmed with nuance | Verbal link **high**; Eliphaz turns Job's report of the wicked against him, and claims Job's disavowal ("far from me") for himself |
| C7b | 22:22 → 23:12 | sweep | Confirmed with nuance | **Moderate**; shared instruction idiom (Prov 2:1; 7:1) |
| — | "The third round is a set of pointed rejoinders" | — | Needs reframing | **Low** as a pattern; the 21 → 22 junction is the only verbatim rejoinder at any adjacent junction in Job |

### The findings two auditors reached independently

**Zophar's 11:6–9 behind Job 28.** Auditors B and C, working on different claims and blind to each other, both surfaced Zophar's speech as a Job-internal source for the poem. Zophar wished God would show Job "the secrets of wisdom (תַּעֲלֻמוֹת חָכְמָה)" (11:6) and asked, "Can you discover (תִּמְצָא) the depths (חֵקֶר) of God? Can you discover the limits (תַּכְלִית) of the Almighty?" (11:7). תַּעֲלֻמָה ("hidden thing") occurs only at Job 11:6, 28:11 and Ps 44:22; 11:7 is the only verse joining חֵקֶר and תַּכְלִית, and 28:3 joins the verb חקר with תַּכְלִית. The poem's miner reaches "every limit" and brings "the hidden thing" to light, yet wisdom is not found (תִּמָּצֵא, 28:12–13). **Moderate–high** (Job-internal). The sweep had noted 11:6 → 28:11 and 11:7 → 28:3 separately; the audit shows them as one answer to Zophar.

**Ps 114:8 at Job 28:9.** Auditors A and C both found that חַלָּמִישׁ ("flint") + הפך ("overturn") occur only at Job 28:9 and Ps 114:8 ("who turned the rock into a pool of water, the flint into a fountain of water"), and that this is 28:9's only exclusive pair. It belongs to the wilderness rock-and-water cluster (A1) and is closer for the flint line than Deut 8:15. **Moderate**, as part of that tradition.

### What the audit changes, in one paragraph

The third round's text holds up. The breakdown is registered by the book itself in three independent ways — Bildad's last speech borrows half its lines (25:4b = 9:2b; 25:5b = 15:15b), the speech formula changes after 26:1 (Job no longer "answers" but "takes up his discourse"), and 32:1–5 narrates that the friends "ceased answering" — and nothing in the text, the apparatus or the Greek supports redistributing 24:18–25 or 27:13–23 to the friends. Chapter 28 stands within Job's discourse, at moderate confidence. The 28:1–28 dig's strongest claims survive (28:28 → 1:1, 8; 2:3; 28:26 = 38:25; the miner's exclusive pairs; the three strophes), but three of its headlines are cut back: **Proverbs 2 falls from moderate–high to low–moderate**, because its first-place rank was a tie on common words; **the internal window test is withdrawn as evidence of design**, because most Job chapters have a more prominent top neighbour; and the ear-and-eye line, the Eliphaz "fear" series and the miner design each fall to moderate. Outside chapter 28, Job 24's catalogue of oppression proves to speak in the words of Deuteronomy's law of the vulnerable (moderate–high), Amos 5:8 at 24:17 falls to low (the Amos doxologies belong at 9:5–10), and Job 26's sea monster is a shared hymnic idiom with one genuinely unique epithet shared with Isa 27:1.

### Confidence Change Propagation

| Claim | Where it sits | Was | Now | Action |
|---|---|---|---|---|
| Prov 2:1–6 at 28:20–28 (#92) | 28 dig Headline 6; Tool 11; Canonical position | moderate–high | **low–moderate** (conceptual) | Restate as comparison; drop the 28:1–13 extension and "first of 887" |
| Internal window test (C3) | 28 dig Headline 2 | moderate–high | **withdrawn as design**; specific links as rated | Rewrite Headline 2 on the particular lines |
| 26:14 → 28:22–24 | 28 dig Headline 2; Move 4 | moderate–high | **low–moderate** (קָצָה); בִּין low | Downgrade |
| 23:3, 10 → 28:12–14, 23 | 28 dig Context; Move 4 | moderate–high | ידע + דֶּרֶךְ **moderate**; ידע + מצא and עִמָּדִי **low** | Keep 23:10 → 28:23; drop the rest as evidence |
| Ear and eye (#95) | 28 dig Headline 3 | moderate–high | **moderate** | Downgrade; note 13:1; 29:11 |
| Eliphaz "fear" series | 28 dig Headline 1 | moderate–high | **moderate** | Downgrade the series; keep the 1:1 frame high |
| Miner design (#94) | 28 dig Headline 4 | moderate–high (design) | **moderate**; pair (iii) moderate | Downgrade; add Ps 114:8 and Zophar 11:6–7 |
| Speaker of 28 (#99) | 28 dig Headline 7; overview CJ2 | moderate | **moderate** (unchanged) | Correct two markers (person shift at 27:13; wayyiqtol as creation narrative) |
| Deut 8 / wilderness rock (#93) | 28 dig Headline 6 | tradition moderate; Deut 8 low–moderate | unchanged; Ps 114:8 added | Add Ps 114:8 |
| Isa 33:6 (#96) | 28 dig Tool 11 | moderate | **low–moderate** | Downgrade; add Deut 4:6 and Prov 15:16 |
| Isa 40:12–13 (#98) | 28 dig; sweep | moderate | moderate | Note the unique root cluster; Prov 8:27–29 for 28:26–27 |
| Prov 8 / 3 (B2) | 28 dig Headline 6; overview map | high (words) | **moderate**; 26:10 / Prov 8:27 moderate–high | Restate; add the circle |
| Motto at 28:28 (B4) | overview map; 28 dig | high | high (formula and frame) | Reframe "tested before taught" (Ps 34; 111 precede Job) |
| Gem field (#97) | 28 dig Vocabulary | field moderate; source low | unchanged; Lam 4:1–7 added | Add Lam 4 |
| Amos 5:8 at 24:17 (#45) | queue; audit 2 new candidate | moderate–high | **low** | Move the Amos evidence to 9:5–10 |
| Isa 51:9 at 26:12–13 (#55) | queue | moderate–high (words) | **moderate** as idiom; Isa 27:1 lexical high | Restate |
| Deut 24:17 at 24:3 (A6) | sweep | moderate | **moderate–high**, as Deut 24:10–21 block | Raise; widen |
| 27:13–23, 24:18–25 (C5) | overview CJ1 | contested | text attributes both to Job **high**; disorder not shown | Revise CJ1 |
| Breakdown (C6) | overview arc map | stated | high (text); moderate–high (design) | Add the three markers |
| 21:14–16 → 22:17–18 (C7a) | sweep Table B | high (self-quotation) | high (verbal); "Eliphaz turns Job's words" | Restate |
| "Every speech ends with a marker except 27:23" | overview; sweep | stated as Masoretic | **true of the WLC transcription; in BHS 19:29 also lacks one** | Qualify |

### Recommended book-overview revisions

1. **Contested judgement 1 (the third cycle).** Restate: as the text stands, 24:18–25 and 27:13–23 are Job's (high); disorder is not demonstrated by any marker, apparatus note or Greek reading; Job taking up the friends' lines is possible for 27:13–23 (it cites Zophar's 20:29, and both b-lines open "and the heritage of"), weak for 24:18–25. Add the three breakdown markers (Bildad's borrowed lines; the change of formula after 26:1; 32:1–5).
2. **The paragraphing line.** "Every speech ends with a marker except 27:23" is true of Leningrad as the WLC transcribes it. As BHS prints it, 19:29 also has none. Say so.
3. **Contested judgement 2 (chapter 28).** Within Job's discourse, moderate. Remove the person shift and the wayyiqtol as signs of another voice (C4). Keep Andersen's narrator view as `[S]`.
4. **Intertextual map.**
   - 28:28: the shared formula and the 1:1 frame high; no single Proverbs verse as source.
   - Canonical position: replace "tested before taught" with "taught in the Psalter (Ps 34:12, 15; 111:10), tested in Job, set out for daily life in Proverbs".
   - Prov 8 moderate (26:10 / Prov 8:27 moderate–high); Prov 2 low–moderate.
   - Add Deut 24:10–21 (with 19:14; 27:17) at Job 24:2–12, moderate–high.
   - Add the Amos doxologies at 9:5–10, moderate (already audited as #15 in audit 2: "9:8b–9 moderate–high; pattern moderate"); drop Amos 5:8 at 24:17 below moderate.
   - Isa 51:9 at 26:12–13 as idiom, moderate; Isa 27:1 "fleeing serpent" at 26:13, lexical high.
   - The wilderness rock tradition at 28:9–11, moderate (Ps 114:8; Ps 78:15–16; Isa 48:21; Deut 8:15).
5. **Echo Table.** Add Zophar 11:6–7 → 28:3, 11–13 (moderate–high); 23:10 → 28:23 (moderate); 25:4b–6 ← 15:14–16 and 9:2b (high); 21:14–16 → 22:17–18 as "Eliphaz turns Job's words" (high).

### Recommended dig revisions

**The 28:1–28 dig (to v1.1).**

1. **Headline 1.** Keep 28:28 → 1:1, 8; 2:3 high. Lower the Eliphaz "fear" series to moderate (`[S: audit 4]`, C2b).
2. **Headline 2.** Withdraw the internal window test as evidence of design (z 3.46; 31 of 41 chapters higher). Rest the relation to 22, 26 and 38 on: 28:26b = 38:25b (high); Ophir 22:24–25 / 28:16 (moderate); ידע + דֶּרֶךְ 23:10 / 28:23 (moderate). Lower 26:14 → 28:23–24 to low–moderate.
3. **Headline 3.** Lower the ear-and-eye line to moderate; add 13:1 and 29:11.
4. **Headline 4.** Pairs (i), (ii), (iv) high; (iii) moderate; design moderate. Add Ps 114:8 (הפך + חַלָּמִישׁ) and Zophar 11:6–7, and the Greek ἀνακαλύπτω + βάθ- (Dan 2:22; Job 12:22; 28:11, Swete).
5. **Headline 6.** Prov 2 to low–moderate, as comparison (tie; fragile rank; image words absent); remove "first of 887, no null". Prov 8 moderate; 26:10 / Prov 8:27 moderate–high; Prov 8:27–29 for 28:26–27. Isa 33:6 low–moderate; add Deut 4:6 (wisdom + understanding + הִיא, identity form) and Prov 15:16. Deut 8: add Ps 114:8 to the tradition.
6. **Headline 7.** Keep moderate. Correct: the change of person is at 27:13, not 28:1; the wayyiqtol of 28:28 continues the creation narrative of 28:25–27 (compare 38:11); BHS has no apparatus note at 28:10. Add the formula change after 26:1 and 14:7 (כִּי יֵשׁ לְ- opening a stanza inside Job's speech, as 28:1).
7. **Canonical position.** Replace "tested before taught" (B4d).
8. **Context.** "25:4 repeats Job's 9:2" → "25:4b repeats 9:2b"; add 25:5b = 15:15b.
9. **Tool 11 table and Move 4** to match the above. Add Lam 4:1–7 to the gem field.

**Claim audit 2.** Remove Job 28:23 from the trigram list (already recorded in the queue, 8 October).

**The sweep.** No correction of fact; its 9:2 / 25:4 "exact clause" statement is accurate. Its paragraphing sentence carries the same WLC/BHS qualification as the overview.

### New links surfaced by the audit

| Link | Found by | Rating | Queue |
|---|---|---|---|
| Zophar 11:6–9 → 28:3, 11–14 (internal) | B, C | moderate–high | not queued (verified lexical chain) |
| Ps 114:8 at 28:9 (הפך + חַלָּמִישׁ) | A, C | moderate (with A1) | not queued (verified pair; part of #93's tradition) |
| Bildad 25:4b–6 built from 15:14–16 and 9:2b (25:5b = 15:15b) | C | high | not queued (verified chain) |
| The formula change after 26:1 (no more "answered"; 32:3, 5 מַעֲנֶה) | C | high (structural) | not queued |
| ידע + דֶּרֶךְ 23:10 → 28:23 | C | moderate | not queued (verified pair) |
| 28:28 וַיֹּאמֶר and 38:11 וָאֹמַר — divine speech at creation | C | moderate | not queued |
| 14:7 → 28:1 (כִּי יֵשׁ לְ- opening a stanza) | C | low–moderate | not queued |
| The Amos doxologies at 9:5–10 (Amos 4:13; 5:8) | A | moderate | **#100** |
| Jer 10:12 = 51:15 at 26:12 (and 26:7), with Jer 10:12–13 at 28:24–27 | A, B | moderate / low–moderate | **#101** |
| Jer 31:35–36 at 26:10–12 (רֹגַע הַיָּם) | A | low–moderate | **#102** |
| Prov 8:27–29 at 26:10 and 28:26–27 (the circle; the "when He set … a decree" idiom) | A, B | moderate–high / moderate | **#103** |
| Prov 15:16 (fear of the LORD + treasure) as rival to Isa 33:6 at 28:28 | A | moderate | **#104** |
| Prov 23:10 at 24:2–3 (landmark + orphan) | A | moderate | **#105** |
| Isa 59:8–10 at 24:13–16 | A | low–moderate | **#106** |
| Lam 4:1–7 at 28:15–19 (סלא / סלה "weigh against gold") | B | low–moderate (field companion) | **#107** |
| Deut 4:5–10 at 28:28 (identity syntax; "learn to fear Me") | B | low–moderate | **#108** |
| Prov 2:1; 7:1 behind 22:22 / 23:12 (the instruction formula) | C | moderate | **#109** |
| Job 3:21 ↔ Prov 2:4 (מַטְמוֹנִים) | B | low–moderate | **#110** |
| Isa 13:12 at 28:13, 16–17 | B | low | not queued |
| Sir 24:5 (Greek) as reception of 22:14 | B | not rated | Logos (reception) |

---

## Critical Assessment

1. **History of interpretation was not checked.** Every Hays table records it as *not checked*. Andersen's narrator view of 28 (Logos round 2) is the only library evidence already in hand for these claims. A Logos round is the next check for the links now rated moderate–high or above: Deut 24 at Job 24:2–12; Prov 8:27 at 26:10; Zophar 11:6–7 behind 28; Isa 27:1 at 26:13; and the speaker of 28 and the third-cycle question in the commentaries Patrick owns.
2. **The auditors shared one set of search routines.** A fault in those routines would be common to all three, and the spot checks used the same routines. The two independent rebuilds were written fresh in the main session, but on the same lemma index. They caught one error, and it was an edition error, not a fault in the routines.
3. **An edition slip, caught.** Auditor C's paragraphing script read the WLC transcription and its report said "BHS". The difference at 19:29 / 20:1 is small but bears directly on an attribution argument. This is the second time in the Job audits that a WLC/BHS difference in the markers has mattered; any future paragraphing argument should be run on the BHS export by default.
4. **The weak null.** For gems (B3) and rock-and-water (A1) the Job-passage null cannot separate "source" from "shared field", because no other Job passage uses those fields. The auditors said so; the ratings reflect it.
5. **Rank stability is now a test.** B1 shows that a first-place rank with a clean null can still be an artefact of a tie and a narrow setting. Future window-rank claims should report the rank under at least two window lengths and frequency ceilings before they are called evidence.
6. **The proposing run was this session's own.** Four of the claims came from the 28:1–28 dig written earlier the same day. The auditors were blind to it; they cut three of its headlines back. The audit did what it is for.

---

## Queue and Triggers

**Audited and closed:** #45, #55, #92–99 (10 items), plus seven non-queue claims from the overview, the sweep and the 28 dig. **Added:** #100–110 (11 items) from this audit. **Job queue after audit 4: 61** — the 50 not audited (#1–6, 8–12, 17–22, 25, 27–29, 31–34, 40–44, 46–53, 80–91) plus the 11 new.

**Triggers.**

1. Count limb still armed by the backlog (61), with digs since last audit reset to 0. The next audit is best batched with the Sermon 6–7 material (29–37) or the Finalise pass, whichever comes first.
2. **Satisfied for the Sermon 5 unit dig and backbone**, once the 28:1–28 dig is patched to v1.1 with these verdicts (recommended above): every allusion, design and structure claim that would carry a Sermon 5 headline has now been audited, and the unit dig takes the verdicts as `[S: audit 4]`. #21 (Ezek 14:22–23 ↔ 42:11) remains armed before the 42:7–17 dig.
3. Unchanged. Finalise is not yet planned.

**The plan's decision point.** The third-cycle audit was to precede the choice between nine sermons and ten (22–27 and 28 apart). The text allows either: there is no marker before 28 and a ס after it, and the breakdown of 22–27 and the poem's answer can be preached together or apart. Nothing in this audit forces the choice.

---

## Colophon

- **Report:** `Job/dig-deeper-job-claim-audit-4.{md,odt,html}`.
- **Auditors:** three blind general-purpose subagents, run one after another on 8 October 2026; auditor C was re-run after a session break interrupted its first run. Their working parts are reproduced unaltered above, with headings demoted one level and BHS's Fraktur sigla rendered in roman (the only changes to their text). The main session's correction to C4 is given in Spot Checks and the verdict table; the auditor's own text is left as written.
- **Briefs:** a common brief plus three claims files, written before the auditors ran and held in the session workspace, which is not retained.
- **Corpus:** WLC with lemma and morphology index; BHS with apparatus (Job); Swete; Rahlfs (as listed); SBLGNT; NASB95, ESV and NIV84 exports.
- **Spot checks:** 26, all reproduced; two independent rebuilds, one reproduced and one corrected.
- **Verdicts:** 0 Confirmed; 14 Confirmed with nuance; 6 Needs reframing; 0 Uncertain; 0 Discard (one sub-claim discarded).
- **Warrant:** every count names its edition; every "only" was checked by lemma and, for phrases, by exact consonants; every absence was preceded by a passing positive control. History of interpretation was not checked.
