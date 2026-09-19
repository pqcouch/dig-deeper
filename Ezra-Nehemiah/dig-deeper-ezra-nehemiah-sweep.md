# Dig Deeper: Ezra–Nehemiah — Multi-Passage Sweep

**Primary texts:** WLC Hebrew and Aramaic (`_texts/hebrew-wlc/03-Ketuvim/10a-Ezra.txt`, `10b-Nehemiah.txt`), read complete, cover to cover, before any English; with the WLC lemma index for every count. Also opened: Swete LXX (`greek-lxx-swete/15-1-Esdras.txt`, `16-2-Esdras-Ezra.txt`, `17-Nehemiah.txt`); the Logos exports of Rahlfs-Hanhart (carrying both Esdras A and Esdras B) and of the BHS apparatus, as citation of record.
**Study text:** NASB95 (Logos export, parsed verse by verse — 686 verses)
**Second English witness:** ESV (Logos export, parsed — 664 verses recovered; the export's last line is truncated)
**Pulpit text:** None — no sermon is in view, so none has been declared and none has been invented. Where the NASB95 and the ESV part company on something a finding rests on, the note is given anyway, so that it is ready when an engagement is declared.
**Date:** 19 September 2026
**Mode:** Fresh Exegesis, Multi-Passage Sweep (19 units)
**Book-overview context:** In conversation — `Ezra-Nehemiah/book-overview-ezra-nehemiah.md` (v1.1, Draft, 19 September 2026, clean-room build). Front-loaded at Phase 0.5; reconciled at Phase 5.5.
**Series context:** Whole-book sweep through the overview's nineteen preaching units, run to test the Draft overview and to decide which units need solo digs.

Warrant tags: `[T]` derivable from the text on the page · `[I]` a reasonable inference from the text · `[S]` supplied by a secondary source and held provisionally.

> **Versification.** The corpus uses Hebrew versification; the NASB95 and ESV use the other, and Nehemiah is where it bites. **MT Neh 3:33–38 = Eng 4:1–6; MT Neh 4:1–17 = Eng 4:7–23; MT Neh 10:1–40 = Eng 9:38 + 10:1–39.** Every count below was made on the Hebrew. **References are given in English numbering only where the unit table says so; everywhere else they are MT**, with the English in brackets where it differs and the difference matters. Apparatus entries are cited by their own (Hebrew) numbers.

> **Sweep-format note.** A great deal here is constant across all nineteen units: the author's purpose, the genre, the canonical position, the two languages, the two Greek forms, the historical background, the original audience, and the book's verified vocabulary map. That material is worked once in **Book-Level Foundations** and assumed under every unit. Each unit then does the work that belongs to it: the Positional Necessity Check, structure, vocabulary, translations, repetition, and the allusion work with Move 4, followed by the unit's own difficulties. **The passage text is not reprinted in full for each unit** — 685 verses in three languages. The Hebrew of each unit's load-bearing verses is quoted with the NASB95; the full text is in the corpus. Depth is proportional across the session. **A ⭐ unit needs a full solo dig before the pulpit.**

> **Synthetic claims.** A claim assembled across passages is marked **(synthetic)**. For every such claim in this report, **each constituent reference was checked by lemma against the WLC with `_texts/tools/find.py`**, so the word-level chains are verified; several were additionally gated with `find.py verify`, which exits non-zero if any reference fails. Claims about *design* built on those chains are held at **moderate** unless stated otherwise, pending a claim audit.

---

## Units Worked

References follow the **English** versification, as the overview's table does; the MT range is given where it differs.

| # | Verses | Working title | Weight |
|---|---|---|---|
| 1 | Ezra 1:1–11 | The king's decree and the vessels that came home | ⭐ |
| 2 | Ezra 2:1–70 | Counted and named | Standard |
| 3 | Ezra 3:1–13 | The altar before the foundation | ⭐ |
| 4 | Ezra 4:1–24 | "Let us build with you" | ⭐ |
| 5 | Ezra 5:1–6:22 | The search of the archive | Standard |
| 6 | Ezra 7:1–28 | The scribe who set his heart | ⭐ |
| 7 | Ezra 8:1–36 | The fast at the river Ahava | Standard |
| 8 | Ezra 9:1–10:44 | The holy seed | ⭐ |
| 9 | Neh 1:1–2:20 | A cupbearer's sad face | ⭐ |
| 10 | Neh 3:1–4:23 (MT 3:1–38; 4:1–17) | Builders, and the men who laughed | Standard |
| 11 | Neh 5:1–19 | The debt that had to be cancelled | ⭐ |
| 12 | Neh 6:1–7:5 | Fifty-two days | Standard |
| 13 | Neh 7:6–73 (MT 7:6–72) | The book he found | Standard |
| 14 | Neh 8:1–18 | The book opened | ⭐ |
| 15 | Neh 9:1–37 | The longest prayer in the Bible | ⭐ |
| 16 | Neh 9:38–10:39 (MT 10:1–40) | Signed and sealed | Standard |
| 17 | Neh 11:1–12:26 | Filling the holy city | Standard |
| 18 | Neh 12:27–47 | Two choirs on the wall | Standard |
| 19 | Neh 13:1–31 | Remember me | ⭐ |

---

## Headline Findings (sweep level)

Five claims from the whole sweep. Each emerged under several tools, and every word-level element was verified by lemma against the WLC before it was written.

### 1. The covenant clause of Neh 10 is broken at Neh 13 in the covenant's own words — and no English version shows it. `[T]` (synthetic)

The overview's covenant table already pairs Neh 10:38–40 with Neh 13:10–11. What the corpus adds is that the pairing is **verbal, not merely thematic**, and that it runs on the root the book has spent nine chapters loading.

- **The clause.** Neh 10:40 (Eng 10:39) ends וְלֹא נַעֲזֹב אֶת־בֵּית אֱלֹהֵינוּ ("and we will not forsake the house of our God").
- **The breach.** Neh 13:11 asks מַדּוּעַ נֶעֱזַב בֵּית־הָאֱלֹהִים ("Why is the house of God forsaken?"). Same root, עזב, same object, בֵּית הָאֱלֹהִים. Nehemiah is not describing a failure; he is quoting the signature back.
- **The root's loading.** עזב stands in **twelve verses** of the book (WLC, by lemma): Ezra 8:22; 9:9; 9:10; Neh 3:8; 3:34; 5:10; 9:17; 9:19; 9:28; 9:31; 10:40; 13:11. **Four of those twelve are in the great prayer of Neh 9, and in all four the subject is God** — "you did not forsake them" (9:17, 9:19, 9:31) and, once, "you forsook them into the hand of their enemies" (9:28). The people sign a promise not to do the thing God has three times been praised for not doing. Three chapters later they have done it.
- **The Greek carries it.** Esdras B renders the root with ἐγκαταλείπω at **ten of the twelve**, including both ends of the pair — οὐκ ἐγκαταλείψομεν τὸν οἶκον τοῦ θεοῦ ἡμῶν (10:40) and Διὰ τί ἐγκατελείφθη ὁ οἶκος τοῦ θεοῦ; (13:11). The two it does not carry (Neh 3:8, 3:34) are the two whose Hebrew sense is itself disputed. `[T — Rahlfs-Hanhart export, checked]`
- **And no English version shows it.** NASB95: "we will not **neglect** the house of our God" / "Why is the house of God **forsaken**?" ESV: "We will not **neglect** the house" / "Why is the house of God **forsaken**?" **Both break the link in the same place and the same way.** A congregation hearing either version hears a complaint; the Hebrew and the Greek both have a prosecution.
- *Surfaced by:* Repetition, Vocabulary, Move 4 (units 16 and 19), Translations, Structure. *High confidence on the words and on the versions; high on the design, because the object is repeated as well as the verb.*

### 2. Ezra tears out his own hair; Nehemiah tears out theirs — and the root stands only twice in the book. `[T]`

- **The two verses.** Ezra 9:3 — וָאֶמְרְטָה מִשְּׂעַר רֹאשִׁי וּזְקָנִי ("and I pulled out some of the hair of my head and my beard"). Neh 13:25 — וָאַכֶּה מֵהֶם אֲנָשִׁים וָאֶמְרְטֵם ("and I struck some of them and pulled out their hair").
- **The count.** מרט occurs in **exactly two verses of Ezra–Nehemiah**, and in **eleven verses of the whole Hebrew Bible** (12 occurrences): Lev 13:40, 41; 1 Kgs 7:45; Isa 50:6; Ezek 21:14, 15, 16, 33; 29:18; Ezra 9:3; Neh 13:25. `[T — verified by lemma across all 23,213 WLC verses; gated with find.py verify, exit 0]`
- **What it shows.** The book gives the same sin — foreign marriage — to two men, and lets the same rare gesture divide them. Ezra's grief is self-directed and immobilising; he sits down מְשׁוֹמֵם ("appalled") until the evening offering. Nehemiah's is outward and immediate. The text does not adjudicate between them, and a sermon that prefers one temperament to the other is choosing where the book declines to.
- **And the Christological pointer is in the word's own company.** The eleven verses include **Isa 50:6** — וּלְחָיַי לְמֹרְטִים ("and my cheeks to those who pluck out the beard"), the third Servant Song. In the whole Hebrew Bible, the only other person who has his beard plucked in a scene of covenant grief is the Servant, and he is the one who **receives** the gesture rather than giving it. This is a trajectory, not a prophecy, and it should be preached as one — but it is the text's own vocabulary, not an imported connection.
- **The Greek cannot carry it.** Rahlfs renders Ezra 9:3 with ἔτιλλον and Neh 13:25 with ἐμαδάρωσα — **two different verbs for one Hebrew root**, so the doublet is invisible in Greek. Swete (Vaticanus) omits the Neh 13:25 clause altogether. **Both English versions, by contrast, keep "pulled … hair" in both places**, so this one a congregation *can* see.
- *Surfaced by:* Vocabulary, Repetition, Move 4 (units 8 and 19), Christological Reading, Translations. *High confidence on the count and the versions; moderate-to-high on the Isa 50:6 trajectory.*

### 3. The book runs on hands — strengthened, weakened, and one hand that is good — and the vocabulary is verifiable and vast. `[T]` (synthetic)

- **חזק ("to be strong, to strengthen, to repair") stands in 39 verses of the book, 47 occurrences: 5 verses in Ezra, 34 in Nehemiah.** `[T — lemma, WLC]` Twenty-eight of Nehemiah's are the relentless הֶחֱזִיק ("repaired") of the builders' register in ch. 3.
- **Its opposite, רפה ("to let drop, to slacken"), stands in exactly three verses: Ezra 4:4; Neh 6:3, 6:9.** `[T]` The people of the land are מְרַפִּים יְדֵי עַם־יְהוּדָה ("weakening the hands of the people of Judah", Ezra 4:4); the enemies' whole stated aim is יִרְפּוּ יְדֵיהֶם מִן־הַמְּלָאכָה ("their hands will drop from the work", Neh 6:9).
- **The two poles meet in one verse.** Neh 6:9 puts the enemies' intention (hands drop) and Nehemiah's prayer in the same breath: וְעַתָּה חַזֵּק אֶת־יָדָי ("but now, strengthen my hands"). One verse, both roots.
- **And the hand that settles it is God's.** The phrase כְּיַד־אֱלֹהָיו הַטּוֹבָה עָלָיו and its variants stand at **Ezra 7:9; 8:18; Neh 2:8; 2:18** with the adjective, and the same idea without it at Ezra 7:6, 7:28, 8:22, 8:31 — eight places, four of them in the overview already. Against them stands **Ezra 9:2**: וְיַד הַשָּׂרִים וְהַסְּגָנִים הָיְתָה בַּמַּעַל הַזֶּה רִאשׁוֹנָה ("and the hand of the officials and the chief men has been foremost in this unfaithfulness"). **The book's one hostile hand is not the enemy's; it is the leadership's.**
- **The English breaks it once, and the ESV is the better witness.** At Neh 6:9 the **ESV** keeps the idiom — "Their hands will drop from the work" — while the **NASB95** flattens it to "They will become discouraged with the work", leaving "strengthen my hands" in the same verse with nothing to answer. This is one of the few places in the book where the ESV is the more literal of the two.
- *Surfaced by:* Repetition, Vocabulary, Translations, Structure, Move 4. *High confidence on the counts; high on the design, since Neh 6:9 states both poles itself.*

### 4. Nehemiah denies Sanballat the only "memorial" in the book, and then asks God for one six times. `[T]`

- **The denial.** Neh 2:20 — וְלָכֶם אֵין־חֵלֶק וּצְדָקָה **וְזִכָּרוֹן** בִּירוּשָׁלִָם ("and you have no portion or right or **memorial** in Jerusalem"). **זִכָּרוֹן occurs once in Ezra–Nehemiah, here.** `[T — lemma, WLC]`
- **The petitions.** The verb זכר stands in **nine verses, all in Nehemiah, none in Ezra**: 1:8; 4:8; 5:19; 6:14; 9:17; 13:14; 13:22; 13:29; 13:31. `[T]` Six of the nine are addressed to God about a person — four "remember *me*" (5:19; 13:14, 22, 31) and two "remember *them*" (6:14; 13:29) — and the book's last four words are זָכְרָה־לִּי אֱלֹהַי לְטוֹבָה ("remember me, O my God, for good").
- **And the empire keeps its own records.** The Aramaic middle of Ezra turns on a search of the archive: Ezra 4:15 twice, בִּסְפַר־דָּכְרָנַיָּא ("in the book of records"), and Ezra 6:2, דִּכְרוֹנָה ("a record"). **The Persian empire remembers by filing; Nehemiah asks God to remember without a file.** The two vocabularies are cognate and the book puts them in the same volume, in its two languages.
- **The Greek keeps it and one English version does not.** Esdras B has μνημόσυνον at 2:20 and μνήσθητί μου at 5:19, 13:14, 13:22, 13:31 — one stem throughout. **NASB95 keeps it too** ("memorial" … "remember me"). **The ESV does not:** it renders 2:20 "you have no portion or right or **claim** in Jerusalem". A preacher working from the ESV will not see that Nehemiah refuses his enemy exactly what he spends the rest of the book begging for.
- *Surfaced by:* Vocabulary, Move 4 (units 9 and 19), Translations, Repetition, Structure. *High confidence.*

### 5. Two halves, two vocabularies — and the split is sharper than the overview's wall/house pair. `[T]` (synthetic)

The overview establishes חוֹמָה ("wall") in 28 verses, all Nehemiah. The corpus shows the same clean break in **four more words**, in both directions, and the pattern is too consistent to be accident:

| Root | Ezra | Nehemiah | What it is |
|---|---|---|---|
| דרש ("to seek, enquire") | **5 verses** (4:2; 6:21; 7:10; 9:12; 10:16) | **0** | Ezra's verb. He "set his heart לִדְרוֹשׁ the law" (7:10) |
| ירא ("to fear, to be afraid") | **0** | **10 verses** (1:5, 11; 2:2; 4:8; 6:9, 13, 14, 19; 7:2; 9:32) | Nehemiah's field, and it runs both ways: God is "great and awesome" (1:5; 4:8; 9:32), the enemies are "making us afraid" (6:9, 14, 19) |
| דלת ("door") | **0** | **11 verses** (3:1, 3, 6, 13, 14, 15; 6:1; 7:1, 3; 13:19) | The doors are hung in chs. 3 and 7 — and the last thing the book does with them is shut them against Tyrian fish (13:19) |
| חֶרְפָּה ("reproach") | **0** | **4 verses** (1:3; 2:17; 3:36; 5:9) | The presenting complaint (1:3) and the stated aim of the building (2:17) |

`[T — all four verified by lemma, WLC]`

**What it shows.** Ezra's half is about *enquiry* — a man seeks the Torah and a community is examined by it. Nehemiah's half is about *exposure* — a city with no doors, a people under reproach, a governor whose enemies work by fear. These are not two authors competing; they are one book giving its two halves different jobs, which is exactly what the overview said to expect. The vocabulary now shows it mechanically rather than impressionistically.

*Surfaced by:* Vocabulary, Structure, Author's Purpose, Repetition. *High confidence on the counts; moderate-to-high on the design, and held at moderate as a synthetic claim until a claim audit.*

---

## Book-Level Foundations

*Worked once and assumed under every unit below.*

### Phase 0.5 — the overview's four threads, extracted

- **Christological trajectory** (overview): contrast and unfinished trajectory, not prophecy. A lesser house whose foundation-noise is never resolved (Ezra 3:12–13); a priesthood disqualified by its own registers, with the Urim-and-Thummim question asked twice (Ezra 2:63; Neh 7:65) and never answered; kingship present only as a hole and as a slander (Neh 6:6–7); a signed covenant that fails; separation working by exclusion; "remember me" as the book's last word. The moralism check is "be a Nehemiah".
- **Intertextual map** (overview): **Torah-saturated and prophet-light.** Live sources: Deuteronomy 23:4–9 (3 uses), Deuteronomy 7:1–3 (4), Exodus 34:6 / Numbers 14:18 (2), the David–Solomon temple order (3), Haggai and Zechariah (2). Named single uses: Jer 25:11–12 / 29:10; Jer 51:11; 2 Chr 36:22–23; Deut 33:1; Lev 23:33–43; Joshua; 1 Kgs 11:1–8; Lev 18:24–30; 2 Kgs 19:15 // Isa 37:16. **The overview's own instruction: "A dig on any passage here should lean on Move 4 (internal echo) before Move 2."** This sweep has done that, and it is where nearly all of its new material came from.
- **Preaching traps** (overview): (1) the leadership manual; (2) the allegorised wall; (3) the Ezra 9–10 flinch and its opposite; (4) treating the dedication as the climax; (5) tidying the chronology of Ezra 4; (6) "the joy of the LORD is your strength" as a slogan.
- **Presenting situation** (overview): an anonymous book framing two first-person memoirs; a community in the province of עֲבַר נַהֲרָה ("Beyond the River"); an occasion that is a permission rather than a crisis; and one dominant pressure — *they are home and still slaves* (Ezra 9:9; Neh 9:36).

**Monograph-sourcing flag.** The overview draws on no single monograph. Its `[S]` material is five named works reached through a Logos pass (Batten; Manor; Young; Eskenazi; Blenkinsopp; Japhet; Bledsoe & Seal). **This sweep opened none of them**, and adds nothing to their standing; everything below that is not tagged `[S]` came off the corpus.

### Author's Purpose (Tool 1, book level)

Following the text. The book states an occasion in its first sentence and never leaves it: לִכְלוֹת דְּבַר־יְהוָה מִפִּי יִרְמְיָה ("to fulfil the word of the LORD by the mouth of Jeremiah", Ezra 1:1). Everything that follows is what happens when a promise comes true under a foreign crown. `[T]`

Three things recur across both halves and carry the purpose:

1. **Building, and what stops it.** בנה stands in 9 verses of Hebrew Ezra and 22 of Nehemiah, with the Aramaic בנא in a further 18 verses of Ezra 4–6. `[T — lemma, WLC]` Three things are built — altar, house, wall — each opposed, each finished.
2. **Reading, and doing what is read.** The citation formula is not prophetic but practical: כַּכָּתוּב ("as it is written") five times (Ezra 3:2, 3:4; Neh 8:15; 10:35, 10:37), reinforced by "they found written" (Neh 8:14; 13:1). `[T — confirmed against the overview's count]` The book cites Torah in order to *do* something.
3. **Separating, and failing to.** בדל stands in **nine verses** — Ezra 6:21; 8:24; 9:1; 10:8; 10:11; 10:16; Neh 9:2; 10:29; 13:3. `[T — lemma, WLC]` **This is three more than the overview lists**, and one of the three matters (see Book-Overview Tensions 1).

**Purpose, as the sweep reads it.** To show a people how to be the people of God when the kingdom has not come back — by rebuilding what can be rebuilt, reading what has been written, and separating what has been mixed — and to be honest that the mechanism does not hold. `[I]` This confirms the overview's purpose statement without qualification.

### Genre (Tool 12)

Post-exilic narrative history **built out of documents**, which is the feature that governs reading. Inside the narrative frame stand: royal decrees in Aramaic (Ezra 4:17–22; 6:3–12; 7:12–26); official correspondence in both directions (Ezra 4:11–16; 5:7–17); two copies of one register (Ezra 2:1–70; Neh 7:6–72); a builders' roster organised by gate (Neh 3); a list of offenders (Ezra 10:18–44); two first-person memoirs (Ezra 7:27–9:15; most of Neh 1–7 and 12:31–13:31); a national confession in prayer form (Neh 9:5–37); a signed and sealed document with its signatory list (Neh 10); settlement and priestly lists (Neh 11–12:26).

**Reading rule.** The narrator's habit is to *show the document and then show what was done with it*. A sermon that skips the documents to get to the action is skipping the book's own method — and the registers are where two of this sweep's findings live (units 2 and 13).

**The Psalter caution does not apply**, but its principle does: no form-critical label about how these documents were assembled decides what the finished book means.

### Bible Timeline (Tool 14) and Canonical Position (Phase 0.55)

Extracted from the overview's five-field block, which this sweep has checked rather than re-derived. In brief:

- **Section and neighbours.** Ketuvim; **Daniel** before, **Chronicles** after, in the order BHS prints. The reader arriving by this route meets Cyrus's decree here first and hears Chronicles repeat it as the canon's last word.
- **The caveat the overview names, and this sweep endorses.** That reading rests on the BHS and Talmudic sequence, **not on Codex Leningradensis itself**, where Chronicles stands first among the Writings. Any weight put on "Chronicles closes the canon" must name which sequence it depends on. `[T]` for the divergence; the choice between them is `[S]`.
- **Presupposes** (overview, verified): Jeremiah's seventy years; a written, consultable Torah; Deuteronomy's marriage law and its exclusion of Ammon and Moab; Deuteronomy's exile-and-return clause; the exodus-to-conquest story entire; David's and Solomon's arrangement of temple worship; Solomon's fall; Haggai and Zechariah as living contemporaries.
- **The sweep adds one entry to *Presupposes*: Deut 33:4.** See unit 11 — קְהִלָּה occurs in exactly two verses of the Hebrew Bible, Deut 33:4 and Neh 5:7. `[T — verified across all 23,213 WLC verses]`
- **Where canonical and compositional order diverge.** The 2 Chr 36:22–23 // Ezra 1:1–3a overlap is reported and **not resolved**, per Phase 0.55. Chronicles breaks off mid-sentence at וְיָעַל; Ezra carries the sentence to its end. That is the datum; what it proves is open.
- **The reader's timeline.** The reader stands this side of the resurrection. The question the book leaves open — who will stand as priest with Urim and Thummim (Ezra 2:63; Neh 7:65) — is one the New Testament answers, and the book's own unanswered question is a better route to Christ than any allegory of the wall.

### Historical and Cultural Background

- **Setting.**
  - **Time period.** Three Persian reigns, named: Cyrus, Darius, Artaxerxes — and Ezra 6:14 puts all three in one breath. `[T]` Ahasuerus is named once, at Ezra 4:6, out of sequence with its context. `[T]`
  - **Location.** Yehud, a province (מְדִינָה, Ezra 2:1; Neh 1:3; 7:6; 11:3) inside the satrapy עֲבַר נַהֲרָה / עֵבֶר הַנָּהָר ("Beyond the River"), which the book names in both languages. `[T]`
  - **Political context.** A community with no king, governed by a פֶּחָה ("governor", Neh 5:14, 15, 18; 12:26) who answers to Susa and is paid — or in Nehemiah's case declines to be paid — out of the province. Imperial permission is the book's enabling condition and imperial taxation is its standing grievance (Neh 5:4; 9:37). `[T]`
- **What the original audience knew without explanation.**
  - **That an archive search settles a dispute.** Ezra 5:17–6:2 is not a plot device; it is how the Achaemenid administration worked, and the narrative expects the reader to find it unremarkable that a scroll is found at Ecbatana rather than Babylon. `[I]`, high confidence.
  - **What a הַתִּרְשָׁתָא is.** The Persian title stands at Ezra 2:63; Neh 7:65, 69; 8:9; 10:2 and is never glossed. `[T]` Both Greek editions simply transliterate it.
  - **What the Aramaic signals.** The switch at Ezra 4:8 is announced by the text itself (4:7), and the reader is expected to know that official business is conducted in that language. `[T]`
  - **The temple vessels.** Ezra 1:7–11 and 5:14–15 assume the reader knows those vessels were taken (2 Kgs 25:13–15; Jer 52:17–23) and what their return means. `[I]`
  - **Sanballat, Tobiah and Geshem as real office-holders**, not stock villains — a Horonite, an Ammonite servant, an Arab. `[T]` for the labels.
- **What this changes about how we read.** The opposition in Ezra 4–6 and Neh 2–6 is **legal and procedural before it is military**. Letters, accusations of sedition, a request for an archive check, a summons to a meeting at Ono, a hired prophet. A sermon that pictures siege warfare has the wrong picture: the weapon is paperwork, and the counter-weapon is a better archive.

### Original Audience Reception (book level)

- **Canonical section and reader.** The Writings. The canonical reader has the Torah and the Prophets entire, has Psalms, Job and Proverbs in the ear, and arrives — as the Nevi'im closes with Malachi — already post-exilic and already living with promises that have not resolved.
- **What they brought.** Deuteronomy's promises and threats as live terms (the book quotes them and prays them); Jeremiah's seventy years as a clock that has now run out; and the memory of a first temple that some of them had seen (Ezra 3:12).
- **Shocking.** That the returned community's first recorded corporate act after the Torah is read is a mass dismissal of wives and children (Ezra 10) — and that the list closes at 10:44 **without saying what became of them**. `[T]`
- **Surprising.** That the book's most generous words about God come from a foreign king's decree (Ezra 1:2) and from the mouth of the empire's own bureaucracy (Ezra 6:10; 7:23).
- **Comforting.** כִּי־לְעוֹלָם חַסְדּוֹ ("for his lovingkindness is for ever", Ezra 3:11) sung at the foundation of a house nobody thought adequate.
- **Disturbing.** הִנֵּה אֲנַחְנוּ הַיּוֹם עֲבָדִים ("behold, we are slaves today", Neh 9:36), said aloud by the whole assembly on a fast day, three verses before they sign a covenant.
- **What we bring that they didn't.** A managerial reading of Nehemiah, in which a wall is a project and a governor is a leader; and an instinct to resolve Ezra 9–10 morally before reading it historically.
- **Candidate Fallen Condition Focus (book level):**

| Field | Content |
|---|---|
| **What they felt** | That the promised end of exile had arrived and had not delivered — the altar rebuilt, the house rebuilt, the wall rebuilt, and still "we are slaves today" (Ezra 9:9; Neh 9:36) `[T]` |
| **Candidate FCF** | We keep arriving at the thing we were promised and finding that it has not finished the ache — and we respond either by building something else or by pretending the ache is gone |
| **Shared / differs** | Shared: the gap between a real deliverance and an unfinished one. Differs: this side of the resurrection the gap has a name and a date — "he who began a good work… will perfect it" (Phil 1:6) — where for them it had neither |
| **Confidence** | Anchored (Ezra 3:12–13; 9:8–9; Neh 9:36–37; 13:31) |

### Biblical-Theological Themes (book level)

Three, and they **converge climactically** rather than running in parallel — which is where the preaching gold is.

1. **Temple / God's presence.** The house is rebuilt (Ezra 6:15) and dedicated בְּחֶדְוָה ("with joy", 6:16), and at its foundation the old men weep (3:12). **No glory cloud is reported, and the book never comments on the absence.** Trajectory: Hag 2:9's greater glory → John 2:19–21.
2. **Covenant.** Deuteronomy is quoted, prayed, and signed — and then broken clause by clause inside eleven chapters (Headline Finding 1). The book demonstrates not that this people was unusually bad but that **the mechanism is insufficient**, which is Jeremiah's argument for a covenant written somewhere other than on a sealed page (Jer 31:33).
3. **Priesthood.** Priests are excluded at the outset for want of a written genealogy, with the question deferred עַד עֲמֹד כֹּהֵן לְאוּרִים וּלְתֻמִּים (Ezra 2:63 // Neh 7:65) — and the deferral is never lifted. Priests head the intermarriage list (Ezra 10:18); the high priest's grandson marries into Sanballat's family and is driven out (Neh 13:28).

**The relation is (c) climactic convergence.** The three meet in one place: **a house with no glory, a covenant that cannot hold, and a priesthood that cannot be verified are the same problem stated three ways** — the machinery of access to God is running without the thing that made it work. Hebrews argues precisely this convergence and resolves it in one person (Heb 7–10). Preaching any one of the three alone in this book under-reads it.

### Christological Reading (book-level frame)

The overview's categories stand: **contrast and unfinished trajectory**, with no messianic citation of this book in the New Testament. The sweep confirms them and adds two refinements, both text-first:

1. **The Urim question is also a *standing* question, and the book's other standing-verbs answer it ironically.** עמד stands in 10 verses of Ezra and 24 of Nehemiah. `[T — lemma, WLC]` The book cannot produce a priest who **stands** with Urim (Ezra 2:63; Neh 7:65), and Ezra's prayer concedes אֵין לַעֲמוֹד לְפָנֶיךָ ("there is no standing before you", Ezra 9:15). What it *can* do is set people to stand: Ezra stands on a wooden platform and the people stand when the book is opened (Neh 8:4–5), and the governor's last recorded acts are וָאַעֲמִדֵם עַל־עָמְדָם ("and I set them in their place", 13:11) and וָאַעֲמִידָה מִשְׁמָרוֹת ("and I appointed watches", 13:30). **A book that cannot make a priest stand spends its last chapter making everyone else stand.** *Moderate-to-high confidence; the counts are verified, the irony is `[I]`.*
2. **Isa 50:6 stands inside the book's own rare vocabulary** (Headline Finding 2). This is a trajectory reading, not typology: it passes the theological-category test (covenant grief over the people's sin) and the authorial-pattern test (the book itself uses the root twice, at its two crises), but has **no NT precedent** for this specific connection and does not escalate in the way a type does. **Categorise it as trajectory and say so from the pulpit.**

**Moralism check (book level).** The overview's is right and the sweep confirms it at unit level. The specific corrective this sweep can add: the book's own answer to "be a Nehemiah" is **Neh 13:14 beside 13:22**. Nehemiah asks God not to wipe out חֲסָדַי ("my loyal deeds", 13:14) and, eight verses later, asks to be spared כְּרֹב חַסְדֶּךָ ("according to the greatness of your lovingkindness", 13:22). **One root, two owners, one chapter.** The book's most self-justifying voice ends by appealing to mercy, and it does so in the very word it had used of its own record. `[T — lemma, WLC: חסד in Ezra 3:11; 7:28; 9:9; Neh 1:5; 9:17; 9:32; 13:14; 13:22]` **Both English versions break this link** (NASB95: "my loyal deeds" / "Your lovingkindness"; ESV: "my good deeds" / "your steadfast love"), and the Greek keeps it (ἔλεός μου / τοῦ ἐλέους σου).

### The book's verified vocabulary map

Every figure below was produced with `find.py lemma` against the WLC and is reproducible in one line. **Counts are verses unless stated.** This table is the evidence base for several findings and is given once so the units need not restate it.

| Root / word | Gloss | Ezra | Nehemiah | Note |
|---|---|---|---|---|
| חזק | to strengthen, repair | 5 | 34 | 28 of Nehemiah's are in ch. 3 |
| רפה | to let drop, slacken | 1 (4:4) | 2 (6:3, 6:9) | the opposite pole |
| עזב | to forsake | 3 | 9 | 4 of Nehemiah's are in ch. 9, of God |
| עמד | to stand | 10 | 24 | |
| בנה | to build (Heb.) | 9 | 22 | plus Aramaic בנא in 18 verses of Ezra |
| שמע | to hear | 3 | 27 | the opposition's trigger, then the Torah's |
| ירא | to fear | 0 | 10 | |
| יִרְאָה | fear (noun) | 0 | 2 (5:9, 5:15) | both of "the fear of God" |
| דרש | to seek, enquire | 5 | 0 | |
| בין | to understand | 2 | 8 | 6 of the 8 are in ch. 8 |
| בדל | to separate | 6 | 3 | **three more than the overview lists** |
| חוֹמָה | wall | 0 | 28 | overview, confirmed |
| גָּדֵר | wall (metaphor) | 1 (9:9) | 0 | overview, confirmed |
| דלת | door | 0 | 11 | |
| חֶרְפָּה | reproach | 0 | 4 | |
| זכר | to remember | 0 | 9 | |
| זִכָּרוֹן | memorial | 0 | 1 (2:20) | |
| חסד | lovingkindness | 3 | 5 | |
| מרט | to pluck out hair | 1 (9:3) | 1 (13:25) | 11 verses in the whole Hebrew Bible |
| נטה | to extend | 2 (7:28; 9:9) | 0 | both with חֶסֶד; the only two |
| מעל (verb) | to act unfaithfully | 2 (10:2, 10:10) | 2 (1:8; 13:27) | |
| מַעַל (noun) | unfaithfulness | 3 (9:2, 9:4; 10:6) | 0 | 7 verses in total — overview, confirmed |
| שׂמח / שִׂמְחָה | to rejoice / joy | 3 | 5 | **5 words of the root in Neh 12:43 alone** |
| מצא | to find | 4 | 7 | |
| כתב | to write | 5 | 10 | |
| קְהִלָּה | assembly | 0 | 1 (5:7) | **2 verses in the whole Hebrew Bible** |
| גּוֹרָל | lot | 0 | 2 (10:35; 11:1) | |
| אֲמָנָה | firm agreement | 0 | 2 (10:1; 11:23) | |
| צַדִּיק | righteous | 1 (9:15) | 2 (9:8, 9:33) | all three of God, in prayer |
| Tobiah | — | 0 | 13 | named more often than Sanballat |
| Sanballat | — | 0 | 10 | |

### Textual, apparatus and language notes (book level)

**The two languages, re-verified independently.** The Aramaic runs **Ezra 4:8–6:18 and 7:12–26 — 67 verses**, a figure this sweep reproduced by counting the range directly and which matches the overview's morph-code result exactly. `[T]`

**The ketiv, and why it matters more in this book than in almost any other.** The WLC prints the ketiv **unpointed**, leaving the qere to the Masorah, so a pattern spelling the qere does not see the verse. The mechanical signal is a word carrying Hebrew consonants and no combining marks at all. Measuring that across the corpus (NFD-decomposed, splitting on whitespace **and maqqef and paseq**):

| | Verses with ≥1 unpointed form | % |
|---|---|---|
| **Ezra** | 29 / 280 | **10.4%** |
| **Nehemiah** | 22 / 405 | **5.4%** |
| Whole WLC | 1,099 / 23,213 | **4.73%** |

`[T — measured, reproducible]` **Ezra is the fifth densest book in the Hebrew Bible by this measure**, behind Daniel (22.4%), Lamentations (13.0%), 2 Samuel (10.9%) and Ruth (10.6%), and more than twice the canon average. **And inside Ezra the Aramaic is denser again: 12 of 67 Aramaic verses (17.9%) against 17 of 213 Hebrew verses (8.0%).** `[T]` This is a fact about **Leningrad's reading tradition as the WLC prints it**, not about the authors; its spread across the manuscripts has **not** been checked, and no finding in this sweep rests on it. It is reported because it is the practical reason the gate matters here more than elsewhere.

> **A method note, and a correction to the toolkit.** The skill's Phase 10.5 gate item (e3) states that "16.8 % of the Hebrew Bible's verses carry at least one unpointed form, and in Ezra it is 52.9 %." **Neither figure reproduces against this corpus by the definition stated in the gate itself** — I measure 4.73% and 10.4%. The definition I used is the one the gate gives: a token of two or more Hebrew consonants carrying no combining marks, after splitting on whitespace, maqqef and paseq. It is possible the original figures counted something else. **The lesson the gate teaches is unaffected and is if anything better supported** — Ezra really is among the most ketiv-dense books in the canon — but the numbers should be corrected or their definition stated. Drafted here as a candidate amendment; not applied.

**And the maqqef caught my own tooling first.** My first pass at the table above split on whitespace only and returned **28/280 for Ezra**, missing **Neh 2:13** (אֲשֶׁר־המפרוצים) and **Neh 9:17** (וְרַב־וחסד) — the two verses in this book most often cited as ketiv examples, including by the overview. Both are joined to the preceding word by maqqef, so the token carried combining marks and passed the test. Adding maqqef and paseq to the split recovered both. **Amendment J is not a hypothetical; it bit this run's own measuring instrument.**

**The two Greek forms.** Esdras B (Rahlfs' Εσδρας Βʹ) is one continuous 23-chapter book: Ezra = chs. 1–10, Nehemiah = chs. 11–23, so Neh 13 is Esdras B 23. `[T — verified in the Rahlfs export, whose chapter headers this sweep parsed directly]` Esdras A (1 Esdras) relocates Ezra 4:7–24 to just after the decree, omits 4:6, adds the bodyguards' contest, removes Nehemiah, and stops mid-sentence at Neh 8:13a. Both were in view; Esdras A is not a witness to an older Hebrew and is used here only where the shape of its rearrangement illuminates a unit.

**Where this sweep's Greek work corrected itself.** At **Neh 13:25** Swete (Vaticanus) has no equivalent of וָאֶמְרְטֵם: the clause is simply absent, and a report resting on Swete alone would have said "the Greek drops the hair-pulling". **Rahlfs has it — καὶ ἐμαδάρωσα αὐτούς.** The omission is Vaticanus's, not the Greek tradition's, and **BHS's apparatus carries no note at 13:25 at all**, which is a fair measure of how little weight it bears. The corpus README's rule did the work: observe from Swete, cite from Rahlfs. Reported here because the near-miss is the method functioning.

**Swete's two spellings of the Tirshatha** (Ἁθερσαὰ at Ezra 2:63, Ἁσερσαθὰ at Neh 7:65) are likewise a **Vaticanus** feature: Rahlfs has Αθερσαθα in both. Named so that nobody builds a translator-profile on it.

**Apparatus findings.** This sweep introduces **no new finding that rests on an apparatus feature** — no parashah, accent, ketiv or Masorah reading is load-bearing anywhere below. The overview's two apparatus notes (Neh 9:17 בְּמִרְיָם against 𝔊's ἐν Αἰγύπτῳ; and the ketiv וחסד against the qere) are carried forward as it states them, with their witnesses named, and are not re-derived here.

---
## Unit 1 — Ezra 1:1–11 ⭐ The king's decree and the vessels that came home

> 1:1 וּבִשְׁנַת אַחַת לְכוֹרֶשׁ מֶלֶךְ פָּרַס לִכְלוֹת דְּבַר־יְהוָה מִפִּי יִרְמְיָה **הֵעִיר יְהוָה אֶת־רוּחַ** כֹּרֶשׁ מֶלֶךְ־פָּרַס
> "Now in the first year of Cyrus king of Persia, in order to fulfill the word of the LORD by the mouth of Jeremiah, the LORD stirred up the spirit of Cyrus king of Persia" (NASB95)

### Headline Findings

1. **The book's first sentence names its clock and borrows its idiom from the same prophet.** Ezra 1:1 says it is fulfilling the word מִפִּי יִרְמְיָה ("by the mouth of Jeremiah") and in the same breath says God הֵעִיר … אֶת־רוּחַ ("stirred up the spirit") of Cyrus — which is Jeremiah's own phrase for the power that would take Babylon (Jer 51:11). `[T]`
2. **The chapter is a transfer of custody, counted.** Eleven verses, and five of them are an inventory (1:9–11). The vessels are the one thing in the book that goes out and comes back unchanged. `[T]`
3. **Two "stirrings" frame the chapter.** God stirs the king's spirit (1:1) and then stirs the people's (1:5) — the same verb, the same construction, four verses apart. `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** In canonical (BHS) sequence, Daniel. The reader has just watched a Judahite in the Persian court pray towards a ruined Jerusalem and be told of seventy weeks. `[I]`, moderate. More sharply: **2 Chr 36:22–23 contains these same verses and breaks off mid-sentence** at וְיָעַל ("and let him go up"). `[T]`

**Necessity answer.** This passage exists *here* because a promise with a date on it has come due, and the book will not begin with the people. It begins with the decree, because everything the community will later celebrate rests on a permission it did not obtain for itself. Position the chapter anywhere later and the whole book becomes a story about returnees; where it stands, the returnees are the second thing that happens.

**Implication.** The unit is not "the people go home". It is "the word of the LORD came true, and this is what that looked like": a Persian civil service memorandum. `[I]`

### 3. Structure

| Verses | Section | Function |
|---|---|---|
| 1:1 | The narrator's frame | Names Jeremiah, names the agent, names the means |
| 1:2–4 | The decree, quoted | The king speaks; a foreign mouth names יְהוָה אֱלֹהֵי הַשָּׁמַיִם |
| 1:5–6 | The response | God stirs the spirit again; neighbours contribute |
| 1:7–11 | The inventory | Numbers, and a total |

**The device is a frame that closes on an accountant's line.** The chapter opens with a prophetic word and ends with 5,400 items. That descent from oracle to inventory is the book's characteristic movement and should not be smoothed.

### 7. Vocabulary

- **הֵעִיר אֶת־רוּחַ ("stirred up the spirit").** Twice in the chapter (1:1, 1:5). The overview verified that the idiom stands in the whole Hebrew Bible only at 1 Chr 5:26; 2 Chr 21:16; 2 Chr 36:22; Jer 51:11; Hag 1:14; Ezra 1:1; 1:5. `[S: overview, verified there]` Its closest parallels are therefore a prophet announcing Babylon's fall and a prophet restarting a building site.
- **כְּלִי ("vessel").** The word that carries the chapter (1:7, 1:10, 1:11) and returns at Ezra 5:14–15; 7:19; 8:25–30, 33; and — pointedly — at **Neh 13:8–9**, where Nehemiah throws Tobiah's כְּלֵי ("household goods") out of the temple chamber and brings back the כְּלֵי בֵּית הָאֱלֹהִים ("vessels of the house of God"). *Moderate-to-high confidence on the link; the word is common enough that the weight rests on the shared setting, not the lexeme.*
- **הַגּוֹלָה ("the exile / the exiles").** Introduced at 1:11 and becomes the community's self-description through Ezra (2:1; 4:1; 6:19, 20, 21; 8:35; 9:4; 10:6, 7, 8, 16). `[T]`

**Proper-noun inventory:** Cyrus; Persia; Jeremiah; Jerusalem; Judah; Israel; Babylon; Nebuchadnezzar; Mithredath; Sheshbazzar. Routine scenery apart from three. **Jeremiah** carries the canonical freight (see Move 1 below). **Nebuchadnezzar** is named only as the man who took the vessels — the book's one backward glance at the catastrophe, and it is made in a property inventory. **Sheshbazzar** is named הַנָּשִׂיא לִיהוּדָה ("the prince of Judah", 1:8), a title the book never explains and never repeats.

### 8. Translations

**NASB95** "the LORD stirred up the spirit of Cyrus"; **ESV** identical. No divergence bearing on the findings.

One note worth carrying: both versions render the decree's opening כֹּה אָמַר כֹּרֶשׁ as "Thus says Cyrus", which in English sounds like the prophetic formula. It is the same formula, and the book has put it in a pagan king's mouth. Neither version is wrong; the preacher should simply know the echo is in the Hebrew too and is not a translator's artefact. `[T]`

**Ancient versions check.** 1 Esdras 2:1–14 carries this chapter, with the Greek at 2:11 giving a total of 5,469 vessels against the MT's 5,400 — BHS's apparatus notes the MT total as *numerus mendosus* and cites 𝔊α. `[T — apparatus, checked]` **Triage: category 2**, a substantive divergence in a number. It affects nothing a sermon would say, and the preacher should simply not build on the arithmetic of 1:9–11, which does not add up in either tradition.

### 10. Repetition

- **עלה ("to go up")** three times in eleven verses (1:3, 1:5, 1:11). The book's standing verb for the return, and **all 27 of its occurrences in Ezra–Nehemiah are physical movement** — the overview's audit finding, confirmed here by lemma (14 occurrences in 13 verses of Ezra, 13 in 13 of Nehemiah). `[T]` **There is no "going up spiritually" in this book**, and a sermon that finds one is importing it.
- **בנה ("to build")** three times (1:2, 1:3, 1:5), all of the house, before a stone is laid.
- **כֶּסֶף וְזָהָב ("silver and gold")** at 1:4 and 1:6, and again in the inventory.

### 11. Quotation / Allusion — with Move 4

**Jeremiah 25:11–12 / 29:10 → Ezra 1:1** *(high confidence for the citation; moderate for which oracle)*

*Source context:* Jeremiah 25 is an oracle of judgement in which the seventy years are a sentence on Judah *and* a term set against Babylon; 29:10 is the letter to the exiles, in which the seventy years are the term after which God will visit them and bring them back. The register differs: 25 is prosecution, 29 is pastoral assurance. **A citation of 29:10 brings a promise of return to a specific, named, waiting people; a citation of 25:11–12 brings the end of an empire.** Ezra 1:1 gets both because it does not name the verse.
*Book usage:* first use; Jeremiah is named once more only by implication.
*OT-to-OT:* 2 Chr 36:21 states the seventy-year form explicitly and ties it to Lev 26:34–35's sabbaths of the land. `[T]`
*What it adds:* the book's opening does not say "the exile ended". It says a spoken word finished running. The agent of the ending is a clock, not a movement.

**Jeremiah 51:11 → Ezra 1:1, 1:5** *(high confidence)*

*Source context:* Jer 51 is the oracle against Babylon; 51:11 reads הֵעִיר יְהוָה אֶת־רוּחַ מַלְכֵי מָדַי ("the LORD has stirred up the spirit of the kings of the Medes"), and what follows is Babylon's destruction. The idiom's home is *the raising up of a foreign power against Babylon.*
*What it adds:* Ezra 1:1 is not saying God gave Cyrus a good idea. It is using Jeremiah's own phrase for the instrument of Babylon's fall, in the sentence that names Jeremiah. **The added weight of the overview's v1.1 amendment is that the verse cites Jeremiah's clock and borrows Jeremiah's vocabulary at once.** `[S: overview, verified there]`

**Internal (Move 4):**
- *Planted for later:* **אֱלֹהֵי הַשָּׁמַיִם ("the God of heaven", 1:2)**, the title the empire uses for Israel's God. The overview verified it stands twelve times and **every one falls between Ezra 1:2 and Neh 2:20**, after which it is never used again. `[S: overview, verified there]` Cyrus opens the bracket; Nehemiah closes it by throwing the title at Sanballat. *High.*
- *Planted for later:* **the vessels.** Answered at Ezra 5:14–15 (the Persian record of them), 8:25–33 (weighed out and weighed in), and inverted at Neh 13:8–9. *Moderate-to-high.*
- *Planted for later:* **הַנִּשְׁאָר ("the one who remains", 1:4)** — the remnant vocabulary that returns as פְּלֵיטָה in Ezra 9:8, 9:13, 9:14, 9:15 and as הַנִּשְׁאָרִים in Neh 1:2–3. *Moderate.*

### 16. So What? (brief)

The author's intended response is not imitation but recognition: that a permission granted by a hostile empire is how a promise landed. `[I]` The behavioural edge is against two opposite errors — treating providence as a substitute for obedience, and treating secular machinery as beneath God's use. The prayer this unit drives is thanksgiving for openings one did not arrange.

### Passage-specific difficulties

- **Cyrus's theology.** 1:2 has a pagan king saying יְהוָה אֱלֹהֵי הַשָּׁמַיִם נָתַן לִי ("the LORD, the God of heaven, has given me"). The Cyrus Cylinder has him crediting Marduk in similar terms elsewhere; the book is not claiming his conversion, and a sermon should not either. `[S]`, well known, and worth naming from the pulpit before a hearer raises it.
- **The chronology.** Ezra 1:1 is 538 BC; the reader who knows Ezra 4:6–23 is coming should be told now that the narrator groups material thematically.

---

## Unit 2 — Ezra 2:1–70 Counted and named

### Headline Findings

1. **The chapter is one half of the book's structural bracket**, re-read a century later at Neh 7:6–72 (see unit 13). `[T]`
2. **It contains the book's unanswered question.** Ezra 2:63 defers the priestly question עַד עֲמֹד כֹּהֵן לְאוּרִים וּלְתֻמִּים, and the deferral is repeated at Neh 7:65 and never lifted. `[T]`
3. **Its arithmetic does not work, and the book lets it stand.** The itemised figures total 29,818; the stated total is 42,360 (2:64). `[S: overview, verified there]` The narrator prints both.

### 2. Context — Positional Necessity Check

**Preceding movement.** Ch. 1 has given a decree and an inventory of objects.

**Necessity answer.** Because the objects have been counted, the people must be. The chapter exists *here* — before the altar, before the foundation — because **this community is constituted by a document before it does anything**. Its first corporate act in the book is to be enumerated. Nothing is built until everyone is named. `[I]`, high confidence.

**Implication.** The register is not an interruption of the narrative; it is the narrative's first event.

### 3. Structure

Laypeople by family and by town (2:3–35) → priests (36–39) → Levites, singers, gatekeepers (40–42) → temple servants and Solomon's servants (43–58) → **those who could not prove their descent** (59–63) → totals (64–67) → offerings (68–69) → settlement (70).

**The structural point is the penultimate section.** A list organised by descent ends with the people who have no descent to show, and the chapter's last named act before the totals is an exclusion.

### 7. Vocabulary

- **הַתִּרְשָׁתָא ("the governor", 2:63).** A Persian title, unglossed, and the one who pronounces the exclusion. Both Greek editions transliterate it. `[T]`
- **הַנְּתִינִים ("the temple servants", 2:43, 58, 70).** Esdras B transliterates rather than translates (Ναθεινίμ), which the overview notes as the mark of a wooden translator. `[S: overview]`
- **וְלֹא נִמְצָאוּ ("and they were not found", 2:62).** The first occurrence of מצא in the book, and it is a negative. See Move 4.

**Proper-noun inventory:** some sixty family and place names. Routine, with one exception. **Barzillai (2:61)** is a character-dossier case: the priest who married into Barzillai's family took *their* name and is therefore un-provable. Barzillai the Gileadite provisioned David in flight and declined his reward (2 Sam 17:27–29; 19:31–39), and David's dying charge was that his sons be kept at the royal table (1 Kgs 2:7). `[T — source narrative re-read]` **The irony is exact: a family honoured by name in David's will is disqualified by name in Ezra's register.** *Moderate confidence on the irony as design; high on the data.* Cross-reported to Tool 11.

### 8. Translations

NASB95 2:63 "until a priest stood up with Urim and Thummim"; ESV "until there should be a priest to consult Urim and Thummim". **The ESV supplies "to consult", which the Hebrew does not have** (עַד עֲמֹד כֹּהֵן לְאוּרִים וּלְתֻמִּים), and in doing so decides that the priest's function is divinatory. The NASB95 leaves it open. Worth knowing, because the point of the verse is what is *missing*, and the ESV's addition specifies the lack in a way the Hebrew declines to.

**Ancient versions check.** Both Greek editions give the fuller form here — τοῖς φωτίζουσιν καὶ τοῖς τελείοις ("for the enlightening ones and the perfect ones") — and **abbreviate at Neh 7:65 to φωτίσων ("one who will give light"), dropping Thummim entirely.** `[T — Swete and Rahlfs both checked]` **Triage: category 1**, translation-level, not a variant: the Hebrew's exact doublet is a Hebrew-only exactness. Report as a fact about the Hebrew.

### 10. Repetition

בְּנֵי ("sons of") as a list-formula, some fifty times; the numeral formula; and **כְּאֶחָד ("as one", 2:64)** of the whole assembly. Note that this is *not* the phrase כְּאִישׁ אֶחָד ("as one man") of Ezra 3:1 and Neh 8:1 — the overview's verified pair. Two different phrases, both about unity, and the register uses the weaker one. `[T]`

### 11. Quotation / Allusion — with Move 4

No external citation. Move 2: not applicable.

**Internal (Move 4):**
- *Planted for later — and never resolved:* **Ezra 2:63 // Neh 7:65**, the Urim and Thummim deferral. The overview verified this is the only pair. **The sweep adds that the two Hebrew verses are near-identical while the Greek is not** (above), and that the book's other 33 uses of עמד make the un-standing priest conspicuous (Book-Level Christological frame). *High.*
- *Planted for later:* **the register itself**, re-read at Neh 7:6–72 as a book Nehemiah *found* (7:5). *High.*
- *Answers §earlier:* **the vessels of ch. 1 are matched by the people of ch. 2.** Two inventories, one of things, one of persons, in consecutive chapters. *Moderate, `[I]`.*
- *Planted for later:* **וְלֹא נִמְצָאוּ (2:62).** The book's finding-verb answers this at Neh 7:5 (וָאֶמְצָא סֵפֶר, "and I found the book"), 8:14 (וַיִּמְצְאוּ כָּתוּב, "and they found written") and 13:1 (וְנִמְצָא כָתוּב, "and there was found written"), and repeats the failure at Neh 7:64. **What cannot be found is a priestly genealogy; what can be found is a book.** מצא stands in 4 verses of Ezra and 7 of Nehemiah. `[T — lemma, WLC]` *Moderate-to-high; this is a genuine sweep finding and is not in the overview.*

### 16. So What? (brief)

A community that begins by being counted is a community that can be *checked* — and the chapter's honesty about who failed the check is the point. `[I]` For the church: membership that cannot be examined is not membership. Against moralism: the chapter's unresolved exclusion is not solved by effort.

### Passage-specific difficulties

- **Preaching a list.** The unit is Standard-weight for good reason; the overview's advice to preach it alongside Neh 7 or not at all is sound.
- **The numbers.** Do not defend the arithmetic. The narrator prints an itemised list that does not match its own total and does so twice; that is a datum about how he uses documents, not a problem to be solved.

---

## Unit 3 — Ezra 3:1–13 ⭐ The altar before the foundation

> 3:1 וַיֵּאָסְפוּ הָעָם **כְּאִישׁ אֶחָד** אֶל־יְרוּשָׁלִָם
> "the people gathered together as one man to Jerusalem" (NASB95)
>
> 3:13 וְאֵין הָעָם מַכִּירִים קוֹל תְּרוּעַת הַשִּׂמְחָה לְקוֹל בְּכִי הָעָם … וְהַקּוֹל נִשְׁמַע עַד־לְמֵרָחוֹק
> "so that the people could not distinguish the sound of the shout of joy from the sound of the weeping of the people … and the sound was heard far away" (NASB95)

### Headline Findings

1. **The altar is built before the foundation is laid, and the stated reason is fear.** 3:3 — כִּי בְּאֵימָה עֲלֵיהֶם מֵעַמֵּי הָאֲרָצוֹת ("for they were terrified because of the peoples of the lands"). `[T]` The book's first act of worship is a frightened one.
2. **The chapter ends on a noise the narrator refuses to sort out**, and never returns to resolve it. `[T]`
3. **It is one end of the book's clearest inclusio.** כְּאִישׁ אֶחָד occurs exactly twice — here and at Neh 8:1. `[S: overview, verified there]`

### 2. Context — Positional Necessity Check

**Preceding movement.** A decree, a register, and a people settled in their towns (2:70).

**Necessity answer.** Because the people are in their towns and the seventh month has come (3:1), the calendar itself requires an altar. The passage exists *here* because **the festival year will not wait for the building programme**. Sacrifice resumes before the site is prepared, and the narrator's clause וְהֵיכַל יְהוָה לֹא יֻסָּד ("but the temple of the LORD had not been founded", 3:6) marks the gap deliberately.

**Implication.** The chapter is about the order of priorities under pressure, and the order is: worship, then infrastructure. But the motive given for the haste is dread, not devotion — and the sermon must hold both. `[T]` for the motive.

### 3. Structure

3:1–3 the altar and the fear → 3:4–6 the festivals kept "as it is written", and the note that no foundation exists → 3:7 the contract with Sidon and Tyre → 3:8–9 the Levites appointed → 3:10–11 the foundation laid, with liturgy → 3:12–13 the noise.

**Bookends.** The chapter opens with the people gathered כְּאִישׁ אֶחָד and closes with them unable to tell their own two voices apart. `[I]`, and it is the chapter's best structural observation.

### 7. Vocabulary

- **כַּכָּתוּב ("as it is written", 3:2, 3:4).** Two of the book's five. `[T]`
- **מֹשֶׁה אִישׁ־הָאֱלֹהִים ("Moses the man of God", 3:2).** The Torah's own closing title for Moses (Deut 33:1). The phrase also stands at Josh 14:6; Ps 90:1; 1 Chr 23:14; 2 Chr 30:16. `[S: overview, verified there]` *Moderate-to-high.* **And the book uses the same title of David at Neh 12:24 and 12:36** — דָּוִיד אִישׁ־הָאֱלֹהִים. `[T]` The two men whose authority the liturgy runs on are given the same epithet, at the two ends of the book.
- **בְּאֵימָה ("in dread", 3:3).** A hapax in the book. The community's first motive. `[T]`
- **מֵרָחוֹק ("from afar", 3:13).** One of two in the book; the other is Neh 12:43. `[S: overview, verified there]`

**Proper-noun inventory:** Jeshua son of Jozadak; Zerubbabel son of Shealtiel; Moses; Sidonians; Tyrians; Lebanon; Joppa; Cyrus; Asaph; David. **Two carry freight.** *Zerubbabel son of Shealtiel* is a Davidid, and **the book never says so in those terms**, here or anywhere. `[T]` *Asaph and David* import the first temple's musical order wholesale (1 Chr 25; 2 Chr 5:12–13).

### 8. Translations

NASB95 3:3 "they were terrified because of the peoples of the lands"; ESV "for fear was on them because of the peoples of the lands". Both keep it. No divergence bearing on the findings.

**Ancient versions check.** The liturgical formula of 3:11, כִּי טוֹב כִּי־לְעוֹלָם חַסְדּוֹ, is the standing refrain of 2 Chr 5:13; 7:3; Ps 136 and elsewhere; the Greek renders it with its usual ὅτι ἀγαθόν, ὅτι εἰς τὸν αἰῶνα τὸ ἔλεος αὐτοῦ. No split.

### 9. Tone and Feel

The chapter's register changes twice. Verses 1–9 are administrative — dates, contracts, appointments, cedar from Lebanon by way of Joppa. Verses 10–11 are liturgical — trumpets, cymbals, antiphon. Verses 12–13 are neither: they are **reportage of an indistinguishable noise**, and the narrator's last word is that it carried. **The sermon's emotional architecture must not resolve what the text leaves unresolved.** If the congregation leaves able to say whether the day was happy or sad, the preacher has answered a question the author declined.

### 10. Repetition

- **עֹלָה ("burnt offering")** five times in six verses (3:2, 3:3 ×2, 3:4, 3:5, 3:6). The chapter piles the word up before the building exists.
- **קוֹל ("voice, sound")** four times in two verses (3:12–13).
- **תְּרוּעָה ("shout")** three times (3:11, 3:12, 3:13).

### 11. Quotation / Allusion — with Move 4

**Leviticus 23:33–43 → Ezra 3:4** *(high confidence)*

*Source context:* the Booths legislation, which is where the seventh-month festival calendar is set out and which specifies the daily burnt offerings by number. Its register is instructional and its setting is the wilderness, where Israel had no land and lived in shelters.
*Book usage:* the first of two — Neh 8:14–17 keeps the same feast, and the difference between the two occasions is the sweep's finding at unit 14.
*OT-to-OT:* Num 29:12–38 supplies the "number, according to the ordinance" of 3:4; Lev 23 and Num 29 are already a pair in the Torah's own festival law.
*What it adds:* the first thing the returned community does, having no house, is keep the feast that commemorates having no house.

**The 2 Chronicles 5 problem** *(moderate confidence)*. The liturgy of 3:10–11 reproduces the first temple's dedication (2 Chr 5:12–13) — same Asaphite singers, same trumpets and cymbals, same refrain. **In Chronicles the cloud of glory then fills the house. Here nothing fills it.** `[T]` for the parallel and for the absence. **Admissible as a pattern-break absence**, because the pattern is established by the source text and cited by this one; but the weight is capped at *moderate*, and the honest form of the claim is that the book does not comment.

**Internal (Move 4):**
- *Planted for later:* **כְּאִישׁ אֶחָד (3:1) → Neh 8:1.** The overview's v1.1 amendment. Gathered first by dread to build an altar, gathered last by hunger to hear a book. *High.*
- *Planted for later:* **מֵרָחוֹק (3:13) → Neh 12:43.** The unsortable noise becomes unambiguous joy — one chapter before the relapse. *High.*
- *Answers §earlier:* **the fear of 3:3 answers nothing yet, but is answered at Neh 6:16**, where it is the enemies who וַיִּפְּלוּ מְאֹד בְּעֵינֵיהֶם ("fell greatly in their own eyes"). `[I]`, *moderate*.
- *Planted for later:* **שִׂמְחָה (3:12, 3:13).** The root שׂמח stands in 8 verses of the book — Ezra 3:12, 3:13, 6:22; Neh 8:12, 8:17, 12:27, 12:43, 12:44 — and **its three moments are the foundation, the book, and the wall**. `[T — lemma, WLC]` *High on the count; moderate on the design.* Not in the overview.

### 16. So What? (brief)

The intended response is to build the altar anyway. `[I]` But the motive-clause forbids congratulating the builders: they did the right thing while frightened, and the text says so. Worldview: obedience under dread is still obedience, and God does not wait for better motives. The prayer is for honesty about mixed motives rather than their removal.

### Passage-specific difficulties

- **The weeping.** 3:12 does not say why the old men wept, and the two readings (grief at the lesser house; overwhelmed joy) are both defensible. **State the options; do not resolve.** The narrator's own interest is in the indistinguishability, not the cause.
- **"They set the altar on its foundations… for fear."** A preacher tempted to make this a courage text should notice the conjunction. `[T]`

---

## Unit 4 — Ezra 4:1–24 ⭐ "Let us build with you"

### Headline Findings

1. **The refusal at 4:3 is the first of a matched pair.** לֹא־לָכֶם וָלָנוּ לִבְנוֹת בַּיִת לֵאלֹהֵינוּ ("You have nothing in common with us in building a house to our God") is answered by Nehemiah's וְלָכֶם אֵין־חֵלֶק וּצְדָקָה וְזִכָּרוֹן בִּירוּשָׁלִָם ("you have no portion or right or memorial in Jerusalem", Neh 2:20). Two refusals, one at each half's opening. `[T]` *Not in the overview.*
2. **The adversaries use the book's own verb.** 4:2 — כִּי כָכֶם נִדְרוֹשׁ לֵאלֹהֵיכֶם ("for we seek your God as you do"). דרש stands in five verses of Ezra and none of Nehemiah, and one of the five is on the adversaries' lips. `[T]`
3. **The opposition's weapon is a letter, and the narrator files it.** 4:11–16 is quoted verbatim in Aramaic; 4:17–22 is the reply. **The chapter is where the book changes language.** `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** A foundation has been laid, with a noise heard far away (3:13).

**Necessity answer.** Because the noise carried. 4:1 opens וַיִּשְׁמְעוּ צָרֵי יְהוּדָה ("now when the enemies of Judah heard") — **the chapter exists here because the previous chapter ended with a sound**, and the book's opposition is triggered by hearing, every time (see Repetition).

**Implication.** Opposition in this book is a *consequence of visible progress*, not an ambient condition. That reframes Neh 4 and 6 as well.

**The chronological seam.** 4:6–23 covers the reigns of Ahasuerus and Artaxerxes — decades after Darius, whose reign 4:24 returns to. **The narrator has grouped opposition material thematically.** 1 Esdras relocated the block to just after the decree, omitting 4:6 entirely. `[T — Swete checked; the overview's correction of the Logos summary from "4:6–24" to "4:7–24" stands]` **The preacher's move is to show the seam, not to tidy it.**

### 3. Structure

4:1–3 the offer and the refusal (Hebrew) → 4:4–5 the campaign of discouragement, Cyrus to Darius (Hebrew) → 4:6 a letter under Ahasuerus (Hebrew) → 4:7 a letter under Artaxerxes, and the language-note → **4:8–23 the Aramaic dossier: accusation and rescript** → 4:24 return to Darius (Aramaic).

**The device is a dossier inserted into a narrative**, with the narrator's own frame at each end. The Aramaic begins mid-chapter and does not end until 6:18.

### 4. Linking Words

- **4:2 כִּי ("for") ←for←** the adversaries ground their request in shared worship.
- **4:3 כִּי ("but/for") ←for←** the refusal is grounded not in ethnicity but in a royal command: כַּאֲשֶׁר צִוָּנוּ הַמֶּלֶךְ כּוֹרֶשׁ ("as King Cyrus commanded us"). **The stated ground of exclusion is the decree's wording, not the seed.** `[T]` That matters for unit 8.
- **4:13, 4:16 הֵן ("if") — conditional**, twice, in the accusation: *if* this city is rebuilt, *then* revenue stops. The letter argues from fiscal consequence.
- **4:22 לְמָה ("why should…") — purpose/warning**, the rescript's closing pressure.

### 7. Vocabulary

- **טְעֵם (Aramaic, "decree, order").** Seventeen times, every one inside the Aramaic. `[S: overview, verified there]` The chapter contains six of them.
- **בְּטֵל (Aramaic, "to cease, to stop").** Six occurrences in five verses, all Aramaic — and **three of them are in this chapter** (4:21, 4:23, 4:24). `[S: overview, verified there]`
- **מְרַפִּים יְדֵי ("weakening the hands", 4:4).** The book's one occurrence of רפה in Ezra, and the pole against which all 47 occurrences of חזק stand. See Headline Finding 3. `[T]`
- **שִׂטְנָה ("accusation", 4:6).** A hapax in the book, cognate with the noun *śāṭān*. Flagged, not pressed: the consonantal link is real but nothing in the passage corroborates a demonic reading, and the hard rule for sound-based claims applies. *Uncertain — do not preach.*

**Proper-noun inventory:** Esarhaddon king of Assyria; Zerubbabel; Cyrus; Darius; Ahasuerus; Artaxerxes; Rehum; Shimshai; a list of transplanted peoples (4:9–10); Osnappar; Samaria; Beyond the River; Jerusalem. **Esarhaddon (4:2)** carries the freight: the adversaries date their own worship to the Assyrian deportations, which is the narrator's way of telling the reader who they are without saying it. `[T]` **Samaria (4:10, 4:17)** is named as an administrative centre, not yet as a religious rival.

### 8. Translations

NASB95 4:3 "You have nothing in common with us in building a house to our God"; ESV "You have nothing to do with us in building a house to our God." Both smooth the Hebrew's blunt לֹא־לָכֶם וָלָנוּ ("not to you and to us"). Neither is wrong, and the flatness of the original is worth saying aloud.

**Pulpit divergence note:** N/A — no pulpit text declared.

**Ancient versions check.** 1 Esdras places 4:7–24 immediately after the decree and omits 4:6. **Triage: category 2** in shape rather than wording — a whole-block rearrangement, and the scholarly consensus that Esdras A is secondary means it is best read as **an ancient editor's solution to the very difficulty the preacher faces**. `[S — overview's sources; the Greek itself verified]` That is the most useful thing to say about it from a pulpit.

### 10. Repetition

- **שמע ("to hear") as the opposition's trigger.** The root stands in 3 verses of Ezra and **27 of Nehemiah**. `[T — lemma, WLC]` The narrative refrain "when X heard" runs **Ezra 4:1; Neh 2:10; 2:19; 3:33; 4:1; 4:9; 6:1; 6:16** — eight times, and it introduces every episode of opposition in the book. `[T]` **Against it stands the other hearing: Neh 8:2–3, 8:9 (the people hear the Torah) and 13:3 (כְּשָׁמְעָם אֶת־הַתּוֹרָה, "when they heard the law").** Two kinds of hearing, and the book's shape is the turn from the first to the second. *High on the data; moderate-to-high on the design.* **This is a sweep finding and is not in the overview.**
- **בנה (Aramaic and Hebrew)** saturates the chapter: 4:1, 2, 3, 4 (Hebrew), 4:12, 13, 16, 21 (Aramaic).
- **קִרְיְתָא דָךְ ("that city")** three times in the accusation (4:13, 15, 16) — the letter's contemptuous demonstrative.

### 11. Quotation / Allusion — with Move 4

No external OT citation. Move 2: the book's live Deuteronomy source is not invoked here, which is itself notable — **the refusal of 4:3 is argued from Cyrus's decree, not from Deut 7 or Deut 23.** `[T]` The Torah ground is not brought in until Ezra 9.

**Internal (Move 4):**
- *Planted for later:* **4:1–3 → Neh 13:4–9.** The outsider refused at the gate is found living in the sanctuary. `[S: overview]` *High.*
- *Planted for later:* **4:3 → Neh 2:20.** The two refusals. `[T]` **Sweep finding; add to the overview's echo table.** *High — the forms differ but the speech-act, the position (each half's first opposition scene) and the tripartite denial are all parallel.*
- *Planted for later:* **4:4's "weakening the hands" → Neh 6:9's "their hands will drop".** The same strategy, named in both halves in the same idiom. `[T]` *High.* **Sweep finding.**
- *Answers §earlier:* the offer at 4:2 answers the dread of 3:3 — the peoples the builders feared now propose partnership. `[I]`, *moderate*.

### 13 / 15. Copycat and Who Am I?

**Copycat.** The refusal at 4:3 is **descriptive with a stated warrant** (a royal command), not a standing rule. The temptation to read it as a policy for ecumenical co-operation should be resisted in both directions: the text neither authorises nor forbids the modern analogue, and the community's ground is a decree that no longer exists.

**Who Am I?** Not Zerubbabel. The reader's place in this chapter is with the people whose work stops for fifteen years and who are not told why.

### 16. So What? (brief)

The response sought is endurance under procedural attack and clear-sightedness about offers of help. `[I]` The worldview note is the harder one: **the same imperial machinery that stops the work is the machinery that later funds it** (4:21 against 6:8), and the book will not let the reader classify the empire as simply hostile.

### Passage-specific difficulties

- **The chronology** (Preaching Trap 5). Address it in one sentence and move on.
- **"Let us build with you" refused.** A congregation will hear exclusivism. The honest exegesis: the ground given is a decree, the outsiders' claim is dated to a deportation, and the book later has the same community refusing to separate from anyone at all (Neh 13). Do not flatten it into a principle.

---

## Unit 5 — Ezra 5:1–6:22 The search of the archive

### Headline Findings

1. **The work restarts because of prophets and continues because of a filing system.** 5:1–2 (Haggai and Zechariah) and 6:1–2 (the scroll found at Ecbatana) are the two causes the narrative gives, and it gives them equal weight. `[T]`
2. **"The eye of their God was on the elders" (5:5) is the narrator's one theological comment in the Aramaic**, and it is what makes the rest of the correspondence readable. `[T]`
3. **Ezra 6:14 puts three kings in one clause** — מִטְּעֵם כּוֹרֶשׁ וְדָרְיָוֶשׁ וְאַרְתַּחְשַׁשְׂתְּא — after crediting the decree of the God of Israel. `[T]` The verse is the book's compressed theology of empire.

### 2. Context — Positional Necessity Check

**Preceding movement.** 4:24 has left the work stopped until the second year of Darius.

**Necessity answer.** Because a stoppage that ends needs a cause, and the narrator supplies two of different orders: a prophetic word (5:1) and an administrative precedent (6:1–2). **The passage exists here to show that the second did not replace the first.** The elders do not appeal to the archive; they build, and the archive is searched *by their opponents' initiative* (5:17).

**Implication.** Providence in this book works through procedure without being reducible to it.

### 3. Structure

5:1–2 the prophets and the restart → 5:3–5 the challenge, and the narrator's comment → 5:6–17 Tattenai's letter, with the elders' answer quoted inside it → 6:1–5 the search and the memorandum → 6:6–12 Darius's rescript → 6:13–15 completion → 6:16–18 dedication → 6:19–22 Passover.

**The device is a letter containing a speech containing a history.** 5:11–16 is the elders' own account of the exile and the decree, quoted inside their opponents' report to the king. **The community's confession of sin (5:12: "because our fathers had provoked the God of heaven to wrath") reaches Darius inside a hostile dossier.** `[T]` That is the finest structural touch in Ezra.

### 4. Linking Words

- **5:12 לָהֵן מִן־דִּי ("but because") ←for←** the elders ground the destruction of the temple in their fathers' provocation, not in Babylonian power.
- **6:8 וּמִנִּי שִׂים טְעֵם ("and I issue a decree") →therefore→** the reversal: the empire will now pay.
- **6:10 דִּי־לֶהֱוֺן מְהַקְרְבִין … וּמְצַלַּיִן לְחַיֵּי מַלְכָּא ("that they may offer … and pray for the life of the king") — purpose.** The stated imperial motive for funding the temple.
- **6:22 כִּי ("for") ←for←** twice: the joy is grounded in the LORD's having made them joyful and turned the king's heart.

### 7. Vocabulary

- **אָסְפַּרְנָא (Aramaic, "diligently, without delay").** Seven occurrences, all Aramaic, and **four of them in this unit** (5:8; 6:8, 6:12, 6:13). `[S: overview, verified there]`
- **מֶלֶךְ אַשּׁוּר ("king of Assyria", 6:22).** The narrator calls Darius the Persian "king of Assyria". `[T]` A deliberate anachronism, or the standing name for the imperial power. Either way the effect is to collapse three empires into one office.
- **חֶדְוָה (Aramaic, "joy", 6:16).** The dedication word; its Hebrew cognate חֶדְוָה stands at Neh 8:10 — חֶדְוַת יְהוָה הִיא מָעֻזְּכֶם ("the joy of the LORD is your strength"). **These are the book's only two.** *Moderate-to-high confidence; the two forms are cognate rather than identical, and the languages differ.* **Sweep observation; worth a preacher's attention at unit 14.**
- **בְּנֵי הַגּוֹלָה ("the sons of the exile", 6:16, 19, 20).** The community's name at its moment of success.

**Proper-noun inventory:** Haggai; Zechariah son of Iddo; Zerubbabel; Jeshua; Tattenai; Shethar-bozenai; Sheshbazzar; Nebuchadnezzar; Cyrus; Darius; Artaxerxes; Ecbatana; Media; Babylon; Beyond the River. **Haggai and Zechariah** carry real freight and are the only prophets the book names as contemporaries; **Ecbatana** matters because the scroll was *not* in Babylon, where the search began (5:17; 6:1–2) — the empire's memory required looking in the second place.

### 8. Translations

NASB95 6:22 "for the LORD had caused them to rejoice, and had turned the heart of the king of Assyria toward them"; ESV "for the LORD had made them joyful and had turned the heart of the king of Assyria to them". **Both keep "king of Assyria"**, which is right and which a congregation will find puzzling — prepare for the question.

**Ancient versions check.** The Aramaic of this unit is rendered closely by Esdras B. 1 Esdras 6:1–7:15 covers Ezra 5–6 and adds nothing material. No split.

### 10. Repetition

- **טְעֵם**, six times in the unit (5:3, 5:9, 5:13, 5:17; 6:1, 6:3, and again at 6:8, 6:11, 6:12, 6:14). **The whole contest is decrees answering decrees**, which the overview names and which the unit-level count bears out.
- **בקר (Aramaic, "to search")** at 5:17; 6:1 — the same verb in the request and in the compliance.
- **בֵּית אֱלָהָא ("the house of God")** relentlessly throughout, against Nehemiah's חוֹמָה.
- **שלם / שכלל ("to finish, complete")** at 5:11, 5:16; 6:14, 6:15.

### 11. Quotation / Allusion — with Move 4

**Haggai and Zechariah → Ezra 5:1; 6:14** *(high confidence — they are named)*

*Source context:* Haggai's four oracles in 520 BC are precisely about this stoppage: the people say "the time has not come" (Hag 1:2), Haggai says the house lies waste, and **Hag 1:14 uses the same idiom as Ezra 1:1 — "the LORD stirred up the spirit of Zerubbabel… and the spirit of all the remnant"**. `[T]` Zechariah 1–8 addresses the same months.
*Book usage:* the second of two (5:1; 6:14), and the only prophets named as living.
*OT-to-OT:* Hag 2:3's question — "who is left among you who saw this house in its former glory?" — is the same question Ezra 3:12 has already answered by showing the men who wept. **Haggai and Ezra are describing the same group of old men.** `[T]` *High.*
*What it adds:* the prophets are not decoration. Ezra 5–6 is the administrative history of the months Haggai preached into, and Hag 2:9's promise — "the latter glory of this house will be greater than the former" — is the answer to the unresolved noise of Ezra 3:13 that the book itself never gives.

**1 Chronicles 23–26 / 2 Chronicles 8:14 → Ezra 6:18** *(moderate confidence)*

*Source context:* David's division of priests and Levites into courses. Ezra 6:18 sets the priests בִּפְלֻגָּתְהוֹן ("in their divisions") and the Levites בְּמַחְלְקָתְהוֹן ("in their sections") — **and grounds it not in David but in כִּכְתָב סְפַר מֹשֶׁה ("as it is written in the book of Moses")**. `[T]`
*What it adds:* a small but real tension. The courses are Davidic in Chronicles and Mosaic here. The book's habit is to attribute liturgical order to David (Ezra 3:10; Neh 12:24, 45–46) and legal order to Moses; this verse does the opposite. Worth flagging rather than resolving.

**Internal (Move 4):**
- *Answers §earlier:* **5:14–15 answers Ezra 1:7–11.** The vessels are now described from the Persian side, by a governor reporting to a king. *High.*
- *Answers §earlier:* **6:16's dedication בְּחֶדְוָה answers 3:12–13's unsortable noise** — the first unambiguous corporate joy in the book. *Moderate.*
- *Planted for later:* **6:21's הַנִּבְדָּל ("everyone who had separated himself")** — and note that this occurrence is **inclusive**: those who separated *from the uncleanness of the nations of the land to join them* eat the Passover. `[T]` **The book's first use of בדל admits people.** That is not how the root behaves in Ezra 9–10, and the difference is the sweep's contribution to the separation theme (Book-Overview Tension 1). *High on the data.*
- *Planted for later:* **6:22's שִׂמְּחָם יְהוָה ("the LORD made them joyful") → Neh 12:43's הָאֱלֹהִים שִׂמְּחָם ("God made them rejoice").** The same construction at the two completions. `[T — lemma, WLC]` *High.* **Sweep finding.**

### 16. So What? (brief)

The response sought is confidence that God's purposes are not stalled by procedure, and patience with the fifteen years in which they appeared to be. `[I]` The motivation given is 5:5 — the eye of their God was on the elders — which is offered as a fact, not a feeling.

### Passage-specific difficulties

- **Praying for the king's life (6:10).** A pagan king funds sacrifices and asks for prayers in return. The community accepts. A congregation formed on separation texts will find this hard; the honest answer is that the book is not consistent on the question and does not try to be.
- **"King of Assyria" at 6:22.** Address it; do not silently correct it.

---

## Unit 6 — Ezra 7:1–28 ⭐ The scribe who set his heart

> 7:10 כִּי עֶזְרָא הֵכִין לְבָבוֹ **לִדְרוֹשׁ** אֶת־תּוֹרַת יְהוָה וְלַעֲשֹׂת וּלְלַמֵּד בְּיִשְׂרָאֵל חֹק וּמִשְׁפָּט
> "For Ezra had set his heart to study the law of the LORD and to practice it, and to teach His statutes and ordinances in Israel." (NASB95)

### Headline Findings

1. **7:10 is the book's one explicit statement of a man's inner purpose**, and it is tripartite: seek, do, teach. `[T]`
2. **The chapter turns on a genealogy that skips six generations** and lands on Aaron (7:1–5), and then on a Persian rescript that gives a foreign scribe judicial power over a satrapy (7:25–26). Descent and commission, in that order.
3. **The chapter ends with the book's first-person voice beginning** (7:27), and with the only two occurrences of נטה + חֶסֶד in the book. `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** The house is built and dedicated (6:15–18); the Passover has been kept (6:19–22). The building programme is complete.

