# Dig Deeper: Job 16:1–17:16

**Primary texts:**
- **Hebrew:** BHS (Logos export, `_texts/logos-exports/01-Old-Testament/03-Ketuvim/02-Job-BHS.txt`), read first, with the BHS apparatus for chapters 16–17 (`02-Job-BHS-App.txt`). The WLC lemma and morphology index (`_texts/hebrew-wlc/`) is used for every count and chain.
- **Greek:** Swete for the wording, which numbers chapter 16 one verse ahead of the Hebrew from 16:5 onward. The Rahlfs export (`02-Job-LXX.txt`), which keeps the Hebrew numbering, is used for the asterisks and for verse alignment. Greek is cited by the Hebrew verse number.
- **New Testament:** SBLGNT for every Greek check.

**Study text:** NASB95 (Logos export).
**Pulpit text:** ESV, declared for the series on 28 September 2026 and confirmed for this run. Every ESV quotation below was checked against the Logos export.
**Date:** 5 October 2026 · **Version:** 1.1 (patched 7 October 2026 from claim audit 3; see *What Changed in v1.1*); Logos round 6 notes added 7 October 2026 (see Open Questions)

**Book-overview context:** `Job/book-overview-job.md` (v0.1.1), front-loaded at Phase 0.5. Neighbouring reports consulted at the checking stage:
- the sweep's Unit 8, 15:1–17:16 (`Job/dig-deeper-job-sweep.md`);
- the Unit 1 report on 1:1–3:1, the opening unit and so a permanent neighbour;
- the Job 3 report;
- the consolidation report on 4:1–14:22, with its solo digs on 9–10 and 13–14;
- claim audit 2;
- the Sermon 3 backbone;
- the Logos round 2 assessment (5 October), whose answers on 16:19 (Ash; the study Bibles; Keil–Delitzsch cited for wording) are the only commentary material in view.
- **v1.1:** claim audit 3 (`Job/dig-deeper-job-claim-audit-3.md`), which tested this dig's source claims (queue #7, #57, #58, #60–62) with three blind auditors and a window-rank null. Its verdicts are applied in place and tagged `[S: audit 3]`.

**Series context:** the first of the two HIGH solo digs inside Sermon 4 (15:1–21:34). The other is 19:1–29. The unit report for Sermon 4 will be a consolidation dig on 15:1–21:34.

**Extent.**
- **The speech.** Job's reply to Eliphaz's second speech (15:1–35) runs from 16:1 to 17:16. Leningrad, as BHS prints it, marks no paragraph inside the speech and closes it with a setumah after 17:16. A setumah also closes Eliphaz's speech (15:35).
- **Chapter 15.** This dig works 16:1–17:16, the unit the series plan names. It reads chapter 15 as the speech Job is answering, because the speech answers it phrase by phrase (Headline 2).
- **Chapter 18.** It also reads chapter 18 as the speech that answers this one.

**Warrant tags:**
- `[T]` derivable from the text itself;
- `[I]` a reasonable inference from the text;
- `[S]` supplied by a secondary source and held provisionally;
- `[S: audit]` a verdict of this project's claim audits, accepted;
- `[S: audit 3]` a verdict of claim audit 3, applied in v1.1.

> **Counts and chains.**
> - **Method.** Every count is a count **in the Hebrew**, made against the WLC lemma index (by lemma, never by surface form) unless it says "phrase search". Phrase searches normalise maqqef, paseq and sof pasuq, strip the pointing, and run a second skeletal pass.
> - **Ketiv.** Chapters 16–17 carry one ketiv, 16:16 חמרמרה ("red"), found mechanically, and no chain depends on it.
> - **Positive controls.** Every "only" was run against a positive control: the matcher's control is חֶסֶד ("kindness") in Job, which returns 6:14, 10:12 and 37:13.
> - **Lemma splits.** Three splits in the index were met and allowed for:
>   - הלך ("go") is filed as 1980 or 3212 by form, so "go and not return" needs both;
>   - מַטָּרָה ("target") shares its number with מַטָּרָה ("guard, prison"), so the target sense was isolated by reading the hits;
>   - שׁמם ("be desolate") is split between the verb (8074) and the adjective (8076).
> - **The log** is `~/j1617/chk.py` and the follow-up runs.

---

## The Passage

*Text: BHS as exported from Logos, with the NASB95 beneath each verse. ᵃ marks a BHS apparatus note (see Textual Variants). Leningrad, as BHS prints it, has no paragraph marker inside 16:1–17:16; a setumah (ס) follows 15:35 and 17:16.*

**16:1** וַיַּ֥עַן אִיֹּ֗וב וַיֹּאמַֽר׃  
Then Job answered,

**16:2** שָׁמַ֣עְתִּי כְאֵ֣לֶּה רַבֹּ֑ות מְנַחֲמֵ֖י עָמָ֣ל כֻּלְּכֶֽם׃  
“I have heard many such things; Sorry comforters are you all.

**16:3** הֲקֵ֥ץ לְדִבְרֵי־ר֑וּחַ ᵃאֹ֥ו מַהᵃ־יַּ֝מְרִֽיצְךָ֗ כִּ֣י תַעֲנֶֽה׃  
“Is there no limit to windy words? Or what plagues you that you answer?

**16:4** גַּ֤ם׀ אָנֹכִי֮ כָּכֶ֪ם אֲדַ֫בֵּ֥רָה ל֤וּ־יֵ֪שׁ נַפְשְׁכֶ֡ם תַּ֤חַת נַפְשִׁ֗י אַחְבִּ֣ירָה עֲלֵיכֶ֣ם בְּמִלִּ֑ים וְאָנִ֥יעָה עֲ֝לֵיכֶ֗ם בְּמֹ֣ו רֹאשִֽׁי׃  
“I too could speak like you, If I were in your place. I could compose words against you And shake my head at you.

**16:5** אֲאַמִּצְכֶ֥ם בְּמֹו־פִ֑י וְנִ֖יד שְׂפָתַ֣י יַחְשֹֽׂךְ׃  
“I could strengthen you with my mouth, And the solace of my lips could lessen your pain.

**16:6** אִֽם־אֲ֭דַבְּרָה לֹא־יֵחָשֵׂ֣ךְ כְּאֵבִ֑י וְ֝אַחְדְּלָ֗ה מַה־מִנִּ֥יᵃ יַהֲלֹֽךְ׃  
“If I speak, my pain is not lessened, And if I hold back, what has left me?

**16:7** אַךְ־עַתָּ֥ה הֶלְאָ֑נִי הֲ֝שִׁמֹּ֗ותָ כָּל־עֲדָתִֽי׃  
“But now He has exhausted me; You have laid waste all my company.

**16:8** וַֽ֭תִּקְמְטֵנִי לְעֵ֣ד הָיָ֑ה וַיָּ֥קָם בִּ֥י כַ֝חֲשִׁ֗י בְּפָנַ֥י יַעֲנֶֽה׃  
“You have shriveled me up, It has become a witness; And my leanness rises up against me, It testifies to my face.

**16:9** אַפֹּ֤ו טָרַ֨ף׀ וַֽיִּשְׂטְמֵ֗נִי חָרַ֣ק עָלַ֣י בְּשִׁנָּ֑יו צָרִ֓י׀ יִלְטֹ֖ושׁ עֵינָ֣יו לִֽי׃  
“His anger has torn me and hunted me down, He has gnashed at me with His teeth; My adversary glares at me.

**16:10** פָּעֲר֬וּ עָלַ֨י׀ בְּפִיהֶ֗ם בְּ֭חֶרְפָּה הִכּ֣וּ לְחָיָ֑י יַ֝֗חַד עָלַ֥י יִתְמַלָּאֽוּן׃  
“They have gaped at me with their mouth, They have slapped me on the cheek with contempt; They have massed themselves against me.

**16:11** יַסְגִּירֵ֣נִי אֵ֭ל אֶ֣ל עֲוִ֑ילᵃ וְעַל־יְדֵ֖י רְשָׁעִ֣ים יִרְטֵֽנִי׃  
“God hands me over to ruffians And tosses me into the hands of the wicked.

**16:12** שָׁ֘לֵ֤ו הָיִ֨יתִי׀ וַֽיְפַרְפְּרֵ֗נִי וְאָחַ֣ז בְּ֭עָרְפִּי וַֽיְפַצְפְּצֵ֑נִי וַיְקִימֵ֥נִי לֹ֝֗ו לְמַטָּרָֽה׃  
“I was at ease, but He shattered me, And He has grasped me by the neck and shaken me to pieces; He has also set me up as His target.

**16:13** יָ֘סֹ֤בּוּ עָלַ֨י׀ רַבָּ֗יו יְפַלַּ֣ח כִּ֭לְיֹותַי וְלֹ֣א יַחְמֹ֑ול יִשְׁפֹּ֥ךְ לָ֝אָ֗רֶץ מְרֵרָֽתִי׃  
“His arrows surround me. Without mercy He splits my kidneys open; He pours out my gall on the ground.

**16:14** יִפְרְצֵ֣נִי פֶ֭רֶץ עַל־פְּנֵי־פָ֑רֶץ יָרֻ֖ץ עָלַ֣י כְּגִבֹּֽור׃  
“He breaks through me with breach after breach; He runs at me like a warrior.

**16:15** שַׂ֣ק תָּ֭פַרְתִּי עֲלֵ֣י גִלְדִּ֑י וְעֹלַ֖לְתִּי בֶעָפָ֣ר קַרְנִֽי׃  
“I have sewed sackcloth over my skin And thrust my horn in the dust.

**16:16** פָּנַ֣י חֳ֭מַרְמְרֻה מִנִּי־בֶ֑כִי וְעַ֖ל עַפְעַפַּ֣י צַלְמָֽוֶת׃  
“My face is flushed from weeping, And deep darkness is on my eyelids,

**16:17** עַ֭ל לֹא־חָמָ֣ס בְּכַפָּ֑י וּֽתְפִלָּתִ֥י זַכָּֽה׃  
Although there is no violence in my hands, And my prayer is pure.

**16:18** אֶ֭רֶץ אַל־תְּכַסִּ֣י דָמִ֑י וְֽאַל־יְהִ֥י מָ֝קֹ֗ום לְזַעֲקָתִֽיᵃ׃  
“O earth, do not cover my blood, And let there be no resting place for my cry.

**16:19** גַּם־עַ֭תָּה הִנֵּה־בַשָּׁמַ֣יִם עֵדִ֑י וְ֝שָׂהֲדִ֗י בַּמְּרֹומִֽים׃  
“Even now, behold, my witness is in heaven, And my advocate is on high.

**16:20** ᵃמְלִיצַ֥י רֵעָ֑יᵃ אֶל־אֱ֝לֹ֗והַᵇ דָּלְפָ֥ה עֵינִֽי׃  
“My friends are my scoffers; My eye weeps to God.

**16:21** וְיֹוכַ֣ח לְגֶ֣בֶר עִם־אֱלֹ֑והַּ וּֽבֶןᵃ־אָדָ֥ם לְרֵעֵֽהוּ׃  
“O that a man might plead with God As a man with his neighbor!

**16:22** כִּֽי־שְׁנֹ֣ות מִסְפָּ֣ר יֶאֱתָ֑יוּ וְאֹ֖רַח לֹא־אָשׁ֣וּב אֶהֱלֹֽךְ׃  
“For when a few years are past, I shall go the way of no return.

**17:1** רוּחִ֣י חֻ֭בָּלָה יָמַ֥י נִזְעָ֗כוּᵃ קְבָרִ֥ים לִֽי׃  
“My spirit is broken, my days are extinguished, The grave is ready for me.

**17:2** אִם־לֹ֣א הֲ֭תֻלִים עִמָּדִ֑י וּ֝בְהַמְּרֹותָ֗ם תָּלַ֥ן עֵינִֽי׃  
“Surely mockers are with me, And my eye gazes on their provocation.

**17:3** שִֽׂימָה־נָּ֭א עָרְבֵ֣נִיᵃ עִמָּ֑ךְ ᵇמִֽי ה֝֗וּאᵇ לְיָדִ֥י יִתָּקֵֽעַ׃  
“Lay down, now, a pledge for me with Yourself; Who is there that will be my guarantor?

**17:4** כִּֽי־לִ֭בָּם צָפַ֣נְתָּ מִּשָּׂ֑כֶל עַל־כֵּ֝֗ן לֹ֣א תְרֹמֵֽםᵃ׃  
“For You have kept their heart from understanding, Therefore You will not exalt them.

**17:5** לְ֭חֵלֶק יַגִּ֣יד רֵעִ֑ים וְעֵינֵ֖י בָנָ֣יו תִּכְלֶֽנָה׃  
“He who informs against friends for a share of the spoil, The eyes of his children also will languish.

**17:6** וְֽ֭הִצִּגַנִי לִמְשֹׁ֣לᵃ עַמִּ֑ים וְתֹ֖פֶתᵇ לְפָנִ֣ים אֶֽהְיֶֽה׃  
“But He has made me a byword of the people, And I am one at whom men spit.

**17:7** וַתֵּ֣כַהּ מִכַּ֣עַשׂ עֵינִ֑י וִֽיצֻרַ֖י כַּצֵּ֣ל כֻּלָּֽםᵃ׃  
“My eye has also grown dim because of grief, And all my members are as a shadow.

**17:8** יָשֹׁ֣מּוּ יְשָׁרִ֣ים עַל־זֹ֑את וְ֝נָקִ֗י עַל־חָנֵ֥ף יִתְעֹרָֽר׃  
“The upright will be appalled at this, And the innocent will stir up himself against the godless.

**17:9** וְיֹאחֵ֣ז צַדִּ֣יק דַּרְכֹּ֑ו וּֽטֳהָר־יָ֝דַ֗יִם יֹסִ֥יף אֹֽמֶץ׃  
“Nevertheless the righteous will hold to his way, And he who has clean hands will grow stronger and stronger.

**17:10** וְֽאוּלָ֗ם כֻּלָּ֣םᵃ תָּ֭שֻׁבוּ וּבֹ֣אוּ נָ֑א וְלֹֽא־אֶמְצָ֖א בָכֶ֣ם חָכָֽם׃  
“But come again all of you now, For I do not find a wise man among you.

**17:11** יָמַ֣י עָ֭בְרוּ זִמֹּתַ֣יᵃ נִתְּק֑וּ מֹ֖ורָשֵׁ֣י לְבָבִֽי׃  
“My days are past, my plans are torn apart, Even the wishes of my heart.

**17:12** לַ֭יְלָה לְיֹ֣ום יָשִׂ֑ימוּ אֹ֝֗ור קָרֹ֥וב מִפְּנֵי־חֹֽשֶׁךְ׃  
“They make night into day, saying, ‘The light is near,’ in the presence of darkness.

**17:13** אִם־אֲ֭קַוֶּה שְׁאֹ֣ול בֵּיתִ֑י בַּ֝חֹ֗שֶׁךְ רִפַּ֥דְתִּי יְצוּעָֽי׃  
“If I look for Sheol as my home, I make my bed in the darkness;

**17:14** לַשַּׁ֣חַת קָ֭רָאתִי אָ֣בִי אָ֑תָּה אִמִּ֥י וַ֝אֲחֹתִ֗י לָֽרִמָּֽה׃  
If I call to the pit, ‘You are my father’; To the worm, ‘my mother and my sister’;

**17:15** וְ֭אַיֵּה אֵפֹ֣ו תִקְוָתִ֑י וְ֝תִקְוָתִ֗יᵃ מִ֣י יְשׁוּרֶֽנָּה׃  
Where now is my hope? And who regards my hope?

