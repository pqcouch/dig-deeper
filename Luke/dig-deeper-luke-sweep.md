# Dig Deeper: Luke — Whole-Book Sweep

**Mode:** Multi-Passage Sweep — 34 pericopes, Luke 1:1–24:53, merged from the book overview's 60 preaching units at the Greek seams
**Primary text (observation):** SBLGNT with the MorphGNT word index, `_texts/greek-nt-sblgnt/03-Luke.txt` and `_index/03-Luke.tsv` — 1,149 verses, 24 chapters, read in Greek before any English
**Majority text (collated):** Robinson–Pierpont 2018, `_texts/source/byzantine-rp2018/03-Luke-RP2018.csv` — 1,150 verses
**Citation of record:** NA28 text and apparatus, `_texts/logos-exports/02-New-Testament/03-Luke-NA28.txt` and `03-Luke-NA28-apparatus.txt`
**Greek OT:** Swete, `_texts/greek-lxx-swete/` (observation only — Rahlfs-Hanhart was not opened)
**Hebrew OT:** WLC, `_texts/hebrew-wlc/`, checked with `tools/find.py`
**Study text:** NASB95, `_texts/logos-exports/02-New-Testament/03-Luke-NASB95.txt`
**Pulpit text:** None — no sermon in view. A sweep declares no pulpit text, and none has been invented
**Book-overview context:** `Luke/book-overview-luke.md`, Draft v0.1.0 (27 September 2026)
**Date:** 27 September 2026

---

## How to Read This Sweep

This is planning material, not pulpit preparation. Thirty-four pericopes at proportional depth cannot each receive what a solo run gives one passage, and checking is the first thing proportional depth cuts. Four consequences govern everything below.

**Every cross-passage claim is synthetic and capped at moderate confidence** until a claim audit has tested it — except where the report says a chain has been verified by lemma against the SBLGNT index, which most of the chains here have been. The verified ones say so; treat the rest as candidates.

**For any ⭐ pericope, run a full solo dig before the pulpit.** Sweep depth is enough to plan a series and to audit an overview. It is not enough to preach from.

**Each pericope is worked in the same order**: its position in the book (the two Phase 0.6 questions), its structure, the text-first findings, the Old Testament citations with the Citation Triad on every direct quotation and high-confidence allusion, the internal echoes (Move 4), and whichever of the remaining tools the passage makes live — Copycat, Translations, a difficulty, a pitfall. Tools that add nothing at sweep depth are not listed pericope by pericope; the book-level Tools 12 (Genre) and 14 (Bible Timeline) are stated once below and hold throughout unless a pericope says otherwise.

**Warrant tags.** `[T]` derivable from the text on the page · `[I]` a reasonable inference from it · `[S]` supplied by a secondary source and held provisionally. Counts name their edition, because a count belongs to a text, not to a book. Greek and Hebrew stand in their own script with the English in brackets after them, every time.

**One independence caveat, stated plainly.** The overview this sweep consumes was drafted in this same session, earlier today, by the same model. A sweep that re-reads its own overview can only agree with it unless it deliberately works from the Greek first. Every pericope below was re-read in the SBLGNT before the overview's claims about it were consulted, and every overview claim the sweep tested is reported in *Book-Overview Tensions* whether it held or not. But the reader should weigh the confirmations accordingly: an overview confirmed by its own author is a weaker thing than an overview confirmed by an independent run.

**What the corpus showed at the outset.** SBLGNT Luke has 1,149 verses. It has no 17:36 (absent also from the Majority text) and no 23:17 (present in the Majority text); the NASB95 prints both, bracketed. **The SBLGNT text file carries NA-style variation sigla (⸀ ⸂ ⸃) inside the words**, and a surface search that does not strip them misses verses silently: a first search for τί ποιήσωμεν ("what shall we do?") returned 3:14 and missed 3:10 and 3:12, where a siglum sits before the verb. The positive control caught it; the search tool was corrected and every surface search in this report was run after the fix. Lemma searches are unaffected.

---

## Headline Findings

Five book-level findings that emerged from several tools converging, each verified against the corpus rather than recalled.

**1. The necessity is scriptural, and so is the cure for blindness.** δεῖ ("it is necessary") stands in 18 verses (SBLGNT), from the boy in his Father's house (2:49) to the risen Lord's last word (24:44). Beside it runs a chain of not-understanding — συνίημι ("to understand"), κρύπτω ("to hide"), παρακαλύπτομαι ("to conceal") at 2:50; 9:45; 18:34; 19:42 — broken only when he διήνοιξεν αὐτῶν τὸν νοῦν τοῦ συνιέναι τὰς γραφάς ("opened their minds to understand the Scriptures", 24:45). Abraham's "if they do not listen to Moses and the Prophets, they will not be persuaded even if someone rises" (16:31) is the book's own theory of certainty, and Luke 24 enacts it. *Verified; confidence high.*

**2. The book ends by doing what it opened by promising.** A priest who cannot bless (1:21–22) against the risen Lord who lifts his hands and blesses in Aaron's gesture (24:50; Lev 9:22 Swete); "great joy" announced (2:10) and returned (24:52); the righteous man waiting (2:25; 23:50–51); ἐπιγινώσκω (1:4; 24:16, 31); διανοίγω (2:23; 24:31, 32, 45). The Gospel is framed by the temple and the priestly blessing, and the Spirit is promised but withheld (24:49). *Verified; synthetic, moderate–high.*

**3. One visitation, two outcomes.** God "visits" (1:68, 78; 7:16); the city "did not know the time of your visitation" (19:44), in the exact words of Jer 6:15 Swete — an oracle of false peace and siege; "these are days of vengeance" (21:22), in Hos 9:7's Greek, where the Hebrew reads "days of visitation". The same noun ἐκδίκησις names God's vindication of his elect (18:7–8). *Verified in Greek and Hebrew; the design is moderate–high.*

**4. The cross is told in the book's own vocabulary.** The disciple's cross carried "behind Jesus" (23:26; 9:23); the scoffers' verb (16:14 → 23:35, its only two NT uses); Peter's "Christ of God" (9:20 → 23:35); three tests to "save yourself" against the three wilderness tests; the last of eleven σήμερον ("today", 23:43); the centurion's δίκαιος ("righteous", 23:47; Isa 53:11) and ὄντως ("truly", → 24:34); and the crowds beating their breasts at a distance, like the tax collector who went home justified (18:13 → 23:48–49). *Verified; synthetic, high for the chains.*

**5. The Last Supper is a covenant meal in both its halves.** The cup is ἡ καινὴ διαθήκη ("the new covenant", 22:20); the kingdom is given with the cognate verb, διατίθεμαι ὑμῖν, καθὼς διέθετό μοι ὁ πατήρ μου βασιλείαν ("I covenant to you a kingdom, as my Father covenanted to me", 22:29) — the verb-and-noun pair of both source texts (Exod 24:8; Jer 38:31 Swete). The blood "poured out for you" uses the verb of "the blood of all the prophets, poured out" (11:50 → 22:20). And the Isa 53:12 quotation at 22:37 follows the Hebrew's "with transgressors", not the Septuagint's "among". *Verified; the NASB95's "grant" at 22:29 hides the covenant verb.*

---

## Book-Overview Active Layer (Phase 0.5)

The four threads were extracted from the Draft overview before any pericope was worked, and held in peripheral vision.

| Thread | What is live across the book |
|---|---|
| **Christological trajectory** | Son of the Most High and Son of God (1:32, 35; 3:22, 38; 22:70); David's heir and King (1:32–33; 18:38; 19:38; 23:38, 42); σωτήρ ("Saviour") twice, of God (1:47) and of Jesus (2:11); the narrator's ὁ κύριος ("the Lord") from 7:13; the prophet like Moses and greater than Elijah; the Servant (22:37; 23:35, 47); the Son of Man (24 occurrences). In the one who comes, Israel's God visits (1:68, 78; 7:16; 19:44) |
| **Intertextual map** | Live sources, ranked: Isaiah (≈16 locations), Psalms (≈15, weighted to chs. 19–23), Deuteronomy (8), the Elijah–Elisha cycle (7), Exodus (7), Abraham and Sarah (6+), Daniel (5), Malachi 3 (4–5), Jeremiah (4), Leviticus (4), 1 Samuel (3), Ezekiel 34 (2). **For Move 2:** every source is tracked across the book below, pericope by pericope |
| **Preaching traps** | (1) the poor without the ἄφεσις ("release"); (2) parables as moral tales; (3) supersession; (4) Christmas sentiment; (5) "the kingdom within you" (17:21); (6) Luke without Acts, or Acts read back into Luke |
| **Presenting situation** | ἀσφάλεια ("certainty", 1:4) for a catechised reader, under the strain of a crucified Messiah refused by Jerusalem's rulers, whose salvation goes out to the nations. `[I]` — a reconstruction from the prologue and the book's own strain-points, not a text statement |

**Monograph-sourcing flag.** The overview draws on no single monograph; its `[S]` material is general knowledge of the literature (authorship, date, the Western order of the Gospels, chiastic schemes for the journey). None of it is load-bearing for the pericope work below.

---

## Book-Level Positional Frame (Phase 0.6)

**What the preceding movement set up.** For a Gospel the preceding movement is the canon it presupposes and the prologue it opens with. The Scriptures are named at the end as "the Law of Moses and the Prophets and the Psalms" (24:44), and the book's whole claim is that what happened was written there beforehand. The prologue sets the purpose: Theophilus is to know τὴν ἀσφάλειαν ("the certainty") of what he has been taught (1:4) `[T]`.

**Why the book exists here.** Because "many" have compiled accounts already (1:1) `[T]`, and this one exists to give an *ordered* account (καθεξῆς ("in consecutive order"), 1:3) that produces certainty. The strain on that certainty is visible in the book itself: the disciples cannot understand (9:45; 18:34), the Emmaus pair's hope has collapsed (24:21), and the leaders refuse what the people receive (19:47–48; 23:35) `[T]`. The book's answer is its most repeated word — δεῖ ("it is necessary"), 18 verses in the SBLGNT — and the risen Jesus' last word on it: οὕτως γέγραπται ("thus it is written", 24:46) `[T]`.

**Implication for every pericope.** Each passage is read for its contribution to an ordered account of fulfilment. Where a pericope seems self-contained — a parable, a healing, a meal — the positional question asks what it contributes to the certainty the prologue promised.

**Book-level Genre (Tool 12).** Narrative — a διήγησις ("account", 1:1), with embedded canticles (1:46–55, 68–79; 2:14, 29–32), a genealogy (3:23–38), parables, discourse (6:20–49; 12; 21:5–36) and table-talk (14:1–24; 22:14–38). Reading rules: it happened, it is theologically shaped, and the narrator's comments are authoritative (Tool 6). Parables carry one main thrust and are not allegorised detail by detail; the eschatological discourse is prophetic-apocalyptic vision-language (21:25–27) set inside a historical prediction (21:20–24).

**Book-level Bible Timeline (Tool 14).** The events stand at the hinge of the timeline: the promises to Abraham and David (1:55, 73; 1:32) are being kept; the incarnation, cross, resurrection and ascension are narrated; Pentecost is promised and withheld (24:49). The reader stands on the far side of all of it, in the time of the proclamation "to all the nations" (24:47), awaiting the Son of Man's coming (21:27). This holds for every pericope, and is not repeated below.

---

## 1. Luke 1:1–4 — That You May Know the Certainty ⭐

**Position.** Q1: nothing precedes but the canon and "many" earlier accounts. Q2: the prologue exists first because it names the purpose every later episode serves — ἀσφάλεια ("certainty") about what was taught — and the method by which it is delivered: an ordered account from those who were there from the start.

**Structure.** One periodic sentence in three members: the occasion (ἐπειδήπερ ("inasmuch as"), 1:1–2: many have compiled a διήγησις ("account") of the things fulfilled among us, as eyewitnesses and servants of the word handed them down); the decision (ἔδοξε κἀμοί ("it seemed fitting for me also"), 1:3: having followed everything carefully from the beginning, to write in order); the purpose (ἵνα ("so that"), 1:4: that you may know the certainty). `[T]`

**Text-first findings.**

- **Four NT rarities in four verses.** διήγησις ("account") and αὐτόπτης ("eyewitness") each stand once in the NT, here; καθεξῆς ("in consecutive order") occurs five times, all in Luke–Acts (Luke 1:3; 8:1; Acts 3:24; 11:4; 18:23); ἀσφάλεια ("certainty") occurs three times (Luke 1:4; Acts 5:23; 1 Thess 5:3). All four verified by lemma in the SBLGNT. `[T]` The register is literary Greek, and it stops abruptly at 1:5.
- **"Fulfilled", not merely "accomplished".** πεπληροφορημένων (πληροφορέω, "to fulfil, bring to full measure", 1:1) is rendered "accomplished" by the NASB95. Elsewhere in the NT the verb means "fully convinced" (Rom 4:21; 14:5) or "fully carry out" (2 Tim 4:5, 17). The book's recurring fulfilment vocabulary — πληρόω ("to fulfil") at 1:20; 4:21; 24:44 — makes the stronger sense likely here. `[T]` for the data; `[I]` for the reading, moderate–high.
- **The witnesses are not the author.** The writer places himself among those to whom the tradition "was handed down" (παρέδοσαν ἡμῖν ("they delivered to us"), 1:2), distinct from the αὐτόπται ("eyewitnesses") and ὑπηρέται τοῦ λόγου ("servants of the word"). `[T]`
- **Κατηχήθης ("you were taught", 1:4)** — a verb of instruction used in Acts of Apollos (18:25) and of teaching about Paul (21:21, 24). Theophilus has already been instructed; the book confirms, it does not introduce. `[T]`
- **The style shift at 1:5 is itself a datum.** From one periodic sentence the narrative moves into the idiom of the Greek Scriptures: Ἐγένετο ἐν ταῖς ἡμέραις ("it came about in the days", 1:5). Twenty-seven verses of Luke begin with (Καὶ) ἐγένετο ("and it came about"), against two in Mark, five in Matthew and ten in Acts (SBLGNT, counted with the sigla stripped — the overview's figure of 26 missed a verse where a siglum stands before the word). `[T]` The book announces in its grammar that it is continuing Israel's scripture. `[I]`, high.

**Tool 11.** No quotation. The prologue has the form of a Hellenistic historiographical preface (Josephus, *Against Apion* 1.1; the medical writers) `[S]`, and it names no Scripture.

*Internal:* **plants §24:48** — the αὐτόπται and ὑπηρέται of 1:2 become the μάρτυρες ("witnesses") the risen Jesus commissions (24:48) (moderate–high). **Plants Acts 2:36** — ἀσφάλεια is answered by ἀσφαλῶς ("assuredly") in the conclusion of the first sermon (high on the data; moderate that it is designed). **Plants §24:47** — ἀπ' ἀρχῆς ("from the beginning", 1:2) against ἀρξάμενοι ἀπὸ Ἰερουσαλήμ ("beginning from Jerusalem", 24:47) (uncertain).

**Translations.** The NASB95's "the exact truth" (1:4) catches ἀσφάλεια's accuracy and loses its *security*. Its "accomplished" (1:1) keeps the event and loses the fulfilment. Neither is wrong; both narrow.

**Pitfall.** Reading καθεξῆς as "in strict chronological order" and then worrying about Luke's differences from Mark. The word's other uses show ordered *sequence* for the purpose of understanding: at Acts 11:4 Peter explains the Cornelius events to Jerusalem καθεξῆς, and the order is the argument. The corrective: an ordered account is an account arranged to persuade, which is what 1:4 says it is for.

---

## 2. Luke 1:5–25 — A Priest Struck Silent

**Position.** Q1: the prologue promised an account "from the beginning". Q2: the beginning is here because Luke's story starts where Israel's did — a righteous, aged, barren couple — and in the one place the story must end: the temple. The first scene sets up the last (24:50–53).

**Structure.** Setting (5–7: the couple, righteous and childless); the appearance in the sanctuary (8–12); the announcement (13–17); the question and the sign (18–20); the waiting people and the mute priest (21–23); Elizabeth's conception (24–25).

**Text-first findings.**

- **Righteous and barren.** δίκαιοι ἀμφότεροι … ἄμεμπτοι ("both righteous … blameless", 1:6) `[T]`. Barrenness here is not judgement; the narrator rules that out before the problem is stated. στεῖρα ("barren") occurs three times in Luke — 1:7, 1:36 and 23:29, where Jesus tells the daughters of Jerusalem that the days are coming when they will say μακάριαι αἱ στεῖραι ("blessed are the barren") — verified by lemma. The book opens with barrenness overcome and closes it with barrenness called blessed, because of what is coming on the city. `[T]` for the data; `[I]` for the design, moderate.
- **The hour of incense and the waiting people.** Zechariah is chosen by lot θυμιᾶσαι ("to burn incense", 1:9) while πᾶν τὸ πλῆθος … τοῦ λαοῦ ("the whole multitude of the people", 1:10) prays outside. Gabriel appears at the altar of incense. In Daniel, Gabriel comes "at the hour of the evening offering" (Dan 9:21, Swete ἐν ὥρᾳ θυσίας ἑσπερινῆς) `[T]`. The only two angels named in the Hebrew canon are Gabriel and Michael, both in Daniel; the one who appears here is the one who explained the seventy weeks. `[T]` for the name; `[I]` for the evocation, high.
- **The mute priest.** Zechariah comes out κωφός ("mute", 1:22) and cannot speak to the people who were προσδοκῶν ("waiting for", 1:21) him. After the incense a priest came out and blessed the people (Num 6:22–27; Sir 50:20–21, Simon the high priest lifting his hands after the offering) `[S]` for the liturgical practice. The blessing the scene leads the reader to expect does not come. `[I]`, moderate–high. See *Internal*.
- **The first δεῖ-shaped word: fulfilment.** οἵτινες πληρωθήσονται εἰς τὸν καιρὸν αὐτῶν ("which will be fulfilled in their proper time", 1:20) — the first use of πληρόω ("to fulfil") in the narrative, spoken by Gabriel about his own words. `[T]`

**Tool 11.**

**Mal 3:23–24 (Eng 4:5–6; Swete 4:4–5) → 1:17** *(high — named figure plus distinctive wording)*. *Source context:* the last words of the Twelve. The LORD will send Elijah before the great day, who will turn the hearts of fathers to sons, "lest I come and strike the land with a curse" — the Prophets close on a threat and a forerunner. *Book usage:* first use; Malachi returns at 1:76 (Mal 3:1), at 1:78 (Mal 3:20, the sun of righteousness rising — see pericope 4) and explicitly at 7:27 (Mal 3:1). Luke works through the last chapter of Malachi in his first chapter. *OT-to-OT:* Sir 48:10 already reads Malachi's Elijah as the one who will ἐπιστρέψαι καρδίαν πατρὸς πρὸς υἱόν ("turn the heart of a father to a son") and "restore the tribes of Jacob" — the passage was in conversation before Luke reached it. *Triage (category 3, the NT's own text):* Luke's ἐπιστρέψαι καρδίας πατέρων ἐπὶ τέκνα ("to turn the hearts of fathers to children") is closer to the Hebrew וְהֵשִׁיב לֵב־אָבוֹת עַל־בָּנִים ("he will turn the heart of fathers to sons") and to Sirach than to Swete's ἀποκαταστήσει ("he will restore"). *What it adds:* the story begins exactly where the Prophets stopped. Luke's first announcement answers the last line of the Nevi'im, and the "curse" that line threatened is what the forerunner comes to avert.

**Gen 15:8; 18:11–14 → 1:7, 18** *(high — exact phrase)*. *Source context:* Abram, promised the land, asks Δέσποτα Κύριε, κατὰ τί γνώσομαι ("O Lord God, how may I know?", Gen 15:8) and receives a covenant ceremony; Abraham and Sarah are πρεσβύτεροι προβεβηκότες ἡμερῶν ("old, advanced in days", Gen 18:11), and the LORD asks whether anything is impossible for him (18:14). *Book usage:* first use; the Abraham thread runs through the book (1:55, 73; 3:8; 13:16; 16:22–30; 19:9). *OT-to-OT:* Gen 15 and 18 are one promise told twice, the covenant and the laughter. *What it adds:* Zechariah asks Abraham's question in Abraham's words — κατὰ τί γνώσομαι (1:18) — and is struck mute where Abraham was given a sign. The scene places Zechariah inside the Abraham story and then marks the difference.

**Num 6:3 → 1:15** *(moderate–high)*. Move 1 only: οἶνον καὶ σίκερα οὐ μὴ πίῃ ("he shall drink no wine or strong drink") is the Nazirite abstinence. σίκερα ("strong drink") stands once in the NT. 1 Sam 1:11 Swete adds the same clause to Hannah's vow for Samuel (οἶνον καὶ μέθυσμα οὐ πίεται) `[T]`, so the Samuel overtone that the Magnificat will make explicit is already present.

**Gen 30:23 → 1:25** *(moderate)*. Move 1 only: Rachel's ἀφεῖλεν ὁ θεός μου τὸ ὄνειδος ("God has taken away my reproach"), heard in Elizabeth's ἀφελεῖν ὄνειδός μου.

*Internal:* **plants §24:50–53** — the priest who cannot bless (1:22) against the risen Jesus who lifts his hands and blesses (24:50) and the disciples who are "continually in the temple blessing God" (24:53) (high; see the echo table in the overview, confirmed here). **Plants §7:27** — κατεσκευασμένον ("prepared", 1:17) anticipates κατασκευάσει ("he will prepare", 7:27); κατασκευάζω occurs in Luke at these two places only, verified by lemma, and the second is the Malachi quotation itself (high). **Plants §23:29** — στεῖρα (above). **Plants §24:11, 41** — Zechariah's unbelief (οὐκ ἐπίστευσας ("you did not believe"), 1:20) against the disciples' ἠπίστουν ("they would not believe", 24:11) and ἀπιστούντων ("while they still could not believe", 24:41) (moderate).

**Copycat and Who Am I?** Zechariah is not a cautionary tale about doubt. The narrator has called him δίκαιος ("righteous", 1:6), and the muteness is a sign, not a sentence — it ends in blessing (1:64). He is a *representative* of waiting Israel, righteous and still unable to believe that the promise is now. `[I]`

**Pitfall.** "Don't doubt God like Zechariah." It moralises a sign-narrative, and it ignores that the blessing withheld here is given by Jesus at the end. The corrective: preach Zechariah as Israel waiting at the altar for a blessing that only the Son will give.

---

## 3. Luke 1:26–56 — Nothing Impossible with God ⭐

**Position.** Q1: 1:5–25 has told one annunciation and set its template. Q2: the second annunciation follows because the book is built in paired panels, and the pairing exists to be broken — the second child is greater, and the second hearer believes.

**Structure.** The annunciation to Mary (26–38); the visitation (39–45); the Magnificat (46–55); the return (56). The first panel mirrors 1:5–25 point by point `[T]`:

| Element | Zechariah | Mary |
|---|---|---|
| Gabriel sent | 1:19 | 1:26 |
| Troubled | ἐταράχθη ("he was troubled", 1:12) | διεταράχθη ("she was very perplexed", 1:29) |
| "Do not be afraid" | 1:13 | 1:30 |
| A son; "you will call his name" | Ἰωάννην ("John", 1:13) | Ἰησοῦν ("Jesus", 1:31) |
| "He will be great" | μέγας ἐνώπιον τοῦ κυρίου ("great in the sight of the Lord", 1:15) | μέγας καὶ υἱὸς Ὑψίστου ("great … Son of the Most High", 1:32) |
| The question | κατὰ τί γνώσομαι; ("how shall I know?", 1:18) | πῶς ἔσται τοῦτο; ("how can this be?", 1:34) |
| The outcome | silenced (1:20) | μακαρία ἡ πιστεύσασα ("blessed is she who believed", 1:45) |

**Text-first findings.**

- **The greater son.** John will be "great before the Lord"; Jesus will be "great" and "Son of the Most High", given David's throne, reigning over the house of Jacob εἰς τοὺς αἰῶνας ("for ever"), and of his kingdom οὐκ ἔσται τέλος ("there will be no end", 1:32–33) `[T]`.
- **The overshadowing.** δύναμις Ὑψίστου ἐπισκιάσει σοι ("the power of the Most High will overshadow you", 1:35). ἐπισκιάζω occurs twice in Luke: here and at 9:34, where the cloud of the Transfiguration overshadows the disciples `[T]`, verified by lemma. In Swete's Old Testament the verb stands four times, and the one narrative use is Exod 40:29 (English 40:35): ἐπεσκίαζεν ἐπ' αὐτὴν ἡ νεφέλη, καὶ δόξης Κυρίου ἐπλήσθη ἡ σκηνή ("the cloud overshadowed it, and the tent was filled with the glory of the Lord") `[T]`. The presence that filled the tabernacle comes upon Mary. `[I]`, moderate–high.
- **The two "according to your word"s.** γένοιτό μοι κατὰ τὸ ῥῆμά σου ("may it be done to me according to your word", 1:38). κατὰ τὸ ῥῆμά σου occurs twice in Luke: here and in Simeon's νῦν ἀπολύεις … κατὰ τὸ ῥῆμά σου ("now you are releasing … according to your word", 2:29) `[T]`, verified. Both righteous hearers take their stand on the word spoken.
- **Leaping.** ἐσκίρτησεν τὸ βρέφος ἐν τῇ κοιλίᾳ αὐτῆς ("the baby leaped in her womb", 1:41, 44). σκιρτάω occurs three times in the NT, all in Luke (1:41, 44; 6:23) `[T]`. Gen 25:22 Swete: ἐσκίρτων δὲ τὰ παιδία ἐν αὐτῇ ("the children leaped within her") — Rebekah's twins, of whom "the older shall serve the younger" `[T]`. *Moderate*: the elder child in Elizabeth's womb honours the younger. Mal 4:2 Swete has σκιρτήσετε ("you will leap") in the verse of the rising sun of righteousness (see pericope 4) — *uncertain*.
- **The ark and the three months.** Elizabeth's πόθεν μοι τοῦτο ἵνα ἔλθῃ ἡ μήτηρ τοῦ κυρίου μου πρὸς ἐμέ; ("how has it happened to me that the mother of my Lord would come to me?", 1:43) stands beside David's Πῶς εἰσελεύσεται πρὸς μὲ ἡ κιβωτὸς Κυρίου; ("how can the ark of the LORD come to me?", 2 Sam 6:9 Swete); the ark stayed in the house of Obed-edom μῆνας τρεῖς ("three months", 2 Sam 6:11), and Mary stays ὡς μῆνας τρεῖς ("about three months", 1:56); David ἀνέστη καὶ ἐπορεύθη ("arose and went", 2 Sam 6:2) into Judah, and Mary Ἀναστᾶσα … ἐπορεύθη ("arising … went", 1:39) εἰς πόλιν Ἰούδα ("to a city of Judah") `[T]` for every verbal datum. Four points of contact, none of them a quotation. *Moderate* — a pattern of the ark's coming to a house in Judah and blessing it; and a pattern claim, not a quotation.

**Tool 11.**