**Necessity answer.** Because a finished house raises a question the house cannot answer: *what is it for?* The narrator's own bridge is וְאַחַר הַדְּבָרִים הָאֵלֶּה ("now after these things", 7:1), covering some fifty-seven years in four words. **The chapter exists here because the book's second half is about the Torah rather than the building, and the hinge is a man who carries one.** `[I]`, high confidence.

**Implication.** Ezra 7 is not a new start; it is the answer to Ezra 6. A completed temple without a taught Torah is what the first temple had, and the book knows how that ended.

### 3. Structure

7:1–5 genealogy, backwards to Aaron → 7:6 the summary verse (scribe, hand of God, all his request) → 7:7–9 the journey, dated → 7:10 the narrator's verdict → 7:11–26 the rescript, in Aramaic → 7:27–28 Ezra's blessing, in Hebrew and the first person.

**The device is a hinge.** The chapter changes language twice and voice once, and the voice-change is permanent for three chapters.

### 4. Linking Words

- **7:6 כְּיַד־יְהוָה אֱלֹהָיו עָלָיו ("according to the hand of the LORD his God upon him") ←for←** the reason the king granted everything.
- **7:9 כִּי ("for") ←for←** the dates are grounded in the same hand.
- **7:10 כִּי ("for") ←for←** — and this is the load-bearing one. **7:10 explains 7:6.** The king granted his requests *because* the hand of God was on him, and the hand of God was on him in the context of a man who had set his heart to seek, do and teach. The two "for"s stack. `[T]`
- **7:23 דִּי־לְמָה ("lest") — purpose/apprehension.** Artaxerxes' stated motive: lest there be wrath against the king's realm.