**17:16** בַּדֵּ֣יᵃ שְׁאֹ֣ל תֵּרַ֑דְנָה אִם־יַ֖חַד עַל־עָפָ֣ר נָֽחַת׃  
“Will it go down with me to Sheol? Shall we together go down into the dust?”

---
## Headline Findings

The exegetically strongest claims, each surfaced by several tools:

1. **Two witnesses: Job's body testifies against him on earth, and his witness in heaven testifies for him. The witness does the work of the umpire Job said did not exist, and Job asks God to stand surety for him with God.** `[T]` for the words; `[I]` for the design
   - **עֵד ("witness") occurs in Job only three times, and the three tell a story** (WLC, lemma 5707; positive control passed):
     - "You renew Your witnesses (עֵדֶיךָ) against me" (10:17);
     - "You have shriveled me up, it has become a witness (לְעֵד)" (16:8);
     - "Even now, behold, my witness (עֵדִי) is in heaven, and my advocate (שָׂהֲדִי) is on high" (16:19).
     - God's witnesses against Job, then Job's own wasted body as a witness against him, then a witness in heaven who is "mine".
   - **The law of the malicious witness.** At 16:8 the witness "rises up (וַיָּקָם) against me … it testifies (יַעֲנֶה) to my face".
     - עֵד ("witness") with קום ("rise up") and ענה ("answer, testify") occurs in one verse **only** at Deut 19:16 and Job 16:8 (lemma). Deut 19:16 reads: "If a malicious witness (עֵד־חָמָס, literally 'a witness of violence') rises up against a man to accuse him of wrongdoing".
     - Nine verses later Job swears that there is "no violence (חָמָס) in my hands" (16:17).
     - The law requires two or three witnesses (Deut 19:15) and punishes the false one (19:18–19).
     - Job's body is cast as the hostile witness the law distrusts. Psalm 35, also a psalm of gnashing teeth (35:16), has "malicious witnesses (עֵדֵי חָמָס) rise up" (35:11).
     - `[T]` for the words; `[I]` for the design. *v1.0: moderate–high.* **v1.1: moderate.** The triad עֵד + קום + ענה is exclusive, but "a witness rises" is legal stock shared with Deut 19:15–18, Ps 27:12 and Ps 35:11, and Ps 35 is as close a window. Rahlfs asterisks 16:8b, so the Old Greek lacked the clause `[S: audit 3]`.
   - **The umpire's verb.** At 9:33 there was "no umpire" (מוֹכִיחַ, "one who argues, decides"). Eliphaz then mocked him: "Should he argue (הוֹכֵחַ) with useless talk?" (15:3). Now Job hopes that the witness "will argue (וְיוֹכַח) for a man with God, as a son of man for his neighbor" (16:21, literally). All three verses use יכח ("argue, decide a case") (lemma).
   - **The surety.** "Lay down, now, a pledge for me with Yourself (עָרְבֵנִי עִמָּךְ); who is there that will be my guarantor?" (17:3).
     - Job asks God to stand surety for him, and to do it with God.
     - This is the clearest form in the speech of the appeal to God against God. It is also the text that best explains 16:19–21: the one who argues Job's case "with God" (16:21) is asked for here in God's own presence ("with Yourself").
   - **Earth and heaven.** Job addresses the earth ("O earth, do not cover my blood", 16:18, a feminine imperative to אֶרֶץ, "earth") and in the next line names heaven ("my witness is in heaven", 16:19).
     - These are the two witnesses Moses called "against you" (Deut 4:26; 30:19; 31:28: עוד, "call to witness", with הַשָּׁמַיִם, "the heavens", and הָאָרֶץ, "the earth"; only these three verses, lemma).
     - Job calls them for himself. `[I]` *Moderate.*
   - *Surfaced by:* Vocabulary, Repetition, Move 4, Original Languages (the address test), Christological Reading. *High on the words; moderate–high on the design.*

2. **Job answers Eliphaz's second speech in its own words, and Bildad's reply (chapter 18) answers Job's in his.** **New** except where marked. `[T]` for each verbal link; `[I]` for the pattern
   - **Comfort.** Eliphaz: "Are the consolations of God (תַּנְחֻמוֹת אֵל) too small for you?" (15:11). Job: "Sorry comforters (מְנַחֲמֵי עָמָל, 'comforters of trouble') are you all" (16:2).
     - The noun "trouble" is Eliphaz's last word but two: the wicked "conceive trouble (עָמָל)" (15:35) (sweep).
     - The verb is the friends' own purpose in coming: "to sympathize with him and comfort him (וּלְנַחֲמוֹ)" (2:11).
   - **Wind.** Eliphaz opened: "Should a wise man answer with windy knowledge (דַעַת־רוּחַ)?" (15:2). Job: "Is there no limit to windy words (לְדִבְרֵי־רוּחַ)?" (16:3).
   - **Purity, heaven and the holy ones.** Eliphaz: "What is man, that he should be pure (יִזְכֶּה)?… He puts no trust in His holy ones (בִקְדֹשָׁו), and the heavens (וְשָׁמַיִם) are not pure (זַכּוּ) in His sight" (15:14–15). Job: "my prayer is pure (זַכָּה)" (16:17), and "my witness is in heaven (בַשָּׁמַיִם)" (16:19).
     - Eliphaz has twice denied Job any help from the heavenly ones: "to which of the holy ones (קְדֹשִׁים) will you turn?" (5:1), and 15:15. קָדוֹשׁ ("holy one") occurs in Job only at 5:1, 6:10 and 15:15 (lemma).
     - Job answers with a witness in heaven. `[T]` for the words; `[I]` for the answer.
   - **The warrior reversed.** Eliphaz: the wicked man "conducts himself arrogantly (יִתְגַּבָּר, 'plays the warrior') against the Almighty; he rushes (יָרוּץ) at Him" (15:25–26). Job: "He runs (יָרֻץ) at me like a warrior (כְּגִבּוֹר)" (16:14).
     - רוץ ("run") occurs in Job only at 9:25, 15:26 and 16:14 (lemma).
     - In Eliphaz the wicked charges God; in Job God charges the innocent.
   - **The numbered years.** "Numbered are the years (וּמִסְפַּר שָׁנִים) stored up for the ruthless" (15:20). Job: "when a few years (שְׁנוֹת מִסְפָּר, 'years of number') are past" (16:22).
   - **Bildad's reply (chapter 18) takes up Job's words.**
     - **"In your anger."** Job: "His anger (אַפּוֹ) has torn (טָרַף) me" (16:9). Bildad: "O you who tear (טֹרֵף) yourself in your anger (בְּאַפּוֹ)" (18:4). טרף ("tear") with אַף ("anger") occurs in one verse only at Amos 1:11, Job 16:9 and 18:4 (lemma).
     - **"Torn away."** Job: "my plans are torn apart (נִתְּקוּ)" (17:11). Bildad: "He is torn (יִנָּתֵק) from the security of his tent" (18:14). These are the only two verses of נתק ("tear away") in Job (lemma).
     - **The limbs.** Job: "the bars (בַּדֵּי) of Sheol" (17:16). Bildad: "The firstborn of death devours his limbs (בַּדָּיו)" (18:13).
     - **"Appalled."** Job: "You have laid waste (הֲשִׁמּוֹתָ) all my company" (16:7); "The upright will be appalled (יָשֹׁמּוּ)" (17:8). Bildad: "Those in the west are appalled (נָשַׁמּוּ)" (18:20). שׁמם ("be appalled, desolate") occurs in Job only at 16:7, 17:8, 18:20 and 21:5 (lemma).
     - **Light and darkness.** Job: "'The light (אוֹר) is near,' in the presence of darkness (חֹשֶׁךְ)" (17:12). Bildad: "the light of the wicked goes out" (18:5–6), and "He is driven from light (אוֹר) into darkness (חֹשֶׁךְ)" (18:18).
     - **Extinguished.** Job: "my days are extinguished (נִזְעָכוּ)" (17:1). Several manuscripts read נִדְעָכוּ (BHS), Bildad's verb: "the light of the wicked goes out (יִדְעָךְ)" (18:5–6). *Moderate:* the link rests on the variant.
   - *Surfaced by:* Move 4, Vocabulary, Repetition. *High on each exclusive link.* **v1.1:** the pattern is a **pointed reply, moderate — not lexical design**. A speech-pair baseline ranks 16–17 → 18 99th of 120 pairs (19 dig); queue #59 is closed with claim audit 3 `[S: audit 3]`. This continues round one's habit of quotation (the 4:1–14:22 report, Headline 3) into the second cycle.

3. **Job speaks in the words of Lamentations 2–3 — mocked, shot, struck on the cheek — and innocent. The Servant is a canonical echo, not a demonstrated design (v1.1).** `[T]` for the words; `[I]` for the design; direction of dependence open
   - **v1.1 (claim audit 3): the main source is Lamentations 2:10–17.** All three blind auditors reached it independently.
     - **Window rank.** The window over Lam 2:10–17 ranks 1st of 887 against 16:4–16 (8–9 shared rare lemmas; the next 4–6). It beats every one of 72 arbitrary Job passages of the same length.
     - **Exclusive items.** שׁפך + לָאָרֶץ with a bodily organ ("poured out on the ground": Lam 2:11 כְּבֵדִי, "my liver"; Job 16:13 מְרֵרָתִי, "my gall"); עָפָר + שַׂק ("dust" + "sackcloth": Lam 2:10; Job 16:15); the reduplicated חמר ("be in ferment": Lam 1:20; 2:11; Job 16:16).
     - **The mockers.** Lam 2:15–16 supplies the shaken head, the open mouths and the gnashing teeth (16:4, 9–10).
     - Lam 3:12–13 and 3:30 complete it. *High (words); direction open* `[S: audit 3]`.
     - **The Servant pattern is low.** Isa 53:9's phrase is low–moderate: its fuller form, "no violence in my hands", is shared with 1 Chr 12:18. The cheek's exclusive partner is Lam 3:30, not Isa 50:6 `[S: audit 3]`.
   - **Lamentations 3** (overview row, moderate; **strengthened**):
     - **Target and kidneys.** "He has… set me up as His target (לְמַטָּרָה). His arrows surround me. Without mercy He splits my kidneys (כִּלְיוֹתַי) open" (16:12–13). Lam 3:12–13: "He bent His bow and set me as a target (כַּמַּטָּרָא) for the arrow. He made the arrows of His quiver to enter into my inward parts (בְּכִלְיוֹתָי)." מַטָּרָה ("target") and כִּלְיָה ("kidney") within one verse of each other occur **only** at Job 16:12–13 and Lam 3:12–13 (lemma; the target sense isolated from the homograph "guard, prison").
     - **Cheek and reproach.** "They have slapped me on the cheek (לְחָיָי) with contempt (בְּחֶרְפָּה)" (16:10). Lam 3:30: "Let him give his cheek (לֶחִי) to the smiter, let him be filled with reproach (בְּחֶרְפָּה)." לְחִי ("cheek") with חֶרְפָּה ("reproach") occurs **only** in these two verses (lemma).
     - **Made desolate.** "You have laid waste (הֲשִׁמּוֹתָ)" (16:7); "He has made me desolate (שֹׁמֵם)" (Lam 3:11), the verse before the target. The root is the same; the index splits verb and adjective.
     - **Gnashing teeth.** "He has gnashed at me with His teeth (חָרַק … בְּשִׁנָּיו)" (16:9). Lam 2:16: "They hiss and gnash their teeth (וַיַּחַרְקוּ־שֵׁן)." The phrase also occurs at Ps 35:16; 37:12; 112:10.
     - **Lam 3:30 counsels submission** to the smiter. Job uses its words as protest. `[I]`
   - **Isaiah's Servant:**
     - **"No violence."** "Although there is no violence in my hands" — עַל לֹא־חָמָס בְּכַפָּי (16:17). Isa 53:9: "because He had done no violence" (עַל לֹא־חָמָס עָשָׂה). The phrase עַל לֹא־חָמָס occurs **only** in these two verses (phrase search, skeletal pass included; sweep, confirmed).
     - **The cheek.** "They have slapped (הִכּוּ) me on the cheek" (16:10). Isa 50:6: "I gave My back to those who strike (לְמַכִּים) Me, and My cheeks (וּלְחָיַי) to those who pluck out the beard … humiliation and spitting (וָרֹק)."
     - **The spitting.** "I am one at whom men spit (וְתֹפֶת)" (17:6) — a different word from Isaiah's, which returns at Job 30:10.
     - **Handed over.** "God hands me over (יַסְגִּירֵנִי) to ruffians" (16:11). Swete has παρέδωκεν ("handed over"), the passion verb.
     - claim audit 2 confirmed Isa 50:8–9 at 13:19, 28 (moderate–high) `[S: audit]`. This chapter adds Isa 50:6 and 53:9 to the same servant sequence.
   - **The ruler struck.** At Mic 4:14 [Eng 5:1] the judge of Israel is struck on the cheek with a rod (לְחִי with נכה, "strike"). *Moderate.*
   - *Surfaced by:* Tool 11 (Moves 1–3), Vocabulary, Christological Reading. *High on the two exclusive Lamentations pairs and the Isaiah phrase; moderate–high on Lamentations 3 as a live source; moderate on the servant pattern.* **v1.1:** high on Lam 2:10–17 with Lam 3:12–13, 30; Isa 53:9's phrase low–moderate; the servant pattern low `[S: audit 3]`.

4. **"Be surety for me": Job prays what Hezekiah prayed at the gate of Sheol — and the hope he cannot find ends in God, not in the grave.** **New.** `[T]` for the words; `[I]` for the comparison
   - **The petition.** The imperative of ערב ("stand surety") occurs only three times in the Hebrew Bible, and each time it is a prayer to God (WLC morphology):
     - "Be surety for Your servant for good" (Ps 119:122);
     - "O Lord, I am oppressed, be my security (עָרְבֵנִי)" (Isa 38:14, Hezekiah, when he "became mortally ill", 38:1);
     - "Lay down, now, a pledge for me (עָרְבֵנִי) with Yourself" (Job 17:3).
     - Isaiah and Job have the identical form.
   - **Hezekiah's lament shares more of the speech** (Isa 38:3, 5, 10–18):
     - the eyes raised "to the heights (לַמָּרוֹם)" (Isa 38:14; Job 16:19 "on high", בַּמְּרוֹמִים; 16:20 "my eye weeps to God");
     - weeping (בְּכִי, Isa 38:3; Job 16:16);
     - "the gates of Sheol" (Isa 38:10; Job 17:16 "the bars of Sheol");
     - the pit (שַׁחַת, Isa 38:17; Job 17:14);
     - hope at the edge of the pit: "those who go down to the pit cannot hope for Your faithfulness" (Isa 38:18, with a different verb, שׂבר, "hope"); Job 17:13, 15.
     - Hezekiah's prayer was answered: "I have heard your prayer (תְּפִלָּתֶךָ), I have seen your tears; behold, I will add (יוֹסִף) fifteen years to your life" (Isa 38:5).
     - Job: "my prayer (תְּפִלָּתִי) is pure" (16:17), the only תְּפִלָּה ("prayer") in Job (lemma); "he who has clean hands will add (יֹסִיף) strength" (17:9, literally; NASB95 "will grow stronger and stronger").
     - *Chance check:* Isaiah 38 ranks 29th of 887 Hebrew Bible chapters for rare lemmas shared with Job 16:16–17:16 (lemma frequency 70 or under). That is the top 3½ per cent, but not distinctive by count alone. The case rests on the identical petition. *Moderate (synthetic), queued.*
     - **v1.1:** the form is **moderate**, not high. It depends on the Masoretic pointing; the imperative with "me" is the natural form for anyone asking a guarantor; and 17:3b's "strike hands" is Proverbs' surety idiom (ערב + תקע only Job 17:3; Prov 6:1; 11:15; 17:18; 22:26). The Hezekiah frame is **low–moderate**: its other items are ordinary Sheol vocabulary, and Job 17:16 has "bars", not Isa 38:10's "gates", of Sheol `[S: audit 3]`.
   - **Hope, three times in three verses.** "If I hope (אֲקַוֶּה) for Sheol as my house …" (17:13, ESV; NASB95 "look for"); "where now is my hope (תִקְוָתִי)? And who regards my hope (וְתִקְוָתִי)?" (17:15).
     - The verb and the noun share the root קוה ("hope").
     - The round-one Leitwort continues from "You destroy man's hope" (14:19) to "He has uprooted my hope like a tree" (19:10).
     - The Greek of 17:13 is ἐὰν γὰρ ὑπομείνω ("if I endure / wait"), the verb of James's ὑπομονή ("steadfastness").
   - **Where hope goes.** Job's hope has nowhere on earth to go: the grave is "my father", the worm "my mother and my sister" (17:14). But the speech has already sent it to heaven (16:19) and asked God to guarantee it (17:3).
   - *Surfaced by:* Vocabulary, Repetition, Tool 11, Original Audience. *v1.0: high on the petition; moderate on the Isaiah 38 pattern.* **v1.1: moderate on the petition; low–moderate on the pattern** `[S: audit 3]`.