**2 Sam 7:12–16 → 1:32–33** *(high)*. *Source context:* Nathan's oracle to David, after David proposes to build the LORD a house: the LORD will build David a house, raise up his seed, establish the throne of his kingdom for ever; "I will be a father to him, and he shall be a son to me" (7:14). *Book usage:* first use; the Davidic promise returns at 1:69 (the horn in the house of David), 2:4, 11 (David's city), 18:38–39 ("Son of David") and 20:41–44 (David's Lord). *OT-to-OT:* Isa 9:7 Swete takes up the same promise — ἐπὶ τὸν θρόνον Δαυεὶδ … ἀπὸ τοῦ νῦν καὶ εἰς τὸν αἰῶνα ("upon the throne of David … from now and for ever") — and Luke's "no end" stands closer to Isaiah's οὐκ ἔστιν ὅριον ("there is no boundary") than to Samuel. *What it adds:* the Son of the Most High is the son of 2 Sam 7:14; the one conceived by the Spirit is David's promised seed, and his kingdom has no end.

**Gen 18:14 → 1:37** *(high)*. *Source context and book usage:* see pericope 2. Mary is answered with Sarah's promise: οὐκ ἀδυνατήσει παρὰ τοῦ θεοῦ πᾶν ῥῆμα ("nothing will be impossible with God", 1:37) against μὴ ἀδυνατεῖ παρὰ τῷ θεῷ ῥῆμα; ("is anything impossible with God?", Gen 18:14 Swete). *What it adds:* the virgin conception is set in the line of the barren conceptions, and exceeds them.

**1 Sam 1:11; 2:1–10 (Hannah) → 1:46–55** *(high)*. *Source context:* Hannah, barren and provoked, vows her son to the LORD if he will look on τὴν ταπείνωσιν τῆς δούλης σου ("the humiliation of your maidservant", 1:11); her song celebrates the LORD who brings low and raises up, breaks the bow of the mighty, feeds the hungry, and ends — before any king exists — with "he will give strength to his king and exalt the horn of his anointed" (2:10). *Book usage:* Samuel has been in view since 1:15; 2:52 will describe Jesus in Samuel's words (see pericope 6). *OT-to-OT:* the Magnificat weaves Hannah with the Psalms (Ps 111:9 Swete 110:9 ἅγιον … τὸ ὄνομα αὐτοῦ ("holy is his name") at 1:49; Ps 103:17 at 1:50; Ps 89:10 Swete 88:11 διεσκόρπισας … ἐν τῷ βραχίονι ("you scattered … with your arm") at 1:51; Ps 107:9 Swete 106:9 πεινῶσαν ἐνέπλησεν ἀγαθῶν ("he filled the hungry with good things"), near-verbatim, at 1:53), with Isaiah (Isa 41:8–9 Swete ἀντελαβόμην … Ἰσραήλ, παῖς μου ("I took hold of … Israel, my servant") at 1:54) and with Micah (Mic 7:20, ἔλεον τῷ Ἀβραάμ ("mercy to Abraham") at 1:55). Sir 10:14's θρόνους ἀρχόντων καθεῖλεν ὁ κύριος ("the Lord has brought down the thrones of rulers") stands behind 1:52's καθεῖλεν δυνάστας ἀπὸ θρόνων ("he has brought down rulers from their thrones"). Hannah's song already ended on a king; Mary's is sung over the king. *What it adds:* the song of reversal that opened the story of Israel's monarchy is sung again at its fulfilment. The aorists (ἐποίησεν ("he has done"), καθεῖλεν ("he has brought down"), ὕψωσεν ("he has exalted")) announce as done what the book will narrate as it happens. `[T]` for the tenses; `[I]` for the prophetic force, high.

*Internal:* **plants §6:20–26; 14:11; 18:14** — the exaltation of the humble. ὑψόω ("to exalt") occurs at 1:52; 10:15; 14:11; 18:14, and ταπεινόω ("to humble") at 3:5; 14:11; 18:14 — the Magnificat's reversal becomes the refrain "everyone who exalts himself will be humbled" twice (14:11; 18:14), verified by lemma (high). **Plants §11:27–28** — "all generations will call me blessed" (μακαριοῦσίν, 1:48; μακαρίζω occurs twice in the NT, here and Jas 5:11) against the woman's "blessed is the womb that bore you" and Jesus' answer, "blessed rather are those who hear the word of God and keep it" (11:28). The book itself defines Mary's blessedness as hearing and believing (1:45) (moderate–high). **Plants §9:34** — ἐπισκιάζω (above).

**Pitfall.** Two opposite errors. The first isolates Mary as an object of devotion; the second skips her as a Christmas figure. The book does neither: it calls her μακαρία ("blessed") *because she believed* (1:45), and it redefines her blessedness in those terms at 11:28. The corrective: preach Mary as the first believer of the word about Jesus.

---

## 4. Luke 1:57–80 — The God Who Visits ⭐

**Position.** Q1: 1:20 promised Zechariah's silence "until the day these things take place"; 1:13 promised the name. Q2: the birth of John is told here, briefly, so that the father's restored voice can interpret the whole of chs. 1–2 in advance. The Benedictus is the book's first theological summary.

**Structure.** Birth and rejoicing (57–58); the naming and the opened mouth (59–66); the Benedictus (67–79) in two strophes — God's act for Israel (68–75) and the child's role (76–79); the child in the wilderness (80).

**Text-first findings.**

- **The mouth opened in blessing.** ἀνεῴχθη δὲ τὸ στόμα αὐτοῦ … καὶ ἐλάλει εὐλογῶν τὸν θεόν ("his mouth was opened … and he began to speak in praise of God", 1:64) `[T]`. The priest who could not bless the people now blesses God. The people are not blessed; that waits (24:50). `[I]`, moderate–high.
- **A visitation bracket.** The song opens with ἐπεσκέψατο ("he has visited", aorist, 1:68) and closes with ἐπισκέψεται ("will visit", future, 1:78) `[T]`. What God has done and what he will do bracket the song. The verb returns at 7:16, and its noun at 19:44 — four occurrences of the group in Luke, verified.
- **Three salvations and a fourth.** σωτηρία ("salvation") occurs three times in the Benedictus (1:69, 71, 77) and once more in the whole book: σήμερον σωτηρία τῷ οἴκῳ τούτῳ ἐγένετο ("today salvation has come to this house", 19:9), verified by lemma. `[T]` The salvation sung over the Davidic horn arrives at Zacchaeus' table.
- **The oath to Abraham.** ὅρκον ὃν ὤμοσεν πρὸς Ἀβραάμ ("the oath which he swore to Abraham", 1:73) — the oath of Gen 22:16–17, sworn after the Akedah `[T]`.
- **Release of sins.** γνῶσιν σωτηρίας … ἐν ἀφέσει ἁμαρτιῶν αὐτῶν ("knowledge of salvation … by the forgiveness of their sins", 1:77) — the first ἄφεσις ("release, forgiveness") of the book's five `[T]`.
- **A dawn from on high.** ἀνατολὴ ἐξ ὕψους ("the Sunrise from on high", 1:78). ὕψος ("height") occurs twice in Luke — here and at 24:49, δύναμιν ἐξ ὕψους ("power from on high") `[T]`, verified.

**Tool 11.**

**Ps 111:9 (Swete 110:9) → 1:68** *(moderate–high)*. Move 1: λύτρωσιν ἀπέστειλεν τῷ λαῷ αὐτοῦ ("he sent redemption to his people"), in a psalm of the works of the LORD and his covenant remembered. Luke: ἐποίησεν λύτρωσιν τῷ λαῷ αὐτοῦ ("he accomplished redemption for his people"). The same psalm's ἅγιον … τὸ ὄνομα αὐτοῦ ("holy is his name") stood at 1:49; one psalm feeds both songs.

**Ps 132:17 (Swete 131:17) → 1:69** *(moderate)*. Move 1: ἐκεῖ ἐξανατελῶ κέρας τῷ Δαυείδ ("there I will make a horn sprout for David"), in the psalm of the LORD's oath to David and his choice of Zion. Luke's ἤγειρεν κέρας σωτηρίας … ἐν οἴκῳ Δαυίδ ("raised up a horn of salvation … in the house of David"). The psalm's verb ἐξανατελῶ ("I will make sprout") belongs to the same family as the ἀνατολή of 1:78 `[T]`.

**Ps 107:10 (Swete 106:10) with Isa 9:2 → 1:79** *(high)*. *Source context:* Ps 107 is the psalm of the redeemed gathered "from the east and the west, from the north and the sea" (107:2–3), who sat καθημένους ἐν σκότει καὶ σκιᾷ θανάτου ("in darkness and the shadow of death", 107:10) and were brought out. Isa 9:2 (Heb 9:1) is the light on the people who walked in darkness, before the child born and the throne of David (9:6–7). *Book usage:* Ps 107 fed 1:53 (107:9) and returns at 13:29 (107:3); Isa 9 stood behind 1:32–33. *OT-to-OT:* the psalm's darkness is exile, and Isaiah's darkness is the northern tribes under Assyria; both are answered by the LORD's deliverance, and Isaiah's by a Davidic child. *What it adds:* the redeemed of the psalm and the people of Isaiah's darkness are joined in the one "dawn from on high", and the next two uses of these sources — the gathering of 13:29 and the throne of 1:32 — are already folded in.

**Mal 3:1 with Isa 40:3 → 1:76** *(high)*. *Source context:* Malachi's messenger who prepares the way before the LORD's sudden coming to his temple; Isaiah's voice preparing the way of the LORD in the wilderness. *Book usage:* Mal 3:23–24 at 1:17; both texts return at 3:4–6 and 7:27. *OT-to-OT:* Malachi's "prepare the way" (Heb פִּנָּה־דֶרֶךְ) is Isaiah's wording (Isa 40:3, פַּנּוּ דֶּרֶךְ) — Malachi already reads Isaiah `[T]`, verified in the WLC. *What it adds:* John goes ἐνώπιον κυρίου ("before the Lord"); the Lord whose way he prepares is, in Luke's story, Jesus (1:43; 3:4). `[I]`, high.

**ἀνατολή: Jer 23:5; Zech 3:8; 6:12; Mal 3:20 (Swete 4:2) → 1:78** *(moderate)*. Move 1: in Swete ἀνατολή renders צֶמַח ("Branch"), the Davidic shoot (Jer 23:5, ἀναστήσω τῷ Δαυεὶδ ἀνατολὴν δικαίαν ("I will raise up for David a righteous Branch"); Zech 6:12, Ἀνατολὴ ὄνομα αὐτῷ ("his name is Branch")). Mal 4:2 Swete has the verb: ἀνατελεῖ ὑμῖν … ἥλιος δικαιοσύνης ("the sun of righteousness will rise for you"). Luke's phrase joins both senses — the Davidic Branch and the rising light — and "from on high" and "shine upon" (1:79) favour the light. **A Malachi sequence (synthetic, moderate):** 1:17 takes Mal 3:23–24; 1:76 takes Mal 3:1; 1:78 takes Mal 3:20. Luke's first chapter draws on Malachi's last chapter three times. `[T]` for each wording; `[I]` for the sequence.

*Internal:* **plants §19:9** (σωτηρία, above; high). **Plants §7:16; 19:44** (the visitation group; high). **Plants §24:49** (ἐξ ὕψους; moderate–high). **Plants §24:47** — ἄφεσις ἁμαρτιῶν ("forgiveness of sins", 1:77) against the same phrase in the commission (24:47); ἄφεσις occurs at 1:77; 3:3; 4:18 (twice); 24:47 and nowhere else in Luke, verified (high). **Plants §10:1** — ἀνάδειξις ("public appearance", 1:80) is a NT hapax, and its verb ἀναδείκνυμι ("to appoint publicly") occurs twice in the NT: Luke 10:1 (the appointment of the seventy-two) and Acts 1:24 (the choice of Matthias) (uncertain).

**Pitfall.** Preaching the Benedictus as John's song. Nine of its twelve verses concern the Davidic horn and God's oath. John enters at 1:76 as the one who goes before. The corrective: the father's song over his own son is about someone else's son.

---

## 5. Luke 2:1–20 — Today a Saviour

**Position.** Q1: 1:32–33 and 1:69 promised a Davidic king in the house of David. Q2: the birth follows because the promise needs a place — David's city — and Luke moves the family there by an imperial decree. The emperor's order serves the Lord's promise. `[I]`, high.

**Structure.** The decree and the journey (1–5); the birth (6–7); the shepherds and the angel (8–12); the heavenly army's praise (13–14); the shepherds' visit (15–20).

**Text-first findings.**

- **Emperor and people.** δόγμα παρὰ Καίσαρος Αὐγούστου ἀπογράφεσθαι πᾶσαν τὴν οἰκουμένην ("a decree from Caesar Augustus, that a census be taken of all the inhabited earth", 2:1) against χαρὰν μεγάλην ἥτις ἔσται παντὶ τῷ λαῷ ("great joy which will be for all the people", 2:10) `[T]`. Augustus was publicly hailed as σωτήρ ("saviour") and bringer of peace, and his birthday called εὐαγγέλια ("good news") in the Priene inscription `[S]`, well attested. The angel's vocabulary — εὐαγγελίζομαι ("I bring good news"), σωτήρ ("Saviour"), εἰρήνη ("peace") — takes the emperor's words for another king. `[I]`, moderate–high.
- **The sign.** βρέφος ἐσπαργανωμένον καὶ κείμενον ἐν φάτνῃ ("a baby wrapped in cloths and lying in a manger", 2:12). φάτνη ("manger") occurs three times in 2:7–16 and once more in Luke, of the ox led from the φάτνη on the Sabbath (13:15) `[T]`. Isa 1:3 Swete, ὄνος τὴν φάτνην τοῦ κυρίου αὐτοῦ ("the donkey knows its master's manger") — *uncertain*.
- **The κατάλυμα.** οὐκ ἦν αὐτοῖς τόπος ἐν τῷ καταλύματι ("there was no room for them in the κατάλυμα", 2:7). κατάλυμα ("lodging, guest room") occurs twice in Luke — here and at 22:11, where Jesus asks for the κατάλυμα in which to eat the Passover `[T]`, verified.
- **Χριστὸς κύριος ("Christ the Lord", 2:11).** The collocation stands in Swete at Lam 4:20 (χριστὸς Κύριος, where the Hebrew is מְשִׁיחַ יְהוָה ("the LORD's anointed")) and at Pss. Sol. 17:36, of the coming Davidic king `[T]`. Luke's phrase reads "the Messiah who is Lord". `[I]`, moderate. *Triage (category 3):* the Greek coincides with a phrase whose Hebrew meant "the LORD's anointed", and Luke's use stands whatever the Hebrew of Lamentations.
- **Peace on earth.** Δόξα ἐν ὑψίστοις θεῷ καὶ ἐπὶ γῆς εἰρήνη ἐν ἀνθρώποις εὐδοκίας ("glory to God in the highest, and on earth peace among people of [his] good pleasure", 2:14) `[T]`. The Majority text reads εὐδοκία ("goodwill"), which the KJV follows ("good will toward men"); the NASB95 follows the critical text ("among men with whom He is pleased").
- **Mary keeps the words.** ἡ δὲ Μαρία πάντα συνετήρει τὰ ῥήματα ταῦτα συμβάλλουσα ἐν τῇ καρδίᾳ αὐτῆς ("Mary treasured all these things, pondering them in her heart", 2:19). See pericope 6 for the Joseph and Daniel echoes, which bear on 2:51.

**Tool 11.** No formula citation. Bethlehem as David's city (2:4, 11) carries 1 Sam 16–17 — David the shepherd of Bethlehem — and shepherds keeping watch there (2:8) `[I]`, moderate. Luke does not cite Mic 5:2, which Matthew does (Matt 2:6) `[T]` — an absence reported without an argument drawn from it.

*Internal:* **plants §19:38** — the Gloria's δόξα ἐν ὑψίστοις … ἐπὶ γῆς εἰρήνη ("glory in the highest … on earth peace") against the disciples' ἐν οὐρανῷ εἰρήνη καὶ δόξα ἐν ὑψίστοις ("peace in heaven and glory in the highest", 19:38); ἐν ὑψίστοις occurs only at these two places in Luke (high). **Plants §22:11** — κατάλυμα (above; moderate). **Plants §24:52** — χαρὰν μεγάλην ("great joy", 2:10) against μετὰ χαρᾶς μεγάλης ("with great joy", 24:52), the only two places in Luke where χαρά ("joy") stands with μέγας ("great"), verified (moderate–high). **Plants §23:53** — wrapped and laid in a manger, wrapped and laid in a tomb (moderate).

**Difficult verse — 2:2, the census of Quirinius.** *Category:* apologetic. Quirinius' known census of Judaea is dated AD 6, after Herod's death (4 BC) `[S]`. Options: an earlier census or governorship of Quirinius; πρώτη ("first") read as "before" ("before Quirinius was governor"); an error. *Handling:* acknowledge if asked; nothing in the text's theology depends on the resolution.

**Pitfall.** The innkeeper. There is none in the text: κατάλυμα is the room Jesus later asks for to eat the Passover (22:11), and the NASB95's "inn" at 2:7 and "guest room" at 22:11 hide the link. The corrective: no room for him at his birth; a room made ready for his Passover.

---

## 6. Luke 2:21–52 — A Light and a Sword ⭐

**Position.** Q1: 1:32–35 named the child Son of God and Son of David; 2:11 named him Saviour, Christ and Lord. Q2: two temple scenes follow because the Son must be brought to his Father's house — first by his parents under the law, then by his own choice. The infancy section ends in the temple where it began.

**Structure.** Circumcision and naming (21); the presentation under the law (22–24); Simeon and the Nunc Dimittis (25–35); Anna (36–38); return and growth (39–40); the boy in the temple at twelve (41–51); growth (52).

**Text-first findings.**

- **The law fivefold.** νόμος ("law") occurs five times in 2:22–39 — κατὰ τὸν νόμον Μωϋσέως ("according to the law of Moses", 2:22), ἐν νόμῳ κυρίου ("in the law of the Lord", 2:23, 24), τοῦ νόμου ("of the law", 2:27), κατὰ τὸν νόμον κυρίου ("according to the law of the Lord", 2:39) — and then not again until 10:26 `[T]`, verified by lemma. The family's Torah-faithfulness is stressed, not assumed. `[I]`, high.
- **The poor family's offering.** ζεῦγος τρυγόνων ἢ δύο νοσσοὺς περιστερῶν ("a pair of turtledoves or two young pigeons", 2:24): the wording is Lev 5:11 Swete's (ζεῦγος τρυγόνων); the occasion is Lev 12:8's, the offering of a woman who cannot afford a lamb `[T]`.
- **Three waiting Israelites.** Simeon is δίκαιος καὶ εὐλαβής ("righteous and devout"), προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ ("looking for the consolation of Israel", 2:25); Anna speaks πᾶσιν τοῖς προσδεχομένοις λύτρωσιν Ἰερουσαλήμ ("to all those who were looking for the redemption of Jerusalem", 2:38) `[T]`. The Spirit is named three times over Simeon (2:25, 26, 27).
- **Anna of Asher.** Φανουήλ ("Phanuel") and φυλῆς Ἀσήρ ("the tribe of Asher", 2:36) `[T]` — a northern tribe, lost since the Assyrian exile, represented at the redemption of Jerusalem. `[I]`, moderate. The number 84 (2:37) as 7 × 12 — *uncertain*, and not used.
- **The sword.** καὶ σοῦ δὲ αὐτῆς τὴν ψυχὴν διελεύσεται ῥομφαία ("a sword will pierce even your own soul", 2:35). Ezek 14:17 Swete, Ῥομφαία διελθάτω διὰ τῆς γῆς ("let a sword pass through the land"), of judgement on a people `[T]` — *uncertain* as an allusion.
- **The first δεῖ.** οὐκ ᾔδειτε ὅτι ἐν τοῖς τοῦ πατρός μου δεῖ εἶναί με; ("did you not know that I had to be in my Father's house?", 2:49). The first of the book's eighteen δεῖ ("it is necessary"), spoken by Jesus of the Father's house, in answer to Mary's ὁ πατήρ σου κἀγὼ … ἐζητοῦμέν σε ("your father and I … were looking for you", 2:48) `[T]`. The correction of "your father" by "my Father" is the Son's first recorded word.
- **Mary keeps the words — Jacob's and Daniel's phrase.** ἡ μήτηρ αὐτοῦ διετήρει πάντα τὰ ῥήματα ταῦτα ἐν τῇ καρδίᾳ αὐτῆς ("his mother treasured all these things in her heart", 2:51). Gen 37:11 Swete: ὁ δὲ πατὴρ αὐτοῦ διετήρησεν τὸ ῥῆμα ("but his father kept the saying in mind") — Jacob over Joseph's dreams. Dan 7:28 Theodotion: τὸ ῥῆμα ἐν τῇ καρδίᾳ μου διετήρησα ("I kept the matter in my heart") — Daniel after the vision of the Son of Man. `[T]` for both wordings. Mary keeps revelatory words about a son as Jacob did and as Daniel did. *Moderate–high* — the triple of διατηρέω ("to keep"), ῥῆμα ("word") and καρδία ("heart") stands in Dan 7:28 Theodotion and in Luke 2:51 `[T]`.
- **Growing like Samuel.** Ἰησοῦς προέκοπτεν σοφίᾳ καὶ ἡλικίᾳ καὶ χάριτι παρὰ θεῷ καὶ ἀνθρώποις ("Jesus kept increasing in wisdom and stature, and in favour with God and people", 2:52). 1 Sam 2:26 (Hebrew): the boy Samuel הֹלֵךְ וְגָדֵל וָטוֹב גַּם עִם־יְהוָה וְגַם עִם־אֲנָשִׁים ("growing on, and good, both with the LORD and with men"); Prov 3:4 (Hebrew): וּמְצָא־חֵן … בְּעֵינֵי אֱלֹהִים וְאָדָם ("and find favour … in the sight of God and man") `[T]`. Luke's χάρις ("favour") answers חֵן ("favour") in the Hebrew of Proverbs; Swete's Prov 3:4 has no equivalent. *Moderate.*

**Tool 11.**

**Exod 13:2, 12 → 2:23** *(high — formula citation)*. *Source context:* the consecration of the firstborn, commanded on the night of the Passover because the LORD struck Egypt's firstborn and spared Israel's (Exod 13:11–15). *Book usage:* first Exodus citation; Exodus returns at 9:31 (ἔξοδος ("departure")), 11:20 (the finger of God), 20:37 and 22:20. *OT-to-OT:* Num 3:11–13 replaces the firstborn with the Levites. *What it adds:* the Son is presented as the firstborn the LORD claimed on the Passover night; his last meal will be a Passover (22:15).

**Isa 49:6; 42:6; 52:10 → 2:30–32** *(high)*. *Source context:* Isa 49:6 — the Servant, told that restoring Jacob is "too small a thing", is given as φῶς ἐθνῶν ("a light of the nations") "that you should be my salvation to the end of the earth"; Isa 52:10 — the LORD bares his holy arm before πάντων τῶν ἐθνῶν ("all the nations"), and all the ends of the earth see the salvation of our God. *Book usage:* Isaiah's Servant has not yet been cited; this is its first appearance, and the Servant returns at 3:22; 22:37; 23:35. *OT-to-OT:* Isa 49 and 52 are one argument — the Servant's mission and the LORD's arm are the same salvation; Isa 40:5 (3:6) belongs to it. *What it adds:* Simeon holds the salvation (τὸ σωτήριόν σου ("your salvation"), 2:30) that Isaiah said all flesh would see, and names its double reach — "light for revelation to the nations, and the glory of your people Israel" (2:32). The nations are named before Israel, and Israel's glory is the last word. `[T]`

**Isa 8:14–15 → 2:34** *(moderate)*. Move 1: the LORD as a stone of stumbling and a rock of offence for both houses of Israel, "and many will stumble and fall" (8:15). Luke's κεῖται εἰς πτῶσιν καὶ ἀνάστασιν πολλῶν ἐν τῷ Ἰσραήλ ("appointed for the fall and rise of many in Israel") and σημεῖον ἀντιλεγόμενον ("a sign to be opposed"). The stone returns at 20:17–18.

**Isa 40:1 and 52:9 → 2:25, 38** *(moderate; uncertain)*. Move 1: "Comfort, comfort my people" (Swete Παρακαλεῖτε, "comfort") is behind παράκλησις τοῦ Ἰσραήλ ("consolation of Israel"). At Isa 52:9 the Hebrew has גָּאַל יְרוּשָׁלָ‍ִם ("he has redeemed Jerusalem"), matching Anna's λύτρωσις Ἰερουσαλήμ ("redemption of Jerusalem"), where Swete reads ἐρύσατο ("he rescued") `[T]`, verified in the WLC and Swete. *Triage (category 1, translation):* the link is visible in the Hebrew and hidden in Swete.

*Internal:* **plants §24:5–7, 46** — lost, sought, found "after three days" in the Father's house, with the first δεῖ (2:46–49), against "why do you seek the living among the dead? … he must … on the third day rise" (24:5–7). ζητέω ("to seek") stands at 2:48, 49 and 24:5, and δεῖ at 2:49 and 24:7 (moderate–high; an unadvertised echo). **Plants §18:34; 24:45** — οὐ συνῆκαν ("they did not understand", 2:50) against διήνοιξεν αὐτῶν τὸν νοῦν τοῦ συνιέναι ("he opened their minds to understand", 24:45); συνίημι occurs at 2:50; 8:10; 18:34; 24:45 (high). **Plants §24:38** — διαλογισμοί ("thoughts", 2:35) against διαλογισμοί ("doubts", 24:38) (moderate). **Plants §23:50–51** — Simeon δίκαιος … προσδεχόμενος against Joseph of Arimathea δίκαιος … προσεδέχετο (23:50–51) (high). **Answers §1:38** — κατὰ τὸ ῥῆμά σου (above; high).

**Translations.** The NASB95's "My Father's house" (2:49) supplies a noun the Greek leaves open (ἐν τοῖς τοῦ πατρός μου ("in the [things/house] of my Father")); "house" is the likelier sense, and the KJV's "about my Father's business" is the other. **Textual variant, 2:33 and 2:43:** the Majority text has "Joseph and his mother" and "Joseph and his mother" where the SBLGNT has "his father and mother" and "his parents" — a reading that protects the virginal conception verbally; the critical reading leaves that to 1:34–35 and 3:23 ("as was supposed"). *High confidence* that the critical reading is the harder one; the doctrine rests on 1:34–35 either way.

**Pitfall.** Preaching 2:41–52 as adolescent independence, or as a lesson on obedient children from 2:51. The scene's weight falls on the Son's first δεῖ and the correction of "your father" by "my Father". The corrective: the first thing Jesus says in the book is that he must be where his Father is.

---

## 7. Luke 3:1–38 — The Way Prepared; Son of Adam, Son of God

**Position.** Q1: 1:80 left John in the wilderness "until the day of his public appearance to Israel"; 1:17 and 1:76 promised a forerunner. Q2: the second beginning comes here because the infancy has named Jesus and now the forerunner must prepare the way before the Son's public work; and the genealogy stands *after* the baptism, so that the voice's "my Son" is followed at once by the line that ends "son of God".

**Structure.** The dated beginning (1–2); John's preaching, with Isa 40 (3–6); the warning and the three "what shall we do?" questions (7–14); the stronger one (15–17); John removed to prison (18–20); the baptism (21–22); the genealogy (23–38).

**Text-first findings.**

- **The word of God came.** ἐγένετο ῥῆμα θεοῦ ἐπὶ Ἰωάννην ("the word of God came to John", 3:2). Swete's Jeremiah opens ΤΟ ῥῆμα τοῦ θεοῦ ὃ ἐγένετο ἐπὶ Ἰερεμίαν ("the word of God which came to Jeremiah", Jer 1:1) — the only prophetic book in Swete to open with ῥῆμα τοῦ θεοῦ ("the word of God") `[T]`, verified by surface search across Swete. John is introduced as Jeremiah was. *High on the wording; moderate–high on the design.*
- **Seven rulers.** Tiberius, Pontius Pilate, Herod, Philip, Lysanias, Annas, Caiaphas (3:1–2) `[T]` — the powers of empire, client kingdom and temple, set against one prophet in the wilderness.
- **"What shall we do?" three times.** τί ποιήσωμεν; ("what shall we do?") from the crowds (3:10), the tax collectors (3:12) and the soldiers (3:14) `[T]`, verified after the siglum correction. The question returns as the lawyer's and the ruler's τί ποιήσας … κληρονομήσω; ("what shall I do to inherit …?", 10:25; 18:18), and as the Pentecost crowd's τί ποιήσωμεν; (Acts 2:37).
- **The stronger one.** ἔρχεται δὲ ὁ ἰσχυρότερός μου ("one is coming who is mightier than I", 3:16). ἰσχυρότερος ("stronger") returns at 11:22, where the stronger man overcomes the strong man `[T]`. *Internal*, high.
- **John removed before the baptism.** Luke narrates John's imprisonment (3:19–20) before Jesus' baptism (3:21), and names no baptiser `[T]`. The forerunner leaves the stage before the Son enters it.
- **Praying at the hinge.** Ἰησοῦ βαπτισθέντος καὶ προσευχομένου ("when Jesus was baptised and was praying", 3:21) — the first of Luke's prayers at the turning points (5:16; 6:12; 9:18, 28–29; 22:41–44) `[T]`.
- **The genealogy's count.** From Joseph back to Adam the line names 75 ancestors, then θεοῦ ("of God"); with Joseph and Jesus it has 77 human names `[T]`, counted in the SBLGNT. It runs through Nathan, not Solomon (3:31), and includes Καϊνάμ ("Cainan", 3:36), who stands in Swete's Genesis (10:24; 11:12–13) and not in the Hebrew `[T]`, verified in both. *Triage (category 3, the NT's own text):* Luke's genealogy follows the Greek Genesis here, and that is a fact about Luke's Bible whatever the Hebrew. The symbolic reading of 77 (11 × 7) is `[S]`, uncertain, and is not used.

**Tool 11.**

**Isa 40:3–5 → 3:4–6** *(high — formula citation)*. *Source context:* the opening of Isaiah's comfort: "Comfort, comfort my people" (40:1); a voice calls to prepare the LORD's way in the wilderness, every valley filled, every mountain lowered; the glory of the LORD revealed, and all flesh seeing it together; then the word of our God that stands for ever (40:8). *Book usage:* Isa 40:1 lay behind 2:25 (παράκλησις ("consolation")) and Isa 40:3 behind 1:76; the salvation seen stood at 2:30. *OT-to-OT:* Mal 3:1 is already reading Isa 40:3 (pericope 4). *Triage (category 3):* Luke extends Mark's quotation, which stops at 40:3 (Mark 1:3), to 40:5, and ends on καὶ ὄψεται πᾶσα σὰρξ τὸ σωτήριον τοῦ θεοῦ ("and all flesh will see the salvation of God") — the Greek of 40:5, where the Hebrew has וְרָאוּ כָל־בָּשָׂר יַחְדָּו ("and all flesh will see [it] together") `[T]`, verified. *What it adds:* the extension exists to reach σωτήριον and πᾶσα σάρξ ("all flesh"). τὸ σωτήριον τοῦ θεοῦ ("the salvation of God") occurs here and at Acts 28:28 and nowhere else in the NT, verified: the quotation opens the two-volume work's account of salvation for the nations, and Acts closes on it.

**Ps 2:7 with Isa 42:1 and Gen 22:2 → 3:22** *(moderate–high)*. *Source context:* Ps 2 — the nations rage against the LORD and his anointed; the LORD installs his king on Zion, and the king recounts the decree, "You are my Son; today I have begotten you" (2:7). Isa 42:1 — "Behold my servant … my chosen, in whom my soul delights; I have put my Spirit upon him". Gen 22:2 — τὸν υἱόν σου τὸν ἀγαπητόν ("your beloved son"). *Book usage:* Ps 2 is not cited again in Luke (Acts 4:25–26; 13:33); Isa 42:1 returns at 9:35 (critical text) and 23:35 (ὁ ἐκλεκτός ("the chosen one")); ἀγαπητός ("beloved") returns only at 20:13. *OT-to-OT:* the anointed king and the Spirit-bearing servant are already one figure in Isaiah's reading of the Davidic promise (Isa 11:1–2; 42:1; 61:1). *What it adds:* the voice combines the royal decree and the Servant's anointing, and the Spirit descends to fulfil Isa 42:1's "I have put my Spirit upon him" — which the Nazareth sermon will claim at 4:18.

**Jer 1:1 → 3:2** *(high on the wording)*. Move 1 only: Jeremiah the priest's son called as a prophet to the nations; John the priest's son (1:5) called in the wilderness.

*Internal:* **answers §1:17, 76, 80** — the forerunner appears, preparing the way (high). **Plants §11:22** — the stronger one (high). **Plants §12:49–50** — "he will baptise you with the Holy Spirit and fire" (3:16) against Jesus' πῦρ ἦλθον βαλεῖν ἐπὶ τὴν γῆν ("I have come to cast fire upon the earth") and βάπτισμα δὲ ἔχω βαπτισθῆναι ("I have a baptism to undergo", 12:49–50) (moderate). **Plants §4:3, 9** — "son of Adam, son of God" (3:38) is followed immediately by "if you are the Son of God" (4:3) (high). **Plants §23:43** — Ἀδάμ (3:38), once in Luke, against παράδεισος ("paradise", 23:43), once in Luke and Gen 2:8's word (uncertain).

**Copycat.** John's three answers (3:11–14) are *prescriptive* for their hearers in their callings — share, take no more than is due, extort no one — and a *normative pattern* for repentance as fruit. They are not a complete ethic, and the book's own later answers to τί ποιήσω; (10:25–37; 18:18–30) go further.

**Pitfall.** Skipping the genealogy, or harmonising it with Matthew's before reading it. Its place after the voice is the point: the Son of God declared at the Jordan is traced to Adam, "son of God", and the next scene tests him as Adam was tested. The corrective: read 3:38 and 4:3 together.

---

## 8. Luke 4:1–13 — If You Are the Son of God ⭐

**Position.** Q1: 3:22 declared "You are my Son"; 3:38 closed "son of Adam, son of God". Q2: the testing follows at once because the declared Son must be proved where Adam and Israel failed, before he can announce release to others.

**Structure.** The setting — full of the Spirit, led by the Spirit, forty days (1–2); the first test, bread (3–4); the second, the kingdoms (5–8); the third, the temple (9–12); the departure "until an opportune time" (13).

**Text-first findings.**

- **"If you are the Son of God".** Εἰ υἱὸς εἶ τοῦ θεοῦ ("if you are the Son of God", 4:3, 9) takes up the voice of 3:22 and the genealogy's last line (3:38) `[T]`.
- **The Jerusalem order.** Luke's third test is the temple in Jerusalem (4:9) `[T]`; Matthew's third is the mountain (Matt 4:8–10). Luke's order ends where his book ends. `[I]`, high — a synoptic observation, checkable in the corpus.
- **The devil's claim and the Son's.** ὅτι ἐμοὶ παραδέδοται ("because it has been handed over to me", 4:6). At 10:22 Jesus says πάντα μοι παρεδόθη ὑπὸ τοῦ πατρός μου ("all things have been handed over to me by my Father") — the same verb, in the true claim `[T]`. *Moderate–high.*
- **Worship, not fear.** Jesus answers with Deut 6:13 as Κύριον τὸν θεόν σου προσκυνήσεις ("you shall worship the Lord your God", 4:8). Swete's Deuteronomy reads φοβηθήσῃ ("you shall fear"), and the Hebrew תִּירָא ("you shall fear") `[T]`. Luke's verb answers the devil's ἐὰν προσκυνήσῃς ("if you worship", 4:7). *Triage (category 2 or 3):* the reading προσκυνήσεις is attested in some Greek witnesses to Deuteronomy (Alexandrinus) `[S]`; whichever it is, the NT's form stands, and it makes the answer fit the temptation exactly.
- **What the devil leaves out.** Luke's quotation of Ps 91:11 stops at τοῦ διαφυλάξαι σε ("to guard you", 4:10); Swete continues ἐν ταῖς ὁδοῖς σου ("in your ways", Ps 90:11) `[T]`. *Uncertain* whether the omission is meant to be noticed.
- **Until an opportune time.** ἀπέστη ἀπ' αὐτοῦ ἄχρι καιροῦ ("he left him until an opportune time", 4:13) `[T]`. διάβολος ("devil") occurs at 4:2, 3, 6, 13 and 8:12; Σατανᾶς ("Satan") at 10:18; 11:18; 13:16; 22:3, 31 — verified by lemma. The next move is Satan's entry into Judas (22:3).

**Tool 11.**

**Deut 8:3; 6:13; 6:16 → 4:4, 8, 12** *(high — formula citations)*. *Source context:* Deut 6–8 are Moses' sermon on the testing in the wilderness. The LORD led Israel forty years to humble and test them, fed them manna "that he might make you know that man does not live by bread alone" (8:2–3), disciplined them "as a man disciplines his son" (8:5); Israel is to fear and serve the LORD alone (6:13) and not test him as at Massah (6:16). *Book usage:* first Deuteronomy citations; Deuteronomy returns at 9:35 (18:15), 10:27 (6:5), 18:20 (5:16–20), 20:28 (25:5) and 21:22 (32:35). Luke draws on Deuteronomy at the testing, at the Transfiguration, and at the question of eternal life. *OT-to-OT:* Ps 95:8–11 already reads Massah as the paradigm of testing the LORD; the psalm and Deut 6:16 were in conversation before Luke. *What it adds:* the Son answers every test from the chapters about Israel as God's son tested in the wilderness. Where Israel tested God and grumbled for bread, this Son trusts the word, worships the LORD alone, and refuses to test him — forty days for forty years.

**Ps 91:11–12 (Swete 90) → 4:10–11** *(high — quoted by the devil)*. *Source context:* the psalm of the one who dwells in the shelter of the Most High; angels guard him, and he treads on lion and serpent (91:13). *Book usage:* 91:13 returns at 10:19, where the seventy-two are given authority to tread on serpents and scorpions. *OT-to-OT:* none in this passage. *What it adds:* the devil quotes the promise to make it a test; Jesus refuses to use the promise to force the proof. At 10:19 the serpent-treading of the psalm's next verse is given to his disciples — the promise was true, and its time was not the devil's.

*Internal:* **answers §3:22, 38** (high). **Plants §22:3, 31, 53** — ἄχρι καιροῦ (above; high). **Plants §22:28** — πειρασμός ("temptation", 4:13) against "you are those who have stood by me in my πειρασμοῖς ('trials')" (22:28); πειρασμός occurs at 4:13; 8:13; 11:4; 22:28, 40, 46 (moderate). **Plants §23:35–39** — the "if you are" form returns three times at the cross ("if this is the Christ of God … if you are the King of the Jews … are you not the Christ?"), each with σῶσον σεαυτόν ("save yourself") (high). **Plants §10:22** — παραδίδωμι (above; moderate–high).

**Christological reading.** *Contrast and typology:* Adam (3:38) and Israel as son (Deut 8:5) failed their tests; the Son passes his. The Israel-typology passes the category test (sonship), the NT-precedent test (Hos 11:1 at Matt 2:15, the same kind of connection), the escalation test, and the authorial-pattern test (forty; Deuteronomy's own "son"). *High.*

**Pitfall.** "Use Scripture to fight temptation like Jesus." It makes the Son's victory a technique, and it forgets that the devil also quotes Scripture (4:10–11). The corrective: this is the Son of God succeeding where Adam and Israel failed, for them; the disciple's part comes later (11:4; 22:40, 46), and it is prayer.

---

## 9. Luke 4:14–44 — Today, in Your Hearing ⭐

**Position.** Q1: 3:22 anointed the Son with the Spirit, and 4:1–13 proved him. Q2: the Nazareth sermon comes here because the anointed Son must say what the anointing is for before he does it. It is the book's programme, and its rejection is the book's first prophecy of the cross.

**Structure.** The return in the Spirit's power (14–15); the Nazareth synagogue — the reading (16–20), "today" (21), wonder turning to hostility (22–24), Elijah and Elisha (25–27), the attempted killing (28–30); Capernaum — authority in word (31–37), healing at Simon's house (38–41), the other towns (42–44).

**Text-first findings.**

- **Today.** Σήμερον πεπλήρωται ἡ γραφὴ αὕτη ἐν τοῖς ὠσὶν ὑμῶν ("today this Scripture has been fulfilled in your hearing", 4:21). The second σήμερον ("today") of eleven, and the first of Jesus' own `[T]`.
- **Acceptable and not acceptable.** ἐνιαυτὸν κυρίου δεκτόν ("the favourable year of the Lord", 4:19) and οὐδεὶς προφήτης δεκτός ἐστιν ἐν τῇ πατρίδι αὐτοῦ ("no prophet is welcome in his hometown", 4:24). δεκτός ("acceptable, welcome") occurs twice in Luke, here and here `[T]`, verified. The year of the Lord's favour is proclaimed by a prophet his town will not have. The NASB95's "favorable" and "welcome" hide the repetition.
- **Elijah and Elisha go to foreigners.** A widow of Zarephath in Sidon (4:26; 1 Kgs 17:9) and Naaman the Syrian (4:27; 2 Kgs 5:14) `[T]`. The sermon's rage (ἐπλήσθησαν πάντες θυμοῦ ("all were filled with rage"), 4:28) follows these two names, not the Isaiah reading.
- **"Physician, heal yourself".** Ἰατρέ, θεράπευσον σεαυτόν (4:23) `[T]`: the first of the "yourself" taunts. σεαυτοῦ ("yourself") occurs at 4:9, 23; 5:14; 10:27; 23:37, 39, verified; the taunt returns at the cross as σῶσον σεαυτόν ("save yourself", 23:37, 39).
- **Out of the city to be thrown down.** ἐξέβαλον αὐτὸν ἔξω τῆς πόλεως ("they drove him out of the city", 4:29) — and in the vineyard parable the son is ἐκβαλόντες … ἔξω τοῦ ἀμπελῶνος ("thrown out of the vineyard", 20:15) `[T]`. *Moderate.*
- **Sent for this.** ὅτι ἐπὶ τοῦτο ἀπεστάλην ("for I was sent for this purpose", 4:43) answers ἀπέσταλκέν με ("he has sent me", 4:18), and δεῖ εὐαγγελίσασθαι ("I must preach the good news", 4:43) is the second δεῖ `[T]`.

**Tool 11.**

**Isa 61:1–2 with Isa 58:6 → 4:18–19** *(high — the scroll read)*. *Source context:* Isa 61 is spoken by an anointed figure — the Servant's vocation now in the first person — sent with good news to the poor, liberty to the captives, the year of the LORD's favour and the day of vengeance, to comfort all who mourn in Zion and rebuild the ancient ruins; Isa 58:6 is the fast the LORD chooses: to loose the bonds of wickedness and ἀπόστελλε τεθραυσμένους ἐν ἀφέσει ("send away the oppressed in release"). *Book usage:* Isaiah has already been cited at 3:4–6 (Isa 40) and echoed at 2:30–32 (Isa 49; 52). Isa 61 returns at 7:22, where Jesus answers John in its words. *OT-to-OT:* Isa 61 speaks the jubilee of Lev 25 — ἄφεσις ("release") is Swete's jubilee word (Lev 25:10, ἐνιαυτὸς ἀφέσεως ("a year of release")) `[T]` — and Isa 58 condemns a fast that ignores the oppressed. Luke's insertion of 58:6 makes ἄφεσις sound twice, so the reading proclaims the jubilee twice over. *Triage:* (category 3) τυφλοῖς ἀνάβλεψιν ("recovery of sight to the blind") is the Greek of Isa 61:1, where the Hebrew has פְּקַח־קוֹחַ ("opening [of the prison]") — and Luke's Jesus will give sight to the blind (7:21–22; 18:35–43); (category 2, within the NT) the critical text lacks "to heal the broken-hearted", which the Majority text has with Isa 61:1. *What it adds:* the reading stops at 61:2a, before "and the day of vengeance" (Hebrew וְיוֹם נָקָם; Swete ἀνταποδόσεως ("recompense")). The day withheld here surfaces at 21:22, ἡμέραι ἐκδικήσεως ("days of vengeance"), for the city that refused the year of favour — see the Cross-Passage Findings.

**1 Kgs 17 and 2 Kgs 5 → 4:25–27** *(high — named)*. *Source context:* Elijah, fed by ravens and then by a widow of Sidon in the famine, raises her son (1 Kgs 17); Elisha cleanses Naaman, commander of Israel's enemy, who returns to confess the God of Israel (2 Kgs 5). *Book usage:* first use of the Elijah–Elisha cycle, which the book then *enacts without citation*: the widow's son at Nain (7:11–17), fire from heaven (9:54), the plough (9:61–62), the foreign leper who returns (17:11–19), the taking up (9:51; 24:51). *OT-to-OT:* both stories stand in Kings as God's word going outside Israel in the days of Israel's apostasy under Ahab. *What it adds:* Nazareth is told that the prophets of Israel's worst days were sent beyond Israel; the town's response confirms that it is in such days.

*Internal:* **answers §3:22** — "the Spirit of the Lord is upon me" names the descent at the Jordan (high). **Plants §7:22** — Isa 61 in Jesus' answer to John (high). **Plants §7:11–17; 17:11–19** — Elijah and Elisha enacted (high; moderate). **Plants §21:22** — the day of vengeance (moderate). **Plants §23:35–39** — the "yourself" taunt (high). **Plants §24:47** — ἄφεσις (high).

**Historical background.** A synagogue service with a reading from the Prophets and a seated teacher `[S]`, well attested for the first century. The attempted execution by throwing from a height resembles a stoning `[S]`.

**Pitfall.** Book-level trap 1 bites here first. The Nazareth manifesto is preached either as a social programme alone or as spiritual release alone. The reading itself joins the two: good news to the poor, sight to the blind, and ἄφεσις ("release") twice — a word that in the rest of the book means the forgiveness of sins (1:77; 3:3; 24:47). The corrective: preach the release as Luke does — material and spiritual at once, and the same word throughout.

---

## 10. Luke 5:1–6:11 — Who Can Forgive Sins?

**Position.** Q1: 4:18–19 proclaimed release, and 4:43 said "I must preach the good news of the kingdom". Q2: this block follows because the programme now meets people — a fisherman who knows he is a sinner, a leper, a paralysed man, a tax collector — and meets opposition. It is the first controversy cycle, and it ends with the opponents discussing "what they might do to Jesus" (6:11).

**Structure.** Five scenes, then five disputes that rise in sharpness `[T]`:

| Verses | Scene | The objection |
|---|---|---|
| 5:1–11 | The catch and the call of Simon | — |
| 5:12–16 | A leper cleansed | — |
| 5:17–26 | A paralysed man forgiven and healed | "Who can forgive sins but God alone?" (5:21) |
| 5:27–32 | Levi's feast | "Why do you eat with tax collectors and sinners?" (5:30) |
| 5:33–39 | Fasting; new wine | "Yours eat and drink" (5:33) |
| 6:1–5 | Grain on the Sabbath | "Why do you do what is not lawful?" (6:2) |
| 6:6–11 | The withered hand | They watch "to find a reason to accuse him" (6:7); they are "filled with rage" (6:11) |

**Text-first findings.**

- **"Depart from me, for I am a sinful man."** ἀνὴρ ἁμαρτωλός εἰμι, κύριε (5:8) — the first ἁμαρτωλός ("sinner") of seventeen verses in Luke, and it is a disciple's self-description `[T]`, verified. The last is "delivered into the hands of sinful men" (24:7).
- **Catching people alive.** ἀπὸ τοῦ νῦν ἀνθρώπους ἔσῃ ζωγρῶν ("from now on you will be catching men", 5:10). ζωγρέω stands twice in the NT (here; 2 Tim 2:26) `[T]`. In Swete it means to take alive — to spare in war — as Rahab and her father's house were spared (Josh 2:13; 6:25, ἐζώγρησεν) `[T]`, verified. Simon's new work is to take people alive. `[I]`, moderate.
- **The first Son of Man.** ὁ υἱὸς τοῦ ἀνθρώπου ἐξουσίαν ἔχει ἐπὶ τῆς γῆς ἀφιέναι ἁμαρτίας ("the Son of Man has authority on earth to forgive sins", 5:24) — the first of the title's twenty-four occurrences in Luke, and it is about forgiveness `[T]`, verified by lemma sequence.
- **"Today" again.** Εἴδομεν παράδοξα σήμερον ("we have seen remarkable things today", 5:26) `[T]`.
- **Called to repentance.** οὐκ ἐλήλυθα καλέσαι δικαίους ἀλλὰ ἁμαρτωλοὺς εἰς μετάνοιαν ("I have not come to call the righteous but sinners to repentance", 5:32). Mark 2:17 and Matt 9:13 lack εἰς μετάνοιαν ("to repentance") `[T]`, checked in the SBLGNT. Luke's version names the purpose of the call.
- **Old wine.** καὶ οὐδεὶς πιὼν παλαιὸν θέλει νέον ("no one, after drinking old wine, wishes for new", 5:39) — found only in Luke `[T]`. It explains the resistance just narrated: people prefer what they know. `[I]`, moderate.
- **Save or destroy.** ψυχὴν σῶσαι ἢ ἀπολέσαι; ("to save a life or to destroy it?", 6:9) — the first σῴζω ("to save") of the book's seventeen, and set against ἀπόλλυμι ("to destroy, lose"), the verb of the lost in ch. 15 and 19:10 `[T]`.

**Tool 11.**

**1 Sam 21:1–6 → 6:3–4** *(high — named)*. *Source context:* David, fleeing Saul, asks Ahimelech the priest at Nob for bread and receives the bread of the Presence, holy bread, because nothing else is there; Doeg the Edomite is watching (21:7), and the priests of Nob will die for it (22:18). *Book usage:* first use of David's story after the Davidic promises of chs. 1–2. *OT-to-OT:* none in this passage. *What it adds:* the anointed but not-yet-reigning David, hunted by the king, eats holy bread with his companions. The Son of David, whose kingship is contested, claims to be κύριος … τοῦ σαββάτου ("Lord of the Sabbath", 6:5).

**Lev 14 → 5:14** *(high — "as Moses commanded")*. Move 1 only: the priestly inspection and offering for a cleansed leper. Jesus sends the man to the priest, εἰς μαρτύριον αὐτοῖς ("as a testimony to them") — the healer keeps the law.

*Internal:* **plants §22:31–34, 54–62; 24:34** — Simon, who confesses himself a sinner at his call (5:8), will deny Jesus three times, be prayed for, turn, and be the first named witness of the resurrection ("the Lord has really risen and has appeared to Simon", 24:34) (high). **Plants §7:36–50** — "who can forgive sins but God alone?" (5:21) is asked again at the woman's forgiveness: "who is this who even forgives sins?" (7:49) (high). **Plants §15:1–2; 19:7** — the grumbling at table-fellowship with sinners (ἐγόγγυζον ("they were grumbling"), 5:30; διεγόγγυζον, 15:2; 19:7) (high). **Plants §6:11 → 22:2** — "what they might do to Jesus" becomes "how they might put him to death" (22:2) (moderate).

**Pitfall.** "Fishers of men" as an evangelism technique. The call is the fruit of a confession of sin (5:8), and its verb means to spare alive. The corrective: preach the call as grace to a sinner before it is a commission.

---

## 11. Luke 6:12–49 — Blessings and Woes

**Position.** Q1: 5:1–6:11 gathered followers and hardened opponents. Q2: the Twelve are chosen, and the sermon is given to disciples, here because the growing community needs its foundation words before the next phase — and because the reversal Mary sang (1:51–53) must be spoken by her son as his own teaching.

**Structure.** A night of prayer and the choosing of the Twelve (12–16); the descent to a level place and the crowds (17–19); four blessings and four woes (20–26); love of enemies (27–36); judging and giving (37–38); the blind guide, the log, the fruit (39–45); hearing and doing — the two builders (46–49).

**Text-first findings.**

- **Prayer before the choice.** ἦν διανυκτερεύων ἐν τῇ προσευχῇ τοῦ θεοῦ ("he spent the whole night in prayer to God", 6:12) `[T]`.
- **Twelve apostles.** ἐκλεξάμενος … δώδεκα, οὓς καὶ ἀποστόλους ὠνόμασεν ("he chose twelve, whom he also named apostles", 6:13). ἀπόστολος ("apostle") occurs six times in Luke (6:13; 9:10; 11:49; 17:5; 22:14; 24:10) `[T]`, verified. The Twelve will sit on thrones "judging the twelve tribes of Israel" (22:30).
- **Four and four, and "now" four times.** μακάριοι … οὐαί ("blessed … woe"), each set of four in mirror order — poor/rich, hungry now/full now, weeping now/laughing now, hated/well spoken of `[T]`. νῦν ("now") stands four times (6:21 twice; 6:25 twice) `[T]`. The blessings are addressed to disciples in the second person (6:20, ἐπάρας τοὺς ὀφθαλμοὺς αὐτοῦ εἰς τοὺς μαθητὰς αὐτοῦ ("turning his gaze toward his disciples")) `[T]`.
- **The Magnificat as teaching.** πεινῶντες … χορτασθήσεσθε ("you who hunger … you will be satisfied", 6:21) and οὐαὶ ὑμῖν τοῖς πλουσίοις ("woe to you who are rich", 6:24) take up πεινῶντας ἐνέπλησεν ἀγαθῶν καὶ πλουτοῦντας ἐξαπέστειλεν κενούς ("he filled the hungry with good things and sent the rich away empty", 1:53) `[T]`.
- **"You have your consolation."** ἀπέχετε τὴν παράκλησιν ὑμῶν ("you are receiving your comfort in full", 6:24). παράκλησις ("consolation") occurs twice in Luke — Simeon's παράκλησις τοῦ Ἰσραήλ ("consolation of Israel", 2:25) and here `[T]`, verified. The rich already have the consolation Simeon waited for. At 16:25 Lazarus νῦν … ὧδε παρακαλεῖται ("now … is being comforted here") and the rich man is in agony `[T]`.
- **Leap.** σκιρτήσατε ("leap for joy", 6:23) — the third and last σκιρτάω in the NT, after John in the womb (1:41, 44) `[T]`.
- **Sons of the Most High.** ἔσεσθε υἱοὶ Ὑψίστου ("you will be sons of the Most High", 6:35) — the title given to Jesus at 1:32 (υἱὸς Ὑψίστου) extended to those who love their enemies `[T]`.
- **Merciful as the Father.** γίνεσθε οἰκτίρμονες καθὼς ὁ πατὴρ ὑμῶν οἰκτίρμων ἐστίν ("be merciful, just as your Father is merciful", 6:36). Exod 34:6 Swete names the LORD οἰκτείρμων καὶ ἐλεήμων ("compassionate and merciful") `[T]`. *Moderate* — the formula of the divine name made the pattern of the disciple. Lev 19:2's "be holy, for I am holy" is the shape; mercy replaces holiness as the Father's imitable attribute. `[I]`, moderate.
- **Hearing and doing.** ὁ … ἀκούων μου τῶν λόγων καὶ ποιῶν αὐτούς ("everyone who hears my words and acts on them", 6:47; the reverse at 6:49) `[T]`. The pair returns in 8:21, "my mother and my brothers are these who hear the word of God and do it", and in 11:28, "blessed are those who hear the word of God and observe it" `[T]`.

**Tool 11.** No formula citation. The level place (τόπου πεδινοῦ, 6:17) after the mountain of prayer (6:12) is set against Matthew's mountain `[T]` — no Sinai pattern is claimed. Exod 34:6 at 6:36 (above) receives Move 1 only: in its source the name is proclaimed to Moses after the golden calf, the mercy of the God who forgives a sinning people.

*Internal:* **answers §1:51–53** (high). **Answers §2:25** — παράκλησις (above; high). **Plants §16:19–31** — the rich who have their consolation and the poor man comforted (moderate–high). **Plants §23:34** — "love your enemies … pray for those who mistreat you" (6:27–28) is enacted at the cross, "Father, forgive them" (23:34a) (high, and critical-text-dependent only in that NA28 double-brackets 23:34a; SBLGNT and the Majority text both print it). **Plants §8:21; 11:28** — hearing and doing (high). **Plants §22:30** — the Twelve and the tribes (high).

**Copycat.** The commands of 6:27–38 are *direct commands* to disciples, grounded in the Father's character (6:35–36) and the promised reward (6:23, 35). The blessings are *declarations*, not conditions.

**Pitfall.** Book-level trap 1 again. Two readings flatten the blessings: "the poor in spirit" imported from Matthew to spiritualise them, or an economic programme that forgets they are addressed to disciples who have left everything (5:11, 28). The corrective: they are real poverty, real hunger, and real weeping, suffered by followers of the Son of Man (6:22), and the kingdom is theirs.

---

## 12. Luke 7:1–35 — Are You the One Who Is to Come? ⭐

**Position.** Q1: 4:18–19 read Isa 61, and 4:25–27 named Elijah's widow and Elisha's foreigner. Q2: this block exists here to *enact* both: a Gentile's faith (7:1–10), a widow's son raised as Elijah raised one (7:11–17), and then John's question answered in the words of Isa 61 (7:18–23). The book's own programme is fulfilled in front of the reader before the question is asked.

**Structure.** The centurion's servant (1–10); the widow's son at Nain (11–17); John's question and Jesus' answer (18–23); Jesus on John (24–30); this generation (31–35).

**Text-first findings.**

- **Not worthy.** The elders say the centurion is ἄξιος ("worthy", 7:4); he says οὐ γὰρ ἱκανός εἰμι ("I am not fit", 7:6) — John's word of himself before the stronger one (οὐκ εἰμὶ ἱκανός, 3:16) `[T]`. "Not even in Israel have I found such faith" (7:9).
- **Only sons and daughters.** μονογενής ("only") occurs three times in Luke, each of a child restored — the widow's son (7:12), Jairus' daughter (8:42), the boy with the spirit (9:38) `[T]`, verified.
- **The Lord's compassion.** ἰδὼν αὐτὴν ὁ κύριος ἐσπλαγχνίσθη ἐπ' αὐτῇ ("when the Lord saw her, he felt compassion for her", 7:13) — the narrator's first ὁ κύριος ("the Lord") for Jesus, and the first of three σπλαγχνίζομαι ("to be moved with compassion") in Luke (7:13; 10:33; 15:20) `[T]`, verified.
- **"He gave him to his mother."** ἔδωκεν αὐτὸν τῇ μητρὶ αὐτοῦ (7:15) is **verbatim** from 3 Kgdms 17:23 Swete, where Elijah gives the widow of Zarephath's son back to her `[T]`, verified. The scene at the city gate (πύλῃ τῆς πόλεως, 7:12) with a widow repeats 3 Kgdms 17:10, where Elijah meets the widow εἰς τὸν πυλῶνα τῆς πόλεως ("at the gate of the city") `[T]`.
- **"God has visited his people."** Προφήτης μέγας ἠγέρθη ἐν ἡμῖν … Ἐπεσκέψατο ὁ θεὸς τὸν λαὸν αὐτοῦ ("a great prophet has arisen among us … God has visited his people", 7:16) — the crowd voices the Benedictus' ἐπεσκέψατο (1:68) `[T]`. The third of the visitation group's four occurrences.
- **The demonstration before the answer.** ἐν ἐκείνῃ τῇ ὥρᾳ ἐθεράπευσεν πολλούς … καὶ τυφλοῖς πολλοῖς ἐχαρίσατο βλέπειν ("at that very time he cured many … and he gave sight to many who were blind", 7:21) — a narrator's comment that makes the messengers eyewitnesses before Jesus answers `[T]`.
- **The people and the Pharisees.** πᾶς ὁ λαὸς … καὶ οἱ τελῶναι ἐδικαίωσαν τὸν θεόν ("all the people and the tax collectors acknowledged God's justice", 7:29); the Pharisees and lawyers τὴν βουλὴν τοῦ θεοῦ ἠθέτησαν εἰς ἑαυτούς ("rejected God's purpose for themselves", 7:30) — a parenthetical narrator's comment `[T]`. βουλή ("purpose, counsel") occurs twice in Luke, here and at 23:51, where Joseph of Arimathea οὐκ ἦν συγκατατεθειμένος τῇ βουλῇ ("had not consented to their plan") `[T]`, verified. God's counsel refused at 7:30; the council's counsel refused by one righteous member at 23:51.
- **Justified.** δικαιόω ("to justify") stands at 7:29, 35; 10:29; 16:15; 18:14 `[T]`, verified: the people justify God, wisdom is justified by her children, the lawyer and the Pharisees justify themselves, and the tax collector goes home justified.

**Tool 11.**

**Isa 61:1 with Isa 35:5–6; 26:19; 29:18 → 7:22** *(high)*. *Source context:* Isa 35 — the desert blooms, the ransomed return to Zion, the blind see, the deaf hear, the lame leap; Isa 26:19 — "your dead will live"; Isa 29:18 — the deaf hear the words of a book; Isa 61:1 — good news to the poor. *Book usage:* Isa 61 was read at 4:18; this is its second use, and it answers the question "are you the one?" in the programme's own words. *OT-to-OT:* Isaiah's signs of the age to come were already one cluster in Isaiah, and 4Q521 joins the raising of the dead to good news for the poor `[S]`, moderate. *What it adds:* two of the six signs are not in Isaiah's lists — λεπροὶ καθαρίζονται ("lepers are cleansed") and νεκροὶ ἐγείρονται ("the dead are raised") as an act of the anointed — and both are the Elijah–Elisha signs Luke has just narrated (the leper, 5:12–16; the widow's son, 7:11–17; cf. Naaman, 4:27). The answer to John joins Isaiah's programme to the Elijah–Elisha deeds. `[I]`, moderate–high.

**Mal 3:1 with Exod 23:20 → 7:27** *(high — formula citation)*. *Source context:* Exod 23:20 — "Behold, I send an angel before you to guard you on the way and bring you to the place I have prepared", the exodus angel who leads Israel to the land; Mal 3:1 — "Behold, I send my messenger, and he will prepare the way before me; and the Lord whom you seek will suddenly come to his temple". *Book usage:* Malachi at 1:17, 1:76, 1:78; this is the explicit citation that those allusions anticipated — κατασκευάσει ("he will prepare") answers 1:17's κατεσκευασμένον ("prepared") `[T]`. *OT-to-OT:* Malachi's wording is already built from Exod 23:20 (הִנֵּה אָנֹכִי שֹׁלֵחַ מַלְאָךְ ("behold, I am sending an angel") in Exodus; הִנְנִי שֹׁלֵחַ מַלְאָכִי ("behold, I am sending my messenger") in Malachi) `[T]`, verified in the WLC. *Triage:* the Hebrew of Mal 3:1 has לְפָנָי ("before *me*") — the LORD speaks of his own coming; Luke has πρὸ προσώπου σου … ἔμπροσθέν σου ("before *your* face … before *you*"), from Exodus. Swete's Malachi has ἐπιβλέψεται ("he will survey"), not κατασκευάσει; the NT's κατασκευάζω renders the Hebrew פִּנָּה ("clear, prepare") better than Swete does (category 3). *What it adds:* the forerunner of the LORD's coming to his temple goes before Jesus. The quotation places Jesus where Malachi placed the LORD `[I]`, high — and the book will end with Jesus in the temple (19:45–21:38).

**1 Kgs 17:10, 23 → 7:11–17** *(high)*. *Source context and book usage:* see pericope 9 (4:25–26). *What it adds:* the crowd calls him a "great prophet" (7:16), which is true and not enough; the narrator has already called him ὁ κύριος ("the Lord", 7:13). Luke lets the crowd see Elijah and lets the reader see more.

*Internal:* **answers §4:18–27** (high). **Answers §1:17, 76** — κατασκευάζω (high). **Answers §1:68; plants §19:44** — the visitation (high). **Answers §3:16; plants §13:35; 19:38** — ὁ ἐρχόμενος ("the one who is coming", 7:19, 20) takes up John's ἔρχεται ("one is coming", 3:16), and the phrase returns in the psalm Jesus quotes at 13:35 and the crowd sings at 19:38: εὐλογημένος ὁ ἐρχόμενος ("blessed is the one who comes") (high). **Plants §23:51** — βουλή (above; moderate–high).

**Pitfall.** Reading John's question as a lapse of faith to be pitied or rebuked. Jesus praises him at once (7:24–28). The corrective: the question is the book's own — who is this? — and the answer is given in deeds and Scripture together.

---

## 13. Luke 7:36–8:21 — Forgiven Much; How You Hear

**Position.** Q1: 7:34 quoted the charge, "a friend of tax collectors and sinners". Q2: the next scene shows what the friendship is: a sinful woman at a Pharisee's table. The block then turns to the word — its sowing, its hearers, and the family it makes — because the question 7:49 asks ("who is this?") is answered only by those who hear.

**Structure.** The woman and Simon the Pharisee (7:36–50); the women who follow (8:1–3); the sower (8:4–8); the reason for parables (8:9–10); the sower explained (8:11–15); the lamp (8:16–18); the true family (8:19–21).

**Text-first findings.**

- **"If this man were a prophet."** Οὗτος εἰ ἦν προφήτης, ἐγίνωσκεν ἂν τίς καὶ ποταπὴ ἡ γυνή ("if this man were a prophet he would know who and what sort of person this woman is", 7:39). Jesus answers the thought he was not told (7:40) `[T]` — the narrator lets the reader see that he is.
- **The crux of 7:47.** οὗ χάριν … ἀφέωνται αἱ ἁμαρτίαι αὐτῆς αἱ πολλαί, ὅτι ἠγάπησεν πολύ ("for this reason … her sins, which are many, have been forgiven, for she loved much", 7:47). The parable just told (7:41–43) makes love the *result* of forgiveness: the one forgiven more loves more. So ὅτι here gives the evidence, not the ground — "her sins are forgiven, *as* her great love shows". `[T]` for the parable's logic; `[I]` for the reading of ὅτι, high.
- **"Your faith has saved you; go in peace."** ἡ πίστις σου σέσωκέν σε· πορεύου εἰς εἰρήνην (7:50) `[T]`. ἡ πίστις σου σέσωκέν σε occurs four times in Luke — the woman (7:50), the bleeding woman (8:48), the Samaritan leper (17:19), the blind man at Jericho (18:42) `[T]`, verified.
- **The women.** Mary Magdalene, Joanna, Susanna "and many others" διηκόνουν αὐτοῖς ἐκ τῶν ὑπαρχόντων αὐταῖς ("were contributing to their support out of their private means", 8:3) `[T]`. Mary Magdalene and Joanna return at the tomb (24:10). *Internal.*
- **The seed is the word of God.** Ὁ σπόρος ἐστὶν ὁ λόγος τοῦ θεοῦ ("the seed is the word of God", 8:11). ὁ λόγος τοῦ θεοῦ ("the word of God") stands four times in Luke — the crowd pressing to hear it (5:1), the seed (8:11), the true family who hear and do it (8:21), and the blessed who hear and keep it (11:28) `[T]`, verified.
- **Endurance.** καρποφοροῦσιν ἐν ὑπομονῇ ("bear fruit with perseverance", 8:15). ὑπομονή ("perseverance") occurs twice in Luke, here and at 21:19, ἐν τῇ ὑπομονῇ ὑμῶν κτήσασθε τὰς ψυχὰς ὑμῶν ("by your endurance you will gain your lives") `[T]`, verified.
- **The devil and the "time of testing".** The devil takes the word ἵνα μὴ πιστεύσαντες σωθῶσιν ("so that they will not believe and be saved", 8:12); the rocky ground believes πρὸς καιρόν ("for a while") and falls away ἐν καιρῷ πειρασμοῦ ("in time of temptation", 8:13) `[T]` — the vocabulary of 4:13 (πειρασμός, καιρός).

**Tool 11.**

**Isa 6:9 → 8:10** *(high)*. *Source context:* Isaiah's commission, after the vision of the LORD enthroned: go and tell this people, "keep on listening but do not perceive; keep on looking but do not understand" — a hardening that lasts "until cities are devastated" and a stump remains, "the holy seed" (6:13). *Book usage:* first use in Luke; Isaiah is the book's chief live source. Luke quotes only part of it here, and Acts quotes it in full at the end of the two volumes (Acts 28:26–27), with συνῆτε ("understand") and συνῶσιν ("they understand") `[T]`. *OT-to-OT:* Isa 6:13's "holy seed" and the parable's σπόρος ("seed") — *uncertain*. *What it adds:* the parable of the word's sowing is framed by the prophecy of its rejection; the same Isaiah text closes Acts. συνίημι ("to understand") runs through Luke at 2:50; 8:10; 18:34; 24:45 — and the understanding that fails here is opened by the risen Christ (24:45). *Synthetic — the chain is verified by lemma; the design is moderate.*

*Internal:* **answers §5:21** — "who is this who even forgives sins?" (7:49) (high). **Plants §8:48; 17:19; 18:42** — "your faith has saved you" (high). **Plants §23:49, 55; 24:10** — the women from Galilee (high). **Plants §21:19** — ὑπομονή (moderate). **Plants §11:28** — hearing the word (high). **Answers §1:38, 45** — Mary believed the word; at 8:21 the family is defined by hearing and doing it (moderate–high).

**Difficult verse — 7:47.** *Category:* doctrinal. *Common misreading:* love earns forgiveness. *Rhetorical function:* 7:47 applies the parable (7:41–43), whose logic is forgiveness → love. *Options:* evidential ὅτι ("as is shown by her love") or causal. *Honest exegesis:* the parable decides for the evidential reading, and 7:48, 50 ground her salvation in forgiveness and faith. *High.* *Handling:* address briefly; it is the hinge of the scene.

**Pitfall.** Identifying the woman of 7:36–50 with Mary Magdalene. Mary is introduced afresh at 8:2, as the one from whom seven demons had gone out, and the text never joins them. The corrective: leave the woman unnamed, as Luke does; her anonymity makes her every forgiven sinner.

---

## 14. Luke 8:22–9:17 — Who Then Is This?

**Position.** Q1: 7:49 and 8:10 raised the question of who Jesus is and who understands. Q2: four acts of power follow — over sea, demons, disease and death — and then the Twelve are sent and the crowd fed, because the question must be asked by everyone (the disciples, 8:25; Herod, 9:9) before Peter answers it (9:20).

**Structure.** The storm (8:22–25); Legion (8:26–39); Jairus' daughter and the bleeding woman, interleaved (8:40–56); the Twelve sent (9:1–6); Herod's question (9:7–9); the feeding of the five thousand (9:10–17).

**Text-first findings.**

- **Four domains.** Wind and water (8:24–25), a legion of demons (8:30), twelve years of bleeding (8:43), and death (8:53) `[T]` — the four spheres the Son commands, in rising order. `[I]`, high.
- **The question asked three times.** Τίς ἄρα οὗτός ἐστιν ("who then is this?", 8:25); τίς δέ ἐστιν οὗτος ("who is this?", Herod, 9:9); and the question Jesus puts, "who do you say that I am?" (9:20) `[T]`.
- **"Master, we are perishing!"** Ἐπιστάτα ἐπιστάτα, ἀπολλύμεθα (8:24). ἐπιστάτης ("Master") occurs seven times in Luke, only on the lips of disciples (5:5; 8:24 twice, 45; 9:33, 49) and of the ten lepers (17:13) `[T]`, verified.
- **Sitting at his feet.** The healed man sits ἱματισμένον καὶ σωφρονοῦντα παρὰ τοὺς πόδας τοῦ Ἰησοῦ ("clothed and in his right mind, sitting at the feet of Jesus", 8:35). The phrase "at his feet" stands five times in Luke — the woman (7:38), the healed man (8:35), Jairus (8:41), Mary (10:39) and the Samaritan leper (17:16) `[T]`, verified.
- **God and Jesus.** "Return to your house and describe what great things God has done for you" — and he went through the city proclaiming "what great things Jesus had done for him" (8:39) `[T]`. The sentence puts ὁ θεός ("God") and ὁ Ἰησοῦς ("Jesus") in the same slot. `[I]`, moderate–high.
- **Twelve and twelve.** A daughter θυγάτηρ μονογενής … ὡς ἐτῶν δώδεκα ("an only daughter, about twelve years old", 8:42) and a woman bleeding ἀπὸ ἐτῶν δώδεκα ("for twelve years", 8:43); Jesus calls the woman Θυγάτηρ ("Daughter", 8:48) `[T]`.
- **The spirit returned.** ἐπέστρεψεν τὸ πνεῦμα αὐτῆς ("her spirit returned", 8:55); Elijah prayed ἐπιστραφήτω δὴ ἡ ψυχὴ τοῦ παιδαρίου τούτου ("let the soul of this child return", 3 Kgdms 17:21 Swete) `[T]`. *Moderate* — the Elijah cycle again.
- **Herod wants to see him.** ἐζήτει ἰδεῖν αὐτόν ("he kept trying to see him", 9:9) — and at the trial ἦν … θέλων ἰδεῖν αὐτόν ("he had wanted to see him for a long time", 23:8) `[T]`.
- **The feeding's evening and actions.** Ἡ δὲ ἡμέρα ἤρξατο κλίνειν ("the day was ending", 9:12); λαβὼν … ἀναβλέψας εἰς τὸν οὐρανὸν εὐλόγησεν αὐτοὺς καὶ κατέκλασεν καὶ ἐδίδου ("he took … looking up to heaven, he blessed them, and broke them, and kept giving", 9:16) `[T]`. See *Internal*.

**Tool 11.**

**Ps 107:23–30 (Swete 106) and Jonah 1 → 8:22–25** *(moderate)*. Move 1 only: the psalm's sailors cry to the LORD and he stills the storm (ἔστησεν καταιγίδα αὐτῆς ("he stilled its storm"), 106:29 Swete); Jonah sleeps in the ship while the captain begs him to call on God "so that we may not perish" (μὴ ἀπολώμεθα, Jonah 1:6 Swete) `[T]`. Ps 107 has already fed 1:53 and 1:79 and will feed 13:29 — a live source. Here Jesus does what the psalm says the LORD does.

**Isa 65:4 → 8:27, 32** *(moderate)*. Move 1 only: a rebellious people ἐν τοῖς μνήμασιν … κοιμῶνται ("sleep in the tombs") and eat κρέας ὕειον ("swine's flesh", Swete) `[T]`. Tombs and pigs together; the demoniac lives ἐν τοῖς μνήμασιν ("in the tombs", 8:27) beside a herd of swine.

**2 Kgs 4:42–44 → 9:12–17** *(moderate)*. Move 1 only: Elisha feeds a hundred men with twenty loaves; his servant objects; "they ate and had some left over, according to the word of the LORD" (Swete ἔφαγον καὶ κατέλιπον) `[T]`. The disciples object (9:13), the people eat (ἔφαγον ("they ate")), and twelve baskets are left over (9:17) — Elisha's miracle at a greater scale. With the Exodus manna in the "desolate place" (ἐν ἐρήμῳ τόπῳ, 9:12) as a second frame `[I]`, moderate.

*Internal:* **plants §24:29–31, 35** — the day declining (9:12; 24:29, κέκλικεν ἤδη ἡ ἡμέρα ("the day is now nearly over")) and taking, blessing, breaking and giving (9:16; 24:30; cf. 22:19). κλίνω ("to decline") for the day occurs only at 9:12 and 24:29, verified; the recognition "in the breaking of the bread" (24:35) is the feeding remembered (high). **Plants §23:8** — Herod (high). **Plants §10:39; 17:16** — at his feet (high). **Answers §4:25–27** — Elijah and Elisha enacted (moderate).

**Pitfall.** "Jesus calms the storms of your life." It turns a revelation of who he is into a promise about circumstances; the disciples end the scene φοβηθέντες ("fearful", 8:25), not comforted. The corrective: the storm is stilled so that they ask the right question.

---

## 15. Luke 9:18–27 — The Christ of God Must Suffer ⭐

**Position.** Q1: 8:25 and 9:9 asked who he is, and 9:7–8 listed the crowd's answers. Q2: the confession comes here because the question has been asked by everyone else, and because the confession must be followed at once by the δεῖ ("it is necessary") of the passion. Luke has no Caesarea Philippi and no Peter's rebuke; the confession moves straight to the cross. `[T]`

**Structure.** Jesus praying alone; the crowd's answers (18–19); Peter's confession (20); the command to silence and the first passion prediction (21–22); the call to daily cross-bearing (23–26); some standing here (27).

**Text-first findings.**

- **The same three answers.** "John the Baptist, others Elijah, others that one of the prophets of old has risen" (9:19) repeats 9:7–8 almost word for word `[T]`.
- **"The Christ of God".** Τὸν χριστὸν τοῦ θεοῦ ("the Christ of God", 9:20). The phrase occurs twice in Luke: Peter's confession here, and the rulers' sneer at the cross, εἰ οὗτός ἐστιν ὁ χριστὸς τοῦ θεοῦ, ὁ ἐκλεκτός ("if this is the Christ of God, his Chosen One", 23:35) `[T]`, verified. The confession returns as mockery.
- **The first passion δεῖ.** Δεῖ τὸν υἱὸν τοῦ ἀνθρώπου πολλὰ παθεῖν καὶ ἀποδοκιμασθῆναι … καὶ ἀποκτανθῆναι καὶ τῇ τρίτῃ ἡμέρᾳ ἐγερθῆναι ("the Son of Man must suffer many things and be rejected … and be killed and be raised up on the third day", 9:22) `[T]`. ἀποδοκιμάζω ("to reject") occurs three times in Luke — here, at 17:25, and in the quotation of Ps 118:22 at 20:17 (λίθον ὃν ἀπεδοκίμασαν ("the stone which the builders rejected")) `[T]`, verified. The prediction uses the psalm's verb before the psalm is cited.
- **Daily.** ἀράτω τὸν σταυρὸν αὐτοῦ καθ' ἡμέραν ("take up his cross daily", 9:23). Mark 8:34 lacks καθ' ἡμέραν ("daily") `[T]`, checked. The cross is not only martyrdom; it is every day.

**Tool 11.** No formula citation. **Ps 118:22** stands behind ἀποδοκιμασθῆναι ("be rejected", 9:22) *(moderate–high)* — the verb is the psalm's, and Luke will quote the psalm at 20:17. Move 1: the stone rejected by the builders becomes the head of the corner, "the LORD's doing, marvellous in our eyes", in a psalm of the king's entry through the gates (118:19–27). The psalm is a live source: 13:35 and 19:38 take its v.26. *What it adds:* the first prediction already contains the rejection-and-exaltation of the entry psalm.

*Internal:* **plants §23:35** — "the Christ of God" (high). **Plants §17:25; 20:17** — ἀποδοκιμάζω (high). **Plants §24:7, 46** — τῇ τρίτῃ ἡμέρᾳ ("on the third day"); τρίτος stands of the resurrection day at 9:22; 18:33; 24:7, 21, 46, verified (high). **Plants §24:6–8** — the prediction the women are told to remember (high).

**Tool 8.** The NASB95 renders δεῖ as "must" here and at 24:7, 26 ("was it not necessary"), 44 ("must be fulfilled"); the English reader can follow the thread, but not at 2:49 ("I had to be") or 13:33 ("I must journey"), where the rendering changes. No pulpit text is declared.

**Pitfall.** "Everyone has a cross to bear." It shrinks the cross to ordinary hardship. The cross here is the Son of Man's rejection and death (9:22), and the disciple's daily cross is to follow him into it (9:23–24). The corrective: the "daily" makes it every day, not merely a hard day.

---

## 16. Luke 9:28–50 — His Exodus ⭐

**Position.** Q1: 9:27 promised that some standing there would see the kingdom before tasting death, and 9:22 predicted the passion. Q2: the Transfiguration follows at once, eight days later, because the glory must be seen *with* the talk of the exodus to be accomplished in Jerusalem — and because the book is about to turn towards that city (9:51). The descent into faithlessness and misunderstanding (9:37–50) completes a pattern begun on the mountain.

**Structure.** The ascent to pray (28); the change and the two men (29–31); the sleeping disciples and Peter's tents (32–33); the cloud and the voice (34–36); the descent: the boy and the faithless generation (37–43a); the second prediction, hidden from them (43b–45); who is greatest (46–48); the outsider exorcist (49–50).

**Text-first findings.**

- **Eight days, and prayer.** ὡσεὶ ἡμέραι ὀκτώ ("some eight days", 9:28) where Mark 9:2 has μετὰ ἡμέρας ἕξ ("six days") `[T]`, checked; ἀνέβη εἰς τὸ ὄρος προσεύξασθαι ("he went up on the mountain to pray") and ἐν τῷ προσεύχεσθαι αὐτόν ("while he was praying", 9:28–29) — the change happens in prayer `[T]`.
- **The face.** τὸ εἶδος τοῦ προσώπου αὐτοῦ ἕτερον ("the appearance of his face became different", 9:29). Moses came down from Sinai not knowing ὅτι δεδόξασται ἡ ὄψις τοῦ χρώματος τοῦ προσώπου αὐτοῦ ("that the appearance of the skin of his face was glorified", Exod 34:29 Swete) `[T]`. *Moderate.*
- **The exodus.** ἔλεγον τὴν ἔξοδον αὐτοῦ ἣν ἤμελλεν πληροῦν ἐν Ἰερουσαλήμ ("they were speaking of his departure which he was about to accomplish at Jerusalem", 9:31). ἔξοδος ("departure, exodus") stands once in Luke `[T]`; it is the name of the book Moses is associated with, and its verb πληροῦν ("to fulfil") is the book's fulfilment word. The NASB95's "departure" hides the exodus.
- **Heavy with sleep.** ἦσαν βεβαρημένοι ὕπνῳ ("were overcome with sleep", 9:32); at Olivet Jesus finds them κοιμωμένους … ἀπὸ τῆς λύπης ("sleeping from sorrow", 22:45) `[T]`. *Moderate.* The disciples sleep through the glory and through the agony.
- **Entering the cloud.** ἐγένετο νεφέλη καὶ ἐπεσκίαζεν αὐτούς· ἐφοβήθησαν δὲ ἐν τῷ εἰσελθεῖν αὐτοὺς εἰς τὴν νεφέλην ("a cloud formed and began to overshadow them; and they were afraid as they entered the cloud", 9:34). ἐπισκιάζω is the verb of the tabernacle cloud (Exod 40:29 Swete) and of Mary's conception (1:35) `[T]`; Moses εἰσῆλθεν … εἰς τὸ μέσον τῆς νεφέλης ("entered the midst of the cloud", Exod 24:18 Swete) `[T]`.
- **"The faithless and perverted generation".** Ὦ γενεὰ ἄπιστος καὶ διεστραμμένη ("you unbelieving and perverted generation", 9:41). Mark 9:19 has only ἄπιστος ("unbelieving") `[T]`, checked. διεστραμμένη ("perverted") is from the Song of Moses: γενεὰ σκολιὰ καὶ διεστραμμένη ("a crooked and perverse generation", Deut 32:5 Swete), and γενεὰ ἐξεστραμμένη … υἱοὶ οἷς οὐκ ἔστιν πίστις ("a perverse generation, sons in whom is no faith", 32:20) `[T]`. *High on the wording.*
- **"He gave him back to his father."** ἀπέδωκεν αὐτὸν τῷ πατρὶ αὐτοῦ (9:42) — the third only child (μονογενής, 9:38) restored with the Elijah formula of 7:15 `[T]`.
- **Hidden.** ἦν παρακεκαλυμμένον ἀπ' αὐτῶν ἵνα μὴ αἴσθωνται αὐτό ("it was concealed from them so that they would not perceive it", 9:45) `[T]`. (MorphGNT lemmatises the verb as παρακαλύπτομαι; a first search under παρακαλύπτω returned nothing — positive control.)

**Tool 11.**

**Deut 18:15 with Ps 2:7 and Isa 42:1 → 9:35** *(moderate–high)*. *Source context:* Deut 18:15–19 — the LORD will raise up a prophet like Moses from among Israel; αὐτοῦ ἀκούσεσθε ("you shall listen to him"); the promise answers Israel's request at Horeb not to hear the voice from the fire again (18:16). *Book usage:* Deuteronomy was cited three times at the testing (4:4, 8, 12); this is its fourth use, and the Mosaic frame of the whole scene (Moses present, the cloud, the face) makes it high-probability. *OT-to-OT:* the Horeb setting of Deut 18:16 is the Sinai of Exod 24 and 34 — the passage's other frame. *Triage (category 2, within the NT):* the critical text's ὁ ἐκλελεγμένος ("the Chosen One") takes up Isa 42:1 (ὁ ἐκλεκτός μου ("my chosen")) and sets up 23:35 (ὁ ἐκλεκτός); the Majority text's ὁ ἀγαπητός ("the beloved") repeats 3:22. *What it adds:* on the mountain where Moses and Elijah appear, the voice says that the one to be heard now is this Son — the prophet like Moses whom Moses himself is speaking with.

**Deut 32:5, 20 with the Exod 32 pattern → 9:37–43** *(moderate — pattern and wording)*. Move 1: the Song of Moses indicts a perverse generation with no faith, after Moses' last ascent. The adjacency check applies: the pericope has staged a Sinai ascent (mountain, cloud, glory, Moses), and it is followed by a descent into a failing crowd, as Moses came down to the calf (Exod 32:7 Swete, κατάβηθι· ἠνόμησεν γὰρ ὁ λαός σου ("go down, for your people have acted lawlessly")). The contrast matters as much as the likeness: Moses breaks the tablets; Jesus heals the boy and gives him back to his father.

*Internal:* **answers §1:35** — ἐπισκιάζω (moderate–high). **Plants §9:51; 22–24** — the exodus to be fulfilled in Jerusalem (high). **Plants §22:45** — the sleeping disciples (moderate). **Plants §23:35** — ὁ ἐκλεκτός, critical text only (moderate–high). **Plants §18:34; 24:45** — "hidden from them" (9:45) against "hidden from them" (κεκρυμμένον, 18:34) and "he opened their minds" (24:45) (high). **Answers §7:15** — the Elijah formula (high). **Plants §16:29–31; 24:27, 44** — Moses and Elijah, the Law and the Prophets, speak with Jesus about his death; the risen Jesus will interpret "Moses and all the prophets" about himself (moderate–high).

**Pitfall.** "Mountaintop experiences." The scene is not about religious highs; it is about the exodus Jesus will accomplish by dying in Jerusalem, and Peter's wish to stay (9:33) is corrected by the voice. The corrective: preach what Moses and Elijah were talking about.

---

## 17. Luke 9:51–10:24 — He Set His Face ⭐

**Position.** Q1: 9:22 and 9:44 predicted the passion, and 9:31 named the exodus to be fulfilled "in Jerusalem". Q2: the journey begins here because the destination has now been named twice and the disciples still do not understand (9:45). Everything from here to 19:27 is told on the road to the city where the prophet must die (13:33).

**Structure.** The solemn turn and the Samaritan refusal (9:51–56); three would-be followers (9:57–62); the seventy-two sent (10:1–12); woes on the Galilean towns (10:13–16); the return and Satan's fall (10:17–20); the Son's thanksgiving and the blessed eyes (10:21–24).

**Text-first findings.**

- **The solemn turn.** Ἐγένετο δὲ ἐν τῷ συμπληροῦσθαι τὰς ἡμέρας τῆς ἀναλήμψεως αὐτοῦ ("when the days were approaching for his ascension", 9:51) `[T]`. ἀνάλημψις ("taking up") stands once in the NT; its verb ἀναλαμβάνω is Swete's word for Elijah's departure (4 Kgdms 2:9–11) and Luke's for the ascension in Acts (1:2, 11, 22) `[T]`, verified. The journey to the cross is dated by its end in heaven.
- **The face, three times.** τὸ πρόσωπον ἐστήρισεν ("he set his face", 9:51); ἀπέστειλεν ἀγγέλους πρὸ προσώπου αὐτοῦ ("he sent messengers on ahead of him", 9:52); τὸ πρόσωπον αὐτοῦ ἦν πορευόμενον εἰς Ἰερουσαλήμ ("his face was set toward Jerusalem", 9:53); and at 10:1 the seventy-two go πρὸ προσώπου αὐτοῦ ("ahead of him") `[T]`. πρόσωπον ("face") occurs four times in 9:51–10:1 `[T]`, verified. The NASB95 renders 9:51 "He was determined", which loses both the idiom and the repetition. The idiom is Ezekiel's: στήρισον τὸ πρόσωπόν σου ἐπὶ Ἰερουσαλήμ ("set your face towards Jerusalem", Ezek 21:2 Swete), a command to prophesy against the city and its sanctuary; and the Servant sets his face "like flint" in Isa 50:7 (Swete ἔθηκα τὸ πρόσωπόν μου ὡς στερεὰν πέτραν) `[T]`. *Moderate–high* for Ezekiel (the verb and the city match), *moderate* for Isaiah.
- **The disciples as the messengers.** ἀπέστειλεν ἀγγέλους πρὸ προσώπου αὐτοῦ (9:52) is the wording of Mal 3:1 and Exod 23:20 as quoted at 7:27, ἀποστέλλω τὸν ἄγγελόν μου πρὸ προσώπου σου ("I send my messenger ahead of you") `[T]`. John was the messenger; now the disciples are. `[I]`, high.
- **Fire refused.** Κύριε, θέλεις εἴπωμεν πῦρ καταβῆναι ἀπὸ τοῦ οὐρανοῦ καὶ ἀναλῶσαι αὐτούς; ("Lord, do you want us to command fire to come down from heaven and consume them?", 9:54) — Elijah's fire on the king's messengers, καταβήσεται πῦρ ἐκ τοῦ οὐρανοῦ (4 Kgdms 1:10, 12 Swete) `[T]`. Jesus rebukes them (9:55). The Majority text adds "as Elijah did" and "the Son of Man did not come to destroy men's lives but to save them"; the critical text leaves the allusion unspoken.
- **The plough.** Elisha, called from the plough, asks to kiss his father first, and Elijah lets him (3 Kgdms 19:20 Swete) `[T]`; Jesus does not (9:61–62). Luke's Jesus is the greater Elijah in both directions — gentler than Elijah's fire and more demanding than Elijah's call. `[I]`, high.
- **Appointed.** ἀνέδειξεν ὁ κύριος καὶ ἑτέρους ἑβδομήκοντα δύο ("the Lord appointed seventy-two others", 10:1). ἀναδείκνυμι ("to appoint publicly") occurs twice in the NT, here and at Acts 1:24 `[T]`. Its noun ἀνάδειξις was John's "appearance to Israel" (1:80), a NT hapax.
- **Greet no one.** μηδένα κατὰ τὴν ὁδὸν ἀσπάσησθε ("greet no one on the way", 10:4). Elisha sends Gehazi with the staff: ζῶσαι τὴν ὀσφύν σου … ἐὰν εὕρῃς ἄνδρα οὐκ εὐλογήσεις αὐτόν ("gird your loins … if you meet any man, do not salute him", 4 Kgdms 4:29 Swete) `[T]`. *Moderate* — the urgency of a mission to raise the dead.
- **Satan fallen.** Ἐθεώρουν τὸν Σατανᾶν ὡς ἀστραπὴν ἐκ τοῦ οὐρανοῦ πεσόντα ("I was watching Satan fall from heaven like lightning", 10:18) `[T]`. The adversary who claimed the kingdoms (4:6) falls as the kingdom's messengers go out.
- **The Son's joy and the Father's pleasure.** ἠγαλλιάσατο τῷ πνεύματι τῷ ἁγίῳ ("he rejoiced greatly in the Holy Spirit", 10:21). ἀγαλλιάω ("to rejoice greatly") occurs twice in Luke — Mary's ἠγαλλίασεν τὸ πνεῦμά μου ("my spirit has rejoiced", 1:47) and here `[T]`; εὐδοκία ("good pleasure") occurs twice — the Gloria's ἀνθρώποις εὐδοκίας ("people of [his] good pleasure", 2:14) and here, οὕτως εὐδοκία ἐγένετο ἔμπροσθέν σου ("this way was well-pleasing in your sight", 10:21) `[T]`, both verified. The infancy's vocabulary of joy and good pleasure returns in the Son's own prayer.
- **Handed over.** πάντα μοι παρεδόθη ὑπὸ τοῦ πατρός μου ("all things have been handed over to me by my Father", 10:22) — the devil's ἐμοὶ παραδέδοται ("it has been handed over to me", 4:6) answered with the same verb `[T]`.

**Tool 11.**

**2 Kgs 1:10–12 and 1 Kgs 19:19–21 → 9:54, 61–62** *(high; moderate–high)*. *Source context:* Elijah calls down fire on two companies sent by Ahaziah to arrest him (2 Kgs 1), and throws his mantle over Elisha at the plough, allowing him to take leave of his parents (1 Kgs 19). *Book usage:* named at 4:25–26; enacted at 7:11–17 and 8:55; here twice in one pericope, and the taking up (2 Kgs 2) stands behind 9:51. *OT-to-OT:* the whole Elijah–Elisha succession — mantle, fire, taking up — is one story in Kings. *What it adds:* the journey begins by invoking Elijah three times in thirteen verses (the taking up, the fire, the plough). Luke's Jesus is taken up like Elijah, refuses Elijah's fire, and calls more urgently than Elijah — and the Spirit that Elisha asked for "double" (2 Kgs 2:9) is what the disciples are told to wait for (24:49). *Synthetic, moderate.*

**Isa 14:12–15 → 10:15, 18** *(high; moderate)*. *Source context:* the taunt over the king of Babylon, the day star who said "I will ascend to heaven … I will make myself like the Most High", brought down to Sheol. *Book usage:* first use of Isa 14. *OT-to-OT:* Ezek 28 applies the same fall-from-heaven pattern to Tyre, which is named in 10:13–14 `[I]`. *What it adds:* Capernaum's pride is judged in Babylon's words (ἕως οὐρανοῦ … ἕως τοῦ ᾅδου ("to heaven … to Hades"), 10:15), and the fall from heaven that Isaiah taunted is seen happening to Satan.

**Ps 91:13 (Swete 90) → 10:19** *(moderate)*. Move 1: the one under the Most High's shelter treads on the adder and the serpent. The devil quoted the psalm's vv.11–12 at 4:10–11; here the authority of v.13 is given to the disciples. **Book usage (Move 2):** the psalm returns at 13:34 — ὑπὸ τὰς πτέρυγας ("under the wings", Ps 90:4 Swete) — making Ps 91 a live source with three uses `[T]`.

*Internal:* **answers §9:31** — the exodus to Jerusalem begins (high). **Answers §7:27** — the messengers πρὸ προσώπου (high). **Answers §4:6** — παραδίδωμι (moderate–high). **Answers §1:47; §2:14** — ἀγαλλιάω and εὐδοκία (moderate–high). **Answers §4:25–27** — Elijah (high). **Plants §24:51; Acts 1:2** — ἀνάλημψις (high).

**Number allusion — 10:1.** *Seventy or seventy-two*: the SBLGNT and NA28 read 72, the Majority text 70, and the NASB95 "seventy". The nations of Gen 10 number seventy in the Hebrew and seventy-two in the Greek tradition `[S]`; the elders of Num 11:24–26 are seventy, and two more receive the Spirit in the camp `[T]` for Numbers. Either reading has an Old Testament model; neither is decisive. *Uncertain* — carried to Open Questions.

**Pitfall.** Reading 9:57–62 as "Jesus is harsh to would-be followers". The three sayings are the Elijah call made absolute because the kingdom's urgency now exceeds Elijah's. The corrective: preach them beside 9:51 — the one who says "do not look back" has set his own face to die.

---

## 18. Luke 10:25–42 — Who Is My Neighbour? The One Thing

**Position.** Q1: 10:21–24 blessed those who see and hear what prophets and kings longed for. Q2: a lawyer comes "testing" him with the question of eternal life, and the answer is given in two scenes: a parable of love to the neighbour, and a woman who sits and hears. Together they answer the two commandments the lawyer quotes. `[I]`, moderate–high.

**Structure.** The lawyer's question and the two commandments (25–28); "who is my neighbour?" and the parable (29–37); Martha and Mary (38–42).

**Text-first findings.**

- **Testing.** νομικός τις ἀνέστη ἐκπειράζων αὐτόν ("a lawyer stood up and put him to the test", 10:25). ἐκπειράζω occurs twice in Luke — here, and in the Deuteronomy citation of the testing, Οὐκ ἐκπειράσεις κύριον τὸν θεόν σου ("you shall not put the Lord your God to the test", 4:12) `[T]`, verified.
- **The question asked twice.** Διδάσκαλε, τί ποιήσας ζωὴν αἰώνιον κληρονομήσω; ("Teacher, what shall I do to inherit eternal life?", 10:25) — the ruler asks it again at 18:18, adding only ἀγαθέ ("good") to the address `[T]`, checked.
- **Justifying himself.** θέλων δικαιῶσαι ἑαυτόν ("wishing to justify himself", 10:29) — the third of Luke's five δικαιόω (7:29, 35; 10:29; 16:15; 18:14), against the tax collector who goes home δεδικαιωμένος ("justified", 18:14) `[T]`.
- **The third compassion.** Σαμαρίτης … ἰδὼν ἐσπλαγχνίσθη ("a Samaritan … when he saw him, felt compassion", 10:33) — the second of the three σπλαγχνίζομαι, between the Lord at Nain (7:13) and the father (15:20) `[T]`.
- **"The one who did the mercy."** Ὁ ποιήσας τὸ ἔλεος μετ' αὐτοῦ ("the one who showed mercy toward him", 10:37). ἔλεος ("mercy") occurs six times in Luke: five in ch. 1, all of God's mercy (1:50, 54, 58, 72, 78), and this last one, done by a Samaritan `[T]`, verified. The mercy the canticles sang is done on the Jericho road by the man Israel despised.
- **Do.** τοῦτο ποίει καὶ ζήσῃ ("do this and you will live", 10:28) and πορεύου καὶ σὺ ποίει ὁμοίως ("go and do the same", 10:37) bracket the parable with ποιέω ("to do"), answering the lawyer's τί ποιήσας (10:25) `[T]`.
- **Hearing at his feet.** Mary παρακαθεσθεῖσα πρὸς τοὺς πόδας τοῦ Ἰησοῦ ἤκουεν τὸν λόγον αὐτοῦ ("seated at the Lord's feet, was listening to his word", 10:39); Martha περιεσπᾶτο ("was distracted") and μεριμνᾷς ("you are worried", 10:41) `[T]`. μεριμνάω ("to be anxious") returns at once in 12:11, 22, 25, 26, and μέριμνα ("worry") chokes the seed at 8:14 `[T]`, verified.

**Tool 11.**

**Deut 6:5 and Lev 19:18 → 10:27** *(high)*. *Source context:* Deut 6:4–9 is the Shema, Israel's confession of the one LORD and the command to love him with all; Lev 19:18 closes a chapter of neighbour-laws, "you shall love your neighbour as yourself: I am the LORD", and Lev 19:34 extends the same love to the stranger. *Book usage:* Deuteronomy's fifth use (4:4, 8, 12; 9:35); Leviticus' third (2:24; 5:14). *OT-to-OT:* the joining of the two commands is the lawyer's, and Jesus approves it (10:28); Lev 19:34 already pushes the neighbour to the stranger. *What it adds:* the parable answers "who is my neighbour?" by Lev 19:34's logic and then reverses it: the neighbour is not the one you must love but the one who loved — and he is a Samaritan.

**2 Chr 28:8–15 → 10:30–35** *(moderate–high — pattern and wording)*. *Source context:* the northern army takes captives from Judah; the prophet Oded rebukes them; men of Samaria clothe the naked captives, feed them, anoint them (ἀλείψασθαι), put the weak on donkeys (ἐν ὑποζυγίοις) and bring them to Jericho (εἰς Ἰερειχὼ πόλιν φοινίκων), and return to Samaria (2 Chr 28:15 Swete) `[T]`, read in full. *Book usage:* Chronicles was named at 11:51 (Zechariah) — the last book of the Tanak's span. *OT-to-OT:* none in this passage. *What it adds:* the Samaritan who binds, anoints with oil, sets the man on his own animal and brings him to shelter on the Jericho road repeats what Samaritans once did for Judah's captives on the road to Jericho. The lawyer's own Scripture contained a good Samaritan.

**Lev 18:5 → 10:28** *(moderate–high)*. Move 1 only: "you shall keep my statutes … by doing which a man shall live". The lawyer is answered in the terms of the law he asked about.

*Internal:* **answers §4:12** — ἐκπειράζω (high). **Plants §18:18** — the same question (high). **Answers §1:50–78** — ἔλεος (high). **Answers §7:13; plants §15:20** — the compassion triad (high). **Answers §8:14; plants §12:22–26; 21:34** — anxiety (moderate). **Answers §8:21** — hearing the word (moderate–high).

**Pitfall.** Book-level trap 2. "Be a Good Samaritan" preaches the parable as a moral tale and leaves out the question it answers and the reversal it performs. The lawyer wanted to limit his obligation; the parable made the hated outsider the one who fulfils the law. The corrective: preach it to the man who wanted to justify himself (10:29) — and then preach Mary, who sat at the feet of the one who does the mercy.

---

## 19. Luke 11:1–54 — Teach Us to Pray; the Stronger Man; Woes

**Position.** Q1: 10:38–42 set hearing Jesus' word above anxious service. Q2: the disciples' request to be taught to pray follows, because hearing turns into asking; and the chapter then sets the Father's gift of the Spirit (11:13) beside a controversy over what spirit Jesus acts by (11:15), and ends in woes on those who shut others out of knowledge.

**Structure.** The prayer (1–4); the friend at midnight (5–8); ask, seek, knock — the Father gives the Holy Spirit (9–13); Beelzebul and the stronger man (14–23); the returning spirit (24–26); "blessed rather" (27–28); the sign of Jonah (29–32); the lamp of the body (33–36); six woes at a Pharisee's table (37–54).

**Text-first findings.**

- **Daily.** τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δίδου ἡμῖν τὸ καθ' ἡμέραν ("give us each day our daily bread", 11:3) — the καθ' ἡμέραν ("each day") of the daily cross (9:23) `[T]`.
- **Temptation.** μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν ("lead us not into temptation", 11:4) — the prayer Jesus bids them pray at Olivet, προσεύχεσθε μὴ εἰσελθεῖν εἰς πειρασμόν ("pray that you may not enter into temptation", 22:40, 46) `[T]`.
- **The Holy Spirit, not "good things".** πόσῳ μᾶλλον ὁ πατὴρ ὁ ἐξ οὐρανοῦ δώσει πνεῦμα ἅγιον τοῖς αἰτοῦσιν αὐτόν ("how much more will your heavenly Father give the Holy Spirit to those who ask him?", 11:13). Matt 7:11 has ἀγαθά ("good things") `[T]`, checked. Luke names the gift the book will withhold until 24:49 and Acts 2.
- **The finger of God and the stronger man.** εἰ δὲ ἐν δακτύλῳ θεοῦ ἐκβάλλω τὰ δαιμόνια ("if I cast out demons by the finger of God", 11:20); ἐπὰν δὲ ἰσχυρότερος αὐτοῦ ἐπελθὼν νικήσῃ αὐτόν ("when someone stronger than he attacks him and overpowers him", 11:22) `[T]`. ἰσχυρότερος ("stronger") answers John's ὁ ἰσχυρότερός μου ("one mightier than I", 3:16).
- **Blessed rather.** Μακαρία ἡ κοιλία ἡ βαστάσασά σε ("blessed is the womb that bore you", 11:27) — Μενοῦν μακάριοι οἱ ἀκούοντες τὸν λόγον τοῦ θεοῦ καὶ φυλάσσοντες ("on the contrary, blessed are those who hear the word of God and observe it", 11:28) `[T]` — Mary's blessedness (1:42, 45, 48) defined by hearing.
- **Something greater here.** πλεῖον Σολομῶνος ὧδε … πλεῖον Ἰωνᾶ ὧδε ("something greater than Solomon is here … greater than Jonah is here", 11:31, 32) `[T]`.
- **Six woes.** οὐαί ("woe") falls six times in 11:42–52 — three on the Pharisees (11:42, 43, 44), three on the lawyers (11:46, 47, 52) `[T]`, verified.
- **From Abel to Zechariah.** ἵνα ἐκζητηθῇ τὸ αἷμα πάντων τῶν προφητῶν … ἀπὸ αἵματος Ἅβελ ἕως αἵματος Ζαχαρίου ("so that the blood of all the prophets … may be charged against this generation, from the blood of Abel to the blood of Zechariah", 11:50–51) `[T]`. See *Tool 11*.

**Tool 11.**

**Exod 8:19 (Swete; Heb 8:15) → 11:20** *(high)*. *Source context:* after the third plague, Pharaoh's magicians, who have matched the first two signs, cannot produce gnats and say Δάκτυλος θεοῦ ἐστὶν τοῦτο ("this is the finger of God"); Pharaoh's heart is hardened. *Book usage:* Exodus at 2:23 and in the ἔξοδος of 9:31. *OT-to-OT:* the finger of God writes the tablets (Exod 31:18) `[I]`. *What it adds:* the opponents who attribute the exorcisms to Beelzebul take the part of the hardened Pharaoh, while the magicians knew better. The exorcisms are signs of a new exodus.

**Isa 49:24–25 and 53:12 → 11:21–22** *(moderate)*. Move 1: "can the prey be taken from the mighty? … the captives of the mighty shall be taken"; the Servant divides τῶν ἰσχυρῶν … σκῦλα ("the spoil of the strong", 53:12 Swete). Luke's τὰ σκῦλα αὐτοῦ διαδίδωσιν ("he distributes his plunder", 11:22) `[T]`. The Servant who will be "numbered with transgressors" (22:37, citing the same verse) is the stronger man.

**Jonah 3 and 1 Kgs 10:1 → 11:29–32** *(high — named)*. *Source context:* the Ninevites repent at Jonah's preaching (Jonah 3); the queen of Sheba comes to test Solomon's wisdom (1 Kgs 10). *Book usage:* Jonah's sleeping in the storm stood behind 8:22–25 (moderate); Solomon's glory returns at 12:27. *OT-to-OT:* both are Gentiles who received Israel's word — a prophet and a king. *What it adds:* the sign of this generation is the Son of Man himself, greater than the prophet and the king; and the Gentiles who heard lesser voices will condemn those who refuse the greater.

**Gen 4:10 and 2 Chr 24:20–22 → 11:50–51** *(high — named)*. *Source context:* Abel's blood cries from the ground (Gen 4:10); Zechariah son of Jehoiada, filled with the Spirit, rebukes the people and is stoned in the court of the LORD's house by the king's command, and dies saying יֵרֶא יְהוָה וְיִדְרֹשׁ ("may the LORD see and require it", 2 Chr 24:22) `[T]`, verified in the WLC (דָּרַשׁ, 1875). *Book usage:* Chronicles also supplied the Samaritans of 10:30–35. *OT-to-OT:* Gen 9:5's "I will require (ἐκζητήσω) the blood" and Reuben's τὸ αἷμα αὐτοῦ ἐκζητεῖται ("his blood is required", Gen 42:22 Swete) belong to the same vocabulary `[T]`. *Triage (category 1/3):* Luke's ἐκζητηθῇ ("be required") answers the Hebrew יִדְרֹשׁ exactly; Swete's κρινάτω ("let him judge") does not. *What it adds:* the first and last martyrs of the Tanak in BHS order — Genesis to Chronicles — frame "all the prophets". The dying prophet's prayer that God would "require" his blood is answered: it will be required of this generation. See *Canonical Position* in the overview for the caveat on the Chronicles-last sequence.

*Internal:* **answers §3:16** — the stronger one (high). **Answers §1:45, 48** — blessedness (moderate–high). **Answers §9:23** — καθ' ἡμέραν (moderate). **Plants §22:40, 46** — temptation (high). **Plants §24:49** — the Spirit to be given (high). **Plants §13:33–34** — the prophets killed in Jerusalem (high).

**Pitfall.** The friend at midnight (11:5–8) preached as "keep pestering God until he gives in". The next verses make the point by contrast: if a friend in bed will get up, and if evil fathers give good gifts, "how much more" the Father (11:13). The corrective: the parable argues from the lesser to the greater, not from nagging to success.

---

## 20. Luke 12:1–59 — Fear, Greed, Readiness, Fire

**Position.** Q1: 11:37–54 exposed Pharisaic hypocrisy and ended with the opponents lying in wait (11:54). Q2: the teaching turns to the disciples, "first", about hypocrisy and fear (12:1–12), because the hostility just shown will reach them (12:11); then to possessions and anxiety, and to readiness for the master's return, because the journey to the cross opens a time between his going and his coming.

**Structure.** Hypocrisy and the fear of God (1–12); the rich fool (13–21); anxiety and the kingdom (22–34); watchful servants (35–48); fire, baptism and division (49–53); reading the time (54–59).

**Text-first findings.**

- **Friends who need not fear.** Λέγω δὲ ὑμῖν τοῖς φίλοις μου ("I say to you, my friends", 12:4) `[T]`.
- **Hairs counted.** αἱ τρίχες τῆς κεφαλῆς ὑμῶν πᾶσαι ἠρίθμηνται ("the very hairs of your head are all numbered", 12:7); θρὶξ ἐκ τῆς κεφαλῆς ὑμῶν οὐ μὴ ἀπόληται ("not a hair of your head will perish", 21:18) `[T]`. θρίξ ("hair") occurs four times in Luke — the woman's hair (7:38, 44) and these two `[T]`, verified.
- **Deny.** ὁ δὲ ἀρνησάμενός με ἐνώπιον τῶν ἀνθρώπων ἀπαρνηθήσεται ("he who denies me before men will be denied", 12:9); ἀπαρνέομαι ("to deny") occurs three times in Luke — here and of Peter (22:34, 61) `[T]`, verified.
- **The fool's feast.** Ψυχή, ἔχεις πολλὰ ἀγαθὰ … ἀναπαύου, φάγε, πίε, εὐφραίνου ("soul, you have many goods … take your ease, eat, drink and be merry", 12:19); εἶπεν δὲ αὐτῷ ὁ θεός· Ἄφρων ("but God said to him, 'You fool!'", 12:20) `[T]`. εὐφραίνω ("to make merry") occurs six times in Luke — this fool's feast (12:19), the father's feast four times (15:23, 24, 29, 32), and the rich man who feasted every day (16:19) `[T]`, verified. Two rich men's feasts bracket the father's.
- **Loins girded.** Ἔστωσαν ὑμῶν αἱ ὀσφύες περιεζωσμέναι καὶ οἱ λύχνοι καιόμενοι ("be dressed in readiness, and keep your lamps lit", 12:35) — the Passover instruction, αἱ ὀσφύες ὑμῶν περιεζωσμέναι ("your loins girded", Exod 12:11 Swete), in the same form `[T]`. *Moderate–high.*
- **The master who serves.** περιζώσεται καὶ ἀνακλινεῖ αὐτοὺς καὶ παρελθὼν διακονήσει αὐτοῖς ("he will gird himself to serve, and have them recline at the table, and will come up and wait on them", 12:37). περιζώννυμι ("to gird") occurs three times in Luke: the servants' readiness (12:35), the master who serves (12:37), and the servant who serves his master (17:8) `[T]`, verified. At the Last Supper, ἐγὼ δὲ ἐν μέσῳ ὑμῶν εἰμι ὡς ὁ διακονῶν ("I am among you as the one who serves", 22:27).
- **Baptism to be accomplished.** βάπτισμα δὲ ἔχω βαπτισθῆναι, καὶ πῶς συνέχομαι ἕως ὅτου τελεσθῇ ("I have a baptism to undergo, and how distressed I am until it is accomplished!", 12:50). τελέω ("to accomplish") occurs four times in Luke (SBLGNT): the family completing the law (2:39), this baptism (12:50), "all things written through the prophets … will be accomplished" (18:31), and "this which is written must be fulfilled (τελεσθῆναι) in me" (22:37) `[T]`, verified.

**Tool 11.**

**Sir 11:18–19; Eccl 8:15 → 12:16–20** *(moderate–high; moderate)*. Move 1: Ben Sira's rich man says εὗρον ἀνάπαυσιν, καὶ νῦν φάγομαι ἐκ τῶν ἀγαθῶν μου ("I have found rest, and now I will eat of my goods"), and οὐκ οἶδεν … καταλείψει αὐτὰ ἑτέροις καὶ ἀποθανεῖται ("he does not know … he will leave them to others and die", Sir 11:19 Swete) `[T]`. The fool's ἀναπαύου … φάγε ("take your ease … eat") and God's ἃ δὲ ἡτοίμασας, τίνι ἔσται; ("the things you have prepared — whose will they be?") follow Sirach closely. Qoheleth's "eat, drink and be merry" (8:15) is the context the fool has misread `[I]`.

**Exod 12:11 → 12:35** *(moderate–high)*. Move 1: the Passover meal eaten in haste, loins girded, sandals on, staff in hand, the night of the LORD's passing through. The disciples are to live as on Passover night, ready for the exodus. The Passover returns at 22:1–20.

**Mic 7:6 → 12:53** *(high)*. Move 1: Micah's lament over a society in which "a man's enemies are the men of his own household", followed by "but as for me, I will watch for the LORD" (7:7). The division Jesus brings is the prophet's night before the dawn.

**Ps 147:9; Job 38:41 → 12:24** *(moderate)*. Move 1: God gives the young ravens their food. Luke names κόρακες ("ravens"), where Matthew has "birds" (Matt 6:26) `[T]`.

*Internal:* **plants §21:18** — the hairs (high). **Plants §22:34, 57, 61** — denial (high). **Plants §15:23–32; 16:19** — the feasts (high). **Plants §17:8; 22:27** — the girded server (high). **Plants §18:31; 22:37** — τελέω (high). **Answers §3:16** — "fire" (12:49) and "baptism" (12:50) take up John's "he will baptise you with the Holy Spirit and fire" (moderate). **Answers §10:41; plants §21:34** — μεριμνάω, μέριμνα (moderate). **Plants §21:14–15** — "the Holy Spirit will teach you in that very hour what you ought to say" (12:12) becomes "I will give you utterance and wisdom" (21:15) (moderate–high).

**Pitfall.** Preaching 12:13–34 as financial prudence. The fool is not condemned for saving but for being "not rich toward God" (12:21) and for treating his soul as his own; and 12:33 ("sell your possessions") is a command to disciples. The corrective: the question is where the heart's treasure is (12:34), asked of people on the road to the cross.

---

## 21. Luke 13:1–35 — Repent; a Daughter of Abraham Set Free; Jerusalem, Jerusalem ⭐

**Position.** Q1: 12:54–59 rebuked the crowds for not reading "this present time". Q2: this chapter reads the time for them — calamities that call for repentance, a fig tree given one last year, a kingdom growing from a seed, a narrow door closing — and ends with Jesus naming Jerusalem as the place where he must die. It is the journey's first lament over the city.

**Structure.** Two disasters and "unless you repent" (1–5); the barren fig tree (6–9); the bent woman freed on the Sabbath (10–17); mustard seed and leaven (18–21); the narrow door (22–30); Herod the fox and "today, tomorrow, the third day" (31–33); the lament over Jerusalem (34–35).

**Text-first findings.**

- **"You will all likewise perish."** ἐὰν μὴ μετανοῆτε πάντες ὁμοίως ἀπολεῖσθε ("unless you repent, you will all likewise perish", 13:3, 5) — twice, verbatim except ὁμοίως/ὡσαύτως `[T]`.
- **Eighteen, three times.** The eighteen on whom the tower fell (13:4); the woman bent for eighteen years (13:11, 16) `[T]`. Calamity and bondage stand side by side; the difference is release.
- **Duelling necessities.** The synagogue ruler: Ἓξ ἡμέραι εἰσὶν ἐν αἷς δεῖ ἐργάζεσθαι ("there are six days in which work should be done", 13:14). Jesus: ταύτην δὲ θυγατέρα Ἀβραὰμ οὖσαν … οὐκ ἔδει λυθῆναι ἀπὸ τοῦ δεσμοῦ τούτου τῇ ἡμέρᾳ τοῦ σαββάτου; ("and this woman, a daughter of Abraham … should she not have been released from this bond on the Sabbath day?", 13:16) `[T]`. Two δεῖ in three verses, the ruler's and the Son's.
- **Daughter and son of Abraham.** θυγατέρα Ἀβραάμ ("a daughter of Abraham", 13:16) and υἱὸς Ἀβραάμ ("a son of Abraham", 19:9) — the only two such phrases in Luke, and both introduce a release on the journey `[T]`, verified. The book that warned "do not say, 'we have Abraham as our father'" (3:8) calls two outsiders his children.
- **Bound by Satan, loosed.** ἣν ἔδησεν ὁ Σατανᾶς ("whom Satan has bound", 13:16); Γύναι, ἀπολέλυσαι τῆς ἀσθενείας σου ("woman, you are freed from your sickness", 13:12) `[T]`. The healing is framed as release from Satan's bond — the ἄφεσις ("release") of 4:18 enacted. `[I]`, high.
- **Today, tomorrow, the third day.** σήμερον καὶ αὔριον, καὶ τῇ τρίτῃ τελειοῦμαι ("today and tomorrow, and the third day I reach my goal", 13:32); πλὴν δεῖ με σήμερον καὶ αὔριον καὶ τῇ ἐχομένῃ πορεύεσθαι, ὅτι οὐκ ἐνδέχεται προφήτην ἀπολέσθαι ἔξω Ἰερουσαλήμ ("nevertheless I must journey on today and tomorrow and the next day; for it cannot be that a prophet would perish outside of Jerusalem", 13:33) `[T]`. τελειόω ("to complete, reach the goal") occurs twice in Luke: the boy's family "completing" the Passover days (2:43) and here `[T]`, verified. Two σήμερον, a δεῖ, and the third day in one saying.

**Tool 11.**

**Ps 118:26 (Swete 117) → 13:35** *(high — formula of the psalm)*. *Source context:* Ps 118 is the song of the king's entry through the gates of righteousness — the rejected stone made head of the corner (118:22), "this is the day the LORD has made" (118:24), "blessed is he who comes in the name of the LORD; we bless you from the house of the LORD" (118:26), and the festal procession to the altar (118:27). *Book usage:* the psalm's rejection verb stood in the first passion prediction (9:22, ἀποδοκιμασθῆναι); v.26 is sung at the entry (19:38) and v.22 quoted at 20:17. Luke follows the psalm's own movement — rejected, then hailed at the gate, then vindicated as the cornerstone. *OT-to-OT:* Jer 22:5 (below) is Jeremiah's temple-gate sermon; the psalm is a temple-gate liturgy. *What it adds:* "you will not see me until you say" — the entry of 19:38 answers the saying, but on the lips of the disciples, not of the city. The city's greeting is still outstanding.

**Jer 22:5; 12:7 → 13:35a** *(moderate)*. Move 1: at the palace of the king of Judah, Jeremiah warns that if the king does not do justice "this house will become a desolation" (22:5); in 12:7 the LORD says "I have forsaken my house, I have abandoned my inheritance". Ἰδοὺ ἀφίεται ὑμῖν ὁ οἶκος ὑμῶν ("behold, your house is left to you", 13:35) takes up both. The Majority text and the NASB95 add ἔρημος ("desolate"), which makes Jer 22:5 explicit.

**Ps 91:4 (Swete 90:4) → 13:34** *(moderate)*. Move 1: ὑπὸ τὰς πτέρυγας αὐτοῦ ἐλπιεῖς ("under his wings you will trust") — Luke's ὑπὸ τὰς πτέρυγας ("under her wings"). The psalm's third use (4:10–11; 10:19): the refuge the devil tried to exploit and the city refused.

**Ps 6:8; Ps 107:3 → 13:27, 29** *(high; moderate–high)*. Move 1: "depart from me, all you workers of iniquity" (Ps 6:8) — the sufferer's word to his enemies becomes the householder's word to those shut out; the redeemed gathered "from east and west, north and south" (Ps 107:3) are the guests at the kingdom's table. Ps 107's fourth use (1:53, 79; 8:24).

**The fig tree: Isa 5:1–7; Hos 9:10; Mic 7:1 → 13:6–9** *(moderate)*. Move 1: God looks for fruit from his vineyard and finds none (Isa 5); Israel was like early figs (Hos 9:10). The fig tree planted *in the vineyard* (13:6) joins the two images. Isa 5 returns explicitly at 20:9.

*Internal:* **answers §4:18** — release (high). **Answers §3:8; plants §19:9** — Abraham's children (high). **Plants §19:38** — Ps 118:26 (high). **Plants §19:41–44; 21:20–24; 23:28–31** — the lament over Jerusalem (high). **Plants §24:7, 21, 46** — the third day (moderate–high). **Answers §11:47–51** — the prophets killed (high).

**Pitfall.** Book-level trap 3. "Jerusalem rejected Jesus, so God rejected Jerusalem." The lament is spoken with longing — ποσάκις ἠθέλησα ἐπισυνάξαι τὰ τέκνα σου ("how often I wanted to gather your children together", 13:34) — and ends not in a verdict but in a condition ("until you say"). The corrective: preach the hen's wings before the empty house.

---

## 22. Luke 14:1–35 — The Great Banquet; Counting the Cost

**Position.** Q1: 13:29 promised a table in the kingdom for people from east and west, and 13:30 said the last would be first. Q2: a Sabbath meal at a Pharisee's house follows, where the question of who sits where and who is invited is acted out at table, and the parable of the banquet shows who will actually eat in the kingdom. Then the crowds are told what following costs.

**Structure.** The man with dropsy on the Sabbath (1–6); places at table (7–11); whom to invite (12–14); the great banquet (15–24); the cost of discipleship (25–35).

**Text-first findings.**

- **Silent opponents.** οἱ δὲ ἡσύχασαν ("but they kept silent", 14:4); ἡσυχάζω occurs twice in Luke — here, and of the women who τὸ μὲν σάββατον ἡσύχασαν κατὰ τὴν ἐντολήν ("rested on the Sabbath according to the commandment", 23:56) `[T]`, verified. *Uncertain* as a designed echo.
- **The same four, twice.** κάλει πτωχούς, ἀναπείρους, χωλούς, τυφλούς ("invite the poor, the crippled, the lame, the blind", 14:13); τοὺς πτωχοὺς καὶ ἀναπείρους καὶ τυφλοὺς καὶ χωλοὺς εἰσάγαγε ὧδε ("bring in here the poor and crippled and blind and lame", 14:21) `[T]`. ἀνάπηρος ("crippled") occurs in the NT only in these two verses `[T]`. (The SBLGNT prints the spelling ἀναπείρους, but MorphGNT files the lemma as ἀνάπηρος; a first lemma search under ἀνάπειρος returned nothing — positive control.) The master of the banquet does what Jesus told the host to do.
- **Exalt and humble.** πᾶς ὁ ὑψῶν ἑαυτὸν ταπεινωθήσεται καὶ ὁ ταπεινῶν ἑαυτὸν ὑψωθήσεται ("everyone who exalts himself will be humbled, and he who humbles himself will be exalted", 14:11) — repeated verbatim at 18:14, and the Magnificat's reversal (1:52) made a rule `[T]`.
- **Three excuses.** A field, five yoke of oxen, a new wife (14:18–20) `[T]`. See *Tool 11*.
- **Two sweeps of the city.** First εἰς τὰς πλατείας καὶ ῥύμας τῆς πόλεως ("into the streets and lanes of the city", 14:21), then εἰς τὰς ὁδοὺς καὶ φραγμούς ("into the highways and along the hedges", 14:23) — outside the city `[T]`. The second sweep reaches beyond Israel's town. `[I]`, moderate.

**Tool 11.**

**Prov 25:6–7 → 14:8–10** *(moderate–high)*. Move 1: "do not put yourself forward in the king's presence … for it is better to be told, 'Come up here' (Swete Ἀνάβαινε πρὸς μέ), than to be put lower in the presence of the prince" `[T]`. Luke's Φίλε, προσανάβηθι ἀνώτερον ("friend, move up higher", 14:10). Jesus turns a proverb of court etiquette into a picture of the kingdom's reversal.

**Deut 20:5–7; 24:5 → 14:18–20** *(moderate)*. Move 1: the exemptions from holy war — a man with a new house, a new vineyard, a betrothed wife; a newly married man stays home a year. The guests plead the holy-war exemptions for a feast, and the feast is the kingdom `[I]`. *Pattern, not quotation.*

*Internal:* **answers §1:52–53** — reversal (high). **Answers §13:29–30** — the kingdom table (high). **Plants §18:14** — the repeated saying (high). **Answers §9:23** — "whoever does not carry his own cross" (14:27) (high). **Plants §16:19–31** — the poor man at the rich man's gate (moderate).

**Pitfall.** Reading 14:26 ("hate father and mother") literally as a command to hostility, or softening it into "love less". It is Semitic comparison at its sharpest, placed beside the cross (14:27) and the renunciation of all possessions (14:33). The corrective: preach the cost as the cost of following the one who is going to Jerusalem to die.

---

## 23. Luke 15:1–32 — Lost and Found ⭐

**Position.** Q1: 14:21–23 had the master fill his house with the poor and outsiders, and 14:35 closed "he who has ears to hear, let him hear". Q2: tax collectors and sinners now come "to hear him" (15:1), the Pharisees grumble, and Jesus answers with three parables that defend his table and invite the grumblers to the feast.

**Structure.** The setting — sinners drawing near to hear, the Pharisees grumbling (1–2); the lost sheep (3–7); the lost coin (8–10); the lost son and the elder brother (11–32).

**Text-first findings.**

- **Hearing and grumbling.** Ἦσαν δὲ αὐτῷ ἐγγίζοντες πάντες οἱ τελῶναι καὶ οἱ ἁμαρτωλοὶ ἀκούειν αὐτοῦ ("all the tax collectors and the sinners were coming near him to listen to him", 15:1); καὶ διεγόγγυζον ("and they began to grumble", 15:2) `[T]`. διαγογγύζω occurs twice in Luke, here and at Zacchaeus' house (19:7) `[T]`, verified. In Swete it is the verb of Israel grumbling in the wilderness (Exod 16:7, 8; Num 16:11) `[T]`. *Moderate.*
- **A hundred, ten, two.** One of a hundred sheep, one of ten coins, one of two sons `[T]`: the proportion narrows until the lost one is half the household.
- **Lost and found, joy and repentance.** ἀπόλλυμι ("to lose; to perish") and εὑρίσκω ("to find") run through all three; χαρά ("joy") at 15:7, 10; χαίρω ("to rejoice") at 15:5, 32; συγχαίρω ("rejoice with") at 15:6, 9 `[T]`. συγχαίρω occurs three times in Luke — the neighbours rejoicing with Elizabeth (1:58) and the two calls to neighbours here (15:6, 9) `[T]`, verified.
- **The refrain.** οὗτος ὁ υἱός μου νεκρὸς ἦν καὶ ἀνέζησεν, ἦν ἀπολωλὼς καὶ εὑρέθη ("this son of mine was dead and has come to life again; he was lost and has been found", 15:24), repeated to the elder brother with ὁ ἀδελφός σου ("your brother", 15:32) `[T]`.
- **The third compassion.** εἶδεν αὐτὸν ὁ πατὴρ αὐτοῦ καὶ ἐσπλαγχνίσθη καὶ δραμὼν ἐπέπεσεν ἐπὶ τὸν τράχηλον αὐτοῦ καὶ κατεφίλησεν αὐτόν ("his father saw him and felt compassion for him, and ran and embraced him and kissed him", 15:20) `[T]` — the last of the three σπλαγχνίζομαι.
- **Scattered.** διεσκόρπισεν τὴν οὐσίαν αὐτοῦ ("he squandered his estate", 15:13). διασκορπίζω occurs three times in Luke — God scattering the proud (1:51), the son scattering his estate (15:13), and the manager scattering his master's goods (16:1) `[T]`, verified.
- **"It was necessary."** εὐφρανθῆναι δὲ καὶ χαρῆναι ἔδει ("but we had to celebrate and rejoice", 15:32) `[T]` — a δεῖ of celebration, spoken by the father.

**Tool 11.**

**Ezek 34:11–16 → 15:3–7** *(high — pattern with wording at 19:10)*. *Source context:* the LORD condemns Israel's shepherds, who have not sought the lost, and says he himself will seek his sheep: τὸ ἀπολωλὸς ζητήσω ("I will seek the lost", 34:16 Swete), then set one shepherd, "my servant David", over them (34:23). *Book usage:* first appearance; the wording surfaces at 19:10 (ζητῆσαι καὶ σῶσαι τὸ ἀπολωλός ("to seek and to save the lost")), which closes the journey. *OT-to-OT:* Ps 119:176 (Swete 118:176), ἐπλανήθην ὡσεὶ πρόβατον ἀπολωλός ("I have gone astray like a lost sheep"), is the lost sheep's own prayer `[T]`. *What it adds:* the shepherd who goes after the lost is the LORD of Ezek 34, doing what the leaders — here, the grumbling Pharisees — did not.

**Gen 33:4 → 15:20** *(moderate–high)*. *Source context:* Jacob, who had taken his brother's birthright and blessing, returns after twenty years expecting vengeance; προσέδραμεν Ἠσαὺ εἰς συνάντησιν αὐτῷ, καὶ περιλαβὼν αὐτὸν ἐφίλησεν καὶ προσέπεσεν ἐπὶ τὸν τράχηλον αὐτοῦ ("Esau ran to meet him, embraced him, fell on his neck and kissed him", Swete) `[T]`. *Book usage:* first use of the Jacob–Esau story, whose womb-leaping stood behind 1:41 (moderate). *OT-to-OT:* none in this passage. *What it adds:* the father runs, falls on the son's neck and kisses him — the elder brother's welcome in Genesis. In the parable the elder brother will not come in. The one who should have run as Esau ran stays outside.

*Internal:* **answers §5:30** — the grumbling at table (high). **Answers §1:51** — διασκορπίζω (moderate). **Answers §7:13; 10:33** — the compassion triad completed (high). **Answers §12:19** — the fool's merrymaking against the father's (high). **Answers §1:58** — neighbours rejoicing (moderate). **Plants §19:7–10** — the grumbling and the lost found (high). **Plants §24:5** — "dead and alive again … lost and found" against "why do you seek the living among the dead?" (moderate). **Plants §16:25** — the father's Τέκνον ("son, child", 15:31) to the elder brother against Abraham's Τέκνον to the rich man (16:25); Mary's Τέκνον to the boy (2:48) is the first (moderate).

**Pitfall.** Book-level trap 2 again, in its best-known form. "The Prodigal Son" preached as a conversion story about the younger son, with the elder brother as an afterthought. The parables are told to the grumblers (15:2), and the third ends with the elder brother outside and the father pleading (15:28). The corrective: preach it as Jesus aimed it — at the respectable, with the door still open.

---

## 24. Luke 16:1–31 — God and Mammon; Moses and the Prophets ⭐

**Position.** Q1: 15:11–32 ended with a son who "squandered" his estate and a father who was generous. Q2: two parables about rich men follow, because the grumbling Pharisees are φιλάργυροι ("lovers of money", 16:14), and because the last question of the book — will they believe if someone rises from the dead? — must be asked before the journey reaches Jerusalem.

**Structure.** The shrewd manager (1–8); mammon and faithfulness (9–13); the Pharisees' scoffing and Jesus' reply — the law and the kingdom (14–18); the rich man and Lazarus (19–31).

**Text-first findings.**

- **Scattering.** ὡς διασκορπίζων τὰ ὑπάρχοντα αὐτοῦ ("as squandering his possessions", 16:1) — the verb of the younger son (15:13) `[T]`.
- **Faithful in a very little.** Ὁ πιστὸς ἐν ἐλαχίστῳ καὶ ἐν πολλῷ πιστός ἐστιν ("he who is faithful in a very little thing is faithful also in much", 16:10); the king in the parable of the minas: ὅτι ἐν ἐλαχίστῳ πιστὸς ἐγένου ("because you have been faithful in a very little thing", 19:17) `[T]`, verified. *Internal*, high.
- **Scoffing.** ἐξεμυκτήριζον αὐτόν ("they were scoffing at him", 16:14). ἐκμυκτηρίζω occurs twice in the NT — the money-loving Pharisees here, and the rulers at the cross, ἐξεμυκτήριζον δὲ καὶ οἱ ἄρχοντες ("even the rulers were sneering at him", 23:35) `[T]`, verified. Its source is Ps 22:7 (Swete 21:8), πάντες οἱ θεωροῦντές με ἐξεμυκτήρισάν με ("all who see me sneer at me"). The scoffing that begins at the teaching on money ends at the cross.
- **The law and the prophets until John.** Ὁ νόμος καὶ οἱ προφῆται μέχρι Ἰωάννου ("the Law and the Prophets were proclaimed until John", 16:16), followed at once by the permanence of the law (16:17) `[T]`.
- **The named beggar.** πτωχὸς δέ τις ὀνόματι Λάζαρος ("a poor man named Lazarus", 16:20) — the only named character in a parable of Jesus in the Gospels `[T]` for Luke; the name is Greek for Eleazar, "God helps" `[S]`, high.
- **Comforted now.** νῦν δὲ ὧδε παρακαλεῖται σὺ δὲ ὀδυνᾶσαι ("but now he is being comforted here, and you are in agony", 16:25) — the woe "you have your consolation" (6:24) enacted `[T]`.
- **Moses and the prophets.** Ἔχουσι Μωϋσέα καὶ τοὺς προφήτας· ἀκουσάτωσαν αὐτῶν ("they have Moses and the Prophets; let them hear them", 16:29); Εἰ Μωϋσέως καὶ τῶν προφητῶν οὐκ ἀκούουσιν, οὐδ' ἐάν τις ἐκ νεκρῶν ἀναστῇ πεισθήσονται ("if they do not listen to Moses and the Prophets, they will not be persuaded even if someone rises from the dead", 16:31) `[T]`.

**Tool 11.** No formula citation; the pericope's scriptural weight is **Moses and the prophets named as sufficient witness**. *Move 2 — how the book uses this pair:* Μωϋσῆς ("Moses") occurs in Luke at 2:22; 5:14; 9:30, 33; 16:29, 31; 20:28, 37; 24:27, 44, and προφήτης ("prophet") twenty-nine times, verified. "Moses and the prophets" as a phrase stands at 16:29, 31; 24:27 (Μωϋσέως καὶ … πάντων τῶν προφητῶν ("Moses and all the prophets")) and 24:44 (νόμῳ Μωϋσέως καὶ προφήταις καὶ ψαλμοῖς ("the Law of Moses and the Prophets and the Psalms")) `[T]`. The parable's claim — that the Scriptures, not a resurrection, persuade — is what Luke 24 enacts: the risen Jesus does not rely on his appearance but opens the Scriptures (24:25–27, 44–47). *Synthetic — each constituent verified; the design is moderate–high.*

**Ps 22:7 (Swete 21:8) → 16:14** *(moderate)*. Move 1: the sufferer mocked by all who see him, in the psalm whose v.18 is quoted at 23:34 and whose v.7 stands behind 23:35. The verb's first use in Luke is here, against the Pharisees.

*Internal:* **answers §6:24** — the consolation (high). **Answers §15:13** — scattering (moderate). **Plants §19:17** — faithful in very little (high). **Plants §23:35** — ἐκμυκτηρίζω (high). **Plants §24:27, 44** — Moses and the prophets (high). **Plants §24:11, 25, 41** — resurrection does not by itself persuade: the apostles think the women's report λῆρος ("nonsense", 24:11) and still disbelieve when he stands among them (24:41) (high). **Answers §3:8** — "Father Abraham" (16:24, 27, 30) is what John warned against trusting in (moderate–high).

**Pitfall.** Reading the rich man and Lazarus as a map of the afterlife. The parable uses the picture current in its world `[S]` to make a point about hearing Moses and the prophets now. The corrective: the ending is the point — and the book's own ending proves it.

---

## 25. Luke 17:1–18:34 — Faith, the Day of the Son of Man, and Prayer

**Position.** Q1: 16:31 closed on unbelief that a resurrection would not overcome. Q2: this block turns to faith — faith to forgive (17:3–6), faith that returns to give thanks (17:19), faith the Son of Man may not find when he comes (18:8), faith that receives the kingdom as a child (18:17) — and ends with the third passion prediction, which the Twelve do not understand (18:34). The journey notice (17:11) opens it; the prediction (18:31) closes it.

**Structure.** Stumbling, forgiveness, faith, duty (17:1–10); ten lepers, one Samaritan (17:11–19); the kingdom and the day of the Son of Man (17:20–37); the widow and the judge (18:1–8); the Pharisee and the tax collector (18:9–14); the children (18:15–17); the rich ruler (18:18–30); the third prediction (18:31–34).

**Text-first findings.**

- **The foreigner who returned.** εἷς δὲ ἐξ αὐτῶν, ἰδὼν ὅτι ἰάθη, ὑπέστρεψεν μετὰ φωνῆς μεγάλης δοξάζων τὸν θεόν … καὶ αὐτὸς ἦν Σαμαρίτης ("one of them, when he saw that he had been healed, turned back, glorifying God with a loud voice … and he was a Samaritan", 17:15–16); εἰ μὴ ὁ ἀλλογενὴς οὗτος ("except this foreigner", 17:18) `[T]`. ἀλλογενής ("foreigner") stands once in the NT `[T]`. The word stood on the Jerusalem temple's warning inscription barring foreigners from the inner courts `[S]`, high.
- **"Your faith has saved you."** The third of four (17:19) `[T]`.
- **"Within you" or "among you".** ἰδοὺ γὰρ ἡ βασιλεία τοῦ θεοῦ ἐντὸς ὑμῶν ἐστιν ("for behold, the kingdom of God is in your midst", 17:21), said to Pharisees (17:20) `[T]`. See Pitfall.
- **The δεῖ of rejection again.** πρῶτον δὲ δεῖ αὐτὸν πολλὰ παθεῖν καὶ ἀποδοκιμασθῆναι ἀπὸ τῆς γενεᾶς ταύτης ("but first he must suffer many things and be rejected by this generation", 17:25) — the second ἀποδοκιμάζω of three (9:22; 17:25; 20:17) `[T]`.
- **Vindication and vengeance.** The widow's Ἐκδίκησόν με ("give me legal protection", 18:3); the judge's ἐκδικήσω αὐτήν ("I will give her legal protection", 18:5); ὁ δὲ θεὸς οὐ μὴ ποιήσῃ τὴν ἐκδίκησιν τῶν ἐκλεκτῶν αὐτοῦ ("will not God bring about justice for his elect?", 18:7, 8) `[T]`. ἐκδίκησις ("vindication, vengeance") occurs three times in Luke — twice here, and at 21:22, ἡμέραι ἐκδικήσεως ("days of vengeance"), of Jerusalem `[T]`, verified. The same noun names God's vindication of his chosen and his judgement on the city.
- **"Be propitious to me."** Ὁ θεός, ἱλάσθητί μοι τῷ ἁμαρτωλῷ ("God, be merciful to me, the sinner", 18:13) — ἱλάσκομαι, the verb of atonement, once in Luke `[T]`. Ps 79:9 (Swete 78:9), ἱλάσθητι ταῖς ἁμαρτίαις ἡμῶν ("atone for our sins"), is the same prayer in the plural `[T]` — *moderate*. The prayer is made in the temple (18:10), the place of atonement.
- **Justified.** κατέβη οὗτος δεδικαιωμένος ("this man went to his house justified", 18:14) — the last of the five δικαιόω, against the Pharisee who trusted that he was righteous (18:9) `[T]`.
- **Impossible and possible.** Τὰ ἀδύνατα παρὰ ἀνθρώποις δυνατὰ παρὰ τῷ θεῷ ἐστιν ("the things that are impossible with people are possible with God", 18:27) — Gabriel's οὐκ ἀδυνατήσει παρὰ τοῦ θεοῦ πᾶν ῥῆμα ("nothing will be impossible with God", 1:37), now said of a rich man's salvation `[T]`.
- **Written through the prophets; hidden.** τελεσθήσεται πάντα τὰ γεγραμμένα διὰ τῶν προφητῶν τῷ υἱῷ τοῦ ἀνθρώπου ("all things which are written through the prophets about the Son of Man will be accomplished", 18:31); καὶ ἦν τὸ ῥῆμα τοῦτο κεκρυμμένον ἀπ' αὐτῶν ("and the meaning of this statement was hidden from them", 18:34) `[T]`. Three verbs of non-understanding stack in 18:34 (οὐδὲν … συνῆκαν ("they understood none"), κεκρυμμένον ("hidden"), οὐκ ἐγίνωσκον ("they did not comprehend")).

**Tool 11.**

**2 Kgs 5 → 17:11–19** *(moderate–high — named at 4:27)*. *Source context:* Naaman the Syrian, a leper, is told to wash in the Jordan; cleansed, he ἐπέστρεψεν ("returned") to Elisha with all his company and confessed "there is no God in all the earth except in Israel" (2 Kgs 5:15 Swete) `[T]`. *Book usage:* named at Nazareth (4:27) as the one leper Elisha cleansed; the Elijah–Elisha cycle is the book's fourth live source. *OT-to-OT:* none in this passage. *What it adds:* the one of ten who returns to give glory is the foreigner, as at Nazareth Jesus said he would be. What was named at the start of the ministry is enacted on the road to Jerusalem.

**Gen 6–7; 19 → 17:26–32** *(high — named)*. Move 1: the flood and Sodom — judgement falling on people eating, drinking, buying, building; Lot's wife looks back (Gen 19:26 Swete ἐπέβλεψεν … εἰς τὰ ὀπίσω ("looked back")). Luke: μὴ ἐπιστρεψάτω εἰς τὰ ὀπίσω ("must not turn back", 17:31) — and at 9:62, βλέπων εἰς τὰ ὀπίσω ("looking back") disqualifies a disciple `[T]`. *Internal*, moderate–high.

**Exod 20:12–16 / Deut 5:16–20 → 18:20** *(high)*. Move 1: the commandments of the second table, in the order adultery, murder, theft, false witness, honour of parents. The ruler has kept them (18:21); what he lacks is the first table's single love, shown in parting with what he loves (18:22) `[I]`, moderate–high.

*Internal:* **answers §4:27** — Naaman (moderate–high). **Answers §1:37** — impossible with God (high). **Answers §14:11** — exalt and humble (high). **Answers §10:25** — the same question (high). **Answers §9:22, 44** — the third prediction (high). **Answers §9:62** — looking back (moderate–high). **Plants §21:22** — ἐκδίκησις (moderate). **Plants §23:35** — ἐκλεκτός ("chosen") occurs twice in Luke, God's "elect" (18:7) and the rulers' "Chosen One" (23:35) (moderate). **Plants §24:45** — understanding (high).

**Pitfall.** Book-level trap 5. "The kingdom of God is within you" (KJV) preached as inner spirituality. It is said to the Pharisees, who are asking when the kingdom will come; the kingdom is ἐντὸς ὑμῶν in the person of Jesus standing among them. The corrective: read 17:21 with 11:20 ("the kingdom of God has come upon you").

---

## 26. Luke 18:35–19:27 — To Seek and to Save the Lost; the King Who Goes Away ⭐

**Position.** Q1: 18:31–34 predicted the passion for the third time, and 18:18–30 asked whether a rich man can be saved. Q2: at Jericho, the last town before the ascent, a blind man sees and follows and a rich man is saved — the answers to 18:34 (they could not see) and 18:26 ("then who can be saved?") — and 19:10 sums up the whole journey. The parable of the minas follows, "because he was near Jerusalem", to stop the entry being misread (19:11).

**Structure.** The blind man at Jericho (18:35–43); Zacchaeus (19:1–10); the parable of the minas (19:11–27); the last journey notice (19:28).

**Text-first findings.**

- **"Son of David, have mercy."** Ἰησοῦ υἱὲ Δαυίδ, ἐλέησόν με (18:38, 39) — the first time anyone in Luke calls Jesus Son of David, and it is a blind beggar `[T]`. ἐλεάω ("to have mercy") occurs four times in Luke: the rich man to Abraham (16:24), the ten lepers (17:13), and the blind man twice (18:38, 39) `[T]`, verified. (MorphGNT lemma ἐλεάω; a first search under ἐλεέω returned nothing — positive control.)
- **Sight.** Ἀνάβλεψον ("receive your sight", 18:42) — the ἀνάβλεψις ("recovery of sight") of the Nazareth reading (4:18) given `[T]`.
- **Rich, small, seeking.** Zacchaeus is ἀρχιτελώνης καὶ … πλούσιος ("a chief tax collector, and he was rich", 19:2) — πλούσιος like the ruler who went away sad (18:23) `[T]`. He ἐζήτει ἰδεῖν τὸν Ἰησοῦν ("was trying to see who Jesus was", 19:3) — the phrase used of Herod (9:9; cf. 23:8). But the Son of Man ἦλθεν … ζητῆσαι ("came to seek", 19:10). The seeker is sought. `[T]`
- **Today, must, today.** σήμερον γὰρ ἐν τῷ οἴκῳ σου δεῖ με μεῖναι ("for today I must stay at your house", 19:5); Σήμερον σωτηρία τῷ οἴκῳ τούτῳ ἐγένετο ("today salvation has come to this house", 19:9) `[T]`. Two σήμερον and a δεῖ; the last σωτηρία ("salvation") of the four (1:69, 71, 77; 19:9).
- **Fourfold.** ἀποδίδωμι τετραπλοῦν ("I will give back four times as much", 19:8). The law of theft: τέσσερα πρόβατα ἀντὶ τοῦ προβάτου ("four sheep for a sheep", Exod 22:1 Swete) `[T]`; and David's verdict on the rich man of Nathan's parable, יְשַׁלֵּם אַרְבַּעְתָּיִם ("he shall repay fourfold", 2 Sam 12:6) — where Swete reads ἑπταπλασίονα ("sevenfold") `[T]`, verified in both. *Triage (category 1/2):* Zacchaeus' fourfold matches the Hebrew of 2 Sam 12:6 and Exod 22:1, not Swete's Samuel. *Moderate* for the Samuel echo.
- **A son of Abraham.** καθότι καὶ αὐτὸς υἱὸς Ἀβραάμ ἐστιν ("because he, too, is a son of Abraham", 19:9) — the pair to the daughter of Abraham (13:16) `[T]`.
- **"We do not want this man to reign."** Οὐ θέλομεν τοῦτον βασιλεῦσαι ἐφ' ἡμᾶς ("we do not want this man to reign over us", 19:14), answered at 19:27 by the order to slaughter τοὺς μὴ θελήσαντάς με βασιλεῦσαι ἐπ' αὐτούς ("who did not want me to reign over them") `[T]` — the parable's inclusio.
- **Faithful in a very little.** 19:17 repeats 16:10 (above) `[T]`.

**Tool 11.**

**Ezek 34:16 → 19:10** *(high)*. *Source context:* see pericope 23. *Book usage:* the lost sheep of 15:3–7 was the pattern; here the wording arrives, ζητῆσαι καὶ σῶσαι τὸ ἀπολωλός ("to seek and to save the lost") against τὸ ἀπολωλὸς ζητήσω ("I will seek the lost") `[T]`. *OT-to-OT:* Ezek 34:23–24 sets David as the one shepherd — and the blind man has just called Jesus "Son of David" (18:38) `[T]`. *What it adds:* the journey's closing summary is the LORD's shepherd promise, spoken by the Son of David on the edge of Jerusalem.

**Dan 7:13–14 → 19:12, 15** *(moderate — from the dig in hand)*. The 19:11–27 dig (12 July 2026) argued that the nobleman who goes "to receive a kingdom and return" follows the Son of Man's investiture in Dan 7, activated by Luke at 21:27 and 22:69 `[S: dig]`. The sweep confirms the grid is present in the parable's wording (λαβεῖν ἑαυτῷ βασιλείαν καὶ ὑποστρέψαι ("to receive a kingdom for himself and then return"), 19:12) `[T]`, and keeps the allusion at moderate: there is no verbal contact with Daniel in the parable itself.

*Internal:* **answers §4:18** — sight to the blind (high). **Answers §18:23–27** — a rich man saved (high). **Answers §15:1–7** — the lost sought (high). **Answers §13:16** — Abraham's children (high). **Answers §1:69–77** — σωτηρία (high). **Answers §16:10** — faithful in very little (high). **Plants §19:41–44; 20:14; 23:18** — the citizens who will not have him reign: at the vineyard, ἀποκτείνωμεν αὐτόν ("let us kill him", 20:14); before Pilate, Αἶρε τοῦτον ("away with this man", 23:18) (high; the dig's finding, verified). **Plants §23:8** — seeking to see (moderate).

**Checking stage — the dig in hand.** The 19:11–27 dig predates the corpus and worked from the ESV recalled; its verdicts stand as `[S: dig]`. The sweep confirms three of them from the Greek: the purpose preface of 19:11 is a Lukan habit (15:3; 18:1, 9), not an anomaly; 19:28 is the last journey notice; the judgement-of-rejecters inclusio (19:14, 27) is the parable's clearest forward thread. It adds one thing the dig did not see: **19:17 repeats 16:10**, so the parable's commendation takes up the teaching on faithfulness with money.

**Pitfall.** Zacchaeus preached as a model of generosity ("give half your goods"). The order in the text runs the other way: Jesus' "today I must stay at your house" (19:5) comes first, then the response, then the declaration of salvation (19:9) and its ground in the Son of Man's seeking (19:10). The corrective: preach the seeking Saviour before the generous tax collector.


---

## 27. Luke 19:28–48 — The King, the Tears, the Temple ⭐

**Position.** Q1: 13:35 said Jerusalem would not see him "until you say, 'Blessed is he who comes in the name of the Lord'", and the parable just told (19:11–27) warned that the kingdom was not about to appear at once and that the citizens would refuse their king. Q2: the entry follows because both sayings now come true at the gate. The king is acclaimed — by his disciples, not by the city — and the visitation announced in 1:68 arrives and is not recognised (19:44).

**Structure.** The last journey notice and the colt (28–36); the acclamation on the descent (37–40); the lament over the city (41–44); the temple cleared and daily teaching (45–48).

**Text-first findings.**

- **A colt no one has sat on.** πῶλον δεδεμένον, ἐφ' ὃν οὐδεὶς πώποτε ἀνθρώπων ἐκάθισεν ("a colt tied there, on which no one yet has ever sat", 19:30); the tomb is one οὗ οὐκ ἦν οὐδεὶς οὔπω κείμενος ("where no one had ever lain", 23:53) `[T]`. The unused beast and the unused tomb bracket the Jerusalem narrative. `[I]`, moderate.
- **"The Lord has need of it."** Ὁ κύριος αὐτοῦ χρείαν ἔχει (19:31, 34) — the title the narrator has used since 7:13, now in Jesus' own instruction `[T]`.
- **The king, written in.** Εὐλογημένος ὁ ἐρχόμενος βασιλεὺς ἐν ὀνόματι κυρίου ("blessed is the King who comes in the name of the Lord", 19:38). Swete Ps 117:26 has no βασιλεύς ("king") `[T]`; Mark 11:10 has "the coming kingdom of our father David" and Matt 21:9 "Son of David" `[T]`, checked. Luke (with John 12:13) puts the title into the psalm.
- **Peace in heaven.** ἐν οὐρανῷ εἰρήνη καὶ δόξα ἐν ὑψίστοις ("peace in heaven and glory in the highest", 19:38) — the angels sang δόξα ἐν ὑψίστοις θεῷ καὶ ἐπὶ γῆς εἰρήνη ("glory to God in the highest, and on earth peace", 2:14) `[T]`. At the birth, peace was announced *on earth*; at the entry, the disciples place it *in heaven*, and four verses later Jesus weeps because the city did not know τὰ πρὸς εἰρήνην ("the things which make for peace", 19:42) `[T]`. The earthly peace of 2:14 has been refused by the city. `[I]`, moderate–high.
- **The stones.** οἱ λίθοι κράξουσιν ("the stones will cry out", 19:40); two verses later, οὐκ ἀφήσουσιν λίθον ἐπὶ λίθον ("they will not leave one stone upon another", 19:44), repeated at 21:6 `[T]`. The stones that would acclaim him will be thrown down.
- **Weeping.** ἰδὼν τὴν πόλιν ἔκλαυσεν ἐπ' αὐτήν ("he saw the city and wept over it", 19:41); at the cross, μὴ κλαίετε ἐπ' ἐμέ ("stop weeping for me", 23:28) `[T]`. κλαίω ("to weep") occurs in Luke 11 times in 9 verses, verified; Jesus is its subject only here.
- **Hidden.** νῦν δὲ ἐκρύβη ἀπὸ ὀφθαλμῶν σου ("but now they have been hidden from your eyes", 19:42). κρύπτω ("to hide") has three occurrences in Luke: the leaven "hidden" in the flour (13:21), the passion saying hidden from the Twelve (18:34), and peace hidden from the city (19:42) `[T]`, verified. The disciples' blindness and the city's are named with one verb, but only the disciples' is opened (24:31, 45).
- **The siege.** παρεμβαλοῦσιν οἱ ἐχθροί σου χάρακά σοι καὶ περικυκλώσουσίν σε ("your enemies will throw up a barricade against you, and surround you", 19:43); ἐδαφιοῦσίν σε καὶ τὰ τέκνα σου ἐν σοί ("they will level you to the ground and your children within you", 19:44) `[T]`. χάραξ ("barricade") and ἐδαφίζω ("to dash to the ground") occur once each in the NT `[T]`, verified. See *Tool 11*.
- **The visitation missed.** ἀνθ' ὧν οὐκ ἔγνως τὸν καιρὸν τῆς ἐπισκοπῆς σου ("because you did not recognise the time of your visitation", 19:44). ἐπισκοπή ("visitation") stands once in Luke `[T]`; its verb ἐπισκέπτομαι ("to visit") is Zechariah's ἐπεσκέψατο ("he has visited", 1:68, 78) and the crowd's at Nain (7:16) `[T]`. Zechariah blessed the God who visits; the city does not know him when he comes.
- **The temple taken for teaching.** Καὶ ἦν διδάσκων τὸ καθ' ἡμέραν ἐν τῷ ἱερῷ ("and he was teaching daily in the temple", 19:47), matched at 21:37 and cited by Jesus at his arrest, καθ' ἡμέραν ὄντος μου μεθ' ὑμῶν ἐν τῷ ἱερῷ ("while I was with you daily in the temple", 22:53) `[T]`. The people ἐξεκρέματο αὐτοῦ ἀκούων ("were hanging on to every word he said", 19:48) — ἐκκρέμαμαι, a NT hapax `[T]`, verified by surface search (under the lemma ἐκκρεμάννυμι the index returns nothing). The leaders seek to destroy him; the people hang on his words. That split — rulers against people — runs to 23:35.

**Tool 11.**

**Ps 118:26 (Swete 117:26) → 19:38** *(high — quoted)*. *Source context:* the gate liturgy (see pericope 21). *Book usage:* foretold at 13:35; now sung; v.22 follows at 20:17. *OT-to-OT:* the king entering the LORD's house in procession belongs with Zech 9:9 and 1 Kgs 1 (below). *What it adds:* the disciples fulfil 13:35 early and in part. The saying was addressed to Jerusalem, and Jerusalem does not say it.

**Zech 9:9 and 1 Kgs 1:33–40 → 19:30–38** *(moderate — enacted, not quoted)*. Move 1: Zechariah's king comes to the daughter of Jerusalem δίκαιος καὶ σώζων … ἐπιβεβηκὼς ἐπὶ ὑποζύγιον καὶ πῶλον νέον ("righteous and saving … riding on a beast of burden and a young colt", Zech 9:9 Swete) `[T]`; David has Solomon set on his own mule and brought down to Gihon to be anointed and acclaimed (1 Kgs 1:33, 38 Swete; 3 Kgdms) `[T]`. Luke has πῶλος ("colt"), no citation, and the title "King". Garments spread for a king: Jehu, 2 Kgs 9:13 (Swete 4 Kgdms), ἔλαβεν ἕκαστος τὸ ἱμάτιον αὐτοῦ καὶ ἔθηκαν ὑποκάτω αὐτοῦ ("each man took his garment and placed it under him") and cried Ἐβασίλευσεν Εἰού ("Jehu is king") `[T]`; Luke's ὑπεστρώννυον τὰ ἱμάτια ἑαυτῶν ("they were spreading their coats", 19:36). *Moderate* for each, *moderate–high* for the combined royal pattern.

**Jer 6:14–15 → 19:42–44** *(moderate–high)*. *Source context:* Jeremiah indicts prophets and priests who say "Peace, peace" when there is no peace; they do not know their shame, and "in the time of their visitation they shall perish" — ἐν καιρῷ ἐπισκοπῆς ἀπολοῦνται (Jer 6:15 Swete), after a siege command in 6:6 `[T]`, verified. *Book usage:* Jeremiah was the source of 13:35 (22:5; 12:7) and supplies 19:46 (7:11). *OT-to-OT:* Jer 6 and Jer 7 are consecutive oracles against Jerusalem and its temple. *What it adds:* peace, ignorance and ἐν καιρῷ ἐπισκοπῆς ("in the time of visitation") all stand in Jer 6:14–15; Luke's τὸν καιρὸν τῆς ἐπισκοπῆς σου ("the time of your visitation") matches the phrase exactly `[T]`. **Book-overview note:** the overview's Jer 6:15 row originally cited the noun as a Hebrew lemma check; the WLC has the verb, not the noun — already corrected in the overview's colophon.

**Isa 29:3; Ps 137:9 (Swete 136:9); Hos 14:1 (Swete; Eng 13:16) → 19:43–44** *(moderate)*. Move 1: the LORD besieges Ariel (Jerusalem), βαλῶ περὶ σὲ χάρακα ("I will set a barricade around you", Isa 29:3 Swete) `[T]` — Luke's rare χάραξ. ἐδαφίζω ("dash to the ground") is the verb of Ps 136:9 Swete (ἐδαφιεῖ τὰ νήπιά σου ("will dash your little ones")) and of Hos 14:1 Swete (τὰ ὑποτίτθια αὐτῶν ἐδαφισθήσονται ("their infants will be dashed to pieces")) `[T]`. Jerusalem is to suffer what Babylon and Samaria were threatened with.

**Isa 56:7 and Jer 7:11 → 19:46** *(high — quoted, Γέγραπται ("it is written"))*. *Source context:* Isa 56:1–8 promises foreigners and eunuchs who hold the covenant a place in God's house, ὁ γὰρ οἶκός μου οἶκος προσευχῆς κληθήσεται πᾶσιν τοῖς ἔθνεσιν ("for my house shall be called a house of prayer for all the nations", Swete) `[T]`; Jer 7:1–15 is the temple sermon — "has this house … become a den of robbers?" — ending with the threat of Shiloh `[T]`. *Book usage:* the second Jeremiah use in the Jerusalem section, after 13:35. *OT-to-OT:* Isaiah's promise and Jeremiah's threat are about the same house. *What it adds:* Luke's quotation stops at οἶκος προσευχῆς ("house of prayer") and leaves out πᾶσιν τοῖς ἔθνεσιν ("for all the nations"), which Mark 11:17 keeps and Matthew also omits `[T]`, verified. For a book that ends with repentance proclaimed "to all the nations" (24:47), the omission is striking. The inference `[I]`, moderate: the nations will be reached, but not through this temple — the book ends in the temple (24:53), and the mission goes out "from Jerusalem" (24:47).

**Mal 3:1 → 19:45** *(moderate)*. Move 1: ἐξέφνης ἥξει εἰς τὸν ναὸν ἑαυτοῦ κύριος ("the Lord … will suddenly come to his temple", Swete) `[T]`, after the messenger prepares the way — the verse Luke has used for John (1:76; 7:27) and for the disciples (9:52). *Book usage:* Malachi's last use (after 1:17, 76, 78; 7:27; 9:52; 10:1). The Lord whose way was prepared comes to his temple, and "who can endure the day of his coming?" (Mal 3:2).

*Internal:* **answers §13:35** — Ps 118:26 (high). **Answers §2:14** — peace and glory (moderate–high). **Answers §1:68, 78; 7:16** — the visitation (high). **Answers §18:34** — κρύπτω (moderate–high). **Answers §19:14, 27** — the king rejected (high). **Plants §21:6** — stone on stone (high). **Plants §21:20–24; 23:28–31** — the city's children (high). **Plants §22:53** — daily in the temple (high). **Plants §23:53** — no one yet (moderate). **Plants §24:53** — the temple (high).

**Translations.** The NASB95 follows the Majority text's word order at 19:38 but otherwise tracks the SBLGNT here. At 19:44 its "the time of your visitation" keeps the link to 1:68 ("visited") that looser versions lose.

**Pitfall.** Book-level trap 4 in a new setting — "Palm Sunday triumph". Luke has no palms and no "Hosanna", and his entry ends in tears and in a prophecy of destruction. The corrective: preach 19:37–44 as one unit — the disciples' praise and the Lord's weeping — and the lament as a word of grief, not of satisfaction.

---

## 28. Luke 20:1–21:4 — By What Authority? The Rejected Stone; God of the Living; David's Lord

**Position.** Q1: 19:47–48 set the leaders seeking to destroy him and the people hanging on his words, in the temple. Q2: the leaders now come to him in the temple with a series of questions — about authority, tribute and resurrection — each meant to discredit him before the people (20:19–20, 26). He answers each and closes with a question of his own that they cannot answer (20:41–44), and the unit ends with a widow in the treasury.

**Structure.** Authority and John's baptism (20:1–8); the tenants of the vineyard (20:9–19); tribute to Caesar (20:20–26); the Sadducees and the resurrection (20:27–40); David's son and David's Lord (20:41–44); beware of the scribes (20:45–47); the widow's two coins (21:1–4).

**Text-first findings.**

- **The people as a threat.** ὁ λαὸς ἅπας καταλιθάσει ἡμᾶς ("all the people will stone us to death", 20:6) — καταλιθάζω, a NT hapax `[T]`, verified; the people are feared at 20:19 and 22:2 as well `[T]`.
- **A man planted a vineyard.** Ἄνθρωπος ἐφύτευσεν ἀμπελῶνα ("a man planted a vineyard", 20:9) — Isaiah's ἐφύτευσα ἄμπελον σωρήκ ("I planted a choice vine", Isa 5:2 Swete) and ἀμπελών ("vineyard", 5:1) `[T]`.
- **The beloved son.** πέμψω τὸν υἱόν μου τὸν ἀγαπητόν ("I will send my beloved son", 20:13). ἀγαπητός ("beloved") occurs twice in Luke, here and in the voice at the Jordan, ὁ υἱός μου ὁ ἀγαπητός (3:22) `[T]`, verified. The owner's question Τί ποιήσω; ("what shall I do?") is also the rich fool's (12:17) and the manager's (16:3) `[T]`. *Moderate* as a designed echo.
- **"Perhaps they will respect him."** ἴσως τοῦτον ἐντραπήσονται (20:13). ἐντρέπω ("to respect") occurs three times in Luke: the unjust judge who "did not respect man" (18:2, 4) and here `[T]`, verified.
- **"Let us kill him."** Οὗτός ἐστιν ὁ κληρονόμος· ἀποκτείνωμεν αὐτόν ("this is the heir; let us kill him", 20:14) — Joseph's brothers: νῦν οὖν δεῦτε ἀποκτείνωμεν αὐτόν ("come now, let us kill him", Gen 37:20 Swete) `[T]`. *Moderate–high* — the same hortatory, of the same kind of victim: the favoured son sent by the father.
- **The stone that crushes.** πᾶς ὁ πεσὼν ἐπ' ἐκεῖνον τὸν λίθον συνθλασθήσεται· ἐφ' ὃν δ' ἂν πέσῃ, λικμήσει αὐτόν ("everyone who falls on that stone will be broken to pieces; but on whomever it falls, it will scatter him like dust", 20:18) `[T]`. See *Tool 11*.
- **Pretending to be righteous.** ἐγκαθέτους ὑποκρινομένους ἑαυτοὺς δικαίους εἶναι ("spies who pretended to be righteous", 20:20) — the δίκαιος ("righteous") chain, which runs from Zechariah and Elizabeth (1:6) to the centurion's verdict and Joseph (23:47, 50) `[T]`. They pretend to be what the centurion will say Jesus was.
- **The accusation that will be falsified.** ἀπόδοτε τὰ Καίσαρος Καίσαρι ("render to Caesar the things that are Caesar's", 20:25); before Pilate, κωλύοντα φόρους Καίσαρι διδόναι ("forbidding to pay taxes to Caesar", 23:2) `[T]`. The charge is refuted by the narrative before it is made.
- **Sons of the resurrection.** ἰσάγγελοι γάρ εἰσιν καὶ υἱοί εἰσιν θεοῦ τῆς ἀναστάσεως υἱοὶ ὄντες ("they are like angels, and are sons of God, being sons of the resurrection", 20:36) — ἰσάγγελος, a NT hapax `[T]`, verified. "Son of God" was Adam's title in the genealogy (3:38) and Jesus' (1:35) `[T]`.
- **All live to him.** θεὸς δὲ οὐκ ἔστιν νεκρῶν ἀλλὰ ζώντων, πάντες γὰρ αὐτῷ ζῶσιν ("he is not the God of the dead but of the living; for all live to him", 20:38) — the last clause in Luke only `[T]`. The angels at the tomb take it up: Τί ζητεῖτε τὸν ζῶντα μετὰ τῶν νεκρῶν; ("why do you seek the living one among the dead?", 24:5) `[T]`. A 4 Maccabees parallel (7:19; 16:25) is often cited `[S]`; a surface search of Swete's 4 Maccabees for the wording returned nothing, so it is not asserted here.
- **"In the book of Psalms."** αὐτὸς γὰρ Δαυὶδ λέγει ἐν βίβλῳ ψαλμῶν ("for David himself says in the book of Psalms", 20:42) — Luke's name for the collection, which returns as ψαλμοῖς ("the Psalms", 24:44) `[T]`.
- **Widows.** The scribes οἳ κατεσθίουσιν τὰς οἰκίας τῶν χηρῶν ("who devour widows' houses", 20:47); a poor widow gives πάντα τὸν βίον ὃν εἶχεν ("all that she had to live on", 21:4) `[T]`. χήρα ("widow") occurs nine times in Luke — Anna (2:37), Zarephath (4:25, 26), Nain (7:12), the persistent widow (18:3, 5), and these three (20:47; 21:2, 3) `[T]`, verified. βίος ("living") is the word of the younger son's inheritance (15:12, 30) and of the woman who spent her living on physicians (8:43) `[T]`, verified.

**Tool 11.**

**Isa 5:1–7 → 20:9–16** *(high — retold)*. *Source context:* the song of the vineyard: the beloved does everything for his vineyard, it yields wild grapes, and the LORD will tear down its wall; "the vineyard of the LORD of hosts is the house of Israel" (5:7). *Book usage:* Isa 5 stood behind the fig tree in the vineyard (13:6–9, moderate). *OT-to-OT:* Ps 80:8–16 (the vine brought out of Egypt) belongs to the same image `[I]`. *What it adds:* Luke's parable relocates the failure. In Isaiah the vineyard yields no fruit; in the parable the tenants withhold it (20:10). The leaders understand at once — ἔγνωσαν γὰρ ὅτι πρὸς αὐτοὺς εἶπεν ("for they understood that he spoke this parable against them", 20:19) `[T]` — and the vineyard is given to others, not destroyed.

**Ps 118:22 (Swete 117:22) → 20:17** *(high — quoted, τὸ γεγραμμένον ("that which is written"))*. *Source context:* see pericope 21. *Book usage:* the third use of the psalm (13:35; 19:38; 20:17), following the psalm's own order backwards: the procession of 118:26 at the gate, then the rejected stone of 118:22. The verb ἀπεδοκίμασαν ("they rejected") is Swete's, and Luke has placed it in the first and second passion predictions (9:22; 17:25) `[T]`, verified — three ἀποδοκιμάζω, all tied to this verse. *OT-to-OT:* Isa 8:14–15 and 28:16 (below). *What it adds:* the passion predictions said the Son of Man "must" be rejected; here the text that required it is named.

**Isa 8:14–15; Dan 2:34–35, 44 (Theodotion) → 20:18** *(moderate; moderate–high)*. Move 1: the LORD is a stone of stumbling, πεσοῦνται καὶ συντριβήσονται ("they shall fall and be broken", Isa 8:15 Swete) `[T]` — Simeon's πτῶσιν … πολλῶν ("the fall … of many", 2:34) came from the same verse; the stone cut without hands crushes the kingdoms, λεπτυνεῖ καὶ λικμήσει ("it will crush and winnow", Dan 2:44 Theodotion) `[T]`, verified. Luke's λικμήσει ("will winnow, scatter as chaff") matches Theodotion's rare verb. The rejected stone becomes the stone of Daniel's kingdom.

**Exod 3:6 → 20:37** *(high — named, ἐπὶ τῆς βάτου ("at the bush"))*. Move 1: Ἐγώ εἰμι … θεὸς Ἀβραὰμ καὶ θεὸς Ἰσαὰκ καὶ θεὸς Ἰακώβ ("I am … the God of Abraham, the God of Isaac and the God of Jacob", Swete) `[T]`. The God who names himself by the dead patriarchs at the moment he comes down to deliver (Exod 3:8) is the God of the living. Abraham has been alive in Luke since 16:22–31.

**Deut 25:5 → 20:28** *(high)*. Move 1 only: the levirate law, which the Sadducees use to make resurrection absurd.

**Ps 110:1 (Swete 109:1) → 20:42–43** *(high — quoted)*. *Source context:* the LORD says to David's lord, "sit at my right hand until I make your enemies your footstool"; v.4 names him "a priest for ever after the order of Melchizedek". *Book usage:* posed as a riddle here; claimed at the trial (22:69). *OT-to-OT:* Dan 7:13 joins it at 22:69. *What it adds:* the Son of David title (18:38–39) and the King title (19:38) are not enough. David calls his son "Lord" — and the book has called Jesus ὁ κύριος ("the Lord") since 7:13.

*Internal:* **answers §3:22** — the beloved son (high). **Answers §9:22; 17:25** — ἀποδοκιμάζω (high). **Answers §2:34** — the stone of stumbling (moderate). **Answers §19:14** — "let us kill him" / "we do not want this man to reign" (high). **Answers §18:2–5** — ἐντρέπω and the widow (moderate). **Plants §22:69** — Ps 110:1 (high). **Plants §23:2** — the Caesar charge refuted in advance (high). **Plants §23:47** — δίκαιος (moderate–high). **Plants §24:5** — the living (moderate–high). **Plants §24:44** — the Psalms (moderate).

**Pitfall.** Preaching 21:1–4 as a stewardship sermon ("give sacrificially like the widow"). It follows directly on "they devour widows' houses" (20:47), and 21:5–6 follows it with the destruction of the temple she gave to. The corrective: preach her beside the scribes who consume her and the temple that will fall — she is commended, and the system is condemned.

---

## 29. Luke 21:5–38 — Not One Stone upon Another ⭐

**Position.** Q1: 19:43–44 prophesied the siege and levelling of Jerusalem, and the widow has just given everything to the temple (21:1–4). Q2: when some admire the temple's stones (21:5), Jesus gives the full prophecy, because the disciples must be told what will happen to the city and what they must do between its fall and the Son of Man's coming. The discourse is set in the temple (21:37–38), not on the Mount of Olives as in Mark.

**Structure.** The question about the temple (5–7); deceivers, wars, and "the end is not yet" (8–11); persecution first (12–19); Jerusalem surrounded and trampled (20–24); signs and the Son of Man (25–28); the fig tree (29–33); watch and pray (34–36); the daily pattern (37–38).

**Text-first findings.**

- **Stone on stone, again.** οὐκ ἀφεθήσεται λίθος ἐπὶ λίθῳ ὃς οὐ καταλυθήσεται ("there will not be left one stone upon another which will not be torn down", 21:6) — the lament of 19:44 extended from city to temple `[T]`.
- **"It must first."** δεῖ γὰρ ταῦτα γενέσθαι πρῶτον, ἀλλ' οὐκ εὐθέως τὸ τέλος ("for these things must take place first, but the end does not follow immediately", 21:9) `[T]`. The phrase ἃ δεῖ γενέσθαι ("what must take place") is Daniel's, in Theodotion (Dan 2:28) `[T]`, verified. *Moderate.* The δεῖ of the passion extends into the church's future.
- **A mouth and wisdom.** ἐγὼ γὰρ δώσω ὑμῖν στόμα καὶ σοφίαν ("for I will give you utterance and wisdom", 21:15) — the Lord's promise to Moses, ἐγὼ ἀνοίξω τὸ στόμα σου ("I will open your mouth", Exod 4:12 Swete) `[T]`. *Moderate.* At 12:12 the teacher was the Holy Spirit; here it is Jesus himself.
- **Hairs and endurance.** θρὶξ ἐκ τῆς κεφαλῆς ὑμῶν οὐ μὴ ἀπόληται ("not a hair of your head will perish", 21:18); ἐν τῇ ὑπομονῇ ὑμῶν κτήσασθε τὰς ψυχὰς ὑμῶν ("by your endurance you will gain your lives", 21:19) `[T]`. ὑπομονή ("endurance") occurs twice in Luke — the good soil that bears fruit ἐν ὑπομονῇ ("with perseverance", 8:15) and here `[T]`, verified. The parable of the sower and the discourse on the end share their last word.
- **Desolation, not the abomination.** Ὅταν δὲ ἴδητε κυκλουμένην ὑπὸ στρατοπέδων Ἰερουσαλήμ, τότε γνῶτε ὅτι ἤγγικεν ἡ ἐρήμωσις αὐτῆς ("when you see Jerusalem surrounded by armies, then recognise that her desolation is near", 21:20) `[T]`. ἐρήμωσις ("desolation") occurs once in Luke; Mark and Matthew have τὸ βδέλυγμα τῆς ἐρημώσεως ("the abomination of desolation"), Daniel's phrase `[T]` for the Synoptics. Luke names the thing plainly: armies around the city.
- **Days of vengeance.** ὅτι ἡμέραι ἐκδικήσεως αὗταί εἰσιν τοῦ πλησθῆναι πάντα τὰ γεγραμμένα ("because these are days of vengeance, so that all things which are written will be fulfilled", 21:22) `[T]`. See *Tool 11* and pericope 25.
- **Trampled until.** Ἰερουσαλὴμ ἔσται πατουμένη ὑπὸ ἐθνῶν, ἄχρι οὗ πληρωθῶσιν καιροὶ ἐθνῶν ("Jerusalem will be trampled underfoot by the Gentiles until the times of the Gentiles are fulfilled", 21:24) `[T]`. ἄχρι οὗ ("until") sets a limit to the trampling. What follows the limit is not said. `[I]`, moderate — carried to Open Questions.
- **The cloud, singular.** τὸν υἱὸν τοῦ ἀνθρώπου ἐρχόμενον ἐν νεφέλῃ μετὰ δυνάμεως καὶ δόξης πολλῆς ("the Son of Man coming in a cloud with power and great glory", 21:27) — Daniel's μετὰ τῶν νεφελῶν τοῦ οὐρανοῦ ("with the clouds of heaven", Dan 7:13 Theodotion) `[T]`, and Mark 13:26's ἐν νεφέλαις ("in clouds") made singular. The cloud of the transfiguration (9:34–35) and of the ascension, νεφέλη ὑπέλαβεν αὐτόν ("a cloud received him", Acts 1:9) — and the two men's promise οὕτως ἐλεύσεται ("he will come in just the same way", Acts 1:11) `[T]`. *Moderate–high.*
- **Redemption drawing near.** διότι ἐγγίζει ἡ ἀπολύτρωσις ὑμῶν ("because your redemption is drawing near", 21:28). ἀπολύτρωσις ("redemption") occurs once in Luke; λύτρωσις ("redemption") twice, in the Benedictus (1:68) and of those waiting in Jerusalem (2:38); λυτρόομαι ("to redeem") once, in the Emmaus pair's lost hope (24:21) `[T]`, verified. The redemption of Israel the infancy awaited is here set at the end.
- **Weighed down.** μήποτε βαρηθῶσιν ὑμῶν αἱ καρδίαι ἐν κραιπάλῃ καὶ μέθῃ καὶ μερίμναις βιωτικαῖς ("so that your hearts will not be weighted down with dissipation and drunkenness and the worries of life", 21:34). βαρέω ("to weigh down") occurs twice in Luke — the disciples βεβαρημένοι ὕπνῳ ("overcome with sleep", 9:32) at the transfiguration, and here `[T]`, verified. μέριμνα ("worry") and βιωτικός take up the thorns ὑπὸ μεριμνῶν καὶ πλούτου καὶ ἡδονῶν τοῦ βίου ("by worries and riches and pleasures of this life", 8:14) `[T]`.
- **A snare.** ὡς παγίς· ἐπεισελεύσεται γὰρ ἐπὶ πάντας τοὺς καθημένους ἐπὶ πρόσωπον πάσης τῆς γῆς ("like a trap; for it will come upon all those who dwell on the face of all the earth", 21:35) — φόβος καὶ βόθυνος καὶ παγὶς ἐφ' ὑμᾶς τοὺς ἐνοικοῦντας ἐπὶ τῆς γῆς ("terror and pit and snare are upon you, O inhabitant of the earth", Isa 24:17 Swete) `[T]`. *Moderate–high.*
- **Early to hear him.** πᾶς ὁ λαὸς ὤρθριζεν πρὸς αὐτὸν ἐν τῷ ἱερῷ ἀκούειν αὐτοῦ ("all the people would get up early in the morning to come to him in the temple to listen to him", 21:38) — ὀρθρίζω, a NT hapax `[T]`, verified.

**Tool 11.**

**Hos 9:7 and Deut 32:35 → 21:22** *(moderate)*. *Source context:* Hosea: ἥκασιν αἱ ἡμέραι τῆς ἐκδικήσεως, ἥκασιν αἱ ἡμέραι τῆς ἀνταποδόσεώς σου ("the days of vengeance have come, the days of your recompense have come", Hos 9:7 Swete) — the Hebrew is יְמֵי הַפְּקֻדָּה ("days of visitation") `[T]`; the Song of Moses: ἐν ἡμέρᾳ ἐκδικήσεως ἀνταποδώσω ("in the day of vengeance I will repay", Deut 32:35 Swete) `[T]`. *Book usage:* ἐκδίκησις ("vindication, vengeance") was the widow's vindication at 18:7–8. *OT-to-OT:* Hosea's "days of visitation" rendered "days of vengeance" joins the two Lukan ideas — the visitation missed (19:44) and the vengeance that follows (21:22). *Triage (category 1):* an English reader of Hosea sees "punishment" or "visitation" and misses what Luke's Greek audience heard. *Synthetic, moderate.*

**The Nazareth reading stopped short: Isa 61:2 → 4:19 and 21:22** *(moderate)*. At Nazareth Luke's quotation ends with κηρύξαι ἐνιαυτὸν κυρίου δεκτόν ("to proclaim the favourable year of the Lord", 4:19), before Isaiah's καὶ ἡμέραν ἀνταποδόσεως ("and the day of recompense", Isa 61:2 Swete) `[T]`. Isaiah's second half surfaces at 21:22, in the ἀνταπόδοσις ("recompense") vocabulary of Hos 9:7 and Deut 32:35, not in Isaiah's words. *Synthetic, uncertain* — no verbal link from 21:22 back to Isa 61:2.

**Dan 7:13–14 (Theodotion) → 21:27** *(high)*. *Source context:* one like a son of man comes with the clouds to the Ancient of Days and is given dominion, glory and a kingdom that shall not pass away. *Book usage:* the "Son of Man" title throughout; the nobleman's kingdom (19:12, moderate); the trial (22:69). *OT-to-OT:* Ps 110:1 joins it at 22:69. *What it adds:* the discourse ends not in the city's fall but in the Son of Man's coming, and the promise that οἱ λόγοι μου οὐ μὴ παρελεύσονται ("my words will not pass away", 21:33) makes Jesus' words carry the permanence Daniel gave the kingdom (7:14) and Isaiah the word of God (Isa 40:8). `[I]`, moderate–high.

**Isa 13:10; 34:4 → 21:25–26** *(moderate)*. Move 1: sun, moon and stars darkened over Babylon (13:10); αἱ δυνάμεις τῶν οὐρανῶν ("the powers of the heavens") dissolved in the judgement on Edom (34:4 Swete) `[T]`. The sea's roar (ἤχους θαλάσσης ("the roaring of the sea")) matches Ps 65:7 (Swete 64:8, ἤχους κυμάτων ("the roar of its waves")) — the God who stills the sea and the nations `[T]`. *Uncertain* for the Psalm.

**Zech 12:3 → 21:24** *(moderate)*. Move 1: Jerusalem made λίθον καταπατούμενον πᾶσιν τοῖς ἔθνεσιν ("a stone trampled by all the nations", Swete) `[T]`. In Zechariah the nations who trample are destroyed (12:9) and the LORD pours out on Jerusalem a spirit of grace (12:10). The Zechariah context contains the "until" that Luke leaves unspoken. `[I]`, moderate.

**Mic 7:6 → 21:16** *(moderate — second use)*. Betrayal by parents and brothers takes up the division of 12:53.

*Internal:* **answers §19:44** — stone on stone (high). **Answers §12:11–12** — the promised speech before rulers (high). **Answers §12:7** — the hairs (high). **Answers §8:14–15** — worries and endurance (high). **Answers §9:32** — weighed down (moderate). **Answers §18:7–8** — ἐκδίκησις (moderate). **Answers §1:68; 2:38** — redemption (high). **Answers §17:22–37** — the day of the Son of Man (high). **Plants §22:40, 46** — "praying" (21:36) and the Olivet prayer (high). **Plants §23:28–31** — the daughters of Jerusalem (high). **Plants §24:21** — λυτρόομαι (moderate–high). **Plants §24:51; Acts 1:9–11** — the cloud (moderate–high).

**Difficulty.** 21:32, οὐ μὴ παρέλθῃ ἡ γενεὰ αὕτη ἕως ἂν πάντα γένηται ("this generation will not pass away until all things take place"). Luke's structure separates the city's fall (21:20–24, dated within history) from the cosmic signs (21:25–28), with ἄχρι οὗ πληρωθῶσιν καιροὶ ἐθνῶν ("until the times of the Gentiles are fulfilled") between them `[T]`. The saying most naturally refers to the events of 21:8–24 `[I]`, moderate. It is a known crux `[S]`; a preacher should not build a timetable on it.

**Pitfall.** Book-level trap 3 again, with its opposite. One error hears 21:20–24 as God finished with Israel; the other maps the discourse onto current events. Luke dates the siege within history, sets a limit to the trampling (21:24), and ends with a command that applies to every generation: watch and pray (21:36). The corrective: preach what the discourse tells disciples to *do*.

---

## 30. Luke 22:1–38 — The Passover and the New Covenant ⭐

**Position.** Q1: 9:31 named Jesus' ἔξοδος ("exodus") to be fulfilled in Jerusalem, and 12:50 a baptism he must undergo. Q2: the Passover comes now because the exodus the transfiguration named is to be accomplished at the exodus festival. The meal interprets the death before it happens, and the farewell discourse prepares the apostles for the time between.

**Structure.** The plot and Judas (1–6); preparing the Passover (7–13); the meal — cup, bread, cup (14–20); the betrayer at the table (21–23); greatness and the kingdom appointed (24–30); Simon sifted and restored (31–34); purse, bag and sword (35–38).

**Text-first findings.**

- **Satan enters.** Εἰσῆλθεν δὲ Σατανᾶς εἰς Ἰούδαν ("and Satan entered into Judas", 22:3) — the devil left Jesus ἄχρι καιροῦ ("until an opportune time", 4:13) `[T]`. The καιρός ("opportune time") has come.
- **"It was necessary."** ἡ ἡμέρα τῶν ἀζύμων, ἐν ᾗ ἔδει θύεσθαι τὸ πάσχα ("the day of Unleavened Bread on which the Passover lamb had to be sacrificed", 22:7) `[T]` — δεῖ applied to the sacrifice of the lamb.
- **The guest room.** Ποῦ ἐστιν τὸ κατάλυμα ὅπου τὸ πάσχα μετὰ τῶν μαθητῶν μου φάγω; ("where is the guest room in which I may eat the Passover with my disciples?", 22:11). κατάλυμα ("lodging, guest room") occurs twice in Luke: there was no place for them ἐν τῷ καταλύματι ("in the inn", 2:7), and here the Lord asks for one and is given ἀνάγαιον μέγα ἐστρωμένον ("a large, furnished upper room", 22:12) `[T]`, verified. *Moderate* as a designed echo — Mark 14:14 has the same word.
- **"I have earnestly desired."** Ἐπιθυμίᾳ ἐπεθύμησα τοῦτο τὸ πάσχα φαγεῖν μεθ' ὑμῶν πρὸ τοῦ με παθεῖν ("I have earnestly desired to eat this Passover with you before I suffer", 22:15) — the Hebraic cognate intensive `[T]`; "until it is fulfilled in the kingdom of God" (22:16).
- **Breaking bread.** λαβὼν ἄρτον εὐχαριστήσας ἔκλασεν καὶ ἔδωκεν ("when he had taken some bread and given thanks, he broke it and gave it", 22:19). κλάω ("to break") occurs in Luke only here and at Emmaus, λαβὼν τὸν ἄρτον εὐλόγησεν καὶ κλάσας ἐπεδίδου ("he took the bread and blessed it, and breaking it, he began giving it", 24:30); the noun κλάσις ("breaking") at 24:35 and Acts 2:42 `[T]`, verified. The feeding used the compound κατακλάω (9:16) with the same four verbs (take, bless, break, give) `[T]`.
- **Poured out.** Τοῦτο τὸ ποτήριον ἡ καινὴ διαθήκη ἐν τῷ αἵματί μου, τὸ ὑπὲρ ὑμῶν ἐκχυννόμενον ("this cup which is poured out for you is the new covenant in my blood", 22:20). ἐκχέω ("to pour out") occurs three times in Luke — the wine that is spilled (5:37), τὸ αἷμα πάντων τῶν προφητῶν τὸ ἐκκεχυμένον ("the blood of all the prophets, shed", 11:50), and this cup (22:20) `[T]`, verified. The blood of the prophets "required of this generation" and the blood "poured out for you" share a verb. In Acts the same verb pours out the Spirit (2:17, 18, 33) `[T]`.
- **Covenant and appointment.** καινὴ διαθήκη ("new covenant", 22:20) and, nine verses later, κἀγὼ διατίθεμαι ὑμῖν, καθὼς διέθετό μοι ὁ πατήρ μου βασιλείαν ("and just as my Father has granted me a kingdom, I grant you", 22:29) `[T]`. διατίθεμαι ("to make a covenant, to appoint") is the verb of διαθήκη ("covenant"), once in Luke `[T]`, verified. Both OT texts behind 22:20 pair the same verb with the same noun: τὸ αἷμα τῆς διαθήκης ἧς διέθετο Κύριος ("the blood of the covenant which the Lord has made", Exod 24:8 Swete) and διαθήσομαι … διαθήκην καινήν ("I will make … a new covenant", Jer 38:31 Swete; Eng 31:31) `[T]`, verified. The kingdom is given to the apostles *as a covenant*. The NASB95's "grant" hides it.
- **The one who serves.** ἐγὼ δὲ ἐν μέσῳ ὑμῶν εἰμι ὡς ὁ διακονῶν ("but I am among you as the one who serves", 22:27) — the master who girds himself and serves (12:37) `[T]`.
- **"You who have stood by me in my trials."** Ὑμεῖς δέ ἐστε οἱ διαμεμενηκότες μετ' ἐμοῦ ἐν τοῖς πειρασμοῖς μου (22:28) — πειρασμός ("trial, temptation"), the word of 4:13 `[T]`.
- **Sifted, turned, strengthened.** Σίμων Σίμων, ἰδοὺ ὁ Σατανᾶς ἐξῃτήσατο ὑμᾶς τοῦ σινιάσαι ὡς τὸν σῖτον ("Simon, Simon, behold, Satan has demanded permission to sift you like wheat", 22:31); ἐγὼ δὲ ἐδεήθην περὶ σοῦ … καὶ σύ ποτε ἐπιστρέψας στήρισον τοὺς ἀδελφούς σου ("but I have prayed for you … and you, when once you have turned again, strengthen your brothers", 22:32) `[T]`. στηρίζω ("to set firmly, strengthen") occurs three times in Luke: Jesus set (ἐστήρισεν) his face (9:51), the great chasm is fixed (16:26), and Peter is to strengthen his brothers (22:32) `[T]`, verified. "You" (ὑμᾶς, 22:31) is plural; "you" (σοῦ, 22:32) singular `[T]` — Satan's demand concerns all; Jesus' prayer concerns Peter, for their sake.
- **Numbered with the lawless.** τοῦτο τὸ γεγραμμένον δεῖ τελεσθῆναι ἐν ἐμοί, τό· Καὶ μετὰ ἀνόμων ἐλογίσθη ("this which is written must be fulfilled in me, 'And he was numbered with transgressors'", 22:37) — the only explicit Isa 53 quotation in Luke, and the last of the four τελέω (see pericope 20) `[T]`.

**Tool 11.**

**Exod 12; 24:8; Jer 31:31 (Swete 38:31) → 22:7–20** *(high)*. *Source context:* the Passover lamb slain and eaten in haste on the night of deliverance (Exod 12); the blood of the covenant thrown on the people at Sinai (Exod 24:8); the new covenant, not like the one made "when I took them by the hand to bring them out of the land of Egypt", in which the LORD will write his law on the heart and "remember their sin no more" (Jer 31:31–34). *Book usage:* Exodus is live from 2:23 (the firstborn) through 9:31 (the ἔξοδος) and 12:35 (girded loins, pericope 20); Jeremiah from 13:35 and 19:46. *OT-to-OT:* Jeremiah defines the new covenant against the exodus covenant — the same pairing Luke's meal makes. *What it adds:* the exodus named on the mountain (9:31) is accomplished at the exodus meal, and the covenant Jeremiah promised is made in Jesus' blood. The forgiveness of sins Jeremiah ended with is what the risen Jesus sends out to the nations (24:47).

**Isa 53:12 → 22:37** *(high — quoted, τὸ γεγραμμένον ("that which is written"))*. *Source context:* the Servant, who bore the sin of many and made intercession for the transgressors, is allotted a portion with the strong "because he poured out his soul to death and was numbered with the transgressors". *Book usage:* the Servant thread runs from 2:32 (light to the nations) through 3:22 and 9:35 (the voice); the stronger man's spoils (11:22) came from this verse; the fulfilment is narrated at 23:32–33 (two criminals) and 23:47 (δίκαιος ("righteous"), Isa 53:11). *OT-to-OT:* Isa 53:12's "poured out his soul" and "intercession" have their echoes in 22:20 (ἐκχυννόμενον ("poured out")) and 23:34 ("Father, forgive them") `[I]`, moderate. *Triage (category 3 — the NT's own text):* Luke's μετὰ ἀνόμων ("with the lawless") stands closer to the Hebrew, וְאֶת־פֹּשְׁעִים נִמְנָה ("and with transgressors he was numbered", WLC, verified: פֶּשַׁע, 6586; מָנָה, 4487), than to Swete's ἐν τοῖς ἀνόμοις ("among the lawless") `[T]`. Peter's Pentecost sermon names the executioners διὰ χειρὸς ἀνόμων ("by the hands of lawless men", Acts 2:23) `[T]`. *What it adds:* the only formula quotation of Isa 53 in the Gospel explains why the Lord who serves must die among criminals — and the book adds it on the night of the covenant meal, not on the cross.

**Dan 7:9–10; Ps 122:5 (Swete 121:5) → 22:30** *(moderate)*. Move 1: thrones are set for judgement before the Ancient of Days (Dan 7:9); ἐκεῖ ἐκάθισαν θρόνοι εἰς κρίσιν, θρόνοι ἐπὶ οἶκον Δαυείδ ("there thrones were set for judgement, the thrones of the house of David", Ps 121:5 Swete) `[T]`. The Twelve share the Son's kingdom as judges of the twelve tribes — a restored Israel.

**Job 1:12; 2:6; Amos 9:9 → 22:31** *(moderate; uncertain)*. Move 1: Satan asks for permission to test Job and is given it, within limits (Job 1:12 Swete) `[T]`; the LORD sifts the house of Israel among the nations "as one sifts with a sieve" and "not a kernel shall fall" (Amos 9:9 Swete λικμήσω … λικμᾶται) `[T]`. There is no verbal link to either (Luke's σινιάζω ("to sift") is a NT hapax). The Joban pattern — Satan's demand, God's limit, the sufferer preserved — is the closer. *Moderate* for Job, *uncertain* for Amos.

*Internal:* **answers §4:13** — ἄχρι καιροῦ and πειρασμός (high). **Answers §9:31; 12:50** — the exodus and baptism accomplished (high). **Answers §2:7** — κατάλυμα (moderate). **Answers §9:16** — the four verbs (high). **Answers §11:50** — ἐκχέω (moderate–high). **Answers §12:37** — the serving master (high). **Answers §9:46–48** — who is greatest (high). **Answers §9:51** — στηρίζω (moderate). **Answers §18:31** — τελέω (high). **Plants §22:54–62** — the denial (high). **Plants §23:32–33** — the two criminals (high). **Plants §24:30, 35** — breaking bread (high). **Plants §24:34** — Simon's restoration: ὤφθη Σίμωνι ("he has appeared to Simon") (high).

**Translations and text.** 22:19b–20 (the second cup) is absent from Codex Bezae and a few Old Latin witnesses `[S]`; the SBLGNT prints it in single brackets, NA28 without brackets, and the Majority text has it `[T]` for the three editions. The NASB95 includes it. The *cup–bread–cup* order is Luke's under both texts. The covenant findings above depend on 22:20 and therefore hold under the Majority text.

**Pitfall.** Book-level trap 6, in reverse: reading Luke's supper only through Paul (1 Cor 11) or the church's liturgy, and missing the farewell discourse that follows it. Luke places the dispute about greatness *after* the cup (22:24). The corrective: preach the meal and the discourse together — the covenant is made with men who are arguing about rank, and the Lord answers by serving.

---

## 31. Luke 22:39–23:25 — Olivet, Denial, Trials: No Fault in Him

**Position.** Q1: 22:31–34 predicted Peter's denial and the Satanic sifting; 22:37 said Jesus must be numbered with the lawless. Q2: the prayer on the mountain, the arrest, the denial and the trials follow in order, because each prediction is now fulfilled — and at each stage Luke shows Jesus innocent and the Scripture being carried out.

**Structure.** The prayer on the Mount of Olives (22:39–46); the arrest (47–53); Peter's denial (54–62); the mocking (63–65); the council (66–71); before Pilate (23:1–5); before Herod (6–12); Pilate's verdict and the crowd's choice (13–25).

**Text-first findings.**

- **"As was his custom."** κατὰ τὸ ἔθος ("as was his custom", 22:39) — ἔθος ("custom") occurs three times in Luke: Zechariah's priestly custom (1:9), the family's Passover custom (2:42), and Jesus' custom of prayer on the mount (22:39) `[T]`, verified.
- **The cup and the will.** Πάτερ, εἰ βούλει παρένεγκε τοῦτο τὸ ποτήριον ἀπ' ἐμοῦ· πλὴν μὴ τὸ θέλημά μου ἀλλὰ τὸ σὸν γινέσθω ("Father, if you are willing, remove this cup from me; yet not my will, but yours be done", 22:42). θέλημα ("will") occurs three times in Luke: the servant who knew his master's will (12:47), the Father's will here, and Pilate's verdict, τὸν δὲ Ἰησοῦν παρέδωκεν τῷ θελήματι αὐτῶν ("but he delivered Jesus to their will", 23:25) `[T]`, verified. Jesus yields to the Father's will; Pilate hands him over to theirs.
- **The angel and the sweat.** 22:43–44 stands in NA28 in double brackets ⟦ ⟧; the SBLGNT prints it without brackets; the Majority text has it `[T]` for the three editions. Its content — ἄγγελος ἀπ' οὐρανοῦ ἐνισχύων αὐτόν ("an angel from heaven … strengthening him") and ἀγωνία ("agony"), a NT hapax — is not used for any finding in this sweep.
- **Kiss.** Ἰούδα, φιλήματι τὸν υἱὸν τοῦ ἀνθρώπου παραδίδως; ("Judas, are you betraying the Son of Man with a kiss?", 22:48). φίλημα ("kiss") occurs twice in Luke — Simon the Pharisee gave no kiss (7:45) and Judas does (22:48); καταφιλέω ("to kiss affectionately") three times — the sinful woman (7:38, 45) and the father (15:20) `[T]`, verified. The woman, the father and the betrayer: three kisses.
- **The healed ear.** ἁψάμενος τοῦ ὠτίου ἰάσατο αὐτόν ("he touched his ear and healed him", 22:51) `[T]` — Luke alone. The last healing in the Gospel is done for one of the arresting party.
- **As against a robber.** Ὡς ἐπὶ λῃστὴν ἐξήλθατε μετὰ μαχαιρῶν καὶ ξύλων; ("have you come out with swords and clubs as you would against a robber?", 22:52). λῃστής ("robber") occurs four times in Luke: the robbers on the Jericho road (10:30, 36), the robbers' den the temple had become (19:46), and here `[T]`, verified. The men who made the temple a den of robbers arrest Jesus as a robber.
- **The hour of darkness.** αὕτη ἐστὶν ὑμῶν ἡ ὥρα καὶ ἡ ἐξουσία τοῦ σκότους ("this hour and the power of darkness are yours", 22:53). σκότος ("darkness") occurs four times in Luke: the dawn shining on those in darkness (1:79), the light that is darkness (11:35), this hour, and the darkness over the land (23:44) `[T]`, verified. The devil claimed the ἐξουσία ("authority") of the kingdoms (4:6); here it is given, for an hour.
- **The look.** στραφεὶς ὁ κύριος ἐνέβλεψεν τῷ Πέτρῳ, καὶ ὑπεμνήσθη ὁ Πέτρος τοῦ λόγου τοῦ κυρίου ("the Lord turned and looked at Peter; and Peter remembered the word of the Lord", 22:61) `[T]`. The verb of remembering returns at the tomb, μνήσθητε ὡς ἐλάλησεν ὑμῖν ("remember how he spoke to you", 24:6) and ἐμνήσθησαν τῶν ῥημάτων αὐτοῦ ("they remembered his words", 24:8) `[T]`. μιμνῄσκομαι ("to remember") occurs six times in Luke: God remembering mercy and covenant (1:54, 72), Abraham's "remember" to the rich man (16:25), the criminal's "remember me" (23:42), and the women (24:6, 8) `[T]`, verified.
- **"Today."** Πρὶν ἀλέκτορα φωνῆσαι σήμερον ἀπαρνήσῃ με τρίς ("before a rooster crows today, you will deny me three times", 22:61; cf. 22:34) `[T]`. σήμερον ("today") occurs eleven times in Luke; the ninth and tenth are the day of the denial, and the eleventh is the day of paradise (23:43) `[T]`, verified.
- **"Prophesy!"** Προφήτευσον, τίς ἐστιν ὁ παίσας σε; ("prophesy, who is the one who hit you?", 22:64) `[T]`. The guards mock him as a false prophet three verses after his prophecy about Peter has come true (22:61). `[I]`, high.
- **Seated from now on.** ἀπὸ τοῦ νῦν δὲ ἔσται ὁ υἱὸς τοῦ ἀνθρώπου καθήμενος ἐκ δεξιῶν τῆς δυνάμεως τοῦ θεοῦ ("but from now on the Son of Man will be seated at the right hand of the power of God", 22:69) `[T]`. Mark 14:62 adds καὶ ἐρχόμενον μετὰ τῶν νεφελῶν τοῦ οὐρανοῦ ("and coming with the clouds of heaven") `[T]`, checked; Luke keeps the session and drops the coming, which his readers will see as the ascension (Acts 1:9–11) and the promise that follows it `[I]`, moderate–high.
- **"You say that I am."** Σὺ οὖν εἶ ὁ υἱὸς τοῦ θεοῦ; … Ὑμεῖς λέγετε ὅτι ἐγώ εἰμι ("are you the Son of God, then?" … "Yes, I am", 22:70) — the devil's εἰ υἱὸς εἶ τοῦ θεοῦ ("if you are the Son of God", 4:3, 9) turned into the council's question `[T]`. The NASB95's "Yes, I am" resolves an ambiguous Greek idiom; Ὑμεῖς λέγετε ὅτι ἐγώ εἰμι reads literally "you say that I am".
- **"Perverting the nation."** Τοῦτον εὕραμεν διαστρέφοντα τὸ ἔθνος ἡμῶν ("we found this man misleading our nation", 23:2). διαστρέφω occurs twice in Luke — Jesus' lament Ὦ γενεὰ ἄπιστος καὶ διεστραμμένη ("you unbelieving and perverted generation", 9:41) and this charge `[T]`, verified. The accusers use the word Jesus used of them.
- **Three verdicts of innocence.** Οὐδὲν εὑρίσκω αἴτιον ἐν τῷ ἀνθρώπῳ τούτῳ ("I find no guilt in this man", 23:4); οὐθὲν εὗρον … αἴτιον (23:14); οὐδὲν αἴτιον θανάτου εὗρον ἐν αὐτῷ ("I have found in him no guilt demanding death", 23:22), and the narrator says the third was spoken τρίτον ("a third time") `[T]`. αἴτιος ("guilt, cause") occurs in Luke only in these three verses `[T]`, verified. Three denials by Peter; three declarations of innocence by Pilate.
- **"Beginning from Galilee."** ἀρξάμενος ἀπὸ τῆς Γαλιλαίας ἕως ὧδε ("starting from Galilee even as far as this place", 23:5) — the accusers' summary of the ministry; the risen Jesus' commission, ἀρξάμενοι ἀπὸ Ἰερουσαλήμ ("beginning from Jerusalem", 24:47) `[T]`. *Moderate.*
- **Silence.** αὐτὸς δὲ οὐδὲν ἀπεκρίνατο αὐτῷ ("but he answered him nothing", 23:9) — Herod had long wished to see him and hoped for a sign (23:8), and the sign-seeking generation was promised none but Jonah's (11:29) `[T]`. The Servant οὐκ ἀνοίγει τὸ στόμα ("does not open his mouth", Isa 53:7 Swete) `[T]` — *moderate*.
- **Friends that day.** ἐγένοντο δὲ φίλοι ὅ τε Ἡρῴδης καὶ ὁ Πιλᾶτος ἐν αὐτῇ τῇ ἡμέρᾳ ("now Herod and Pilate became friends with one another that very day", 23:12) `[T]`. In Acts the church prays Ps 2:1–2 — "the kings of the earth took their stand, and the rulers were gathered together against the Lord and against his Christ" — and names Ἡρῴδης τε καὶ Πόντιος Πιλᾶτος ("both Herod and Pontius Pilate", Acts 4:26–27) `[T]`, verified. Luke's second volume supplies the psalm his first volume enacts. *Internal to Luke–Acts*, high.
- **The murderer released.** ἀπέλυσεν δὲ τὸν διὰ στάσιν καὶ φόνον βεβλημένον εἰς φυλακήν ("and he released the man they were asking for who had been thrown into prison for insurrection and murder", 23:25) — and in Acts, ᾐτήσασθε ἄνδρα φονέα χαρισθῆναι ὑμῖν ("you asked for a murderer to be granted to you", Acts 3:14) `[T]`.

**Tool 11.**

**Isa 51:17, 22; Ps 75:8 (Swete 74:9) → 22:42** *(moderate)*. Move 1: Jerusalem has drunk from the LORD's hand τὸ ποτήριον τοῦ θυμοῦ αὐτοῦ ("the cup of his wrath", Isa 51:17 Swete), and the LORD takes it from her hand (51:22) `[T]`; the cup in the LORD's hand that the wicked must drain (Ps 74:9 Swete) `[T]`. *Book usage:* ποτήριον ("cup") has four verses in Luke — the outside of the cup (11:39), the two Passover cups (22:17, 20) and this one `[T]`, verified. *What it adds:* the cup the Son asks to be spared is the cup of judgement the prophets said the LORD would take from Jerusalem. `[I]`, moderate.

**Ps 110:1 (Swete 109:1) and Dan 7:13 → 22:69** *(high; moderate–high)*. *Source context:* see pericopes 28 and 29. *Book usage:* the riddle of 20:41–44 answered. *What it adds:* at his trial, Jesus claims to be David's Lord at God's right hand — and "from now on", while he stands condemned.

**Ps 2:1–2 → 23:12 (via Acts 4:25–27)** *(high as Luke–Acts reading; moderate within the Gospel)*. The Gospel does not quote the psalm; the Acts prayer applies it by name. A sweep reading Luke alone would rate it moderate; reading the two volumes together, high.

*Internal:* **answers §22:31–34** — the denial (high). **Answers §4:3, 9** — "the Son of God" (high). **Answers §4:6** — ἐξουσία (moderate–high). **Answers §7:38, 45; 15:20** — the kisses (moderate). **Answers §9:41** — διαστρέφω (moderate–high). **Answers §19:46** — λῃστής (moderate–high). **Answers §20:25** — the Caesar charge false (high). **Answers §20:41–44** — David's Lord (high). **Answers §11:29** — no sign (moderate). **Answers §19:14; plants §23:18** — "away with this man" (high). **Plants §24:6, 8** — remembering (high). **Plants §23:43** — σήμερον (high). **Plants Acts 3:14; 4:25–27** (high).

**Pitfall.** Treating the trials as a record of Jewish guilt. Luke has Pilate, Herod, the chief priests, the rulers and "the people" all acting (23:13), and Acts gathers them all under Ps 2 — "Herod and Pontius Pilate, with the Gentiles and the peoples of Israel" (Acts 4:27). The corrective: preach the trial as the world against the Lord's Christ, with the Gentile governor three times declaring him innocent.

---

## 32. Luke 23:26–49 — Father, Forgive; Father, into Your Hands ⭐

**Position.** Q1: every passion prediction (9:22, 44; 17:25; 18:31–33; 22:37) has pointed here, and 23:25 has handed Jesus over "to their will". Q2: the crucifixion follows as the fulfilment of what was written — told through the words spoken to and by Jesus, and ending with the verdict of the Gentile centurion.

**Structure.** Simon of Cyrene (26); the daughters of Jerusalem (27–31); the crucifixion between criminals and the first word (32–34); the threefold mockery (35–39); the penitent criminal (40–43); darkness, the curtain, the last word (44–46); the witnesses: centurion, crowds, acquaintances and women (47–49).

**Text-first findings.**

- **Behind Jesus.** ἐπέθηκαν αὐτῷ τὸν σταυρὸν φέρειν ὄπισθεν τοῦ Ἰησοῦ ("they placed on him the cross to carry behind Jesus", 23:26) — the disciple's cross, carried ὀπίσω μου ("after me", 9:23; 14:27) `[T]`. Simon does what the disciples were told to do.
- **Blessed the barren.** Μακάριαι αἱ στεῖραι καὶ αἱ κοιλίαι αἳ οὐκ ἐγέννησαν ("blessed are the barren, and the wombs that never bore", 23:29). στεῖρα ("barren") occurs three times in Luke: Elizabeth (1:7, 36) and here `[T]`, verified. The book opened with a barren woman given a child; on the way to the cross, barrenness is called blessed.
- **The first word.** Πάτερ, ἄφες αὐτοῖς, οὐ γὰρ οἴδασιν τί ποιοῦσιν ("Father, forgive them; for they do not know what they are doing", 23:34a) `[T]`. NA28 double-brackets it (⟦ ⟧); the SBLGNT prints it without brackets; the Majority text has it `[T]` for the three editions. Stephen prays Κύριε, μὴ στήσῃς αὐτοῖς ταύτην τὴν ἁμαρτίαν ("Lord, do not hold this sin against them", Acts 7:60), and Peter says κατὰ ἄγνοιαν ἐπράξατε ("you acted in ignorance", Acts 3:17) `[T]`. *Critical-text-dependent note:* findings that rest on 23:34a hold under the Majority text and the SBLGNT; NA28 marks it as not original.
- **Three mockeries, three conditions.** The rulers: εἰ οὗτός ἐστιν ὁ χριστὸς τοῦ θεοῦ, ὁ ἐκλεκτός ("if this is the Christ of God, his Chosen One", 23:35); the soldiers: Εἰ σὺ εἶ ὁ βασιλεὺς τῶν Ἰουδαίων, σῶσον σεαυτόν ("if you are the King of the Jews, save yourself", 23:37); the criminal: Οὐχὶ σὺ εἶ ὁ χριστός; σῶσον σεαυτὸν καὶ ἡμᾶς ("are you not the Christ? Save yourself and us!", 23:39) `[T]`. Three tests, as in the wilderness (4:3, 9 εἰ υἱὸς εἶ τοῦ θεοῦ ("if you are the Son of God")), and all three urge him to save himself. "The Christ of God" is Peter's confession word for word (9:20, τὸν χριστὸν τοῦ θεοῦ) `[T]`; ἐκλεκτός ("chosen") answers the voice at the transfiguration in the critical text (9:35, ἐκλελεγμένος) — the Majority text reads ἀγαπητός ("beloved") there, so that link fails under the Majority text `[T]`.
- **Sneering.** ἐξεμυκτήριζον ("they were sneering", 23:35) — the second of the two NT uses (16:14) and the verb of Ps 21:8 Swete `[T]`, verified.
- **Remember me.** Ἰησοῦ, μνήσθητί μου ὅταν ἔλθῃς εἰς τὴν βασιλείαν σου ("Jesus, remember me when you come in your kingdom", 23:42) — SBLGNT ἐν τῇ βασιλείᾳ σου ("in your kingdom"); the Majority text has the same preposition and adds κύριε ("Lord") `[T]`. The criminal asks what God did in the canticles (ἐμνήσθη ("he remembered"), 1:54, 72). Joseph's μνήσθητί μου ("remember me", Gen 40:14 Swete) is the same request of a prisoner to one about to be raised up `[T]` — *moderate*.
- **Today, paradise.** Ἀμήν σοι λέγω σήμερον μετ' ἐμοῦ ἔσῃ ἐν τῷ παραδείσῳ ("truly I say to you, today you shall be with me in Paradise", 23:43) — the last of Luke's eleven σήμερον, verified. παράδεισος ("paradise") is once in the Gospels `[T]`; in Swete it names the garden of Gen 2:8 `[T]` (verified in Task 1). The genealogy ended "son of Adam, son of God" (3:38); the Son of God promises the garden. *Uncertain* as design, per the overview.
- **Darkness and the sun.** σκότος ἐγένετο ἐφ' ὅλην τὴν γῆν … τοῦ ἡλίου ἐκλιπόντος ("darkness fell over the whole land … because the sun was obscured", 23:44–45) `[T]` in the SBLGNT; the Majority text reads καὶ ἐσκοτίσθη ὁ ἥλιος ("and the sun was darkened") `[T]` — the verb of Isa 13:10 Swete, σκοτισθήσεται τοῦ ἡλίου ("the sun will be darkened") `[T]`, verified. The Majority reading makes the echo of 21:25 ("signs in the sun") and Isa 13:10 verbal. *Majority-text-dependent*, moderate.
- **The curtain torn.** ἐσχίσθη δὲ τὸ καταπέτασμα τοῦ ναοῦ μέσον ("and the veil of the temple was torn in two", 23:45) — placed *before* the death in Luke (after it in Mark 15:38) `[T]` for Luke's order.
- **The last word.** φωνήσας φωνῇ μεγάλῃ ὁ Ἰησοῦς εἶπεν· Πάτερ, εἰς χεῖράς σου παρατίθεμαι τὸ πνεῦμά μου ("and Jesus, crying out with a loud voice, said, 'Father, into your hands I commit my spirit'", 23:46) `[T]`. Luke has no cry of dereliction (Mark 15:34, Ps 22:1) `[T]`, checked. The SBLGNT's present παρατίθεμαι ("I commit") differs from Swete Ps 30:6's future παραθήσομαι ("I will commit"), which the Majority text reads `[T]`. Jesus' first recorded words were about his Father's house, ἐν τοῖς τοῦ πατρός μου (2:49); his last words from the cross begin Πάτερ ("Father") `[T]`. Stephen dying: Κύριε Ἰησοῦ, δέξαι τὸ πνεῦμά μου ("Lord Jesus, receive my spirit", Acts 7:59) `[T]`.
- **"Certainly righteous."** Ὄντως ὁ ἄνθρωπος οὗτος δίκαιος ἦν ("certainly this man was innocent", 23:47). The NASB95's "innocent" hides δίκαιος ("righteous"), the word of Zechariah and Elizabeth (1:6), Simeon (2:25), and Joseph four verses later (23:50) `[T]`. The Servant is δίκαιον εὖ δουλεύοντα πολλοῖς ("the righteous one who serves many well", Isa 53:11 Swete), and Acts names Jesus τὸν ἅγιον καὶ δίκαιον ("the Holy and Righteous One", Acts 3:14) `[T]`. ὄντως ("certainly, truly") has two occurrences in Luke: the centurion here and the Eleven's ὄντως ἠγέρθη ὁ κύριος ("the Lord has really risen", 24:34) `[T]`, verified. One "truly" at the death, one at the resurrection.
- **Beating their breasts.** τύπτοντες τὰ στήθη ὑπέστρεφον ("they began to return, beating their breasts", 23:48). στῆθος ("breast") occurs twice in Luke: the tax collector who ἔτυπτε τὸ στῆθος αὐτοῦ ("was beating his breast", 18:13) and the crowds here `[T]`, verified. The crowds at the cross make the gesture of the man who went home justified.
- **At a distance.** εἱστήκεισαν δὲ πάντες οἱ γνωστοὶ αὐτῷ μακρόθεν ("and all his acquaintances … were standing at a distance", 23:49). μακρόθεν ("at a distance") occurs four times in Luke: the rich man seeing Abraham (16:23), the tax collector (18:13), Peter following (22:54), and here `[T]`, verified.

**Tool 11.**

**Ps 22:7, 18 (Swete 21:8, 19) → 23:34b–35** *(high; moderate–high)*. *Source context:* the psalm of the righteous sufferer, forsaken, mocked by all who see him ("he trusted in the LORD; let him deliver him", 22:8), his garments divided; it turns at v.21 to praise, and ends with the nations turning to the LORD and a people yet unborn told "that he has done it" (22:27–31). *Book usage:* ἐκμυκτηρίζω first at 16:14; the garments here in the psalm's own words, διαμεριζόμενοι … ἔβαλον κλήρους ("dividing … they cast lots") against Swete's διεμερίσαντο … ἔβαλον κλῆρον (21:19) `[T]`. *OT-to-OT:* Ps 22 and Ps 31 are both laments of the righteous sufferer that end in trust. *What it adds:* Luke draws on Ps 22 for the mockers' actions but not for Jesus' own words — he gives him Ps 31 instead.

**Ps 31:5 (Swete 30:6) → 23:46** *(high — quoted without formula)*. *Source context:* a psalm of refuge: "into your hand I commit my spirit; you have redeemed me, O LORD, faithful God" — ἐλυτρώσω με ("you have redeemed me", Swete) `[T]`. The psalmist is surrounded by enemies and scorned by acquaintances, who "flee from me" (31:11). *Book usage:* the passion Psalms (22, 31, 69, 38/88) in sequence. *OT-to-OT:* Ps 31:11's scorned acquaintances belong with Ps 38:11 and 88:8 behind 23:49. *What it adds:* the psalm's next line is "you have redeemed me". The Emmaus pair will say they had hoped he would redeem Israel (24:21); the psalm Jesus died praying answers them. `[I]`, moderate–high.

**Hos 10:8 → 23:30** *(high — quoted)*. *Source context:* the judgement on Samaria's altars: "they will say to the mountains, 'Cover us', and to the hills, 'Fall on us'" `[T]`. Luke reverses the order (τοῖς ὄρεσιν· Πέσετε ἐφ' ἡμᾶς, καὶ τοῖς βουνοῖς· Καλύψατε ἡμᾶς ("to the mountains, 'Fall on us', and to the hills, 'Cover us'")) against Swete's Καλύψατε … Πέσατε `[T]`. *What it adds:* the judgement once spoken over the northern kingdom's idolatry is spoken over Jerusalem.

**Ezek 20:47 (Swete) → 23:31** *(moderate)*. Move 1: the fire that will devour ξύλον χλωρὸν καὶ ξύλον ξηρόν ("every green tree and every dry tree") in the forest of the Negeb, followed a few verses later by "set your face towards Jerusalem" (Ezek 21:2 Swete) — the verse behind 9:51 `[T]`, verified. Luke's ἐν τῷ ὑγρῷ ξύλῳ … ἐν τῷ ξηρῷ ("when the tree is green … when it is dry") uses a different adjective for "green". *Moderate.*

**Ps 69:21 (Swete 68:22) → 23:36** *(moderate)*. ὄξος ("sour wine") offered in mockery; the psalm's ἐπότισάν με ὄξος ("they gave me sour wine to drink") `[T]`.

**Isa 53:12 → 23:32–33** *(high — fulfilment of 22:37)*. "Two others also, who were criminals" (23:32) — narrated five verses after the prediction of 22:37 had required it.

**Ps 38:11; 88:8 (Swete 37:12; 87:9) → 23:49** *(moderate)*. οἱ ἔγγιστά μου μακρόθεν ἔστησαν ("my nearest stood at a distance", Ps 37:12 Swete); ἐμάκρυνας τοὺς γνωστούς μου ("you have removed my acquaintances far from me", 87:9) `[T]`, verified. Luke's γνωστοί … μακρόθεν ("acquaintances … at a distance") combines the two.

*Internal:* **answers §9:20** — "the Christ of God" (high). **Answers §9:35** — ἐκλεκτός (critical text only; moderate). **Answers §4:3, 9** — three tests (moderate–high). **Answers §16:14** — sneering (high). **Answers §1:7, 36** — στεῖρα (moderate–high). **Answers §22:37** — the criminals (high). **Answers §2:49** — "Father" (moderate). **Answers §18:13** — breast and distance (moderate–high). **Answers §21:25** — the sun (Majority text; moderate). **Answers §3:38** — paradise (uncertain). **Plants §23:50** — δίκαιος (high). **Plants §24:21** — redemption (moderate). **Plants §24:34** — ὄντως (moderate). **Plants Acts 3:14; 7:59–60** (high).

**Translations.** 23:47: NASB95 "innocent" for δίκαιος ("righteous") breaks the chain of Luke's named righteous people — Zechariah and Elizabeth (1:6), Simeon (2:25), Joseph (23:50) — and the link to Isa 53:11. A preacher using an English text should say what the Greek says.

**Pitfall.** Preaching Luke's cross through Mark's (or a harmony's) "My God, why have you forsaken me?" Luke gives three words — forgiveness, paradise, trust — and no dereliction. The corrective: preach Luke's cross as Luke tells it: the righteous Servant who forgives, promises and commits himself to the Father, with a Gentile declaring him righteous and the crowds beating their breasts like the justified tax collector.

---

## 33. Luke 23:50–24:35 — The Tomb, the Women, and the Road to Emmaus ⭐

**Position.** Q1: 23:49 left the acquaintances and the women watching at a distance, and every prediction included "on the third day rise" (9:22; 18:33). Q2: the burial and the tomb follow on the same timetable — Friday, Sabbath, first day — and the Emmaus story answers the question the whole book has raised: why must the Christ suffer, and where is it written? The Standard unit (the tomb) and the ⭐ unit (Emmaus) are merged here because they are one day's narrative (24:1, 13, 33) `[T]`.

**Structure.** Joseph of Arimathea and the burial (23:50–56); the women at the empty tomb (24:1–12); two disciples on the road (13–27); recognition at the table (28–32); return to Jerusalem (33–35).

**Text-first findings.**

- **Righteous and waiting.** ἀνὴρ ἀγαθὸς καὶ δίκαιος … ὃς προσεδέχετο τὴν βασιλείαν τοῦ θεοῦ ("a good and righteous man … who was waiting for the kingdom of God", 23:50–51) — the words of Simeon, δίκαιος … προσδεχόμενος παράκλησιν τοῦ Ἰσραήλ ("righteous … looking for the consolation of Israel", 2:25) `[T]`. The righteous man who waited received the child in the temple; the righteous man who waits buries the body.
- **Not consenting to their counsel.** οὐκ ἦν συγκατατεθειμένος τῇ βουλῇ καὶ τῇ πράξει αὐτῶν ("he had not consented to their plan and action", 23:51). βουλή ("counsel, plan") occurs twice in Luke — the Pharisees and lawyers who ἠθέτησαν τὴν βουλὴν τοῦ θεοῦ ("rejected God's purpose", 7:30) and the council's βουλή here `[T]`, verified. In Acts, τῇ ὡρισμένῃ βουλῇ … τοῦ θεοῦ ("by the predetermined plan … of God", Acts 2:23) stands behind their plan `[T]`.
- **Resting according to the commandment.** τὸ μὲν σάββατον ἡσύχασαν κατὰ τὴν ἐντολήν ("and on the Sabbath they rested according to the commandment", 23:56) `[T]` — the law-keeping family of 2:22–39, where νόμος ("law") stands five times (2:22, 23, 24, 27, 39) at the end of the Gospel `[I]`, moderate.
- **Two men in dazzling clothes.** ἄνδρες δύο ἐπέστησαν αὐταῖς ἐν ἐσθῆτι ἀστραπτούσῃ ("two men suddenly stood near them in dazzling clothing", 24:4) `[T]`. ἄνδρες δύο ("two men") stood with Jesus in glory at the transfiguration (9:30), and ἄνδρες δύο stand by the disciples at the ascension (Acts 1:10) `[T]`. ἀστράπτω ("to flash") occurs twice in Luke: the Son of Man's day like lightning (17:24) and these clothes `[T]`, verified.
- **The living.** Τί ζητεῖτε τὸν ζῶντα μετὰ τῶν νεκρῶν; ("why do you seek the living one among the dead?", 24:5) — "all live to him" (20:38) `[T]`.
- **Remember.** μνήσθητε ὡς ἐλάλησεν ὑμῖν ἔτι ὢν ἐν τῇ Γαλιλαίᾳ, λέγων τὸν υἱὸν τοῦ ἀνθρώπου ὅτι δεῖ παραδοθῆναι … καὶ σταυρωθῆναι καὶ τῇ τρίτῃ ἡμέρᾳ ἀναστῆναι ("remember how he spoke to you while he was still in Galilee, saying that the Son of Man must be delivered … and be crucified, and the third day rise again", 24:6–7) `[T]`. The angels quote the passion prediction back to the women — the δεῖ of 9:22 — and the women "remembered his words" (24:8).
- **Nonsense.** ἐφάνησαν ἐνώπιον αὐτῶν ὡσεὶ λῆρος τὰ ῥήματα ταῦτα, καὶ ἠπίστουν αὐταῖς ("these words appeared to them as nonsense, and they would not believe them", 24:11) — λῆρος, a NT hapax `[T]`, verified. The first witnesses to the resurrection are women, and the apostles disbelieve them. Abraham's warning — "neither will they be persuaded if someone rises from the dead" (16:31) — is enacted among the apostles themselves `[I]`, high.
- **Eyes held, eyes opened.** οἱ δὲ ὀφθαλμοὶ αὐτῶν ἐκρατοῦντο τοῦ μὴ ἐπιγνῶναι αὐτόν ("but their eyes were prevented from recognising him", 24:16); αὐτῶν δὲ διηνοίχθησαν οἱ ὀφθαλμοὶ καὶ ἐπέγνωσαν αὐτόν ("then their eyes were opened and they recognised him", 24:31) `[T]`. The passives are divine `[I]`, high. διανοίγω ("to open") occurs four times in Luke: the firstborn who "opens the womb" (2:23), the eyes (24:31), the Scriptures (24:32), and the mind (24:45) `[T]`, verified. ἐπιγινώσκω ("to recognise, know fully") begins the book — ἵνα ἐπιγνῷς … τὴν ἀσφάλειαν ("so that you may know the exact truth", 1:4) — and brackets the Emmaus recognition (24:16, 31) `[T]`, verified.
- **"A prophet mighty in deed and word."** ἀνὴρ προφήτης δυνατὸς ἐν ἔργῳ καὶ λόγῳ ("a prophet mighty in deed and word", 24:19) — Stephen's description of Moses, δυνατὸς ἐν λόγοις καὶ ἔργοις αὐτοῦ ("a man of power in words and deeds", Acts 7:22) `[T]`, verified. The Emmaus pair describe Jesus as the prophet like Moses (Deut 18:15), and are right as far as they go.
- **"We were hoping."** ἡμεῖς δὲ ἠλπίζομεν ὅτι αὐτός ἐστιν ὁ μέλλων λυτροῦσθαι τὸν Ἰσραήλ ("but we were hoping that it was he who was going to redeem Israel", 24:21). λυτρόομαι ("to redeem") occurs once in Luke; it gathers the λύτρωσις ("redemption") of 1:68 and 2:38 and the ἀπολύτρωσις of 21:28 `[T]`, verified. Anna spoke of him to all who were waiting for the redemption of Jerusalem (2:38); the Emmaus pair's hope is Anna's, and they think it has failed.
- **Must, and beginning with Moses.** οὐχὶ ταῦτα ἔδει παθεῖν τὸν χριστὸν καὶ εἰσελθεῖν εἰς τὴν δόξαν αὐτοῦ; ("was it not necessary for the Christ to suffer these things and to enter into his glory?", 24:26); ἀρξάμενος ἀπὸ Μωϋσέως καὶ ἀπὸ πάντων τῶν προφητῶν διερμήνευσεν αὐτοῖς ἐν πάσαις ταῖς γραφαῖς τὰ περὶ ἑαυτοῦ ("then beginning with Moses and with all the prophets, he explained to them the things concerning himself in all the Scriptures", 24:27) `[T]` — "Moses and the prophets" of 16:29, 31.
- **The day declining; bread broken.** πρὸς ἑσπέραν ἐστὶν καὶ κέκλικεν ἤδη ἡ ἡμέρα ("it is getting toward evening, and the day is now nearly over", 24:29) — the feeding began ἡ δὲ ἡμέρα ἤρξατο κλίνειν ("now the day was ending", 9:12) `[T]`; κλίνω ("to decline") has four uses in Luke, two of them these `[T]`, verified. λαβὼν τὸν ἄρτον εὐλόγησεν καὶ κλάσας ἐπεδίδου αὐτοῖς ("he took the bread and blessed it, and breaking it, he began giving it to them", 24:30) — the four verbs of 9:16 and 22:19 `[T]`.
- **Hearts burning; Simon.** Οὐχὶ ἡ καρδία ἡμῶν καιομένη ἦν ἐν ἡμῖν … ὡς διήνοιγεν ἡμῖν τὰς γραφάς; ("were not our hearts burning within us … while he was explaining the Scriptures to us?", 24:32); ὄντως ἠγέρθη ὁ κύριος καὶ ὤφθη Σίμωνι ("the Lord has really risen and has appeared to Simon", 24:34) — the centurion's ὄντως ("certainly", 23:47) and the restoration promised to Simon (22:32) `[T]`.
- **Known in the breaking of bread.** ὡς ἐγνώσθη αὐτοῖς ἐν τῇ κλάσει τοῦ ἄρτου ("how he was recognised by them in the breaking of the bread", 24:35) — the church's practice in Acts 2:42, τῇ κλάσει τοῦ ἄρτου `[T]`, verified.

**Tool 11.**

**Gen 3:5, 7 → 24:31** *(moderate)*. *Source context:* the serpent promises that when they eat διανοιχθήσονται ὑμῶν οἱ ὀφθαλμοί ("your eyes will be opened", 3:5 Swete); they eat, and διηνοίχθησαν οἱ ὀφθαλμοὶ τῶν δύο ("the eyes of the two were opened", 3:7), and they know that they are naked `[T]`, verified. *Book usage:* the Adam thread — "son of Adam, son of God" (3:38), paradise (23:43) — both uncertain. *OT-to-OT:* none in this passage. *What it adds:* two people, a meal, and eyes opened to recognition — in Genesis to shame, at Emmaus to the risen Lord. Luke's διηνοίχθησαν οἱ ὀφθαλμοί ("their eyes were opened") is Swete's phrase exactly. *Moderate* — the phrase is exact, but it could be natural Greek; there is no second marker. Carried to Open Questions with the Adam thread.

**Deut 18:15 → 24:19, 27** *(moderate–high)*. Move 1: Προφήτην … ὡς ἐμὲ ἀναστήσει Κύριος ὁ θεός σου … αὐτοῦ ἀκούσεσθε ("the Lord your God will raise up for you a prophet like me … you shall listen to him", Swete) `[T]`. *Book usage:* αὐτοῦ ἀκούετε ("listen to him", 9:35) at the transfiguration; Acts 3:22 quotes the verse. The Emmaus pair's description (24:19) is the Mosaic prophet, and the explanation begins ἀπὸ Μωϋσέως ("with Moses", 24:27).

**"All the Scriptures" → 24:25–27** *(synthetic)*. No passage is named. The sweep's Move 2 has traced what Luke has shown to be written about the Christ's suffering: Isa 53:12 (22:37); Ps 118:22 (20:17); Ps 22, 31 and 69 (23:34–46); the Son of Man of Dan 7 (21:27; 22:69); the rejected prophet of the Deuteronomistic tradition (11:47–51; 13:33–34); the smitten shepherd is absent `[T]` for Luke. What the Emmaus explanation contains, the reader is left to reconstruct from the Gospel itself — which is the book's purpose statement (1:4) applied. `[I]`, moderate–high.

*Internal:* **answers §2:25, 38** — the righteous waiting man (high). **Answers §7:30** — βουλή (moderate). **Answers §9:22; 18:33** — the third day (high). **Answers §9:30; plants Acts 1:10** — two men (moderate–high). **Answers §20:38** — the living (moderate–high). **Answers §16:31** — unpersuaded (high). **Answers §22:61** — remembering (high). **Answers §1:68; 2:38; 21:28** — redemption (high). **Answers §9:12, 16; 22:19** — the meal (high). **Answers §1:4** — ἐπιγινώσκω (moderate). **Answers §22:32** — Simon (high). **Answers §18:34** — the hidden meaning opened (high). **Plants §24:45** — the mind opened (high). **Plants Acts 2:42** — breaking of bread (high).

**Text.** 24:12 (Peter at the tomb) is absent from Codex Bezae `[S]`; NA28 marks it in its apparatus, the SBLGNT and Majority text both print it `[T]`. 24:6a (οὐκ ἔστιν ὧδε, ἀλλὰ ἠγέρθη ("he is not here, but he has risen")) is in all three editions `[T]`. No finding above depends on either.

**Pitfall.** Preaching Emmaus as "Jesus walks with us in our disappointments" and stopping there. The pair's problem was not loneliness but misreading Scripture — "slow of heart to believe all that the prophets have spoken" (24:25) — and the cure was an exposition that began with Moses. The corrective: the risen Lord's first pastoral act is to open the Bible, and the recognition at the table follows the exposition, not the other way round.

---

## 34. Luke 24:36–53 — Witnesses, Waiting, Blessed ⭐

**Position.** Q1: the Emmaus pair have just told the Eleven "the things on the road" (24:35), and the book has promised the Spirit (3:16; 11:13; 12:12) and a mission to the nations (2:32; 3:6) without yet giving either. Q2: the book ends here because every thread it opened in chs. 1–2 now closes — the priest's unfinished blessing, the temple, great joy, understanding, redemption — and every thread that runs on into Acts is handed over: the promise of the Father, the witnesses, the nations.

**Structure.** The risen body (36–43); the Scriptures opened and the commission (44–49); the blessing and the parting at Bethany (50–53).

**Text-first findings.**

- **"It is I myself."** ἴδετε τὰς χεῖράς μου καὶ τοὺς πόδας μου ὅτι ἐγώ εἰμι αὐτός· ψηλαφήσατέ με καὶ ἴδετε, ὅτι πνεῦμα σάρκα καὶ ὀστέα οὐκ ἔχει ("see my hands and my feet, that it is I myself; touch me and see, for a spirit does not have flesh and bones", 24:39) `[T]`. ψηλαφάω ("to touch, handle") occurs once in Luke `[T]`, verified. He then eats fish before them (24:42–43).
- **Disbelieving for joy.** ἔτι δὲ ἀπιστούντων αὐτῶν ἀπὸ τῆς χαρᾶς ("while they still could not believe it because of their joy", 24:41). χαρά ("joy") occurs eight times in Luke; χαρὰν μεγάλην ("great joy") was the angel's gospel to the shepherds (2:10), and μετὰ χαρᾶς μεγάλης ("with great joy") is the disciples' return (24:52) `[T]`, verified. The "great joy" announced at the birth returns in the last verse but one.
- **The last δεῖ.** ὅτι δεῖ πληρωθῆναι πάντα τὰ γεγραμμένα ἐν τῷ νόμῳ Μωϋσέως καὶ προφήταις καὶ ψαλμοῖς περὶ ἐμοῦ ("that all things which are written about me in the Law of Moses and the Prophets and the Psalms must be fulfilled", 24:44) — the last of the 18 δεῖ verses (SBLGNT) `[T]`. The three-part naming of the Scriptures stands only here in the NT `[S]`, moderate–high.
- **The mind opened.** τότε διήνοιξεν αὐτῶν τὸν νοῦν τοῦ συνιέναι τὰς γραφάς ("then he opened their minds to understand the Scriptures", 24:45). συνίημι ("to understand") occurs four times in Luke: Mary and Joseph did not understand (2:50); to others the mysteries come in parables "so that … they may not understand" (8:10, Isa 6:9); the Twelve "understood none of these things" (18:34); and here their minds are opened to understand (24:45) `[T]`, verified. The blindness of 9:45 and 18:34 is healed not by more miracles but by the Scriptures opened.
- **"Thus it is written."** οὕτως γέγραπται παθεῖν τὸν χριστὸν καὶ ἀναστῆναι ἐκ νεκρῶν τῇ τρίτῃ ἡμέρᾳ, καὶ κηρυχθῆναι ἐπὶ τῷ ὀνόματι αὐτοῦ μετάνοιαν καὶ ἄφεσιν ἁμαρτιῶν εἰς πάντα τὰ ἔθνη— ἀρξάμενοι ἀπὸ Ἰερουσαλήμ ("thus it is written, that the Christ would suffer and rise again from the dead the third day, and that repentance for forgiveness of sins would be proclaimed in his name to all the nations, beginning from Jerusalem", 24:46–47) `[T]`. What is written includes the mission as well as the passion. μετάνοια … ἄφεσις ἁμαρτιῶν ("repentance … forgiveness of sins") is John's proclamation, βάπτισμα μετανοίας εἰς ἄφεσιν ἁμαρτιῶν ("a baptism of repentance for the forgiveness of sins", 3:3) `[T]`, and ἄφεσις ("release, forgiveness") the Nazareth programme (4:18) `[T]`. *Variant (category 2):* NA28 reads μετάνοιαν εἰς ἄφεσιν ("repentance for forgiveness"), which repeats John's phrase in 3:3 exactly; the SBLGNT and the Majority text read μετάνοιαν καὶ ἄφεσιν ("repentance and forgiveness") `[T]`, checked in all three. The NASB95's "repentance for forgiveness" follows the NA reading. Under the SBLGNT and Majority text the link to 3:3 is a shared pair of nouns; under NA28 it is a repeated phrase.
- **Witnesses.** ὑμεῖς ἐστε μάρτυρες τούτων ("you are witnesses of these things", 24:48) `[T]`. μάρτυς ("witness") occurs twice in Luke — the lawyers as "witnesses" who approve their fathers' killing of the prophets (11:48) and the apostles here `[T]`, verified. The Lord's word through Isaiah, γένεσθέ μοι μάρτυρες ("be my witnesses", Isa 43:10 Swete) `[T]`, and Acts 1:8, ἔσεσθέ μου μάρτυρες ("you shall be my witnesses") `[T]`.
- **From on high.** ἐγὼ ἐξαποστέλλω τὴν ἐπαγγελίαν τοῦ πατρός μου ἐφ' ὑμᾶς· ὑμεῖς δὲ καθίσατε ἐν τῇ πόλει ἕως οὗ ἐνδύσησθε ἐξ ὕψους δύναμιν ("I am sending forth the promise of my Father upon you; but you are to stay in the city until you are clothed with power from on high", 24:49). ὕψος ("height, on high") occurs twice in Luke: the dawn ἐξ ὕψους ("from on high", 1:78) and this power ἐξ ὕψους `[T]`, verified. Gabriel's δύναμις ὑψίστου ("the power of the Most High", 1:35) came on Mary; δύναμις ("power") from on high will clothe the disciples `[T]`. *Moderate–high.*
- **Led out, hands lifted, blessing.** Ἐξήγαγεν δὲ αὐτοὺς ἕως πρὸς Βηθανίαν, καὶ ἐπάρας τὰς χεῖρας αὐτοῦ εὐλόγησεν αὐτούς ("and he led them out as far as Bethany, and he lifted up his hands and blessed them", 24:50) `[T]`. ἐξάγω ("to lead out") occurs once in Luke `[T]`, verified — in Swete it is the verb of the exodus itself, ὅστις ἐξήγαγόν σε ἐκ γῆς Αἰγύπτου ("who brought you out of the land of Egypt", Exod 20:2) `[T]`. The exodus named at 9:31 ends with the Lord leading his people out. `[I]`, moderate.
- **The unfinished blessing given.** Zechariah came out of the sanctuary and could not speak to the people (1:21–22); the book ends with the risen Jesus lifting his hands and blessing (24:50–51), and the disciples ἦσαν διὰ παντὸς ἐν τῷ ἱερῷ εὐλογοῦντες τὸν θεόν ("were continually in the temple blessing God", 24:53) `[T]`. εὐλογέω ("to bless") occurs in 12 verses of Luke; the last three (24:50, 51, 53) are the book's close `[T]`, verified.
- **Parted.** διέστη ἀπ' αὐτῶν ("he parted from them", 24:51) — Elijah's chariot διέστειλεν ἀνὰ μέσον ἀμφοτέρων ("separated the two of them", 4 Kgdms 2:11 Swete) before ἀνελήμφθη Ἠλειού ("Elijah was taken up") `[T]`, verified. The journey that began with the days of ἀνάλημψις ("taking up", 9:51) ends with the taking up.
- **Worship.** καὶ αὐτοὶ προσκυνήσαντες αὐτόν ("and they, after worshipping him", 24:52). προσκυνέω ("to worship") occurs three times in Luke: the devil demands it (4:7), Jesus answers Κύριον τὸν θεόν σου προσκυνήσεις ("you shall worship the Lord your God", 4:8, Deut 6:13), and the disciples worship Jesus (24:52) `[T]`, verified. *Text-dependent:* the SBLGNT brackets προσκυνήσαντες αὐτόν and "and was carried up into heaven" (24:51); NA28 prints both with an apparatus sign; the Majority text has both `[T]`. The finding holds under the Majority text and NA28; it is marked as bracketed in the SBLGNT.

**Tool 11.**

**Lev 9:22 and Sir 50:20 → 24:50** *(moderate–high; moderate)*. *Source context:* at the inauguration of the tabernacle service, Aaron lifts his hand(s) towards the people and blesses them, then comes down from the offering (Lev 9:22), and the glory of the LORD appears to all the people (9:23); Ben Sira's Simon the high priest ἐπῆρεν χεῖρας αὐτοῦ ἐπὶ πᾶσαν ἐκκλησίαν ("lifted up his hands over the whole congregation") to give the blessing, at the close of the daily offering (Sir 50:20 Swete) `[T]`, verified. *Apparatus note (category 2):* the WLC of Lev 9:22 reads the consonants יָדוֹ ("his hand", ketiv) with the qere יָדָיו ("his hands") `[T]`, verified; Swete has τὰς χεῖρας ("the hands"). Luke's τὰς χεῖρας αὐτοῦ ("his hands") agrees with the qere and the Greek. *Book usage:* the priestly thread opened at 1:5–23 with Zechariah unable to bless (Lev 9:22 was not cited there, but the incense hour and the people waiting outside are its setting); it closes here. *OT-to-OT:* Num 6:22–27, the Aaronic blessing, belongs with Lev 9:22 `[I]`. *What it adds:* the book opens with a priest who cannot bless and closes with the risen Lord giving the priestly blessing. It is Luke's last picture of Jesus. *Synthetic, moderate–high.*

**Isa 49:6; 43:10 → 24:47–48** *(moderate–high)*. *Source context:* the Servant is to restore the tribes of Jacob — "too light a thing" — and be εἰς φῶς ἐθνῶν … ἕως ἐσχάτου τῆς γῆς ("a light to the nations … to the end of the earth", Isa 49:6 Swete); Israel is summoned as the LORD's witnesses against the idols (43:10) `[T]`. *Book usage:* Simeon's φῶς εἰς ἀποκάλυψιν ἐθνῶν ("a light of revelation to the Gentiles", 2:32); Paul quotes Isa 49:6 at Acts 13:47 `[T]`, verified; Acts 1:8's ἕως ἐσχάτου τῆς γῆς ("to the end of the earth") is Isa 49:6's phrase `[T]`. *What it adds:* the Servant's mission to the nations, sung by Simeon over the infant, is handed to the witnesses.

**Isa 32:15 → 24:49** *(moderate)*. Move 1: "until the Spirit is poured upon us from on high", Swete πνεῦμα ἀφ' ὑψηλοῦ ("a spirit from on high") `[T]`, after which the wilderness becomes a fruitful field. Luke's ἐξ ὕψους is not Swete's phrase.

*Internal:* **answers §1:21–22** — the blessing (high). **Answers §1:9; 2:22–38** — the temple (high). **Answers §2:10** — great joy (high). **Answers §2:50; 8:10; 18:34** — understanding (high). **Answers §1:35, 78** — power from on high (moderate–high). **Answers §3:3; 4:18** — ἄφεσις (high). **Answers §2:32** — the nations (high). **Answers §4:7–8** — worship (moderate–high; text-dependent). **Answers §9:31, 51** — the exodus and the taking up (moderate–high). **Answers §11:13** — the Spirit promised (high). **Answers §1:2** — the eyewitnesses become the witnesses (high). **Plants Acts 1:4–11; 2:1–4** — the promise, the cloud, Pentecost (high).

**Text.** 24:36 SBLGNT lacks καὶ λέγει αὐτοῖς· Εἰρήνη ὑμῖν ("and he said to them, 'Peace be to you'"); NA28 prints it with an apparatus sign; the Majority text has it `[T]`. 24:53 SBLGNT εὐλογοῦντες ("blessing"); the Majority text αἰνοῦντες καὶ εὐλογοῦντες ("praising and blessing") `[T]`. Neither affects a finding.

**Pitfall.** Book-level trap 6. The end is not an ending. The Spirit is promised and not yet given; the disciples are told to wait in the city. The corrective: preach 24:36–53 as a handover — the blessing given, the witnesses appointed, the promise pending — and let the congregation hear that the story continues in Acts, and in them.

---

## Cross-Passage Convergent Findings

What only becomes visible when the pericopes are read as a sequence. **Every item here is synthetic.** Those marked *verified* have had every constituent reference checked by lemma against the SBLGNT index (or, for the OT side, against Swete and the WLC); the rest are capped at moderate confidence and are the first targets for a claim audit.

**1. The necessity and the blindness — δεῖ in 18 verses; συνίημι, κρύπτω and παρακαλύπτομαι; opened at 24:45.** *Verified.* δεῖ ("it is necessary") runs from the boy in his Father's house (2:49) to the risen Lord's last word (24:44), and fastens on the passion at 9:22; 13:33; 17:25; 22:37; 24:7, 26. Beside it runs a chain of incomprehension: Mary and Joseph οὐ συνῆκαν ("did not understand", 2:50); the passion saying ἦν παρακεκαλυμμένον ("was concealed", 9:45); οὐδὲν τούτων συνῆκαν … κεκρυμμένον ("they understood none of these things … hidden", 18:34); peace ἐκρύβη ("was hidden") from the city (19:42); eyes ἐκρατοῦντο ("were prevented", 24:16). It is broken only when he διήνοιξεν αὐτῶν τὸν νοῦν τοῦ συνιέναι τὰς γραφάς ("opened their minds to understand the Scriptures", 24:45). **What the sequence shows:** the necessity is scriptural, and so is the cure. Neither miracle nor resurrection appearance opens the disciples' understanding; the opened Scriptures do (16:31 → 24:25–27, 44–47).

**2. The temple bookends and the priestly blessing — 1:8–22 → 24:50–53, with Lev 9:22.** *Verified.* A priest in the sanctuary cannot bless the waiting people (1:21–22); the risen Jesus ἐπάρας τὰς χεῖρας αὐτοῦ εὐλόγησεν αὐτούς ("lifted up his hands and blessed them", 24:50), in Aaron's gesture (Lev 9:22 Swete ἐξάρας … τὰς χεῖρας … εὐλόγησεν αὐτούς); the disciples are "continually in the temple blessing God" (24:53). Around the frame: χαρὰ μεγάλη ("great joy", 2:10 → 24:52); the righteous man waiting (Simeon, 2:25 → Joseph, 23:50–51); ἐπιγινώσκω ("to know fully", 1:4 → 24:16, 31); διανοίγω ("to open", 2:23 → 24:31, 32, 45); Zechariah's unbelief (1:20 → 24:11, 41). **What the sequence shows:** the book ends by doing what it opened by promising. The overview's echo table has the frame; the sweep adds the joy, the opening, and the knowing.

**3. The visitation, missed and avenged — 1:68, 78; 7:16 → 19:44 → 21:22, with Jer 6:15 and Hos 9:7.** *Verified for the Greek chain; moderate for the Hosea link.* God has "visited" (ἐπεσκέψατο, 1:68); "God has visited his people" (7:16); the city "did not know the time of your visitation" (ἐπισκοπή, 19:44) — Jeremiah's ἐν καιρῷ ἐπισκοπῆς ("in the time of visitation", Jer 6:15 Swete), in an oracle of false peace and siege; and "these are days of vengeance" (21:22) — Hosea's ἡμέραι τῆς ἐκδικήσεως, which translate the Hebrew יְמֵי הַפְּקֻדָּה ("days of visitation"). The same noun ἐκδίκησις names God's vindication of his chosen (18:7–8). **What the sequence shows:** the one visitation brings salvation to those who receive it and judgement to the city that does not recognise it — and Luke's Greek Old Testament had already put "visitation" and "vengeance" in one verse.

**4. The cross uses the book's own vocabulary — 23:26–49.** *Verified.* Simon carries the cross ὄπισθεν τοῦ Ἰησοῦ ("behind Jesus", 23:26; cf. 9:23; 14:27). The rulers ἐξεμυκτήριζον ("sneered", 23:35), the verb of the money-loving Pharisees (16:14), the only other NT use. They call him "the Christ of God" — Peter's confession (9:20). Three mockeries, each urging him to save himself, answer the three tests in the wilderness (4:3, 9). The eleventh σήμερον ("today") is paradise (23:43). The centurion calls him δίκαιος ("righteous", 23:47; Isa 53:11), and his ὄντως ("truly") is answered by the Eleven's ὄντως (24:34). The crowds go home τύπτοντες τὰ στήθη ("beating their breasts", 23:48) like the tax collector who ἔτυπτε τὸ στῆθος αὐτοῦ (18:13), and the acquaintances stand μακρόθεν ("at a distance", 23:49) where he stood (18:13). **What the sequence shows:** Luke tells the crucifixion in words his readers have already learned — the vocabulary of the disciple's cross, the scoffers, the confession, the temptation, and the sinner who went home justified.

**5. The covenant meal — διαθήκη and διατίθεμαι (22:20, 29); ἐκχέω (11:50 → 22:20).** *Verified.* The cup is ἡ καινὴ διαθήκη ("the new covenant", 22:20); nine verses later the kingdom is given with the cognate verb, διατίθεμαι ὑμῖν, καθὼς διέθετό μοι ὁ πατήρ μου βασιλείαν ("I covenant to you, as my Father covenanted to me, a kingdom", 22:29). Both Old Testament texts behind the cup join the same verb and noun: ἧς διέθετο Κύριος (Exod 24:8 Swete) and διαθήσομαι … διαθήκην καινήν (Jer 38:31 Swete). And the blood "poured out" (ἐκχυννόμενον) for the disciples uses the verb of "the blood of all the prophets, poured out" (τὸ ἐκκεχυμένον, 11:50). **What the sequence shows:** the apostles' kingdom is a covenant grant made at the covenant meal; and the blood that "this generation" must answer for and the blood shed "for you" are placed in one line of thought.

**6. Elijah and Elisha, enacted without citation — 4:25–27 · 7:11–17 · 8:55 · 9:51–62 · 17:11–19 · 24:51.** *Verified for each wording.* Named once, at Nazareth (the widow of Zarephath; Naaman). Then enacted: the widow's only son given back ἔδωκεν αὐτὸν τῇ μητρὶ αὐτοῦ ("he gave him back to his mother", 7:15; 1 Kgs 17:23); the returning spirit, ἐπέστρεψεν τὸ πνεῦμα αὐτῆς ("her spirit returned", 8:55), where Elijah prays for the child's soul to return (1 Kgs 17:21); the days of ἀνάλημψις (9:51; 4 Kgdms 2:9–11); Elijah's fire refused (9:54); Elisha's farewell refused (9:61–62); Gehazi's no-greeting (10:4; 4 Kgdms 4:29); a Samaritan leper who returns like Naaman (17:15–18; 2 Kgs 5:15); διέστη ("he parted", 24:51) as the chariot διέστειλεν ("parted", 4 Kgdms 2:11). **What the sequence shows:** the cycle runs from the first sermon to the last verse, always as pattern and never as formula, and Luke both claims it and corrects it — gentler than Elijah's fire, more urgent than his call, and taken up as he was.

**7. Psalm 107 — 1:53 · 1:79 · 8:24 · 13:29.** *Moderate–high.* The hungry filled (107:9), those in darkness and the shadow of death (107:10), the storm stilled (107:29), the redeemed gathered from east and west (107:3). **What the sequence shows:** Luke uses one psalm of the regathered exiles for the Magnificat, the Benedictus, the stilling of the storm and the kingdom banquet. **A claim audit should test whether 107:20 — ἀπέστειλεν τὸν λόγον αὐτοῦ καὶ ἰάσατο αὐτούς ("he sent his word and healed them", Swete 106:20) — stands behind the centurion's εἰπὲ λόγῳ, καὶ ἰαθήτω ὁ παῖς μου ("just say the word, and my servant will be healed", 7:7).**

**8. The Malachi sequence — 1:17 · 1:76 · 1:78 · 7:27 · 9:52 · 10:1 · 19:45.** *Verified for each wording; moderate for 9:52, 10:1 and 19:45.* Malachi's last chapter (Hebrew 3) supplies Elijah turning the hearts (1:17), the messenger (1:76), the rising sun (1:78) and the explicit citation (7:27); the messenger formula is extended to the disciples (9:52; 10:1); and the Lord comes to his temple (19:45; Mal 3:1). **What the sequence shows:** Luke opens where the Prophets close, and the Lord whose way was prepared arrives at the temple.

**9. The three compassions, the three only children, the three kisses.** *Verified.* σπλαγχνίζομαι ("to be moved with compassion"): the Lord at Nain (7:13), the Samaritan (10:33), the father (15:20), grounded in σπλάγχνα ἐλέους θεοῦ ("the tender mercy of our God", 1:78). μονογενής ("only"): three only children restored (7:12; 8:42; 9:38). καταφιλέω/φίλημα ("kiss"): the sinful woman (7:38, 45), the father (15:20), the betrayer (22:48). **What the sequence shows:** Luke's recurring triads cluster around restoration, and the one intimate gesture that is not restorative is Judas'.

**10. The scoffers and the rejected — ἐκμυκτηρίζω 16:14 → 23:35; ἀποδοκιμάζω 9:22 → 17:25 → 20:17; "we do not want this man to reign" 19:14 → 20:14 → 23:18.** *Verified.* The rejection named in the passion predictions comes from Ps 118:22, and the text is quoted at 20:17; the citizens' refusal in the parable (19:14) becomes the tenants' "let us kill him" (20:14; Gen 37:20) and the crowd's "away with this man" (23:18). **What the sequence shows:** Luke builds the rejection in three steps — prediction, parable, event — and ties each to a named Scripture.

**11. Remembering — μιμνῄσκομαι 1:54, 72 → 16:25 → 23:42 → 24:6, 8; ὑπομιμνῄσκω 22:61.** *Verified.* God remembers his mercy and covenant (1:54, 72); Abraham tells the rich man to remember (16:25); the criminal asks Jesus to remember him (23:42); Peter remembers the word of the Lord (22:61); the women are told to remember, and do (24:6, 8). **What the sequence shows:** the verb moves from God to the dying man's prayer to the disciples' recovery of Jesus' words. *Moderate* as design; the distribution is certain.

**12. Hearing the word and bearing fruit ἐν ὑπομονῇ — 8:15 → 21:19; 8:21; 10:39; 11:28.** *Verified.* The good soil bears fruit ἐν ὑπομονῇ ("with perseverance", 8:15); the disciples gain their lives ἐν τῇ ὑπομονῇ ("by your endurance", 21:19) — ὑπομονή's only two Lukan uses. Between them: "my mother and my brothers are those who hear the word of God and do it" (8:21); Mary seated, hearing his word (10:39); "blessed rather are those who hear the word of God and observe it" (11:28). And the thorns of 8:14 (μέριμνα, βίος) are the weights of 21:34. **What the sequence shows:** the parable of the sower is the book's charter for discipleship to the end.

***

## Book-Overview Tensions

Surfaced, not resolved. The overview was drafted in this session and is marked Draft v0.1.0; these are the points a Finalise pass should work through first.

**1. The ἐγένετο count is 27, not 26.** The overview says 26 verses begin with (Καὶ) ἐγένετο. With the SBLGNT's sigla stripped, the count is 27 (Mark 2, Matthew 5, Acts 10) `[T]`, verified; the overview's search missed a verse where a siglum stands before the word. Correct the figure and add the sigla trap to its colophon.

**2. The Malachi sequence should be named as a sequence.** The overview lists Mal 3:1 (at 1:76; 7:27; 9:52; 10:1) and Mal 3:23–24 (at 1:17) as separate rows and ranks "Malachi 3 (4–5)". The sweep finds seven Lukan locations and a sequence: Malachi's last chapter worked through in Luke's first (1:17, 76, 78) and completed at the temple (19:45). Recommend one row for the sequence and an upgrade in the live-source ranking.

**3. The covenant pairing at 22:20, 29 is missing.** The overview has Exod 24:8 and Jer 31:31 at 22:20 but does not notice διατίθεμαι ("to covenant, appoint", 22:29) or that both source texts join it to διαθήκη ("covenant"). This is a sweep finding and should enter the overview's Christological trajectory (the Twelve's kingdom as a covenant grant) once audited.

**4. Isa 53:12 at 22:37 needs a triage note.** Luke's μετὰ ἀνόμων ("with the lawless") agrees with the Hebrew's וְאֶת־פֹּשְׁעִים ("and with transgressors") against Swete's ἐν τοῖς ἀνόμοις ("among the lawless") — category 3, the NT's own text. The overview's row treats the quotation as LXX-standard.

**5. The Christological "pattern" leans on two passages NA28 double-brackets.** The overview lists Jesus at prayer at 22:41–44 and forgiving enemies at 23:34 as a pattern for disciples. 22:43–44 and 23:34a both stand in ⟦ ⟧ in NA28; the SBLGNT prints both unbracketed and the Majority text has both `[T]`. Under the user's declared priority (the Majority text) the pattern stands; the overview should say which text it rests on and cite 22:41 (unaffected) as its anchor.

**6. The 9:35 ↔ 23:35 ἐκλεκτός echo fails under the Majority text.** Already flagged in the overview's text table; the sweep confirms that the Servant link at 23:35 must rest on Isa 42:1 alone, not on an internal echo, when the Majority text is followed.

**7. Luke's omission of "for all the nations" (19:46) is shared with Matthew.** The overview's row says "Luke omits"; Mark 11:17 keeps the phrase and Matt 21:13 lacks it `[T]`, verified. The inference about the temple and the nations can stand, but not as a Lukan distinctive against both other Synoptists.

**8. Add-rows for the intertextual map.** Sources the sweep found live and the overview lacks, each verified in Swete or the WLC: Gen 25:22 (1:41); 2 Sam 6 (1:39–56); Gen 37:11 and Dan 7:28 Theodotion (2:19, 51); Jer 1:1 (3:2); Prov 3:4 Hebrew (2:52); Isa 52:9 Hebrew (2:38); Deut 32:5, 20 (9:41); 2 Kgs 4:42–44 (9:10–17); Isa 65:4 (8:27–32); 1 Kgs 17:21 (8:55); ζωγρέω with Josh 6:25 (5:10); 2 Kgs 4:29 (10:4); 2 Chr 28:15 (10:30–35); Sir 11:19 (12:19–20); Exod 12:11 (12:35); Prov 25:6–7 (14:8–10); Deut 20:5–7 (14:18–20); Gen 33:4 (15:20); Ps 119:176 (15:4–6); Exod 22:1 and 2 Sam 12:6 Hebrew (19:8); Ps 79:9 (18:13); 1 Kgs 1:33–38 and 2 Kgs 9:13 (19:30–36); Isa 29:3, Ps 137:9 and Hos 14:1 (19:43–44); Mal 3:1 (19:45); Gen 37:20 (20:14); Exod 4:12 (21:15); Dan 2:28 Theodotion (21:9); Isa 24:17 (21:35); Isa 51:17, 22 (22:42); Ps 2:1–2 via Acts 4:25–27 (23:12); Ezek 20:47 (23:31); Gen 40:14 (23:42); Gen 3:5, 7 (24:31); Isa 43:10 (24:48); Exod 20:2, ἐξάγω (24:50). None is a formula citation; the confidence of each is given at its pericope.

**9. Two overview rows should be weakened.** Isa 32:15 at 24:49: the idea matches but Luke's ἐξ ὕψους ("from on high") is not Swete's ἀφ' ὑψηλοῦ — keep at moderate, and note that Luke's own phrase answers 1:78. Job 1:12 at 22:31: there is no verbal contact; the pattern is Joban, the wording is not.

**10. One overview row should be strengthened.** 2 Kgs 2:9–11 at 9:51 and 24:51: the verbal contacts are stronger than the overview says — ἀναλαμβάνω (Swete 4 Kgdms 2:9, 10; Acts 1:2, 11, 22) and διέστειλεν ‖ διέστη. Upgrade from moderate–high to high.

**11. The Majority text supplies two echoes the critical text lacks.** At 23:45 the Majority text's ἐσκοτίσθη ὁ ἥλιος ("the sun was darkened") is Isa 13:10's verb, which the SBLGNT's τοῦ ἡλίου ἐκλιπόντος is not; at 23:46 the Majority text's παραθήσομαι ("I will commit") is Swete Ps 30:6's tense, against the SBLGNT's παρατίθεμαι. The overview's text section lists the variants but not what they do to the intertextual map. Given the user's stated priority, both should be noted there.

**12. The presenting situation holds.** Every pericope's Q2 answer is compatible with the overview's reconstruction (certainty under the strain of a crucified Messiah refused by Jerusalem's rulers). The sweep found no passage that contradicts it and several that sharpen it: 16:31 and 24:11, 41 (unbelief even after resurrection), 19:42 and 23:28–31 (grief, not triumph, over the city), 24:45 (certainty given through Scripture). It remains `[I]`.

***

## Preaching Pitfalls (book level)

Passage-level pitfalls are given at each pericope. These four operate across the whole book.

### Pitfall: preaching Luke as ethics

- **What it looks like:** "be a Good Samaritan", "come home like the prodigal", "give like Zacchaeus", "pray like Jesus", "be generous like the widow".
- **Why it is wrong:** in each case Luke sets the divine act first. The compassion verb belongs first to the Lord at Nain and to the God of 1:78; the parables of ch. 15 are told to grumblers about God's joy; Zacchaeus is sought before he gives (19:5, 10); the widow stands between the scribes who devour her and the temple that will fall.
- **The corrective:** ask of every Lukan scene *who visits whom?* before asking *what should I do?*

### Pitfall: the poor without the release, and the release without the poor

- **What it looks like:** on one side, a social programme drawn from 4:18 and 6:20; on the other, a spiritualised "poor in spirit" that removes the widows, beggars and crippled from the text.
- **Why it is wrong:** ἄφεσις ("release, forgiveness") governs the Nazareth reading (4:18, twice), John's baptism (3:3) and the final commission (24:47); and the poor, crippled, lame and blind are named twice in four verses (14:13, 21), and Lazarus has a name.
- **The corrective:** preach the release and the poor together, as the Nazareth reading does.

### Pitfall: Jerusalem as villain

- **What it looks like:** "the Jews rejected Jesus, so God rejected them."
- **Why it is wrong:** Jesus weeps over the city (19:41) and laments with longing (13:34); "all the people" hang on his words (19:48) and beat their breasts at the cross (23:48); the trial gathers Herod, Pilate, the Gentiles and the peoples (Acts 4:27); the trampling has a limit (21:24); and the mission begins "from Jerusalem" (24:47).
- **The corrective:** preach the grief before the judgement, and the city as the place where forgiveness is first proclaimed.

### Pitfall: Luke without Acts, or Acts read back into Luke

- **What it looks like:** a Gospel that ends at the ascension as a finale; or Pentecost preached in Luke 24.
- **Why it is wrong:** the Spirit is promised and withheld (3:16; 11:13; 12:12; 24:49); the witnesses are appointed but not yet sent; the last verse is a waiting community in the temple.
- **The corrective:** preach the ending as a handover.

***

## Open Questions / Uncertainties

1. **Seventy or seventy-two (10:1, 17).** SBLGNT and NA28 72; the Majority text and NASB95 70. Both have OT models (Gen 10; Num 11:24–26). **Check the NA28 apparatus and Metzger** before preaching the number.
2. **9:35 ἐκλελεγμένος / ἀγαπητός.** The critical text's reading supports an echo at 23:35; the Majority text's does not. **Check the NA28 apparatus** for the witnesses.
3. **22:43–44 and 23:34a.** Double-bracketed in NA28, unbracketed in the SBLGNT, present in the Majority text. **Check the apparatus and Metzger.** No sweep finding depends on 22:43–44; the 23:34a findings are marked text-dependent.
4. **22:19b–20; 24:12; 24:36b; 24:51b; 24:52a** — the "Western non-interpolations". The sweep's covenant finding (22:20, 29) and worship finding (24:52 ← 4:7–8) depend on the longer text, which the Majority text and NA28 both print. **Check the NA28 apparatus** before building a sermon point on the worship inclusio.
5. **24:47 μετάνοιαν εἰς/καὶ ἄφεσιν.** NA28 εἰς (repeating 3:3); SBLGNT and Majority καί. Small, but it decides whether 24:47 quotes John's formula or pairs its nouns.
6. **2:33, 43 and 4:44** (Joseph named or not; Judea or Galilee) — carried from the overview; not affected by any sweep finding. **Check the apparatus.**
7. **The 2 Sam 6 ark pattern at 1:39–56** — attractive, three verbal contacts, contested in the literature `[S]`. **Ask Logos** whether it is argued from the Greek.
8. **Jer 6 behind 19:42–44** — the phrase ἐν καιρῷ ἐπισκοπῆς is exact; whether the Jeremianic context of false peace and siege is being invoked is the sweep's most attractive untested claim in chs. 19–21.
9. **Gen 3:7 at 24:31 and the Adam thread (3:38; 23:43).** Three uncertain links; together they would form a pattern that crosses the ≥3 gate. **Do not enter them in the overview without an audit.**
10. **21:24 "until the times of the Gentiles are fulfilled"** and **21:32 "this generation"** — named, not resolved.
11. **Ps 107:20 behind 7:7** — a candidate fifth use of the psalm (Convergent Finding 7). Untested.
12. **Is ἐκδίκησις at 18:7–8 and 21:22 a designed pair?** Two senses (vindication, vengeance) of one noun; the distribution is certain, the design is not.

***

## Text-First Declaration

**Mode:** Multi-Passage Sweep, 34 pericopes, merged from the overview's 60 preaching units at the Greek seams (17:1–18:34, 22:39–23:25 and 23:50–24:35 are merged units; the ⭐ units are kept whole).

**Primary texts actually opened:** SBLGNT `greek-nt-sblgnt/03-Luke.txt` — **all 1,149 verses read in Greek before any English was consulted**; its MorphGNT lemma index `_index/03-Luke.tsv` for every count and chain; the SBLGNT NT files for Synoptic and Acts comparisons (Mark 11:10, 17; 13:3, 14, 26; 14:62; 15:34, 38; Matt 7:11; 21:9, 13; John 12:13; Acts 1:2–11, 22; 2:17–42; 3:14, 17; 4:25–27; 7:22, 59–60; 13:47); Robinson–Pierpont 2018 `_texts/source/byzantine-rp2018/03-Luke-RP2018.csv`, collated in full and consulted verse by verse at every text-dependent finding; NA28 `logos-exports/02-New-Testament/03-Luke-NA28.txt` for the double brackets and apparatus signs at 22:19–20, 43–44; 23:34; 24:6, 12, 36, 47, 51, 52; Swete `greek-lxx-swete/` for every Greek OT wording quoted (Genesis, Exodus, Leviticus, Deuteronomy, 1–4 Kingdoms, 2 Chronicles, Psalms, Proverbs, Job, Sirach, Isaiah, Jeremiah, Ezekiel, Daniel Theodotion, Hosea, Amos, Micah, Habakkuk, Zechariah, Malachi, 4 Maccabees); WLC `hebrew-wlc/` via `tools/find.py` for 2 Chr 24:22 (דָּרַשׁ, 1875), 2 Sam 12:6, Isa 53:12 (פֶּשַׁע, 6586; מָנָה, 4487), Lev 9:22 (ketiv), and the Hebrew checks carried from chs. 1–9; NASB95 export for Tool 8.

**Editions named:** every Greek NT count is stated against the **SBLGNT**; every Greek OT wording against **Swete**; every Hebrew against the **WLC**. **Rahlfs-Hanhart was not opened**; any finding that comes to turn on a Rahlfs reading must be re-checked in Logos before it is cited. NA28 was consulted only where brackets or apparatus signs are load-bearing; its apparatus witnesses were **not** read, and every "check the apparatus" item in Open Questions is outstanding.

**Majority text:** collated throughout, per the user's instruction that the dig depend first on the Majority text. Findings that fail or change under it are marked in place: 9:35 → 23:35 (fails); 23:45 and 23:46 (the Majority text adds an echo); 24:47 (NA28 alone repeats 3:3); 24:51–52 (bracketed only in the SBLGNT).

**Secondary sources present in context:** the Draft overview (this session, same model — see the independence caveat at the head of the report) and the prior dig on 19:11–27 (12 July 2026, pre-corpus). The dig was read only after pericope 26 was drafted; its three confirmed verdicts are tagged `[S: dig]` where used. No commentary or monograph was opened.

**Tools worked before secondary sources consulted:** Confirmed for every pericope. The overview's threads were held in peripheral vision (Phase 0.5); its specific claims were checked only after each pericope's Greek work, and every claim tested appears in *Book-Overview Tensions*.

**Passage text:** Verified. Every Greek quotation is copied from the corpus files, not reconstructed. Every English quotation of Luke is the NASB95 as exported.

**Reference files viewed:** core tool files 01–07; extensions `preacher-extras`, `historical-background`, `original-audience`, `original-languages`, `textual-variants`, `biblical-theology`, `difficult-verses`, `christological-reading`; worked example `romans-8-31to39-worked.md` from `_skill-examples/` as the calibration anchor; `_texts/README.md`; the Acts sweep as the format model. **Not viewed:** `schnittjer-pass.md` (N/A — not Torah); `claim-audit-format.md` and `macro-synthesis-format.md` (N/A — neither mode is active).

**Depth floors:** Sweep mode, so solo floors do not apply. Each pericope carries the Positional Necessity Check, a structure note, text-first findings with warrants, Tool 11 with the Citation Triad on every direct quotation and high-confidence allusion and an explicit Move 4, and a pitfall; Translations, Difficulty and Text notes where live. Headline Findings: 5. Cross-passage findings: 12. Book-level pitfalls: 4. Open questions: 12.

**Chains verified:** **more than 150 lemma chains in Luke checked against the SBLGNT index**, among them δεῖ (by parse code), σήμερον, ἐπισκέπτομαι/ἐπισκοπή, ἄφεσις, σπλαγχνίζομαι, μονογενής, ἔλεος, ἐλεάω, εὐφραίνω, διασκορπίζω, ἐκμυκτηρίζω, ἀποδοκιμάζω, ἀρνέομαι/ἀπαρνέομαι, τελέω, τελειόω, δικαιόω, δίκαιος, ἐκδίκησις, ἐκλεκτός, ἀγαπητός, κρύπτω, συνίημι, διανοίγω, ἐπιγινώσκω, μιμνῄσκομαι, κλάω/κατακλάω/κλάσις, ἐκχέω, διαθήκη/διατίθεμαι, στηρίζω, κατάλυμα, θέλημα, σκότος, ποτήριον, λῃστής, φίλημα/καταφιλέω, στεῖρα, στῆθος, μακρόθεν, ὄντως, χαρά, ὕψος, προσκυνέω, εὐλογέω, λύτρωσις/ἀπολύτρωσις/λυτρόομαι, ὑπομονή, βαρέω, μέριμνα, χήρα, βίος, βουλή, πρόσωπον, and the NT hapaxes ἀνάλημψις, ἀλλογενής, ἀνάπηρος, ἐκμυκτηρίζω (with 23:35), χάραξ, ἐδαφίζω, καταλιθάζω, ἰσάγγελος, ὀρθρίζω, σινιάζω, λῆρος, ἐκκρέμαμαι. **No chain in this report is tagged unverified.** Where a claim failed a check it was corrected in place, not hedged (18:18 is not word for word with 10:25; 10:29 is the third δικαιόω, not the fourth; the SBLGNT spells ἀναπείρους; 24:47 reads καί in the SBLGNT).

**Positive controls that failed (and were caught):** (a) **SBLGNT sigla inside words** broke surface regex until stripped — see *What the corpus showed at the outset*. (b) **MorphGNT lemma forms** returned silent zeros under the expected dictionary form: σωτήριον → σωτήριος; εὐαγγελίζομαι → εὐαγγελίζω; ἱερόν → ἱερός; λυτρόω → λυτρόομαι; ἐλεέω → ἐλεάω; παρακαλύπτω → παρακαλύπτομαι; ἀνάπειρος → ἀνάπηρος; διατίθημι → διατίθεμαι; ἐκχύννω → ἐκχέω; ἐκκρεμάννυμι → (nothing; confirmed by surface search); and δεῖ is filed under δέω, separated by parse code. (c) **Swete file-naming:** a book-prefix search for "4Kgdms" matched nothing because the files are named "Reigns" (refs 1Ki/2Ki for 3–4 Kingdoms); re-run with the right prefix. (d) **`find.py verify` argument order:** a first run with the reference before the lemma reported FAIL for a verse that contains the lemma; re-run as `verify LEMMA Book:c:v`, it passed. Each of these would have produced a false negative had it not been checked against a verse known to contain the word.

**Three-way triage applied** at five Hebrew/Greek divergences: Mal 3:1 at 7:27 (category 3 — the NT follows Exod 23:20); 2 Chr 24:22 at 11:50–51 (category 1/3 — ἐκζητέω answers דָּרַשׁ, Swete's κρινάτω does not); 2 Sam 12:6 at 19:8 (category 1/2 — Hebrew fourfold, Swete sevenfold); Isa 53:12 at 22:37 (category 3 — μετὰ ἀνόμων with the Hebrew); Hos 9:7 at 21:22 (category 1 — "visitation" rendered "vengeance"). Plus the Lev 9:22 ketiv (category 2, apparatus). None is reported as a translation-tradition split, and none is resolved by preferring one text by default.

**Tool 8 divergence check ran.** Findings a preacher using the NASB95 should notice: 9:51 "was determined" hides the set face (and Ezek 21:2); 22:29 "grant" hides the covenant verb; 23:47 "innocent" hides δίκαιος; 24:47 "for forgiveness" follows NA against the SBLGNT and the Majority text.

**Synthetic-claim discipline:** all twelve Cross-Passage Convergent Findings are marked synthetic. Nine are marked *verified* in their Greek constituents; three (Ps 107; Malachi at 9:52, 10:1, 19:45; remembering as design) are capped at moderate. **No cross-passage claim from this sweep should enter the book overview until it has been audited.**

**Warrant counts** (tag occurrences across the whole report, the legend in *How to Read* included): `[T]` 475 · `[I]` 59 · `[S]` 24 (three of them `[S: dig]`, from the prior 19:11–27 run; the rest general-literature items — the manuscript history of the Western readings, the Lazarus/Eleazar etymology, the ἀλλογενής temple inscription, the seventy-nations tradition, the 2 Sam 6 debate — none load-bearing).

*Health note:* this report could **not** have been written by someone who read the overview without opening the Greek. Of the twelve cross-passage findings, six are absent from the overview (the blindness chain, the cross's reuse of the book's vocabulary, the covenant pairing, remembering, the triads beyond σπλαγχνίζομαι, ὑπομονή); the visitation–vengeance link through Hos 9:7 was already in the overview's map and is here confirmed, and the Tensions section corrects the overview at four points. The weakness is the one the independence caveat names: the overview and the sweep share an author, and a claim audit by a separate run is the proper next step.