### 7. Vocabulary

- **סֹפֵר מָהִיר ("a skilled scribe", 7:6).** מָהִיר occurs four times in the Hebrew Bible; in Ps 45:2 it describes a ready writer's tongue and in Prov 22:29 a man skilled in his work. *Moderate confidence on the resonance; the term is professional, not honorific.*
- **לִדְרוֹשׁ ("to seek", 7:10).** One of Ezra's five; the root is absent from Nehemiah entirely. `[T]` **Ezra seeks the Torah; the adversaries claimed to seek the God (4:2); the community is told not to seek the peace of the peoples (9:12).** One root, three objects, and the book's judgement on each is different.
- **הֵכִין לְבָבוֹ ("set his heart").** The idiom recurs in Chronicles of kings who prepared their hearts to seek God (2 Chr 12:14; 19:3; 30:19). *Moderate-to-high.* **Ezra is described in the vocabulary Chronicles uses for good kings, in a book that has no king.** `[I]`, and it is the best Christological pointer in the unit.
- **הִטָּה־חֶסֶד ("extended lovingkindness", 7:28).** נטה occurs in **exactly two verses of the book — Ezra 7:28 and 9:9 — and both are with חֶסֶד.** `[T — lemma, WLC]` At 7:28 God extends it to Ezra before one king; at 9:9 to the whole community before "the kings of Persia". **Ezra's personal experience becomes the nation's confession two chapters later, in the same idiom.** *High.* **Sweep finding; not in the overview.**

**Proper-noun inventory:** sixteen generations from Ezra to Aaron; Artaxerxes; Babylon; Jerusalem; Persia. **Aaron the chief priest (7:5)** is the freight: the genealogy exists to establish that the man who will enforce the marriage law is himself of the line the register of Ezra 2 could not verify for others.

### 8. Translations

NASB95 7:10 "had set his heart to study the law of the LORD and to practice it"; ESV "had set his heart to study the Law of the LORD and to do it". **Both render לִדְרוֹשׁ as "study"**, which is defensible but narrow: the root is the book's seeking-verb and elsewhere both versions give it as "seek" (Ezra 6:21). A preacher should say that the word behind "study" is the word behind "seek the LORD".

**Ancient versions check.** No split of consequence in this unit.

### 10. Repetition

- **כֹּהֵן ("priest")** and **סֹפֵר ("scribe")** paired at 7:11, 7:12, 7:21 — Ezra holds both offices, and the rescript addresses him by both.
- **יַד ("hand")** at 7:6, 7:9, 7:14 (בִּידָךְ, "in your hand", of the law), 7:25 (דִּי־בִידָךְ, "which is in your hand", of the wisdom of God), 7:28. **Five times, and twice of what Ezra is carrying.** The hand of God is on him and the law of God is in his hand. `[T]` *Sweep observation.*
- **אָסְפַּרְנָא** three times in the rescript (7:17, 7:21, 7:26).

### 11. Quotation / Allusion — with Move 4

No direct quotation. **Move 2 (book usage):** the Torah is named four times in the chapter (7:6, 7:10, 7:12, 7:14, 7:25–26 as דָּת) but never quoted. **The chapter is about the book rather than from it** — which is exactly the position it occupies structurally.

**Internal (Move 4):**
- *Answers §earlier:* **7:5's Aaronic descent answers 2:61–63's failed priestly registers.** The book brings on a priest whose genealogy *is* recorded, sixteen generations of it, in a book that had to exclude priests who could not produce theirs. **It still does not answer the Urim question.** `[I]` on the design, `[T]` on the data. *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **7:10's לִדְרוֹשׁ … וְלַעֲשֹׂת וּלְלַמֵּד ("to seek… to do… to teach") → Neh 8:7–8**, where the Levites are מְבִינִים אֶת־הָעָם לַתּוֹרָה ("giving the people understanding of the law"). The teaching clause of 7:10 is executed a book later by other people. *Moderate.*
- *Planted for later:* **7:28's "extended lovingkindness before the king" → 9:9.** *High.*
- *Planted for later:* **the first person.** 7:27 begins the memoir, which the narrator drops without explanation at 10:1. *High on the data.*

### 13 / 15. Copycat and Who Am I?

**Copycat.** 7:10 is the book's one genuinely **normative pattern**, and the NT warrant for reading it so is the general commendation of Scripture-formed teachers rather than any citation of this verse. Label it as a pattern, not a command — and note that the *order* is the teachable part: seek, do, then teach.

**Who Am I?** Not Ezra, in the sense of the commission — he is given judicial authority over a satrapy by a king. But 7:10 is the one place in this book where imitation is the right instinct, and the preacher should say so plainly, having denied it everywhere else.

### 16. So What? (brief)

The intended response is the three-fold discipline of 7:10, with the order kept. `[I]` The motivation is not duty but the hand of God: the chapter's own logic is that the hand rested on a man whose heart was set, and it declines to tell us which caused which. The prayer is for a set heart before a successful ministry.

### Passage-specific difficulties

- **Artaxerxes' motive (7:23).** "Lest there be wrath against the realm." The empire funds Israel's worship as insurance. Do not spiritualise it.
- **7:26's penalties** — death, banishment, confiscation, imprisonment — are imperial, not Mosaic, and are conferred on a priest. A congregation formed on church-state separation will need this named.

---

## Unit 7 — Ezra 8:1–36 The fast at the river Ahava

### Headline Findings

1. **The chapter is an argument about escorts conducted by not asking for one.** 8:22 — כִּי בֹשְׁתִּי לִשְׁאוֹל מִן־הַמֶּלֶךְ חַיִל וּפָרָשִׁים ("for I was ashamed to request from the king troops and horsemen"). `[T]` **And Nehemiah takes the escort** (Neh 2:9). The book puts two leaders' opposite decisions in the same volume and commends both.
2. **Ezra's separation of twelve priests (8:24) uses the book's exclusion-verb inclusively.** וָאַבְדִּילָה מִשָּׂרֵי הַכֹּהֲנִים שְׁנֵים עָשָׂר ("Then I set apart twelve of the leading priests"). `[T]` **This occurrence is missing from the overview's list of בדל.**
3. **The silver is weighed out and weighed in.** 8:26–30 and 8:33–34: the same verb, the same officers, a written record. **The chapter's theology of trust is an audit trail.**

### 2. Context — Positional Necessity Check

**Preceding movement.** Ezra has a commission, royal funding, and a stated inner purpose (7:10).

**Necessity answer.** Because a commission must be executed, and the execution exposes two things the commission did not: that no Levites volunteered (8:15), and that the funding creates a security problem the commission's own rhetoric forbids solving (8:22). **The chapter exists here to show the cost of what ch. 7 announced.**

**Implication.** The unit is Standard-weight but is the practical hinge between Ezra's commission and Ezra's crisis, and a series that skips it loses the man's character before ch. 9 needs it.

### 3. Structure

8:1–14 the roster of those who went up → 8:15–20 the missing Levites and the recruitment at Casiphia → 8:21–23 the fast → 8:24–30 the weighing-out and the charge → 8:31–34 the journey and the weighing-in → 8:35–36 sacrifices and the delivery of the decrees.

**Bookends:** a list at each end (8:1–14 of people, 8:26–27 and 8:33 of metal), with a fast at the centre.

### 4. Linking Words

- **8:22 כִּי ("for") ←for←** twice, stacked: *because* I was ashamed, *because* we had said to the king that the hand of our God is on all who seek him.
- **8:23 וַיֵּעָתֵר לָנוּ ("and He was entreated by us")** — the result clause, stated in four Hebrew words and not elaborated.

### 7. Vocabulary

- **וָאַבְדִּילָה ("and I set apart", 8:24).** See Headline Finding 2 and Book-Overview Tension 1. **Both NASB95 and ESV render it "set apart" here and "separate" in the exclusion passages** — the same root, two English words, and the link is invisible in English.
- **מְבַקְשָׁיו לְטוֹבָה ("all who seek him for good", 8:22).** The root בקש with טוֹבָה. **And the only other place the book joins them is Neh 2:10**, where Sanballat is grieved that a man came לְבַקֵּשׁ טוֹבָה לִבְנֵי יִשְׂרָאֵל ("to seek the good of the sons of Israel"). `[T]` **Two verses, one idiom, and the second is a pagan's reaction to the first's theology.** *Moderate-to-high.* **Sweep finding.**
- **וְאוֹרֵב ("and the ambusher", 8:31).** A hapax in the book; the danger the escort would have met.
- **שׁקל ("to weigh")** four times in the unit (8:25, 26, 29, 33).

**Proper-noun inventory:** twelve family heads; Ahava; Casiphia; Iddo; Sherebiah; Hashabiah; Meremoth son of Uriah; Eleazar son of Phinehas; Jozabad; Noadiah; Artaxerxes' satraps. **Phinehas (8:33)** is the freight-bearing name: Eleazar son of Phinehas receives the silver, and Phinehas is the priest whose zeal against a foreign marriage stopped the plague (Num 25:6–13) and earned a covenant of perpetual priesthood. `[T — source narrative re-read]` **He is named one chapter before Ezra 9.** *Moderate confidence on the placement as design; high on the data.* **Sweep finding; nothing in the overview notes it.** (**Noadiah** at 8:33 is a Levite; a woman of the same name opposes Nehemiah at Neh 6:14. Different persons; note only so nobody links them.)