5. **The speech is anchored at both ends of the book: it turns chapter 3's words on Job himself, and it plants words that chapters 19 and 42 answer.** **New** except where marked. `[T]` for the words; `[I]` for the design
   - **Back to chapter 3:**
     - **The eyelids.** "Deep darkness (צַלְמָוֶת) is on my eyelids (עַפְעַפַּי)" (16:16). In chapter 3 Job called deep darkness on his day (3:5) and wished it might never "see the breaking dawn" — literally "the eyelids (עַפְעַפֵּי) of the dawn" (3:9, ESV "the eyelids of the morning"). עַפְעַף ("eyelid") occurs in Job only at 3:9, 16:16 and 41:10 (lemma). The darkness he called down on the day's eyelids now lies on his own.
     - **At ease.** "I was at ease (שָׁלֵו), but He shattered me" (16:12) turns "I am not at ease (שָׁלַוְתִּי)" (3:26). The root is the same; the lemmas differ.
     - **The gaping mouths.** In his old honour men "opened their mouth (פִיהֶם פָּעֲרוּ) as for the spring rain" (29:23). Now "they have gaped (פָּעֲרוּ) at me with their mouth" (16:10). פער ("open wide") with פֶּה ("mouth") occurs in Job only at 16:10 and 29:23 (lemma).
   - **Forward to chapter 19, the other HIGH unit of Sermon 4:**
     - **The kidneys.** "He splits my kidneys (כִּלְיוֹתַי) open" (16:13). "My kidneys (כִלְיֹתַי) faint within me!" (19:27, literally; NASB95 and ESV "my heart"). These are the only two כִּלְיָה ("kidney") in Job (lemma).
     - **The adversary.** "My adversary (צָרִי) glares at me" (16:9). "He … considered me as His enemy (כְצָרָיו)" (19:11).
     - **His anger.** "His anger (אַפּוֹ)" (16:9; 19:11).
     - **The siege.** "His arrows surround (יָסֹבּוּ) me … they have massed themselves (יַחַד) against me" (16:10, 13). "His troops come together (יַחַד) … and camp around (סָבִיב) my tent" (19:12).
     - **The friends.** "My friends (רֵעָי)" (16:20; 17:5) → "Pity me, O you my friends (רֵעָי)" (19:21).
     - **The dust.** "Shall we together go down into the dust (עָפָר)?" (17:16) → "at the last He will take His stand on the earth (עַל־עָפָר, 'upon the dust')" (19:25).
     - **The witness becomes the Redeemer.** "My witness is in heaven" (16:19) → "I know that my Redeemer lives" (19:25) (overview; sweep).
   - **Forward to chapter 42 — the sisters.** אָחוֹת ("sister") occurs in Job only three times (lemma):
     - Job's children invited "their three sisters (אַחְיֹתֵיהֶם)" to their feasts (1:4);
     - Job calls the worm "my mother and my sister (וַאֲחֹתִי)" (17:14);
     - at the end "all his brothers and all his sisters (אַחְיֹתָיו)" come and comfort him (42:11).
     - The family Job gave to the grave is given back to him as comforters. `[I]`
   - *Surfaced by:* Move 4, Repetition, Vocabulary, Translations. *High on the words; moderate–high on the design.*

---

## The Sixteen Tools

### 1. Author's Purpose

- **The purpose the book states.** The book states its own purpose only through the frame. The question "Does Job fear God for nothing?" (1:9) is asked in heaven. The verdict "you have not spoken of Me what is right as My servant Job has" (42:7) is given at the end. `[T]`
- **This speech's place in that purpose.** Job's second reply is where the book's longing for a mediator first becomes a confident claim: "Even now, behold, my witness is in heaven" (16:19). It is also where Job's speech to God reaches furthest. He asks God to guarantee him against God (17:3). `[T]` for the words; `[I]` for the function.
- **For the reader who knows the prologue.**
  - The reader knows there *is* an accuser in heaven (1:6–12; 2:1–7), and Job does not.
  - Job's claim of a witness in heaven is therefore set, unknowingly, opposite the Accuser who stood "among them" (1:6).
  - The reader is invited to hold both: in heaven one accused Job, and Job is sure that in heaven one will testify for him. `[I]` *Moderate–high.*

### 2. Context

#### Positional Necessity Check

- **What the preceding movement requires.**
  - Round one ended with Job saying that God destroys man's hope (14:19), and with the one hope Job could name: "You will call, and I will answer You" (14:15).
  - Eliphaz then opened round two by hardening every charge (15:1–35):
    - Job is doing away with the fear of God (15:4);
    - his own mouth condemns him (15:6);
    - the heavens themselves are not pure, and God trusts not his holy ones (15:15);
    - the wicked man is the one who runs at God like a warrior (15:25–26).
  - The book now needs Job's answer to a friend who has removed every helper from heaven. `[T]` for the content; `[I]` for the necessity.
- **Why this speech is here.**
  - It answers chapter 15 point by point (Headline 2). In answering, it places the witness in the very heaven Eliphaz had emptied (15:15; 5:1).
  - It also lays down most of the vocabulary Bildad will turn back on Job in chapter 18.
  - And it prepares the confession of 19:25, which takes the witness of 16:19 one step further. `[I]`

#### Surrounding context

- **Eliphaz, 15:1–35.**
  - Wisdom challenged (15:2–16, with "Were you the first man to be born?", 15:7, using Prov 8:25, overview).
  - The fate of the wicked (15:17–35).
- **Bildad, 18:1–21.** The fate of the wicked again, built of Job's words (Headline 2).
- **Job, 19:1–29.** "I know that my Redeemer lives" (19:25).

### 3. Structure

| Verses | Addressed to | Section | Function |
|---|---|---|---|
| 16:2–5 | the friends (2mp; 16:3 to Eliphaz, 2ms) | "Sorry comforters" | Answers 15:2, 11, 35. "If I were in your place" (16:4) |
| 16:6–8 | God (2ms, 16:7b–8a) | "You have laid waste all my company" | The first witness: Job's own body, "a witness" against him (16:8) |
| 16:9–14 | of God (3ms) | The assault | Wild beast, mob, betrayal, the archer, the warrior |
| 16:15–17 | of himself | Sackcloth, weeping — and innocence | "No violence in my hands, and my prayer is pure" (16:17) |
| 16:18–22 | the earth (2fs), then of the witness | The second witness | Blood not covered; the witness in heaven; the advocate "with God" |
| 17:1–2 | of himself | The grave ready | Mockers about me |
| 17:3–5 | God (2ms, 17:3–4) | "Be surety for me with Yourself" | God hid the friends' hearts; the betrayer's children |
| 17:6–9 | of God, then of the righteous | A byword; the righteous holds his way | "He who has clean hands will grow stronger" (17:9) |
| 17:10–16 | the friends (2mp, 17:10), the pit (2ms, 17:14) | Where is my hope? | Sheol my house; the worm my sister; hope goes down to the dust |

- **The address test** (WLC morphology; every second-person form in 16–17):
  - **The friends (2mp):** 16:2, 4, 5; 17:10.
  - **Eliphaz (2ms):** 16:3.
  - **God (2ms):** 16:7b, 8a; 17:3, 4. The pausal עִמָּךְ ("with You") at 17:3, tagged feminine, is counted as masculine.
  - **The earth (2fs):** 16:18.
  - **The pit (2ms):** 17:14 ("You are my father").
  - Job speaks to five addressees, and the three appeals that matter go upward: to God twice, and, between them, to the earth to keep his cry above ground. `[T]`
- **The divine names.** אֵל ("God") at 16:11; אֱלוֹהַּ ("God") at 16:20, 21. There is no יְהוָה ("the LORD") and no שַׁדַּי ("the Almighty"). The witness is "in heaven", and "God" is the court before whom he argues. `[T]`
- **The paragraphing.**
  - BHS sets a **setumah** after 15:35, 17:16, 18:21 and 21:34, and a petuḥah after 20:29. It prints **no marker after 19:29**, where the WLC transcription has a setumah (BHS export in `_texts/logos-exports`; confirmed by Patrick on screen, 5 Oct). *Corrected 5 Oct 2026:* this line first included 19:29 "as BHS prints it" without checking the BHS export in the folder.
  - **In round one every speech ended with a petuḥah** (5:27; 7:21; 8:22; 10:22; 11:20; 14:22). Patrick's BHS search confirmed all 26 petuḥot against the WLC (5 Oct).
  - The change of marker at the start of the second cycle is a feature of this manuscript's reading tradition, not authorial.
  - `[T]` for Leningrad; `[unchecked — apparatus spread]` for the setumot.
- **The inclusio of the speech.** The speech opens with the friends' words (16:2–5, "windy words") and closes with the friends (17:10, "I do not find a wise man among you"). Between them, Job turns from the friends to God and to the grave, twice. `[I]`

### 4. Linking Words

- **אַךְ עַתָּה ("But now", 16:7)** turns from the friends to God's assault. The phrase occurs only here in the Hebrew Bible (phrase search). `[T]`
- **עַל לֹא ("although there is no", 16:17)** concedes innocence in the middle of the assault. It is the Servant's phrase (Headline 3). `[T]`
- **גַּם־עַתָּה הִנֵּה ("Even now, behold", 16:19)** is the hinge of the speech.
  - At the point of greatest isolation, "even now" a witness exists. The adverb points to the present, not to the future.
  - גַּם עַתָּה occurs at Gen 44:10, 1 Sam 12:16, 1 Kgs 14:14, Hos 8:10, Joel 2:12 and Job 16:19 (phrase search). At Joel 2:12 it introduces a turning to God: "Yet even now", "Return to Me with all your heart".
  - `[T]`
- **כִּי ("for", 16:22; 17:4)** gives the reason for urgency (few years) and for the friends' blindness (God hid their hearts). `[T]`
- **וְאוּלָם ("But", 17:10)** turns back to the friends. אוּלָם ("but") is a speech-turning word in Job (1:11; 2:5; 5:8; 11:5; 12:7; 13:3, 4; 14:18; 17:10; 33:1). `[T]`
- **אִם ("if", 17:13, 16)** turns hope into a sequence of conditions. "If I hope for Sheol … where then is my hope?" (17:13, 15). `[T]`

### 5. Parallels

- **16:19 — עֵדִי // שָׂהֲדִי ("my witness // my advocate"), בַשָּׁמַיִם // בַּמְּרוֹמִים ("in heaven // on high").** Synonymous. The second word is an Aramaism (see Vocabulary). `[T]`
- **16:21 — גֶבֶר // בֶּן־אָדָם ("a man // a son of man"), עִם־אֱלוֹהַּ // לְרֵעֵהוּ ("with God // for his neighbor").** The parallelism likens the witness's case before God to an ordinary man pleading for his neighbour. The second line is asterisked in the Greek (see Translations). `[T]`
- **17:14 — the pit as father; the worm as mother and sister.** A family made of the grave. `[T]`
- **16:12 — two reduplicated verbs:** וַיְפַרְפְּרֵנִי ("He shattered me") and וַיְפַצְפְּצֵנִי ("He shook me to pieces"), before "He set me up as His target". The doubled syllables imitate the blows. `[I]` *Moderate.*

### 6. Narrator's Comment

N/A. The speech has only the narrator's formula, "Then Job answered" (16:1). There is no narrator's evaluation in the dialogue between 3:1 and 32:1–5.

### 7. Vocabulary

- **עֵד ("witness"), 10:17; 16:8; 16:19 — the only three in Job** (lemma 5707).
  - At 16:8 the witness is Job's shrivelled body: "You have shriveled me up (וַתִּקְמְטֵנִי), it has become a witness; and my leanness rises up against me, it testifies (יַעֲנֶה, literally 'answers') to my face". It is the courtroom verb ענה ("answer") used of a witness, and the formula of Deut 19:16 (Headline 1).
  - The witness against Job is his own suffering, read by the friends as evidence. `[T]`; `[I]` for "read by the friends".
  - קמט ("shrivel, snatch away") occurs only at 16:8 and 22:16 (lemma). In his third speech Eliphaz applies it to the wicked, "who were snatched away (קֻמְּטוּ) before their time" (22:16). `[T]`
- **שָׂהֵד ("witness, advocate", 16:19).**
  - It occurs only here in the Hebrew Bible (WLC, lemma 7717).
  - HALOT: an Aramaism, the participle of שׂהד, "witness", parallel with עֵדִי ("my witness"). BDB: an Aramaic loan-word equal to עֵד. `[S: HALOT; BDB]` (Logos round 2).
  - The Aramaic noun stands at Gen 31:47: Laban's name for the cairn, יְגַר שָׂהֲדוּתָא ("heap of witness"), beside Jacob's Hebrew גַּלְעֵד ("heap of witness"). The index files the Aramaic under its own number.
  - The pair עֵד / שָׂהֵד is a Hebrew word and its Aramaic equivalent, used side by side, as at Gen 31:47. `[T]` for the words; `[I]` for the echo. *Moderate.*
- **מְלִיצַי (16:20).**
  - The lemma (3887) is the hiphil participle of ליץ. The index files two senses under it:
    - "interpreter, envoy, mediator": Gen 42:23; 2 Chr 32:31; Isa 43:27; Job 33:23;
    - "scoffer": Ps 1:1; Ps 119:51; Proverbs, fourteen times.
  - Hence the two readings:
    - "My friends are my scoffers" (NASB95; ESV "My friends scorn me");
    - "My intercessor is my friend" (NIV84 text, with the other in the margin).
  - The Greek reads a petition: ἀφίκοιτό μου ἡ δέησις πρὸς κύριον ("may my plea come to the Lord").
  - **Elihu takes up the word.** At 33:23 he speaks of "an angel as mediator (מֵלִיץ) for him, one out of a thousand". He sets it among five uses of שַׁחַת ("the pit"; 33:18, 22, 24, 28, 30), Job's word at 17:14. In Job שַׁחַת otherwise occurs only at 9:31 (lemma).
  - Elihu's mediator who rescues from the pit answers this speech's two words. `[T]` for the words; `[I]` for the answer. *Moderate–high.*