### 8. Translations

NASB95 8:22 "I was ashamed to request from the king troops and horsemen to protect us"; ESV "For I was ashamed to ask the king for a band of soldiers and horsemen to protect us." Substantively identical.

**Ancient versions check.** 1 Esdras 8:1–9:36 covers Ezra 7–10; nothing material diverges here. No split.

### 10. Repetition

- **הַכֶּסֶף וְהַזָּהָב וְהַכֵּלִים ("the silver and the gold and the vessels")** as a fixed triad at 8:25, 8:30, 8:33.
- **קֹדֶשׁ ("holy")** three times in one verse (8:28): the men are holy, the vessels are holy, the silver and gold are a freewill offering.
- **יַד ("hand")** at 8:18 (the good hand of our God), 8:22 (the hand of our God), 8:26 (weighed into their hand), 8:31 (the hand of our God), 8:33 (weighed into the hand of Meremoth). **Five times, and the same word covers divine providence and the physical transfer of bullion.** `[T]` *Sweep observation.*

### 11. Quotation / Allusion — with Move 4

No direct citation. **Move 2:** the Torah is not quoted; the chapter's warrant for the twelve priests and the twelve bulls (8:24, 8:35) is the number, not a text.

**Internal (Move 4):**
- *Answers §earlier:* **8:22's "the hand of our God is on all who seek him" restates 7:6, 7:9, 7:28** — and this time as a public claim Ezra has to live up to. *High.*
- *Answers §earlier:* **8:25–34's weighing answers 1:7–11's counting.** The vessels that Cyrus counted out are weighed in again at Jerusalem, by name, with a written record. *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **8:15's לֹא־מָצָאתִי שָׁם ("I found none there") of the Levites.** The Levite-supply problem recurs at **Neh 13:10**, where the Levites have fled to their fields because their portions were not given. `[T]` **The book opens and closes its Levite theme with a shortage.** *Moderate.* **Sweep finding.**
- *Planted for later:* **Phinehas (8:33) → Ezra 9–10.** *Moderate.*

### 16. So What? (brief)

The response sought is the costly consistency of 8:22: having said a thing about God to an unbeliever, act as though it were true. `[I]` The four audiences are unusually easy here, and the unbeliever's audience is the point — Ezra's shame is specifically about what the king would conclude.

### Passage-specific difficulties

- **Ezra fasts and refuses an escort; Nehemiah accepts one.** A congregation reading the book straight through will notice. The honest answer: the book records both and condemns neither, and Ezra's reason is rhetorical consistency in a specific conversation, not a principle about armed protection.
- **"I proclaimed a fast… that we might humble ourselves"** — do not turn 8:21–23 into a technique.

---

## Unit 8 — Ezra 9:1–10:44 ⭐ The holy seed

> 9:9 כִּי־עֲבָדִים אֲנַחְנוּ וּבְעַבְדֻתֵנוּ לֹא עֲזָבָנוּ אֱלֹהֵינוּ **וַיַּט־עָלֵינוּ חֶסֶד** לִפְנֵי מַלְכֵי פָרַס
> "For we are slaves; yet in our bondage our God has not forsaken us, but has extended lovingkindness to us in the sight of the kings of Persia" (NASB95)

### Headline Findings

1. **Ezra's prayer contains the book's central admission and its central verb in one verse.** 9:9 says both "we are slaves" and "he has not forsaken us" — and עזב is the root the covenant of Neh 10:40 will be signed on and Neh 13:11 will prosecute. `[T]` *This connection is a sweep finding.*
2. **The nations-list of 9:1 is a splice of two Torah laws.** Deut 7:1's seven nations minus Girgashite and Hivite, plus the Ammonite, Moabite and Egyptian of Deut 23. `[S: overview, verified there]`
3. **Ezra tears out his own hair (9:3) — a gesture the book gives only once more, to Nehemiah at 13:25, and then of other men's hair.** `[T]` See Headline Finding 2 at sweep level.
4. **The list ends without saying what became of the women and the children.** 10:44. `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** Ezra has arrived with a Torah, a royal commission including judicial powers (7:25–26), and a proven record of trusting God without an escort.

**Necessity answer.** Because the Torah has arrived. **The crisis exists at this point in the book precisely because a man who can read the law is now in the room** — 9:1 opens וּכְכַלּוֹת אֵלֶּה ("now when these things had been completed"), immediately after the delivery of the king's decrees (8:36). The officials do not report a new sin; they report a standing one, to the first man equipped to name it. **Torah does not find a clean community; it makes an old condition visible.**

**Implication.** The unit is not "Ezra discovers intermarriage". It is "the law arrives, and the first thing it does is expose the leadership" — וְיַד הַשָּׂרִים וְהַסְּגָנִים הָיְתָה בַּמַּעַל הַזֶּה רִאשׁוֹנָה ("and the hand of the princes and the rulers has been foremost in this unfaithfulness", 9:2). `[T]` The book's one hostile hand.

### 3. Structure

9:1–2 the report → 9:3–4 the physical response and the gathering of the tremblers → 9:5–15 the prayer → 10:1–5 Shecaniah's proposal and the oath → 10:6–8 the proclamation → 10:9–15 the assembly in the rain, and the four who opposed → 10:16–17 the commission and its three months → 10:18–44 the list.

**The device is descent from prayer to administration.** The prayer (9:5–15) is the theological peak; everything after it is procedure, and the chapter ends in a list of names. That descent is the same movement as ch. 1 and should be read as the book's signature, not as anticlimax.

### 4. Linking Words

- **9:6 כִּי ("for") ←for←** the shame is grounded in the height of the iniquities.
- **9:8 וְעַתָּה ("and now") — temporal pivot** into grace: כִּמְעַט־רֶגַע ("for a brief moment").
- **9:9 כִּי ("for") ←for←** — the load-bearing connector of the prayer. *Because* we are slaves and he has not forsaken us.
- **9:10 וְעַתָּה ("and now") — the second pivot**, this time into the question the prayer cannot answer: מַה־נֹּאמַר ("what shall we say?").
- **9:14 הֲנָשׁוּב ("shall we again…?") — rhetorical question** functioning as the prayer's conclusion. **The prayer ends without a petition.** `[T]` It states the case and stops: הִנְנוּ לְפָנֶיךָ בְּאַשְׁמָתֵינוּ ("behold, we are before You in our guilt", 9:15). That is structurally remarkable and is the unit's best homiletical point.

### 7. Vocabulary

- **מַעַל ("unfaithfulness").** The noun at 9:2, 9:4, 10:6; the verb at 10:2, 10:10 — and the verb again at **Neh 1:8 and 13:27**. **Seven verses in all.** `[T — lemma, WLC; the overview's figure confirmed]` The root's home is the priestly law of sacrilege (Lev 5:15; Num 5:6, 12), which classifies this marriage problem as **a trespass against holy things**, not as a race problem. That is the single most important lexical fact for preaching this unit. *High confidence on the lexical field.*
- **זֶרַע הַקֹּדֶשׁ ("the holy seed", 9:2).** The phrase occurs in the Hebrew Bible here and at **Isa 6:13** (זֶרַע קֹדֶשׁ מַצַּבְתָּהּ, "the holy seed is its stump"). *Moderate-to-high confidence; the forms differ by the definite article and the contexts differ sharply* — Isaiah's is a promise of survival through devastation, Ezra's is a description of what is being adulterated. **The link is worth naming and worth not pressing.** Flag for a solo dig.
- **פְּלֵיטָה ("escaped remnant").** Four times in the prayer (9:8, 9:13, 9:14, 9:15), and the word Nehemiah's brother uses at Neh 1:2. `[T]` The prayer's whole argument runs on how little is left.
- **חָרֵד ("trembling", 9:4; 10:3).** Those who tremble at the words of God — and Isa 66:2, 5 uses the same word of the people God regards. *Moderate.*
- **מְשׁוֹמֵם ("appalled", 9:3, 9:4).** Twice; Ezra sits still from the report until the evening offering.

**Proper-noun inventory:** the eight nations of 9:1; Shecaniah son of Jehiel; Jehohanan son of Eliashib; Jonathan son of Asahel; Jahzeiah son of Tikvah; Meshullam; Shabbethai; and the 111 names of 10:18–43. **The nations are the freight** (Move 1 below). **Jehohanan son of Eliashib (10:6)** matters for the book's chronology and for Neh 13:4–7, where an Eliashib gives Tobiah a chamber; whether the same family is meant is **uncertain** and should be flagged, not asserted.

### 8. Translations

- **9:2 NASB95 "the holy race has intermingled"; ESV "the holy race has mixed itself".** **Both render זֶרַע הַקֹּדֶשׁ as "the holy race".** The Hebrew is "seed", and "race" imports a category the Hebrew does not carry and that a modern congregation will hear loudly. **This is the most consequential translation note in the book.** A preacher should say "seed", explain that the term is covenantal and cultic (מַעַל, above), and name the mistranslation risk explicitly. *High confidence.*
- **9:3 / 13:25 "pulled … hair" in both versions at both places** — the doublet is visible in English. Good news; use it.
- **10:44 NASB95 "and some of them had wives by whom they had children"; ESV "and some of the women had even borne children".** Both leave the outcome unstated, as the Hebrew does.

**Ancient versions check.** **Triage: category 1.** The Hebrew's מרט doublet and the מַעַל field do not survive into Greek; that is translation, not corruption. No category 2 variant of consequence in the unit.

### 10. Repetition

- **נָשִׁים נָכְרִיּוֹת ("foreign wives")** six times in ch. 10 (10:2, 10:10, 10:11, 10:14, 10:17, 10:18, 10:44 — and at Neh 13:27). The narrator's fixed formula.
- **אַשְׁמָה ("guilt")** five times in the prayer and its aftermath (9:6, 9:7, 9:13, 9:15; 10:10, 10:19).
- **וְעַתָּה ("and now")** three times in the prayer (9:8, 9:10, 9:12) — the pivots.
- **עַמֵּי הָאֲרָצוֹת / עַם הָאָרֶץ ("the peoples of the lands")** at 9:1, 9:2, 9:11; 10:2, 10:11 — and at 3:3, where they were the object of fear.

### 11. Quotation / Allusion — with Move 4

**Deuteronomy 23:4–9 (Eng 3–8) → Ezra 9:12** *(high confidence)*

*Source context:* the law of the assembly. Ammonite and Moabite are excluded to the tenth generation **because they did not meet Israel with bread and water and because they hired Balaam**; Edomite and Egyptian are *admitted* in the third generation, "for you were a sojourner in his land". **The law Ezra cites is a law with an inclusion clause in it**, and the clause is four verses from the one he uses. `[T — source read]`
*Book usage:* three uses (Ezra 9:1, 9:12; Neh 13:1–3), and Neh 13 quotes it openly and by name.
*OT-to-OT:* Deut 23 and Deut 7 are separate laws with different objects — one about assembly membership, one about marriage in the land — and **Ezra 9:1 has spliced them.** `[S: overview, verified there]`
*What it adds:* the exact words וְלֹא־תִדְרְשׁוּ שְׁלֹמָם וְטוֹבָתָם reproduce Deut 23:7, **and the phrase occurs in only those two places in the Hebrew Bible.** `[S: overview, verified there]` So the citation is certain. What the triad adds is that **Ezra applies to marriage a law about the assembly, and omits its own exception clause** — which is not a charge against Ezra but is the fact a preacher must hold when a congregation asks why Ruth the Moabite is in the canon.

**Deuteronomy 7:1–3 → Ezra 9:1–2, 9:12** *(high confidence)*

*Source context:* the conquest law — seven nations, devoted to destruction, no covenant, no intermarriage, **because "he will turn your son away from following me"** (7:4). The stated ground is apostasy, not ancestry. `[T]`
*What it adds:* the ground Deuteronomy gives is precisely the ground Neh 13:26 will give from Solomon. The book's own logic is consistent: the danger named is the turning of the heart.

**Leviticus 18:24–30 → Ezra 9:11** *(moderate confidence)* — אֶרֶץ נִדָּה הִיא ("it is an unclean land") deploys the land-defilement logic of Lev 18, and נִדָּה is menstrual-impurity vocabulary, which is why the mistranslation into racial categories is so damaging.

**Internal (Move 4):**
- *Answers §earlier:* **9:9's גָּדֵר ("a wall in Judah")** — a metaphor in a prayer, the book's only occurrence of the word, built in stone at Neh 6:15 with a different word. `[S: overview]` *Moderate — conceptual, not verbal.*
- *Answers §earlier:* **9:9's נטה + חֶסֶד answers 7:28.** `[T]` *High.* **Sweep finding.**
- *Answers §earlier:* **9:2's "the hand of the princes was foremost" inverts the good hand of 7:6, 7:9, 8:18, 8:22, 8:31.** `[T]` *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **9:9's כִּי־עֲבָדִים אֲנַחְנוּ → Neh 9:36's הִנֵּה אֲנַחְנוּ הַיּוֹם עֲבָדִים.** The overview verified these are the only two. `[S: overview]` *High.*
- *Planted for later:* **9:3's מרט → Neh 13:25.** `[T]` *High.* **Sweep finding.**
- *Planted for later:* **9:1's list of nations → Neh 13:1, 13:23.** Ammonite and Moabite recur; Ashdodite is new at 13:23. `[T]`
- *Recurs, not resolves:* **the whole crisis returns at Neh 13:23–27**, now with Solomon named. `[S: overview]` *High.*

### 13 / 15. Copycat and Who Am I?

**Copycat — the unit's hardest work.** Walk the actors:
- **Ezra's grief (9:3–5):** *normative pattern* for a leader's response to corporate sin; the NT commends such mourning (1 Cor 5:2).
- **Ezra's prayer (9:6–15):** *normative pattern*, and note he says "our" throughout though he has just arrived.
- **Shecaniah's proposal (10:2–4):** *descriptive*. It is a layman's plan, adopted by oath; the narrator neither commends nor condemns it, and **it is not presented as a word from God**. `[T]`
- **The dismissals (10:16–44):** *descriptive only, and situationally unique*. A survival measure by a community the book also shows failing, under a covenant administration that has ended.
- **The four who opposed (10:15):** *descriptive*, and the narrator names them without a verdict. `[T]` **That the text records dissent and does not adjudicate it is itself a datum**, and a preacher should say so.

**Who Am I?** Not Ezra and not Shecaniah. The reader's place is with the assembly sitting in the December rain, מַרְעִידִים ("trembling", 10:9) — because of the matter and because of the rain. The text's own joining of those two causes in one clause is a mercy to anyone who has sat through a church meeting about sin.

### 16. So What? (brief)

The intended response is the recognition that Torah exposes before it repairs, and that the first hand it finds is the leadership's. `[I]` **What the passage does not license is a method.** Its prayer ends without a petition; its solution is proposed by a layman and executed by committee; and its final verse declines to tell us the outcome. The prayer this unit drives is confession that includes oneself in a sin one did not commit.

### Passage-specific difficulties

- **The dismissal of wives and children.** Preaching Trap 3, and the room will contain mixed marriages. The honest exegesis surfaces: (a) the category is מַעַל, cultic trespass, not ethnicity — Ruth, Rahab and the Egyptian of Deut 23:9 are in the canon; (b) the ground Deuteronomy gives is apostasy; (c) four men opposed; (d) the outcome is not stated; (e) the parallel action in Neh 13 is not divorce but an oath and a beating. **Do not flatten in either direction**, and do not resolve what 10:44 leaves open.
- **"The holy race" in both English versions.** Correct it from the pulpit.
- **Is Shecaniah's plan approved?** Genuinely open. Say so.

---
## Unit 9 — Neh 1:1–2:20 ⭐ A cupbearer's sad face

> 1:8 **זְכָר־נָא** אֶת־הַדָּבָר אֲשֶׁר צִוִּיתָ אֶת־מֹשֶׁה עַבְדֶּךָ לֵאמֹר אַתֶּם **תִּמְעָלוּ** אֲנִי אָפִיץ אֶתְכֶם בָּעַמִּים
> "Remember the word which You commanded Your servant Moses, saying, 'If you are unfaithful I will scatter you among the peoples'" (NASB95)
>
> 2:20 וְלָכֶם אֵין־חֵלֶק וּצְדָקָה **וְזִכָּרוֹן** בִּירוּשָׁלִָם
> "but you have no portion, right or memorial in Jerusalem" (NASB95)

### Headline Findings

1. **The unit opens and closes on the same root, and the book's whole ending depends on it.** Nehemiah's first prayer is זְכָר־נָא ("remember, please", 1:8); his answer to Sanballat denies him the only זִכָּרוֹן in the book (2:20); and the book's last four words are זָכְרָה־לִּי אֱלֹהַי לְטוֹבָה. `[T]` See sweep Headline Finding 4.
2. **Nehemiah's prayer names the sin the book will end committing.** He quotes Moses on מעל ("act unfaithfully", 1:8) — and מעל is the charge Nehemiah himself brings at 13:27. **Two of the verb's four occurrences in the book are these two.** `[T]` *Sweep finding.*
3. **The refusal at 2:20 matches Ezra 4:3**: each half's first opposition scene ends with a tripartite denial of standing. `[T]` *Sweep finding.*

### 2. Context — Positional Necessity Check

**Preceding movement.** Ezra ends with a list of men who had married foreign wives, and no statement of outcome (Ezra 10:44).

**Necessity answer.** Because the book's first half has repaired what could be repaired inside the sanctuary and has left the city itself unaddressed. Nehemiah's brother's report is precisely about what Ezra never mentions: **the wall broken down, the gates burned** (1:3). `[T]` **And the unit exists here, twelve years after Ezra's arrival, because the first half's crisis — an unenforceable holiness — is about to be given a physical boundary.** The book's answer to a porous people is a city with doors.

**Implication.** Neh 1–2 is not a fresh start but a second attempt at the same problem with different tools. That reading resists the leadership-manual trap at the structural level, before any application is reached.

### 3. Structure

1:1–3 the report → 1:4–11a the prayer → 1:11b the narrator's late-placed identification ("now I was cupbearer to the king") → 2:1–8 the audience with Artaxerxes → 2:9–10 arrival, and the first "when they heard" → 2:11–16 the night inspection, told to nobody → 2:17–18 the summons and the response → 2:19–20 the second "when they heard", and the refusal.

**The device is a withheld fact.** The reader is not told Nehemiah's position until the prayer is over (1:11). **Held back, it converts the prayer from a courtier's calculation into an act performed before the calculation was possible.** `[I]`, and it is the unit's best structural observation.

### 4. Linking Words

- **1:9 וְשַׁבְתֶּם … אִם־יִהְיֶה ("but if you return… though your outcasts be") — conditional**, quoted from Deut 30. The prayer's whole logic is a conditional the petitioner claims to have satisfied.
- **2:2 וָאִירָא הַרְבֵּה מְאֹד ("then I was very much afraid") — narrative aside**, and the first of ten ירא verses. See Repetition.
- **2:8 כְּיַד־אֱלֹהַי הַטּוֹבָה עָלָי ("because the good hand of my God was on me") ←for←** the king granted it.
- **2:18 וַיֹּאמְרוּ נָקוּם וּבָנִינוּ ("and they said, 'Let us arise and build'") → 2:20 וַאֲנַחְנוּ עֲבָדָיו נָקוּם וּבָנִינוּ.** The same clause twice, once from the people and once to the enemy. `[T]` *Sweep observation.*

### 7. Vocabulary

- **זכר / זִכָּרוֹן.** See Headline Finding 1 and the sweep-level finding. `[T — lemma, WLC: nine verses of the verb, all Nehemiah; one of the noun]`
- **חֶרְפָּה ("reproach", 1:3; 2:17).** Two of the book's four, and they are the complaint and the stated aim. The wall is built לֹא־נִהְיֶה עוֹד חֶרְפָּה ("that we may no longer be a reproach"). `[T]`
- **הָאִישׁ הַזֶּה ("this man", 1:11).** Nehemiah's way of referring to Artaxerxes in prayer, one clause before naming himself as the king's cupbearer. `[T]`
- **הָעֶבֶד הָעַמֹּנִי ("the Ammonite servant", 2:10, 2:19) of Tobiah.** See Move 4 — this is the sweep's most important single planting.
- **צלח ("to succeed", 1:11; 2:20).** The Hebrew root occurs in exactly two verses of the book, and they are Nehemiah's prayer and his answer to Sanballat. `[T — lemma, WLC]` **He asks God for success and then tells his enemy that God will give it.** *High.* **Sweep finding.**

**Proper-noun inventory:** Hacaliah; Chislev; Susa the capital; Hanani; Judah; Jerusalem; Moses; Nisan; Artaxerxes; Asaph keeper of the king's forest; Beyond the River; **Sanballat the Horonite; Tobiah the Ammonite servant; Geshem the Arab**; the Valley Gate, the Dragon's Well, the Refuse Gate, the Fountain Gate, the King's Pool.

**The load-bearing name is Tobiah.** Three checks:
1. *Canonical history.* He is labelled **הָעַמֹּנִי ("the Ammonite")** at his first two appearances (2:10, 2:19). The Ammonite's canonical position is fixed by **Deut 23:4** — no Ammonite may enter the assembly of the LORD, to the tenth generation. `[T — source read]`
2. *Outstanding word.* **That is precisely the verse Neh 13:1 reads aloud**, eleven chapters later, three verses before the reader learns that Tobiah has been given a room in the temple courts. `[T]` **The label planted at 2:10 is detonated at 13:1 and 13:4–8.** The narrator never joins them for us. *High confidence — the pattern is established by the text's own citation, and the identification is explicit at 13:4.* **This is the sweep's single best Move 4 finding and it is not in the overview.**
3. *Name-wordplay.* **טוֹבִיָּה means "the LORD is good"** — and the book puts the root beside the name twice: at **2:10** a man has come לְבַקֵּשׁ טוֹבָה ("to seek the good") of Israel, which grieves Tobiah; and at **6:19** the nobles recite טוֹבֹתָיו ("his good deeds") in the governor's presence. `[T]` **The book's chief domestic adversary is named "Yah is good", is grieved when good is sought, and has his own "goods" recited — in a book whose last petition is זָכְרָה־לִּי אֱלֹהַי לְטוֹבָה ("remember me, O my God, for good").** *Moderate-to-high confidence: the text itself places the root beside the name twice, which is the corroboration the hard rule requires.* **Sweep finding.**

### 8. Translations

- **2:20 NASB95 "but you have no portion, right or memorial in Jerusalem"; ESV "but you have no portion or right or claim in Jerusalem".** **The ESV loses the memory link entirely.** A preacher on the ESV will not see that Nehemiah refuses his enemy exactly what he asks God for six times. *High confidence; this is the unit's key translation note.*
- **1:8 NASB95 "If you are unfaithful"; ESV "If you are unfaithful".** Both keep it — and both then render 13:27 differently (NASB95 "acting unfaithfully", **ESV "act treacherously"**). **The ESV breaks the 1:8 → 13:27 link; the NASB95 keeps it.** *Sweep finding.*

**Pulpit divergence note:** N/A — no pulpit text declared. But note for the future: on both of this unit's load-bearing chains, **the NASB95 is the better witness and the ESV breaks the link.** That is worth knowing before an engagement at a church that uses the ESV.

**Ancient versions check.** Esdras B keeps the memory link (μνημόσυνον at 2:20, μνήσθητί μου at 5:19 and 13:14, 22, 31). At 2:20 both Greek editions read δοῦλοι αὐτοῦ **καθαροί** ("his servants, pure") where the MT has עֲבָדָיו נָקוּם ("his servants; we will arise"), so **the Greek loses the doubled "let us arise and build" of 2:18 // 2:20** while keeping it at 2:18 (Ἀναστῶμεν καὶ οἰκοδομήσωμεν). `[T — Swete and Rahlfs both checked]` **Triage: category 2** — the two editions agree, so it is a Greek-tradition reading, not a single manuscript's slip; but nothing in this sweep rests on it, and it is reported at *moderate* confidence without a position.

### 9. Tone and Feel

The unit's register is **private, and reports its own fear twice**. Nehemiah weeps, mourns, fasts and prays for days (1:4); he is "very much afraid" in the king's presence (2:2); he inspects the wall at night and tells nobody (2:12, 2:16). **The public voice does not appear until 2:17.** A sermon that begins with the vision-casting speech has cut the first thirty-one verses, which are where the man is.

Soundtrack: a single held note under silence, for the night ride.

### 10. Repetition

- **ירא ("to fear")** — the root stands in 10 verses of Nehemiah and none of Ezra. `[T — lemma, WLC]` The unit opens its account: 1:5 (the great and awesome God), 1:11 (those who delight to fear your name), 2:2 (I was very much afraid). **Both directions of the root are established here before the enemies use it as a weapon in ch. 6.**
- **שמע ("when X heard")** twice in the unit (2:10, 2:19), the second and third of the book's eight.
- **חוֹמָה ("wall")** at 1:3, 2:8, 2:13, 2:15, 2:17 — five of the book's twenty-eight, and none of them in Ezra. `[S: overview, verified there]`
- **שַׁעַר ("gate")** five times in the night ride (2:13, 2:14, 2:15) and in the request (2:8).

### 11. Quotation / Allusion — with Move 4

**Deuteronomy 30:1–4 → Neh 1:8–9** *(high confidence)*

*Source context:* the closing covenant chapter, after the blessings and curses. Its movement is: you will be scattered → you will return to the LORD with all your heart → **he will circumcise your heart** (30:6) → and then the gathering. The register is promise, addressed to a people not yet exiled.
*Book usage:* the only citation of Deut 30 in the book.
*OT-to-OT:* Deut 30 is itself the resolution of Deut 28–29's curses and is quoted back to God in the same posture by Solomon (1 Kgs 8:46–53), which is the closest structural parallel to what Nehemiah is doing.
*What it adds:* **the phrase בִּקְצֵה הַשָּׁמַיִם ("at the ends of the heavens") occurs in the Hebrew Bible only at Deut 30:4 and Neh 1:9.** `[S: overview, verified there]` The citation is certain. **And the overview's finding stands and should be preached: Nehemiah prays Deut 30:1–4 and stops one verse short of 30:6's heart-circumcision** — which is the promise the book's ending will prove was needed. *High.*

**Leviticus 26:40 (with Deut 4:27; 28:64) → Neh 1:8** *(moderate confidence)* — the words אַתֶּם תִּמְעָלוּ אֲנִי אָפִיץ אֶתְכֶם בָּעַמִּים are not a verbatim quotation of any one verse; they compress the covenant-curse formula, and מעל is the priestly term Lev 26:40 uses for the fathers' trespass. **Report as a compression, not a citation.** `[T]` for the compression.

**Internal (Move 4):**
- *Planted for later — the book's strongest planting:* **Tobiah the Ammonite (2:10, 2:19) → Neh 13:1 (Deut 23 read aloud) → 13:4–8 (Tobiah evicted).** *High.* **Sweep finding.**
- *Planted for later:* **1:8's תִּמְעָלוּ → 13:27's לִמְעֹל.** *High.* **Sweep finding.**
- *Planted for later:* **2:20's זִכָּרוֹן → 5:19; 13:14, 22, 31.** *High.* **Sweep finding.**
- *Answers §earlier:* **2:20's refusal answers Ezra 4:3's.** *High.* **Sweep finding.**
- *Planted for later:* **1:3's "the wall broken down and its gates burned with fire" → 6:15 and 7:1**, item by item. `[S: overview]` *High.*
- *Planted for later:* **2:8's "the good hand of my God" → 2:18**, and back to Ezra 7:9; 8:18. `[T]`

### 13 / 15. Copycat and Who Am I?

**Copycat — Preaching Trap 1 lives here.** Walk it:
- **The prayer (1:4–11):** *normative pattern.* Confession that includes the petitioner ("I and my father's house have sinned") and argument from God's own word.
- **The night inspection (2:11–16):** *descriptive.* It is good practice; it is not a command, and the text's interest is in the secrecy, not the survey.
- **The speech (2:17–18):** *descriptive*, and the grounds given are two: the state of the city, and the hand of God. **Not a vision.** `[T]`
- **The refusal (2:19–20):** *descriptive*, and its warrant is theological ("the God of heaven will give us success"), not strategic.

**Who Am I?** Not Nehemiah, and the book will make that unmistakable by ch. 13. The reader's place is with the people who said נָקוּם וּבָנִינוּ and then strengthened their hands.

### 16. So What? (brief)

The intended response is prayer that argues from God's word and then acts without announcing itself. `[I]` The worldview note is the hardest: Nehemiah's plan is formed in four months of prayer (Chislev to Nisan, 1:1 and 2:1) and executed in one conversation. The prayer this unit drives is for the four months, not the conversation.

### Passage-specific difficulties

- **The leadership sermon.** Name the trap out loud. The corrective is structural: the man of ch. 2 is dismantled in ch. 13 by the same narrator.
- **"The good hand of my God."** A congregation will hear a success formula. It is used of Ezra's uneventful journey and of Nehemiah's timber requisition, and it is never used of an outcome the leader engineered.

---

## Unit 10 — Neh 3:1–4:23 (MT 3:1–38; 4:1–17) Builders, and the men who laughed

### Headline Findings

1. **Chapter 3 is a register of the verb חזק.** הֶחֱזִיק ("repaired") occurs in 28 verses of the chapter — the single densest concentration of any word in the book — and the same root is what Nehemiah prays for at 6:9 and what the enemies aim to prevent. `[T]`
2. **The register names goldsmiths, perfumers, and a man's daughters** (3:8, 3:12). `[T]` The wall was built by trades and by a family, not by masons.
3. **The opposition's two speeches are quoted in full and are both about stones** (3:34–35 MT): "will they revive the stones from the heaps of rubble, burned as they are?" and "if a fox should jump on it, he would break their stone wall". `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** A public commitment: "Let us arise and build" (2:18).

**Necessity answer.** Because a commitment must be assigned. **The chapter exists here because the book's method is to show the document**: the reader is given the work-allocation before any work is described, in the same way he was given the register before the altar. `[T]` And 3:33 (Eng 4:1) opens with the fourth "when Sanballat heard" — **opposition again triggered by visible progress.**

**Implication.** Ch. 3 is not a list to be skipped on the way to ch. 4; it is the answer to ch. 2, and ch. 4 is the answer to ch. 3.

### 3. Structure

3:1–32 the register, running anticlockwise from the Sheep Gate and back to it → 3:33–38 (Eng 4:1–6) mockery, Nehemiah's imprecation, and the wall to half its height → 4:1–9 (Eng 4:7–15) the conspiracy and the response → 4:10–17 (Eng 4:16–23) the divided workforce, the trumpet, and the clothes not taken off.

**The register is an inclusio in stone:** it begins at שַׁעַר הַצֹּאן ("the Sheep Gate", 3:1) and ends at it (3:32). `[T]` **The wall's literary shape is the wall's physical shape.**

### 4. Linking Words

- **3:5 וְאַדִּירֵיהֶם לֹא־הֵבִיאוּ צַוָּרָם ("but their nobles did not put their necks to the work") — contrast.** The chapter's one editorial sting, in a list.
- **4:4 (Eng 4:10) כָּשַׁל כֹּחַ הַסַּבָּל ("the strength of the burden-bearers is failing") — the internal complaint**, placed between two external threats.
- **4:14 (Eng 4:20) אֱלֹהֵינוּ יִלָּחֶם לָנוּ ("our God will fight for us") — the ground**, and the only theological sentence in the military section.

### 7. Vocabulary

- **חזק.** 28 verses in ch. 3 of the book's 39. `[T — lemma, WLC]` **The English "repaired" conceals that this is the same word as "strengthen my hands" (6:9) and "strengthened their hands" (2:18).** Both NASB95 and ESV use "repaired" throughout ch. 3, which is the right rendering and which breaks the chain. *Tool 8 note.*
- **מְלָאכָה ("the work").** 20 verses in Nehemiah, and **eight of them in chs. 4–6** (4:5, 4:9, 4:10, 4:11, 4:13, 4:15, 4:16; 6:3, 6:9, 6:16). `[T]` The book's name for the project.
- **פרץ ("to break through") and פֶּרֶץ ("breach").** The verb at 1:3, 2:13, 3:35, 4:1; the noun at 6:1 only. `[T — lemma, WLC]` **And Neh 2:13's occurrence is a ketiv** (המפרוצים, printed unpointed), so a surface search for the pointed form misses it. The lemma index has it. **A live instance of Phase 10.5 (e3) in this very unit.**
- **נַעַר ("servant, young man").** 8 verses, all Nehemiah: 4:10, 4:16, 4:17; 5:10, 5:15, 5:16; 6:5; 13:19. `[T]` **Nehemiah's own men, and the last thing he does with them is post them at the gates on the Sabbath (13:19).**

**Proper-noun inventory:** some forty-five builders and their fathers, plus Jericho, Tekoa, Gibeon, Mizpah, Zanoah, Beth-haccherem, Beth-zur, Keilah; the gates; the towers of Hananel and Hammeah; the Ophel; Sanballat, Tobiah, the Arabs, Ammonites, Ashdodites. **Two carry freight.** **"The men of Jericho" (3:2)** are the second name in the register — the city under Joshua's curse (Josh 6:26) whose rebuilder lost his sons (1 Kgs 16:34) — now rebuilding Jerusalem's wall. `[T — source narratives re-read]` *Moderate confidence on the irony; the narrator does not flag it, and the town is simply the next on the list.* **"The Tekoites" (3:5, 3:27)** appear twice, once with the note about their nobles and once doing a second section — **the only group in the register both criticised and shown doing extra.** `[T]` That is a fine pastoral detail and it is in the text, not in the interpreter.

### 8. Translations

NASB95 and ESV agree substantively throughout. One note: **NASB95 3:12 "he and his daughters"; ESV "he and his daughters"** — both keep it, and both are right to; the Hebrew is הוּא וּבְנוֹתָיו. A congregation should hear it.

**Pulpit divergence note:** N/A — no pulpit text declared.

**Ancient versions check.** Esdras B renders the register closely and transliterates heavily. No split of consequence.

### 9. Tone and Feel

Two registers, abutted without transition: **the flat administrative cadence of ch. 3**, thirty-two verses of "next to him repaired", and then **mockery, imprecation, and armed anxiety**. The effect of the flatness is cumulative — by v. 32 the reader has walked the whole circuit — and the mockery lands on a reader who has just been shown how much ordinary work it cost.

### 10. Repetition

- **הֶחֱזִיק** — 28 verses, and **the formula varies just enough to be noticed**: עַל־יָדוֹ ("next to him"), עַל־יָדָם ("next to them"), אַחֲרָיו ("after him"), נֶגֶד בֵּיתוֹ ("opposite his house", 3:10, 3:23, 3:28, 3:29).
- **נֶגֶד בֵּיתוֹ ("opposite his house")** four times. `[T]` **The register's repeated note is that people built the bit in front of where they lived.** That is the chapter's application and it is textual.
- **מִדָּה שֵׁנִית ("a second section")** at 3:11, 3:19, 3:20, 3:21, 3:24, 3:27, 3:30 — seven times.
- **שַׁעַר ("gate")** through the circuit; **דֶּלֶת ("door")** at 3:1, 3:3, 3:6, 3:13, 3:14, 3:15.

### 11. Quotation / Allusion — with Move 4

No external OT citation. **Move 2:** Deuteronomy, the book's live source, is not invoked — and the one theological claim in the military section, אֱלֹהֵינוּ יִלָּחֶם לָנוּ (4:14), is **the language of the holy-war formula** (Exod 14:14; Deut 1:30; 3:22; 20:4). `[T]` *Moderate-to-high confidence as a conceptual allusion: the formula is distinctive and the setting is a defence of the people.* **Worth naming: the one time Nehemiah speaks theologically about the fighting, he uses conquest vocabulary in a book with no conquest.**

**Internal (Move 4):**
- *Answers §earlier:* **the register of ch. 3 answers 1:3's complaint gate by gate**, and the doors that 1:3 says were burned are hung in 3:1, 3:3, 3:6, 3:13, 3:14, 3:15. *High.*
- *Answers §earlier:* **3:33 (Eng 4:1) is the fourth "when X heard"**, continuing the refrain from Ezra 4:1. *High.*
- *Planted for later:* **the doors (דֶּלֶת, 11 verses, all Nehemiah) → 13:19**, where the last use is shutting them against Sabbath trade. `[T]` *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **3:36–37 (Eng 4:4–5), Nehemiah's imprecation** — "turn their reproach on their own head… do not forgive their iniquity" — which is the first of the book's two "remember *them*" prayers (with 6:14 and 13:29). `[T]`
- *Planted for later:* **3:1's Eliashib the high priest** → 13:4–7, where an Eliashib prepares Tobiah's chamber, and 13:28, where his grandson marries Sanballat's daughter. `[T]` **The man who consecrates the Sheep Gate in ch. 3 is the man whose house is compromised in ch. 13.** *Moderate-to-high.* **Sweep finding.**

### 13. Copycat

**Preaching Trap 2 lives here.** The register is *descriptive*, and the temptation to allegorise it ("rebuild the broken walls in your life") is the single most common misuse of this book. The corrective is the detail: **goldsmiths and perfumers and a man's daughters built the section in front of their own houses.** That is more interesting, and more usable, than the allegory — and it is prescriptive at the level of the underlying virtue (*normative pattern*), not of the wall.

### 16. So What? (brief)

The response sought is the ordinary one: build the bit in front of your house, alongside people whose trade is not yours. `[I]` The motivation the text supplies is not the project but 4:14 — God will fight for us — and the honest note is that the chapter's fear is real and is never said to be groundless.

### Passage-specific difficulties

- **The allegorised wall.** Name it.
- **Nehemiah's imprecation (3:36–37 / Eng 4:4–5).** "Do not forgive their iniquity." A congregation will find it sub-Christian. Do not soften it into a wish for justice; it is an imprecatory prayer of the same family as Ps 69 and 109, and it belongs to a man under threat, recorded without comment.
- **The versification.** Anyone comparing Bibles mid-sermon will be lost. Say once, early, that chapters 3–4 are numbered differently in the Hebrew.

---

## Unit 11 — Neh 5:1–19 ⭐ The debt that had to be cancelled

> 5:7 וָאָרִיבָה אֶת־הַחֹרִים וְאֶת־הַסְּגָנִים … וָאֶתֵּן עֲלֵיהֶם **קְהִלָּה גְדוֹלָה**
> "I contended with the nobles and the rulers … and I held a great assembly against them." (NASB95)

### Headline Findings

1. **The word Nehemiah uses for the assembly he convenes against the nobles occurs in only one other verse in the Hebrew Bible — Deut 33:4, "the assembly of Jacob", to whom Moses gave the Torah.** `[T — verified across all 23,213 WLC verses]` **This is the sweep's strongest single lexical find and it is not in the overview.**
2. **The chapter is the book's only internal crisis**, and it interrupts the building. Chapters 4 and 6 are about enemies; 5 is about brothers.
3. **"The fear of God" is the chapter's stated ground, twice** (5:9, 5:15), and the noun יִרְאָה occurs nowhere else in the book. `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** A workforce split between building and guard duty, working from dawn to starlight, not taking off its clothes (4:15–17 MT).

**Necessity answer.** Because that is what caused it. **The outcry of 5:1 is a consequence of the building programme**: men conscripted to a wall are not farming, and 5:2–4 gives three distinct grievances — no grain, mortgaged fields, borrowed money for the king's tax. **The chapter exists here because the wall's cost fell on the poor, and the narrator puts it between the two attack narratives so it cannot be read as an aside.** `[T]` for the grievances; `[I]`, high confidence, for the causal reading.

**Implication.** The most dangerous threat to the project in this book is the project's own economics. A series that treats ch. 5 as a digression has missed the author's placement.

### 3. Structure

5:1–5 the outcry, in three voices → 5:6–7a Nehemiah's anger and his deliberation (וַיִּמָּלֵךְ לִבִּי עָלַי, "my heart consulted itself") → 5:7b–11 the confrontation and the demand → 5:12–13 the oath, the priests, and the shaken garment → 5:14–18 the governor's own practice over twelve years → 5:19 the first "remember me".

**The device is a retrospective appended to a scene.** 5:14–18 covers twelve years and is out of sequence with the narrative around it. `[T]` It is there to establish that the demand of 5:11 was made by a man who had already forgone his own entitlement.

### 4. Linking Words

- **5:5 וְעַתָּה ("and now") — pivot** from the three complaints to their shared logic: כִּבְשַׂר אַחֵינוּ בְּשָׂרֵנוּ ("our flesh is like the flesh of our brothers").
- **5:9 הֲלוֹא ("should you not…?") — rhetorical question** carrying the ground: בְּיִרְאַת אֱלֹהֵינוּ תֵּלֵכוּ ("walk in the fear of our God").
- **5:9 מֵחֶרְפַּת הַגּוֹיִם אוֹיְבֵינוּ ("because of the reproach of the nations, our enemies") ←for←** — **the internal sin is argued from its external witness.** `[T]`
- **5:15 מִפְּנֵי יִרְאַת אֱלֹהִים ("because of the fear of God") ←for←** Nehemiah's own abstention.

### 7. Vocabulary

- **קְהִלָּה ("assembly", 5:7).** **Two occurrences in the Hebrew Bible: Deut 33:4 and here.** `[T — lemma, WLC, whole-canon]` Deut 33:4 reads תּוֹרָה צִוָּה־לָנוּ מֹשֶׁה מוֹרָשָׁה קְהִלַּת יַעֲקֹב ("Moses commanded us a law, a possession for the assembly of Jacob"). **The single other assembly in Scripture to bear this name is the one that received the Torah as an inheritance — and Nehemiah convenes his against men who are foreclosing on inheritances.** *High confidence on the lexical fact; moderate-to-high on the allusion, since the word is rare enough that coincidence is unlikely and the subject-matter (מוֹרָשָׁה, "possession") coheres.* **Sweep finding; add to the overview's intertextual map and to *Presupposes*.**
- **מַשָּׁא ("exaction, burden", 5:7, 5:10) and נשׁה ("to lend on interest", 5:7, 5:10, 5:11).** The chapter's legal vocabulary.
- **יִרְאַת אֱלֹהִים ("the fear of God", 5:9, 5:15).** The noun's only two occurrences in the book; the related adjective describes Hananiah at 7:2 (יָרֵא אֶת־הָאֱלֹהִים מֵרַבִּים, "feared God more than many"). `[T]` **The book's three explicit fear-of-God statements are all about administration** — lending, the governor's table, and who holds the keys of the city.
- **נַעַר ("my servants", 5:10, 5:15, 5:16).** See unit 10.

**Proper-noun inventory:** Judah; Artaxerxes; the nations round about. Sparse by this book's standards — **the chapter names no opponent**, which is itself the point.

### 8. Translations

- **5:10 NASB95 "And likewise I, my brothers and my servants are lending them money and grain. Please, let us leave off this usury."** ESV: "Moreover, I and my brothers and my servants are lending them money and grain. Let us abandon this exacting of interest." **Both make Nehemiah an active lender.** The overview's claim audit flagged the import's phrase "confesses his own predatory lending" as **overstated**, and the sweep agrees: the Hebrew נֹשִׁים בָּהֶם כֶּסֶף וְדָגָן says they are lending, and the next clause proposes abandoning **הַמַּשָּׁא הַזֶּה ("this exaction")** — which may be the interest or the claim itself. **The text does not say Nehemiah was charging interest.** Preach the ambiguity, not the confession. *Moderate confidence; this is a genuine crux.*
- **5:7 NASB95 "a great assembly"; ESV "a great assembly".** Neither can signal the rarity of the word. Tell the congregation.

**Ancient versions check.** Esdras B renders 5:10's ἐγκαταλίπωμεν δὴ τὴν ἀπαίτησιν ταύτην ("let us abandon this exaction") — **and note it uses the ἐγκαταλείπω that carries the book's forsaking-chain** (sweep Headline Finding 1). `[T]` The Hebrew is indeed עזב here (Neh 5:10, one of the twelve). **So the chapter's demand is made in the book's covenant-verb: *let us forsake this exaction*, in a book where forsaking the house of God is the final charge.** *Moderate — the sense is different, but the lexeme is the same and both editions of the Greek agree.* **Sweep observation.**

### 9. Tone and Feel

**Anger, and the book says so.** וַיִּחַר לִי מְאֹד ("I was very angry", 5:6) — and the same clause stands at 13:8 (וַיֵּרַע לִי מְאֹד) and, of the enemies, at 3:33 and 4:1. `[T]` The register is prophetic rather than administrative: a rebuke, a demand for restitution, a symbolic act (the shaken garment, 5:13), a congregational Amen.

### 10. Repetition

- **אָח ("brother")** five times in 5:1–8 — the chapter's argument is entirely kinship.
- **בָּנֵינוּ וּבְנֹתֵינוּ ("our sons and our daughters")** at 5:2, 5:5 ×2 — and the daughters are being taken.
- **שָׂדוֹת וּכְרָמִים ("fields and vineyards")** at 5:3, 5:4, 5:5, 5:11.
- **לֶחֶם הַפֶּחָה ("the governor's food allowance")** at 5:14, 5:18.

### 11. Quotation / Allusion — with Move 4

**Deuteronomy 33:4 → Neh 5:7** *(moderate-to-high confidence)* — see Vocabulary. Move 1: Deut 33 is the blessing of Moses, and v. 4 is its opening declaration that the Torah is the assembly's מוֹרָשָׁה ("inheritance, possession"). Move 2: Deuteronomy is the book's most-used source, though this chapter of it is not used elsewhere. Move 3: Deut 33:4 and the Jubilee/redemption laws (Lev 25:23–28) are already in conversation about inalienable possession. **What it adds:** the assembly Nehemiah convenes is named with the word for the assembly that received the land-law, against men breaking it.

**Exodus 22:24; Leviticus 25:35–37; Deuteronomy 23:20–21 → Neh 5:7–11** *(high confidence as a legal background, moderate as citation)* — the three interest laws. **Nehemiah quotes none of them.** `[T]` He argues from kinship (5:5), from the fear of God (5:9), and from the watching nations (5:9). **That is a finding: the book's most successful reform is the one argued without a proof-text.**

**Internal (Move 4):**
- *Planted for later:* **5:19's זָכְרָה־לִּי אֱלֹהַי לְטוֹבָה → 13:31**, the identical clause as the book's last words. `[S: overview, verified there]` *High — an inclusio around the governor's twelve years.*
- *Answers §earlier:* **5:9's "the reproach of the nations" answers 1:3 and 2:17.** The reproach the wall was built to remove is being generated internally. `[T]` *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **5:13's congregational אָמֵן → 8:6's אָמֵן אָמֵן.** The book's only two. `[T]` *Moderate.*
- *Planted for later:* **5:12's oath administered by priests → 10:1–30's signed covenant and 13:25's oath.** Three oaths, and the last one is imposed with violence. `[T]` *Moderate-to-high.* **Sweep finding.**

### 16. So What? (brief)

The response sought is the cancellation, and its ground is the fear of God argued in front of watching outsiders. `[I]` **For the church, the transferable point is the placement**: the chapter sits between two attacks and insists that the community's treatment of its own poor is a defence question. The prayer is for the nerve of 5:11 among people one needs.

### Passage-specific difficulties

- **Does Nehemiah confess to usury?** Genuinely ambiguous (above). Do not resolve it to make him better or worse.
- **Debt-slavery of daughters (5:5).** The text says וְיֵשׁ מִבְּנֹתֵינוּ נִכְבָּשׁוֹת ("and some of our daughters are forced into bondage"). Do not pass over it; the room may contain people for whom this is not ancient.
- **5:19 immediately after the reform.** A man who has just listed his own generosity asks God to remember it. The book will do this four times and will end on it. **Name the awkwardness now**, so that 13:22's appeal to mercy lands later.

---

## Unit 12 — Neh 6:1–7:5 Fifty-two days

### Headline Findings

1. **The enemies' whole strategy is named with one root, and it is the root Nehemiah's half of the book runs on.** ירא ("to fear") stands in 10 verses of Nehemiah, and four of them are here: 6:9, 6:13, 6:14, 6:19 — all of מְיָרְאִים ("making [us] afraid"). `[T]`
2. **6:9 puts both poles of the book's hand-vocabulary in one verse:** "their hands will drop from the work" (רפה) and "strengthen my hands" (חזק). `[T]` *Sweep finding.*
3. **The wall's completion is credited to God by the enemies**, not by Nehemiah: 6:16 — וַיֵּדְעוּ כִּי מֵאֵת אֱלֹהֵינוּ נֶעֶשְׂתָה הַמְּלָאכָה הַזֹּאת. `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** The wall is at half height (3:38 MT), the workforce is armed, and the internal economic crisis has been settled by oath.

**Necessity answer.** Because the external campaign, having failed at mockery (3:33–35) and at conspiracy (4:1–2), must now try the one thing left: **the leader personally.** `[T]` Four invitations to Ono, a fifth with an open letter, a hired prophet, and a correspondence network inside Judah. **The unit exists here because a wall nearly finished cannot be stopped by force and can still be stopped by discrediting the man who is building it.**

**Implication.** The threat escalates inward — from the work, to the workers, to the leader's reputation, to the leader's piety (6:10–13). That escalation is the unit's structure and its application.

### 3. Structure

6:1–4 the four invitations and the four refusals → 6:5–9 the open letter and the prayer → 6:10–14 the hired prophet and the discernment → 6:15–16 completion in fifty-two days, and the enemies' verdict → 6:17–19 the correspondence with Tobiah → 7:1–5a the appointments, and the city's emptiness → 7:5b the finding of the register.

**The device is a countdown interrupted.** The unit's spine is a sequence of attempts (four, then a fifth, then a prophet), and the completion notice (6:15) arrives in a single verse between the last attempt and the enemies' reaction.

### 4. Linking Words

- **6:3 לָמָּה תִשְׁבַּת הַמְּלָאכָה ("why should the work stop?") — rhetorical question** as the whole answer. **Note what the refusal is *not*:** it is not "I am too important", it is "the work would stop".
- **6:9 כִּי ("for") ←for←** — the reason they were all doing it, stated before the prayer.
- **6:12 כִּי ("for") ←for←** — the discernment: *because* he spoke the prophecy against me, *and* Tobiah and Sanballat had hired him.
- **6:13 לְמַעַן … לְמַעַן … לְמַעַן ("in order that… in order that… in order that") — three purpose clauses stacked** in one verse: hired *in order that* I should be afraid and do so and sin, and it would be to them for an evil name, *in order that* they might reproach me. `[T]` The densest purpose-chain in the book.

### 7. Vocabulary

- **מְיָרְאִים ("making afraid", 6:9, 6:14, 6:19).** `[T — lemma, WLC]` **The enemies' method has a name, and it is the book's own word for what is owed to God.**
- **חַזֵּק אֶת־יָדָי ("strengthen my hands", 6:9).** See Headline Finding 2.
- **הַאִישׁ כָּמוֹנִי יִבְרָח ("should a man like me flee?", 6:11).** And the second clause — וּמִי כָמוֹנִי אֲשֶׁר־יָבוֹא אֶל־הַהֵיכָל וָחָי ("and who is there like me that would go into the temple to save his life?") — **is a layman's scruple about the sanctuary.** `[T]` Nehemiah refuses to enter the הֵיכָל; in ch. 13 he throws furniture out of a temple chamber. The two scenes are worth holding together, and the difference is between entering the holy place and cleansing an outbuilding.
- **פֶּרֶץ ("breach", 6:1).** The noun's only occurrence in the book; the verb stood at 1:3, 2:13, 3:35, 4:1. `[T]` **The word that described the city's ruin is used once more, to say there is none.**
- **כְּאִישׁ אֱמֶת ("a faithful man", 7:2) and יָרֵא אֶת־הָאֱלֹהִים מֵרַבִּים ("feared God more than many").** The book's only character reference. `[T]`

**Proper-noun inventory:** Sanballat, Tobiah, Geshem/Gashmu, the plain of Ono, Shemaiah son of Delaiah son of Mehetabel, Noadiah the prophetess, Hanani, Hananiah the commander of the citadel, Elul, Shecaniah son of Arah, Jehohanan son of Meshullam son of Berechiah. **Two matter.** **Noadiah the prophetess (6:14)** is one of only a handful of named female prophets in the Hebrew Bible, and she is on the wrong side; **Meshullam son of Berechiah (6:18)**, whose daughter married Tobiah's son, is one of the builders of ch. 3 (3:4, 3:30). `[T]` **A man who repaired two sections of the wall is father-in-law to the enemy's son.** *High confidence on the identification — the full patronymic matches.* **Sweep finding.**

### 8. Translations

- **6:9 NASB95 "They will become discouraged with the work"; ESV "Their hands will drop from the work".** **The ESV is the better witness here** — it keeps the hand-idiom that the second half of the verse ("strengthen my hands") answers. One of the few places in the book where that is so. *High confidence; this is the unit's key translation note.*
- **6:11 NASB95 "Should a man like me flee? And could one such as I go into the temple to save his life?"; ESV "Should such a man as I run away? And what man such as I could go into the temple and live?"** Both preserve the scruple.

**Pulpit divergence note:** N/A — no pulpit text declared. For the record: at 6:9 the ESV shows the finding and the NASB95 does not; at 2:20 and 13:27 the reverse. **Neither version is uniformly the better witness in this book**, which is itself worth telling a preacher.

**Ancient versions check.** No split of consequence.

### 10. Repetition

- **כַּדָּבָר הַזֶּה ("in this manner")** four times in 6:4–8 — the formula for the repeated exchange.
- **שלח ("to send")** through 6:2–8 — six times; the whole episode is conducted by messenger.
- **ירא** four times (above).
- **חוֹמָה** at 6:1, 6:6, 6:15; 7:1.

### 11. Quotation / Allusion — with Move 4

No external citation. **Move 2:** the book's live Deuteronomy source is absent again — **the whole of Neh 3–7 quotes no Scripture at all** — no occurrence of תּוֹרָה, no כַּכָּתוּב, and the name of Moses absent from those five chapters (it stands at Neh 1:7, 1:8; 8:1, 8:14; 9:14; 10:30; 13:1 and nowhere between). `[T — lemma, WLC]` A real observation about the building narrative, and it sharpens the contrast with ch. 8.

**Internal (Move 4):**
- *Answers §earlier:* **6:15's completion answers 1:3 item by item**, and 7:1's hanging of the doors answers "its gates are burned with fire". `[S: overview]` *High.*
- *Answers §earlier:* **6:1's "no breach was left in it" answers 1:3's מְפֹרָצֶת and 2:13's ketiv form.** `[T]` *Moderate-to-high.* **Sweep finding.**
- *Answers §earlier:* **6:16's "they fell greatly in their own eyes" inverts Ezra 3:3's "they were in dread because of the peoples of the lands".** `[I]`, *moderate*.
- *Answers §earlier:* **6:9's "their hands will drop" answers Ezra 4:4's "weakening the hands of the people of Judah".** `[T]` *High.* **Sweep finding.**
- *Planted for later:* **6:6's slander אַתָּה הֹוֶה לָהֶם לְמֶלֶךְ ("you are to be their king")** — the only time kingship is named in the book, and it is a lie. `[S: overview]` *High.*
- *Planted for later:* **6:17–19's Tobiah correspondence → 13:4–8.** The network inside Judah is what makes the temple chamber possible. `[T]` *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **7:5's "and I found the book" → the register of ch. 7 and the Torah of ch. 8.** `[T]` *High.*

### 13 / 15. Copycat and Who Am I?

**Copycat.** 6:3 ("I am doing a great work and cannot come down") is the book's most-quoted verse and the overview names it as where Trap 1 bites worst. **Its status is *descriptive with a stated reason*** — the reason is that the work would stop, not that the leader is above meeting people. **Preach the reason or do not preach the verse.**
6:10–13 is *normative pattern* at the level of the underlying discernment: a spiritual counsel that urges sin (entering the sanctuary) is identified as not from God by its content, not by its packaging. `[T]`

**Who Am I?** Not Nehemiah. The reader's place in 6:17–19 is with the nobles of Judah, who were bound to Tobiah by oath and marriage and were reporting both ways.

### 16. So What? (brief)

The response sought is the refusal of a meeting that would stop the work, and the discernment of counsel that recommends sin. `[I]` The motivation is 6:16 — the outcome is God's, and it was the enemies who said so. The prayer is 6:9's, which is four words long.

### Passage-specific difficulties

- **"I am doing a great work."** Named above.
- **Nehemiah's prayer against Tobiah and Sanballat (6:14).** The second of the "remember them" prayers.
- **Was Shemaiah a real prophet?** 6:12 says Nehemiah perceived God had not sent him. The text gives the perception, not a test. Do not manufacture a method from it.

---

## Unit 13 — Neh 7:6–73 (MT 7:6–72) The book he found

### Headline Findings

1. **The register is introduced as a rediscovery, not a record.** 7:5 — וָאֶמְצָא סֵפֶר הַיַּחַשׂ ("and I found the book of the genealogy"). `[T]` The book's habit: do a thing, then find it written, then do it again.
2. **The closing bracket of the book's frame.** Ezra 2 and Neh 7 are the same document, 69% identical at word level on a skeletal comparison. `[S: overview, verified there]`
3. **The MT has no equivalent of the English Neh 7:68**, which is why Hebrew Nehemiah has 405 verses against the English 406 — and why the NASB95 export parses to **686** verses against the WLC's **685**. `[T — both counts made independently in this sweep]`

### 2. Context — Positional Necessity Check

**Preceding movement.** The wall is finished, the doors hung, the gatekeepers appointed — and 7:4 states the problem the wall has created: וְהָעִיר רַחֲבַת יָדַיִם וּגְדוֹלָה וְהָעָם מְעַט בְּתוֹכָהּ ("now the city was large and spacious, but the people in it were few").

**Necessity answer.** Because a wall around an empty city is a liability, and repopulating it requires knowing who has a claim. **The register is produced here as an instrument of settlement policy**, and ch. 11 will draw on it by lot. `[T]` The passage exists here for the same reason Ezra 2 exists where it does: nothing is done until everyone is named.

**Implication.** The re-reading is not nostalgia. The community is about to be redistributed, and the document is the warrant.

### 3. Structure

Identical in shape to Ezra 2: laypeople → priests → Levites, singers, gatekeepers → temple servants → those who could not prove descent → totals → offerings → settlement (7:72 MT), which then runs straight into 8:1.

### 7. Vocabulary

- **סֵפֶר הַיַּחַשׂ ("the book of the genealogy", 7:5).** The noun יַחַשׂ occurs once in the book; the verb התיחש at Ezra 2:62; 8:1, 3; Neh 7:5, 7:64. `[T]`
- **הַתִּרְשָׁתָא** at 7:65, 7:69 — and again at 8:9 and 10:2, where it is attached to Nehemiah's name.

### 8. Translations

**7:65 NASB95 "until a priest arose with Urim and Thummim"; Ezra 2:63 "until a priest stood up with Urim and Thummim".** **The NASB95 varies its English where the Hebrew is identical** (עֲמֹד in both). The ESV varies more (see unit 2). **The book's one unanswered question is asked twice in identical Hebrew and is slightly different in English both times.** *Tool 8 finding; tell the preacher.*

**Ancient versions check.** **Swete prints the verse number 7:68 with nothing after it** — Vaticanus lacks the line too. `[S: overview, verified there]` **Triage: category 2** for the MT's absence of the horses-and-mules line, and it explains a versification difference a congregation may notice between Bibles. Not otherwise consequential.

### 10. Repetition

The register's own formulae, and **the numerals, which differ from Ezra 2 in most entries while both texts state the same total of 42,360.** `[S: overview, verified there]` **The narrator prints two documents that disagree and comments on neither.**

### 11. Quotation / Allusion — with Move 4

No external citation. **Move 2: not applicable.**

**Internal (Move 4):**
- *Replants:* **the whole register answers Ezra 2:1–70.** `[S: overview]` *High.*
- *Replants — and left open:* **7:65 // Ezra 2:63**, the Urim deferral, unanswered. `[S: overview]` *High.*
- *Answers §earlier:* **7:64's "they were not found" repeats Ezra 2:62's, and 7:5's "I found the book" is the book's positive answer to it.** מצא runs through Ezra 2:62; 8:15; Neh 5:8; 7:5; 7:64; 8:14; 13:1. `[T — lemma, WLC]` **What cannot be found is a priesthood; what is found is a book.** *Moderate-to-high.* **Sweep finding, and the strongest reason to preach this unit rather than skip it.**
- *Planted for later:* **7:72's settlement notice runs into 8:1's assembly** without a narrative break in the Hebrew. See the contested seam, below.

### 16. So What? (brief)

The response sought is a community willing to be counted twice and to have its unresolved cases restated rather than quietly dropped. `[I]` The church application is uncomfortable and exact: the second reading of the register does not fix the problem the first one found.

### Passage-specific difficulties

- **The contested seam.** Some divide the book at 7:72/8:1, making the Torah-reading the start of a third block; others at 6:15. **The overview takes the register as the seam and flags the alternative as live, at moderate confidence.** *The sweep's verdict:* the seam is **best left contested, and the sweep's own evidence slightly favours the overview.** The register is introduced as *found* (7:5) and functions administratively toward ch. 11's lot; the assembly of 8:1 is narrated in the third person and brings Ezra back on stage, which reads as a new movement — but **the settlement notice of 7:72 and the assembly of 8:1 are joined by the same וַיִּגַּע הַחֹדֶשׁ הַשְּׁבִיעִי clause that opens Ezra 3:1**, so the Hebrew gives no clean break. `[T]` **Report as contested; do not resolve.** A solo dig on Neh 7–8 should test it.
- **Preaching a repeated list.** The overview's advice stands: preach it alongside Ezra 2 or not at all — but if it is preached, the "found / not found" thread is the reason to.

---

## Unit 14 — Neh 8:1–18 ⭐ The book opened

> 8:10 … כִּי־**חֶדְוַת יְהוָה** הִיא **מָעֻזְּכֶם**
> "for the joy of the LORD is your strength." (NASB95)

### Headline Findings

1. **"The joy of the LORD is your strength" is built from a noun that occurs twice in the Hebrew Bible — here and at 1 Chr 16:27, where it stands beside עֹז, the other strength-word.** `[T — verified by lemma across the whole WLC; gated with find.py verify, exit 0]` **The slogan's vocabulary comes from David's psalm at the bringing-up of the ark.** *Sweep finding; not in the overview.*
2. **The chapter is the densest concentration of "understanding" in the book.** בין stands in 10 verses of Ezra–Nehemiah and **six of them are here** (8:2, 3, 7, 8, 9, 12). `[T]`
3. **The people weep when they understand, and are told to stop** — and the reason given has a meal attached. `[T]`

### 2. Context — Positional Necessity Check

**Preceding movement.** A wall, a register found, a city to be filled.

**Necessity answer.** Because the seventh month has come (7:72b) — the same trigger as Ezra 3:1 — and because the community has just been re-constituted by a document and must now be re-constituted by a different one. **The passage exists here because the book's argument is that a city with doors is not yet a people, and what makes a people is a book read aloud.** `[I]`, high confidence.

**Implication.** Neh 8 is the answer to Neh 1–7, not an appendix to it. Everything built so far has been physical; this is the first thing built that cannot be breached.

### 3. Structure

8:1–3 the request, the bringing, the reading → 8:4–6 the platform, the opening, the blessing and the Amen → 8:7–8 the Levites giving understanding → 8:9–12 the weeping and the command to feast → 8:13–15 the second day and what was found written → 8:16–18 Booths kept, and the comparison with Joshua.

**The device is a sequence of days** (8:2 "the first day"; 8:13 "the second day"; 8:18 "day by day, from the first day to the last"). The chapter's shape is a festival week.

### 4. Linking Words

- **8:9 כִּי ("for") ←for←** the command not to mourn is grounded in the day's holiness.
- **8:10 כִּי … כִּי ("for… for") ←for←** twice: the day is holy to our Lord, **and** the joy of the LORD is your strength. **The second is the ground of the first command, not a general maxim.** `[T]`
- **8:12 כִּי ("for") ←for←** — the reason for the great rejoicing: כִּי הֵבִינוּ בַּדְּבָרִים ("because they understood the words"). **Joy is grounded in comprehension, not in atmosphere.** `[T]`
- **8:17 כִּי ("for") ←for←** the joy was very great *because* they had not done so since the days of Joshua.

### 7. Vocabulary

- **חֶדְוָה ("joy", 8:10).** **Two occurrences in the Hebrew Bible: 1 Chr 16:27 and here.** `[T — verified across all 23,213 WLC verses]` 1 Chr 16:27 reads הוֹד וְהָדָר לְפָנָיו עֹז וְחֶדְוָה בִּמְקֹמוֹ ("splendour and majesty are before Him, strength and joy are in His place"), in David's psalm at the installation of the ark. **Both occurrences pair חֶדְוָה with a strength-word.** Neh 8:10 uses מָעוֹז, its only occurrence in the book. `[T]` *High confidence on the lexical data; moderate-to-high on the allusion — the noun is rare, the collocation with strength is shared, and the settings (the ark's installation; the Torah's reading) are the two moments when the LORD's presence comes to its place.*
  - **The Aramaic cognate חֶדְוָה stands once, at Ezra 6:16**, the temple dedication. `[T]` So the word-family marks the book's three arrivals: house, wall — and book.
- **בין ("to understand").** Six verses here (8:2, 3, 7, 8, 9, 12) of the book's ten. `[T — lemma, WLC]` The forms vary — מֵבִין ("one who understands"), הַמְּבִינִים ("those who caused to understand"), וַיָּבִינוּ ("and they understood"), הֵבִינוּ. **And the root's last occurrence in the book is Neh 13:7, וָאָבִינָה בָרָעָה ("and I understood the evil")** — the same verb for understanding the Torah and for understanding what Eliashib had done. `[T]` *Moderate-to-high.* **Sweep finding.**
- **מְפֹרָשׁ ("distinctly" or "translated", 8:8).** A genuine crux: the same word stands at Ezra 4:18 of the letter read before the king. `[T]` Whether Neh 8:8 means clear articulation or Aramaic rendering is **open**, and the two readings have different implications for preaching (exposition vs translation). **Name both; do not resolve.**
- **תּוֹרָה ("law").** 21 verses in Nehemiah against 4 in Ezra, and **eight of Nehemiah's are in this chapter** (8:1, 2, 3, 7, 8, 9, 13, 14, 18). `[T — lemma, WLC]` **The scribe's book belongs, by frequency, to Nehemiah's half.**

**Proper-noun inventory:** Ezra the scribe; Moses; the Water Gate; thirteen men on the platform; thirteen Levites; Nehemiah the Tirshatha; **Jeshua the son of Nun (8:17)**. **Joshua is the freight.** The comparison is not with Solomon or David but with the conquest generation — and **the returning high priest is himself a יֵשׁוּעַ** (Ezra 3:2, 8; 5:2; Neh 12:1). `[S: overview, which rates the citation high and the name-play moderate]` *The sweep concurs: the name-play is worth mentioning once and not building on.*

### 8. Translations

- **8:8 NASB95 "translating to give the sense"; ESV "clearly".** **The two versions take opposite sides of the מְפֹרָשׁ crux.** *This is the sharpest NASB95/ESV divergence in the book*, and it decides whether Neh 8 is the origin of the synagogue targum or a description of good public reading. A preacher must know his version has already chosen. *High confidence that the divergence exists; the crux itself is open.*
- **8:10 NASB95 "the joy of the LORD is your strength"; ESV "the joy of the LORD is your strength".** Identical, and both right.
- **8:17 NASB95 "since the days of Joshua the son of Nun"; ESV "from the days of Jeshua the son of Nun".** **The ESV transliterates the Hebrew form and so preserves the name-play with the high priest; the NASB95 uses the familiar "Joshua" and loses it.** *Sweep finding; a rare case where the ESV shows something the NASB95 hides.*

**Ancient versions check.** Esdras A stops mid-sentence in this chapter, at Neh 8:13a, with καὶ ἐπισυνήχθησαν. `[S: overview, verified there]` **And at 8:9 Esdras A reads Ἀτταρατή where Esdras B reads Νεεμίας** — Nehemiah's name stripped out. `[S: overview, verified there]` **Triage: category 2** for a whole-book editorial decision, not a wording variant. It is the best available illustration of an ancient editor removing a figure, and worth one sentence from a pulpit.

### 9. Tone and Feel

**Rising, and interrupted.** The chapter builds through request, procession, opening, Amen, prostration — and then breaks on weeping it did not expect. The command "do not mourn or weep" is repeated three times in three verses (8:9, 8:10, 8:11), with the Levites going through the crowd saying הַסּוּ ("hush"). The recovery is not exhortation but food: eat the fat, drink the sweet, send portions to those with nothing ready.

**Soundtrack:** a single voice reading from dawn to midday, then a crowd.

### 10. Repetition

- **קָדוֹשׁ / קָדֹשׁ ("holy")** three times of the day (8:9, 8:10, 8:11).
- **אַל־תֵּעָצֵבוּ ("do not be grieved")** twice (8:10, 8:11).
- **כָּל־הָעָם ("all the people")** — **twelve times in the chapter** (8:1, 3 ×2, 5 ×2, 6, 9 ×2, 11, 12, 13 by implication, 16). `[T]` The chapter's insistent subject.
- **סֻכּוֹת ("booths")** five times in 8:14–17.

### 11. Quotation / Allusion — with Move 4

**Leviticus 23:33–43 → Neh 8:14–17** *(high confidence)*

*Source context:* the Booths law, with its branch-list (Lev 23:40: "the foliage of beautiful trees, palm branches, boughs of leafy trees and willows of the brook"). Its purpose clause is memorial: "that your generations may know that I made the sons of Israel live in booths when I brought them out of Egypt."
*Book usage:* **the second of two** — Ezra 3:4 kept the same feast כַּכָּתוּב, and **the difference between the two occasions is the finding.** At Ezra 3:4 they kept it from practice; here they kept it **because they found it written** (8:14), and the branch-list is read out (8:15). `[T]` **The book's method in one pair of scenes: do it, then find it written, then do it properly.**
*OT-to-OT:* Deut 16:13–15 and Num 29:12–38 are the other Booths texts; **Neh 8:15's branch list matches Lev 23:40 in substance but not in wording**, and adds olive and oil-tree. `[T]` **The community is quoting a law it is also adapting.** Flag, do not resolve.
*What it adds:* Booths is the feast of not-yet-having-a-house. The community keeps it, properly, in the year it finally has a wall.

**Joshua → Neh 8:17** *(high confidence for the citation)* — "the sons of Israel had not done so from the days of Jeshua son of Nun until that day." **Move 1:** the source is not a single verse but the conquest narrative as a whole, and the claim is startling: not Solomon's dedication, not Josiah's Passover, but the entry into the land is the last comparable occasion. `[T]`

**1 Chronicles 16:27 → Neh 8:10** *(moderate-to-high confidence)* — see Vocabulary. **Move 1:** 1 Chr 16 is David's psalm at the ark's installation in Jerusalem, a composite of Pss 105, 96 and 106; v. 27 describes what is "in his place" — that is, in the sanctuary. **Move 2:** the book cites the Davidic liturgy repeatedly (Ezra 3:10; Neh 12:24, 36, 45–46), so this is a live source. **Move 3:** 1 Chr 16 and Ps 96 are already the same text in the canon. **What it adds:** if the allusion holds, "the joy of the LORD is your strength" is not a maxim about cheerfulness but a claim that **what is in the sanctuary is now in the assembly** — which is exactly what a public reading of Torah in a square, rather than a rite in a temple, would mean. *Held at moderate-to-high, and flagged for a solo dig.*

**Internal (Move 4):**
- *Answers §earlier:* **8:1's כְּאִישׁ אֶחָד answers Ezra 3:1's.** The only two. `[S: overview, verified there]` *High.*
- *Answers §earlier:* **8:6's אָמֵן אָמֵן answers 5:13's congregational אָמֵן.** The only two. `[T]` *Moderate.*
- *Answers §earlier:* **8:14–17's Booths answers Ezra 3:4's.** `[S: overview]` *High.*
- *Answers §earlier:* **8:10's חֶדְוָה answers Ezra 6:16's Aramaic חֶדְוָה** at the temple dedication. `[T]` *Moderate.* **Sweep finding.**
- *Planted for later:* **8:15's כַּכָּתוּב → 10:35, 10:37**, the covenant's own citation formula. `[T]`
- *Planted for later:* **בין → 13:7.** `[T]` *Moderate-to-high.* **Sweep finding.**

### 16. So What? (brief)

The response sought is comprehension that issues in feasting and in sending portions to those with nothing ready. `[I]` **The motive clause is 8:12: they rejoiced because they had understood.** Against moralism: the chapter's joy is commanded, dated, and catered; it is not a temperament. The prayer is for understanding before feeling.

### Passage-specific difficulties

- **"The joy of the LORD is your strength" as a slogan.** Preaching Trap 6, and the sweep's lexical finding sharpens the corrective: the noun is rare, the context is a specific holy day, the command is to stop weeping and eat, **and the verse's nearest canonical relative describes what stands in God's sanctuary.** That is a better sermon than the slogan and it is in the text.
- **8:8 and the targum question.** Name the crux; say which side your version has taken.
- **Where is Ezra during Neh 1–7?** The text does not say. Do not fill it in.

---

## Unit 15 — Neh 9:1–37 ⭐ The longest prayer in the Bible

> 9:36 **הִנֵּה אֲנַחְנוּ הַיּוֹם עֲבָדִים** וְהָאָרֶץ אֲשֶׁר־נָתַתָּה לַאֲבֹתֵינוּ … הִנֵּה אֲנַחְנוּ עֲבָדִים עָלֶיהָ
> "Behold, we are slaves today, and as to the land which You gave to our fathers … behold, we are slaves in it." (NASB95)

### Headline Findings

1. **The unit title's claim is true but only just, and the margin is seven words.** Neh 9:6–37 is 32 verses and **495 words** in the WLC; Solomon's dedicatory prayer, 1 Kgs 8:23–53, is 31 verses and **488 words**. `[T — measured]` **Preach it as "the longest continuous prayer in the Hebrew Bible" only if you are willing to say by how little.**
2. **The prayer contains four of the book's twelve occurrences of עזב, and in all four the subject is God.** `[T]` They are the theological foundation the covenant of ch. 10 will be signed on and ch. 13 will break. See sweep Headline Finding 1.
3. **"We are slaves today" is said by the whole assembly, and is the answer to Ezra 9:9's "we are slaves".** `[S: overview, verified there]` **On a fast day, three verses before they sign.**

### 2. Context — Positional Necessity Check

**Preceding movement.** A week of Booths, kept with great joy, ending with a solemn assembly on the eighth day (8:18).

**Necessity answer.** Because joy that came from understanding must now be allowed to reach the rest of what was understood. **The prayer exists here — on the twenty-fourth day of the same month, in sackcloth and earth, after a feast — because Torah read aloud produces both the feasting of ch. 8 and the confession of ch. 9, and the book refuses to let either stand alone.** `[T]` for the dating.

**Implication.** Chs. 8 and 9 are one movement with two halves and must not be separated in a series. The command at 8:9 was "do not mourn *today*"; sixteen days later the mourning is scheduled.

### 3. Structure

9:1–3 the fast, the separation, the reading and confessing in quarters → 9:4–5a the Levites on the platform → 9:5b the call to bless → **9:6–31 the rehearsal: creation, Abraham, exodus, Sinai, wilderness, conquest, judges-cycle, prophets, exile** → 9:32–37 the turn to "and now", and the present.

**The device is a historical recital with a hinge.** 9:32's וְעַתָּה ("and now") is the pivot from what God did to what we are. **The recital's shape is Deuteronomic; its conclusion is not — it ends in a statement of condition, with no petition.** `[T]` So does Ezra's prayer (9:15). **Both of the book's great prayers stop before asking for anything**, which is a finding worth its own sermon.

### 4. Linking Words

- **9:6 אַתָּה־הוּא יְהוָה לְבַדֶּךָ ("You alone are the LORD") — the opening assertion**, not a request.
- **9:8 כִּי צַדִּיק אָתָּה ("for You are righteous") ←for←** God kept his word *because* he is righteous.
- **9:16 וְהֵם וַאֲבֹתֵינוּ הֵזִידוּ ("but they, our fathers, acted arrogantly") — the contrastive pivot**, repeated at 9:26 and 9:29.
- **9:33 וְאַתָּה צַדִּיק ("but You are righteous") ←for←** — the second time, now of the judgement.
- **9:36 הִנֵּה ("behold") ×2 — the prayer's last move**, and it is demonstrative, not petitionary.

### 7. Vocabulary

- **עזב ("to forsake").** 9:17, 9:19, 9:28, 9:31 — **four of the book's twelve, all with God as subject**, three negative and one positive. `[T — lemma, WLC]`
- **צַדִּיק ("righteous").** 9:8, 9:33 — and **Ezra 9:15 is the only other occurrence in the book.** `[T — lemma, WLC]` **Three in all, all of God, all in prayer, and they bracket the two confessions.** *High.* **Sweep finding.**
- **רַחֲמִים ("compassions").** 9:19, 9:27, 9:28, 9:31 — four times, always הָרַבִּים ("many"). `[T]`
- **אֱלוֹהַּ סְלִיחוֹת ("a God of forgivenesses", 9:17).** A hapax construction; the plural noun occurs three times in the Hebrew Bible (Ps 130:4; Dan 9:9; here).
- **הֵזִידוּ ("they acted presumptuously", 9:10, 9:16, 9:29).** Three times; the root זיד is Deuteronomy's word for the presumptuous man (Deut 17:12–13; 18:20).
- **חסד** at 9:17 (the Exod 34:6 formula) and 9:32 (שׁוֹמֵר הַבְּרִית וְהַחֶסֶד, echoing 1:5). `[T]`

**Proper-noun inventory:** Abram/Abraham; Ur of the Chaldeans; the six nations of 9:8; Egypt; the Red Sea; Pharaoh; Sinai; Moses; Sihon; Og of Bashan; the kings of Assyria. **9:8's list is Deut 7:1's seven nations minus the Hivite**, and it is a *promise* list (what God swore to give), where Ezra 9:1's is an *accusation* list. `[T]` **The same catalogue does opposite work in the book's two halves.** *Moderate-to-high.* **Sweep finding.**

### 8. Translations

- **9:17 NASB95 "in their rebellion"; ESV "in their rebellion"** — both follow L's בְּמִרְיָם. **BHS 9:17ᵃ directs to read בְּמִצְרַיִם ("in Egypt") with a few manuscripts and 𝔊, comparing Num 14:4, and Swete has ἐν Αἰγύπτῳ.** `[S: overview, apparatus and Swete both checked there]` **Neither English version footnotes it in the exports consulted.** One consonant decides whether the verse alludes to the wilderness plan to appoint a head and go back to Egypt or generalises it. **Name the witness — "Leningrad, as BHS prints it" — not "the Masoretic text".**
- **9:17's ketiv.** The same verse carries וְרַב־**וחסד**, an unpointed ketiv, where the qere and the versions give the Exod 34:6 formula רַב־חֶסֶד. `[S: overview]` **This is the verse that cost a correctly-normalised whole-Bible search the book's clearest Exodus-34 citation**, and it is the reason the ketiv rule is in the Phase 10.5 gate.

**Ancient versions check.** Run under 9:17, above. **Triage: category 2** for בְּמִרְיָם / בְּמִצְרַיִם — a genuine consonantal variant with versional support, on which the sweep takes no position beyond reporting both.

### 9. Tone and Feel

**Liturgical, cumulative, and finally flat.** Twenty-six verses of recital in the second person — you made, you chose, you saw, you gave, you did not forsake — against three refrains of rebellion. And then the tone drops out of the recital altogether at 9:36 into a plain present-tense statement. **The prayer does not end; it stops.** A sermon that supplies the missing petition has removed the point.

### 10. Repetition

- **וְאַתָּה ("but You")** — the recital's structural hinge, at 9:6, 9:17, 9:19, 9:27, 9:28, 9:31, 9:33.
- **נתן ("to give")** — saturates the recital: land, law, Sabbath, manna, water, kingdoms, saviours.
- **שמע ("to hear")** at 9:9, 9:16, 9:17, 9:27, 9:28, 9:29 — **six of Nehemiah's twenty-seven, and the chapter uses it in both directions**: God hears their cry; they would not hear his commandments. `[T]` *Sweep observation.*
- **עֲבָדִים ("slaves")** twice in 9:36.

### 11. Quotation / Allusion — with Move 4

**Exodus 34:6 (with Num 14:18) → Neh 9:17, 9:31** *(high confidence)*

*Source context:* the LORD's self-proclamation on Sinai after the golden calf, in answer to Moses' intercession. **Its setting is the restoration of a broken covenant**, which is precisely Neh 9's subject.
*Book usage:* two uses (9:17, 9:31), the second in short form.
*OT-to-OT:* Num 14:18 already re-uses Exod 34:6 in intercession after the spies' rebellion — **and Neh 9:17 places its citation beside the verse's own allusion to Num 14:4's "let us appoint a head and return to Egypt".** `[S: overview]` **The prayer is quoting a formula that the canon has already used twice in exactly this situation.**
*What it adds:* the attributes are **reordered** — חַנּוּן וְרַחוּם ("gracious and compassionate") for Exodus's רַחוּם וְחַנּוּן — and prefixed with אֱלוֹהַּ סְלִיחוֹת. `[S: overview, verified there]` The community is not reciting; it is composing with the formula.

**2 Kings 19:15 // Isaiah 37:16 → Neh 9:6** *(moderate-to-high confidence)* — אַתָּה־הוּא יְהוָה לְבַדֶּךָ ("You alone are the LORD"). The overview verified these are **the only three verses in the Hebrew Bible combining אַתָּה־הוּא with לְבַדֶּךָ**. `[S: overview, verified there]` **Move 1:** the source is Hezekiah's prayer in the temple with Sennacherib's letter spread before the LORD — a prayer offered by a people under an empire, asking to be delivered so that all kingdoms may know. **Move 3:** 2 Kgs 19 and Isa 37 are the canon's own synoptic pair. **What it adds:** the assembly opens its confession in the words of the last king who prayed under a siege — and it is praying under a tribute instead.

**Deuteronomy, throughout** — the recital's shape (9:9–25) follows the Deuteronomic retelling, and the covenant formula of 9:32, הָאֵל הַגָּדוֹל הַגִּבּוֹר וְהַנּוֹרָא שׁוֹמֵר הַבְּרִית וְהַחֶסֶד, reproduces Deut 7:21 and 10:17 combined with Deut 7:9. *High confidence for the formula; it also stands at Neh 1:5 and Dan 9:4.* `[T]`

**Internal (Move 4):**
- *Answers §earlier:* **9:36's "we are slaves today" answers Ezra 9:9's "we are slaves".** `[S: overview]` *High.*
- *Answers §earlier:* **9:32's covenant formula answers 1:5's.** Nehemiah's private prayer and the nation's public one open with the same clause. `[T]` *High.* **Sweep finding.**
- *Answers §earlier:* **9:8's nations-list answers Ezra 9:1's.** `[T]` *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **9:14's שַׁבַּת קָדְשְׁךָ ("your holy Sabbath")** is the Sabbath's first appearance in the book — **and the root then stands at 10:32, 10:34 in the covenant and seven times in ch. 13** (13:15, 16, 17, 18, 19, 21, 22). **Ten verses in all, all in Nehemiah, seven of them in the relapse.** `[T — lemma, WLC]` *High.* **Sweep finding: the Sabbath is confessed, then sworn, then broken, in that order, and the count makes the shape visible.**
- *Planted for later:* **9:17, 9:19, 9:28, 9:31's עזב → 10:40 and 13:11.** *High.* **Sweep finding.**

### 16. So What? (brief)

The response sought is confession that rehearses God's acts at length before naming one's own condition, and that is willing to stop without a petition. `[I]` The worldview note is the prayer's arithmetic: twenty-six verses about God to six about us. Against therapeutic prayer: this one begins with creation and ends "we are in great distress", and asks for nothing.

### Passage-specific difficulties

- **The unit title.** Correct it gently (Headline Finding 1).
- **A prayer with no petition.** A congregation will expect one. The absence is the point, and it is shared with Ezra 9:15.
- **9:37's "and we are in great distress" as the last word before a covenant.** Do not let ch. 10 rescue ch. 9 too quickly; the narrator did not.

---

## Unit 16 — Neh 9:38–10:39 (MT 10:1–40) Signed and sealed

### Headline Findings

1. **The document's last clause is the one the book will prosecute.** 10:40 (Eng 10:39) — וְלֹא נַעֲזֹב אֶת־בֵּית אֱלֹהֵינוּ. `[T]` See sweep Headline Finding 1.
2. **The covenant's three main clauses are broken in ch. 13 in the same order** — intermarriage (10:31 → 13:23–27), Sabbath trade (10:32 → 13:15–21), the dues (10:38–40 → 13:10–11). `[S: overview, verified there]`
3. **But not every commitment fails.** The wood offering of 10:35 is shown being arranged at 13:31, in the book's last sentence but one. `[S: overview]` **"Every oath broken" is an overstatement and the overview's audit already corrected it.**

### 2. Context — Positional Necessity Check

**Preceding movement.** A confession that ended with "we are slaves today" and "we are in great distress", and no petition.

**Necessity answer.** Because a prayer that asks for nothing has to be followed by something, and what the community does is **write, seal and sign** — וּבְכָל־זֹאת אֲנַחְנוּ כֹּרְתִים אֲמָנָה וְכֹתְבִים ("and because of all this we are making a firm agreement in writing", 10:1). `[T]` **The passage exists here because the book's answer to an unanswerable condition is a document.** That is its method throughout, and this is the point at which the method is put to the test.

**Implication.** Ch. 10 is not the book's climax; it is its experiment. The narrator has arranged for the result to be reported three chapters later.

### 3. Structure

10:1–28 the signatories: the Tirshatha, priests, Levites, heads of the people → 10:29–30 the rest of the people join by oath → 10:31–40 the clauses: marriage, Sabbath and the seventh year, the temple tax, the wood offering, firstfruits and firstborn, tithes — and the closing commitment.

**The device is a legal instrument.** Parties, then undertaking, then schedule. **The last line of the schedule is a general covenant** (10:40b), which is where a document puts its operative promise.

### 4. Linking Words

- **10:1 וּבְכָל־זֹאת ("and because of all this") →therefore→** the document is the consequence of ch. 9.
- **10:30 בְּאָלָה וּבִשְׁבוּעָה ("into a curse and an oath")** — the instrument's sanction.
- **10:31 וַאֲשֶׁר ("and that…")** — the formula introducing each clause, repeated through the schedule.
- **10:40 וְלֹא נַעֲזֹב ("and we will not forsake")** — the closing undertaking, and the only clause phrased negatively as a general commitment rather than a specific practice. `[T]`

### 7. Vocabulary

- **אֲמָנָה ("firm agreement", 10:1).** **Two occurrences in the book: here and 11:23**, where it is a royal arrangement about the singers. `[T — lemma, WLC]` The community's covenant and an administrative rota share a word, and the second use is thirty verses later.
- **עזב.** 10:40. See above.
- **שַׁבָּת.** 10:32, 10:34. See unit 15.
- **מַעֲשֵׂר ("tithe").** 10:38, 10:39 — and then 12:44; 13:5; 13:12. `[T — lemma, WLC]` **Five verses: two in the covenant, one in the fulfilment notice, two in the relapse and its repair.**
- **כַּכָּתוּב ("as it is written", 10:35, 10:37).** Two of the book's five.
- **הַנִּבְדָּל ("everyone who had separated", 10:29).** בדל again, and again **inclusively**: those who separated from the peoples *to* the law of God, with their wives, sons and daughters. `[T]` See Book-Overview Tension 1.

**Proper-noun inventory:** eighty-four signatories. Routine, with one exception: **the list is headed by נְחֶמְיָה הַתִּרְשָׁתָא בֶּן־חֲכַלְיָה (10:2)**, the only place the memoir's author is given his title and patronymic together in a document. `[T]` **He signs first, and thirteen chapters later he is the one enforcing what he signed.**

### 8. Translations

- **10:39 (MT 10:40) NASB95 "Thus we will not neglect the house of our God"; ESV "We will not neglect the house of our God."** **Both use "neglect"; both use "forsaken" at 13:11.** **The link is invisible in both.** *This is the single most consequential translation note in the book* — see sweep Headline Finding 1. A preacher must supply it.
- **10:1 (Eng 9:38) NASB95 "we are making an agreement in writing"; ESV "we make a firm covenant in writing".** The ESV's "firm covenant" is closer to אֲמָנָה's root (אמן).

**Pulpit divergence note:** N/A — no pulpit text declared.

**Ancient versions check.** Esdras B renders 10:40 with οὐκ ἐγκαταλείψομεν and 13:11 with ἐγκατελείφθη — **the Greek keeps what both English versions lose.** `[T — Rahlfs export, checked]` **Triage: category 1** — an English translation loss, not a textual matter, and it should be reported as a fact about the Hebrew and the Greek rather than as a criticism of the versions, which are each internally reasonable.

### 10. Repetition

- **וַאֲשֶׁר / וְ ("and that")** as the clause-formula through 10:31–40.
- **בֵּית אֱלֹהֵינוּ ("the house of our God")** — **eight times in the schedule** (10:33, 34, 35, 36, 37 ×2, 38, 39, 40). `[T]` The document's recurring object, and the thing the last clause promises not to forsake.
- **לְבֵית ("to the house of")** as the destination of every contribution.

### 11. Quotation / Allusion — with Move 4

**Deuteronomy 7:3 → Neh 10:31** *(high confidence)* — the marriage clause reproduces the prohibition in the same two-directional form (our daughters to them, their daughters to our sons). **Move 2:** the fourth use of Deut 7 in the book (Ezra 9:1, 9:12; Neh 10:31; 13:25). **What it adds:** the community legislates for itself what the Torah had legislated, which is either superfluous or an admission that the Torah's authority needed re-signing. The book does not say which.

**Exodus 30:13 / 38:26 → Neh 10:33** *(moderate confidence)* — the temple tax. **Note the divergence: the Torah's levy is half a shekel; the covenant's is a third.** `[T]` The community has adjusted a Mosaic figure downward, in a document that elsewhere cites Torah as binding, and the book offers no comment. **This is a genuine and under-preached datum about how the community handled the law.** *High confidence on the fact; the explanation is open.*

**Exodus 23:10–11 / Leviticus 25:1–7 / Deuteronomy 15:1–2 → Neh 10:32b** *(high confidence)* — the seventh-year clause combines the fallow-land law with the debt-release, which the Torah keeps in separate codes. `[T]` Another splice, like Ezra 9:1's.

**Internal (Move 4):**
- *Planted for later — the book's central planting:* **10:31, 10:32, 10:38–40 → 13:23–27, 13:15–21, 13:10–11.** `[S: overview, verified there]` *High.*
- *Planted for later:* **10:40's עזב → 13:11.** `[T]` *High.* **Sweep finding.**
- *Planted for later:* **10:35's wood offering → 13:31**, where it is arranged and not broken. `[S: overview]` *High, and the necessary corrective to "every clause".*
- *Answers §earlier:* **10:29's הַנִּבְדָּל answers Ezra 6:21's**, the book's two inclusive separations. `[T]` *Moderate-to-high.* **Sweep finding.**
- *Answers §earlier:* **10:1's signing answers 9:38's decision and 5:12's oath.** Three binding acts, escalating from spoken to sealed. `[T]` *Moderate.*

### 13 / 15. Copycat and Who Am I?

**Copycat.** The covenant is *descriptive*, and specifically it is **an experiment the book reports the failure of**. To preach ch. 10 as a model for congregational covenanting without preaching ch. 13 is to recommend a mechanism the author has already tested.

**Who Am I?** With the eighty-four who signed.

### 16. So What? (brief)

The response sought is sober: a community that writes down what it intends and discovers that writing it down is not enough. `[I]` **The gospel grounding is the one the book itself makes available** — the covenant clause that fails here is answered by a covenant written on hearts (Jer 31:33), and the failure is the argument for it. Against moralism: the answer to a broken covenant is not a better-drafted one.

### Passage-specific difficulties

- **A third of a shekel against Exodus's half.** Name it; do not explain it away.
- **Preaching a signature list.** The names matter because ch. 13 will hold them to it.
- **"Every clause broken."** Not true. The wood offering stands. Say so, because a congregation that catches the overstatement will distrust the rest.

---

## Unit 17 — Neh 11:1–12:26 Filling the holy city

### Headline Findings

1. **The city is populated by lot**, and one in ten is moved in. 11:1 — הִפִּילוּ גוֹרָלוֹת לְהָבִיא אֶחָד מִן־הָעֲשָׂרָה לָשֶׁבֶת בִּירוּשָׁלִַם עִיר הַקֹּדֶשׁ. `[T]`
2. **The people bless the volunteers.** 11:2 — וַיְבָרֲכוּ הָעָם לְכֹל הָאֲנָשִׁים הַמִּתְנַדְּבִים ("and the people blessed all the men who volunteered"). `[T]` **The lot and the volunteering stand in consecutive verses and the book does not reconcile them.**
3. **גּוֹרָל ("lot") occurs twice in the book — 10:35 and 11:1** — and the first is how the wood offering was assigned in the covenant. `[T]` **The community's two uses of the lot are a liturgical rota and a compulsory relocation.**

### 2. Context — Positional Necessity Check

**Preceding movement.** A signed covenant, whose schedule concerns what is brought *to* the house of God.

**Necessity answer.** Because the house needs a city around it, and 7:4 has already stated that the city is large and empty. **The passage exists here because the covenant of ch. 10 is unworkable without people within reach of the temple** — the tithes, the firstfruits, the wood, the daily service all assume a resident population. `[I]`, high confidence.

**Implication.** Chs. 11–12:26 are the covenant's infrastructure, not a list dropped in. Read that way, the unit is the answer to ch. 10 and the preparation for ch. 12:27.

### 3. Structure

11:1–2 the lot and the blessing → 11:3–24 who lived in Jerusalem, by tribe and office → 11:25–36 the villages of Judah and Benjamin → 12:1–7 priests who came up with Zerubbabel → 12:8–9 Levites → 12:10–11 the high-priestly succession → 12:12–21 priestly heads in the days of Joiakim → 12:22–26 the record, and the dating formula.

**The device is a widening and then a narrowing:** Jerusalem, then the villages, then back to the temple personnel.

### 7. Vocabulary

- **עִיר הַקֹּדֶשׁ ("the holy city", 11:1, 11:18).** **The book's only two occurrences**, and the phrase is rare in the Hebrew Bible (Isa 48:2; 52:1; Dan 9:24; Neh 11:1, 18). `[T]` *Moderate-to-high confidence on the Isaianic resonance; the phrase is distinctive and Isaiah 52:1's context — "put on your beautiful garments, O Jerusalem, the holy city; for the uncircumcised and the unclean will no longer come into you" — is thematically exact for this book.* **Sweep observation; the overview lists an untested Isaiah 56–66 chain, and this is a nearby datum a claim audit should take up.**
- **הַמִּתְנַדְּבִים ("those who volunteered", 11:2).** The root נדב runs from Ezra 1:6; 2:68; 3:5; 7:13, 15, 16; 8:28 to here. `[T]` **The book's word for uncompelled giving, used of a relocation assigned by lot.**
- **אֲמָנָה (11:23).** See unit 16.
- **נְגִד בֵּית הָאֱלֹהִים ("leader of the house of God", 11:11).** נָגִיד — the royal-designation term — applied to a priest. `[T]` *Worth one line: the book uses a king-word for a temple officer in a book with no king.*

**Proper-noun inventory:** very large. Two carry freight. **"The sons of Perez" (11:4, 11:6)** — Judah's line through Tamar, and the line that runs to David and to Matt 1:3. `[T]` **Seraiah son of Hilkiah… son of Ahitub (11:11)** reproduces Ezra's own genealogy (Ezra 7:1–2), tying the resident temple leadership to the scribe's line.

### 8. Translations

NASB95 and ESV agree substantively. No divergence bearing on the findings.

**Ancient versions check.** Esdras B transliterates heavily through the lists. No split.

### 10. Repetition

- **יָשַׁב ("to dwell")** through 11:1–36 — the unit's governing verb.
- **וּפָקִיד עֲלֵיהֶם ("and the overseer over them")** at 11:9, 11:14, 11:22 — the administrative refrain.
- **בִּימֵי ("in the days of")** at 12:7, 12:12, 12:22, 12:23, 12:26, 12:47 — the dating formula that carries the second half of the unit and reaches into unit 18.

### 11. Quotation / Allusion — with Move 4

No direct citation. **Move 2:** the David–Solomon temple order is invoked at 12:24 (בְּמִצְוַת דָּוִיד אִישׁ־הָאֱלֹהִים), the book's third use of that live source (Ezra 3:10; Neh 12:24, 45–46). **And note the title:** דָּוִיד אִישׁ־הָאֱלֹהִים, the same epithet Ezra 3:2 gave Moses. `[T]` *Moderate-to-high.* **Sweep finding: the book's two named authorities for how worship is conducted are each called "the man of God", at the two ends of the volume.**

**Internal (Move 4):**
- *Answers §earlier:* **11:1's repopulation answers 7:4's empty city.** `[T]` *High.*
- *Answers §earlier:* **11:1's lot answers 10:35's.** The book's only two. `[T]` *Moderate-to-high.* **Sweep finding.**
- *Planted for later:* **12:10–11's high-priestly succession — Jeshua → Joiakim → Eliashib → Joiada → Jonathan → Jaddua — is the genealogy that makes 13:28 intelligible**, where "one of the sons of Joiada son of Eliashib the high priest" is son-in-law to Sanballat. `[T]` *High.* **Sweep finding: the list exists so that the reader can place the man Nehemiah drives out.**
- *Planted for later:* **11:11's נָגִיד and 12:24's דָּוִיד אִישׁ־הָאֱלֹהִים → 12:36, 12:45–46.** `[T]`

### 16. So What? (brief)

The response sought is willingness to be the one in ten. `[I]` The application is unglamorous and exact: the covenant of ch. 10 required people to live where the work was, and the community blessed those who did. The prayer is for the ordinary obedience of moving house.

### Passage-specific difficulties

- **Lot or volunteering?** 11:1 and 11:2 sit side by side and are not reconciled. Do not smooth it.
- **Preaching lists, again.** This is the third of the book's four major lists. If a series preaches only one, preach Neh 3 for the trades and Neh 11 for the lot.
- **Jaddua (12:11, 12:22).** The name reaches, on the usual reckoning, into the Greek period, and raises a date question the book does not address. Flag as `[S]` and move on; nothing in the sweep rests on it.

---

## Unit 18 — Neh 12:27–47 Two choirs on the wall

> 12:43 … כִּי הָאֱלֹהִים **שִׂמְּחָם שִׂמְחָה** גְדוֹלָה … וַתִּשָּׁמַע **שִׂמְחַת** יְרוּשָׁלִַם מֵרָחוֹק
> "for God had given them great joy … so that the joy of Jerusalem was heard from afar." (NASB95)

### Headline Findings

1. **Neh 12:43 carries five words from the root שׂמח — the densest single verse in the book.** וַיִּשְׂמָחוּ … שִׂמְּחָם … שִׂמְחָה … שָׂמֵחוּ … שִׂמְחַת. `[T — counted directly in the consonantal text]`
2. **Its idiom is Ezra 6:22's.** הָאֱלֹהִים שִׂמְּחָם here; שִׂמְּחָם יְהוָה at the temple's Passover. **The same piel construction at the book's two completions.** `[T — lemma, WLC]` *Sweep finding.*
3. **The chapter is the answer to Ezra 3:13, and it is one chapter early.** מֵרָחוֹק occurs twice in the book; the first is a noise nobody could sort out. `[S: overview, verified there]`

### 2. Context — Positional Necessity Check

**Preceding movement.** The city is populated and the temple staff is recorded.

**Necessity answer.** Because a wall dedicated before the city inside it is inhabited would be a ceremony over an empty space. **The passage exists here, after ch. 11, for the same reason the altar preceded the foundation: the book's order is function before ceremony.** `[T]` for the sequence.

**Implication.** And the harder positional point: **the chapter exists here rather than at the end.** The author had a natural ending available and declined it. Preaching Trap 4.

### 3. Structure

12:27–30 the Levites gathered and the purification → 12:31–37 the first choir, right along the wall → 12:38–39 the second choir, left → 12:40–42 both standing in the house of God → 12:43 the sacrifices and the joy → 12:44–47 the appointments over the storerooms, and the note that all Israel gave the portions.

**The device is a processional chiasm in space.** Two companies leave the same point in opposite directions along the wall and meet in the temple. `[T]` **The wall's circuit is walked liturgically, the same circuit the register of ch. 3 walked administratively.** *Moderate-to-high; the gates named in 12:31–39 overlap substantially with ch. 3's.* **Sweep observation.**

### 4. Linking Words

- **12:43 כִּי ("for") ←for←** the rejoicing is grounded in God's having made them rejoice.
- **12:44 כִּי ("for") ←for←** the appointments are grounded in Judah's joy over the priests and Levites.
- **12:47 וּמַקְדִּשִׁים … וְהַלְוִיִּם מַקְדִּשִׁים ("and they set apart… and the Levites set apart")** — the chain of consecration that 13:10 will break.

### 7. Vocabulary

- **שׂמח / שִׂמְחָה.** Five words of the root in 12:43, plus 12:27 and 12:44. `[T]` **The book's joy-vocabulary stands in eight verses: Ezra 3:12, 3:13, 6:22; Neh 8:12, 8:17, 12:27, 12:43, 12:44** — the foundation, the Passover, the book, and the wall. `[T — lemma, WLC]` **And none in ch. 13.**
- **תּוֹדָה ("thanksgiving choir", 12:31, 12:38, 12:40).** Three times, of the two companies; the noun elsewhere means a thank-offering, and the book uses it for a body of singers.
- **מֵרָחוֹק ("from afar", 12:43).** One of two. `[S: overview]`
- **מְנָאוֹת הַתּוֹרָה ("the portions of the law", 12:44).** A construct found only here. `[T]`

**Proper-noun inventory:** the gates of the circuit; David; Asaph; Ezra the scribe (12:36); Nehemiah (12:47); Zerubbabel. **David (12:36, 12:45, 12:46)** is the freight — **בִּכְלֵי־שִׁיר דָּוִיד אִישׁ הָאֱלֹהִים ("with the musical instruments of David the man of God")** — and the liturgy is grounded in his and Solomon's command (12:45). **Ezra the scribe walks at the head of the first company (12:36)**, his last appearance in the book. `[T]`

### 8. Translations

- **12:43 NASB95 "the joy of Jerusalem was heard from afar"; ESV "the joy of Jerusalem was heard far away".** Both keep the construct. **The Greek reads ἐν Ἰερουσαλήμ ("in Jerusalem")** in both Swete and Rahlfs — a locative where the Hebrew has a construct. `[T]` **Triage: category 1**, a rendering choice, and the English versions are closer to the Hebrew than the Greek is.
- Neither version can show that the verse has five words from one root. **Tell the congregation; it is the point of the verse.**

**Ancient versions check.** Run above. Esdras B has four εὐφρ- words against the Hebrew's five.

### 9. Tone and Feel

**Unambiguous, and the book says so.** Where Ezra 3:13 reported a noise nobody could distinguish, this chapter reports joy five times in one verse and adds that women and children rejoiced too. **The register is the highest in the book and it is one chapter from the lowest.** A sermon should let the height stand — and then say what the author does with it.

### 10. Repetition

- **שׂמח** (above).
- **מֵעַל לַחוֹמָה ("above the wall")** at 12:31, 12:37, 12:38 — the processional refrain.
- **מִשְׁמֶרֶת ("the charge/watch")** at 12:45 ×2 — and the word returns at 13:14, 13:30.
- **כְּמִצְוַת דָּוִיד ("according to the command of David")** at 12:45, with 12:24 and 12:46.

### 11. Quotation / Allusion — with Move 4

**1 Chronicles 23–26 / 2 Chronicles 8:14 → Neh 12:24, 12:45–46** *(moderate-to-high confidence)* — the third and fourth uses of the Davidic liturgical order. **Move 2:** the book's pattern is consistent — legal authority to Moses, liturgical authority to David — with the one exception at Ezra 6:18 (unit 5). **What it adds:** the dedication is performed by a body that understands itself as continuous with the first temple's, in a second temple with no glory cloud.

**Internal (Move 4):**
- *Answers §earlier:* **12:43's מֵרָחוֹק answers Ezra 3:13's.** `[S: overview]` *High.*
- *Answers §earlier:* **12:43's הָאֱלֹהִים שִׂמְּחָם answers Ezra 6:22's שִׂמְּחָם יְהוָה.** `[T]` *High.* **Sweep finding.**
- *Answers §earlier:* **the processional circuit answers ch. 3's register.** *Moderate-to-high.* **Sweep finding.**
- *Answers §earlier:* **12:44's storerooms answer 10:38–40's covenant clause** — the dues are actually being brought. `[T]` *High.*
- *Planted for later — the cruellest planting in the book:* **12:44–47's storerooms and appointments → 13:4–5, where a storeroom is given to Tobiah, and 13:10, where the portions are not given.** `[T]` **The last thing ch. 12 reports working is the first thing ch. 13 reports broken.** *High.* **Sweep finding.**

### 16. So What? (brief)

The response sought is corporate joy that is loud, catered, inclusive of women and children, and credited to God. `[I]` **The motive is 12:43's own clause: God made them rejoice.** The prayer is thanksgiving for finished work, held without assuming it will hold.

### Passage-specific difficulties

- **Treating the dedication as the climax.** Preaching Trap 4. **The corrective is textual and easy: 12:44–47 says the storerooms were staffed and the portions given, and 13:4–10 says a storeroom went to Tobiah and the portions stopped.** The author put them side by side.
- **Two choirs on a wall.** A congregation will enjoy the picture. Let it — and then read 13:1.

---

## Unit 19 — Neh 13:1–31 ⭐ Remember me

> 13:11 וָאָרִיבָה אֶת־הַסְּגָנִים וָאֹמְרָה מַדּוּעַ **נֶעֱזַב** בֵּית־הָאֱלֹהִים
> "So I reprimanded the officials and said, 'Why is the house of God forsaken?'" (NASB95)
>
> 13:22 … גַּם־זֹאת זָכְרָה־לִּי אֱלֹהַי וְחוּסָה עָלַי **כְּרֹב חַסְדֶּךָ**
> "For this also remember me, O my God, and have compassion on me according to the greatness of Your lovingkindness." (NASB95)

### Headline Findings

1. **The chapter prosecutes the covenant in the covenant's own verb.** 13:11's נֶעֱזַב answers 10:40's נַעֲזֹב. `[T]` See sweep Headline Finding 1.
2. **The Ammonite label planted at 2:10 detonates here.** 13:1 reads Deut 23 aloud — no Ammonite in the assembly — and 13:4–8 finds Tobiah the Ammonite in a temple chamber. `[T]` **Eleven chapters apart, and the narrator never joins them.** *Sweep finding.*
3. **Nehemiah's last word about himself and his last word about God use the same root.** 13:14 asks God not to wipe out חֲסָדַי ("my loyal deeds"); 13:22 asks to be spared כְּרֹב חַסְדֶּךָ ("according to the greatness of your lovingkindness"). `[T]` **Both English versions break it.**
4. **He tears out their hair (13:25) with the verb Ezra used of his own (Ezra 9:3), and the book has no third occurrence.** `[T]` See sweep Headline Finding 2.

### 2. Context — Positional Necessity Check

**Preceding movement.** A dedication with two choirs, joy heard from far off, and a working system of storerooms and portions (12:44–47).

**Necessity answer.** Because the author has arranged the book so that its best day is followed immediately by its worst. **The unit exists here because everything before it has been an attempt to secure holiness by a mechanism — a register, a wall, a book, a signature — and the narrative's job now is to report what happened to the mechanism when the governor left the country.** 13:6 is the pivot: וּבְכָל־זֶה לֹא הָיִיתִי בִּירוּשָׁלִָם ("but during all this time I was not in Jerusalem"). `[T]`

**Implication.** The chapter is not an appendix and not a decline narrative. **It is the experiment's result**, and it is placed exactly where a result belongs.

### 3. Structure

13:1–3 the reading of Deut 23 and the separation → 13:4–9 Eliashib, Tobiah, and the chamber → 13:10–14 the Levites' portions, the reprimand, the first "remember me" → 13:15–22 the Sabbath, the shut gates, the second "remember me" → 13:23–29 the foreign wives, Solomon, the high priest's grandson, the "remember them" → 13:30–31 the purification, the provisions, and the last "remember me".

**The device is four reforms, each closed by a prayer.** `[T]` Three petitions for himself (13:14, 13:22, 13:31) and one against others (13:29). The chapter's rhythm is: discover, confront, arrange, pray.

### 4. Linking Words

- **13:6 וּבְכָל־זֶה ("but during all this time") — the disjunctive pivot.** Everything in 13:4–5 happened in the governor's absence.
- **13:11 מַדּוּעַ ("why?") — the accusing question**, and it is the covenant's own wording.
- **13:18 הֲלוֹא כֹה עָשׂוּ אֲבֹתֵיכֶם ("did not your fathers do the same?") ←for←** the Sabbath argument is historical: this is why the city was destroyed.
- **13:26 הֲלוֹא עַל־אֵלֶּה חָטָא־שְׁלֹמֹה ("did not Solomon king of Israel sin regarding these things?") ←for←** the marriage argument is also historical, and it closes the case from the wisest king's failure.
- **13:27 וְלָכֶם הֲנִשְׁמַע ("shall we then listen to you…?")** — the rhetorical close, using שמע, the book's own opposition-verb, of his own people. `[T]`

### 7. Vocabulary

- **עזב.** 13:11. See above.
- **חסד.** 13:14, 13:22. See Headline Finding 3, and the Book-Level Christological frame.
- **מרט.** 13:25. See Headline Finding 4.
- **שַׁבָּת.** 13:15, 16, 17, 18, 19, 21, 22 — **seven of the book's ten, all in this chapter.** `[T — lemma, WLC]`
- **מעל.** 13:27, לִמְעֹל בֵּאלֹהֵינוּ ("to act unfaithfully against our God") — the fourth and last of the verb, answering 1:8's quotation of Moses. `[T]`
- **דֶּלֶת ("doors", 13:19).** The last of eleven; the doors hung in chs. 3 and 7 are shut. `[T]`
- **נַעַר ("my servants", 13:19).** The last of eight; they are posted at the gates. `[T]`
- **בין.** 13:7, וָאָבִינָה בָרָעָה ("and I understood the evil") — the last of ten, and the same verb as Neh 8's understanding of the Torah. `[T]`
- **זָכְרָה ("remember").** 13:14, 13:22, 13:29, 13:31 — four of the nine. `[T]`

**Proper-noun inventory:** Moses; Ammonite, Moabite; Balaam; Eliashib; Tobiah; Judah; Artaxerxes king of **Babylon** (13:6 — the book's one use of that title for a Persian king, matching "king of Assyria" at Ezra 6:22); the Tyrians; Ashdod; Solomon; Joiada son of Eliashib; Sanballat the Horonite.

**Balaam (13:2)** is the chapter's one full name-hyperlink, and it comes inside the Deut 23 citation. **Solomon (13:26)** is the argument's whole weight: the book's only appeal to a named king, made to prove that no amount of favour protects a man from foreign wives. `[T — 1 Kgs 11 re-read: the text's own reason is that his wives turned his heart, which is Deut 7:4's reason]` *High confidence; the citation is explicit.*

### 8. Translations

- **13:11 "forsaken" in both versions, against "neglect" at 10:39.** The book's most consequential English loss. *Supply it.*
- **13:14 / 13:22** — NASB95 "my loyal deeds" / "Your lovingkindness"; ESV "my good deeds" / "your steadfast love". **Both break the link.** The Greek keeps it (ἔλεός μου / τοῦ ἐλέους σου). *Supply it.*
- **13:25 "pulled out their hair" in both versions, matching Ezra 9:3.** **Kept.** Use it.
- **13:27 NASB95 "by acting unfaithfully against our God"; ESV "act treacherously against our God".** **The NASB95 keeps the link to 1:8's "if you are unfaithful"; the ESV breaks it.** *Sweep finding.*

**Pulpit divergence note:** N/A — no pulpit text declared. For a future engagement: **this chapter is where the choice of version costs most.** On three of its four load-bearing chains the NASB95 is the better witness; on none is the ESV.

**Ancient versions check.** **Swete omits וָאֶמְרְטֵם ("and I pulled out their hair") at 13:25 entirely; Rahlfs has καὶ ἐμαδάρωσα αὐτούς.** `[T — both checked]` **The omission is Vaticanus's, and BHS's apparatus carries no note at 13:25**, which is a fair measure of its weight. **Triage: category 2** in principle, of no consequence in practice — and reported chiefly because a report resting on Swete alone would have got it wrong.

### 9. Tone and Feel

**Anger, exhaustion, and self-defence.** וַיֵּרַע לִי מְאֹד ("it was very displeasing to me", 13:8); וָאָרִיבָה ("I contended", 13:11, 13:17, 13:25); וָאֲקַלְלֵם ("I cursed them", 13:25); אִם־תִּשְׁנוּ יָד אֶשְׁלַח בָּכֶם ("if you do so again, I will lay hands on you", 13:21). **And four times, a man stopping mid-narrative to ask God to notice.** The register is not triumphant and not despairing; it is the sound of somebody doing the same job a second time.

**Soundtrack:** something unresolved. There is no cadence at 13:31; the book stops on a petition.

### 10. Repetition

- **בַּיָּמִים הָהֵם / הָהֵמָּה ("in those days")** at 13:15, 13:23 — with בַּיּוֹם הַהוּא at 12:44 and 13:1. **Four loose temporal markers in the last two chapters**, which is how the book signals that the sequence is no longer tight. `[T]`
- **זָכְרָה** four times.
- **וָאָרִיבָה ("and I contended")** three times (13:11, 13:17, 13:25) — and once earlier at 5:7. `[T]` **Nehemiah contends four times in the book, and three of them are here.**
- **שַׁבָּת** seven times.

### 11. Quotation / Allusion — with Move 4

**Deuteronomy 23:4–6 → Neh 13:1–2** *(high confidence — explicit)*

*Source context:* the assembly law. **13:2 reproduces לֹא קִדְּמוּ ("they did not meet [them] with bread and water"), and the overview verified that this exact phrase stands in the Hebrew Bible only at Deut 23:5 and Neh 13:2.** `[S: overview, verified there]` The reason given is twofold: the failure of hospitality and the hiring of Balaam.
*Book usage:* the third and final use of Deut 23 (Ezra 9:1, 9:12; here), and the only one that quotes it openly as "the book of Moses".
*OT-to-OT:* Deut 23:5–6 already summarises Num 22–24, and **Neh 13:2 adds the summary clause the Torah supplies: "but our God turned the curse into a blessing."** `[T]`
*What it adds:* **the citation is read aloud in v. 1 and is contradicted in v. 4 by a fact the narrator has withheld — that an Ammonite is living in the temple.** The chapter's first three verses are the law; the next five are the breach; and the narrator's ordering is the argument.

**1 Kings 11:1–8 → Neh 13:26** *(high confidence — explicit)*

*Source context:* Solomon's foreign wives turn his heart after other gods in his old age, and the kingdom is torn from his son. The passage's own reason is the heart, not the ethnicity, and **the same reason Deut 7:4 gives.** `[T — source read]`
*Book usage:* the only appeal to the monarchy in the book.
*OT-to-OT:* 1 Kgs 11:1–2 itself cites the Deut 7:3–4 prohibition. **So Neh 13:26 is citing a text that is already citing the text Neh 13:25 has just enforced.** `[T]` *High.* **That is the book's tightest OT-to-OT chain and it should be preached.**
*What it adds:* the argument is a fortiori and it is about favour, not merit: "among the many nations there was no king like him, and he was loved by his God… yet the foreign women caused even him to sin."

**Internal (Move 4):**
- *Answers §earlier:* **13:11's נֶעֱזַב answers 10:40's נַעֲזֹב.** *High.* **Sweep finding.**
- *Answers §earlier:* **13:1's Deut 23 answers 2:10 and 2:19's "Tobiah the Ammonite servant".** *High.* **Sweep finding.**
- *Answers §earlier:* **13:27's לִמְעֹל answers 1:8's תִּמְעָלוּ.** *High.* **Sweep finding.**
- *Answers §earlier:* **13:25's מרט answers Ezra 9:3's.** *High.* **Sweep finding.**
- *Answers §earlier:* **13:15–22's Sabbath answers 10:32 and 9:14.** *High.* **Sweep finding.**
- *Answers §earlier:* **13:4–9's chamber answers 12:44's storerooms, and 13:10 answers 12:47.** *High.* **Sweep finding.**
- *Answers §earlier:* **13:28's high priest's grandson is placed by 12:10–11's succession list.** *High.* **Sweep finding.**
- *Answers §earlier:* **13:31's זָכְרָה־לִּי אֱלֹהַי לְטוֹבָה answers 5:19's identical clause**, framing the governorship. `[S: overview, verified there]` *High.*
- *Answers §earlier:* **13:19's doors answer 3:1–15 and 7:1.** `[T]` *Moderate-to-high.* **Sweep finding.**
- *Planted, and never resolved:* **13:29's "they have defiled the priesthood" is the book's last word on the question Ezra 2:63 asked.** `[T]` **The book ends with a priesthood needing purification and no priest able to give it.** *High.*

### 13 / 15. Copycat and Who Am I?

**Copycat — and this is where the book itself answers Trap 1.** Walk it:
- **The reading of the law (13:1–3):** *normative pattern.*
- **Throwing out the furniture (13:8):** *descriptive*, and the action is against property in an outbuilding, not against a person in the sanctuary — which is consistent with 6:11.
- **The reprimand and restoration of the Levites (13:11–13):** *normative pattern* at the level of the principle (those who serve must be supported), and note that Nehemiah's remedy is an appointment of trustworthy men, not a sermon.
- **Shutting the gates (13:19):** *descriptive*, and effective.
- **Beating and cursing (13:25):** *descriptive only.* The narrator reports it without comment. **Do not commend it and do not apologise for it; report it as the text does, and let the contrast with Ezra 9:3 do the work.**
- **Driving out the high priest's grandson (13:28):** *descriptive*, and the one action taken against a named individual's person.

**Who Am I?** **Not Nehemiah, and the chapter is where the book says so most clearly** — because the man asking God four times to remember him is the same man whose reforms had to be done twice. The reader's place is with the officials who let it slip while he was away.

### 16. So What? (brief)

**Stage 1 — the author's intended response.** That the reader should see what a signed covenant is worth, and should ask for something better. `[I]` The chapter is not telling anyone to try harder; it is showing what trying produced.

**Stage 2.** Worldview: holiness cannot be secured by a mechanism, and the book has now tested four — register, wall, book, signature. Behaviour: the honest stop/start is not "be more like Nehemiah" but "stop expecting the arrangement to hold without maintenance, and start maintaining it anyway" — which is what 13:30–31 does, without drama, in two verses.

**Motivation.** 13:22. **The book's most self-justifying voice ends on mercy, in the same word it used of its own record.** That is the gospel grounding the chapter itself supplies.

**Four audiences.** *For me:* which of my reforms is already coming undone? *For a Christian friend:* the second time is the tiring one. *For the church:* our covenants need officers, and our officers need portions. *For an unbeliever:* the book's own verdict on religious self-improvement is this chapter.

**Prayer.** The book's own: remember me, my God, for good — and spare me according to the greatness of your lovingkindness.

### Passage-specific difficulties

- **The beating (13:25).** The room will flinch. Report it plainly, note that the Greek of Vaticanus dropped the hair-pulling and that BHS did not think the omission worth a note, and let Ezra 9:3 stand beside it.
- **"Remember me for good" — is this works-righteousness?** The honest answer is that 13:14 sounds like it and 13:22 does not, and the chapter contains both. **Preach both verses or neither.**
- **Driving out the high priest's grandson.** A congregation will ask what happened to him. Josephus has an account; the book does not. `[S]` Do not supply it.
- **The book's ending.** There is no resolution. A preacher who supplies one has finished a book the author left open.

---
## Convergent Findings

The full list of places where several tools agreed within a unit. The top five are in the Headline Findings above; these are the rest.

1. **The book's opposition is always triggered by hearing.** Eight scenes open with "when X heard" — Ezra 4:1; Neh 2:10; 2:19; 3:33; 4:1; 4:9; 6:1; 6:16 — and שמע stands in 27 verses of Nehemiah against 3 of Ezra. *Structure, Repetition, Vocabulary, Positional Necessity (units 4, 9, 10, 12).* `[T]`

2. **The book's two kinds of hearing are its shape.** The enemies hear that the wall is rising and attack; the people hear the Torah and separate (Neh 8:2–3, 8:9; 13:3). *Repetition, Move 4, Author's Purpose.* `[I]` on the design, *moderate-to-high*.

3. **Both of the book's great prayers stop without a petition.** Ezra 9:15 ends "behold, we are before You in our guilt"; Neh 9:37 ends "and we are in great distress". *Structure, Linking Words, Tone (units 8, 15).* `[T]`

4. **The three occurrences of צַדִּיק in the book are all of God, all in prayer, and they bracket the two confessions** — Ezra 9:15; Neh 9:8; 9:33. *Vocabulary, Move 4.* `[T]`

5. **The community's covenant formula is used three times, twice by Nehemiah privately and once by the nation** — Neh 1:5; 9:32 (with Deut 7:9, 21; 10:17). *Vocabulary, Tool 11, Move 4 (units 9, 15).* `[T]`

6. **The book's two inclusive separations are Ezra 6:21 and Neh 10:29**, and its one consecrating separation is Ezra 8:24. *Vocabulary, Author's Purpose, Move 4 (units 5, 7, 16).* `[T]` See Book-Overview Tension 1.

7. **Ezra 7:28 and Ezra 9:9 are the book's only two occurrences of נטה, and both are with חֶסֶד** — a private mercy generalised into a national confession two chapters later. *Vocabulary, Move 4 (units 6, 8).* `[T]`

8. **The "good hand" of God is answered by the one hostile hand in the book, which belongs to the leadership** (Ezra 9:2). *Vocabulary, Repetition, Structure (units 6, 7, 8).* `[T]`

9. **The finding/not-finding thread runs the length of the book.** What cannot be found is a priestly genealogy (Ezra 2:62; Neh 7:64); what is found is a register (Neh 7:5), the Booths law (8:14) and the assembly law (13:1). *Vocabulary, Move 4 (units 2, 12, 13, 14, 19).* `[T]` on the data, *moderate-to-high* on the design.

10. **The same verb carries the understanding of Torah and the understanding of corruption** — בין at Neh 8:2–12 (six verses) and at 13:7. *Vocabulary, Move 4 (units 14, 19).* `[T]`

11. **Nehemiah contends (ריב) four times, and three of them are in the last chapter** — 5:7; 13:11, 13:17, 13:25. *Repetition, Tone (units 11, 19).* `[T]`

12. **Two named builders from ch. 3 reappear compromised.** Eliashib the high priest, who consecrates the Sheep Gate (3:1), prepares Tobiah's chamber (13:4–7) and is the grandfather of Sanballat's son-in-law (13:28); Meshullam son of Berechiah, who repairs two sections (3:4, 3:30), is father-in-law to Tobiah's son (6:18). *Proper-noun inventory, Move 4, Character dossier (units 10, 12, 19).* `[T]` on the identifications.

13. **The doors are the book's quiet index of the project's fate** — hung (3:1–15; 7:1), reported still unhung (6:1), and finally shut against Sabbath trade (13:19). Eleven verses, all in Nehemiah. *Vocabulary, Repetition, Move 4.* `[T]`

14. **The book's joy-vocabulary marks three arrivals and then stops.** Eight verses: the foundation (Ezra 3:12–13), the Passover (6:22), the book (Neh 8:12, 17), the wall (12:27, 43, 44) — and none in ch. 13. *Vocabulary, Tone, Move 4.* `[T]`

15. **The Aramaic block is the book's ketiv-densest stretch** — 17.9% of its verses against 8.0% of Ezra's Hebrew and 4.73% of the whole WLC. *Textual notes, book level.* `[T]` for the measurement; a fact about Leningrad, not about the authors.

---

## Cross-Passage Convergent Findings

**What only becomes visible when the nineteen units are read in sequence.** Every claim here is **synthetic** and is capped at moderate confidence unless the word-level chain is stated as verified.

### 1. The book tests four mechanisms for securing holiness, and reports on each

A register (Ezra 2 // Neh 7), a wall (Neh 3–6), a book (Neh 8), a signature (Neh 10). **Each is introduced as a solution and each is shown, later, not to have held**: the register cannot verify a priest (Ezra 2:62–63; Neh 7:64–65); the wall does not keep Tobiah out (13:4–8); the book is read and then contradicted within three verses (13:1 against 13:4); the signature is broken clause by clause (13:10–27). `[T]` for each pairing; `[I]` for the pattern. **This is the book's argument, and no single unit states it.** *High on the data; moderate-to-high on the design.*

### 2. The forsaking-chain is the spine

עזב, twelve verses. God does not forsake (Ezra 9:9; Neh 9:17, 9:19, 9:31); he once did (9:28); Ezra confesses they forsook the commandments (9:10); Nehemiah proposes forsaking an exaction (5:10); the covenant promises not to forsake the house (10:40); the house is found forsaken (13:11). **Verified by lemma, gated with `find.py verify`, exit 0, and carried in Greek at ten of the twelve.** `[T]` *High — this is the one cross-passage chain in the sweep that is not capped.*

### 3. Deuteronomy is used three ways, and the book never argues from a prophet

The three uses: **as legal ground** (Deut 7 and 23 at Ezra 9:1, 9:12; Neh 10:31; 13:1–3, 13:25); **as prayer** (Deut 30:1–4 at Neh 1:8–9); **as recital** (the whole exodus-to-conquest sequence at Neh 9:9–25). `[T]` **Against this stands the prophetic material: Jeremiah is named once (Ezra 1:1) and quoted by idiom once (1:1, from Jer 51:11); Haggai and Zechariah are named as men, not quoted.** `[T]` **The book's argument is Torah-shaped throughout, and its one appeal to a king is to Solomon's failure (13:26).** *High.*

### 4. Every citation the community makes, it also adapts

Ezra 9:1 splices Deut 7 and Deut 23 into one nations-list; Neh 8:15's branch-list matches Lev 23:40 in substance and not in wording, and adds trees; Neh 10:32b combines the fallow-year with the debt-release, which the Torah keeps apart; Neh 10:33 sets the temple tax at a third of a shekel where Exod 30:13 sets a half. `[T]` for each. **Four adaptations, and the narrator comments on none.** *Moderate-to-high, and a genuinely under-preached pattern.*

### 5. The two halves have different vocabularies and the same problem

דרש 5/0 toward Ezra; ירא 0/10, דלת 0/11, חֶרְפָּה 0/4, חוֹמָה 0/28, זכר 0/9 toward Nehemiah. `[T]` **And both halves end at the same place**: Ezra 10 with an unexplained list of men who had married foreign wives, Neh 13 with the same sin and a beating. *High on the counts; moderate on the reading.*

### 6. The book plants its adversary's disqualification at his first appearance and reads it out eleven chapters later

Tobiah **הָעַמֹּנִי** (2:10, 2:19) → Deut 23:4 read aloud (13:1) → Tobiah in the chamber (13:4–8). `[T]` **And the name itself is the book's one sustained pun**: "Yah is good", grieved that good is sought (2:10), his "goods" recited in the governor's presence (6:19), in a book that ends asking God to remember its author **for good**. *Moderate-to-high, and the sweep's best single narrative finding.*

### 7. The Sabbath is confessed, then sworn, then broken, in that order

שַׁבָּת in ten verses, all Nehemiah: the prayer (9:14), the covenant (10:32, 10:34), and the relapse (13:15, 16, 17, 18, 19, 21, 22 — seven of the ten). `[T]` **The count is the shape.** *High on the count.*

### 8. The book's registers do the narrative work its plot does not

Four major lists — Ezra 2, Ezra 10:18–44, Neh 3, Neh 7, Neh 11–12:26 — and each one is load-bearing: Ezra 2 defers the priestly question; Ezra 10's list ends without an outcome; Neh 3 names the trades and plants Eliashib and Meshullam; Neh 7 is the frame's closing bracket and the finding of a book; Neh 11–12 supplies the succession that makes 13:28 intelligible. `[T]` **A series that skips the lists loses five findings.** *Moderate-to-high.*

### 9. Two men, one sin, two temperaments, one rare verb

Ezra 9:3 and Neh 13:25, מרט, the only two in the book and two of eleven in the canon — one of the other nine being Isa 50:6. `[T]` *High on the data; moderate-to-high on the Servant trajectory.* See sweep Headline Finding 2.

### 10. The book ends on the question it asked at the beginning, unresolved

Ezra 2:63 asks for a priest who will **stand** with Urim and Thummim; Neh 7:65 asks again; Neh 13:29 records that the priesthood has been **defiled**. `[T]` **Between them the book uses עמד 34 times and makes everyone else stand.** *High on the data; moderate-to-high on the irony.*

### 11. Joy, and then nothing

The joy-vocabulary's eight verses stop at 12:44. Chapter 13 has no joy-word, no praise-word, and no feast — and it is the chapter in which the Sabbath, the festivals' own anchor, has to be enforced by shutting gates. `[T]` **Admissible as a pattern-break absence**, because the pattern is established by the book's own eight verses; *capped at moderate*, per the absence rule.

### 12. The empire remembers by filing; the book asks God to remember without a file

Aramaic דָּכְרָן at Ezra 4:15 ×2 and 6:2; Hebrew זִכָּרוֹן once (Neh 2:20) and זכר nine times, six of them petitions. `[T]` **The book's two languages carry its two theories of memory, and it ends on the second.** *Moderate-to-high.*

---

## Preaching Pitfalls

Common ways this book gets mishandled. The overview's six traps stand and are not repeated in full; these are the ones the sweep's own work surfaced or sharpened.

### Pitfall: preaching Neh 10 without Neh 13

- **What it looks like:** "Let us covenant together as a church, as they did in Nehemiah 10."
- **Why it's wrong:** the author wrote ch. 13 so that ch. 10 could not be read that way. The community's covenant is an **experiment whose result the book reports**, and the result is that the clauses were broken in order, in the covenant's own words.
- **The corrective:** preach the pair. The gospel point is not "sign better" but that the failure of a sealed page is Jeremiah's argument for a covenant written on hearts — the very promise Nehemiah's own prayer stopped one verse short of quoting (Deut 30:6, at Neh 1:9).

### Pitfall: reading "the holy seed" as a racial category

- **What it looks like:** a sermon on Ezra 9 that is either embarrassed about ethnic purity or defends it.
- **Why it's wrong:** **both the NASB95 and the ESV render זֶרַע הַקֹּדֶשׁ as "the holy race"** at Ezra 9:2, and the congregation hears a modern category. The Hebrew is "seed", and the book's own classification of the offence is **מַעַל** — the priestly term for trespass against holy things (Lev 5:15; Num 5:6) — which appears in seven verses of this book.
- **The corrective:** say "seed"; name the מַעַל field; note that the ground Deuteronomy itself gives is the turning of the heart (Deut 7:4), which is exactly the ground Neh 13:26 gives from Solomon; and note that Ruth the Moabite and the Egyptian of Deut 23:9 are in the same canon.

### Pitfall: quoting "the joy of the LORD is your strength" as a maxim

- **What it looks like:** the verse on a banner, meaning roughly "cheer up".
- **Why it's wrong:** it is a command to stop weeping on one specific holy day, it has a meal attached, and its stated cause two verses later is that **they understood the words** (8:12). **And the noun חֶדְוָה occurs twice in the Hebrew Bible** — here and at 1 Chr 16:27, in David's psalm at the ark's installation, where it also stands beside a strength-word.
- **The corrective:** preach the whole verse with its meal and its "send portions to those who have nothing ready", and — if the 1 Chr 16:27 link is judged to hold — preach it as the claim that what belongs in God's sanctuary has arrived in a public square where a book is being read.

### Pitfall: treating the two reformers as a model to choose between

- **What it looks like:** "Ezra the gentle scholar" against "Nehemiah the decisive leader", with a recommendation.
- **Why it's wrong:** the book gives them the same rare verb — מרט, which it uses only twice — and has Ezra tear his own hair and Nehemiah tear other men's. **The narrator reports both and adjudicates neither.**
- **The corrective:** let the contrast stand, and note where the canon puts the gesture in a third place: on the cheeks of the Servant, who receives it (Isa 50:6).

### Pitfall: stopping the series at Neh 12

- **What it looks like:** a triumphant final sermon on the two choirs.
- **Why it's wrong:** Preaching Trap 4, and the sweep sharpens it. **12:44–47 reports the storerooms staffed and the portions given; 13:4–10 reports a storeroom given to Tobiah and the portions stopped.** The author put the working system and its collapse in consecutive paragraphs.
- **The corrective:** if the series must end on a high note, end it on 13:22 — which is a higher note than 12:43, because it is mercy rather than celebration.

### Pitfall: supplying the ending

- **What it looks like:** a final sermon that resolves the book — "and so God was faithful to his people."
- **Why it's wrong:** the book stops on a petition. It has no cadence. The priesthood is defiled (13:29), the question of Ezra 2:63 is unanswered, and the last four words ask God to remember.
- **The corrective:** let it stop. The unanswered question is the book's strongest pointer to Christ, and answering it on the book's behalf removes the pointer.

### Pitfall: tidying the numbers

- **What it looks like:** a defence of Ezra 2's arithmetic, or of the divergences between Ezra 2 and Neh 7.
- **Why it's wrong:** the narrator printed an itemised list that does not match its own stated total, and then printed a second copy with different numbers and the same total. **He is showing documents, not reconciling them.**
- **The corrective:** say what the documents are for, and let the figures alone.

---

## Open Questions / Uncertainties

1. **The seam at Neh 7:72 / 8:1.** Contested, as the overview says. **The sweep's own evidence slightly favours the overview's division** (the register functions administratively toward ch. 11's lot; the assembly of 8:1 is third-person and brings Ezra back), **but the Hebrew joins 7:72b to 8:1 with the same seventh-month clause that opens Ezra 3:1, so there is no clean break.** Still contested; a solo dig on Neh 7–8 should test it.

2. **The Isaiah 56–66 chain from the imported overview, six references, still untested.** The sweep adds one nearby datum that a claim audit should take up: **עִיר הַקֹּדֶשׁ ("the holy city") stands at Neh 11:1, 11:18 and, in the Hebrew Bible, at Isa 48:2; 52:1; Dan 9:24.** Isa 52:1's context — "the uncircumcised and the unclean will no longer come into you" — is thematically exact for a book that ends with an Ammonite in the temple. **Not a finding; a lead.**

3. **The 1 Chr 16:27 → Neh 8:10 allusion.** The lexical data are certain (two occurrences in the canon, both beside a strength-word; verified, exit 0). **Whether the allusion is intended is moderate-to-high and would repay a solo dig**, because it would change how the book's most-quoted verse is preached.

4. **The זֶרַע הַקֹּדֶשׁ / Isa 6:13 link.** The phrase differs by the article and the contexts pull in opposite directions. **Flagged, not claimed.** Needs a solo dig or a claim audit.

5. **Does Nehemiah confess to charging interest (5:10)?** The Hebrew says he and his were lending; the demand is to abandon **הַמַּשָּׁא הַזֶּה**, which may be the interest or the claim. **Genuinely open.** The overview's audit was right to call the import's "confesses his own predatory lending" overstated.

6. **מְפֹרָשׁ at Neh 8:8** — "distinctly" or "translated". **The NASB95 and the ESV take opposite sides.** The same word stands at Ezra 4:18 of a letter read before the king, which is some support for "translated" but not decisive. **Open.**

7. **The direction of dependence at 2 Chr 36:22–23 // Ezra 1:1–3a.** Reported by the overview, unresolved, and the sweep adds nothing. **Leave open.**

8. **The temple tax at a third of a shekel (Neh 10:33) against Exodus's half.** The fact is certain; the explanation is not. Economic hardship, a different reckoning, and a deliberate adjustment are all live. **Open, and worth a Logos pass.**

9. **Neh 6:1's פֶּרֶץ and Neh 11:4, 11:6's "sons of Perez" — considered and rejected.** The consonants are identical and the lemmas differ (6556 / 6557). Nothing in either context corroborates a pun, and the hard rule for sound-based claims requires corroboration. **Recorded here so that a later run does not re-derive it as a finding.**

10. **Closed by the corpus in this run, and recorded so the gate can be seen working:** whether the Greek omits the hair-pulling at Neh 13:25. **It does not** — Rahlfs has ἐμαδάρωσα; the omission is Vaticanus's, and BHS carries no apparatus note there. A claim resting on Swete alone would have been wrong.

11. **The skill's own ketiv figures (Phase 10.5, item e3) do not reproduce.** Measured against this corpus by the gate's own definition: whole WLC **4.73%**, Ezra **10.4%** — against the gate's stated 16.8% and 52.9%. **The lesson stands and is better supported than before; the numbers need correcting or their definition stating.** Drafted as a candidate amendment; not applied.

---

## Book-Overview Tensions

Surfaced, not resolved. The overview is a strong, recently built, clean-room document and the sweep confirms the great majority of it. Five places warrant revisiting.

### 1. The separation count is short by three, and one of the three changes the picture

The overview lists **בדל at Ezra 6:21; 9:1; 10:11, 10:16; Neh 9:2; 10:29** — six. **The lemma index gives nine: Ezra 6:21; 8:24; 9:1; 10:8; 10:11; 10:16; Neh 9:2; 10:29; 13:3.** `[T — verified]`

The consequential addition is **Ezra 8:24**, where Ezra **separates twelve priests to carry the temple silver** — a consecrating separation, setting apart *for* service. Together with Ezra 6:21 and Neh 10:29, where the participle הַנִּבְדָּל describes people separating *to* join the community, **the book's separation-verb works in three directions, not one.** The overview's Christological section says the root "works by exclusion: purity is preserved by keeping the unclean out", and warns against the cheap contrast with the gospel. **The sweep's evidence makes the warning stronger and the premise weaker**: the book's own vocabulary already includes separation that admits and separation that consecrates. **Worth correcting in the overview, because it improves the overview's own argument.**

### 2. The echo table is missing three pairs the corpus verifies

Each is `[T]`, verified by lemma, and each is as strong as several already in the table:

- **Ezra 4:3 // Neh 2:20** — the two refusals of standing, one at each half's first opposition scene.
- **Ezra 9:3 // Neh 13:25** — מרט, the only two in the book, eleven in the canon.
- **Neh 10:40 // Neh 13:11** — עזב, the covenant clause and its prosecution, in the same words.

And two more worth considering: **Neh 1:8 // 13:27** (מעל), and **Ezra 6:22 // Neh 12:43** (שִׂמְּחָם).

### 3. The intertextual map is missing Deut 33:4, and it is a strong entry

**קְהִלָּה occurs in exactly two verses of the Hebrew Bible: Deut 33:4 and Neh 5:7.** `[T — verified across all 23,213 WLC verses]` That is a rarer chain than several the map already carries at "high", and it belongs both in the map and in the canonical-position block's **Presupposes** field.

### 4. The unit title "The longest prayer in the Bible" needs a qualifier

Neh 9:6–37 is **495 words** against 1 Kgs 8:23–53's **488** (WLC). `[T — measured]` True by seven words, and only on one way of setting the boundaries. **Either qualify the title or drop the superlative**; a preacher who repeats it from the pulpit and is checked will lose credit he needs later in the series.

### 5. The "prophet-light" characterisation is right and could be sharper

The overview says the book "names only three prophets in all". **The sweep confirms this and can add the mechanism**: Jeremiah is named once and quoted only by idiom; Haggai and Zechariah are named as living men whose preaching restarts a site, and **neither is quoted at all**; and **the whole of Neh 3–7 contains no Scripture citation of any kind.** `[T]` The book's argument really is carried by internal repetition rather than external citation, exactly as the overview's instruction to "lean on Move 4 before Move 2" anticipated — and this sweep's experience confirms that instruction emphatically: **of the roughly forty new findings below the headline level, all but four came from Move 4.**

**Everything else in the overview that this sweep touched, it confirmed** — including the verse totals, the Aramaic extent (independently reproduced at 67 verses), the מַעַל count of seven verses, the עלה audit finding that all 27 occurrences are physical, the twelve occurrences of "the God of heaven" bracketed between Ezra 1:2 and Neh 2:20, the covenant-clause table, and the four Deuteronomy phrases.

---

## Text-First Declaration

**Secondary sources present in context:** the book-overview (`book-overview-ezra-nehemiah.md`, v1.1) and, through it, the import-versus-fresh claim audit (`claim-audit-ezra-nehemiah-import-vs-fresh.md`). The overview's own `[S]` sources — Batten, Manor, Young, Lohr & Kaminsky, Eskenazi, Blenkinsopp, Japhet, Bledsoe & Seal — **were not opened in this run** and nothing here adds to their standing. **No Logos pass was run in this sweep**; the overview's, run four hours earlier on the same day, stands as it reported itself.

**Tools worked before secondary sources consulted:** Confirmed, with one honest exception. The overview was front-loaded at Phase 0.5 as a thread-set, as the skill requires, so its microscript, traps and intertextual map were in peripheral vision throughout. Findings inherited from it are tagged `[S: overview]` and are distinguished from the sweep's own, which are marked **Sweep finding** in the units. The claim audit's verdicts were accepted, not re-derived, per Phase 5.5.

**Passage text:** Verified. Ezra and Nehemiah were read complete in the WLC, cover to cover, before any English text was opened. Every Hebrew word quoted in this report was copied from the corpus files, not reconstructed. The NASB95 and ESV were parsed from the Logos exports programmatically (686 and 664 verses recovered respectively); **the ESV export's final line is truncated, so Neh 13:31's closing petition was read from the NASB95 and the Hebrew.**

**Reference files viewed:** Core 01–07, complete. Extensions: `preacher-extras.md`, `historical-background.md`, `original-audience.md`, `original-languages.md`, `textual-variants.md`, `biblical-theology.md`, `difficult-verses.md`, `christological-reading.md`. `_texts/README.md`. `schnittjer-pass.md` **not viewed** — **N/A, the book is not in the Torah.** **The worked example viewed was `Ecclesiastes/dig-deeper-ecclesiastes-sweep.md`**, the most recent completed sweep in the folder, read as the format and depth anchor for Multi-Passage Sweep mode; the genre-matching solo anchor `_skill-examples/psalm-33-worked.md` was **not** opened, on the ground that this run is a sweep and the Ecclesiastes document is the closer and more current calibration. **Recorded as a deviation from the skill's Required-reading rule**, not as a silent omission.

**Depth floors:** Met per report. Nineteen units, five sweep-level headline findings, fifteen convergent findings, twelve cross-passage findings, seven preaching pitfalls, eleven open questions. Every unit carries a Positional Necessity Check and a Move 4 with an explicit result; **no Move 4 returned nil.** Tools 1, 2, 7, 8, 11 and 16 are worked in every unit or covered at book level; Tools 5, 6 and 13 are frequently N/A with reason (the book is documentary narrative with almost no poetry and few imitable characters).

**Chains verified:** **48 recurrence or citation claims were checked by lemma against the WLC before this document was written.** Specifically: חזק, רפה, עזב, עמד, בנה (Hebrew and Aramaic), שמע, ירא, יִרְאָה, דרש, בין, בדל, דלת, חֶרְפָּה, זכר, זִכָּרוֹן, חסד, מרט (book and whole canon), נטה, מעל (verb and noun), שׂמח and שִׂמְחָה, מצא, כתב, קְהִלָּה (whole canon), גּוֹרָל, אֲמָנָה, צַדִּיק, תּוֹרָה, שַׁבָּת, מַעֲשֵׂר, נַעַר, קָהָל, עלה, פרץ and פֶּרֶץ, חֶדְוָה (both Hebrew and Aramaic, whole canon), מָעוֹז, טוֹב, עַם, Tobiah, Sanballat. **Four chains were additionally gated with `find.py verify`, all exit 0:** מרט at Ezra 9:3 / Neh 13:25 / Isa 50:6; עזב at Neh 10:40 / 13:11 / 9:17 / 9:19 / 9:31; חֶדְוָה at 1 Chr 16:27 / Neh 8:10.

**Positive controls.** Every nil return was controlled before being reported as an absence. The nils were: דרש in Nehemiah, ירא / יִרְאָה / דלת / חֶרְפָּה / גּוֹרָל / פרץ / אֲמָנָה / זכר / זִכָּרוֹן / שַׁבָּת / מַעֲשֵׂר / נַעַר / חוֹמָה in Ezra, and נטה in Nehemiah. **The control in each case was the same command with the same book filter returning results for other lemmas in the same batch** — the searches ran over both books in one pass, so a book filter that returned results for חזק and returned none for דרש is a working filter, not a broken one.

**The positive-control rule earned its place in this run.** A final consolidated re-check of 27 headline counts, scripted rather than run by hand, returned **zero for every one of them** — including the ones this report had already verified individually. The single "pass" was the one case whose expected value was zero (דרש in Nehemiah), which is exactly the false-negative the rule exists to catch: **a broken search and a real absence are indistinguishable from the inside.** The cause was mundane — `find.py` writes its summary line to stderr, and the script captured only stdout. Re-run with a **positive control first** (חזק in Nehemiah, expected non-zero, returned 34), the harness was shown working and **all 27 checks then passed, no failures.** Had the control not been run, this report would have been "corrected" against a broken instrument. *(Gate item (e3), Round 5, adopted on trial: this run is one more case where the control fired, and the cause is a fifth distinct one — an output stream, not a spelling.)*

**Counts name their edition.** Every count above is against the **WLC** unless stated; whole-Bible searches ran over the WLC's **23,213 verses**, a figure this sweep reproduced independently. Greek observations are from **Swete** except the Esdras B chapter arrangement, the Neh 13:25 reading, the Neh 2:20 reading and the ἐγκαταλείπω chain, which are from the **Rahlfs-Hanhart** export. The single apparatus reference (Ezra 1:11) is from the **BHS** apparatus and is cited as such.

**Apparatus findings:** **None introduced by this sweep.** No finding below rests on a parashah, an accent, a ketiv or a Masorah reading. The two ketiv observations made (Neh 2:13; Neh 9:17) are **methodological** — they demonstrate why the gate exists — and carry no exegetical weight. The overview's two apparatus notes are carried forward with its witnesses named and were not re-derived. The ketiv-density measurements are stated as facts about **Leningrad's reading tradition as the WLC prints it**, with their manuscript spread expressly **`[unchecked — apparatus spread]`**, and nothing rests on them.

**Three-way triage.** Every Hebrew/Greek divergence reported is classified. **Category 1 (translation loss):** the מרט doublet (two Greek verbs for one root); the Urim-and-Thummim doublet (full at Ezra 2:63, abbreviated at Neh 7:65 in both editions); Neh 12:43's five-word root-cluster rendered by four εὐφρ- words; the עזב chain's loss in both English versions, which is an English loss and not a Greek one. **Category 2 (substantive variant, no default):** Ezra 1:11's vessel total against 1 Esdras 2:11; the MT's absence of the English Neh 7:68; Neh 2:20's καθαροί in both Greek editions; Neh 9:17's בְּמִרְיָם against 𝔊's ἐν Αἰγύπτῳ; 1 Esdras's relocation of Ezra 4:7–24 and removal of Nehemiah; Swete's omission at Neh 13:25. **No category-2 divergence is resolved by a blanket preference for either text, and on none does this sweep take a position beyond reporting both readings with their evidence.** **Category 3 (the NT's own text):** none — the New Testament does not cite this book.

**Warrant counts:** `[T]` 302 · `[I]` 40 · `[S]` 59 — counted mechanically from the tags in this file, excluding the legend and this line, not estimated.

**Health note.** Text-first and original-language throughout: the substrate was the Hebrew and Aramaic, read complete before any English, and the load-bearing claims are verified counts reproducible in one command. The `[S]` figure is high for a sweep, and all but a handful are the overview's own verified findings carried forward with attribution rather than re-derived — which is the right use of a fresh, clean-room overview and is not a reformatting of it: **of the findings marked *Sweep finding* in the units, none originated in the overview, and three of the five sweep-level Headline Findings are new.** The softest material is the 1 Chr 16:27 allusion at Neh 8:10, the Isa 50:6 trajectory at Ezra 9:3 // Neh 13:25, the "holy city" lead toward Isaiah, and the Tobiah name-play — all flagged at moderate-to-high and all named in Open Questions. **Every cross-passage claim is marked synthetic and capped at moderate except the עזב chain, which is verified end to end and carried in Greek.**

**For the finalise pass, the audit's first targets should be:** the 1 Chr 16:27 link (it would change how Neh 8:10 is preached), the Isaiah 56–66 chain the overview still lists as untested together with the עִיר הַקֹּדֶשׁ lead, and the Tobiah name-play.

---

## Colophon

**Version** 1.0 · **Date** 19 September 2026 · **Mode** Fresh Exegesis, Multi-Passage Sweep (19 units) · **Consumes** `book-overview-ezra-nehemiah.md` v1.1 and `claim-audit-ezra-nehemiah-import-vs-fresh.md`

**Status.** Planning material, not pulpit preparation. **For any ⭐ unit, run a full solo dig before preaching it.** Ten units are ⭐ on the overview's marking — Ezra 1; Ezra 3; Ezra 4; Ezra 7; Ezra 9–10; Neh 1–2; Neh 5; Neh 8; Neh 9; Neh 13 — and the sweep does not propose changing any of them. **The two that would repay a solo dig first are Neh 8** (the חֶדְוָה finding and the מְפֹרָשׁ crux) **and Neh 13** (four verified chains converge there).

**Handoff.** This sweep is ready to be consumed by a **Finalise pass on the overview** (five tensions above, three of them straightforward corrections) and by **`/point-purpose`** for any of the ten ⭐ units. A **macro-synthesis** should wait: the prerequisite gate requires solo digs on all or nearly all pericopes, and there are none yet.