- **יכח ("argue, decide a case").** The verb runs from Eliphaz's "the man whom God reproves (יוֹכִחֶנּוּ)" (5:17) through Job's "umpire" (9:33) and "I desire to argue (וְהוֹכֵחַ) with God" (13:3), to Eliphaz's sneer (15:3) and Job's hope (16:21). 15 verses in Job (lemma). `[T]`
- **עָרַב ("stand surety", 17:3), with תקע ("strike [hands]").**
  - **The surety idiom.** ערב with תקע occurs at Job 17:3, Prov 6:1, 11:15, 17:18 and 22:26 (lemma). The four in Proverbs warn the son against standing surety for a neighbour: "if you have become surety for your neighbor (לְרֵעֶךָ)" (Prov 6:1).
  - **Job and Proverbs.** Job asks God to do what Proverbs tells a wise man not to do. And 16:21 has just pictured the witness arguing "as a son of man for his neighbor (לְרֵעֵהוּ)". `[T]` for the words; `[I]` for the contrast. *Moderate.*
  - **Judah's surety.** It is also Judah's verb when he stands surety for Benjamin: "I myself will be surety for him (אֶעֶרְבֶנּוּ)" (Gen 43:9; 44:32) (sweep).
  - **The petition.** For the imperative of the verb, see Headline 4.
- **The violent vocabulary, 16:9–14.**
  - The terms: טרף ("tear", of a beast); שׂטם ("hate, bear a grudge"); חרק שֵׁן ("gnash the teeth"); לטשׁ ("sharpen"); פרר / פצץ ("shatter", reduplicated); רַבִּים ("archers"); פלח ("split"); פרץ ("breach", of a city wall); גִּבּוֹר ("warrior").
  - **"He hated me."** שׂטם occurs at Gen 27:41; 49:23; 50:15; Ps 55:4; Job 16:9; 30:21 (lemma). It is close in sound to שָׂטָן ("accuser"), whom Job never names. `[T]` for the words; `[I]` for the sound. *Low–moderate.*
  - **The imagery.** Beast, mob, archer, besieger, warrior: Job pictures God in every hostile role. `[T]`
- **Mourning vocabulary, 16:15–16.**
  - **Sewing.** "I have sewed (תָּפַרְתִּי) sackcloth over my skin (גִלְדִּי)". גֶּלֶד ("skin") occurs only here (lemma). תפר ("sew") occurs at Gen 3:7 (the fig leaves), Eccl 3:7, Ezek 13:18 and here. `[T]`
  - **The horn.** "And thrust my horn (קַרְנִי) in the dust (בֶעָפָר)". The horn is the idiom of strength and honour: "my horn is exalted in the LORD" (1 Sam 2:1). `[T]`
  - **"Red."** "My face is flushed (חֳמַרְמְרֻה, ketiv)". The reduplicated form of חמר occurs only at Job 16:16, Lam 1:20 and Lam 2:11 (WLC morphology; the index files Job's form under a separate homograph). Both Lamentations verses describe the speaker's inward parts churning in grief, and Lam 2:11 adds "my eyes fail (כָּלוּ … עֵינַי)" (compare 17:5, 7). `[T]` *Moderate–high* — another Lamentations contact.
- **Hapaxes and rare words.**
  - **Only here in the Hebrew Bible** (lemma): עֲוִיל ("ruffians", 16:11); מְרֵרָה ("gall", 16:13); הֲתֻלִים ("mockers", 17:2); מְשֹׁל ("byword", 17:6); תֹפֶת ("spitting", 17:6); יְצֻרַי ("my members", 17:7).
  - **Rare elsewhere:** ירט ("throw", 16:11; also Num 22:32); דלף ("drip", 16:20; also Eccl 10:18 and Ps 119:28, "my soul weeps because of grief"); מוֹרָשֵׁי ("desires, possessions", 17:11; also Isa 14:23 and Obad 17).
  - The speech's vocabulary is unusually rare. `[T]`
- **Hope (תִּקְוָה, קוה).** Treated under Repetition and Headline 4.
- **Purity: זַךְ, זכה, זכך, טהר ("pure, clean").** Job's purity is answered across the book:
  - Bildad (8:6, "if you are pure and upright") and Zophar (11:4, "you say … I am pure") quote it;
  - Eliphaz denies it to man (15:14) and to the heavens (15:15);
  - Job claims it for his prayer (16:17) and promises strength to the "clean of hands" (טְהָר־יָדַיִם, 17:9);
  - Elihu quotes it back (33:9, "I am pure").
  - טהר ("be clean") occurs in Job at 4:17 (the vision: "Can a man be pure before his Maker?"), 17:9 and 37:21 (lemma). `[T]`

### 8. Translations

- **16:20 — the friends or the intercessor.**
  - NASB95: "My friends are my scoffers".
  - ESV: "My friends scorn me".
  - NIV84: "My intercessor is my friend" (margin "My friends treat me with scorn").
  - **The congregation (ESV) will hear only the hostile reading.** The Hebrew allows the other, and the Greek reads a plea. The preacher should know the ambiguity, though nothing here asks him to announce it. `[T]`
- **16:21 — who argues.**
  - The Hebrew is וְיוֹכַח לְגֶבֶר עִם־אֱלוֹהַּ: a third-person jussive ("and may he argue") with לְ ("for") marking the one argued for.
  - **ESV:** "that he would argue the case of a man with God, as a son of man does with his neighbor". The witness argues, and "son of man" is kept.
  - **NIV84:** "on behalf of a man he pleads with God as a man pleads for his friend".
  - **NASB95:** "O that a man might plead with God as a man with his neighbor!". This makes the man himself the pleader and levels "son of man".
  - **Here the ESV is closer to the Hebrew than the study text, and the pulpit text carries the finding.** `[T]`
- **17:3 — the pledge.**
  - ESV: "Lay down a pledge for me with you; who is there who will put up security for me?" NASB95: "Lay down, now, a pledge for me with Yourself; Who is there that will be my guarantor?" NIV84: "Give me, O God, the pledge you demand. Who else will put up security for me?" — which loses "with Yourself".
  - **The Hezekiah link is lost in every English version.** At Isa 38:14 the ESV renders the same form "be my pledge of safety!", the NASB95 "be my security".
- **17:13 — hope.** ESV "If I hope for Sheol as my house"; NASB95 "If I look for Sheol as my home". **The ESV keeps the root קוה ("hope") audible beside the two "hopes" of 17:15. The NASB95 does not.**
- **17:16.** ESV "the bars of Sheol"; NIV84 "the gates of death"; NASB95 "Will it go down with me to Sheol?", which follows the BHS proposal or the Greek, "with me". See Textual Variants.
- **16:16 and 3:9 — the eyelids.**
  - ESV: "on my eyelids is deep darkness" (16:16) and "the eyelids of the morning" (3:9). **Both are audible.**
  - NASB95: "the breaking dawn" (3:9), which loses the link.
- **The ancient versions** (Rahlfs, Hebrew numbering; Swete wording, Swete numbering one higher from 16:5):
  - **16:2 — παρακλήτορες κακῶν ("comforters of evils").**
    - παρακλήτωρ ("comforter") occurs in Greek Job only here and nowhere else in Swete.
    - The New Testament's παράκλητος ("advocate, helper") is the related noun of John 14:16, 26; 15:26; 16:7; 1 John 2:1.
    - In the Greek, the friends are the false *paraklētores*. The witness in heaven is the true one, in function though not in Greek (16:19 has μάρτυς, "witness", and συνίστωρ, "one who knows with me"). *Category 1, translation; moderate as colour.*
  - **16:19 — ὁ μάρτυς μου … ὁ δὲ συνίστωρ μου ἐν ὑψίστοις ("my witness … my fellow-witness on high").** συνίστωρ occurs in Swete only here.
  - **16:20 — ἀφίκοιτό μου ἡ δέησις πρὸς κύριον ("may my plea come to the Lord").** The Greek reads מְלִיצַי as a plea, not as "scoffers". *Category 1 (an interpretive rendering) or 2 (another vocalisation); uncertain.*
  - **16:21b — "and a son of man to his neighbor" is asterisked** (καὶ υἱὸς ἀνθρώπου τῷ πλησίον αὐτοῦ). The Old Greek lacked the line, and it was supplied from the Hexapla. **The Greek "son of man" here is not the Old Greek's.** `[T]` for Rahlfs.
  - **The other asterisked lines:** 16:3b; 16:8b–c; 17:3b–5a (Rahlfs places the closing sign after 17:5a); 17:10b; 17:12b; 17:16b. The Old Greek of this speech was shorter. `[T]`
  - **16:11 — παρέδωκεν γάρ με ὁ κύριος εἰς χεῖρας ἀδίκου ("the Lord handed me over into the hands of the unjust").**
    - παραδίδωμι ("hand over") is the passion-prediction verb (Mark 9:31, "delivered into the hands of men").
    - The Greek supplies ὁ κύριος ("the Lord") for אֵל ("God").
    - *Category 3 at a distance (sweep); moderate.*
  - **17:3 — the Greek is different:** ἔκλεψαν δέ μου τὰ ὑπάρχοντα ἀλλότριοι ("strangers have stolen my goods"). It may read the consonants of עָרְבֵנִי ("be surety for me") otherwise; the surety petition is in the asterisked lines only. *Category 1; the Hebrew carries the finding.*
  - **17:13 — ἐὰν γὰρ ὑπομείνω ("if I endure / wait") for אִם־אֲקַוֶּה ("if I hope").** ὑπομένω ("endure") here and the noun ὑπομονή ("endurance") at 14:19 make the Greek's hope vocabulary the vocabulary of James 5:11. *Moderate as colour.*
  - **17:15b — ἢ τὰ ἀγαθά μου ὄψομαι; ("or shall I see my good things?").** BHS suggests the translator read וְטוֹבָתִי ("my good") for the second וְתִקְוָתִי ("my hope"). *Category 2 candidate; moderate.* The Hebrew repetition of "hope" is the better-attested text and carries the finding.
- **Pulpit divergence note (ESV).**
  - **The ESV carries:** the two witnesses (10:17; 16:8; 16:19, "witness" each time); the argued case (16:21, with "son of man"); hope (17:13, 15); the eyelids (3:9; 16:16); "although there is no violence" (16:17, and Isa 53:9 "although he had done no violence"). It also carries "set me up as his target" (16:12, and Lam 3:12 "set me as a target"), the kidneys (16:13, and Lam 3:13), and "the comforts of God" / "miserable comforters" (15:11; 16:2).
  - **The ESV loses:**
    - the umpire's verb, between "arbiter" (9:33) and "argue" (16:21);
    - "trouble" (15:35, "conceive trouble") against "miserable comforters" (16:2);
    - the surety petition shared with Isa 38:14;
    - the kidneys of 19:27 ("My heart faints within me", in both English versions).
    - **The eyelids** are lost in the NASB95.

### 9. Tone and Feel

- **The voice moves through four registers:**
  - **Contempt** for the friends: "Sorry comforters are you all" (16:2).
  - **Terror** before God the assailant (16:9–14), in the most violent images of God in the book: beast, mob leader, archer, besieger, warrior.
  - **Defiant innocence** (16:17).
  - **A sudden confidence** (16:19), followed at once by exhaustion: "My spirit is broken, my days are extinguished, the grave is ready for me" (17:1).
  - `[T]`
- **The hope is real and the despair is real, and the speech does not reconcile them.** It ends with a question and no answer: "Shall we together go down into the dust?" (17:16). `[T]`
- **The emotional centre is weeping:**
  - "My face is flushed from weeping" (16:16);
  - "My eye weeps to God" (16:20, דָּלְפָה עֵינִי, "my eye drips");
  - "My eye has also grown dim because of grief" (17:7).
  - Job's tears go to God, not to the friends. `[T]`

### 10. Repetition

- **"Witness" and its verbs:** עֵד at 16:8 and 16:19; שָׂהֵד at 16:19; ענה ("answer, testify") at 16:3 and 16:8; יכח ("argue") at 16:21. `[T]`
- **"Eye" (עַיִן): five times in the speech** (16:9, 16:20; 17:2, 17:5, 17:7) (lemma), with "eyelids" (עַפְעַפַּיִם) at 16:16.
  - The adversary sharpens *his* eyes (16:9). Job's eye drips to God (16:20), dwells on the mockers' provocation (17:2) and grows dim (17:7). The betrayer's children's eyes fail (17:5).
  - The book's next word on eyes is 19:27: "my eyes will see (God)". `[T]`
- **"Friend / neighbour" (רֵעַ):**
  - In this speech: 16:20 ("my friends"), 16:21 ("his neighbor") and 17:5 ("informs against friends").
  - It then returns at 19:21 ("Pity me, O you my friends") and in the epilogue's "your two friends" (42:7) and "when he prayed for his friends" (42:10).
  - In this speech the friends betray, and the witness pleads as one pleads for a neighbour. `[T]`
- **"Days" and "years":** 16:22 (years); 17:1, 11, 12 ("my days", "my days are past", "night into day"). `[T]`
- **"Hope":** קוה ("hope", verb) at 17:13 and תִּקְוָה ("hope", noun) twice at 17:15 (lemma). `[T]`
  - The noun stands in Job in 12 verses. 9 of them fall in round one (4:1–14:22 report). 17:15 is the first after 14:19, and 19:10 the next.
  - Swete keeps ἐλπίς ("hope") at 17:15a.
- **"Dust" and the grave:**
  - עָפָר ("dust") at 16:15 and 17:16;
  - קְבָרִים ("graves") at 17:1;
  - שְׁאוֹל ("Sheol") at 17:13 and 17:16;
  - שַׁחַת ("pit") at 17:14;
  - רִמָּה ("worm") at 17:14.
  - The speech ends in the grave, as every speech of Job's in round one did. `[T]`
- **Purity and violence:**
  - "No violence (חָמָס) in my hands (כַפָּי)" and "my prayer is pure" (16:17);
  - "he who has clean hands (טְהָר־יָדַיִם)" (17:9).
  - The hands are clean twice. `[T]`
- **"Together" (יַחַד):** the mob massed "together" against Job (16:10), and Job and his hope going down "together" into the dust (17:16). Bildad's troops come "together" at 19:12. `[T]`

### 11. Quotation / Allusion — with Move 4

**Isa 53:9 → 16:17** *(v1.0: high on the words. **v1.1: low–moderate** — the exclusive string is short and functional, and its fuller form is shared with 1 Chr 12:18* `[S: audit 3]`*; direction open)*

- **Move 1 — source context.** The fourth Servant Song.
  - The Servant "was assigned a grave with wicked men … because He had done no violence (עַל לֹא־חָמָס עָשָׂה), nor was there any deceit in His mouth" (Isa 53:9).
  - The Song moves from the Servant's suffering for others (53:4–6) and his silence (53:7) to his vindication and intercession: "He … interceded for the transgressors" (53:12).
- **Move 2 — book usage.** Isaiah is live in Job:
  - 12:9 = Isa 41:20 (overview, high);
  - Isa 44:24 at 9:8a (moderate–high) `[S: audit]`;
  - Isa 50:8–9 at 13:19, 28 (moderate–high) `[S: audit]`;
  - Isa 40:27 at 3:23 (queued);
  - Isa 19:5 at 14:11 (queued).
  - This chapter adds Isa 50:6 at 16:10 and Isa 53:9 at 16:17. Together these make a sequence of Servant contacts:
    - the courtroom (13:19, 28);
    - the struck cheek (16:10);
    - "no violence" (16:17);
    - the spitting (30:10);
    - the intercession (42:8–10).
    - **(synthetic)**
- **Move 3 — OT to OT.** Isa 50:6 (the cheek, the spitting) and 53:9 (no violence) fall within one servant sequence. Job 16 touches both within seven verses. Lam 3:30 (the cheek given to the smiter) is the third member of the same complex.
- **What it adds.**
  - Job's protest of innocence is spoken in the words the canon uses for the Servant who suffered "although he had done no violence".
  - The difference is as important as the likeness.
    - **The Servant's mouth:** it had "no deceit", and he "did not open His mouth" (Isa 53:7).
    - **Job's mouth:** it is full of protest. Job opened his mouth (3:1) and has not shut it.
  - `[I]` *v1.1: low–moderate on the words; the type is low. Keep it as canonical reflection* `[S: audit 3]`.
- **The Greek.** Isa 53:9 has ἀνομίαν οὐκ ἐποίησεν ("he did no lawlessness"); Job 16:17 has ἄδικον δὲ οὐδὲν ἦν ἐν χερσίν μου ("there was nothing unjust in my hands"). The link is Hebrew-only (Category 1).

**Lamentations 2–3 → 16:4–16** *(v1.1: **high** — Lam 2:10–17 is the main source, with Lam 3:12–13, 30* `[S: audit 3]`*; direction open)*

- **Move 1 — source context.**
  - Lam 3 is the lament of "the man who has seen affliction because of the rod of His wrath" (3:1).
  - God is pictured as a bear and a lion (3:10), then as an archer: "He bent His bow and set me as a target for the arrow. He made the arrows of His quiver to enter into my inward parts" (3:12–13). The speaker becomes "a laughingstock to all my people" (3:14).
  - The poem turns: "This I recall to my mind, therefore I have hope" (3:21). It counsels: "Let him give his cheek to the smiter, let him be filled with reproach. For the Lord will not reject forever" (3:30–31).
  - Lam 2:16 has the enemies gaping and gnashing their teeth over Zion. Lam 2:11 has the inward parts in ferment and the eyes failing.
- **Move 2 — book usage.** The overview lists Lam 3 as a live source (19:8; 16:12; 16:10; moderate). This run adds:
  - **two exclusive pairs:**
    - target + kidneys (16:12–13 / Lam 3:12–13);
    - cheek + reproach (16:10 / Lam 3:30);
  - **the reduplicated form חמר** ("be in ferment") at 16:16, Lam 1:20 and Lam 2:11 (only these three);
  - **the root שׁמם** ("desolate"; 16:7 / Lam 3:11);
  - **gnashing** (16:9 / Lam 2:16);
  - **the people's mockery:** "a byword of the people (עַמִּים)" (17:6) against "a laughingstock to all my people (עַמִּי)" (Lam 3:14).
- **Move 3 — OT to OT.** Lam 3:30 and Isa 50:6 are the two places where a sufferer gives the cheek to the smiter. Job 16:10 is struck on the cheek without giving it.
- **What it adds.**
  - **Shared images.** Job's assault is pictured in the images of Jerusalem's ruin, personified in one man.
  - **A different conclusion.** Lamentations reaches "Perhaps there is hope (תִּקְוָה)" (Lam 3:29) and counsels the sufferer to give his cheek. Job asks "Where now is my hope?" (17:15), and is struck on the cheek in protest.
  - **The appeal goes to the same place.** Both appeal to God against God's own wrath: "The Lord will not reject forever" (Lam 3:31); "Lay down, now, a pledge for me with Yourself" (Job 17:3).
  - `[I]` *v1.0: moderate–high.*
  - **v1.1 (claim audit 3).** The source is Lam 2 more than Lam 3.
    - Lam 2:10–17 ranks 1st of 887 against 16:4–16 and beats every Job-passage null.
    - Add its exclusives: שׁפך + לָאָרֶץ + organ (Lam 2:11 / 16:13) and עָפָר + שַׂק (Lam 2:10 / 16:15).
    - Add the shaken head of Lam 2:15 at 16:4.
    - *High (words)* `[S: audit 3]`.
  - **Cross-book note:** the Lamentations 3:1–33 dig (v1.1) may wish to record these exclusives from the Lamentations side.

**Isa 38:14 (with Ps 119:122) → 17:3** *(v1.1: moderate on the petition; low–moderate on the wider pattern* `[S: audit 3]`*)*

- **Move 1 — source context.**
  - Hezekiah, mortally ill (Isa 38:1), "wept bitterly" (38:3) and was told: "I have heard your prayer, I have seen your tears; behold, I will add fifteen years to your life" (38:5).
  - His written lament (38:10–20) moves through these stages:
    - from "the gates of Sheol" (38:10)
    - through "My eyes look wistfully to the heights; O Lord, I am oppressed, be my security (עָרְבֵנִי)" (38:14)
    - to "It is You who has kept my soul from the pit (מִשַּׁחַת) of nothingness" (38:17)
    - and "Those who go down to the pit cannot hope for Your faithfulness" (38:18).
- **Move 2 — book usage.** Hezekiah's psalm is otherwise unused in Job. *Single use; not live.* **History of interpretation (Logos round 4):** Delitzsch, on 16:20, compares דָּלְפָה ("weeps, drips") with דַּלּוּ at Isa 38:14 ("my eyes look wistfully"), so a major commentator joins 16:20 to the verse whose עָרְבֵנִי Job repeats at 17:3. Isa 38:14 holds the eyes, the heights (מָרוֹם) and the surety in one verse; Job spreads them over 16:19–17:3. `[S: Delitzsch]`
- **Move 3 — OT to OT.** Ps 119:122, "Be surety for Your servant for good; do not let the arrogant oppress me", has the same petition and the same oppressors (עשׁק, "oppress"; Isa 38:14 עָשְׁקָה, "I am oppressed").
- **What it adds.**
  - A righteous man at the gate of Sheol prays "be my surety", with tears, and God hears. Job prays the same words and is not yet heard.
  - The canon puts an answered form of Job's prayer beside him. `[I]`
  - *Chance check:* Isaiah 38 ranks 29th of 887 chapters for rare lemmas shared with 16:16–17:16. That is high but not distinctive. **The petition carries the case, not the count.** Queued.

**Deut 19:15–19 → 16:8, 17** *(v1.1: moderate — a legal idiom* `[S: audit 3]`*)*

- **Move 1.**
  - The law of witnesses: "A single witness shall not rise up against a man … on the evidence of two or three witnesses a matter shall be confirmed" (Deut 19:15).
  - If a malicious witness "rises up … to accuse him", and is proved false, "you shall do to him just as he had intended to do to his brother" (19:16–19).
- **Moves 2–3.**
  - Deuteronomy is live in Job: Deut 32:39 at 5:18 and 10:7; Deut 28:29 at 5:14 `[S: audit]`.
  - Ps 27:12 and Ps 35:11 use the same image of false witnesses rising up. Psalm 35 adds the gnashing teeth (35:16).
- **What it adds.** Job's suffering "rises up" as a witness against him. In the terms of the law it is a single, malicious witness, and the speech goes on to supply the second, true one (16:19). `[I]`

**Gen 4:10; Isa 26:21 → 16:18** *(Gen 4:10 moderate–high. Isa 26:21, v1.1: one of several partners, with Ezek 24:7–8 as close; Isa 26 as the canonical answer is low–moderate* `[S: audit 3]`*)*

- **Gen 4:10:** "The voice of your brother's blood is crying (צֹעֲקִים) to Me from the ground." Job: "O earth, do not cover my blood (דָמִי), and let there be no resting place for my cry (לְזַעֲקָתִי)." The cry-verbs are cognate (צעק / זעק); BHS cross-refers Gen 4:10.
- **Isa 26:21:** "the earth will reveal her bloodshed and will no longer cover her slain". כסה ("cover") with דָּם ("blood") and אֶרֶץ ("earth") occurs in one verse at Ezek 24:7, Hab 2:17, Isa 26:21 and Job 16:18 (lemma).
- Job asks the earth for what Isaiah says it will one day do. Ash (*Preaching the Word*) links 16:18 with Gen 4 and Isa 26:21 `[S]` (Logos round 2).
- **The New Testament:** "the sprinkled blood, which speaks better than the blood of Abel" (Heb 12:24).

**Heaven and earth as witnesses — Deut 4:26; 30:19; 31:28 → 16:18–19** *(moderate; Move 1 only)*

- Moses calls heaven and earth "to witness against you" (Deut 30:19). עוד ("call to witness") with "the heavens" and "the earth" occurs only in these three verses (lemma).
- Job turns to the earth (16:18) and to heaven (16:19) as witnesses for him. `[I]`

**Prov 6:1; 17:18 → 17:3** *(moderate; Move 1 only)* — See Vocabulary. Proverbs forbids the wise man to strike hands for a neighbour; Job asks God to do it. *v1.1:* claim audit 3 confirms ערב + תקע only at Job 17:3 and Prov 6:1; 11:15; 17:18; 22:26 `[S: audit 3]`.

**Ps 22:8 [Eng 22:7] → 16:4** *(v1.1: low; queue #7 closed)*

- "I could … shake my head (וְאָנִיעָה … רֹאשִׁי) at you" (16:4).
- נוע ("shake") with רֹאשׁ ("head") occurs at 2 Kgs 19:21 = Isa 37:22, Lam 2:15, Ps 22:8, Ps 109:25 and Job 16:4 (lemma).
- Job says he *could* do to the friends what the mockers of Ps 22 and Lam 2 did. It is a fourth Psalm 22 touchpoint for queue #7, but a common idiom. *v1.1: low.* Ps 22 is not distinctive as a source in Job (6th of 36 comparable psalms), and Lam 2:15, already the source of 16:9–16, is the closer partner `[S: audit 3]`.

**Smaller contacts** *(Move 1 only)*

- **Deut 34:7 → 17:7.** "My eye has also grown dim (וַתֵּכַהּ … עֵינִי)". כהה with עַיִן occurs at Gen 27:1 (Isaac), Deut 34:7 (Moses, whose eye "was not dim"), Zech 11:17 and Job 17:7 (lemma). *Low–moderate; colour.*
- **Gen 3:7 → 16:15.** "Sewed" (תפר), of the first couple's coverings. *Low.*
- **Ps 6:8; 31:10 → 17:7.** "My eye has wasted away with grief (מִכַּעַס עֵינִי)". The same noun, with a different verb. *Moderate.*

**Internal (Move 4)**

- **Answers to earlier passages:**
  - **15:2, 3, 11, 14–15, 20, 25–26, 35** → 16:2, 3, 14, 17, 19, 21, 22 (Headline 2). *High on the exclusive links.*
  - **9:33 and 10:17** → 16:19, 21: the umpire and the witnesses (sweep). *High.*
  - **2:11** → 16:2: the friends came "to comfort" (sweep). *High.*
  - **3:5, 9** → 16:16: the eyelids (Headline 5). *High on the words.*
  - **3:26** → 16:12: "at ease", same root. *Moderate.*
  - **29:23** → 16:10 (the order reversed in the book): the gaping mouths. *Moderate–high.*
  - **4:7** → 17:8. Eliphaz's pair "innocent (נָקִי) … upright (יְשָׁרִים)" returns: "The upright (יְשָׁרִים) will be appalled at this, and the innocent (וְנָקִי) will stir up himself against the godless". יָשָׁר with נָקִי occurs in one verse only at Deut 21:9, Job 4:7 and 17:8 (lemma). Eliphaz asked who of the innocent and upright ever perished; Job answers that the innocent and upright will be appalled at what has happened to him. `[T]` *High on the words.*
  - **10:13** → 17:4. "These things You have concealed (צָפַנְתָּ) in Your heart" (10:13); "You have kept (צָפַנְתָּ) their heart from understanding" (17:4). The same verb form, with "heart". God hid his purpose in his own heart, and now hides understanding from theirs. *Moderate.*
  - **11:20** → 17:5. Zophar: "the eyes of the wicked will fail (תִּכְלֶינָה)". Job: "the eyes of his children also will languish (תִּכְלֶנָה)". כלה ("fail") with עַיִן ("eye") also occurs at 31:16, and widely outside Job. *Moderate.*
  - **13:9** → 17:2. התל ("mock"): the verb at 13:9, the noun הֲתֻלִים ("mockers") at 17:2 — the only two in Job. *Moderate.*
  - **14:13–15** → 16:19–22; 17:13–16. Sheol as hiding place (14:13) becomes Sheol as house (17:13). The God who would call (14:15) becomes the witness who argues (16:21). *Moderate–high.*
  - **10:21; 7:9–10** → 16:22. "Before I go — and I shall not return" (10:21); "I shall go the way of no return" (16:22). The lemma index files the two forms of "go" under different numbers (3212, 1980). *High on the words.*
- **Planted for later:**
  - **16:8 קמט ("shrivel")** → 22:16 (Eliphaz). *High on the words.*
  - **16:9; 17:1, 8, 11, 12, 16** → chapter 18 (Bildad) (Headline 2). *High on the exclusives.*
  - **16:9, 10, 13, 20; 17:16** → 19:11, 12, 21, 25, 27 (Headline 5). *High on the words.*
  - **16:19–21** → 19:25–27 (sweep; overview). *High.*
  - **16:20 מֵלִיץ; 17:14 שַׁחַת** → 33:18–30 (Elihu's mediator and the pit). *Moderate–high.*
  - **16:15 קַרְנִי ("my horn")** → 42:14, Keren-happuch (קֶרֶן הַפּוּךְ). The index files the name separately (7163). Surface form only (sweep). *Uncertain.*
  - **17:14 אָחוֹת ("sister")** → 42:11, with 1:4 (Headline 5). *Moderate–high.*
  - **16:2 נחם ("comfort")** → 42:11 "comforted him" (overview Echo Table). *High.*

### 12. Genre

- **The form.** Disputation speech in poetry, combining several known forms:
  - a rebuttal of the opponent (16:2–5; 17:10);
  - an individual lament, with the enemy-assault motif and the "eye" and "tears" of the psalms (16:6–17; 17:6–7);
  - a legal appeal: the witness, the advocate, the pledge (16:18–17:5);
  - a meditation on death (17:11–16).
  - `[T]` for the elements; `[I]` for the classification.
- **What the genre forbids.** Lament is not doctrine. Job's portrait of God as a beast and a warrior (16:9–14) is what lament says. It is not a statement about God's character for the reader to adopt (see Difficult Verses). `[I]`
- **What the legal form adds.** Because Job speaks as a litigant, his witness and surety are legal roles. The witness testifies to the truth of Job's case; the surety guarantees Job's appearance and the debt. They are not mystical intermediaries. `[I]`

### 13. Copycat

- **The cautions.**
  - Job's speech is not offered as a pattern of how to speak to friends: he rebukes them as "sorry comforters".
  - Nor is it offered as a pattern of how to picture God.
  - What the book commends is the direction of his speech (42:7; the introductory backbone): his "eye weeps to God" (16:20), and his appeals go upward.
- **What can be copied.**
  - In isolation, the sufferer may look past failed comforters to God's own testimony in heaven.
  - The sufferer may also ask God for what he cannot supply for himself — a guarantee "with Yourself".
  - `[I]`

### 14. Bible Timeline

- **Setting.** The story is set in a patriarchal world (overview). The book's composition and date are not stated `[S]`.
- **Canonical position.** Ketuvim, after the Psalter (BHS order). The reader comes to Job 16 knowing:
  - the Psalter's laments (Ps 22; 35; 119);
  - the Prophets' Servant (Isa 50; 53) and Hezekiah's psalm (Isa 38);
  - in the canonical Ketuvim, Lamentations comes after Job, so the Lamentations contacts are read forward from Job.
  - `[T]` for the order; direction of dependence open.
- **The New Testament end of the line.** The reader who knows the New Testament reads 16:19–21 alongside "we have an Advocate with the Father" (1 John 2:1) and "He always lives to make intercession for them" (Heb 7:25). They read 17:3 alongside "Jesus has become the guarantee (ἔγγυος) of a better covenant" (Heb 7:22, the only ἔγγυος in the NT, SBLGNT). See Christological Reading.

### 15. Who Am I?

- **Like Job, the reader who suffers** and is accused by those who should comfort. "My friends are my scoffers; my eye weeps to God" (16:20).
- **Like the friends, the reader who comforts with doctrine.** "I too could speak like you, if I were in your place" (16:4).
  - Job's line reminds the comforter that circumstance, not wisdom, separates speaker and sufferer.
  - "I could strengthen you with my mouth" (16:5) is sarcasm in context, though the ESV's "the solace of my lips would assuage your pain" can be heard straight.
- **Unlike Job, the reader who knows the prologue** — and so knows what "witness in heaven" means against an accuser in heaven. `[I]`

### 16. So What?

**Stage 1 — the response the speech seeks.** `[I]`
- The friends' theology has emptied heaven of help (15:15). The reader should see that Job, under God's hand, looks to heaven anyway, and asks God for testimony and surety against God's own blows.
- The book honours that direction (42:7). The friends' "comfort" is shown to be "trouble" (16:2).

**Stage 2.**

| Domain | Application |
|---|---|
| **Worldview** | Heaven is not empty of help, whatever comforters say. God himself is the court of appeal, even when he appears as the assailant |
| **Stop** | Comforting with formulae ("windy words", 16:3); reading suffering as evidence against the sufferer — the "malicious witness" of Deut 19:16 |
| **Start** | Taking tears to God (16:20); asking God to guarantee what we cannot (17:3); sitting where the sufferer sits ("if I were in your place", 16:4) |
| **Motivation** | The witness Job longed for has a name: "we have an Advocate with the Father, Jesus Christ the righteous" (1 John 2:1). The surety Job asked God to provide God has provided (Heb 7:22) |

**Four audiences.**

| Audience | What the speech means |
|---|---|
| **For me** | When I have nothing left but tears, they can go to God. When the evidence of my life seems to testify against me, there is another witness |
| **For a Christian friend** | Do not be the "sorry comforter". Imagine your soul in his place (16:4). Pray *for* him, as the witness argues "for a man with God" |
| **For the church** | A church can be a company of comforters who are "trouble". It can also be the "brothers and sisters" who at last comfort (42:11) |
| **For an unbeliever** | The Bible lets a man say that God tore him like a beast — and still say "my witness is in heaven". Its faith has room for the worst experience of God, and for an advocate within it |

**Prayer.** "Lay down, now, a pledge for me with Yourself" (17:3) — prayed in Christ, who "always lives to make intercession" (Heb 7:25).

## Extensions

### Original Language Observations

- **16:4 לוּ־יֵשׁ ("if there were") and the reading of 9:33.**
  - Job's "I too could speak like you, if I were in your place" is literally "if your soul were (לוּ יֵשׁ) in my soul's place".
  - **Every לוּ immediately followed by יֵשׁ** in the WLC index (lemma 3863 + 3426): Num 22:29 ("Would that there were a sword in my hand"), Job 16:4 and Job 9:33.
  - **The index's treatment of 9:33.** It files 9:33's לֹא under the lemma of לוּ ("if only"), reading the word as לוּ spelled with aleph, though its morphology code marks a negative.
  - **The consequence.** Job's own idiom for an unreal condition is the construction the versions read at 9:33: "Would that there were an umpire between us". The parallel of this speech, five verses before the witness, strengthens that reading.
  - `[T]` *Moderate–high.* This adds to the Logos round 2 finding (Num 22:29). The index's own lemma at 9:33 was not noticed then.
- **16:18 אֶרֶץ אַל־תְּכַסִּי ("O earth, do not cover").** A feminine jussive with אַל ("do not"): the earth is addressed directly as a person. `[T]`
- **16:20 מְלִיצַי.** The index parses it as a hiphil participle, masculine plural with "my" ("my scoffers / my interpreters"). The singular "my intercessor" of the NIV84 needs a different pointing or a loose rendering. `[T]`
- **16:21 וְיוֹכַח לְגֶבֶר.** A waw with the **short (jussive) form** of the hiphil of יכח, with לְ ("for"): "that he may argue …". *Corrected 5 Oct 2026 (Logos round 4):* the index tags the form imperfect, and this report first followed the tag, but the vocalisation is the short form. The long imperfect is יוֹכִיחַ (13:10; Isa 11:3; Prov 3:12); the short form stands in the jussive at Hos 4:4 (וְאַל־יוֹכַח, "let no one reprove") and 1 Chr 12:18 (וְיוֹכַח, "may the God of our fathers see and rebuke"), and in the wayyiqtol (Gen 31:42; Ps 105:14) (WLC). Delitzsch reads it as "voluntative in a final signification, as 9:33". After the jussives of 16:18 it carries the wish. The לְ marks the man as beneficiary (Delitzsch: "of the client", as Isa 11:4), and עִם marks the opponent ("against God", as Ps 55:19; 94:16). `[T]` for the form; `[S: Delitzsch]` for עִם.
- **17:3 שִׂימָה־נָּא עָרְבֵנִי עִמָּךְ ("Lay down, now, a pledge for me with Yourself").**
  - The construction: two imperatives, the first lengthened with the particle of entreaty (נָא, "now, please"), and the preposition עִם with "You".
  - **Who is the surety and who the creditor?** Both are God. `[T]`
  - The second line is a passive: "who is there that will be struck (יִתָּקֵעַ) to my hand?" — the handshake of the pledge, with no one to give it. `[T]`
- **17:15–16 — the hopes go down.** "Where now is my hope? And my hope, who regards it?" (17:15, literally). The next verb is feminine plural: תֵּרַדְנָה ("they will go down", 17:16).
  - The subject is the two "hopes" of 17:15, personified as Job's companions to Sheol: "Will they go down to the bars of Sheol? Shall we together go down into the dust?"
  - NASB95 and ESV have "it". `[T]` *High.*
- **16:16 חמרמרה (ketiv).** The written form is a feminine singular; the qere and most versions read a plural ("my face is red [with weeping]"). Not load-bearing. `[T]`
- **16:9 צָרִי ("my adversary").** In context the adversary is God: the verse's subjects are "His anger", "He has gnashed", "His teeth", "My adversary glares". The NASB95 capitalises "His" throughout and leaves "My adversary" in lower case. The ambiguity is the translators', not the Hebrew's. `[T]` for the pronouns; `[I]` for the identification.

### Textual Variants

*BHS apparatus (Logos export) for chapters 16–17; Rahlfs for the Greek signs.*

#### 16:20 — "my scoffers are my friends", or a mediator?

- **BHS** marks מְלִיצַי רֵעָי ("my scoffers [are] my friends") as uncertain (ᵃ–ᵃ, with a proposed rereading glossed "mediator meus") and adds a note on אֱלוֹהַּ ("God").
- **The Greek** reads a plea (see Translations).
- **The NIV84** prints "My intercessor is my friend".
- **Category 1/2; uncertain.** The Masoretic consonants and the index's parse favour "my scoffers". Elihu's later "angel as mediator (מֵלִיץ)" (33:23) shows that the book knows the other sense.

#### 16:21 — "and between"

- **BHS** records וּבֵין ("and between") for וּבֶן ("and the son of") in a few manuscripts: "between a man and his neighbour".
- **The Greek** asterisks the line.
- *Category 2, weak.* The Masoretic "son of man" is retained in the ESV.

#### 17:1 — "extinguished"

- **BHS** records נִדְעָכוּ (from דעך, "go out") for נִזְעָכוּ (a hapax) in several manuscripts.
- *Category 2, moderate.* The variant makes Job's line the source of Bildad's "goes out" (18:5–6).

#### 17:3 — "my pledge"

- **BHS** proposes עֵרְבֹנִי ("my pledge") for the imperative עָרְבֵנִי ("be surety for me").
- The Masoretic imperative is the form shared with Isa 38:14. *The Masoretic text carries the finding.*

#### 17:6 — "a byword"; "spitting"

- **BHS** takes לִמְשֹׁל as a construct ("a byword of peoples") and glosses תֹפֶת as "an object of aversion", with an Arabic cognate.
- The English "one at whom men spit" is the traditional sense. *Uncertain lexically; not load-bearing.*

#### 17:15 — "my good"

- **The Greek** has τὰ ἀγαθά μου ("my good things"); BHS suggests וְטוֹבָתִי ("my good"). *Category 2 candidate.*
- The Hebrew repetition of תִּקְוָה ("hope") carries the finding.

#### 17:16 — "the bars of Sheol"

- **BHS** proposes בִּידִי ("with me") for בַּדֵּי ("bars, parts"); the Greek has μετ᾽ ἐμοῦ ("with me"). The NASB95's "Will it go down with me to Sheol?" follows this.
- **The ESV** has "the bars of Sheol", the Masoretic text.
- *Category 2, moderate.* Bildad's בַּדָּיו ("his limbs", 18:13) supports the Masoretic consonants as the text Bildad heard.

#### The Greek asterisks

- 16:3b; 16:8b–c; 16:21b; 17:3b–5a; 17:10b; 17:12b; 17:16b (Rahlfs).
- The Old Greek lacked about a fifth of the speech, including "son of man" (16:21b), the surety's handshake (17:3b) and the joint descent "into the dust" (17:16b).

*All Masoretic features here are as BHS prints Leningrad. No variant changes a Headline.* `[unchecked — apparatus spread]` for the setumot (Structure).

### Historical and Cultural Background

- **Sackcloth and the horn in the dust (16:15).** Mourning dress sewn on, not merely worn. "Horn" is the idiom of strength and honour (1 Sam 2:1, 10; Ps 75:5–6 [Eng 75:4–5]). Thrusting it into the dust is the opposite of "exalting the horn". `[T]` for the idiom.
- **Striking the cheek (16:10).** A public insult as well as an injury: Zedekiah struck Micaiah on the cheek (1 Kgs 22:24). In Mic 4:14 [Eng 5:1] the ruler's humiliation is a blow to the cheek. `[T]`
- **Uncovered blood (16:18).** Blood left uncovered on the ground cries for justice (Gen 4:10; Ezek 24:7–8; Isa 26:21). Covering it hides the crime (Gen 37:26). Job asks that his blood never be covered. `[T]`
- **Surety and striking hands (17:3).** A guarantor pledged himself, or his goods, for another's debt or appearance, sealed by a handshake (Prov 6:1; 17:18; 22:26). The guarantor became liable in the debtor's place (Gen 43:9; 44:32–33, where Judah offers himself in Benjamin's place). `[T]`
- **The "bars" of Sheol (17:16).** Sheol pictured as a city or prison with gates and bars: "the gates of Sheol" (Isa 38:10). Compare Jonah 2:7 [Eng 2:6]: the earth "with its bars" (בְּרִחֶיהָ, a different word), from which God brings up the prophet's life "from the pit" (מִשַּׁחַת), the pit of Job 17:14. `[T]` for the image.
- **The malicious witness (16:8).** Israel's law required more than one witness and punished a false one (Deut 19:15–19). Job's case is pictured inside that law. `[T]`

### Original Audience Reception

**Canonical audience.**
- **Section:** Ketuvim. The reader knows:
  - the Torah's law of witnesses (Deut 19);
  - the Prophets' Servant (Isa 50; 53) and Hezekiah's prayer (Isa 38);
  - the Psalter's laments (Ps 22; 35; 119).
- **What the canonical reader knows that no character knows.** There was an accuser in heaven (1:6–12; 2:1–7), and God called Job blameless twice (1:8; 2:3). Job's "my witness is in heaven" is heard against that knowledge.

**The first hearers.** Israel reading its Writings, who knew suffering that seemed to testify against them and comforters who said so. `[I]` *Low* for any specific occasion (overview).

**Surprises, shocks, comforts, disturbances.**
- **Shocking:** God pictured as a beast tearing with his teeth (16:9) and as a warrior breaching walls (16:14). These are images Israel used of its enemies and of God's judgment on Zion (Lam 2–3).
- **Surprising:**
  - that a man under God's hand can say "my witness is in heaven";
  - that he asks God to be his guarantor with God;
  - and that the speech's hope survives into the grave, personified as companions (17:16).
- **Comforting:** the appeal against God's apparent hostility goes to God, and the book does not condemn it (42:7).
- **Disturbing:** "the grave is ready for me" (17:1); "If I call to the pit, 'You are my father'" (17:14).

**What we bring that they didn't.**
- A ready-made answer: "the witness is Christ". This can stop us hearing how bold, and how unresolved, the appeal is within the book.
- And a habit of hearing "my friends scorn me" as a sermon about bad friends, rather than as the turn of a sufferer from friends to God.

**Candidate Fallen Condition Focus.**

| Field | Content |
|---|---|
| **What they felt** | Accused by their own suffering and by those who should comfort, with no advocate on earth `[T]` / `[I]` |
| **Candidate FCF (shared concern)** | **When our suffering seems to testify against us and those around us agree, we fear that heaven is empty of anyone who will speak for us — and that even God is against us.** |
| **Shared / differs** | Shared: the hostile "witness" of circumstance and the failure of comforters. Differs: we know the witness and advocate by name (1 John 2:1; Heb 7:25), and the surety (Heb 7:22) |
| **Confidence** | Anchored in the text (the two witnesses, 16:8, 19; the comforters, 16:2; the surety, 17:3); the "we" is inferred |

**Implication for the sermon.** Let the hostile witness speak (16:8) before the true one (16:19). Do not resolve the appeal "to God against God" too quickly; the book resolves it only at 38–42.

### Biblical-Theological Themes

- **Witness and advocate.** From the law's two witnesses (Deut 19:15) and heaven and earth as covenant witnesses (Deut 30:19), through the sufferer's false witnesses (Ps 27:12; 35:11) and this witness in heaven, to "the faithful witness" (Rev 1:5) and "an Advocate with the Father" (1 John 2:1). `[I]`
- **Surety.** Judah for Benjamin (Gen 43:9; 44:32–33). The forbidden surety of Proverbs (6:1; 17:18). The prayed-for surety of the righteous: Ps 119:122; Isa 38:14; Job 17:3. Then "Jesus has become the guarantee of a better covenant" (Heb 7:22). `[I]`
- **The struck cheek.** Micaiah (1 Kgs 22:24); the ruler of Israel (Mic 4:14 [Eng 5:1]); the man of Lam 3:30; the Servant (Isa 50:6); Job (16:10); Jesus ("others slapped Him", Matt 26:67; "If I have spoken wrongly, testify of the wrong; but if rightly, why do you strike Me?", John 18:23). `[T]` for the texts.
- **The blood that cries.** Abel (Gen 4:10) → Job (16:18) → "the sprinkled blood, which speaks better than the blood of Abel" (Heb 12:24). `[T]` for the texts.
- **Hope and Sheol.** Hezekiah at "the gates of Sheol" (Isa 38:10), heard and rescued (38:5, 17). Job's hopes "go down to the bars of Sheol" (17:16). Then the risen Christ holds "the keys of death and of Hades" (Rev 1:18). `[I]`

### Schnittjer Pass

N/A — Job is not in the Torah.

### Christological Reading

**Type of connection:** trajectory (the witness and advocate; the surety), typology through the servant category, and contrast.

For the servant typology, the four tests:
- **Theological category (servant):** met.
- **NT precedent of the same kind:** met. Isa 53:9 is applied to Christ in 1 Pet 2:22, and Isa 50:6 is enacted in the passion.
- **Escalation:** met.
- **Authorial pattern:** the text uses the Servant's words (16:17) but does not signal a type, so this test is not met.
- Three of four: moderate on the tests. *v1.1: low on the text* `[S: audit 3]`.

**How the speech points to Christ.**
- **The witness and advocate (16:19–21).**
  - Job's witness is "in heaven" and "argues for a man with God, as a son of man for his neighbor".
  - The New Testament names the figure: "we have an Advocate with the Father, Jesus Christ the righteous" (1 John 2:1); "He always lives to make intercession for them" (Heb 7:25).
  - `[I]` *High* for the trajectory.
  - **Keep honest:** the asterisked Greek shows that "son of man" (16:21b) was not in the Old Greek. Do not argue from the Greek title. The Hebrew בֶּן־אָדָם is the ordinary idiom for a human being (25:6; 35:8).
- **The surety (17:3).**
  - Job asks God to be his guarantor "with Yourself".
  - "Jesus has become the guarantee (ἔγγυος) of a better covenant" (Heb 7:22). ἔγγυος occurs only there in the NT (SBLGNT).
  - The guarantor who is himself God, standing for man with God, is what Job asks for and what the gospel announces. `[I]` *Moderate–high* for the trajectory. The Greek link is absent, because the Old Greek of 17:3 is different.
- **The Servant (16:10, 17).**
  - "Although there is no violence in my hands" (16:17) is the phrase of Isa 53:9. 1 Pet 2:22 applies Isa 53:9 to Christ: "who committed no sin, nor was any deceit found in His mouth".
  - The struck cheek (16:10; Isa 50:6) is fulfilled when "others slapped Him" (Matt 26:67), and at John 18:22–23.
  - `[I]` *v1.1: low as a demonstrated pattern.* Claim audit 3 rates the Servant pattern low and Isa 53:9's phrase low–moderate. **Keep it as canonical reflection.** Christians have heard Job's words with the Servant's, and 1 Pet 2:22 licenses that hearing, but Job's words are closer still to Lamentations `[S: audit 3]`.
- **The struck Christ demands a witness.**
  - When struck, Jesus answers: "If I have spoken wrongly, testify (μαρτύρησον) of the wrong; but if rightly, why do you strike Me?" (John 18:23).
  - The struck innocent appeals to testimony, as Job does (16:8, 19). `[I]` *Moderate (conceptual).*
- **The blood (16:18) → Heb 12:24.** *Moderate.*

**Contrast.**
- **Job:** he claims his prayer is pure (16:17), but in this same round he asks God to "pardon my transgression" (7:21) and speaks of "the iniquities of my youth" (13:26). He is righteous, not sinless.
- **Christ:** he "committed no sin" (1 Pet 2:22); "while being reviled, He did not revile in return … but kept entrusting Himself to Him who judges righteously" (1 Pet 2:23).
- **Job reviles God's dealings (16:9–14); Christ entrusts himself.** *High.*

**Moralism check.**
- **The "be like X" temptations:** "Be honest with God like Job", or "Don't be a sorry comforter".
- **The gospel grounding:** the witness Job could only long for, and the surety he asked God to provide, are given in Christ. Our hope does not go down to Sheol with us. It is held by the one who "always lives to make intercession".
- **Christ as hero:** not Job's boldness, but the Advocate who argues our case with God, and the Guarantor who is himself God.

**Confidence:** *high* on the advocate trajectory; *moderate–high* on the surety; *low* on the servant type (v1.1; *moderate* in v1.0).

### Difficult / Contested Verses

#### 16:9–14 — God as beast, mob leader, archer and warrior

- **Category:** doctrinal / pastoral.
- **The difficulty:** Job says God "has torn me", "gnashed at me with His teeth", "hands me over to ruffians", "splits my kidneys open", "runs at me like a warrior".
- **Rhetorical function:** lament, in the vocabulary of Lamentations' picture of God's judgement on Zion (Lam 2–3). It is the speech of a man whose experience feels like this.
- **What an honest exegesis surfaces:**
  - The book neither endorses the picture (38:2, "words without knowledge") nor condemns Job for addressing God in it (42:7).
  - The prologue tells the reader that God permitted the Accuser to act (1:12; 2:6). So the "hostility" Job experiences is real experience, not the truth about God's disposition.
- **Handling:** preach it as lament. Do not soften the images, and do not turn them into theology.

#### 16:19–21 — Who is the witness?

- **The options.**
  - **(a) God himself:** Job appeals to God against God. Ash, Delitzsch `[S]`.
  - **(b) A third, heavenly figure:** an angelic advocate (compare 33:23; 5:1).
  - **(c) Job's own cry,** personified (16:18).
- **What an honest exegesis surfaces.**
  - **(c)** does not fit "my witness is *in heaven* … my advocate *on high*".
  - **(b)** fits Elihu's later "angel as mediator", but Eliphaz has twice denied Job any help from "the holy ones" (5:1; 15:15).
  - **(a)** is supported by 17:3, where Job asks God to stand surety for him "with Yourself", and by 16:20, where Job's tears go "to God" in the same breath.
  - The text holds the tension: God is the one appealed against (16:9–14) and the one appealed to (16:20; 17:3).
- **Handling:** let the tension stand within Job. The New Testament resolves it in the Son, who is God and "with the Father" (1 John 2:1).

#### 16:20 — "My friends are my scoffers"

- **Category:** textual / lexical. See Textual Variants.
- **Handling:** preach the ESV's line. Do not build on "my intercessor is my friend" (NIV84), which rests on a reading the Hebrew allows but does not favour.

#### 17:13–16 — Sheol as home; the pit as father

- **Category:** pastoral (death-wish) / apologetic (no afterlife hope?).
- **What an honest exegesis surfaces.**
  - Job does not wish to die here. He states that the grave is all that is left, and asks where hope can go: "Shall we together go down into the dust?"
  - The question is answered within the book by 19:25–27, and beyond it by the canon.
- **Handling:** do not make 17:16 a denial of resurrection, and do not make it a hidden affirmation. It is a question. If anyone in the room is in that place, the sermon should say plainly that help is available.

#### 16:17 — "My prayer is pure"

- **Category:** doctrinal. Is Job claiming sinlessness?
- **No.** "No violence in my hands" answers Eliphaz's charges (15:4–6, 20–35). "My prayer is pure" means sincere, not hypocritical (compare 15:34, the "godless"). Elsewhere Job owns sins (7:21; 13:26).
- **Handling:** do not preach 16:17 as perfectionism. It is a plea of not guilty to the specific charge.

## Convergent Findings

- **The two witnesses** (10:17 → 16:8 → 16:19; Deut 19:16 at 16:8; יכח 9:33 → 15:3 → 16:21).
  - *Surfaced by:* Vocabulary, Repetition, Move 4, Tool 11, Christological Reading.
  - *High on the words; moderate–high on the design.*
- **Job answers Eliphaz's speech (chapter 15) in its own words, and Bildad answers Job's (chapter 18) in his** (Headline 2).
  - *Surfaced by:* Move 4, Vocabulary, Repetition.
  - *High on the exclusive links; moderate–high on the pattern.*
- **Lamentations 2–3 as a live source:**
  - target + kidneys and cheek + reproach (both exclusive);
  - the reduplicated חמר ("be in ferment"; Lam 1:20; 2:11);
  - gnashing; the root "desolate"; the people's mockery.
  - *Surfaced by:* Tool 11, Vocabulary, Translations.
  - *v1.1: high.* Lam 2:10–17 is the main source, with Lam 3:12–13, 30, and all three auditors of claim audit 3 reached it `[S: audit 3]`.
- **The Servant sequence, adding Isa 50:6 and 53:9** to audit 2's Isa 50:8–9.
  - *Surfaced by:* Tool 11, Christological Reading.
  - *v1.1: low–moderate on Isa 53:9's phrase; low on the pattern* `[S: audit 3]`.
- **The surety petition, shared only with Isa 38:14 and Ps 119:122.**
  - *Surfaced by:* Vocabulary (morphology), Tool 11, Biblical Theology.
  - *v1.1: moderate on the petition; low–moderate on the Isaiah 38 pattern* `[S: audit 3]`.
- **Hope going down into the dust:** קוה + תִּקְוָה ×2 at 17:13–15; the feminine plural "they will go down" (17:16); 14:19 → 17:15 → 19:10.
  - *Surfaced by:* Repetition, Original Languages, Move 4.
  - *High.*
- **Both ends of the book:**
  - 3:5, 9 → 16:16;
  - 29:23 → 16:10;
  - 16:13 → 19:27;
  - 17:14 → 42:11 (with 1:4).
  - *Surfaced by:* Move 4, Repetition.
  - *High on the words; moderate–high on the design.*
- **The appeal to God against God:** 16:20 ("to God"), 16:21 ("with God"), 17:3 ("with Yourself").
  - *Surfaced by:* Original Languages, Structure (the address test), Difficult Verses.
  - *High on the words; the identification of the witness moderate.*

---

## Preaching Pitfalls

### Pitfall: "The witness is Jesus" in the first five minutes

- **What it looks like:** reading 16:19 straight as a prophecy of Christ.
- **Why it's wrong:**
  - Within the book the witness is unresolved, and the boldness of the appeal — to God against God (17:3) — is lost if it is resolved too soon.
  - The Greek "son of man" (16:21b) is not Old Greek.
- **The corrective:** let 16:8 (the hostile witness) and 16:19 (the true one) stand in tension. Bring 1 John 2:1 and Heb 7:22 as the canon's answer to a longing Job could not resolve.

### Pitfall: Softening the God of 16:9–14 — or adopting him

- **What it looks like:** either "Job didn't really mean God", or a sermon on God's hostility.
- **Why it's wrong:**
  - The subjects are God ("His anger", "God hands me over", 16:9, 11).
  - The book treats the speech as lament addressed to God (42:7), "without knowledge" in its content (38:2).
- **The corrective:** name it as lament, in the vocabulary of Lamentations. Show where it goes: "my eye weeps to God" (16:20).

### Pitfall: A sermon on bad friends

- **What it looks like:** 16:2–5 and 17:10 as the main point: "don't be a sorry comforter".
- **Why it's wrong:** the speech's movement is from the friends to God. The application to comforters is real, but secondary.
- **The corrective:** use 16:4 ("if I were in your place") as a word to comforters. Keep the sermon's weight on the witness and the surety.

### Pitfall: "My prayer is pure" as perfectionism

- **What it looks like:** using 16:17 for a claim of sinlessness, or to rebuke it.
- **Why it's wrong:** the verse answers specific charges (chapter 15). Job owns sins elsewhere (7:21; 13:26).
- **The corrective:** read it as a plea of not guilty.

### Pitfall: Reading 17:13–16 as despair only, or as a creed

- **What it looks like:** either "Job has given up", or "Job believes in resurrection".
- **Why it's wrong:** 17:16 is a question, and its subject is Job's hopes, personified as companions to Sheol. The speech has already placed a witness in heaven (16:19).
- **The corrective:** let the question stand. It is answered in 19:25–27 and in Christ, who has "the keys of death and of Hades" (Rev 1:18).

---

## Open Questions / Uncertainties

**Open.**

1. **The identity of the witness (16:19–21).** God, a heavenly advocate, or neither? The text favours God appealed to against God (17:3; 16:20). **Logos round 4 (5 Oct):** Delitzsch takes the witness to be God himself — "Job appeals from God to God … *nemo contra Deum, nisi Deus ipse*" — and confirms Gen 4:10, Ezek 24:7–8 and Isa 26:21 at 16:18, שָׂהֵד as an Aramaism (Greek συνίστωρ), and 15:20 at 16:22. Each was reached here first. `[S: Delitzsch]` **Answered for the house reading; option (b), an angelic advocate, remains a minority view to report.**
2. **16:20 מְלִיצַי** — "my scoffers" or "my mediator(s)"? **Closed (Logos rounds 4–5, 5 Oct): "my scoffers".** HALOT's entry for the noun מֵלִיץ ("interpreter, envoy, spokesman; interceding angel") lists Gen 42:23; 2 Chr 32:31; Isa 43:27; Job 33:23 as every biblical reference, and **not** Job 16:20. Its entry for ליץ puts 16:20, queried, under the hiphil "scoff, deride". Delitzsch reads "my mockers" (Ps 119:51); the index parses a participle "my scoffers". BHS's conjecture ("my mediator, my friend") and the NIV84 ("My intercessor is my friend") take the minority reading. `[S: HALOT; Delitzsch]` **Pulpit:** the ESV carries the majority reading; if preaching from the NIV84, say that it follows a conjecture.
3. **17:3 and Isa 38:14** — the identical petition. Is it designed, or a shared formula of prayer (with Ps 119:122)? **Audited (claim audit 3):** the form is moderate, a natural prayer form beside Proverbs' surety idiom; the Hezekiah frame is low–moderate `[S: audit 3]`.
4. **Lamentations 2–3 as a source** — direction of dependence, and whether the contacts reach beyond 16:7–16 and 19:8. **Audited (claim audit 3):** the main source at Job 16 is Lam 2:10–17 (high); Lam 3:1–9 at 19:6–20 is moderate–high; the direction stays open `[S: audit 3]`.
5. **The Bildad pattern (16–17 → 18)** — a design, or the natural reuse of a shared vocabulary of the wicked's end? A chance baseline across the second cycle is needed. **Answered:** the speech-pair baseline (19 dig) ranks 16–17 → 18 99th of 120 pairs. It is a pointed reply, not lexical saturation. Queue #59 is closed with claim audit 3.
6. **17:6 תֹפֶת** and **17:16 בַּדֵּי** — **both closed (Logos rounds 4–5, 5 Oct).** תֹּפֶת: HALOT "spittle" (a hapax, from an onomatopoeic root "spit"), so "one at whom men spit". בַּדֵּי: HALOT and BHS both offer conjectures towards the Greek's μετ᾽ ἐμοῦ ("with me"): HALOT reads הַעִמָּדִי, and BHS *l frt* בִּידִי. **Keep the Masoretic text.** The construct plural בַּדֵּי occurs in Job only at 17:16 and 18:13, where Bildad answers it ("the parts of his skin"), and elsewhere only of the ark's poles (Exod 25:13; 27:6; 37:4) (WLC). The echo in 18:13 is evidence that Bildad heard בַּדֵּי. Read "the bars" (or "parts, recesses") of Sheol. `[T]` for the forms; `[S: HALOT; BHS]` for the conjectures. **Pulpit:** the ESV keeps the Hebrew ("the bars of Sheol"); the NASB95 follows the Greek ("with me to Sheol"), as it does at 14:3.
7. **The setumot of the second cycle** — **closed (5 Oct).** The BHS export in the folder has setumot after 15:35, 17:16, 18:21 and 21:34, a petuḥah after 20:29, and **no marker after 19:29**, which Patrick confirmed on screen. The WLC transcription has a setumah after 19:29, so the WLC and BHS differ there. Across the book BHS has 26 petuḥot (identical to the WLC) and 12 setumot (the WLC has 13). Spread across other manuscripts stays `[unchecked — apparatus spread]`.
8. **The Greek asterisks** — the Old Greek lacked about a fifth of the speech. The Göttingen apparatus (not owned) would show more.

**Added by Logos round 4 (5 Oct 2026), corpus-checked.**

- **1 Chr 12:18 → 16:17, 21** *(moderate–high on the words; direction open).* David at Ziklag: "if to betray me to my adversaries, although there is no violence in my hands (בְּלֹא חָמָס בְּכַפַּי), may the God of our fathers see and rebuke (וְיוֹכַח)". Job: "although there is no violence in my hands (עַל לֹא־חָמָס בְּכַפָּי)" (16:17) … "that he may argue (וְיוֹכַח)" (16:21). חָמָס + כַּף with the negative occurs only at 1 Chr 12:18 and Job 16:17 (Isa 59:6 and Jonah 3:8 are positive); חָמָס + יכח in one verse only at 1 Chr 12:18; the exact form וְיוֹכַח only at 1 Chr 12:18 and Job 16:21 (WLC lemma index; חֶסֶד control passed). The oath of innocence with the call on God to judge. Chronicles closes the Ketuvim, so it is read forward from Job. `[T]` for the data. **v1.1: moderate.** It is a shared oath-of-innocence formula: Gen 31:42 stands behind 1 Chr 12:18, and Isa 53:9 is as close to 16:17. Direct dependence is not shown `[S: audit 3]`.
- **"His friend" (רֵעֵהוּ): 6:14 → 12:4 → 16:21 → 42:10** *(moderate–high).* The singular "his friend" (7453 with the 3ms suffix) in Job: kindness "from his friend" owed to the despairing (6:14); "a laughingstock to his friend" (12:4); the witness arguing "for a son of man with his friend" (16:21); and "when he prayed for his friend(s)" (42:10) (WLC; 39:8 מִרְעֵהוּ, "his pasture", excluded). Lange (on 42:7) says God "fulfils literally the wish uttered by Job (ch. 16:21)". The irony runs both ways: Job longs for someone to argue his case against his friend; at the end he prays for his friend. `[T]` for the chain; `[S: Lange]` for the fulfilment. *Echo Table candidate for the overview upgrade.*

**Added by Logos round 6 (7 Oct 2026), corpus-checked** (`claude/job-logos-answers-round-6-assessment.md`).

- **Lamentations — history of interpretation.** Delitzsch compares 16:13 (the gall poured out) with Lam 2:11, and 16:16 (the reduplicated "in ferment") with Lam 1:20 and 2:11. He also reads 16:15 עֹלַלְתִּי ("I have dealt with, defiled") by Lam 3:51 עוֹלְלָה. Andersen and Konkel–Longman draw no comparison. `[S: Delitzsch]`
  - The two rarest Lam 2 items therefore have a major commentator behind them. The rating stays **high**.
  - The WLC files 16:15 under a different homograph (5953 d) from Lamentations' poel "deal severely" (5953 a: Lam 1:22; 2:20; 3:51). If Delitzsch is right, it is a fourth Lamentations item in 16:13–16. **Queue #91, possible–moderate.**
- **17:3.** Delitzsch calls עָרְבֵנִי "a word of entreaty which occurs also in Hezekiah's psalm, Isa 38:14, and Ps 119:122". He reads the hand-striking by Prov 6:1, makes עִמָּךְ ("with Yourself") the point, and cites Heb 7:22 (ἔγγυος). This is the audit's verdict exactly: a shared prayer word, moderate, with Proverbs' idiom beside it. It also supports the God-against-God reading. `[S: Delitzsch]`
- **16:8 כַּחַשׁ ("my leanness").** HALOT gives 1. "leanness" at 16:8, alternatively 2. "lie, deception", with the Greek, Aquila and the Vulgate. In its five other verses the word means "lie" (Hos 7:3; 10:13; 12:1; Nah 3:1; Ps 59:13; WLC). The Greek line "and my lie (τὸ ψεῦδός μου) rose up in me" is asterisked in Rahlfs, so it is the Hexaplaric supplement. Delitzsch reads "a wasting away". Job's wasted body rises and testifies against him as a *lying* witness — the witness law's case. **The forensic reading of 16:8 rises to moderate–high**; Deut 19:16 itself stays moderate `[S: HALOT]`.

**Closed in this dig.**

- **Is עֵד ("witness") found elsewhere in Job?** Only 10:17, 16:8 and 16:19 (lemma; the חֶסֶד control passed).
- **Is עַל לֹא־חָמָס ("although no violence") found outside Job 16:17?** Only Isa 53:9 (phrase search, skeletal pass included).
- **Are "target" and "kidneys" together anywhere else?** Only Lam 3:12–13 (lemma; target sense isolated).
- **Are "cheek" and "reproach" together anywhere else?** Only Lam 3:30.
- **Is the imperative of ערב ("be surety") found elsewhere?** Only Ps 119:122 and Isa 38:14 (morphology).
- **Does Bildad reuse נתק ("tear away")?** Yes; 17:11 and 18:14 are its only verses in Job.
- **Is the "witness who rises and answers" formula found elsewhere?** Only Deut 19:16.
- **Is לוּ יֵשׁ ("if there were") found in Job?** Yes, at 16:4. The WLC index also files 9:33 under לוּ ("if only"), so the "would that" reading of 9:33 is the index's own lemma.
- **Is the reduplicated form of חמר ("be in ferment") found elsewhere?** Only Lam 1:20 and 2:11.

---

## Book-Overview Tensions

*Surfaced, not resolved. The overview is v0.1.1 (Draft); the interim upgrade (v0.2) follows Sermon 4's unit dig.*

1. **Intertextual Map — Lam 3 row.**
   - Add the two exclusive pairs (16:12–13 / Lam 3:12–13; 16:10 / Lam 3:30), the reduplicated חמר (16:16; Lam 1:20; 2:11), and gnashing (Lam 2:16).
   - Raise the row from *moderate* to *moderate–high*. The direction stays open.
   - **v1.1:** raise it to **high** and re-key it to **Lam 2:10–17** at 16:4–16, with Lam 3:12–13, 30 `[S: audit 3]`.
2. **Intertextual Map — new rows:**
   - **Isa 53:9 → 16:17**, high on the phrase (*v1.1: low–moderate*);
   - **Isa 38:14 (with Ps 119:122) → 17:3**, high on the petition, moderate on the pattern (*v1.1: moderate; low–moderate*);
   - **Deut 19:15–19 → 16:8**, moderate–high (*v1.1: moderate*);
   - **Deut 4:26; 30:19; 31:28 → 16:18–19**, moderate.
3. **Christological Trajectory.**
   - **The mediator sequence.** Add **17:3 (the surety) → Heb 7:22** to 9:33 → 16:19–21 → 19:25 → 33:23.
   - **The type section.** It cites Isa 50:6 for 16:10. Add Isa 53:9 for 16:17, with 1 Pet 2:22. *v1.1:* present the Servant as canonical reflection (low as a pattern), and give Lam 3:30 as the textual partner of 16:10 `[S: audit 3]`.
   - **The keep-honest note.** Add that "son of man" at 16:21b is asterisked in the Greek.
4. **Text and Versions.**
   - **9:33:** the WLC index files the word under לוּ ("if only"), and 16:4 has לוּ יֵשׁ.
   - **The Greek asterisks of 16–17.**
   - **17:16:** NASB95 follows the "with me" proposal, ESV the Masoretic "bars".
5. **Echo Table — additions:**
   - 3:5, 9 → 16:16 (eyelids);
   - 29:23 → 16:10 (gaping mouths);
   - 16:13 → 19:27 (kidneys);
   - 16:9 → 19:11 (adversary; anger);
   - 17:14 → 42:11 with 1:4 (sisters);
   - 16:20; 17:14 → 33:18–30 (mediator; pit);
   - 16:8 → 22:16 (קמט);
   - 4:7 → 17:8 (innocent and upright);
   - 10:13 → 17:4 (concealed in the heart).
6. **Table B (Job quotes itself, and is quoted) — additions:**
   - 15:2, 3, 11, 14–15, 20, 25–26 → 16:2, 3, 14, 17, 19, 21, 22;
   - 16:9; 17:1, 8, 11, 12, 16 → 18:4, 5–6, 13, 14, 18, 20.
7. **Structural Arc Map.** Record that in BHS the second cycle's speeches end with setumot (Zophar's with a petuḥah; Job's at 19:29 with none, though the WLC has a setumah there), where round one's ended with petuḥot `[unchecked — apparatus spread]`.
8. **Preaching Units.** The overview's unit 15:1–17:16 joins Eliphaz's speech to Job's reply. This dig confirms that pairing: Job's reply cannot be understood without chapter 15. It adds that chapter 18 is built from it, so the Sermon 4 unit (15:1–21:34) is the right frame.
9. **Confirmations.** The overview's Christological trajectory item 16:19–21, its type item on Isa 50:6 at 16:10, its Lam 3 row and its Echo Table row 16:2 → 42:11 all stand. The sweep's Unit 8 findings were re-derived independently and agree: Isa 53:9, the 9:33 / 10:17 links, the Gen 43:9 surety, 15:6 → 9:20 and 15:16 → 34:7.

---

## What Changed in v1.1

Patched on 7 October 2026 from `dig-deeper-job-claim-audit-3.md`. Nothing else in the report was altered. The structure, the address test, the internal echoes, the grammar, the textual notes and the pulpit notes all stand.

| Location | v1.0 | v1.1 |
|---|---|---|
| Headline 1 | Deut 19:16 at 16:8, moderate–high | **Moderate.** A legal idiom shared with Ps 27:12 and 35:11; Rahlfs asterisks 16:8b. The three עֵד verses and the umpire's verb stand |
| Headline 2 | Bildad's reply as a pattern, moderate–high | **A pointed reply, moderate.** Not lexical design (speech-pair baseline; #59 closed) |
| Headline 3 | Lamentations 3 and the Servant | **Lamentations 2:10–17 is the main source (high)**, with Lam 3:12–13, 30. It was found by all three auditors and beats every Job-passage null. The Servant pattern is **low**; Isa 53:9's phrase is low–moderate |
| Headline 4 | The surety petition high; the Hezekiah pattern moderate | **Petition moderate; frame low–moderate.** Proverbs' surety idiom sits beside it; Job 17:16 has "bars", not "gates" |
| Tool 11 | Isa 53:9 high; Lam 2–3 moderate–high; Isa 38 high / moderate; Deut 19 moderate–high; Isa 26:21 moderate–high; Ps 22:8 moderate | Isa 53:9 **low–moderate**; Lam 2–3 **high** (re-keyed to Lam 2); Isa 38 **moderate / low–moderate**; Deut 19 **moderate**; Isa 26 as the answer **low–moderate**; Ps 22:8 **low** |
| Christological Reading | Servant type moderate | **Low as a pattern; keep as canonical reflection.** The witness, advocate and surety trajectories stand |
| Convergent Findings | Lamentations moderate–high; Servant moderate; surety high | Lamentations **high**; Servant **low**; surety **moderate** |
| Open Questions 3, 4, 5; 1 Chr 12:18 | queued | answered by the audit; 1 Chr 12:18 **moderate** (shared formula) |
| Book-Overview Tensions 1–3 | as proposed | revised to match |

**Ratings that rested on a window rank** are not used. This dig's Isaiah 38 rank (29th of 887) was already marked non-distinctive. The Lam 2 rank is the one rank in the round that beats the Job-passage null.

---

## Text-First Declaration

**Secondary sources present in context:**
- the book overview (v0.1.1);
- the sweep's Unit 8;
- the Unit 1 report;
- the Job 3 report;
- the 4:1–14:22 consolidation report and its solo digs;
- claim audit 2;
- the Sermon 3 backbone;
- the Logos round 2 assessment (Ash, the study Bibles and Keil–Delitzsch on 16:19; HALOT and BDB on שָׂהֵד);
- **v1.1:** claim audit 3, whose verdicts were applied after the run.

All were produced in this project or are Patrick's library returns. No commentary was opened in this run.

**The `[S]` items:**
- HALOT and BDB on שָׂהֵד;
- Ash on 16:18 and 16:19;
- the "God against God" option attributed to Delitzsch (via the Logos assessment);
- the composition date (not stated).

**Tools worked before secondary sources consulted:** Confirmed.
- The BHS text and apparatus, Swete and Rahlfs were read first.
- The structure, the address test, the repetitions and the candidate intertexts were derived and verified in the WLC (`chk.py` and follow-ups) before the sweep's Unit 8 and the overview's 16–17 rows were re-read.
- **The finds new to this run:**
  - **Witnesses and law:** the three עֵד verses as a sequence; Deut 19:16 at 16:8 (exclusive); Deut 4:26 / 30:19 / 31:28 at 16:18–19; Ps 35:11.
  - **Lamentations and Isaiah:** the Lamentations exclusives (16:12–13; 16:10) and the reduplicated חמר; Isa 38:14 and Ps 119:122 (the ערב imperative); Prov 6:1; 17:18.
  - **Chapter 15:** the answers to 15:2, 11, 14–15, 20 and 25–26 (the sweep had 15:35 → 16:2 and 15:6 → 9:20).
  - **Chapter 18:** Bildad's reuse — טרף + אַף (16:9 → 18:4); נתק (17:11 → 18:14); בַּד (17:16 → 18:13); שׁמם (17:8 → 18:20); the 17:1 variant → 18:5–6.
  - **Elsewhere in Job:** 3:9 → 16:16; 3:26 → 16:12; 29:23 → 16:10; 16:13 → 19:27; 16:9 → 19:11; 17:14 → 42:11 with 1:4; 16:20 and 17:14 → 33:18–30; 16:8 → 22:16; 4:7 → 17:8; 10:13 → 17:4; 11:20 → 17:5; 13:9 → 17:2.
  - **Grammar and versions:** the WLC lemma of 9:33 and 16:4's לוּ יֵשׁ; the feminine plural of 17:16; the Greek asterisks of 16–17 and παρακλήτωρ at 16:2.
- **Re-derived independently, in agreement:** the sweep's findings (Isa 53:9; 9:33 / 10:17 → 16:19–21; 15:35 → 16:2; the surety and Gen 43:9; 15:16 → 34:7; 16:15 → 42:14) and the overview's (the Lam 3 row; Isa 50:6 at 16:10; 16:2 → 42:11; the mediator sequence).

**Passage text:** Verified.
- The Hebrew is BHS, from the Logos export, not retyped.
- NASB95, ESV and NIV84 are from the Logos exports, and every quotation was checked against them. This includes the parallels in Isaiah, Lamentations, Deuteronomy, Genesis, Psalms and Proverbs, and the New Testament verses (1 John 2:1; Heb 7:22, 25; 12:24; Rev 1:5, 18; Matt 26:67; John 18:23; 1 Pet 2:22–23).
- Swete and Rahlfs were read for both chapters. SBLGNT was used for ἔγγυος, παράκλητος and μαρτύρησον.
- Mic 4:14 [Eng 5:1] and Jonah 2:7 are given in paraphrase, not quoted, because the Twelve's English exports were not staged this run.

**Warrant counts** (tags in the report body, excluding the legend): `[T]` 71 · `[I]` 42 · `[S]` 5 (including `[S: HALOT; BDB]`) · `[S: audit]` 4 · `[S: audit 3]` 26 (v1.1). No Headline rests on an `[S]` item alone.

**Phase 10.5 gate.**
- **Controls.** Every "only" and every chain was rerun by lemma with the חֶסֶד positive control passing (6:14; 10:12; 37:13).
- **Lemma splits** were met and allowed for: הלך (1980 / 3212), מַטָּרָה (target / guard), שׁמם (8074 / 8076), חמר (2560 a / c). Each "only" touching them was confirmed by reading the hits.
- **Corrections made at the gate:**
  - Lam 3:12 spelled כַּמַּטָּרָא;
  - Isa 38:18's verb distinguished (שׂבר, not קוה);
  - the "eye" count restated (five, plus "eyelids");
  - 16:12's reduplicated verbs restated (two, not three);
  - 16:21's verb restated as imperfect, not jussive — *withdrawn 5 Oct (Logos round 4): the form is the short, jussive form; see Original Language Observations*;
  - the 10:21 positive control, which failed on lemma 1980 alone, restated with 3212.
- **Apparatus features** (petuḥot, setumot, the ketiv) name Leningrad as BHS prints it. The setumot remain `[unchecked — apparatus spread]`.
