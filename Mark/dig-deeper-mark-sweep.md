# Dig Deeper: Mark — Whole-Book Sweep

**Mode:** Multi-Passage Sweep — 37 pericopes, Mark 1:1–16:8 with a note on [16:9–20], following the book overview's 37 preaching units exactly
**Primary text (observation):** SBLGNT with the MorphGNT word index, `_texts/greek-nt-sblgnt/02-Mark.txt` and `_index/02-Mark.tsv` — 661 verses in 1:1–16:8, read in Greek before any English
**Citation of record:** NA28 text and apparatus, `_texts/logos-exports/02-New-Testament/02-Mark-NA28.txt` and `02-Mark-NA28-apparatus.txt`
**Greek OT:** Swete, `_texts/greek-lxx-swete/` (observation); Rahlfs–Hanhart text exports in `_texts/logos-exports/` where a Greek OT reading carries weight. **There is no Rahlfs apparatus in the folder**, so no finding here rests on an LXX variant
**Hebrew OT:** WLC, `_texts/hebrew-wlc/`, checked with `tools/find.py`; BHS text and apparatus exports where a reading is cited
**Study text:** NASB95, `_texts/logos-exports/02-New-Testament/02-Mark-NASB95.txt`
**Pulpit text:** ESV — Crossway's 2025 US text (`02-Mark-ESV.txt`), declared for the series. Not the ESV Anglicised
**Book-overview context:** `Mark/book-overview-mark.md`, Draft v0.1.0 (29 September 2026)
**Date:** 29 September 2026
**Post-audit note:** 21 of this sweep's Old Testament allusion claims were tested by independent auditors in `Mark/dig-deeper-mark-claim-audit.md` (29 September 2026). Where they differ, **the audit supersedes this report**: Hosea 9 (11:12–21), Isa 63:11–14 (1:10) and Amos 2:16 (14:52) do not stand as proposed, and Headline Finding 4, Convergent Findings 4, 8, 9 and 12, and Tensions 1–6 and 9 are revised there. The 74 lexical chains are unaffected.

---

## How to Read This Sweep

This is planning material, not pulpit preparation. Thirty-seven pericopes at proportional depth cannot each receive what a solo run gives one passage, and checking is the first thing proportional depth cuts. Four consequences govern everything below.

**Every cross-passage claim is synthetic and capped at moderate confidence** until a claim audit has tested it — except where the report says a chain has been verified by lemma against the SBLGNT index. The verified ones say so; treat the rest as candidates.

**For any ⭐ pericope, run a full solo dig before the pulpit.** Sweep depth is enough to plan a series and to audit an overview. It is not enough to preach from.

**Each pericope is worked in the same order**: its position in the book (the two Phase 0.6 questions), its structure, the text-first findings, the Old Testament citations with the Citation Triad on every direct quotation and high-confidence allusion, the internal echoes (Move 4), and whichever of the remaining tools the passage makes live — Translations, a difficulty, a pitfall. Tools that add nothing at sweep depth are not listed pericope by pericope; the book-level Tools 12 (Genre) and 14 (Bible Timeline) are stated once below and hold throughout unless a pericope says otherwise.

**Warrant tags.** `[T]` derivable from the text on the page · `[I]` a reasonable inference from it · `[S]` supplied by a secondary source and held provisionally. Counts name their edition, because a count belongs to a text, not to a book. Greek and Hebrew stand in their own script with the English in brackets after them, every time.

**One independence caveat, stated plainly.** The overview this sweep consumes was drafted in this same session, earlier today, by the same model. A sweep that re-reads its own overview can only agree with it unless it deliberately works from the Greek first. Every pericope below was re-read in the SBLGNT before the overview's claims about it were consulted, and every overview claim the sweep tested is reported in *Book-Overview Tensions* whether it held or not. But the reader should weigh the confirmations accordingly: an overview confirmed by its own author is a weaker thing than an overview confirmed by an independent run.

**What the corpus showed at the outset.** SBLGNT Mark has 661 verses in 1:1–16:8. **The index files the shorter ending under 16:8 and the longer ending under 16:9–20**, so every count below was made after both were removed; a count that forgets this gains εὐαγγέλιον ("gospel"), πιστεύω ("to believe"), σημεῖον ("sign") and a dozen other words. **Surface searches are accent-sensitive.** A first search for παρὰ τὴν ὁδόν ("beside the road") returned 4:4 and 10:46 and missed 4:15, where the accent is grave (ὁδὸν); the positive control caught it, and every surface search in this report was re-run with accents stripped and final ς normalised to σ. Lemma searches are unaffected, but MorphGNT files several words under forms the searcher would not guess (δεῖ under δέω; ἱερόν under ἱερός; Χριστός with a capital). In the Hebrew, ketiv forms stand unpointed in the WLC (Jer 16:16 לדוגים; Hos 9:16 בלי), and they are quoted unpointed here.

---

## Headline Findings

Five book-level findings that emerged from several tools converging, each verified against the corpus rather than recalled.

**1. The passion night is told on the watches of Mark 13, and the call of the first disciples is undone point by point.** The master may come "in the evening, at midnight, at cockcrow, or at dawn" (13:35), and the night of the passion runs through exactly those watches: ὀψίας γενομένης ("when evening came", 14:17), Gethsemane and the arrest, ἀλέκτωρ ἐφώνησεν ("a cock crowed", 14:68, 72), πρωΐ ("at dawn", 15:1). γρηγορέω ("to watch") stands only at 13:34, 35, 37 and 14:34, 37, 38. Inside that frame the call is reversed: the first four ἀφέντες ("leaving") their nets followed him (1:18, 20), and ἀφέντες αὐτόν ("leaving him") they all fled (14:50); the first ἄγωμεν ("let us go") was to preach elsewhere (1:38), and the last is to meet the betrayer (14:42); and Jesus calls Peter "Simon" once after renaming him — at 14:37, asleep. *Verified; synthetic, high for the chains.*

**2. What was plotted at the end of the first cycle is carried out in the passion.** The plot of 3:6 is a συμβούλιον ("council, plot"), and so is the morning council of 15:1 — the word's only two uses. They watched him in the synagogue ἵνα κατηγορήσωσιν αὐτοῦ ("so that they might accuse him", 3:2), and before Pilate κατηγόρουν αὐτοῦ ("they were accusing him", 15:3–4) — again the only uses. The one who blasphemes the Spirit is ἔνοχος ("guilty", 3:29); the court finds Jesus ἔνοχος θανάτου ("guilty of death", 14:64). And the death of John rehearses it all in advance: an oath (ὀμνύω, 6:23 → 14:71), a ruler περίλυπος ("very sorrowful", 6:26 → 14:34), an "opportune" day (εὔκαιρος, 6:21 → εὐκαίρως, 14:11), a king (5 times of Herod in ch. 6; 6 times of Jesus in ch. 15), a corpse and a tomb. *Verified; the design is moderate–high.*

**3. The feedings are Supper-shaped, and the bread runs only through the middle of the book.** Taking, blessing or giving thanks, breaking and giving stand at 6:41, 8:6 and 14:22–23; εὐχαριστέω ("to give thanks") occurs only at 8:6 and 14:23. ἄρτος ("bread, loaf") stands in 19 verses, 16 of them between 6:8 and 8:19. The shepherd who feeds the sheep without a shepherd (6:34) is the shepherd struck and the sheep scattered (14:27) — ποιμήν ("shepherd") and πρόβατον ("sheep") only at those two places. The disciples' failure in the boat is a failure to understand "about the loaves" (6:52; 8:14–21). *Verified; synthetic, high.*

**4. Mark's Scriptures come as chapters, not proof-texts, and several come through the Hebrew.** One chapter of Hosea supplies the fig, the expulsion "from my house", the roots dried up and the end of fruit (Hos 9:10, 15, 16 behind 11:12–21). Isaiah's prayer to "tear the heavens and come down" (Isa 63:19 Heb) comes with the Spirit and the one "brought up out of the sea" four verses before it (63:11, 14). Daniel's abomination (Dan 11:31) is followed, in Mark as in Daniel, by the tribulation "such as has not been" (Dan 12:1 → 13:19). And the passion is told in Ps 22 — whose last movement, the nations turning to worship, is enacted two verses after the cry by a Gentile centurion's confession. To the overview's six Hebrew-side contacts the sweep adds a seventh: γυμνὸς ἔφυγεν ("naked, he fled", 14:52) is Amos 2:16's Hebrew עָרוֹם יָנוּס ("naked he will flee"), against the Greek's "the naked one will pursue". *Verified in Swete, Rahlfs and the WLC; the reading of each as a whole-chapter allusion is moderate to moderate–high.*

**5. The ending is a promise the reader has twice seen kept.** "As he said" — καθὼς εἶπεν — stands at 11:6 (the colt found), 14:16 (the room found) and 16:7 ("there you will see him, as he told you"). The first two are fulfilled on the page; the third is left to the reader. The women's silence reverses the leper's command (μηδενὶ μηδέν, 1:44 → οὐδενὶ οὐδέν, 16:8); their τρόμος ("trembling") and ἔκστασις ("astonishment") are the words of the healed woman (5:33) and the raised girl (5:42); and their fear (φοβέομαι, "to fear") is the disciples' at the sea (4:41). The longer ending, by contrast, uses a dozen words found nowhere in 1:1–16:8 and calls Jesus ὁ κύριος ("the Lord") in the narrator's voice, which Mark never does. *Verified; the reading of 16:8 is `[I]`.*

---

## Book-Overview Active Layer (Phase 0.5)

The four threads were extracted from the Draft overview before any pericope was worked, and held in peripheral vision.

| Thread | What is live across the book |
|---|---|
| **Christological trajectory** | The Son in the place of YHWH (the way of the Lord, 1:2–3; "God alone" forgives, 2:7; the sea, 4:39; 6:48–50; David's Lord, 12:35–37; the right hand, 14:62). The necessary sufferer (δεῖ, 8:31; the ransom, 10:45; the covenant blood, 14:24; the cup, 14:36; the cry, 15:34). The pattern of discipleship, grounded each time in a passion prediction that comes first. Son of God declared by God (1:11; 9:7), cried by demons (3:11; 5:7), and confessed by one human being, the centurion (15:39) |
| **Intertextual map** | Live sources: **Isaiah** (≈14 places), the **Psalms** (2, 22, 110, 118), **Daniel** (2, 7, 9–12), **Zechariah** (9, 13, 14, 2), **Malachi and the Elijah texts**, **Exodus** and **Deuteronomy**. Two concentrations: the prologue and the passion. The Galilee chapters are carried more by internal repetition than citation. **For Move 2, read Swete, Rahlfs and the WLC**, because Mark several times stands nearer the Hebrew |
| **Preaching traps** | (1) the messianic secret as technique; (2) disciples as simple models or simple failures; (3) miracles as proofs or as promises of the same; (4) Mark 13 as a timetable; (5) the cry of dereliction explained away or left without the narrative's answer; (6) the ending ignored or overcorrected |
| **Presenting situation** | A Greek-reading, largely Gentile audience (ten Aramaic glosses; Jewish practice explained; Latin loanwords), under persecution, holding together two scandals — a crucified Messiah and failing disciples. `[I]` — a reconstruction from the book's own features, not a text statement |

---

## Book-Level Positional Frame (Phase 0.6)

**What the preceding movement set up.** For a Gospel the preceding movement is the canon it presupposes. Mark's first sentence after the heading is καθὼς γέγραπται ("as it is written", 1:2) `[T]`, and γέγραπται ("it is written") stands seven times (1:2; 7:6; 9:12, 13; 11:17; 14:21, 27) `[T]`. The Scriptures have promised a way prepared for the Lord (Isa 40:3), a messenger before him (Mal 3:1; Exod 23:20), Elijah's return (Mal 3:23), and the Lord's coming to his temple (Mal 3:1). The book presents itself as the ἀρχή ("beginning") of the good news about that coming (1:1) `[T]`.

**Why the book exists here.** Because the one declared "my beloved Son" (1:11) was rejected, handed over and crucified, and his closest followers deserted him (14:50) `[T]`. The book's answer is its δεῖ ("must", 8:31; 9:11; 13:7, 10, 14; 14:31) and its γέγραπται, together with the ransom saying (10:45) and the message to "his disciples and Peter" (16:7) `[T]`. The sweep adds one strand to the overview's account: the book's repeated fulfilment of Jesus' own words within the narrative (11:6; 14:16; 14:30 → 72), which grounds the last promise (16:7) that the narrative does not fulfil `[I]`, high.

**Implication for every pericope.** Each passage is read for what it contributes to the question "who is this?" (1:27; 2:7; 4:41; 6:2–3; 8:27–29; 14:61; 15:39) and to the necessity of the cross. Where a pericope seems self-contained — a healing, a controversy, a parable — the positional question asks what it plants for the passion.

**Book-level Genre (Tool 12).** Narrative — an εὐαγγέλιον ("good news", 1:1). It is episodic, paratactic (καί, "and", and εὐθύς, "immediately", 41 times as an adverb in the SBLGNT) and fast in Galilee, and slow in Jerusalem, with parables (4:1–34; 12:1–12), controversy stories (2:1–3:6; 11:27–12:37), one long discourse (13:5–37) and six intercalations (3:20–35; 5:21–43; 6:7–30; 11:12–25; 14:1–11; 14:53–72). Reading rules: it happened, it is theologically shaped, and the narrator's comments are authoritative (Tool 6) — notably 7:19c, 11:13 and 13:14. Parables carry one main thrust. Chapter 13 is prophetic-apocalyptic vision-language set inside a historical prediction.

**Book-level Bible Timeline (Tool 14).** The events stand at the hinge of the timeline: the Prophets' promises of the way, the messenger and Elijah are fulfilled (1:2–8; 9:13); the Son of Man is crucified and raised. The Spirit-baptism promised at 1:8 is not narrated, and the gospel's going to all nations is foretold (13:10; 14:9) but not narrated. The reader stands on the far side of the resurrection and before the Son of Man's coming (13:26; 14:62), in the time of watching (13:37). This holds for every pericope, and is not repeated below.

---

## 1. Mark 1:1–13 — The Beginning of the Gospel ⭐

**Position.** *Q1:* nothing precedes this unit except the canon, and the book says so in its second clause. καθὼς γέγραπται ("as it is written", 1:2) hangs from the verbless heading, so the "beginning of the gospel" is defined as the fulfilment of something already written `[T]`. *Q2:* the prologue stands first because it tells the reader what no character in the story will know until 8:29, and what no human voice will say until 15:39: that Jesus is the Son on whom the Spirit rests and to whom the heavens have been opened `[T]`/`[I]`. Everything from 1:14 to 8:26 is read by someone who has already heard the Voice, and the disciples have not heard it. That imbalance is how the first half of the book works.

**Structure.**

| Verses | Section | Function |
|---|---|---|
| 1:1 | Heading | Ἀρχὴ τοῦ εὐαγγελίου ("the beginning of the gospel"): verbless, and governing everything that follows |
| 1:2–3 | Scripture | The messenger and the voice: the way of the Lord is to be prepared |
| 1:4–8 | The forerunner | John appears in the wilderness; all Judaea goes out; the Stronger One is announced |
| 1:9–11 | The Son | Jesus comes; the heavens are torn; the Spirit descends; the Voice speaks |
| 1:12–13 | The wilderness | The Spirit drives him out; forty days; Satan, the wild beasts, the angels |

**Device.** ἔρημος ("wilderness") stands at 1:3, 4, 12 and 13, four times in thirteen verses (SBLGNT). It occurs in nine verses in all of Mark, and five of the other six are withdrawals to "a desolate place" (1:35, 45; 6:31, 32, 35) `[T]`. The prologue is a wilderness frame: the voice in the wilderness, the forerunner in the wilderness, and the Son driven into it. The verbs of coming are chained together. ἔρχεται ὁ ἰσχυρότερός μου ("the one stronger than I is coming", 1:7) is followed by ἦλθεν Ἰησοῦς ("Jesus came", 1:9), and the promise is met two verses later `[T]`.

**Text-first findings.**

- **"Your" face, and "his" paths.** In Exod 23:20, the text 1:2 reproduces word for word, πρὸ προσώπου σου ("before your face") means Israel. In Mal 3:1 the messenger clears the way before the LORD, לְפָנָי ("before me"). Mark's "your" is addressed to the one who comes next, Jesus (1:9) `[I]`, high. At 1:3 Mark follows Isa 40:3 LXX verbatim until its last phrase, and there he writes αὐτοῦ ("his") for τοῦ θεοῦ ἡμῶν ("of our God"). So the κύριος ("Lord") whose way is prepared — Hebrew יְהוָה ("YHWH") in the Isaiah verse — is the one who arrives at the Jordan `[T]` for the wording, `[I]` for the identification, high.
- **The first sentence joins three texts, and the Hebrew shows why.** Exod 23:20 and Mal 3:1 share the Hebrew formula "behold, I send (שָׁלַח, "to send") my messenger (מַלְאָךְ, "messenger")", and Mal 3:1 and Isa 40:3 share פָּנָה דֶּרֶךְ ("to clear a way"). All four lemmas were verified in the WLC with `find.py` `[T]`. Mark's κατασκευάσει ("will prepare") stands nearer the Hebrew פִּנָּה ("he will clear") than the LXX's ἐπιβλέψεται ("will look upon") *(moderate–high)*. **Triage:** category 3 in its effect — the NT's own form of the text — reached through a Hebrew link.
- **A heaven torn, a Spirit coming down, a man coming up out of the water.** σχιζομένους τοὺς οὐρανούς ("the heavens being torn", 1:10) is not the language of any Greek Old Testament text in the corpus: no form of σχίζω ("to tear") is used of heaven anywhere in Swete. It *is* the Hebrew of Isa 63:19, לוּא־קָרַעְתָּ שָׁמַיִם יָרַדְתָּ ("O that you would tear the heavens and come down"), where Swete and Rahlfs both have ἀνοίξῃς ("open"). Both קָרַע ("to tear") and יָרַד ("to come down") were verified at Isa 63:19 `[T]`. Four verses earlier the same Isaianic prayer asks, "Where is he who brought them up out of the sea with the shepherd of his flock? Where is he who put his Holy Spirit in their midst?" (Isa 63:11, Swete ὁ ἀναβιβάσας ἐκ τῆς θαλάσσης τὸν ποιμένα τῶν προβάτων … τὸ πνεῦμα τὸ ἅγιον). Isa 63:14 adds κατέβη πνεῦμα παρὰ Κυρίου ("the Spirit came down from the Lord"). Mark has ἀναβαίνων ἐκ τοῦ ὕδατος ("coming up out of the water"), τὸ πνεῦμα ("the Spirit") and καταβαῖνον ("coming down") in one verse `[T]`. The prayer of Isa 63–64 for a new exodus, with Spirit and shepherd, is being answered *(moderate–high; synthetic, since it rests on three verses of Isaiah)*.
- **The Spirit "throws him out".** ἐκβάλλει ("drives out", 1:12) is the exorcism verb. ἐκβάλλω ("to cast out") occurs in 16 verses in 1:1–16:8, most of them of demons (1:34, 39; 3:15, 22, 23; 6:13; 7:26; 9:18, 28, 38) `[T]`. Its first use is of the Spirit sending the Son into Satan's territory. The NASB95 has "impelled" and the ESV "drove", and neither lets the reader hear the verb of 1:34 in it.
- **The wilderness scene has no temptation content.** Mark gives no dialogue and no three tests: "forty days, tested by Satan; and he was with the wild beasts, and the angels were serving him" `[T]`. The imperfect διηκόνουν ("were serving") is the verb of Simon's mother-in-law (1:31), of the Son of Man (10:45) and of the women at the cross (15:41). διακονέω ("to serve") occurs at these four places only `[T]`, verified.
- **The promise the book never narrates.** αὐτὸς δὲ βαπτίσει ὑμᾶς ἐν πνεύματι ἁγίῳ ("but he will baptise you with the Holy Spirit", 1:8) is not fulfilled within 1:1–16:8. The nearest approach is 13:11, "it is not you who speak, but the Holy Spirit" `[T]`. Like 14:28 and 16:7, it is a promise that runs past the book's last verse `[I]`, high.

**Tool 11.**

**Exod 23:20 + Mal 3:1 → 1:2** *(high — formula quotation)*. *Source context:* Exod 23:20 comes at the end of the Book of the Covenant. The LORD sends his angel before Israel "to guard you on the way and bring you into the place I have prepared", with a warning to obey his voice. Mal 3:1 answers a people who ask "where is the God of justice?" (2:17): the messenger will clear the way, and then "the Lord whom you seek will suddenly come to his temple" — a coming that refines and judges ("who can endure the day of his coming?", 3:2). *Book usage:* first use; Malachi returns at 9:11–13 (Elijah) and in the temple arrival (11:11, 15). *OT-to-OT:* Malachi reuses the wording of Exodus in the Hebrew (verified above), so the text Mark cites is already a network of texts. *What it adds:* the gospel begins with an exodus guide *and* a temple visitation. The messenger prepares for a Lord who will come to his house, and 11:11–17 is where he arrives.

**Isa 40:3 → 1:3** *(high — formula quotation, Greek verbatim bar one word)*. *Source context:* the opening of Isaiah's comfort (40:1–11): the time of hard service is completed; a voice cries to prepare YHWH's way in the wilderness, for "the glory of the LORD will be revealed" and "the word of our God stands for ever" (40:8). The Lord comes as a shepherd (40:11). *Book usage:* first use of Isaiah, the book's dominant source (see the overview). *OT-to-OT:* Mal 3:1 is itself a reuse of Isa 40:3 (the shared פָּנָה דֶּרֶךְ), so the conflation under Isaiah's name follows a link the Prophets had already made. *What it adds:* the way prepared is YHWH's own coming. Isa 40:8 returns at 13:31 ("my words will not pass away") and the shepherd at 6:34; both are moderate and are taken up at their pericopes.

**Ps 2:7 + Isa 42:1 + Gen 22:2 → 1:11** *(high for Ps 2:7 on Σὺ εἶ ὁ υἱός μου ("You are my Son"); moderate for Isa 42:1, through the Hebrew; moderate–high for Gen 22:2, through ἀγαπητός ("beloved"))*. *Source context:* Ps 2 is the LORD's decree to his anointed king against the rebellious nations. Isa 42:1 is the Servant on whom God puts his Spirit, bringing justice to the nations. Gen 22:2 is the command to offer "your son, your beloved, whom you love, Isaac" (Hebrew יְחִידְךָ, "your only one", which the LXX renders ἀγαπητόν ("beloved")). *Book usage:* all three return. Ps 2:7 comes back at 9:7; ἀγαπητός occurs only at 1:11, 9:7 and 12:6; and the Servant returns at 10:45 and 14:24 (Isa 53). *OT-to-OT:* Isa 42:1 ("my Spirit on him") and the Spirit descending at 1:10 belong together. Ps 2 and Isa 42 both look to the nations. Gen 22 brings the note of an offered son. *What it adds:* king, Servant and beloved son are declared at once. The cross is already present in the word "beloved", and the vineyard parable (12:6) will make that explicit.

**2 Kgs 1:8 → 1:6** *(high)*. *Source context:* Ahaziah's messengers describe the man who turned them back: "a hairy man, with a belt of leather girded round his waist." The king says, "It is Elijah the Tishbite." He then sends three companies of soldiers, and fire falls on two of them. *Book usage:* Elijah will return at 6:15; 8:28; 9:4–5, 11–13; 15:35–36. *OT-to-OT:* Mal 3:23 (Swete 4:4) promises Elijah before the day of the LORD, and Mal 3:1 has just been cited. Mark quotes Malachi's promise and then dresses John in 2 Kings' Elijah, so the reader identifies him without being told `[I]`, high. *What it adds:* John is the Elijah of Malachi. 9:13 will say so, and will add that "they did to him whatever they wished".

**Moderate and uncertain.** The forty days recall Moses (Exod 34:28) and Elijah (1 Kgs 19:8), but the shared wording is only τεσσεράκοντα ἡμέρας ("forty days") *(uncertain)*. The wild beasts have been read as Adam in paradise or as the peace of Isa 11:6–9 `[S]`. Mark supplies nothing to decide between these *(uncertain; do not preach either as the point)*.

*Internal:* **plants §15:37–39** — the torn heavens, the Spirit, the voice and the Son are answered by the torn veil, the breathed-out spirit, the loud voice and the confession (high; verified, see the overview's echo table). **Plants §9:7 and §12:6** — ἀγαπητός ("beloved"), at three places only (high). **Plants §10:52** — the ὁδός ("way") prepared becomes the road Bartimaeus follows (high). **Plants §1:31; §10:45; §15:41** — διακονέω ("to serve") (moderate–high). **Plants §3:23–27** — Satan's first appearance is a test in the wilderness, and his second is the binding of the strong man (moderate). **Plants unresolved** — the Spirit baptism of 1:8 is not narrated (high).

**Translations.** The NASB95's "ahead of you" (1:2) loses πρὸ προσώπου ("before the face") and with it Exod 23:20's idiom; the ESV's "before your face" keeps it. The NASB95's "opening" (1:10) loses the tear, and the ESV's "torn open" keeps it. **Pulpit divergence:** on this unit the ESV is the more literal of the two and serves the findings better. Both print "the Son of God" at 1:1, where the SBLGNT omits it and NA28 brackets it (see the overview).

**Copycat and Who Am I?** The baptism and the wilderness are unique events, not a template. Jesus is not a model believer being tested. He is the Son going ahead into the enemy's territory, and the angels serve *him* `[I]`.

**Pitfall.** "Resist temptation as Jesus did in the wilderness." Mark gives nothing to copy — no quotations of Deuteronomy and no three answers. The corrective: preach 1:12–13 as the Son sent by the Spirit into Satan's domain, which 3:27 explains as the Stronger One entering the strong man's house.

---

## 2. Mark 1:14–20 — "Come Behind Me"

**Position.** *Q1:* the prologue announced the coming one and the gospel. *Q2:* the unit exists here because the forerunner's work ends — μετὰ τὸ παραδοθῆναι τὸν Ἰωάννην ("after John was handed over", 1:14) — and the first act of the Son is to gather people "behind" him. The book's first scene with human beings in it is a call `[T]`.

**Structure.** A summary of the proclamation (14–15). Then two call-scenes in parallel (16–18; 19–20): παράγων / προβάς ("passing along" / "going on"), εἶδεν ("he saw"), the call, and εὐθύς ἀφέντες … ἠκολούθησαν / ἀπῆλθον ὀπίσω αὐτοῦ ("immediately leaving … they followed / went behind him") `[T]`.

**Text-first findings.**

- **The first παραδίδωμι ("to hand over") is John's.** The verb that will carry Jesus' passion (9:31; 10:33; 14:41; 15:1, 15) and the disciples' (13:9, 11, 12) is used first of the forerunner `[T]`. 20 occurrences in 19 verses, verified.
- **The proclamation is compressed into four clauses.** πεπλήρωται ὁ καιρός ("the time has been fulfilled"), ἤγγικεν ἡ βασιλεία τοῦ θεοῦ ("the kingdom of God has come near"), μετανοεῖτε ("repent"), πιστεύετε ἐν τῷ εὐαγγελίῳ ("believe in the gospel") `[T]`. The first two are perfects: they say what has already happened. The second two are imperatives that follow from it. πληρόω ("to fulfil") occurs only here and at 14:49, "that the Scriptures might be fulfilled", at the arrest `[T]`, verified.
- **ὀπίσω μου ("behind me").** Δεῦτε ὀπίσω μου ("come behind me", 1:17) uses the same phrase as John's "he comes ὀπίσω μου" (1:7). It returns with Peter at 8:33, Ὕπαγε ὀπίσω μου, Σατανᾶ ("get behind me, Satan"), and with everyone at 8:34, εἴ τις θέλει ὀπίσω μου ἐλθεῖν ("if anyone wishes to come behind me") `[T]`. The phrase stands at these four places only.
- **"Fishers of men."** In Jer 16:16 the LORD sends "many fishers" (הִנְנִי שֹׁלֵחַ לדוגים רַבִּים, "behold, I am sending for many fishermen" — the WLC prints the ketiv לדוגים unpointed) to catch a people for judgement, before the promise of a return. Ezek 29:4–5 and Amos 4:2 use hooks for judgement `[T]` for the texts. Mark gives no citation, and ἁλιεῖς ἀνθρώπων ("fishers of men") is not the wording of Swete at Jer 16:16 (ἁλεεῖς) *(uncertain)*. The usual preaching of "fishers of men" as evangelism is `[I]` from the context of 3:14 ("to send them out to preach"), and is fair.

**Tool 11.** No quotation. Jer 16:16 *(uncertain)* receives Move 1 only: an oracle of judgement followed by restoration (16:14–15, a new exodus from the north).

*Internal:* **plants §13:3** — the four named here are named together at 1:29, and after that only at 13:3 (moderate–high). **Plants §8:33–34** — ὀπίσω μου (high). **Plants §14:49** — πληρόω (moderate–high). **Plants §10:28** — "we have left everything and followed you": ἀφέντες ("leaving", 1:18, 20) becomes ἀφήκαμεν ("we have left", 10:28) (high, verbal).

**Translations.** NASB95 "Follow Me"; ESV "Follow me". Both render Δεῦτε ὀπίσω μου ("come behind me") as "follow", and so lose the link to ὀπίσω μου at 8:33, where both render "Get behind me". **Pulpit divergence:** none bearing beyond this.

**Pitfall.** "Leave your nets": preaching the call as a demand for heroic renunciation. The text puts the call first and the leaving second. The fishermen leave because he calls; they do not earn the call by leaving. The corrective: preach 1:17 — "I will make you become" — as the promise that carries the leaving.

---

## 3. Mark 1:21–45 — Authority: A Day in Capernaum and a Leper Made Clean

**Position.** *Q1:* the kingdom has come near (1:15). *Q2:* this unit shows what that nearness looks like in a single day (1:21–34) and then on the move (1:35–45). It shows authority in word and deed, the question the authority raises, and the first command to silence — all before any opposition has appeared `[T]`.

**Structure.** A synagogue exorcism (21–28); Simon's mother-in-law (29–31); evening at the door (32–34); prayer before dawn and "let us go elsewhere" (35–39); the leper (40–45). The bookends are the synagogue (1:21) and "all the synagogues of Galilee" (1:39), and then comes the leper `[T]`.

**Text-first findings.**

- **Authority is the keyword.** The crowd is ἐξεπλήσσοντο ("astonished"): he taught ὡς ἐξουσίαν ἔχων ("as one having authority", 1:22). After the exorcism: διδαχὴ καινὴ κατ' ἐξουσίαν ("a new teaching, with authority", 1:27) `[T]`. ἐξουσία ("authority") stands in 9 verses (SBLGNT): 1:22, 27; 2:10; 3:15; 6:7; 11:28, 29, 33; 13:34. It runs from the synagogue here to the temple, where "by what authority?" is asked and left unanswered (11:28–33) `[T]`, verified.
- **The demon knows, and is silenced.** οἶδά σε τίς εἶ, ὁ ἅγιος τοῦ θεοῦ ("I know who you are — the Holy One of God", 1:24). Jesus answers φιμώθητι ("be muzzled", 1:25). φιμόω ("to muzzle, silence") occurs twice in Mark: here, and at 4:39, spoken to the sea `[T]`, verified. **The sea is silenced with the exorcist's word.** English hides it in both versions (NASB95 "Be quiet" / "be still"; ESV "Be silent" / "Be still").
- **The first "raising".** ἤγειρεν αὐτὴν κρατήσας τῆς χειρός ("he raised her, taking her by the hand", 1:31). The same wording returns for Jairus' daughter (5:41) and the boy "like a corpse" (9:27) `[T]`. ἐγείρω ("to raise") is also the verb of 16:6 `[T]`. And she διηκόνει ("was serving", 1:31) — see 1:13 and 15:41.
- **Prayer at night.** πρωῒ ἔννυχα λίαν … κἀκεῖ προσηύχετο ("very early, while it was still night … and there he was praying", 1:35). Jesus prays three times in Mark, each time alone and each time at a turning point: 1:35, 6:46 and 14:32–39. προσεύχομαι ("to pray") of Jesus occurs at these places only; the other uses are teaching (11:24, 25; 13:18) or scribes (12:40) `[T]`, verified.
- **The leper, and 1:41.** "If you are willing (θέλῃς), you can make me clean." "I am willing (θέλω); be clean." The SBLGNT reads ὀργισθείς ("angered") and NA28 σπλαγχνισθείς ("moved with compassion"); see the overview. Nothing here depends on the choice, but note that ἐμβριμησάμενος ("having sternly warned", 1:43) is a strong word whichever reading stands at 1:41 `[T]`. The leper is sent to the priest εἰς μαρτύριον αὐτοῖς ("for a testimony to them", 1:44), and the phrase returns at 6:11 and 13:9 `[T]`.
- **The doubled silence.** ὅρα μηδενὶ μηδὲν εἴπῃς ("see that you say nothing to anyone", 1:44). He goes out and proclaims (κηρύσσειν, "to proclaim", 1:45), and Jesus is left outside, ἐπ' ἐρήμοις τόποις ("in desolate places"), where the leper had been. The last verse of the book reverses this (see the overview's echo table: the doubled "no one … nothing" stands at 1:44 and 16:8 only, verified).

**Tool 11.** **Lev 13–14 → 1:44** *(high — explicit reference to "what Moses commanded", not a quotation)*. *Source context:* the law of the leper's cleansing (Lev 14:2–32), which is performed *after* healing, by a priest who can only pronounce, never effect. *Book usage:* the first explicit reference to Moses (Μωϋσῆς ("Moses") returns at 7:10; 9:4–5; 10:3–4; 12:19, 26). *OT-to-OT:* 2 Kgs 5 (Naaman) is the only healing of leprosy in the Former Prophets, and there too the healed man is sent back with a confession `[I]`. *What it adds:* Jesus does what the priest could only declare, and sends the man to the priest as evidence.

**1 Kgs 17:18 → 1:24** *(uncertain)*. τί ἡμῖν καὶ σοί ("what have we to do with you?") is the widow of Zarephath's cry to Elijah, but the idiom is common (Judg 11:12; 2 Kgs 3:13; 2 Chr 35:21).

*Internal:* **plants §4:39** — φιμόω (high, verified). **Plants §5:41; §9:27; §16:6** — raising by the hand (moderate). **Plants §6:46; §14:32–39** — the three prayers (moderate–high). **Plants §11:28–33** — ἐξουσία (high). **Plants §16:8** — the doubled silence reversed (high on the wording). **Plants §3:6** — the healing on the Sabbath at 1:21–31 passes without comment; by 3:1–6 it will be the charge (moderate).

**Translations.** See 1:41 above. The NASB95's "Moved with compassion" and the ESV's "Moved with pity" both follow NA28. **Pulpit divergence:** the ESV's "sternly charged" at 1:43 is nearer the force of ἐμβριμάομαι ("to warn sternly, snort") than the NASB95's "sternly warned"; neither is wrong.

**Difficulty.** The messianic secret begins here (1:25, 34, 44). See the overview's Trap 1.

**Pitfall.** "Jesus heals whoever asks in faith." The leper's faith is conditional ("if you are willing") and Jesus' answer turns on his own will ("I am willing"). The corrective: preach the healing as a disclosure of his willingness and authority, not as a formula for the petitioner.

---

## 4. Mark 2:1–12 — Authority to Forgive Sins ⭐

**Position.** *Q1:* authority over demons and disease has been shown (1:21–45). *Q2:* this unit exists here because it moves the question from what Jesus can *do* to who he *is*. It carries the first Son of Man saying, the first charge of blasphemy, and the first controversy. It also opens the five-scene cycle 2:1–3:6, which ends in the plot to destroy him `[T]`/`[I]`.

**Structure.** A sandwich in miniature: the healing is begun (2:1–5a), the forgiveness and the scribes' objection are set inside it (2:5b–10), and then the healing is completed (2:11–12) `[T]`. The mid-sentence break at 2:10, where Jesus turns from the scribes to the paralytic, is the hinge.

**Text-first findings.**

- **Sin vocabulary clusters here and nowhere else.** ἁμαρτία ("sin") occurs in six verses of Mark: 1:4 and 1:5 (John's baptism "for the forgiveness of sins", confessing sins), then 2:5, 7, 9 and 10 (SBLGNT, verified) `[T]`. It never appears again. ἄφεσις ("forgiveness") occurs only at 1:4 and 3:29, "never has forgiveness" `[T]`, verified. **After 2:10 the book stops *naming* sin and forgiveness, and speaks instead of ransom (10:45) and covenant blood poured out "for many" (14:24).** `[T]` for the distribution, `[I]` for its significance, moderate–high.
- **"Who can forgive sins except God alone?"** τίς δύναται ἀφιέναι ἁμαρτίας εἰ μὴ εἷς ὁ θεός (2:7). The scribes' theology is right; Mark never corrects it `[T]`. The phrase εἷς ὁ θεός ("God alone") returns in Jesus' own mouth at 10:18, and the Shema's "one" at 12:29 and 32 `[T]`, verified. The book lets the scribes state the premise from which the reader must draw the conclusion `[I]`, high.
- **The first charge is the last.** βλασφημεῖ ("he is blaspheming", 2:7) comes back at the trial: ἠκούσατε τῆς βλασφημίας ("you have heard the blasphemy", 14:64). The only other uses of the root are 3:28–29 (blasphemy against the Spirit), 7:22 and 15:29 (the passers-by "blaspheming" him) `[T]`, verified.
- **The Son of Man has authority "on earth".** ἐξουσίαν ἔχει ὁ υἱὸς τοῦ ἀνθρώπου … ἐπὶ τῆς γῆς (2:10). This is the first of 14 Son of Man sayings (SBLGNT), and it is an *authority* saying. The one like a son of man in Dan 7:14 is given ἐξουσία ("authority", Dan 7:14 OG, Swete) — in heaven. Mark's "on earth" places that authority in the present `[I]`, moderate.
- **"Child, your sins are forgiven."** Τέκνον ("child", 2:5). The passive ἀφίενταί ("are forgiven") leaves the agent unnamed until the scribes name him `[T]`.

**Tool 11.** **Dan 7:13–14 → 2:10** *(moderate — title plus ἐξουσία)*. *Source context:* Daniel's night vision. After the beasts are judged, one like a son of man comes with the clouds to the Ancient of Days and receives dominion, glory and a kingdom that will not pass away. *Book usage:* first Son of Man saying; Dan 7:13 is cited openly at 13:26 and 14:62. *OT-to-OT:* in Dan 7:18, 22 and 27 the kingdom is given to "the saints of the Most High", so the figure is both individual and corporate `[T]` for Daniel. *What it adds:* the title that ends with the Son of Man enthroned (14:62) begins here with the authority to forgive on earth.

**Isa 43:25; Exod 34:6–7 → 2:7** *(moderate — conceptual)*. Move 1 only: in both texts forgiveness is YHWH's own act ("I, I am he who blots out your transgressions for my own sake"). The scribes quote the doctrine; Mark does not quote the text.

*Internal:* **plants §14:64** — blasphemy (high, verified). **Plants §10:18; §12:29, 32** — God "alone"/"one" (moderate–high). **Answers §1:4–5** — John's baptism was "for" (εἰς) the forgiveness of sins; here forgiveness is spoken outright (moderate). **Plants §2:12 → §16:6** — ἠγέρθη ("he got up", 2:12) is the resurrection verb of 16:6. The same form occurs at both places (moderate; a verbal fact, uncertain as design).

**Translations.** The NASB95's "Son" and the ESV's "Son" at 2:5 render Τέκνον ("child"). Both lose the tenderness, but nothing turns on it. **Pulpit divergence:** none bearing.

**Copycat.** The friends' faith is seen (ἰδὼν … τὴν πίστιν αὐτῶν, "seeing their faith", 2:5), and this is description, not a method. The unit's weight falls on *who* forgives, not on what the four did.

**Pitfall.** Preaching the friends as the heroes ("bring your friends to Jesus"). The text subordinates the roof to the forgiveness and the forgiveness to the question of who he is. The corrective: preach 2:7 and 2:10 as the centre, with the roof as the occasion.

---

## 5. Mark 2:13–3:6 — The Bridegroom, the Sabbath, and the Plot

**Position.** *Q1:* 2:1–12 raised the charge of blasphemy. *Q2:* four more controversies follow — eating with sinners, fasting, grain on the Sabbath, healing on the Sabbath. Each one escalates, and the cycle ends where the opposition's logic leads: συμβούλιον … ὅπως αὐτὸν ἀπολέσωσιν ("a plot … how they might destroy him", 3:6). The first Galilean cycle closes on the first plot `[T]`.

**Structure.** The call of Levi and the meal (2:13–17). Fasting and the bridegroom (2:18–22). Grain on the Sabbath (2:23–28). The withered hand (3:1–6). Each scene has a question or objection and a saying of Jesus that answers it (2:17, 19–22, 27–28; 3:4) `[T]`.

**Text-first findings.**

- **The first hint of the cross.** ἐλεύσονται δὲ ἡμέραι ὅταν ἀπαρθῇ ἀπ' αὐτῶν ὁ νυμφίος ("the days will come when the bridegroom is taken away from them", 2:20). ἀπαίρω ("to take away") stands once in Mark. This is the book's first veiled passion saying, spoken before any plot exists `[T]`/`[I]`, high.
- **The bridegroom is a divine title.** In the Prophets the LORD is Israel's husband (Hos 2:16–20; Isa 54:5; 62:5). Isa 62:5 Swete: ὃν τρόπον εὐφρανθήσεται νυμφίος ἐπὶ νύμφῃ ("as a bridegroom rejoices over a bride") `[T]`. Jesus applies the image to himself without comment *(moderate)*.
- **New and old.** The patch and the wineskins: καινόν ("new", 2:21, 22), and later καινὴ διδαχή ("a new teaching", 1:27). καινός ("new") returns at 14:25, "until I drink it new in the kingdom" `[T]`. The new wine of 2:22 and the new wine of 14:25 are the only wine sayings of Jesus in the book *(moderate, as design)*.
- **Lord of the Sabbath.** κύριός ἐστιν ὁ υἱὸς τοῦ ἀνθρώπου καὶ τοῦ σαββάτου ("the Son of Man is lord even of the Sabbath", 2:28) is the second Son of Man saying, and it is again about authority `[T]`.
- **"To save a life or to kill?"** ψυχὴν σῶσαι ἢ ἀποκτεῖναι (3:4). The question is answered by the plot two verses later: those who forbid saving on the Sabbath plan killing. ψυχή ("life, soul") returns at 8:35–37 (save/lose), at 10:45 ("to give his ψυχή as a ransom") and at 14:34 ("my ψυχή is very sorrowful"). σῴζω ("to save") returns at 15:30–31, "save yourself … he cannot save himself" `[T]`, verified. *Synthetic*: moderate–high.
- **Anger and grief at hardness.** μετ' ὀργῆς ("with anger"), συλλυπούμενος ἐπὶ τῇ πωρώσει τῆς καρδίας αὐτῶν ("grieved at the hardness of their heart", 3:5). πώρωσις ("hardness") is the first member of the three-verse chain (3:5; 6:52; 8:17) that closes each Galilean cycle (see the overview) `[T]`, verified.
- **Pharisees with Herodians.** The first alliance is 3:6; it recurs at 12:13. Ἡρῳδιανοί ("Herodians") occurs at these two places only `[T]`, verified.

**Tool 11.** **1 Sam 21:1–6 → 2:25–26** *(high — explicit reference "have you never read")*. *Source context:* David, fleeing Saul, receives the consecrated bread from the priest at Nob (Ahimelech in 1 Sam 21). The next chapter tells of Doeg and the slaughter of the priests, and Abiathar alone escapes (1 Sam 22:20). *Book usage:* first reference to David; David returns at 10:47–48 (Son of David), 11:10 and 12:35–37. *OT-to-OT:* the Chronicler and the Psalms both remember David as the king whose need and whose house are bound up with the sanctuary *(uncertain)*. *What it adds:* the anointed king and his companions eat what the priests alone may eat, and the Son of Man is lord of the Sabbath. **Difficulty:** ἐπὶ Ἀβιαθὰρ ἀρχιερέως ("in the time of Abiathar the high priest") where 1 Sam 21 names Ahimelech. The phrase may mean "in the passage about Abiathar" (compare ἐπὶ τοῦ βάτου, "in the passage about the bush", 12:26) `[S]`. This is one of Mark's known cruxes and should be taken to Logos before it is preached.

**Isa 62:5; Hos 2:16–20 → 2:19** *(moderate)*. Move 1 only: the LORD's marriage to his restored people.

*Internal:* **plants §14:25** — new wine (moderate). **Plants §3:6 → §11:18; §12:12–13; §14:1** — the plot and its alliance (high). **Plants §15:30–31** — "save"/"kill" (moderate–high, synthetic). **Plants §6:52; §8:17** — the hardness chain (high, verified).

**Translations.** NASB95 "reclining at the table … dining with" (2:15); ESV "reclined at table … reclining with". Nothing turns on it. **Pulpit divergence:** none bearing.

**Pitfall.** "Jesus abolished the Sabbath." The text claims Jesus' lordship over the Sabbath and asks about doing good on it. It does not abolish it. The corrective: preach 2:28 and 3:4 as statements of who Jesus is and what the Sabbath is for, not as the repeal of a law.

---

## 6. Mark 3:7–35 — The Stronger One and the Strong Man ⭐

**Position.** *Q1:* the first cycle ended with the plot (3:6). *Q2:* the second cycle opens here, and it opens as the first did, with disciples (3:13–19; compare 1:16–20). It also answers the plot with a definition. Jesus' family are those who "do the will of God" (3:35), and his opponents' charge — that he casts out demons by Beelzebul — is shown to be the blasphemy that has no forgiveness `[T]`/`[I]`.

**Structure.**

| Verses | Section |
|---|---|
| 3:7–12 | Summary: crowds from every region; unclean spirits cry "You are the Son of God"; silenced |
| 3:13–19 | The Twelve appointed on the mountain |
| 3:20–21 | *Opened:* his own come to seize him — "he is out of his mind" |
| 3:22–30 | *Inside:* scribes from Jerusalem — Beelzebul; the strong man; the unforgivable blasphemy |
| 3:31–35 | *Closed:* mother and brothers stand outside; whoever does God's will |

The first sandwich of the book `[T]`: 3:20–21 and 3:31–35 bracket 3:22–30, and the family's "he is out of his mind" is set beside the scribes' "he has Beelzebul".

**Text-first findings.**

- **The Twelve are made "to be with him".** ἐποίησεν δώδεκα, ἵνα ὦσιν μετ' αὐτοῦ καὶ ἵνα ἀποστέλλῃ αὐτούς ("he made twelve, so that they might be with him and that he might send them out", 3:14) `[T]`. ἐποίησεν ("he made") is used twice (3:14, 16), and δώδεκα ("twelve") stands in 15 verses of Mark (verified). The number of Israel's tribes is `[I]`, high. The purpose order — first *with him*, then *sent* — is the order the book keeps.
- **Judas is named in the list as the betrayer.** ὃς καὶ παρέδωκεν αὐτόν ("who also handed him over", 3:19). The narrator tells the reader the end at the start `[T]`.
- **The Stronger One binds the strong man.** οὐδεὶς δύναται εἰς τὴν οἰκίαν τοῦ ἰσχυροῦ … ἐὰν μὴ πρῶτον τὸν ἰσχυρὸν δήσῃ ("no one can enter the strong man's house … unless he first binds the strong man", 3:27). ἰσχυρός ("strong") occurs at 1:7 and 3:27 (twice) only `[T]`, verified. The ἰσχυρότερος ("stronger") John announced is the one who binds. δέω ("to bind") returns in reverse at 15:1: δήσαντες τὸν Ἰησοῦν ("having bound Jesus") `[T]`. *Synthetic*: moderate.
- **Blasphemy against the Spirit is named, and the narrator explains it.** The narrator adds ὅτι ἔλεγον· Πνεῦμα ἀκάθαρτον ἔχει ("because they were saying, 'He has an unclean spirit'", 3:30). The unforgivable sin is defined in the text as calling the Spirit's work in Jesus unclean `[T]`. ἄφεσις ("forgiveness") stands only at 1:4 and here `[T]`.
- **Inside and outside.** ἔξω στήκοντες ("standing outside", 3:31, 32). Those περὶ αὐτόν ("around him", 3:32, 34) are his family. ἔξω ("outside") returns at 4:11, τοῖς ἔξω ("to those outside"), in the parable chapter that follows `[T]`.

**Tool 11.** **Isa 49:24–25 → 3:27** *(moderate)*. *Source context:* the exiles ask, "Can the prey be taken from the mighty?" The LORD answers: "Even the captives of the mighty will be taken … I will contend with those who contend with you, and I will save your children." Swete: λήμψεται σκῦλα … παρὰ ἰσχύοντος ("he will take spoils … from the strong one") `[T]`. *Book usage:* Isaiah is Mark's live source; this is its first use for the exorcisms. *OT-to-OT:* Isa 53:12, "he will divide the spoil with the strong" (τῶν ἰσχυρῶν μεριεῖ σκῦλα, Swete), comes from the same book and uses the same words `[T]`. *What it adds:* the exorcisms are the LORD's promised rescue of captives from a strong captor. The shared wording (ἰσχυρός ("strong"), spoils) is partial, so this stays moderate.

*Internal:* **answers §1:7** — the Stronger One (high, verified). **Answers §1:12–13** — the wilderness contest with Satan is explained (moderate). **Plants §14:10–11, 43–46** — Judas (high). **Plants §4:11** — the insiders and the outsiders (high). **Plants §15:1** — the binder bound (moderate, synthetic). **Plants §6:3** — Jesus' family and hometown again (moderate).

**Translations.** At 3:14 the **ESV** includes "(whom he also named apostles)", which the SBLGNT does not print and the NASB95 omits. It is a variant: NA28 prints [οὓς καὶ ἀποστόλους ὠνόμασεν] ("whom he also named apostles") in single brackets `[T]`, verified; the apparatus evidence should be checked in Logos. At 3:21 οἱ παρ' αὐτοῦ ("those from him") is the NASB95's "His own people" and the ESV's "his family"; the ESV decides what the Greek leaves open, though the sandwich (3:31) supports it. **Pulpit divergence:** the ESV reads the variant at 3:14. The congregation will hear "apostles" named at the appointment, where on the critical text the word first appears at 6:30.

**Difficulty.** 3:28–30, the unforgivable sin. *Category:* pastoral. *Function in context:* a verdict on the scribes from Jerusalem, and its definition is supplied by the narrator (3:30). *Corrective for anxious hearers:* the sin is attributing the Spirit's work in Jesus to Satan — the hardened verdict of the scribes, not the fear of the troubled believer.

**Pitfall.** "Jesus' family thought he was mad, so family ties do not matter." The unit redefines family and does not despise it (compare 7:10–13 and 10:19). The corrective: preach 3:35 as the creation of a new family around Jesus.

---

## 7. Mark 4:1–34 — Parables: Seeing and Not Perceiving ⭐

**Position.** *Q1:* 3:20–35 divided the people around Jesus into insiders and outsiders. *Q2:* the parable discourse, the longest teaching in the book before chapter 13, explains that division. The word is sown; hearing sorts the hearers; what is hidden is meant to be revealed; and the kingdom grows from almost nothing `[T]`/`[I]`.

**Structure.**

| Verses | Section |
|---|---|
| 4:1–2 | Setting: the boat, the sea, the crowd on the land |
| 4:3–9 | *Ἀκούετε* ("Listen!"): the sower; "whoever has ears to hear, let him hear" |
| 4:10–12 | Private: the μυστήριον ("secret") given to insiders; parables for "those outside"; Isa 6:9–10 |
| 4:13–20 | The sower explained |
| 4:21–25 | Lamp and measure: hidden to be revealed; "take care what you hear" |
| 4:26–29 | The seed growing by itself |
| 4:30–32 | The mustard seed |
| 4:33–34 | Summary: parables to them, everything explained privately to the disciples |

A frame of hearing: Ἀκούετε ("Listen!", 4:3) and "let him hear" (4:9, 23), with καθὼς ἠδύναντο ἀκούειν ("as they were able to hear", 4:33) `[T]`. ἀκούω ("to hear") occurs 13 times in 4:1–34 `[T]` (SBLGNT, verified).

**Text-first findings.**

- **The word is the seed.** ὁ σπείρων τὸν λόγον σπείρει ("the sower sows the word", 4:14). λόγος ("word") occurs eight times in 4:14–20 alone `[T]`. The explained parable is about how the λόγος is received.
- **Isa 6:9–10 ends on forgiveness.** μήποτε ἐπιστρέψωσιν καὶ ἀφεθῇ αὐτοῖς ("lest they turn and it be forgiven them", 4:12). The Hebrew has וָשָׁב וְרָפָא לוֹ ("and turn and it heal him") and Swete has ἰάσομαι αὐτούς ("I will heal them") `[T]`. Mark's "be forgiven" follows neither. The Aramaic Targum's "and it be forgiven them" is `[S]` *(moderate; check in Logos)*. **Triage:** category 3 — the NT's own text.
- **"Endure for a while … when affliction or persecution arises."** θλίψεως ἢ διωγμοῦ (4:17). θλῖψις ("affliction") returns at 13:19 and 24; διωγμός ("persecution") returns at 10:30, "with persecutions". Both belong to the book's awareness of a suffering audience (see the overview) `[T]`, verified. σκανδαλίζονται ("they fall away", 4:17) is the verb of 14:27, 29: πάντες σκανδαλισθήσεσθε ("you will all fall away") `[T]`. **The rocky ground describes the Twelve in chapter 14.** *Synthetic*: moderate–high.
- **Hidden in order to be revealed.** οὐ γάρ ἐστιν κρυπτὸν ἐὰν μὴ ἵνα φανερωθῇ ("for nothing is hidden except to be revealed", 4:22). The purpose clause (ἵνα) makes the hiddenness temporary and deliberate `[T]`. The saying governs the messianic secret: the commands to silence (1:44; 5:43; 8:30; 9:9) are provisional, and 9:9 sets their limit, "until the Son of Man rises from the dead" `[I]`, high.
- **The seed grows αὐτομάτη ("by itself", 4:28), ὡς οὐκ οἶδεν αὐτός ("he does not know how", 4:27).** The sower καθεύδῃ ("sleeps", 4:27). Eleven verses later Jesus sleeps in the storm (4:38) `[T]`.

**Tool 11.**

**Isa 6:9–10 → 4:12** *(high — quotation without formula)*. *Source context:* Isaiah's commission in the year King Uzziah died, after the vision of the LORD "high and lifted up" in the temple. The prophet is sent to make the people's heart fat "until cities lie waste" (6:11), and a holy seed remains in the stump (6:13, זֶרַע קֹדֶשׁ מַצַּבְתָּהּ, "the holy seed is its stump") `[T]`. *Book usage:* Isaiah's second use, after 1:2–3. It returns at 8:17–18, where the disciples' "having eyes, do you not see?" (with Jer 5:21) applies the hardening to the insiders. *OT-to-OT:* Isa 6:13's "holy seed" and the sower's seed are both seed after judgement `[I]`, moderate. Jer 5:21 and Ezek 12:2 reuse Isa 6:9–10's eyes and ears (Swete wording overlaps, verified). *What it adds:* the parables work as Isaiah's preaching did. They harden those outside, and a seed survives. And Mark turns the prophet's word against the disciples at 8:18.

**Joel 4:13 (Swete 3:13) → 4:29** *(high)*. *Source context:* the nations are summoned to the valley of Jehoshaphat, "put in the sickle, for the harvest is ripe" — a harvest of judgement at the day of the LORD. *Book usage:* first use of Joel. *OT-to-OT:* none in this passage. *What it adds:* the quiet seed ends in the eschatological harvest. Mark's θερισμός ("harvest") follows the Hebrew קָצִיר ("harvest") against Swete's τρυγητός ("vintage"; see the overview).

**Ezek 17:23; 31:6; Dan 4:9, 18; Ps 104:12 → 4:32** *(moderate)*. Move 1 only. Ezekiel's cedar sprig planted on Israel's high mountain, under which "every bird will nest" (17:23), is a messianic promise. Ezek 31 and Dan 4 are trees of pagan empire that are cut down. Mark's shrub, a μικρότερον ("smallest") seed, borrows the imperial image and shrinks the plant.

*Internal:* **plants §14:27–29** — σκανδαλίζω, the rocky ground (moderate–high, synthetic). **Plants §8:17–18** — Isa 6 against the disciples (high). **Plants §9:9** — the hidden to be revealed (moderate–high). **Plants §4:38** — sleeping (moderate). **Plants §13:10; §14:9** — the word preached to the world (moderate). **Answers §3:31–35** — the "outside" (high).

**Translations.** The NASB95's "the mystery" and the ESV's "the secret" (4:11) both render μυστήριον ("secret"); the ESV's word is nearer the sense of something disclosed to insiders. **Pulpit divergence:** none bearing.

**Genre.** Parables are comparisons with a main thrust. The explanation of the sower (4:14–20) licenses its own allegory, but the lamp, the seed and the mustard seed are not given one.

**Pitfall.** "Four kinds of people — which soil are you?" The explanation invites self-examination, but the parable's weight falls on the sower's persistence and on the final yield (thirty, sixty, a hundred). The corrective: preach the harvest that comes *despite* the losses, and 4:22's promise that the hidden will be revealed.

---

## 8. Mark 4:35–41 — Who Then Is This? ⭐

**Position.** *Q1:* the parable discourse ended with things "explained privately to his own disciples" (4:34). *Q2:* the first thing the insiders then face is a storm that shows they do not know who he is. The unit turns the question of hearing into the question of identity: Τίς ἄρα οὗτός ἐστιν ("who then is this?", 4:41) `[T]`.

**Structure.** Evening departure (35–36); the storm and the sleeper (37–38); the rebuke of wind and sea (39); the rebuke of the disciples (40); the great fear and the question (41).

**Text-first findings.**

- **The exorcist's word to the sea.** ἐπετίμησεν τῷ ἀνέμῳ … Σιώπα, πεφίμωσο ("he rebuked the wind … 'Be silent, be muzzled'", 4:39). ἐπιτιμάω ("to rebuke") is the verb of 1:25 and 3:12, and φιμόω ("to muzzle") stands only at 1:25 and here `[T]`, verified. The sea is addressed as a demonic power `[I]`, high.
- **Jonah's great fear.** ἐφοβήθησαν φόβον μέγαν ("they feared a great fear", 4:41) is verbatim with Jonah 1:10 LXX (Swete) `[T]`. Jonah's storm has the same shape: a man asleep in the ship (Jonah 1:5), terrified sailors who wake him, a sea that grows calm (1:15) and a great fear (1:16). But the sailors' fear in Jonah comes because they *know* whom Jonah is fleeing; the disciples' fear comes because they do *not* know who this is `[I]`.
- **"Do you not care that we are perishing?"** οὐ μέλει σοι ὅτι ἀπολλύμεθα (4:38) — the same question the sailors put to the sleeping Jonah (Swete 1:6, ὅπως διασώσῃ ὁ θεὸς ἡμᾶς καὶ μὴ ἀπολώμεθα, "so that God may save us and we may not perish") *(moderate–high)*. ἀπόλλυμι ("to perish, destroy") is the verb of the plot (3:6; 11:18) and of the demons' fear (1:24) `[T]`.
- **"No faith yet."** οὔπω ἔχετε πίστιν ("have you still no faith?", 4:40). οὔπω ("not yet") returns at 8:17 and 8:21, "do you not yet understand?" `[T]`.
- **Fear, not faith, is the response.** The miracle produces φόβος ("fear") and a question; it does not produce a confession `[T]`. φοβέομαι ("to fear") occurs in 12 verses of Mark, and the last is 16:8.

**Tool 11.**

**Jonah 1:4–16 → 4:35–41** *(high — verbatim clause plus a matching sequence)*. *Source context:* the prophet flees the LORD's commission to Nineveh; the LORD hurls a storm; the sleeping prophet is woken by men who pray to their gods; he is thrown into the sea, the sea grows calm, and the pagan sailors fear the LORD and sacrifice to him. *Book usage:* first use of Jonah; no other use in Mark *(so not live)*. *OT-to-OT:* Ps 107:23–30, the storm stilled by the LORD for sailors who cry to him, shares the pattern *(uncertain on wording)*. *What it adds:* Jesus sleeps like Jonah and then does what only the LORD does in Jonah. In Jonah the calm comes by throwing a man overboard; here it comes by a word. The one in the boat is not the fugitive but the Lord of the sea.

**Ps 107:29 (Swete 106:29) → 4:39** *(uncertain on wording, moderate on pattern)*. Move 1 only.

*Internal:* **answers §1:25** — φιμόω (high). **Plants §6:45–52** — the second sea crossing, where "it is I" answers "who is this?" (high). **Plants §8:17, 21** — οὔπω ("not yet") (moderate–high). **Plants §14:37–41** — the sleeper reversed (moderate). **Plants §16:8** — the great fear (moderate–high).

**Translations.** NASB95 "Hush, be still"; ESV "Peace! Be still!" Both hide φιμόω and its link to 1:25. **Pulpit divergence:** the ESV's "Peace!" gives the congregation a word the Greek does not have here. Σιώπα means "be silent". The NASB95's "Hush" is nearer.

**Pitfall.** "Jesus will calm the storms in your life." Mark's point is the question in 4:41, and the one who stills the storm will not be spared his own (15:30–32). The corrective: preach who he is — the Lord of wind and sea — and let the disciples' fear stand as the right response to that discovery.

---

## 9. Mark 5:1–20 — Legion

**Position.** *Q1:* the storm was silenced like a demon (4:39). *Q2:* on the far shore Jesus meets the demonic power in its fullest form, and this is the first crossing into Gentile territory. The unit answers the disciples' question (4:41) with a demon's confession: "Jesus, Son of the Most High God" (5:7) `[T]`.

**Structure.** The man among the tombs (1–5); the encounter and the name (6–10); the swine (11–13); the townsfolk and their fear (14–17); the sending (18–20).

**Text-first findings.**

- **Uncleanness piled up.** Tombs (ἐν τοῖς μνήμασιν, "in the tombs", 5:3, 5), swine (χοῖροι, 5:11–16) and an unclean spirit (5:2, 8, 13). The scene is set where an Israelite reader would find every kind of uncleanness at once `[T]` for the details, `[I]` for the reader's response, high. Isa 65:4 Swete: those who sit ἐν τοῖς μνήμασιν … οἱ ἔσθοντες κρέας ὕειον ("in the tombs … who eat swine's flesh"), in an indictment of a rebellious people `[T]` *(moderate)*.
- **No one could bind him.** οὐδεὶς ἐδύνατο αὐτὸν δῆσαι … οὐδεὶς ἴσχυεν αὐτὸν δαμάσαι ("no one could bind him … no one had strength to subdue him", 5:3–4). δέω ("to bind") and ἰσχύω ("to be strong") are the vocabulary of the strong man in 3:27 `[T]`. The one who is stronger binds what no one else could *(moderate, synthetic)*.
- **"Son of the Most High God."** υἱὲ τοῦ θεοῦ τοῦ ὑψίστου (5:7). θεοῦ τοῦ ὑψίστου ("of God Most High") is Melchizedek's title for God (Gen 14:18, Swete), a title used by and of Gentiles `[T]` *(moderate)*. The demon kneels (προσεκύνησεν, "bowed down", 5:6), and προσκυνέω ("to bow down") recurs only at 15:19, in the soldiers' mock homage `[T]`, verified.
- **"Legion."** λεγιών ("legion", 5:9, 15) is a Latin military loanword (see the overview). The name's political overtone (a Roman legion; the boar as a legion's emblem) is `[S]` *(uncertain; do not preach it as the point)*.
- **The drowning.** ἐπνίγοντο ἐν τῇ θαλάσσῃ ("they were drowned in the sea", 5:13). The sea that was silenced swallows the unclean spirits. Exod 14:28 (Pharaoh's army covered by the sea) is *uncertain*.
- **The healed man is told to speak.** Ὕπαγε … ἀπάγγειλον αὐτοῖς ὅσα ὁ κύριός σοι πεποίηκεν ("go … tell them how much the Lord has done for you", 5:19). He proclaims ὅσα ἐποίησεν αὐτῷ ὁ Ἰησοῦς ("how much Jesus had done for him", 5:20) `[T]`. Jesus says "the Lord", and the man says "Jesus". The narrator lets the substitution stand `[I]`, high. This is the one command to *speak* in Galilee's cycles, and it is given in Gentile territory `[T]`.

**Tool 11.** **Isa 65:4 → 5:3–5** *(moderate)*. *Source context:* the LORD has held out his hands "to a rebellious people" who sacrifice in gardens, "sit in the tombs, spend the night in secret places, eat swine's flesh" (Isa 65:2–4). The next verses promise a remnant and new heavens and a new earth (65:8–17). *Book usage:* Isaiah is live. *OT-to-OT:* none in the passage. *What it adds:* the man lives the life Isaiah condemns, and he is cleansed rather than condemned.

**Gen 14:18 → 5:7** *(moderate)*. Move 1 only.

*Internal:* **answers §4:41** — the identity question is answered by a demon (high). **Answers §3:27** — the strong man's captive freed (moderate). **Plants §15:19** — προσκυνέω (moderate, verified). **Plants §7:24–8:10** — Gentile territory (moderate). **Reverses §1:44** — told to speak, not to be silent (high).

**Translations.** NASB95 "what great things the Lord has done for you"; ESV "how much the Lord has done for you". Both keep "Lord" and "Jesus" distinct. **Pulpit divergence:** none bearing.

**Difficulty.** The swine and their owners (5:13–17). *Category:* ethical/apologetic. *Function:* the loss of the herd is what leads the townsfolk to beg him to leave. The text registers the cost and does not comment on it.

**Pitfall.** Preaching the healed man as a model evangelist ("go home and tell"). He asked to be with Jesus (ἵνα μετ' αὐτοῦ ᾖ, "that he might be with him", 5:18), the very phrase of the Twelve's calling in 3:14, and he was refused. The corrective: his commission is particular, and the contrast with the Twelve is part of the point.

---

## 10. Mark 5:21–43 — Daughter, and Little Girl

**Position.** *Q1:* Jesus has silenced a storm and freed a man whom no one could bind (4:35–5:20). *Q2:* the next opponent is death, and the unit sets two daughters side by side. One is twelve years ill and one is twelve years old, and the second is raised. It is the peak of the Galilean deeds. It is followed at once by the hometown's unbelief (6:1–6a), which closes the second cycle `[T]`/`[I]`.

**Structure.** The second sandwich of the book `[T]`: Jairus' plea (21–24) → the woman with the flow of blood (25–34) → the message of death and the raising (35–43). Two δώδεκα ("twelve") frame it: ἔτη δώδεκα ("twelve years", 5:25) and ἦν γὰρ ἐτῶν δώδεκα ("for she was twelve years old", 5:42) `[T]`.

**Text-first findings.**

- **Two daughters.** Jairus says τὸ θυγάτριόν μου ("my little daughter", 5:23). Jesus calls the woman Θυγάτηρ ("Daughter", 5:34), the only person in Mark he addresses so `[T]`. The messengers then say ἡ θυγάτηρ σου ἀπέθανεν ("your daughter has died", 5:35). The woman is made a daughter while the daughter is dying *(moderate, as design)*.
- **σῴζω ("to save") throughout.** ἵνα σωθῇ καὶ ζήσῃ ("that she may be saved and live", 5:23); σωθήσομαι ("I shall be saved", 5:28); ἡ πίστις σου σέσωκέν σε ("your faith has saved you", 5:34) `[T]`. The same sentence is spoken to Bartimaeus (10:52). σῴζω is also the verb of the mockery at the cross (15:30–31), "he saved others; he cannot save himself" `[T]`, verified. *Synthetic*: high on the words, moderate on the design.
- **Uncleanness again.** A woman ἐν ῥύσει αἵματος ("with a flow of blood", 5:25) — the wording of Lev 15:25 Swete, γυνὴ ἐὰν ῥέῃ ῥύσει αἵματος ("if a woman has a flow of blood") — and a corpse. Both would make a Jew who touched them unclean (Lev 15:19–27; Num 19:11) `[T]` for the law. Jesus is touched by the first and takes the second by the hand. Uncleanness does not pass to him; power goes out from him (τὴν ἐξ αὐτοῦ δύναμιν ἐξελθοῦσαν, "the power that had gone out from him", 5:30) `[T]`/`[I]`.
- **"Do not fear; only believe."** Μὴ φοβοῦ, μόνον πίστευε (5:36). Fear and faith are set against each other, as at 4:40–41 `[T]`.
- **Laughed at, then astonished.** κατεγέλων αὐτοῦ ("they laughed at him", 5:40); ἐξέστησαν εὐθὺς ἐκστάσει μεγάλῃ ("they were immediately astonished with great astonishment", 5:42) `[T]`. ἔκστασις ("astonishment") occurs at 5:42 and 16:8 only — the raising of the girl, and the empty tomb `[T]`, verified.
- **The first of the three witnesses.** Peter, James and John alone go in (5:37). The same three are with him on the mountain (9:2) and in Gethsemane (14:33); with Andrew they hear the discourse (13:3). Peter and James are named together at these four verses only `[T]`, verified.
- **The Aramaic word is kept.** Ταλιθα κουμ, ὅ ἐστιν μεθερμηνευόμενον ("which is translated", 5:41). μεθερμηνεύω ("to translate") returns at 15:22 (Golgotha) and 15:34 (Eloi) `[T]`, verified. The three translated Aramaic sayings are a raising and two sayings at the cross.

**Tool 11.** **1 Kgs 17:17–24; 2 Kgs 4:18–37 → 5:35–43** *(moderate — pattern, not wording)*. *Source context:* Elijah raises the widow's son and Elisha the Shunammite's son. Elisha shuts the door "behind the two of them" (2 Kgs 4:33) and prays, and both prophets stretch themselves on the child. *Book usage:* the Elijah material is live (1:6; 6:15; 8:28; 9:4–13). *OT-to-OT:* the two raisings are a pair within Kings, the second retelling the first. *What it adds:* the pattern is followed — the room cleared, the chosen witnesses — and broken. There is no prayer and no stretching; there is a word and a hand.

**Lev 15:25 → 5:25** *(high on wording)*. Move 1 only: the law of the woman whose flow continues, who makes unclean whatever she touches (15:26–27).

*Internal:* **answers §1:31** — "taking her by the hand" (moderate). **Plants §10:52** — "your faith has saved you" (high, verbal). **Plants §15:30–31** — σῴζω (moderate, synthetic). **Plants §16:8** — ἔκστασις and τρόμος ("trembling"; the woman came φοβηθεῖσα καὶ τρέμουσα, "fearing and trembling", 5:33) (moderate). **Plants §9:2; §14:33** — the three (high). **Plants §6:22, 28** — κοράσιον ("girl") (see the next pericope).

**Translations.** At 5:34 NASB95 "has made you well" and ESV "has made you well" both render σέσωκέν σε ("has saved you"); both hide the link with 15:31. **Pulpit divergence:** none beyond this.

**Pitfall.** "Touch Jesus in faith and you will be healed." Jesus insists on finding the woman (5:30–32), and the healing ends in a relationship ("Daughter") and a public confession, not in private contact. The corrective: preach the word "Daughter" as the goal of the scene.

---

## 11. Mark 6:1–6a — A Prophet Without Honour

**Position.** *Q1:* Jesus has raised the dead (5:41–42). *Q2:* the unit exists here to close the second Galilean cycle, as 3:6 closed the first. Its last word is ἀπιστία ("unbelief", 6:6): the hometown rejects the one who raised a girl a few verses earlier `[T]`.

**Structure.** Arrival and teaching (1–2a); the astonished questions (2b–3); the saying about the prophet (4); the verdict — he *could not* do mighty works, and he *marvelled* (5–6a).

**Text-first findings.**

- **The questions are the right ones.** Πόθεν τούτῳ ταῦτα, καὶ τίς ἡ σοφία ("where did this man get these things, and what is this wisdom?", 6:2). The hometown asks what 4:41 asked. Their answer — the τέκτων ("carpenter"), ὁ υἱὸς τῆς Μαρίας ("the son of Mary"), his brothers and sisters — is correct and insufficient `[T]`/`[I]`.
- **"Son of Mary."** In Mark Jesus is never called Joseph's son. The phrase stands alone and unexplained `[T]`. That it implies a slur is `[S]` *(uncertain; do not preach it as fact)*.
- **ἐσκανδαλίζοντο ἐν αὐτῷ ("they were offended at him", 6:3).** The rocky-ground verb (4:17) and the Twelve's verb (14:27, 29) `[T]`.
- **He could not.** οὐκ ἐδύνατο ἐκεῖ ποιῆσαι οὐδεμίαν δύναμιν ("he could do no mighty work there", 6:5) `[T]`. Only Mark says "could not". The next clause qualifies it at once: "except that he laid his hands on a few sick people and healed them" `[T]`.
- **Jesus marvels.** ἐθαύμαζεν διὰ τὴν ἀπιστίαν αὐτῶν ("he marvelled because of their unbelief", 6:6). θαυμάζω ("to marvel") is used of the Decapolis (5:20) and twice of Pilate (15:5, 44), and here of Jesus. ἀπιστία ("unbelief") recurs at 9:24, "help my unbelief" `[T]`, verified.

**Tool 11.** No quotation. The proverb of the prophet without honour has no Old Testament source. Its application to Jesus invites Jer 11:21 (Anathoth's men plotting against Jeremiah) *(uncertain)*.

*Internal:* **answers §3:20–21, 31–35** — the family theme, now at home (moderate). **Plants §9:24** — ἀπιστία (moderate). **Closes the second cycle** — see the overview's three-cycle table (high).

**Translations.** NASB95 "took offense"; ESV "took offense". Both lose σκανδαλίζω's link with 14:27. **Pulpit divergence:** none.

**Pitfall.** Preaching 6:5 as a limit on Jesus' power, or explaining it away. The text says both things — "could not" and "except". The corrective: let the sentence stand as a statement about unbelief's refusal, and pair it with 9:23–24.

---

## 12. Mark 6:6b–30 — The Twelve Sent, and John Beheaded

**Position.** *Q1:* the second cycle closed on unbelief (6:6). *Q2:* the third cycle opens, like the first two, with the disciples (3:13–19; 1:16–20). This time they are *sent*, and the mission is wrapped around the story of the first man whose preaching led to his being "handed over" (1:14). The sending is set inside a martyrdom `[T]`/`[I]`.

**Structure.** A sandwich `[T]`: the sending (6:7–13) → Herod's fear and the story of John's death (6:14–29) → the return, οἱ ἀπόστολοι ("the apostles", 6:30).

**Text-first findings.**

- **The Twelve do what Jesus did.** κηρύσσω ("to proclaim"), ἐξουσία ("authority") over unclean spirits, ἵνα μετανοῶσιν ("that they should repent", 6:12; compare 1:15), casting out demons and healing (6:13) `[T]`. The apostles are the Son's mission extended.
- **Travel light.** A staff and sandals only (6:8–9). Exod 12:11 (Passover eaten with staff in hand and sandals on) is *uncertain* on wording: Swete has βακτηρίαι ("staffs") and ὑποδήματα ("sandals"), not Mark's ῥάβδος ("staff") and σανδάλια ("sandals").
- **Herod is "king" five times.** ὁ βασιλεὺς Ἡρῴδης ("King Herod", 6:14); ὁ βασιλεύς ("the king", 6:22, 25, 26, 27) `[T]`. βασιλεύς ("king") occurs in 12 verses of Mark: five in this story, one generic (13:9), and six in chapter 15, all of Jesus ("King of the Jews", 15:2, 9, 12, 18, 26; "King of Israel", 15:32) `[T]`, verified. **The book has two kings. One kills a prophet at his birthday feast; the other is killed as "King of the Jews".** That Antipas was a tetrarch, not a king, is `[S]`, and the title may be ironic `[I]`, moderate.
- **John's death rehearses Jesus' death.** See the overview's echo table. The pattern is: ἐκράτησεν … ἔδησεν ("he seized … bound", 6:17; compare 14:46; 15:1); a ruler who fears the man and hears him gladly (6:20; compare 11:18, 32; 12:37 ἡδέως, "gladly"); a ruler περίλυπος ("very sorry", 6:26 — the same word as Jesus' "my soul is περίλυπος", 14:34, its only other use); a ruler who gives way because of those present; a πτῶμα ("corpse") laid ἐν μνημείῳ ("in a tomb", 6:29; compare 15:45–46) `[T]`, verified. Herod ὤμοσεν ("swore", 6:23), and ὀμνύω ("to swear") occurs only here and at 14:71, where Peter swears he does not know Jesus `[T]`, verified.
- **Two girls.** κοράσιον ("girl") occurs at 5:41, 42 and 6:22, 28, and nowhere else `[T]`, verified. One girl is raised from death; the next girl asks for a man's head. The juxtaposition is `[I]` *(moderate)*.
- **"Raised."** Ἰωάννης ὁ βαπτίζων ἐγήγερται ἐκ νεκρῶν ("John the Baptiser has been raised from the dead", 6:14; ἠγέρθη, "he has been raised", 6:16). Herod's guess uses the verb of 16:6. The first resurrection claim in the book is a mistaken one `[T]`/`[I]`.

**Tool 11.** **Esth 5:3, 6; 7:2 → 6:23** *(high on wording; see the overview)*. *Source context:* at Esther's banquets Ahasuerus offers "up to half my kingdom", and Esther uses the offer to save her people and to have Haman hanged. *Book usage:* first and only use of Esther. *OT-to-OT:* none here. *What it adds:* the oath is Persian court language, and Herod's banquet inverts Esther's: a woman's request brings death to the righteous, not deliverance.

**1 Kgs 19:2, 10; 21 (Jezebel and Ahab) → 6:17–29** *(moderate — conceptual, and invited by 9:13)*. *Source context:* Jezebel seeks Elijah's life after Carmel (19:2); Ahab, weak and compliant, lets Jezebel have Naboth killed (21:5–16). *Book usage:* the Elijah thread (1:6; 6:15; 9:11–13). *OT-to-OT:* Mal 3:23 promised Elijah's return. *What it adds:* 9:13 says of Elijah (John) that "they did to him whatever they wished, *as it is written of him*" (καθὼς γέγραπται ἐπ' αὐτόν). The only place where it is written that someone sought to do Elijah harm is the Jezebel story. So Herodias is Jezebel and Herod is Ahab *(moderate; the verbal overlap in Swete is thin — καθώς only)*.

*Internal:* **plants §9:11–13** — "they did to him whatever they wished" (high). **Plants §14:34; §14:71** — περίλυπος and ὀμνύω (moderate–high, verified). **Plants §15** — the two kings (moderate, synthetic). **Plants §15:45–46** — πτῶμα and μνημεῖον (high, verified). **Answers §1:14** — "after John was handed over" is now narrated (high).

**Translations.** At 6:14 the NASB95 has "people were saying" and the ESV "Some said" for ἔλεγον ("they were saying"), the SBLGNT's reading; NA28's apparatus has ἔλεγεν ("he was saying") as a variant `[S]`, which is not load-bearing. At 6:29 both render πτῶμα as "body" and so lose the link with 15:45, where the ESV has "corpse". **Pulpit divergence:** none bearing beyond this.

**Pitfall.** Preaching John's death as a separate moral tale (the dangers of rash oaths, or of dancing). Mark sets it inside the mission, where it is a warning of what preaching repentance costs, and a rehearsal of the passion. The corrective: preach it with 6:7–13 and 9:13.

---

## 13. Mark 6:30–52 — A Shepherd for the Shepherdless; "It Is I" ⭐

**Position.** *Q1:* the apostles return from their mission (6:30), and a king has just held a banquet that killed a prophet (6:21–29). *Q2:* the next meal is Jesus' own, in the wilderness, for sheep without a shepherd. The contrast between the two banquets is placed deliberately, back to back `[I]`, high. The sea crossing that follows answers the storm's question of 4:41 in Jesus' own words, ἐγώ εἰμι ("it is I", 6:50). The narrator's comment (6:52) then begins the third cycle's closing theme, the disciples' hardened heart `[T]`.

**Structure.** Withdrawal to a desolate place (30–33); compassion and teaching (34); the feeding (35–44); the dismissal and the prayer on the mountain (45–46); the walking on the sea (47–51); the narrator's verdict (52). (6:30 is the hinge between this unit and the last, as the overview's units overlap there.)

**Text-first findings.**

- **Compassion first becomes teaching.** ἐσπλαγχνίσθη ἐπ' αὐτοὺς ὅτι ἦσαν ὡς πρόβατα μὴ ἔχοντα ποιμένα, καὶ ἤρξατο διδάσκειν αὐτοὺς πολλά ("he had compassion on them, because they were like sheep without a shepherd, and he began to teach them many things", 6:34) `[T]`. The shepherd's first act is to teach; the feeding comes after.
- **Shepherd and sheep occur twice.** ποιμήν ("shepherd") and πρόβατον ("sheep") stand in Mark at 6:34 and 14:27, and nowhere else: "I will strike the shepherd, and the sheep will be scattered" `[T]`, verified. **The shepherd provided for the shepherdless is the shepherd struck.** *Synthetic, verified:* high on the distribution, moderate–high on the design.
- **A meal ordered like Israel in the wilderness.** "Sit down συμπόσια συμπόσια ("group by group") on the green grass"; ἀνέπεσαν πρασιαὶ πρασιαί ("they reclined, bed by bed"), κατὰ ἑκατὸν καὶ κατὰ πεντήκοντα ("by hundreds and by fifties", 6:39–40) `[T]`. Moses organised Israel in hundreds and fifties (Exod 18:21, 25) *(uncertain)*.
- **The four verbs of the Supper.** λαβὼν … εὐλόγησεν καὶ κατέκλασεν … καὶ ἐδίδου ("taking … he blessed and broke … and gave", 6:41). The same sequence stands at 8:6 (εὐχαριστήσας, "having given thanks") and 14:22 (λαβὼν ἄρτον εὐλογήσας ἔκλασεν καὶ ἔδωκεν, "taking bread, having blessed, he broke and gave") `[T]`, verified. The feeding anticipates the Supper `[I]`, high.
- **"You give them to eat."** Δότε αὐτοῖς ὑμεῖς φαγεῖν (6:37). Elisha said δότε τῷ λαῷ καὶ ἐσθιέτωσαν ("give to the people and let them eat", 2 Kgs 4:42–43 Swete), and there was food left over (4:44) `[T]`. Twenty loaves fed a hundred; five loaves feed five thousand `[I]`.
- **The walking on the sea is a theophany.** περιπατῶν ἐπὶ τῆς θαλάσσης ("walking on the sea") is the wording of Job 9:8 Swete (περιπατῶν ὡς ἐπ' ἐδάφους ἐπὶ θαλάσσης, "walking on the sea as on dry ground"), said of God alone `[T]`. ἤθελεν παρελθεῖν αὐτούς ("he intended to pass by them", 6:48) uses the verb of the LORD "passing by" Moses (Exod 33:19, 22 Swete, παρελεύσομαι; Exod 34:6, παρῆλθεν) and Elijah on the mountain, with "a great and strong wind" (1 Kgs 19:11 Swete, ἰδοὺ παρελεύσεται Κύριος, "behold, the Lord will pass by") `[T]`, verified in Swete. Jesus has just come down from a mountain where he prayed (6:46), and the wind is against them (6:48) `[T]`. Then comes ἐγώ εἰμι ("it is I", "I am", 6:50) `[T]`. *Synthetic*: moderate–high.
- **The same calm, in the same words.** ἐκόπασεν ὁ ἄνεμος ("the wind ceased") stands identically at 4:39 and 6:51 `[T]`. The second crossing answers the first.
- **The narrator's verdict.** οὐ γὰρ συνῆκαν ἐπὶ τοῖς ἄρτοις, ἀλλ' ἦν αὐτῶν ἡ καρδία πεπωρωμένη ("for they had not understood about the loaves, but their heart was hardened", 6:52) `[T]`. This is the second member of the πώρωσις/πωρόω ("hardness") chain (3:5; 6:52; 8:17), and it is now said of the disciples. It links the sea to the loaves: understanding the feeding would have been understanding who walks on the sea `[I]`, high.

**Tool 11.**

**Num 27:17 (with 1 Kgs 22:17; Ezek 34:5) → 6:34** *(high — distinctive phrase)*. *Source context:* Moses, told he will die outside the land, asks the LORD to appoint a man over the congregation "who will go out before them and come in before them … so that the congregation of the LORD may not be like sheep which have no shepherd". The answer is Joshua — Ἰησοῦς ("Jesus") in the Greek — a man "in whom is the Spirit" (27:18) `[T]`. Micaiah sees Israel scattered "like sheep that have no shepherd" when Ahab dies (1 Kgs 22:17). In Ezek 34 the LORD judges the false shepherds and promises "I will set over them one shepherd, my servant David" (34:23). *Book usage:* first use of the shepherd image; it returns at 14:27 (Zech 13:7). *OT-to-OT:* Ezek 34 and Zech 13:7 are in conversation. Both concern the LORD's shepherd, and in Zech 13 the shepherd is struck and the flock is refined. *What it adds:* the Joshua-named shepherd Moses asked for, and the David-shepherd Ezekiel promised, feeds the flock that Herod's court has just shown to be shepherdless. Isa 63:11's "the shepherd of his flock", brought up from the sea (see unit 1), may also be in view *(uncertain)*.

**Job 9:8; Exod 33:19–22; 34:6; 1 Kgs 19:11 → 6:48–50** *(moderate–high — shared verbs in a theophany setting)*. *Source context:* Job praises the God who alone treads the sea. The LORD passes by Moses in the cleft of the rock and proclaims his name. The LORD passes by Elijah on Horeb in wind, earthquake and fire, and then in a thin voice. *Book usage:* first theophany in Mark after the baptism. *OT-to-OT:* 1 Kgs 19 deliberately retells Exod 33–34, Elijah at the same mountain `[S]`. *What it adds:* the disciples see what Moses and Elijah saw — the LORD passing by — and they do not understand. Moses and Elijah will appear with him at 9:4.

**2 Kgs 4:42–44 → 6:35–44** *(moderate)*. See the overview.

*Internal:* **answers §4:35–41** — "who is this?" is answered by "it is I" (high). **Plants §14:22** — the Supper verbs (high). **Plants §14:27** — the shepherd (high, verified). **Plants §8:17** — hardness (high). **Answers §6:21–29** — Herod's banquet against the wilderness meal (moderate). **Plants §9:4** — Moses and Elijah (moderate).

**Translations.** At 6:50 the NASB95's "it is I" and the ESV's "it is I" both render ἐγώ εἰμι ("I am"); the divine-name resonance is lost in both. At 6:52 the NASB95's "had not gained any insight from" hides συνίημι ("to understand"), and the ESV's "did not understand" keeps it. **Pulpit divergence:** the ESV is better here for the chain of understanding.

**Copycat.** "You give them to eat" is a command to the disciples within the story, and they cannot do it. The feeding is his act.

**Pitfall.** Preaching the feeding as a lesson in sharing, or the sea-walking as "keep your eyes on Jesus" (which comes from Matthew's Peter). Mark's point is the theophany and the disciples' failure to see it (6:52). The corrective: preach "It is I" as the answer to "Who is this?", and the narrator's verdict as the warning.

---

## 14. Mark 6:53–7:23 — What Defiles ⭐

**Position.** *Q1:* the loaves (ἄρτοι) have been multiplied and not understood (6:52). *Q2:* the next dispute is about eating bread (ἐσθίουσιν τὸν ἄρτον, "they eat the bread", 7:2, 5) with defiled hands. It defines where impurity comes from and prepares for a Gentile to receive the children's bread (7:27). ἄρτος ("bread") occurs in 19 verses of Mark, and 16 of them fall in 6:8–8:19 `[T]`, verified.

**Structure.** A summary of healings (6:53–56); the Pharisees' question (7:1–5), with the narrator's explanation of Jewish custom (7:3–4); Jesus' answer from Isaiah and Moses (7:6–13); the parable to the crowd (7:14–15); the explanation to the disciples (7:17–23), with the narrator's aside (7:19c).

**Text-first findings.**

- **The narrator explains Judaism to outsiders.** "For the Pharisees and all the Jews do not eat unless they wash …" (7:3–4) `[T]`. The audience needs the custom explained (see the overview's Presenting Situation).
- **Tradition against commandment.** παράδοσις ("tradition") occurs five times in 7:3–13; ἐντολὴ τοῦ θεοῦ ("the commandment of God") at 7:8 and 9; ἀκυροῦντες τὸν λόγον τοῦ θεοῦ ("making void the word of God", 7:13) `[T]`. Κορβᾶν (7:11) is glossed ὅ ἐστιν Δῶρον ("that is, a gift").
- **Isaiah quoted in the Greek.** Isa 29:13 is cited with the LXX's μάτην δὲ σέβονταί με ("in vain do they worship me"), where the Hebrew reads וַתְּהִי יִרְאָתָם אֹתִי מִצְוַת אֲנָשִׁים מְלֻמָּדָה ("their fear of me is a commandment of men learned by rote") `[T]`. **Triage:** category 3 — the NT's own text. The Greek sharpens the point to "worship in vain", but the Hebrew makes the same charge, of human command displacing the fear of God.
- **The heart.** "Their heart (καρδία) is far from me" (7:6); food "does not go into his heart but into his stomach" (7:19); "from within, out of the heart of men" (7:21) `[T]`. καρδία ("heart") occurs in 11 verses of Mark, and its sequence is instructive: the scribes' hearts (2:6, 8), the Pharisees' hardness of heart (3:5), the disciples' hardened heart (6:52; 8:17), and here the source of defilement (7:6, 19, 21) `[T]`, verified.
- **"Cleansing all foods."** καθαρίζων πάντα τὰ βρώματα (7:19c) is a narrator's comment, a participle hung from the sentence `[T]`. καθαρίζω ("to cleanse") was the leper's word (1:40–42) `[T]`.
- **The vice list.** διαλογισμοὶ οἱ κακοί ("evil thoughts") is followed by twelve items: six plurals (πορνεῖαι, κλοπαί, φόνοι, μοιχεῖαι, πλεονεξίαι, πονηρίαι — "sexual immoralities, thefts, murders, adulteries, covetings, wickednesses") and six singulars (δόλος, ἀσέλγεια, ὀφθαλμὸς πονηρός, βλασφημία, ὑπερηφανία, ἀφροσύνη — "deceit, sensuality, an evil eye, slander, pride, folly") `[T]`. Murder, adultery and theft are Decalogue sins, and the evil eye is a Hebrew idiom for envy `[I]`.
- **"Are you also without understanding?"** Οὕτως καὶ ὑμεῖς ἀσύνετοί ἐστε; (7:18). συνίημι ("to understand") and its compounds run through this third cycle: 6:52; 7:14 (σύνετε, "understand"), 7:18; 8:17, 21 `[T]`.

**Tool 11.**

**Isa 29:13 → 7:6–7** *(high — formula quotation, "Isaiah prophesied")*. *Source context:* the "Ariel" oracle (Isa 29:1–24). Jerusalem is besieged; the prophets are blinded; the vision is a sealed book (29:10–12); the people honour God with their lips. The next verse promises that "the wisdom of their wise men shall perish" (29:14), and then that "the deaf shall hear … and the eyes of the blind shall see" (29:18) `[T]`. *Book usage:* Isaiah's third named or open use (1:2–3; 4:12). *OT-to-OT:* Isa 29:10–12's blindness and sealed book continues Isa 6:9–10, cited at 4:12. *What it adds:* the next two pericopes heal a deaf man (7:32–37) and a blind man (8:22–26) — the promise of Isa 29:18, which follows directly on the verse Jesus quotes *(moderate–high; synthetic)*.

**Exod 20:12 (Deut 5:16); Exod 21:17 (Swete 21:16) → 7:10** *(high)*. Move 1: the fifth commandment and its sanction. *Book usage:* the Decalogue returns at 10:19. *What it adds:* "Moses said" is set against "but you say" (7:10–11) — God's word against the tradition that makes it void.

*Internal:* **answers §6:52** — the bread theme continues (high). **Plants §7:24–30** — the children's bread (high). **Plants §8:17–21** — understanding (high). **Answers §1:40–44** — καθαρίζω (moderate). **Plants §10:19** — the commandments (moderate).

**Translations.** At 7:19c the NASB95 prints "(Thus He declared all foods clean.)" and the ESV "(Thus he declared all foods clean.)". Both supply "he declared", reading the participle as the narrator's comment. The Greek allows it and the construction probably requires it `[I]`, moderate. **Pulpit divergence:** none. 7:16 is absent from the ESV and bracketed in the NASB95.

**Difficulty.** 7:19c and the food laws. *Category:* doctrinal. *Function:* a narrator's aside drawing the consequence for his readers. See the Bible Timeline tool: Mark writes for a mixed or Gentile audience on the far side of the cross.

**Pitfall.** "Jesus attacks religious ritual." The target is tradition that voids God's command, and a heart far from God. It is not ritual as such. The corrective: preach 7:6–13 as a defence of God's word, and 7:20–23 as a diagnosis of the heart that no washing touches.

---

## 15. Mark 7:24–37 — Crumbs for the Dogs; the Deaf Hear

**Position.** *Q1:* defilement has been located in the heart, not in food (7:1–23). *Q2:* the next two scenes happen in Gentile territory — Tyre, then the Decapolis. The first is a Greek woman who asks for the children's bread, and the second a deaf man who is healed as Isaiah promised (7:37) `[T]`/`[I]`.

**Structure.** Tyre: the woman and her daughter (24–30). The Decapolis: the deaf man (31–37).

**Text-first findings.**

- **"Let the children first be fed."** Ἄφες πρῶτον χορτασθῆναι τὰ τέκνα (7:27). χορτάζω ("to feed to fullness") is the verb of both feedings: ἐχορτάσθησαν ("they were satisfied", 6:42; 8:8), and χορτάσαι ("to satisfy", 8:4) `[T]`, verified. **The saying about the children's bread stands between two feedings — the first on the Jewish side of the lake, the second after this Gentile journey.** *Synthetic*: moderate–high.
- **The only person in Mark to call Jesus κύριε ("Lord").** Κύριε (7:28) is the only vocative κύριε in Mark (SBLGNT, verified by parse) `[T]`. A Syrophoenician Greek woman is the one person who addresses him as Lord.
- **"For this word."** Διὰ τοῦτον τὸν λόγον ὕπαγε ("because of this word, go", 7:29). Her λόγος ("word") is the thing Jesus commends `[T]`.
- **The deaf man, from Isaiah.** μογιλάλον ("speaking with difficulty", 7:32) is a New Testament hapax, and in Swete the word occurs only at Isa 35:6 `[T]`, verified. The crowd's verdict — τοὺς κωφοὺς ποιεῖ ἀκούειν καὶ ἀλάλους λαλεῖν ("he makes the deaf hear and the mute speak", 7:37) — is Isa 35:5–6 in substance *(high)*. The healing is effected by a word, Εφφαθα ("Ephphatha"), glossed Διανοίχθητι ("be opened", 7:34), with the Aramaic kept `[T]`.
- **"He has done all things well."** Καλῶς πάντα πεποίηκεν (7:37). Gen 1:31 Swete: εἶδεν ὁ θεὸς τὰ πάντα ὅσα ἐποίησεν, καὶ ἰδοὺ καλὰ λίαν ("God saw all that he had made, and behold, it was very good") `[T]`. The shared words are πάντα ("all"), ποιέω ("to make") and καλ- ("good") *(moderate–uncertain; creation language at a healing)*.
- **Sighing and looking up.** ἀναβλέψας εἰς τὸν οὐρανὸν ἐστέναξεν ("looking up to heaven, he sighed", 7:34). He looked up to heaven at the feeding (6:41), and he sighs again at the Pharisees' demand for a sign, ἀναστενάξας (8:12) `[T]`.

**Tool 11.** **Isa 35:5–6 → 7:32, 37** *(high — hapax plus paraphrase)*. *Source context:* after the judgement of Edom (Isa 34), the wilderness blossoms and "your God will come … he will come and save you. Then the eyes of the blind shall be opened, and the ears of the deaf unstopped; then the lame shall leap like a deer, and the tongue of the mute sing for joy" (35:4–6). A highway called the Holy Way runs through the desert for the ransomed of the LORD (35:8–10) `[T]`. *Book usage:* Isaiah is live; this follows Isa 29:18 (see 7:6–7). *OT-to-OT:* Isa 35:5 and Isa 29:18 both promise the deaf hearing and the blind seeing; Isa 35:8's "way" (דֶּרֶךְ, "way") belongs with Isa 40:3's (דֶּרֶךְ verified at Isa 35:8 by lemma). *What it adds:* the crowd, without knowing it, says that God has come (Isa 35:4). The blind man follows at 8:22–26, and the Way section begins with the blind.

**Gen 1:31 → 7:37** *(uncertain)*. Move 1 only.

*Internal:* **answers §7:1–23** — the Gentile and the bread (high). **Plants §8:1–10** — the second feeding (high). **Plants §8:22–26** — the blind, Isa 35's other half (moderate–high). **Plants §8:12** — sighing (moderate).

**Translations.** At 7:24 the **ESV** reads "the region of Tyre and Sidon"; the SBLGNT and NA28 print Τύρου ("of Tyre") only, and the NASB95 "Tyre". The NA28 apparatus shows καὶ Σιδῶνος ("and Sidon") in א A B and the Majority text `[T]`, so the ESV's reading is well attested. At 7:28 the NASB95's "Yes, Lord" and the ESV's "Yes, Lord" add ναί ("yes"), read by א B and the Majority text; the SBLGNT and NA28 print Κύριε ("Lord") alone, with 𝔓⁴⁵ W Θ `[T]`, verified in the apparatus. **Pulpit divergence:** both are text-critical choices the congregation will not know about; nothing in the findings turns on either.

**Difficulty.** 7:27, "the dogs". *Category:* ethical/pastoral. *Function:* the saying sets an order ("first") and not a refusal, and the woman's answer takes up that order. The diminutive κυνάρια ("little dogs, house dogs") softens it `[T]`/`[I]`.

**Pitfall.** Preaching the woman's persistence as a technique ("keep asking and God will give in"). Jesus commends her *word* — that even crumbs from the Lord's table are enough. The corrective: preach her faith as a right reading of the "first", and as the Gentile inclusion the book is moving towards.

---

## 16. Mark 8:1–21 — Do You Not Yet Understand?

**Position.** *Q1:* Gentiles have been reached (7:24–37). *Q2:* a second feeding in the wilderness, then a demand for a sign, then a boat conversation in which the disciples' hardness is exposed by Jesus' own questions. This closes the third Galilean cycle with Οὔπω συνίετε; ("do you not yet understand?", 8:21) `[T]`.

**Structure.** The four thousand (1–10); the Pharisees seek a sign (11–13); the leaven and the loaves (14–21).

**Text-first findings.**

- **The same compassion.** Σπλαγχνίζομαι ἐπὶ τὸν ὄχλον ("I have compassion on the crowd", 8:2). This time Jesus says it himself; at 6:34 the narrator reported it `[T]`. σπλαγχνίζομαι ("to have compassion") occurs at 6:34, 8:2 and 9:22 in the SBLGNT, and at 1:41 too in NA28 `[T]`.
- **Twelve κόφινοι, seven σπυρίδες.** The baskets are different words — κόφινος ("basket", 6:43; 8:19) and σπυρίς ("large basket", 8:8, 20) — and Jesus' questions keep them distinct (8:19–20) `[T]`, verified. The numbers are asked for and answered, twelve and seven. That twelve evokes Israel and seven the nations is `[S]`/`[I]` *(uncertain; the text asks the disciples to remember the numbers, but does not interpret them)*.
- **No sign for this generation.** τί ἡ γενεὰ αὕτη ζητεῖ σημεῖον; … εἰ δοθήσεται τῇ γενεᾷ ταύτῃ σημεῖον ("why does this generation seek a sign? … if a sign will be given to this generation", 8:12). The εἰ is an oath formula, Hebraic in form (אִם, "if [it be so]"), meaning "no sign will be given" `[T]`/`[I]`, high. γενεά ("generation") recurs at 8:38 ("adulterous and sinful"), 9:19 ("faithless") and 13:30 `[T]`, verified. The sign they ask for is asked again at the cross: "let him come down now … that we may see and believe" (15:32) `[I]`.
- **Leaven of the Pharisees and of Herod.** 8:15. Herod was last seen killing John (6:14–29), and the Pharisees last seen seeking a sign (8:11). The two leavens unite the two alliances (3:6; 12:13) `[I]`, moderate.
- **The questions.** In seven questions Jesus uses the vocabulary of 4:12 and Isa 6:9–10: οὔπω νοεῖτε οὐδὲ συνίετε; πεπωρωμένην ἔχετε τὴν καρδίαν ὑμῶν; ὀφθαλμοὺς ἔχοντες οὐ βλέπετε καὶ ὦτα ἔχοντες οὐκ ἀκούετε; ("do you not yet perceive or understand? Do you have your heart hardened? Having eyes, do you not see, and having ears, do you not hear?", 8:17–18) `[T]`. **What was said of "those outside" (4:11–12) is now said to the Twelve.** νοέω ("to perceive") occurs three times in Mark: 7:18, 8:17, and 13:14, ὁ ἀναγινώσκων νοείτω ("let the reader perceive") `[T]`, verified. *The reader is asked to do what the disciples could not.*

**Tool 11.** **Jer 5:21; Ezek 12:2 (with Isa 6:9–10) → 8:18** *(high)*. *Source context:* Jer 5:21, "hear this, O foolish and senseless people, who have eyes but see not, who have ears but hear not", in an oracle against a people who do not fear the LORD who set the sea its bounds (5:22). Ezek 12:2, the rebellious house, just before the exile is acted out. *Book usage:* follows Isa 6:9–10 (4:12). *OT-to-OT:* both reuse Isaiah's commission (verified overlaps in Swete). *What it adds:* Jer 5:22 is about the LORD who bounds the sea, and the disciples have just crossed a sea twice without understanding who commands it *(moderate — context of the source, not a verbal link)*.

*Internal:* **answers §4:12** — insiders spoken to as outsiders (high). **Closes the cycle** — πωρόω (3:5; 6:52; 8:17) (high, verified). **Plants §13:14** — νοέω (moderate–high, verified). **Plants §15:32** — the sign demanded (moderate). **Answers §6:34 and plants §14:22–23** — the feeding verbs (high).

**Translations.** At 8:12 the NASB95's "no sign will be given" and the ESV's "no sign will be given" both resolve the oath. **Pulpit divergence:** none.

**Pitfall.** Allegorising the numbers (twelve tribes, seven nations, five books of Moses). The text asks the disciples to *remember*, and the point of the memory is who has fed them, not what the numbers mean. The corrective: keep the numbers as memory-prompts for Jesus' sufficiency.

---

## 17. Mark 8:22–9:1 — You Are the Christ; the Son of Man Must Suffer ⭐

**Position.** *Q1:* the disciples have been accused of eyes that do not see (8:18). *Q2:* a blind man is healed in two stages, and then Peter "sees" — Σὺ εἶ ὁ χριστός ("You are the Christ") — but only halfway, since he rebukes the suffering at once. **This is the book's hinge** (see the overview's arc map). The identity question asked since 1:27 is answered, and the second half's question, what kind of Christ, begins with δεῖ ("must", 8:31) `[T]`/`[I]`.

**Structure.**

| Verses | Section |
|---|---|
| 8:22–26 | The blind man at Bethsaida, healed in two touches |
| 8:27–30 | On the way: "Who do people say I am?" — "You are the Christ" — silence |
| 8:31–33 | The first passion prediction; Peter rebukes; "Get behind me, Satan" |
| 8:34–9:1 | To the crowd and the disciples: self-denial, the cross, the soul, shame, the kingdom in power |

**Text-first findings.**

- **A two-stage healing.** The man sees "men like trees walking" (8:24) and then, after a second laying on of hands, διέβλεψεν καὶ ἀπεκατέστη καὶ ἐνέβλεπεν τηλαυγῶς ἅπαντα ("he saw clearly and was restored and saw everything distinctly", 8:25) `[T]`. It is the only healing in the Gospels that takes two stages `[S]`. Placed between "do you not see?" (8:18) and Peter's half-sight (8:29–33), it enacts the disciples' condition `[I]`, high.
- **Spittle.** πτύσας εἰς τὰ ὄμματα αὐτοῦ ("having spat on his eyes", 8:23; compare 7:33). πτύω ("to spit") is Jesus' healing gesture at 7:33 and 8:23. ἐμπτύω ("to spit on") is what is done to him, predicted at 10:34 and done at 14:65 and 15:19 `[T]`, verified. *Moderate*: the book uses one root for the healing touch he gives and the contempt he receives.
- **The answer to the book's question.** The disciples' report — John, Elijah, one of the prophets (8:28) — repeats word for word the opinions around Herod (6:14–15) `[T]`. Peter's Σὺ εἶ ὁ χριστός ("You are the Christ", 8:29) is the first human confession of the title in the narrative `[T]`. Χριστός ("Christ") occurs in 7 verses: 1:1; 8:29; 9:41; 12:35; 13:21; 14:61; 15:32 (verified).
- **ἐπιτιμάω ("to rebuke") three times in four verses.** Jesus ἐπετίμησεν αὐτοῖς ("warned them", 8:30); Peter ἤρξατο ἐπιτιμᾶν αὐτῷ ("began to rebuke him", 8:32); Jesus ἐπετίμησεν Πέτρῳ ("rebuked Peter", 8:33) `[T]`. The verb of the exorcisms (1:25; 3:12; 9:25) and the storm (4:39) is used of Peter, and "Satan" is the word Jesus speaks to him `[T]`.
- **"Plainly."** παρρησίᾳ τὸν λόγον ἐλάλει ("he was speaking the word plainly", 8:32). παρρησία ("plainness, openness") occurs only here in Mark `[T]`, verified. After chapters of parables and silence, the passion is the first thing said openly.
- **The necessity and the rejection.** δεῖ … ἀποδοκιμασθῆναι ("must … be rejected", 8:31). The verb is Ps 118:22's (ἀπεδοκίμασαν, "they rejected", cited at 12:10), and the only two Markan uses are these `[T]`, verified.
- **The first cross is the disciple's.** ἀράτω τὸν σταυρὸν αὐτοῦ ("let him take up his cross", 8:34) is the first use of σταυρός ("cross") in Mark. The next three are Simon of Cyrene's (15:21), the passers-by's (15:30) and the priests' (15:32) `[T]`, verified. **The only man in the book who literally takes up (ἄρῃ) Jesus' cross is a passer-by pressed into it (15:21, ἵνα ἄρῃ τὸν σταυρὸν αὐτοῦ, "so that he might carry his cross").** The verb and object are the same `[T]`. *Synthetic*: moderate–high.
- **ψυχή ("life, soul") four times in three verses** (8:35–37), then 10:45 and 14:34 `[T]`. "What will a man give ἀντάλλαγμα τῆς ψυχῆς αὐτοῦ ("in exchange for his soul")?" (8:37) — and at 10:45 the Son of Man gives τὴν ψυχὴν αὐτοῦ λύτρον ("his soul as a ransom"). Ps 49:8–9 (Swete 48:8–9): no man can give God a ransom (λύτρωσις, "redemption") for his soul `[T]` *(moderate)*.

**Tool 11.**

**Ps 118:22 → 8:31** *(moderate–high — rare verb, cited openly at 12:10)*. See unit 26 for the full triad. *What it adds here:* the first passion prediction already speaks in the psalm's words.

**Dan 7:13–14 (with Zech 14:5) → 8:38** *(moderate–high)*. *Source context:* see unit 4. Zech 14:5 Swete: ἥξει Κύριος ὁ θεός μου, καὶ πάντες οἱ ἅγιοι μετ' αὐτοῦ ("the Lord my God will come, and all the holy ones with him") `[T]`. *Book usage:* the Son of Man's coming (Dan 7) returns at 13:26 and 14:62; Zechariah 14 is live (the Mount of Olives, 11:1; 13:3; 14:26). *OT-to-OT:* Dan 7 and Zech 14 both describe a coming of God, or his agent, with a heavenly retinue. *What it adds:* the suffering Son of Man and the coming Son of Man are one person, in one paragraph.

**Ps 49:8–9 → 8:37** *(moderate)*. Move 1: a wisdom psalm on the folly of trusting wealth, since no one can ransom a life. *What it adds:* it plants the question that 10:45 answers.

*Internal:* **answers §1:27; 2:7; 4:41; 6:2–3, 14–16** — the identity question (high). **Answers §6:14–15** — the same three opinions (high, verbal). **Plants §10:45** — ψυχή and ransom (moderate–high). **Plants §15:21** — the cross carried (moderate–high). **Plants §14:65; 15:19** — spitting (moderate). **Plants §12:10** — the rejected stone (high). **Answers §1:17** — ὀπίσω μου (high, verified).

**Translations.** At 8:25 the ESV's "he opened his eyes" renders διέβλεψεν ("he saw clearly"), which the NASB95 gives as "he looked intently". Neither is exact. At 8:34 the NASB95's "come after Me" and the ESV's "come after me" render ὀπίσω μου ἐλθεῖν ("to come behind me"). At 8:33 both have "Get behind me", so the link between the two verses is kept in both. **Pulpit divergence:** none bearing.

**Pitfall.** Preaching "take up your cross" as bearing life's burdens (an illness, a difficult relative). In context the cross is death with Jesus, "for my sake and the gospel's" (8:35). The corrective: preach it as following the one who must be killed, and hear it as Mark's first readers, under persecution (see the overview), would have heard it.

---

## 18. Mark 9:2–13 — Transfigured; Elijah Has Come ⭐

**Position.** *Q1:* the passion has just been announced, and discipleship defined as losing one's life (8:31–38), with a promise that some would see the kingdom come in power (9:1). *Q2:* six days later three disciples see the Son's glory. The Voice repeats the baptism's word to them, and the conversation on the way down ties the glory to the suffering. The book's middle disclosure (see the overview's arc map) stands between the first and third passion predictions `[T]`/`[I]`.

**Structure.** The ascent and the transfiguration (2–4); Peter's proposal (5–6); the cloud and the Voice (7); Jesus alone (8); the descent: silence until the resurrection (9–10); the Elijah question (11–13).

**Text-first findings.**

- **Sinai in every detail.** μετὰ ἡμέρας ἕξ ("after six days"; the cloud covers Sinai for six days, Exod 24:16), a high mountain, garments dazzling, νεφέλη ἐπισκιάζουσα ("a cloud overshadowing", 9:7) — Swete Exod 40:29 (Heb 40:35): ἐπεσκίαζεν ἐπ' αὐτὴν ἡ νεφέλη ("the cloud overshadowed it"), of the tabernacle filled with glory, which Moses could not enter `[T]`, verified in Swete. Peter proposes three σκηνάς ("tents, tabernacles", 9:5). And ἔκφοβοι ("terrified", 9:6) is Moses' own word at Sinai in Deut 9:19 (ἔκφοβός εἰμι, "I am terrified"). The adjective occurs in the Greek Bible only there, at Wis 17:19, at 1 Macc 13:2, here, and at Heb 12:21, which quotes Deut 9:19 `[T]`, verified. *Synthetic*: high.
- **The Voice to the disciples.** Οὗτός ἐστιν ὁ υἱός μου ὁ ἀγαπητός, ἀκούετε αὐτοῦ ("This is my beloved Son; hear him", 9:7). At 1:11 the Voice spoke *to* Jesus (Σὺ εἶ, "you are"); here it speaks *about* him to the three `[T]`. ἀκούετε αὐτοῦ ("hear him") is Deut 18:15's αὐτοῦ ἀκούσεσθε ("him you shall hear"), of the prophet like Moses `[T]` *(moderate–high)*. It picks up Ἀκούετε ("Listen!") of the parables (4:3) and looks ahead to Ἄκουε, Ἰσραήλ ("Hear, O Israel", 12:29).
- **"Jesus only."** οὐκέτι οὐδένα εἶδον ἀλλὰ τὸν Ἰησοῦν μόνον ("they saw no one any more, but Jesus only", 9:8) `[T]`. Moses and Elijah withdraw, and the one to be heard remains.
- **The silence has an end date.** "Tell no one … except when the Son of Man has risen from the dead" (9:9) `[T]`. The one command to silence with a stated limit governs the rest (see the overview's Trap 1).
- **Elijah has come, and suffered "as it is written of him".** The scribes say Elijah δεῖ ἐλθεῖν πρῶτον ("must come first", 9:11; Mal 3:23). Jesus agrees that he restores (ἀποκαθιστάνει, "restores" — the verb of Mal 3:23 Swete 4:5, ἀποκαταστήσει, and of the healed hand and the healed eyes, 3:5; 8:25) `[T]`, verified. He adds two things. The Son of Man must suffer and ἐξουδενηθῇ ("be treated with contempt"), "as it is written" (9:12). And Elijah ἐλήλυθεν ("has come"), and "they did to him whatever they wished" (9:13) — that is, John `[I]`, high.

**Tool 11.**

**Exod 24:15–18; 40:34–35 (Swete 40:29); Deut 9:19 → 9:2–7** *(high — the pattern with distinctive words: ἓξ ἡμέρας ("six days"), ἐπισκιάζω ("to overshadow"), νεφέλη ("cloud"), σκηνή ("tent"), ἔκφοβος ("terrified"))*. *Source context:* Moses ascends Sinai, the glory covers the mountain six days, and on the seventh the LORD calls him out of the cloud (Exod 24:16). At the completion of the tabernacle the cloud covers it and the glory fills it, "and Moses was not able to enter" (40:35). Deut 9:19: Moses, fearing the LORD's wrath after the golden calf, prays for forty days. *Book usage:* Exodus is live (1:2; 7:10; 12:26; 14:24). *OT-to-OT:* the tabernacle is Sinai made portable, so the two Exodus texts are one pattern `[I]`. *What it adds:* the disciples stand where Moses stood, and hear the voice from the cloud say "hear him". The Deut 9:19 echo imports the context of the golden calf, and the next scene (9:14–29) is a descent into a faithless crowd (see below).

**Deut 18:15 → 9:7** *(moderate–high)*. *Source context:* Moses promises a prophet like himself, whom Israel must hear, since at Horeb they could not bear to hear God's voice directly (18:16). *Book usage:* first use. *OT-to-OT:* the prophet like Moses and the Sinai theophany belong together in Deut 18:16. *What it adds:* the one Israel must hear is the Son; Moses himself is present to see it.

**Ps 2:7 → 9:7** — see unit 1. *Book usage:* second use (1:11); the Son declared a second time.

**Mal 3:23–24 (Swete 4:4–5) → 9:11–12** *(high)*. *Source context:* see the overview; the last words of the Prophets. *Book usage:* Malachi at 1:2, now completed. *OT-to-OT:* Sir 48:10 reads the same text of Elijah's return `[S]`. *What it adds:* Elijah has come and been killed, so the forerunner's fate is written before the Son's.

**Ps 22:7 / Isa 53:3 → 9:12** *(uncertain)*. ἐξουδενηθῇ ("be treated with contempt"): Ps 21:7 Swete has ἐξουδένημα λαοῦ ("despised by the people"); Isa 53:3 Swete has ἄτιμον ("dishonoured"), not the verb.

*Internal:* **answers §1:11** — the Voice again (high). **Answers §9:1** — the kingdom seen in power, as a foretaste (moderate). **Plants §16:5** — λευκός ("white") (moderate). **Plants §14:33** — the same three (high). **Answers §6:14–29** — John as Elijah (high). **Plants §14:62; 16:6** — the Son of Man's resurrection (high).

**Translations.** NASB95 "tabernacles"; ESV "tents" (9:5). The NASB95's word keeps the tabernacle link with Exod 40:29 Swete (σκηνή, "tent, tabernacle"). NASB95 "listen to Him"; ESV "listen to him" (9:7). The Deut 18:15 echo survives in both. **Pulpit divergence:** the ESV's "tents" makes the Sinai–tabernacle pattern harder to hear. A word of explanation from the pulpit restores it.

**Pitfall.** "Mountain-top experiences": preaching the transfiguration as a model of spiritual highs. The text immediately takes the disciples down the mountain, into talk of suffering and a faithless crowd. The corrective: preach the Voice's command, "hear him" — and what he has just said is 8:31–38.

---

## 19. Mark 9:14–29 — "I Believe; Help My Unbelief"

**Position.** *Q1:* on the mountain the disciples saw glory and heard "hear him" (9:2–8). *Q2:* at the foot of the mountain they find a crowd, arguing scribes, and disciples who could not cast out a spirit. **This is the Sinai pattern completed.** Moses came down from the cloud and the glory into a camp in disorder (Exod 32), and the Son comes down from the cloud into a "faithless generation" `[I]`, moderate — the adjacency and narrative-pattern check of Tool 11, run because the ascent frame has just been established.

**Structure.** The scene below (14–18); the lament over the generation (19); the father's plea and Jesus' reply (20–24); the exorcism, "like a corpse", raised (25–27); in the house: "only by prayer" (28–29).

**Text-first findings.**

- **"Faithless generation."** Ὦ γενεὰ ἄπιστος, ἕως πότε … ("O faithless generation, how long …", 9:19). Deut 32:20 Swete: γενεὰ ἐξεστραμμένη ἐστίν, υἱοὶ οἷς οὐκ ἔστιν πίστις ἐν αὐτοῖς ("it is a perverse generation, sons in whom there is no faith"), in the Song of Moses `[T]`, verified in Swete *(moderate–high)*. Num 14:27, ἕως τίνος ("how long?"), is the LORD's complaint in the wilderness *(uncertain on wording)*.
- **"All things are possible."** πάντα δυνατὰ τῷ πιστεύοντι ("all things are possible to the one who believes", 9:23). The same phrase returns at 10:27, πάντα γὰρ δυνατὰ παρὰ τῷ θεῷ ("for all things are possible with God"), and at 14:36, Αββα ὁ πατήρ, πάντα δυνατά σοι ("Abba, Father, all things are possible for you") `[T]`, verified. **In Gethsemane the Son prays to the God for whom all is possible, and the cup is not removed.** *Synthetic*: moderate–high.
- **The father's cry.** Πιστεύω· βοήθει μου τῇ ἀπιστίᾳ ("I believe; help my unbelief", 9:24) `[T]`. ἀπιστία ("unbelief") recurs from 6:6, and the father's honesty stands against the generation's faithlessness `[I]`.
- **A second resurrection scene.** ἐγένετο ὡσεὶ νεκρὸς ὥστε τοὺς πολλοὺς λέγειν ὅτι ἀπέθανεν. ὁ δὲ Ἰησοῦς κρατήσας τῆς χειρὸς αὐτοῦ ἤγειρεν αὐτόν, καὶ ἀνέστη ("he became like a corpse, so that most said, 'He is dead.' But Jesus, taking him by the hand, raised him, and he arose", 9:26–27) `[T]`. ἐγείρω ("to raise") and ἀνίστημι ("to rise") come together in one verse, just after the descent in which "rising from the dead" was puzzled over (9:9–10) `[T]`/`[I]`.
- **Prayer.** Τοῦτο τὸ γένος ἐν οὐδενὶ δύναται ἐξελθεῖν εἰ μὴ ἐν προσευχῇ ("this kind can come out by nothing except by prayer", 9:29). προσευχή ("prayer") occurs only here and at 11:17, "a house of προσευχῆς for all the nations" `[T]`, verified. "And fasting" is absent from the SBLGNT, NA28, the NASB95 and the ESV (see the textual-variants catalogue).

**Tool 11.** **Exod 32:15–24 → 9:14–19** *(moderate — narrative pattern, established by the adjacent Sinai frame)*. *Source context:* Moses descends from the mountain with the tablets, finds the calf and the people "let loose", and asks Aaron, "What did this people do to you?" *Book usage:* Exodus 24 and 40 have just been used (9:2–7). *OT-to-OT:* Deut 9:19 (ἔκφοβος, "terrified", at 9:6) is Moses' retelling of this very episode, so the two scenes are joined in Deuteronomy's own memory `[T]`, verified. *What it adds:* the lament "how long must I bear with you?" is a mediator's, like Moses', and the disciples who "could not" (οὐκ ἴσχυσαν, 9:18) take Aaron's place *(moderate)*.

**Deut 32:20 → 9:19** *(moderate–high)*. Move 1: the Song of Moses' indictment of a faithless generation, followed by the LORD's jealousy, judgement and vindication of his people (32:36–43).

*Internal:* **answers §9:9–10** — "rising from the dead", enacted (moderate). **Plants §10:27; §14:36** — "all things possible" (moderate–high, verified). **Plants §11:17** — προσευχή (moderate). **Answers §6:6** — ἀπιστία (moderate). **Plants §14:33; §16:5** — ἐκθαμβέομαι ("to be astonished") is first used here of the crowd (9:15), then of Jesus (14:33) and the women (16:5–6) (moderate).

**Translations.** At 9:23 the ESV's "'If you can'! All things are possible for one who believes" and the NASB95's "'If You can?' All things are possible to him who believes" both render the article τό, which marks the father's words as a quotation. **Pulpit divergence:** none.

**Pitfall.** "The disciples failed because they did not pray hard enough." Jesus' answer names prayer, which is dependence, not a technique — and the father's "help my unbelief" is the prayer the passage models. The corrective: preach 9:24 as the prayer, and 9:29 as its warrant.

---

## 20. Mark 9:30–50 — The Greatest and the Least

**Position.** *Q1:* the second passion prediction is given privately in Galilee (9:30–31). *Q2:* the unit follows the pattern set at 8:31–38 — prediction, misunderstanding, teaching — and the teaching here is about status and stumbling within the community `[T]`.

**Structure.** The prediction and the incomprehension (30–32); "who is greatest" and the child (33–37); the stranger exorcist (38–41); stumbling, hell, and salt (42–50).

**Text-first findings.**

- **"Into the hands of men."** παραδίδοται εἰς χεῖρας ἀνθρώπων ("is handed over into the hands of men", 9:31). At 14:41 it becomes εἰς τὰς χεῖρας τῶν ἁμαρτωλῶν ("into the hands of sinners") `[T]`, verified. These are the only two "into [the] hands" sayings.
- **They did not understand, and were afraid to ask.** ἠγνόουν τὸ ῥῆμα, καὶ ἐφοβοῦντο αὐτὸν ἐπερωτῆσαι ("they did not understand the saying, and they were afraid to ask him", 9:32) `[T]`. ῥῆμα ("saying") recurs only at 14:72, where Peter remembers τὸ ῥῆμα `[T]`, verified.
- **"On the way" they argued about greatness.** ἐν τῇ ὁδῷ ("on the way", 9:33, 34) `[T]`.
- **First and last, servant.** πρῶτος … ἔσχατος … διάκονος ("first … last … servant", 9:35) is picked up at 10:31 and 10:43–44 `[T]`. Jesus takes a child ἐναγκαλισάμενος ("taking him in his arms", 9:36). ἐναγκαλίζομαι ("to take in one's arms") occurs only here and at 10:16 `[T]`, verified.
- **"In my name."** ἐπὶ τῷ ὀνόματί μου / ἐν τῷ ὀνόματί σου ("in my name / your name", 9:37, 38, 39) and ἐν ὀνόματι ὅτι Χριστοῦ ἐστε ("in the name that you are Christ's", 9:41) `[T]`.
- **Stumbling, four times.** σκανδαλίζω ("to cause to stumble", 9:42, 43, 45, 47) `[T]`. The same verb is used of the Twelve's falling away (14:27, 29).
- **The last verse of Isaiah.** ὅπου ὁ σκώληξ αὐτῶν οὐ τελευτᾷ καὶ τὸ πῦρ οὐ σβέννυται ("where their worm does not die and the fire is not quenched", 9:48) `[T]`. 9:44 and 9:46, which repeat it, are absent from the SBLGNT and bracketed by the NASB95.
- **Salted with fire.** Πᾶς γὰρ πυρὶ ἁλισθήσεται ("for everyone will be salted with fire", 9:49). Lev 2:13 Swete: πᾶν δῶρον θυσίας ὑμῶν ἁλὶ ἁλισθήσεται … ἅλα διαθήκης ("every offering of your sacrifice shall be salted with salt … the salt of the covenant") `[T]`, verified in Swete. The verb ἁλισθήσεται ("will be salted") is shared *(moderate–high)*. The disciple as a sacrifice salted by fire `[I]`, moderate.

**Tool 11.** **Isa 66:24 → 9:48** *(high)*. *Source context:* the last verse of Isaiah. After new heavens and new earth and all flesh coming to worship (66:22–23), the worshippers go out and see "the corpses of the men who rebelled against me", whose worm does not die. *Book usage:* Isaiah is live and frames the book; the first citation is Isa 40:3, and this is the book's end. *OT-to-OT:* Isa 66:24 closes the book that Isa 40:3 opened the second half of. *What it adds:* the warning carries Isaiah's final contrast — worship or ruin — and it is spoken to disciples.

**Lev 2:13 → 9:49** *(moderate–high)*. Move 1: the grain offering must be salted, "the salt of the covenant of your God".

*Internal:* **plants §14:41** — "into the hands" (high, verified). **Plants §14:72** — ῥῆμα (moderate). **Plants §10:16** — ἐναγκαλίζομαι (moderate). **Plants §10:31, 43–44** — first/last, servant (high). **Plants §14:27, 29** — σκανδαλίζω (moderate).

**Translations.** At 9:42–47 the NASB95's "stumble" and the ESV's "sin" render σκανδαλίζω. The NASB95 keeps the link to 14:27 ("fall away" in both); the ESV's "sin" loses the image. **Pulpit divergence:** the ESV's "causes you to sin" is interpretive. The congregation will not hear that this is the verb of 4:17 and 14:27.

**Pitfall.** Literal self-mutilation, or the opposite — reducing 9:43–48 to a metaphor with no threat in it. The text uses hyperbole to press a real alternative, "life" or "Gehenna". The corrective: preach the urgency and keep the Isaianic end in view.

---

## 21. Mark 10:1–16 — From the Beginning of Creation; the Children

**Position.** *Q1:* the disciples have been told to receive children and not to cause stumbling (9:36–42). *Q2:* the journey now enters Judaea (10:1). The first test is about marriage, and the answer appeals beyond Moses' concession to "the beginning of creation". Then the children come, and the disciples, who were told to receive one, rebuke them (10:13) `[T]`.

**Structure.** The test (2–9); in the house (10–12); the children (13–16).

**Text-first findings.**

- **"Testing him."** πειράζοντες αὐτόν ("testing him", 10:2). πειράζω ("to test") is Satan's verb (1:13), and the Pharisees' (8:11; 10:2; 12:15) `[T]`, verified.
- **Moses' concession, and "the beginning".** Πρὸς τὴν σκληροκαρδίαν ὑμῶν ("because of your hardness of heart", 10:5). σκληροκαρδία ("hardness of heart") occurs only here and in the longer ending (16:14). ἀπὸ δὲ ἀρχῆς κτίσεως ("but from the beginning of creation", 10:6) — the phrase ἀρχῆς κτίσεως ("beginning of creation") returns at 13:19, ἀπ' ἀρχῆς κτίσεως ἣν ἔκτισεν ὁ θεός ("from the beginning of the creation which God created") `[T]`, verified. ἀρχή ("beginning") occurs four times in Mark: 1:1; 10:6; 13:8, 19.
- **What God joined.** ὃ οὖν ὁ θεὸς συνέζευξεν ἄνθρωπος μὴ χωριζέτω ("what therefore God has joined, let not man separate", 10:9) `[T]`.
- **The woman may divorce too.** ἐὰν αὐτὴ ἀπολύσασα τὸν ἄνδρα αὐτῆς ("if she divorces her husband", 10:12). Only Mark addresses this `[T]`, and it was possible under Roman law but not under Jewish law `[S]` — which fits the overview's Roman-audience inference `[I]`, moderate.
- **Jesus indignant.** ἠγανάκτησεν ("he was indignant", 10:14). ἀγανακτέω ("to be indignant") occurs at 10:14 (Jesus, at the disciples), 10:41 (the ten, at James and John) and 14:4 (some, at the anointing woman) `[T]`, verified. Jesus' indignation is for the children; the other two are about status and money.
- **"Receive the kingdom as a child."** ὡς παιδίον ("as a child", 10:15). The disciples were told to receive a child (9:37); now they must receive the kingdom as one `[T]`.

**Tool 11.** **Gen 1:27 + 2:24 → 10:6–8** *(high — verbatim with the LXX)*. *Source context:* the creation of humanity as male and female in God's image (Gen 1), and the first marriage, "for this reason a man shall leave …", which is the narrator's comment on Adam's delighted recognition (Gen 2:23–24). *Book usage:* first use of Genesis 1–2. *OT-to-OT:* Deut 24:1 (cited by the Pharisees, 10:4) is Torah read against Torah; Jesus reads Deuteronomy's concession by Genesis' design. *What it adds:* creation, not concession, defines marriage. The same "beginning of creation" is the horizon of the tribulation discourse (13:19).

**Deut 24:1 → 10:4** *(high)*. Move 1: a regulation that assumes divorce and restricts remarriage; it does not command divorce.

*Internal:* **plants §13:19** — ἀρχῆς κτίσεως (moderate–high, verified). **Answers §9:36–37** — the child (high). **Plants §10:41; §14:4** — ἀγανακτέω (moderate). **Plants §16:14 (longer ending)** — σκληροκαρδία is borrowed by the later ending (moderate).

**Translations.** NASB95 "hardness of heart"; ESV "hardness of heart". **Pulpit divergence:** none.

**Difficulty.** Divorce and remarriage. *Category:* ethical/pastoral — a landmine. *Function in context:* a test answered from creation. Mark's form has no exception clause, unlike Matt 19:9 `[T]` (Matthew in the SBLGNT). Pastorally, preach the design before the ruling, and deal with the divorced in the congregation with the gospel of 10:45 in view.

**Pitfall.** Preaching 10:13–16 as "childlike innocence". The point is the child's dependence and lack of status in a unit about greatness (9:33–37; 10:35–45). The corrective: to receive the kingdom as a child is to receive it as someone with no claim.

---

## 22. Mark 10:17–31 — One Thing You Lack

**Position.** *Q1:* the kingdom must be received like a child, with no claim (10:15). *Q2:* immediately a man with every claim — commandments kept, great possessions — asks how to inherit eternal life, and cannot let go `[T]`/`[I]`.

**Structure.** The man and Jesus (17–22); wealth and the kingdom, "who can be saved?" (23–27); Peter's "we have left everything" and the hundredfold (28–31).

**Text-first findings.**

- **He kneels, like the leper.** γονυπετήσας ("kneeling", 10:17). γονυπετέω ("to kneel") occurs only at 1:40 and 10:17 `[T]`, verified. The leper was cleansed; this man goes away grieving.
- **"No one is good but God alone."** οὐδεὶς ἀγαθὸς εἰ μὴ εἷς ὁ θεός (10:18) — the premise of 2:7 again, in Jesus' own mouth `[T]`. Jesus does not deny that he is good; he asks what the man means by it `[I]`.
- **The commandments, with one substitution.** Murder, adultery, theft, false witness, honour of parents — and μὴ ἀποστερήσῃς ("do not defraud", 10:19) in place of the tenth commandment `[T]`. Coveting is replaced by defrauding, which a rich man might do `[I]`, moderate. ψευδομαρτυρέω ("to bear false witness") recurs at 14:56–57, where the court breaks this commandment at the trial `[T]`, verified.
- **The only time Jesus is said to love someone.** ἐμβλέψας αὐτῷ ἠγάπησεν αὐτόν ("looking at him, he loved him", 10:21). ἀγαπάω ("to love") occurs in Mark only here and in the great commandment (12:30, 31, 33) `[T]`, verified.
- **"All things are possible with God."** 10:27 (see unit 19). Gen 18:14 Swete, μὴ ἀδυνατεῖ παρὰ τῷ θεῷ ῥῆμα ("is anything impossible with God?"), and Job 42:2, πάντα δύνασαι ("you can do all things") *(moderate)*.
- **The hundredfold.** ἑκατονταπλασίονα ("a hundred times as much", 10:30) echoes the harvest ἓν ἑκατόν ("a hundredfold", 4:8, 20), and adds μετὰ διωγμῶν ("with persecutions") `[T]`. The rocky ground fell away "when persecution arises" (4:17), and here persecution is part of the reward `[I]`.

**Tool 11.** **Exod 20:12–16; Deut 5:16–20 → 10:19** *(high)*. *Source context:* the Decalogue's second table. *Book usage:* Exod 20:12 was used at 7:10. *OT-to-OT:* Deut 24:14–15 (not withholding a labourer's wages) may lie behind "do not defraud" `[S]` *(uncertain on wording)*. *What it adds:* the man has kept the table that concerns neighbours, and he cannot keep the first commandment — no other gods — as his possessions show `[I]`.

**Gen 18:14 → 10:27** *(moderate)*. Move 1: Sarah's laughter and the promise of a son against impossibility.

*Internal:* **answers §1:40** — kneeling (moderate). **Answers §2:7** — God alone (moderate–high). **Plants §12:30–33** — ἀγαπάω (moderate). **Answers §4:8, 17, 20** — the hundredfold and persecution (moderate–high). **Plants §14:56–57** — false witness (moderate, verified). **Answers §1:18, 20** — leaving (high).

**Translations.** At 10:22 the NASB95's "saddened" and the ESV's "disheartened" render στυγνάσας ("gloomy, his face fell"). **Pulpit divergence:** none.

**Pitfall.** "Jesus tells everyone to sell everything", or the opposite, "this was only for him". The command is particular; the diagnosis is universal ("how hard it is to enter", 10:24). The corrective: preach 10:27 as the answer — salvation is impossible with man and possible with God.

---

## 23. Mark 10:32–45 — A Ransom for Many ⭐

**Position.** *Q1:* the question "who can be saved?" (10:26) has been answered with "with God all things are possible" (10:27). *Q2:* the third, most detailed passion prediction follows, then the most self-serving request in the book, and then the saying that explains how God does the impossible: the Son of Man gives his life λύτρον ἀντὶ πολλῶν ("as a ransom for many", 10:45). The Way section's teaching climaxes here `[T]`/`[I]`.

**Structure.** On the road, going up, Jesus ahead, the disciples afraid (32); the third prediction (33–34); James and John's request (35–40); the ten's indignation and the teaching on rule and service (41–44); the ransom saying (45).

**Text-first findings.**

- **Jesus goes ahead.** ἦν προάγων αὐτοὺς ὁ Ἰησοῦς ("Jesus was going ahead of them", 10:32). προάγω ("to go ahead") returns at 14:28 and 16:7, where he goes ahead of them to Galilee `[T]`, verified. They ἐθαμβοῦντο ("were amazed") and ἐφοβοῦντο ("were afraid").
- **The prediction is the passion's table of contents.** παραδοθήσεται … κατακρινοῦσιν … παραδώσουσιν τοῖς ἔθνεσιν … ἐμπαίξουσιν … ἐμπτύσουσιν … μαστιγώσουσιν … ἀποκτενοῦσιν … ἀναστήσεται ("he will be handed over … they will condemn … hand him over to the Gentiles … mock … spit … flog … kill … he will rise", 10:33–34) `[T]`. Each step is narrated with the same verb or its equivalent: κατέκριναν ("condemned", 14:64); παρέδωκαν Πιλάτῳ ("handed him over to Pilate", 15:1); ἐμπτύειν / ἐνέπτυον ("to spit on", 14:65; 15:19); φραγελλώσας ("having flogged", 15:15 — a Latin loanword where the prediction had the Greek μαστιγόω); ἐνέπαιξαν / ἐμπαίζοντες ("mocked", 15:20, 31) `[T]`, each verified by lemma. κατακρίνω ("to condemn") occurs only at 10:33 and 14:64 in 1:1–16:8, and ἐμπαίζω ("to mock") only at 10:34, 15:20 and 15:31. *Synthetic, verified*: high.
- **"In your glory", on your right and left.** ἐκ δεξιῶν … ἐξ ἀριστερῶν / ἐξ εὐωνύμων ("on the right … on the left", 10:37, 40), answered at 15:27 by two robbers (see the overview's echo table; εὐώνυμος ("left") only at 10:40 and 15:27, verified) `[T]`.
- **The cup and the baptism.** τὸ ποτήριον ὃ ἐγὼ πίνω ("the cup that I drink"); τὸ βάπτισμα ὃ ἐγὼ βαπτίζομαι ("the baptism with which I am baptised", 10:38–39) `[T]`. The cup is the Supper's cup (14:23) and the cup of Gethsemane (14:36). The baptism is not named again, but it gives meaning to 1:9 in retrospect `[I]`.
- **Gentile rulers.** οἱ δοκοῦντες ἄρχειν τῶν ἐθνῶν κατακυριεύουσιν … κατεξουσιάζουσιν ("those who seem to rule the nations lord it over … exercise authority over", 10:42) `[T]`. οἱ δοκοῦντες ("those who seem") is ironic: they only seem to rule `[I]`.
- **The ransom.** καὶ γὰρ ὁ υἱὸς τοῦ ἀνθρώπου οὐκ ἦλθεν διακονηθῆναι ἀλλὰ διακονῆσαι καὶ δοῦναι τὴν ψυχὴν αὐτοῦ λύτρον ἀντὶ πολλῶν ("for even the Son of Man did not come to be served but to serve, and to give his life as a ransom for many", 10:45). λύτρον ("ransom") and ἀντί ("in place of") each occur once in Mark `[T]`, verified. πολλῶν ("many") returns in the cup saying, ὑπὲρ πολλῶν ("for many", 14:24) `[T]`.

**Tool 11.**

**Isa 53:10–12 → 10:45** *(moderate — conceptual plus "many"; no λύτρον in the Greek Isaiah)*. *Source context:* the fourth Servant song's close. The LORD makes the Servant's soul an אָשָׁם ("guilt offering", 53:10); he bears the sin of רַבִּים ("many", 53:11, 12); he pours out his soul to death and is numbered with the transgressors (53:12) `[T]`, רַבִּים verified by lemma at 53:11–12. Swete 53:12: παρεδόθη εἰς θάνατον ἡ ψυχὴ αὐτοῦ ("his soul was handed over to death") — ψυχή ("soul") and παραδίδωμι ("to hand over"), the book's own words `[T]`. *Book usage:* Isa 42:1 at 1:11; Isa 53:7 behind the silences (14:61; 15:5); Isa 50:6 behind the spitting (14:65; 15:19). *OT-to-OT:* Isa 53 and Dan 7 are brought together in this verse — see the next item. *What it adds:* the Son of Man, who in Daniel receives service, gives his soul as the Servant does, for many.

**Dan 7:14 → 10:45** *(moderate)*. *Source context:* the one like a son of man receives dominion, and all peoples δουλεύουσιν αὐτῷ ("serve him", Theodotion) `[T]`, verified. *Book usage:* see unit 4. *OT-to-OT:* see above. *What it adds:* the title Son of Man evokes a figure who is served, and "not to be served but to serve" deliberately reverses it `[I]`, moderate. The reversal is the saying's point.

**Ps 49:8–9 → 10:45** *(moderate)*. See unit 17: no man can give God a λύτρωσις ("ransom") for his soul (Swete 48:9), and the Son of Man does.

*Internal:* **answers §8:37** — "what will a man give in exchange for his soul?" (moderate–high, synthetic). **Answers §9:35** — first/last, servant (high). **Plants §14:24** — "many" (high). **Plants §15:27** — right and left (high, verified). **Plants §14:23, 36** — the cup (high). **Plants §14:28; 16:7** — προάγω (high, verified). **Answers §1:13, 31** — διακονέω (moderate–high). **Plants §14:64; 15:1–31** — the prediction's steps (high, verified).

**Translations.** NASB95 "to give His life a ransom for many"; ESV "to give his life as a ransom for many". Both render ψυχή as "life", which hides the link with 8:35–37 (NASB95 "soul" at 8:36–37, "life" at 8:35) and with 14:34 ("my soul"). **Pulpit divergence:** the ESV has "life" at 8:35 and "soul" at 8:36–37 as well, so the congregation will not hear that 10:45 answers 8:37.

**Pitfall.** Preaching 10:45 as an example of servant leadership and stopping there. The "for even" (καὶ γάρ) grounds the disciples' service in the Son of Man's, but the second clause — the ransom — is what no disciple can imitate. The corrective: preach the ransom as the ground, and service as its fruit.

---

## 24. Mark 10:46–52 — On the Way

**Position.** *Q1:* the disciples have asked for glory and been told of ransom (10:35–45). *Q2:* the Way section ends as it began, with a blind man healed (8:22–26). This one asks for the right thing, uses a royal title, and follows Jesus "on the way" into Jerusalem `[T]`/`[I]`.

**Structure.** Jericho and the beggar (46); the cry and the rebuke (47–48); the call (49–50); the question and the healing (51–52).

**Text-first findings.**

- **From beside the road to on the road.** ἐκάθητο παρὰ τὴν ὁδόν ("he was sitting beside the road", 10:46) → ἠκολούθει αὐτῷ ἐν τῇ ὁδῷ ("he was following him on the road", 10:52) `[T]`. παρὰ τὴν ὁδόν ("beside the road") occurs in Mark at 4:4, 4:15 and 10:46: the seed "beside the road" that the birds took, the hearers "beside the road" from whom Satan snatched the word, and the blind man. The first search missed 4:15, whose accent is grave (ὁδὸν). A positive control caught it, and the phrase was re-run accent-stripped `[T]`, verified. *Moderate*, as design: the one "beside the road" is not snatched away but brought onto it.
- **The first "Son of David".** Υἱὲ Δαυὶδ Ἰησοῦ, ἐλέησόν με ("Son of David, Jesus, have mercy on me", 10:47–48) `[T]`. This is the first royal title in the narrative, spoken by a blind man at the edge of Jericho, just before the entry (11:10). ἐλεάω ("to have mercy") occurs at 5:19 ("how he had mercy on you") and 10:47–48 `[T]`, verified.
- **Rebuked to silence, like the demons.** ἐπετίμων αὐτῷ πολλοὶ ἵνα σιωπήσῃ ("many rebuked him to be silent", 10:48) — ἐπιτιμάω ("to rebuke") and σιωπάω ("to be silent") `[T]`. This time the crowd rebukes, and Jesus overrides them.
- **"Take heart."** Θάρσει ("take heart", 10:49). θαρσέω ("to take heart") occurs only here and at 6:50, "take heart, it is I" `[T]`, verified.
- **The same question as to James and John.** Τί σοι θέλεις ποιήσω; ("what do you want me to do for you?", 10:51) — nearly word for word Τί θέλετε ποιήσω ὑμῖν; (10:36) `[T]`, verified. The disciples asked for thrones; the blind man asks to see.
- **He throws off his cloak.** ἀποβαλὼν τὸ ἱμάτιον αὐτοῦ ("throwing off his cloak", 10:50) `[T]`. The cloak is spread on the road for the King a few verses later (11:7–8) *(uncertain as design)*.

**Tool 11.** No quotation. "Son of David" invokes 2 Sam 7:12–16 *(moderate — title, not wording)*: the promise of a son whose throne will be established for ever. *Book usage:* David was first mentioned at 2:25; the title returns at 11:10 and is questioned at 12:35–37. *What it adds:* the title is right, and 12:35–37 will show it to be insufficient.

*Internal:* **answers §8:22–26** — the frame of the Way section (high). **Answers §4:4, 15** — beside the road (moderate). **Answers §10:36** — the question (high, verified). **Answers §6:50** — θαρσέω (moderate). **Answers §5:34** — "your faith has saved you" (high, verbal). **Plants §11:10; 12:35–37** — David (high).

**Translations.** At 10:52 the ESV's "on the way" keeps the thread and the NASB95's "on the road" does not; at 10:46 both have "road"/"roadside". **Pulpit divergence:** here the ESV is the better text for the finding; at 10:46 a word of explanation will make the "beside the road → on the way" movement audible.

**Pitfall.** Preaching Bartimaeus as an example of persistence in prayer. He persists, but the unit's weight is on what he asks for — sight — and what he does with it: he follows on the way to the cross. The corrective: set him against James and John.

---

## 25. Mark 11:1–25 — The King Comes to His Temple ⭐

**Position.** *Q1:* the Son of David has been hailed (10:47–48), and the way prepared since 1:2–3 now reaches Jerusalem. *Q2:* the Lord whose way was prepared "suddenly comes to his temple" (Mal 3:1, cited at 1:2). The unit enacts the second half of the book's opening citation: the arrival (11:1–11), the inspection (11:11), and the verdict enacted twice — on the fig tree and on the temple (11:12–25) `[I]`, high.

**Structure.**

| Verses | Section |
|---|---|
| 11:1–7 | The colt found as he said |
| 11:8–10 | The acclamation: Hosanna; "the coming kingdom of our father David" |
| 11:11 | He enters the temple, looks around at everything, and leaves — it is late |
| 11:12–14 | *Opened:* the fig tree with leaves only, cursed |
| 11:15–19 | *Inside:* the temple action; "a house of prayer for all the nations"; the plot |
| 11:20–25 | *Closed:* the fig tree withered from the roots; faith, the mountain, prayer, forgiveness |

**Text-first findings.**

- **"The Lord has need of it."** Ὁ κύριος αὐτοῦ χρείαν ἔχει ("the Lord has need of it", 11:3). The κύριος ("Lord") of 1:3's prepared way arrives, and the ambiguity (owner? God? Jesus?) is left in place `[T]`/`[I]`.
- **A colt tied, never ridden.** πῶλον δεδεμένον ἐφ' ὃν οὐδεὶς οὔπω ἀνθρώπων ἐκάθισεν ("a colt tied, on which no man has yet sat", 11:2). Gen 49:11 Swete: δεσμεύων πρὸς ἄμπελον τὸν πῶλον αὐτοῦ ("binding his colt to the vine"), in the blessing of Judah, whose sceptre shall not depart `[T]`. Zech 9:9: a king coming ἐπὶ … πῶλον νέον ("on a young colt") `[T]`. Animals never used were fit for sacred purposes (Num 19:2; Deut 21:3; 1 Sam 6:7) `[S]`/`[I]`. *Synthetic*: moderate.
- **Garments on the road.** τὰ ἱμάτια αὐτῶν ἔστρωσαν εἰς τὴν ὁδόν ("they spread their cloaks on the road", 11:8). At Jehu's anointing each man ἔλαβεν … τὸ ἱμάτιον αὐτοῦ καὶ ἔθηκαν ὑποκάτω αὐτοῦ ("took his cloak and put it under him", 2 Kgs 9:13 Swete), and they proclaimed him king `[T]` *(moderate)*.
- **Hosanna.** Ὡσαννά (11:9, 10) transliterates Ps 118:25's הוֹשִׁיעָה נָּא ("save, please"), and 11:9 then quotes Ps 118:26 LXX verbatim `[T]`. This is the psalm whose v.22 is quoted at 12:10 and whose verb is used at 8:31.
- **The inspection.** περιβλεψάμενος πάντα ("having looked around at everything", 11:11) — the Lord arrives at his temple, looks, and leaves `[T]`. Mal 3:1–3: "the Lord whom you seek will suddenly come to his temple … who can endure the day of his coming?" `[I]`, moderate–high.
- **Fig, house and root, from Hosea 9.** The sweep found three verbal contacts with one chapter of Hosea `[T]`, verified in both Swete and Rahlfs, and in the WLC:
  - Hos 9:10: ὡς σκοπὸν ἐν συκῇ πρόιμον εἶδον πατέρας αὐτῶν ("like the first-ripe fruit on the fig tree I saw your fathers").
  - Hos 9:15: ἐκ τοῦ οἴκου μου ἐκβαλῶ αὐτούς ("I will drive them out of my house"; Hebrew מִבֵּיתִי אֲגָרְשֵׁם).
  - Hos 9:16: τὰς ῥίζας αὐτοῦ ἐξηράνθη, καρπὸν οὐκέτι μὴ ἐνέγκῃ ("their roots are dried up, they shall bear fruit no more"; Hebrew שָׁרְשָׁם יָבֵשׁ פְּרִי בלי־יַעֲשׂוּן, where בלי stands unpointed as a ketiv in the WLC).

  Mark has συκῆ ("fig tree", 11:13), ἤρξατο ἐκβάλλειν … ἐν τῷ ἱερῷ ("he began to drive out … in the temple", 11:15) with ὁ οἶκός μου ("my house", 11:17), μηκέτι … καρπὸν φάγοι ("may no one eat fruit ever again", 11:14) and ἐξηραμμένην ἐκ ῥιζῶν ("withered from the roots", 11:20) `[T]`. **One prophetic chapter supplies the fig, the expulsion from "my house", the dried roots and the end of fruit.** *Moderate–high* — not flagged by the overview; see Book-Overview Tensions.
- **"For all the nations."** πᾶσιν τοῖς ἔθνεσιν (11:17), kept by Mark alone of the Synoptics (see the overview) `[T]`. The temple action takes place in the court where the nations could pray `[S]`.
- **The mountain into the sea.** τῷ ὄρει τούτῳ ("this mountain", 11:23), said on the road from Bethany over the Mount of Olives (11:1, 19–20). Zech 14:4 Swete: the Mount of Olives will split, half of it toward the sea (πρὸς θάλασσαν) `[T]` *(moderate — "this mountain" may be the temple mount, with Zech 4:7's "great mountain" also in view `[S]`)*.
- **Forgiveness returns.** ἀφίετε … ἵνα καὶ ὁ πατὴρ ὑμῶν … ἀφῇ ὑμῖν τὰ παραπτώματα ὑμῶν ("forgive … so that your Father also may forgive you your trespasses", 11:25) `[T]`. The prayer that replaces the temple is prayer that forgives `[I]`, moderate. 11:26 is absent from the SBLGNT and ESV and bracketed by the NASB95.

**Tool 11.**

**Ps 118:25–26 (Swete 117) → 11:9–10** *(high — verbatim)*. *Source context:* a thanksgiving liturgy at the temple gates — "open to me the gates of righteousness" (118:19) — sung by one delivered from the nations who surrounded him (118:10–12). It contains the rejected stone (118:22) and the festal procession to the altar (118:27). *Book usage:* 118:22's verb stands behind 8:31, and 118:22–23 is quoted at 12:10–11 — **Mark returns to this one psalm three times in the Way and Jerusalem sections: the rejection predicted (8:31), the acclamation (11:9–10), the exaltation of the rejected stone (12:10–11).** The three uses do not follow the psalm's own order; they follow the story's. *OT-to-OT:* Zech 9:9 and Ps 118 both picture a king entering Zion for salvation. *What it adds:* the crowd sings the psalm of the stone the builders reject, and within the week the builders reject him.

**Mal 3:1–3 → 11:11–17** *(moderate–high — the book's own opening citation, now enacted)*. *Source context:* see unit 1. *Book usage:* Mal 3:1 was cited at 1:2; this is the Lord's arrival. *OT-to-OT:* Mal 3 and Zech 14 (the Mount of Olives, and "no trader in the house of the LORD", 14:21) both close their books with the day of the LORD's coming to Jerusalem. *What it adds:* the book's first sentence is completed. The way was prepared, and the Lord comes suddenly to his temple, to refine it.

**Isa 56:7 + Jer 7:11 → 11:17** *(high — formula quotation)*. *Source context:* Isa 56:3–8 promises that foreigners and eunuchs who hold fast to the covenant will be brought to the LORD's holy mountain, for "my house shall be called a house of prayer for all peoples". Jer 7 is the temple sermon: do not trust "the temple of the LORD"; "has this house … become a den of robbers in your eyes?"; "go to Shiloh … I will do to this house as I did to Shiloh" (7:12–14) `[T]`. *Book usage:* Isaiah is live; Jeremiah was used at 8:18 (Jer 5:21). *OT-to-OT:* one text is the promise for the nations, the other the threat of destruction, and Mark joins them. *What it adds:* the house meant for the nations has been made a robbers' refuge, and Jer 7's Shiloh warning makes the fig tree's withering a verdict on the house.

**Hos 9:10–17 → 11:12–21** *(moderate–high — three verbal contacts in one chapter)*. *Source context:* Hosea recalls Israel as the first-ripe fig, and then its apostasy at Baal-peor and Gilgal: "I will drive them out of my house … their root is dried up … my God will reject them" (9:17). *Book usage:* first use of Hosea. Hos 6:6 stands behind 12:33, so Hosea becomes live. *OT-to-OT:* Jer 8:13, "no figs on the fig tree", joins Hosea in the image of Israel as a barren tree `[T]` for Jeremiah. *What it adds:* the sandwich is interpreted by a single chapter of the Prophets. The tree and the house fall under the same verdict.

**Zech 9:9; Gen 49:11; 2 Kgs 9:13; Zech 14:4, 21** *(moderate each)*. Move 1 only; see above.

*Internal:* **answers §1:2–3** — the way prepared, and the Lord come to his temple (high, synthetic). **Answers §10:47–48** — David (high). **Answers §3:6** — the plot again: ἐζήτουν πῶς αὐτὸν ἀπολέσωσιν ("they sought how to destroy him", 11:18) (high). **Plants §13:28** — the fig tree (moderate, verified). **Plants §14:48; 15:27** — λῃστής ("robber") (high, verified). **Plants §14:58; 15:29, 38** — the house and the ναός ("sanctuary") (moderate). **Plants §12:10** — Ps 118 (high). **Answers §9:29** — προσευχή ("prayer") (moderate).

**Translations.** At 11:3 the NASB95's "The Lord has need of it" and the ESV's "The Lord has need of it" both keep the ambiguity. At 11:17 the NASB95's "ROBBERS' DEN" and the ESV's "den of robbers" are equivalent. At 11:22 Ἔχετε πίστιν θεοῦ ("have faith of God") is "Have faith in God" in both — an interpretive decision on a genitive, and a defensible one. **Pulpit divergence:** none bearing.

**Difficulty.** 11:13, "it was not the season for figs". *Category:* apologetic. *Function:* the narrator's comment, which tells the reader that the curse is a sign and not a tantrum `[I]`, high. The sandwich and Hos 9 confirm it.

**Pitfall.** Preaching 11:23–24 as a promise that faith can get anything ("name it and claim it") — the catalogue flags this as a weaponised text. The corrective: the saying stands inside the temple-and-fig sandwich, on the Mount of Olives. The faith meant is faith in God (11:22) at the end of the temple, joined to forgiveness (11:25).

---

## 26. Mark 11:27–12:12 — The Beloved Son and the Rejected Stone ⭐

**Position.** *Q1:* the temple has been judged in action (11:15–17). *Q2:* the temple authorities ask by what authority, and Jesus answers with a counter-question and then a parable. The parable tells them who he is and what they will do. The Voice's word ἀγαπητός ("beloved") is put into Jesus' own mouth for the only time (12:6) `[T]`.

**Structure.** The authority question and the counter-question about John (11:27–33); the vineyard parable (12:1–9); the psalm citation (12:10–11); the reaction (12:12).

**Text-first findings.**

- **Authority, one last time.** ἐν ποίᾳ ἐξουσίᾳ ("by what authority?") three times (11:28, 29, 33) `[T]`. The word that opened the ministry (1:22, 27) ends here in a refusal to answer: "neither will I tell you" (11:33). The parable answers without stating it `[I]`.
- **John again.** "Was John's baptism from heaven or from men?" (11:30). The Voice at the Jordan came ἐκ τῶν οὐρανῶν ("from the heavens", 1:11) `[T]`. The authorities ἐφοβοῦντο τὸν ὄχλον ("feared the crowd", 11:32; 12:12) `[T]`.
- **The vineyard is Isaiah's.** "A man planted a vineyard, put a hedge around it, dug a vat, built a tower" (12:1) — Isa 5:2 Swete: φραγμὸν περιέθηκα … ᾠκοδόμησα πύργον … προλήνιον ὤρυξα ("I put a hedge around it … built a tower … dug a wine vat") `[T]`. In Isaiah the vineyard is Israel and the judgement falls on the vineyard (5:5–7); in Mark it falls on the tenants (12:9) `[T]`/`[I]`.
- **"One beloved son, sent last."** ἔτι ἕνα εἶχεν, υἱὸν ἀγαπητόν· ἀπέστειλεν αὐτὸν ἔσχατον ("he had still one, a beloved son; he sent him last", 12:6) `[T]`. The owner ἀπέστειλεν ("sent") four times (12:2, 4, 5, 6); at 12:3 the tenants ἀπέστειλαν ("sent") the first servant away empty `[T]`, verified. The Son follows the prophets, and he is the last.
- **Joseph's brothers.** δεῦτε ἀποκτείνωμεν αὐτόν ("come, let us kill him", 12:7) is Gen 37:20 Swete verbatim, the brothers plotting against Joseph `[T]` *(moderate–high)*. οὗτός ἐστιν ὁ κληρονόμος ("this is the heir") is the tenants' own reading of the son `[T]`.
- **Killed and thrown out.** ἀπέκτειναν αὐτόν, καὶ ἐξέβαλον αὐτὸν ἔξω τοῦ ἀμπελῶνος ("they killed him and threw him out of the vineyard", 12:8) `[T]`. ἐκβάλλω ("to throw out") is the verb Jesus used in the temple (11:15).
- **The stone.** Λίθον ὃν ἀπεδοκίμασαν οἱ οἰκοδομοῦντες ("the stone which the builders rejected", 12:10) — Ps 117:22–23 LXX verbatim `[T]`. ἀποδοκιμάζω ("to reject") is the verb of 8:31, and its two Markan uses are these `[T]`, verified.

**Tool 11.**

**Isa 5:1–7 → 12:1–9** *(high — verbatim details)*. *Source context:* the Song of the Vineyard. The beloved plants, hedges and builds; the vineyard yields wild grapes; the LORD will remove the hedge; "the vineyard of the LORD of hosts is the house of Israel … he looked for justice (מִשְׁפָּט) but behold, bloodshed (מִשְׂפָּח); for righteousness (צְדָקָה) but behold, a cry (צְעָקָה)" (5:7) `[T]` — a wordplay the Greek cannot carry (category 1, translation loss). *Book usage:* Isaiah is live; this is its first use as a story. *OT-to-OT:* Isa 5 and Ps 80:8–16 (the vine from Egypt, ravaged) both picture Israel as the LORD's planting *(uncertain on wording)*. *What it adds:* the judgement moves from the vineyard to its keepers. The leaders "knew he had spoken the parable against them" (12:12).

**Ps 118:22–23 (Swete 117) → 12:10–11** *(high — verbatim)*. *Source context:* see unit 25. The stone rejected becomes the head of the corner, "this is the LORD's doing, and it is marvellous in our eyes" — sung by the delivered one at the temple gate. *Book usage:* 8:31 (the verb) and 11:9–10 (Hosanna and the blessing) — **Mark cites Ps 118 three times in the book's sequence: rejection (8:31), acclamation (11:9–10), exaltation (12:10–11).** *OT-to-OT:* Isa 28:16 (a tested cornerstone laid in Zion) and Ps 118:22 belong together in the Prophets' and Psalms' temple imagery `[S]`. *What it adds:* the son killed in the parable is the stone raised in the psalm. The parable ends in death, and the citation reaches past it to the resurrection.

**Gen 37:20 → 12:7** *(moderate–high)*. *Source context:* the brothers see Joseph coming and say "come, let us kill him … and we will see what becomes of his dreams" — the beloved son (37:3) sent by the father (37:13–14). *Book usage:* first use. *What it adds:* the beloved son sent by his father to his brothers, and murdered by them for his inheritance, is Joseph's story. The book knows how it ended — rejected and then exalted (Gen 50:20) `[I]`.

*Internal:* **answers §1:11; §9:7** — ἀγαπητός (high). **Answers §8:31** — ἀποδοκιμάζω (high, verified). **Answers §1:22, 27** — ἐξουσία (high). **Plants §14:1; 14:43–46** — they seek to seize him (ἐζήτουν αὐτὸν κρατῆσαι, 12:12) (high). **Plants §15:20** — "they led him out" (ἐξάγουσιν, "they lead out") (uncertain).

**Translations.** NASB95 "vine-growers"; ESV "tenants". NASB95 "chief corner stone"; ESV "cornerstone" — κεφαλὴν γωνίας ("head of the corner"). **Pulpit divergence:** none bearing.

**Pitfall.** Preaching the parable as "God is patient with sinners" without the son. The whole parable moves towards the son and his death, and the citation reaches beyond it. The corrective: preach the parable as Jesus' self-disclosure to his killers, in the week of his death.

---

## 27. Mark 12:13–44 — Caesar, the Resurrection, the Shema, David's Lord, a Widow

**Position.** *Q1:* the leaders now want to seize him (12:12). *Q2:* three parties try to trap him — Pharisees and Herodians, Sadducees, a scribe — and then he asks them his own question. The unit ends with the scribes condemned and a widow who gives her whole life, placed just before the discourse on the temple's end `[T]`/`[I]`.

**Structure.** Caesar (13–17); the resurrection (18–27); the great commandment (28–34); David's Lord (35–37); beware the scribes (38–40); the widow (41–44).

**Text-first findings.**

- **The image and the inscription.** Τίνος ἡ εἰκὼν αὕτη καὶ ἡ ἐπιγραφή; ("whose image and inscription is this?", 12:16). ἐπιγραφή ("inscription") occurs only here and at 15:26, ἡ ἐπιγραφὴ τῆς αἰτίας αὐτοῦ ("the inscription of the charge against him") — Caesar's coin, and Jesus' cross `[T]`, verified. That "give God what is God's" implies humanity bearing God's image (Gen 1:26–27, εἰκών, "image") is `[I]`, moderate.
- **"You know neither the Scriptures nor the power of God."** μὴ εἰδότες τὰς γραφὰς μηδὲ τὴν δύναμιν τοῦ θεοῦ (12:24) `[T]`. ἐπὶ τοῦ βάτου ("at the passage about the bush", 12:26) — a way of citing a passage by its heading, which may bear on 2:26 `[I]`.
- **The Shema, with "mind" added.** ἐξ ὅλης τῆς καρδίας … ψυχῆς … διανοίας … ἰσχύος ("with all your heart … soul … mind … strength", 12:30) `[T]`. The scribe repeats it with συνέσεως ("understanding", 12:33). συνίημι ("to understand") runs through the book (4:12; 6:52; 7:14; 8:17, 21) `[T]`.
- **ὅλος ("whole, all") ties the commandment to the widow.** ἐξ ὅλης τῆς καρδίας ("with all your heart", 12:30, 33) — and the widow gave ὅλον τὸν βίον αὐτῆς ("her whole living, her whole life", 12:44) `[T]`, verified. She keeps the commandment the scribe could recite `[I]`, moderate–high.
- **"Not far from the kingdom."** 12:34 — the one scribe commended in Mark `[T]`.
- **David's Lord.** "The Lord said to my Lord, sit at my right hand" (12:36, Ps 110:1). The question Πόθεν αὐτοῦ ἐστιν υἱός; ("how then is he his son?", 12:37) is left unanswered until 14:62, where Jesus claims the right hand `[T]`/`[I]`. ὁ πολὺς ὄχλος ἤκουεν αὐτοῦ ἡδέως ("the great crowd heard him gladly", 12:37) — ἡδέως ("gladly") occurs only here and at 6:20, of Herod hearing John `[T]`, verified.
- **Devouring widows' houses, then a widow's two coins.** οἱ κατεσθίοντες τὰς οἰκίας τῶν χηρῶν ("who devour widows' houses", 12:40) — and immediately μία χήρα πτωχή ("a poor widow", 12:42) `[T]`. The juxtaposition is a verdict: she is what the scribes devour `[I]`, high. Isa 10:2 Swete: ὥστε εἶναι αὐτοῖς χήραν εἰς ἁρπαγήν ("so that widows become their prey") *(moderate)*.
- **Two women frame the discourse.** The widow gives πάντα ὅσα εἶχεν ("everything she had", 12:44); the anointing woman ὃ ἔσχεν ἐποίησεν ("did what she had", 14:8) `[T]`. Chapter 13 stands between them `[T]` for the position, `[I]` for the frame, moderate–high.

**Tool 11.**

**Deut 6:4–5 → 12:29–30** *(high — verbatim, with διάνοια ("mind") added)*. *Source context:* the Shema, at the head of Moses' exposition of the first commandment: love the LORD with all your heart, soul and might; these words shall be on your heart; teach them to your children. *Book usage:* anticipated at 2:7 and 10:18 (εἷς ὁ θεός, "God alone"). *OT-to-OT:* the scribe adds Deut 4:35 (οὐκ ἔστιν ἔτι πλὴν αὐτοῦ, "there is no other besides him") and 1 Sam 15:22 / Hos 6:6 (obedience or mercy above sacrifice). Torah, Former Prophets and Latter Prophets agree `[I]`. *What it adds:* at the temple, a scribe says that love is "much more than all whole burnt offerings and sacrifices" (12:33). The temple's end in chapter 13 is anticipated by its own scribe.

**Lev 19:18 → 12:31, 33** *(high)*. Move 1: "you shall love your neighbour as yourself; I am the LORD", closing a list of laws against vengeance and grudges.

**Ps 110:1 (Swete 109:1) → 12:36** *(high)*. *Source context:* the LORD's oracle to the king, "sit at my right hand", with a priesthood after the order of Melchizedek (110:4). *Book usage:* first use; it returns at 14:62 with Dan 7:13 (and at 16:19 in the longer ending). *OT-to-OT:* see 14:62. *What it adds:* David calls his son "Lord", so the Son of David is more than David's son. The claim becomes explicit at the trial.

**Exod 3:6 → 12:26** *(high)*. Move 1: God names himself to Moses as the God of the patriarchs, who are therefore alive to him.

**Deut 25:5; Gen 38:8 → 12:19** *(high)*. Move 1: the levirate law.

*Internal:* **answers §3:6** — Pharisees and Herodians (high, verified). **Plants §15:26** — ἐπιγραφή (moderate–high, verified). **Answers §6:20** — ἡδέως (moderate, verified). **Plants §14:62** — Ps 110 (high). **Plants §14:3–9** — the two women (moderate–high). **Answers §10:21** — ἀγαπάω (moderate).

**Translations.** At 12:14 the NASB95's "poll-tax" keeps κῆνσος ("census tax"), and the ESV's "taxes" is broader. At 12:44 the NASB95's "all she had to live on" and the ESV's "all she had to live on" both render ὅλον τὸν βίον ("her whole living"), and both lose ὅλος ("whole") and the link with 12:30. **Pulpit divergence:** none bearing beyond this.

**Pitfall.** Preaching the widow as a model of sacrificial giving and nothing more. She is set beside scribes who devour widows and before the temple's destruction, so the scene is a lament as well as a commendation. The corrective: preach her as the one who loves God with her whole life, in a system that devours her — and link her with the woman of 14:3–9.

---

## 28. Mark 13:1–23 — Watch Out ⭐

**Position.** *Q1:* the temple has been judged (11:12–25), its leaders silenced (11:27–12:37), its scribes condemned, and a widow has given her whole life to it (12:38–44). *Q2:* leaving the temple, a disciple admires its stones, and Jesus says none will be left on another. The longest speech in the book follows, given privately to the first four disciples, on the Mount of Olives, opposite the temple. It sits between the widow's gift and the anointing, just before the passion begins `[T]`/`[I]`.

**Structure.** The prediction (13:1–2); the question, "when … and what sign?" (13:3–4); **βλέπετε ("watch out")** — deceivers, wars, beginnings of birth pains (13:5–8); **βλέπετε** — handed over, gospel to all nations, the Spirit speaking, family betrayal, endurance (13:9–13); the abomination, flight, tribulation, the days shortened (13:14–20); false christs, "watch out: I have told you everything beforehand" (13:21–23). βλέπετε ("watch out") stands at 13:5, 9, 23 and 33 and frames the discourse `[T]`.

**Text-first findings.**

- **Stone on stone.** οὐ μὴ ἀφεθῇ ὧδε λίθος ἐπὶ λίθον ("there will not be left here stone upon stone", 13:2). Hag 2:15 Swete looks back to the day πρὸ τοῦ θεῖναι λίθον ἐπὶ λίθον ἐν τῷ ναῷ Κυρίου ("before stone was laid upon stone in the temple of the Lord"), the refounding of the second temple `[T]` *(moderate)*. The temple whose first stones Haggai celebrated will lose its last. καταλυθῇ ("will be thrown down", 13:2) uses καταλύω ("to destroy"), which recurs only in the false charge (14:58) and the mockery (15:29) `[T]`, verified.
- **Opposite the temple.** καθημένου αὐτοῦ εἰς τὸ Ὄρος τῶν Ἐλαιῶν κατέναντι τοῦ ἱεροῦ ("as he sat on the Mount of Olives opposite the temple", 13:3). κατέναντι ("opposite") occurs at 11:2, 12:41 (sitting opposite the treasury, watching the widow) and 13:3 `[T]`, verified. He sits opposite the treasury, and then opposite the whole temple. The Mount of Olives is the place of the LORD's coming in Zech 14:4 `[I]`, moderate.
- **The four.** Πέτρος καὶ Ἰάκωβος καὶ Ἰωάννης καὶ Ἀνδρέας ("Peter and James and John and Andrew", 13:3) — the first called (1:16–20), named together here for the last time `[T]`, verified.
- **"I am."** πολλοὶ ἐλεύσονται … λέγοντες ὅτι Ἐγώ εἰμι ("many will come … saying 'I am'", 13:6). ἐγώ εἰμι is Jesus' own saying at 6:50 and 14:62 `[T]`. The imposters claim the divine self-naming *(moderate–high)*.
- **The disciples' passion.** παραδώσουσιν ὑμᾶς εἰς συνέδρια … ἐπὶ ἡγεμόνων καὶ βασιλέων σταθήσεσθε … εἰς μαρτύριον αὐτοῖς ("they will hand you over to councils … you will stand before governors and kings … for a testimony to them", 13:9) `[T]`. Within days Jesus himself stands before the συνέδριον ("council", 14:55; 15:1) and a governor, and is called "king" (15:2) `[T]`. The disciples' future is told in the words of his passion *(moderate–high, synthetic)*.
- **The Spirit speaks.** οὐ γάρ ἐστε ὑμεῖς οἱ λαλοῦντες ἀλλὰ τὸ πνεῦμα τὸ ἅγιον ("for it is not you who speak, but the Holy Spirit", 13:11) — the book's nearest approach to the promised baptism in the Spirit (1:8) `[T]`/`[I]`.
- **"Let the reader understand."** τὸ βδέλυγμα τῆς ἐρημώσεως ἑστηκότα ὅπου οὐ δεῖ, ὁ ἀναγινώσκων νοείτω ("the abomination of desolation standing where he must not — let the reader understand", 13:14) `[T]`. Two grammatical features matter:
  - The participle ἑστηκότα ("standing") is **masculine** with a neuter noun, so the abomination is a person `[T]`.
  - The narrator addresses his reader with νοέω ("to perceive"), the verb Jesus used of the disciples' failure: οὔπω νοεῖτε; ("do you not yet perceive?", 8:17). νοέω occurs only at 7:18, 8:17 and 13:14 `[T]`, verified.
- **The elect.** ἐκλεκτοί ("elect", 13:20, 22, 27) occur only in this discourse `[T]`, verified.

**Tool 11.**

**Dan 9:27; 11:31; 12:11 → 13:14** *(high — the phrase)*. *Source context:* in Daniel the "abomination that makes desolate" is set up in the sanctuary, after the anointed one is cut off (9:26) and the sacrifice abolished; it recurs at 11:31 (the profaning of the temple) and 12:11 (1,290 days to the end) `[T]`. *Book usage:* Dan 2:28 at 13:7 (δεῖ γενέσθαι, "must take place") and Dan 7:13 at 13:26 — the discourse is built on Daniel. *OT-to-OT:* Dan 12:1, the tribulation "such as has not been", comes after Dan 11:31's abomination in Daniel's final vision, and Mark keeps the order: the abomination at 13:14, the tribulation at 13:19 *(moderate–high — the order is `[T]` in both books; that Mark follows Daniel's sequence deliberately is `[I]`)*. *What it adds:* the temple's end is Daniel's end, and the reader is told to understand Daniel.

**Dan 2:28 → 13:7** *(moderate–high)*. Move 1: Daniel tells Nebuchadnezzar that the God in heaven reveals ἃ δεῖ γενέσθαι ἐπ' ἐσχάτων τῶν ἡμερῶν ("what must take place in the last days"), and the stone cut without hands becomes a mountain (2:34–35, 44–45). *What it adds:* the book's δεῖ ("must") is Daniel's.

**Mic 7:6 → 13:12; Isa 19:2 → 13:8; Deut 13:1–3 → 13:22** *(moderate each)*. Move 1 only. Micah's family breakdown before "I will look to the LORD" (7:7); nation against nation in the oracle on Egypt; the false prophet whose sign comes true and who is still not to be followed.

*Internal:* **plants §14:58; 15:29** — καταλύω (high, verified). **Plants §14:55–15:2** — councils, governor, king (moderate–high, synthetic). **Answers §8:17** — νοέω, the reader (moderate–high, verified). **Answers §1:8** — the Spirit (moderate). **Answers §13:3 ← 1:16–20** — the four (moderate–high). **Plants §14:62** — ἐγώ εἰμι, the true and the false (moderate). **Answers §12:41–44** — κατέναντι (moderate).

**Translations.** At 13:14 the **ESV**'s "standing where *he* ought not to be" keeps the masculine participle, and the **NASB95**'s "standing where *it* should not be" levels it. **Pulpit divergence:** here the ESV is closer to the Greek, and the congregation will hear the personal note. At 13:6 the NASB95's "I am He!" and the ESV's "I am he!" both add "he".

**Genre.** Prophetic-apocalyptic discourse: vision language set inside historical prediction (the temple's fall; Judaea; flight to the mountains). Read the imagery as vision, and the warnings as addressed to real hearers.

**Pitfall.** Charting 13:5–23 as a sequence of signs. The discourse's own frame is "watch out" and "do not be alarmed" (13:7). The signs are given to prevent panic and deception, not to fix a date. The corrective: preach the four βλέπετε.

---

## 29. Mark 13:24–37 — The Son of Man Coming; Stay Awake ⭐

**Position.** *Q1:* the tribulation has been described (13:14–23). *Q2:* the discourse moves to the coming of the Son of Man and then to the parable of the doorkeeper. It ends with γρηγορεῖτε ("stay awake", 13:37), addressed to "all". The next chapter shows the disciples failing to do exactly that on the first night of the passion `[T]`/`[I]`.

**Structure.** The cosmic signs and the coming (24–27); the fig tree and "this generation" (28–31); no one knows the day (32); the doorkeeper and the four watches (33–37).

**Text-first findings.**

- **The darkening.** ὁ ἥλιος σκοτισθήσεται, καὶ ἡ σελήνη οὐ δώσει τὸ φέγγος αὐτῆς ("the sun will be darkened, and the moon will not give its light", 13:24) — Isa 13:10 (the day of the LORD on Babylon) with Joel 2:10's φέγγος ("light") `[T]`, verified in Swete. At the cross, σκότος ἐγένετο ἐφ' ὅλην τὴν γῆν ("darkness came over the whole land", 15:33) `[T]` *(moderate, synthetic)*.
- **The Son of Man coming "with great power and glory".** 13:26 — Dan 7:13, the third of the three Son of Man glory sayings (8:38; 13:26; 14:62) `[T]`. δόξα ("glory") occurs three times in Mark: 8:38, 10:37 ("in your glory", the request) and 13:26 `[T]`, verified.
- **Gathering the elect "from the four winds".** 13:27 — Zech 2:10 (Swete 2:6) and Deut 30:4 `[T]`, verified.
- **The fig tree again.** Ἀπὸ δὲ τῆς συκῆς μάθετε τὴν παραβολήν ("from the fig tree learn the parable", 13:28). The cursed tree of 11:13–21 becomes a sign that summer is near: ἐγγύς ἐστιν ἐπὶ θύραις ("he is near, at the doors", 13:29) `[T]`. συκῆ ("fig tree") occurs only at 11:13, 20, 21 and 13:28 `[T]`, verified.
- **"My words will not pass away."** οἱ δὲ λόγοι μου οὐ μὴ παρελεύσονται (13:31). Isa 40:8, "the word of our God stands for ever", from the passage whose v.3 opened the book `[I]`, moderate (the Greek wording differs). **Jesus claims for his own words what Isaiah claimed for God's.**
- **"Nor the Son, but the Father."** 13:32 is the only absolute "the Son" alongside "the Father" in Mark `[T]`.
- **The four watches.** ὀψὲ ἢ μεσονύκτιον ἢ ἀλεκτοροφωνίας ἢ πρωΐ ("in the evening, at midnight, at cockcrow, or at dawn", 13:35). ἀλεκτοροφωνία ("cockcrow") is a New Testament hapax `[T]`, verified. The passion follows the same watches: ὀψίας γενομένης ("when evening came", 14:17); Gethsemane and the arrest in the night; ἀλέκτωρ ἐφώνησεν ("a cock crowed", 14:68, 72); πρωΐ ("at dawn", 15:1) `[T]`, verified. γρηγορέω ("to watch") stands only at 13:34, 35, 37 and 14:34, 37, 38 `[T]`, verified. *Synthetic, verified*: high.
- **"To all."** ὃ δὲ ὑμῖν λέγω πᾶσιν λέγω· γρηγορεῖτε ("what I say to you I say to all: stay awake", 13:37) — the discourse given to four is extended to the reader `[T]`.

**Tool 11.**

**Dan 7:13–14 → 13:26** *(high)*. *Source context:* see unit 4. *Book usage:* 2:10 (authority), 8:38 (glory with the angels) and 14:62 (the right hand and the clouds). *OT-to-OT:* Isa 13:10 and Dan 7 both concern the fall of empires and the coming of God's rule; Mark sets the cosmic signs of the one before the coming of the other *(moderate)*. *What it adds:* the vindication of the Son of Man, which the passion predictions promised ("after three days he will rise"), is extended to his coming in glory.

**Isa 13:10; 34:4 (with Joel 2:10) → 13:24–25** *(high)*. *Source context:* Isa 13 is the oracle against Babylon — the day of the LORD, the stars and the sun darkened, the arrogant brought low. Isa 34:4 is judgement on the nations and Edom, "the heavens rolled up like a scroll". *Book usage:* Isaiah is live. *OT-to-OT:* Joel 2:10 applies the same imagery to the LORD's own army against Zion. *What it adds:* the language of the fall of empires is applied to the end of this age, and in the passion to the land (15:33).

**Zech 2:10 (Swete 2:6); Deut 30:4 → 13:27** *(moderate–high)*. Move 1: the scattered gathered from the four winds and from the ends of heaven, after exile. *Book usage:* Zechariah is live (9:9; 13:7; 14:4). *What it adds:* the Son of Man does what the LORD promised to do.

*Internal:* **plants §14:17–15:1** — the watches (high, verified). **Plants §14:34–41** — γρηγορέω and καθεύδω ("to sleep") (high, verified). **Answers §11:13–21** — the fig tree (moderate). **Plants §14:62** — the Son of Man and the clouds (high). **Plants §15:33** — the darkness (moderate). **Answers §1:3 (Isa 40)** — "my words" (moderate).

**Translations.** At 13:35 NASB95 "when the rooster crows" and ESV "when the rooster crows" both render ἀλεκτοροφωνίας ("at cockcrow"), which keeps the link with 14:68, 72. At 13:33 the NASB95 has "Take heed, keep on the alert" and the ESV "Be on guard, keep awake". **Pulpit divergence:** at 13:34–37 the ESV has "stay awake" throughout and "watch" in Gethsemane (14:34–38), where the NASB95 has "alert" and then "keep watch". Neither version uses one English word for γρηγορέω ("to watch") in both chapters, so the congregation will not hear the link unless it is pointed out.

**Difficulty.** 13:30, "this generation will not pass away". *Category:* apologetic/doctrinal. *Function:* the saying answers the disciples' "when will these things be?" (13:4), and "these things" in 13:4 is the temple's destruction. It stands beside 13:32, where no one knows "that day". The two sayings are about two horizons `[I]`, moderate — a crux. Route to Logos before preaching.

**Pitfall.** Preaching 13:32–37 without chapter 14. Mark has built the discourse's watches into the passion night, so the first application of "stay awake" is the disciples' failure in Gethsemane — and the grace that follows it (16:7). The corrective: preach 13:32–37 and 14:32–42 together.

---

## 30. Mark 14:1–11 — Anointed for Burial

**Position.** *Q1:* the discourse has told the disciples to watch, and the plot (3:6; 11:18; 12:12) is still waiting for its moment. *Q2:* the passion opens with a sandwich — the plot, a woman's extravagance, Judas' offer — so that the anointing is framed by betrayal `[T]`.

**Structure.** *Opened:* the plot, two days before Passover (1–2). *Inside:* the anointing at Bethany (3–9). *Closed:* Judas goes to the chief priests (10–11).

**Text-first findings.**

- **"By stealth."** ἐν δόλῳ ("by deceit", 14:1). δόλος ("deceit") was in the vice list from the heart (7:22) `[T]`.
- **In the house of Simon the leper.** λεπρός ("leper") occurs only at 1:40 and 14:3 `[T]`, verified. The first cleansing in the book was of a leper, and the last meal before the Passover is in a leper's house `[I]`.
- **On his head.** κατέχεεν αὐτοῦ τῆς κεφαλῆς ("she poured it over his head", 14:3). Kings were anointed on the head: Saul (1 Sam 10:1, ἐπέχεεν ἐπὶ τὴν κεφαλὴν αὐτοῦ, "poured it on his head") and Jehu (2 Kgs 9:6) `[T]`, verified in Swete *(moderate)*. Jesus reads it as προέλαβεν μυρίσαι τὸ σῶμά μου εἰς τὸν ἐνταφιασμόν ("she has anointed my body beforehand for burial", 14:8) `[T]`. The Messiah — Χριστός, "the anointed" — is anointed for his burial `[I]`, high. κεφαλή ("head") runs through the passion: John's head (6:24–28); the head of the corner (12:10); this head; the head struck with a reed (15:19); heads wagged (15:29) `[T]`, verified.
- **Indignant at the waste.** ἀγανακτοῦντες ("indignant", 14:4); ἀπώλεια ("waste, destruction", 14:4); ἐνεβριμῶντο αὐτῇ ("they scolded her", 14:5). ἐμβριμάομαι ("to rebuke sternly") occurs only at 1:43 and here `[T]`, verified.
- **"The poor you always have."** 14:7 recalls Deut 15:11, "the poor will never cease out of the land; therefore … open your hand" *(moderate; the Swete wording differs)*. The saying assumes the command to give to the poor; it does not cancel it.
- **"In memory of her."** εἰς μνημόσυνον αὐτῆς (14:9). μνημόσυνον ("memorial") occurs in Mark only here, in a Passover setting (14:1). Exod 12:14 Swete: ἔσται ἡ ἡμέρα ὑμῖν αὕτη μνημόσυνον ("this day shall be a memorial for you"), of the Passover `[T]`, verified *(moderate)*. The woman's act is joined to the gospel's proclamation "in the whole world" `[T]`.
- **An "opportune" moment.** Judas ἐζήτει πῶς αὐτὸν εὐκαίρως παραδοῖ ("was seeking how to hand him over at an opportune time", 14:11). εὐκαίρως ("opportunely") occurs only here, and εὔκαιρος ("opportune") only at 6:21, Herod's ἡμέρας εὐκαίρου ("an opportune day") on which John was killed `[T]`, verified. *Moderate*: the two betrayals share their timing word.

**Tool 11.** **1 Sam 10:1; 2 Kgs 9:6 → 14:3** *(moderate — gesture)*. *Source context:* Samuel anoints Saul privately; a young prophet anoints Jehu in an inner room, and Jehu's officers spread their garments under him (9:13, see unit 25). *Book usage:* 2 Kgs 9:13 at 11:8. *OT-to-OT:* both are private anointings of a king before his public acclamation. *What it adds:* the anointing is royal and private, and Jesus reinterprets it as burial.

**Exod 12:14 → 14:9** *(moderate)*. Move 1: the Passover as a perpetual memorial.

*Internal:* **answers §1:40** — the leper (moderate). **Answers §12:41–44** — the two women (moderate–high). **Plants §16:1** — the anointing already done (high). **Answers §6:21** — εὔκαιρος (moderate, verified). **Plants §14:9 → 13:10** — the gospel preached to the world (high).

**Translations.** NASB95 "a good deed"; ESV "a beautiful thing" (14:6, καλὸν ἔργον, "a good/beautiful work"). **Pulpit divergence:** none bearing.

**Pitfall.** Setting worship against giving to the poor. Jesus' reply is about his own imminent death: "you will not always have me". The corrective: preach the woman as the one disciple who understood that he was going to die, and acted on it.

---

## 31. Mark 14:12–31 — The Blood of the Covenant ⭐

**Position.** *Q1:* Jesus has been anointed for burial, and Judas has agreed to hand him over (14:3–11). *Q2:* the Passover meal interprets the death before it happens. The bread and cup say what 10:45 said — "for many" — and the walk to the Mount of Olives predicts the disciples' flight and the shepherd's going ahead `[T]`/`[I]`.

**Structure.** Preparations found "as he said" (12–16); the betrayer at the table (17–21); bread and cup (22–25); to the Mount of Olives: the scattering, the going ahead, Peter's boast (26–31).

**Text-first findings.**

- **"As he said," three times.** εὗρον καθὼς εἶπεν αὐτοῖς ("they found it as he had told them", 14:16). καθὼς εἶπεν ("as he said") stands at 11:6 (the colt), 14:16 (the room) and 16:7 (Galilee: "there you will see him, καθὼς εἶπεν ὑμῖν", "as he told you") `[T]`, verified. **The first two are fulfilled within the book, and the third is not narrated. The reader has twice seen his word come true.** *Synthetic, verified*: high.
- **"One of the twelve," three times.** εἷς τῶν δώδεκα ("one of the twelve", 14:10, 20, 43) `[T]`, verified. ὁ ἐσθίων μετ' ἐμοῦ ("the one eating with me", 14:18) is Ps 41:10's ὁ ἐσθίων ἄρτους μου ("the one eating my bread", Swete 40:10) `[T]` *(moderate–high)*.
- **"As it is written of him."** ὁ μὲν υἱὸς τοῦ ἀνθρώπου ὑπάγει καθὼς γέγραπται περὶ αὐτοῦ ("the Son of Man goes as it is written of him", 14:21) — the sixth of seven γέγραπται ("it is written") `[T]`.
- **The Supper's verbs.** λαβὼν ἄρτον εὐλογήσας ἔκλασεν καὶ ἔδωκεν ("taking bread, having blessed, he broke and gave", 14:22), and λαβὼν ποτήριον εὐχαριστήσας ἔδωκεν ("taking a cup, having given thanks, he gave", 14:23) — the verbs of the two feedings (6:41; 8:6) `[T]`, verified. εὐχαριστέω ("to give thanks") occurs only at 8:6 and 14:23 `[T]`, verified.
- **"My blood of the covenant, poured out for many."** τὸ αἷμά μου τῆς διαθήκης τὸ ἐκχυννόμενον ὑπὲρ πολλῶν (14:24). διαθήκη ("covenant") occurs only here in Mark, and ἐκχέω ("to pour out") only here `[T]`, verified. There is no καινή ("new") before διαθήκη in the SBLGNT or NA28; the Majority text adds τῆς καινῆς (NA28 apparatus, verified). The NASB95 and ESV both omit "new". καινόν ("new") comes in the next verse instead, of the wine in the kingdom (14:25).
- **The last δεῖ is Peter's.** Ἐὰν δέῃ με συναποθανεῖν σοι ("if I must die with you", 14:31). The book's six uses of δεῖ ("must") end in Peter's mouth, using the word of Jesus' passion predictions (8:31) for a death he will not die `[T]`, verified.

**Tool 11.**

**Exod 24:8 (with Zech 9:11) → 14:24** *(high)*. *Source context:* at Sinai Moses reads the book of the covenant, the people answer "all that the LORD has spoken we will do", and he throws the blood on them: "behold, the blood of the covenant (דַם־הַבְּרִית, "blood of the covenant") which the LORD has made with you" `[T]`. Moses and the elders then see God and eat and drink (24:9–11). *Book usage:* Exod 24 stood behind the transfiguration (9:2–7). *OT-to-OT:* Zech 9:11, "because of the blood of your covenant I will set your prisoners free", reuses the Sinai phrase for the king who comes on a colt (9:9, used at 11:2–7) `[T]`, verified in Swete. *What it adds:* the covenant is remade in his blood, and the Sinai meal of 24:11 is present at this table.

**Isa 53:12 → 14:24** *(moderate–high — "many" plus "pour out")*. *Source context:* see unit 23. The Hebrew of 53:12 has הֶעֱרָה לַמָּוֶת נַפְשׁוֹ ("he poured out his soul to death") and חֵטְא־רַבִּים נָשָׂא ("he bore the sin of many") `[T]`. *Book usage:* 10:45 ("many"). *OT-to-OT:* Exod 24 and Isa 53 — the covenant sacrifice and the Servant's self-offering — are joined in one sentence. *What it adds:* the covenant blood is the Servant's soul poured out.

**Zech 13:7 → 14:27** *(high — formula quotation)*. *Source context:* "Awake, O sword, against my shepherd, against the man who stands next to me … strike the shepherd, and the sheep will be scattered; I will turn my hand against the little ones." Two-thirds perish and a third is refined: "they will call upon my name, and I will answer them; I will say, 'They are my people'" (13:8–9) `[T]`. *Book usage:* Zechariah is live (9:9; 14:4); the shepherd was named at 6:34 (Num 27:17). *OT-to-OT:* Zech 13:7 continues Zech 11 (the rejected shepherd valued at thirty pieces of silver) and 12:10 ("they will look on me, whom they have pierced") *(uncertain for Mark's use)*. **Triage:** category 3 — Mark's singular "I will strike the shepherd" follows the Hebrew against the plural of both Swete and Rahlfs, with a BHS apparatus note proposing the first person (see the overview). *What it adds:* the striking is God's act, and the scattering is followed by a refined remnant — which the next verse promises in its own way: "after I am raised, I will go ahead of you to Galilee" (14:28).

**Ps 41:10 → 14:18** *(moderate–high)*. Move 1: the psalmist's trusted friend "who ate my bread has lifted his heel against me", in a psalm that ends in vindication (41:11–13).

*Internal:* **answers §6:34** — the shepherd (high, verified). **Answers §6:41; 8:6** — the meal verbs (high). **Answers §10:45** — "many" (high). **Answers §10:38–39** — the cup (high). **Plants §16:7** — "as he said" (high, verified). **Answers §8:31** — δεῖ (moderate–high). **Answers §2:22** — new wine (moderate). **Plants §14:50** — the scattering fulfilled (high).

**Translations.** At 14:24 NASB95 "which is poured out for many" and ESV "which is poured out for many". At 14:25 the NASB95 has "I will never again drink" and the ESV "I will not drink again" for οὐκέτι οὐ μὴ πίω ("I will no longer, never, drink"), a strong double negative. **Pulpit divergence:** none bearing.

**Pitfall.** Preaching the Supper as a memorial of an example. The words are "blood of the covenant" and "for many", so the Supper interprets a sacrifice. The corrective: preach 14:22–25 with 10:45 and Exod 24.

---

## 32. Mark 14:32–52 — Gethsemane: The Cup and the Watch ⭐

**Position.** *Q1:* the Son has predicted his death, the disciples' flight, and Peter's denial (14:27–31), and has told them to watch (13:33–37). *Q2:* in Gethsemane the Son prays to the Father for whom "all things are possible" and receives no removal of the cup, while the disciples sleep through the watches. Then the betrayer arrives and everyone flees `[T]`.

**Structure.** Arrival and the three (32–34); the prayer (35–36); three returns to sleeping disciples (37–41a); "the hour has come" (41b–42); the kiss and the arrest (43–46); the sword, the protest, the fulfilment (47–49); the flight and the young man (50–52).

**Text-first findings.**

- **Jesus' distress.** ἤρξατο ἐκθαμβεῖσθαι καὶ ἀδημονεῖν ("he began to be greatly distressed and troubled", 14:33). ἐκθαμβέομαι ("to be distressed, astonished") occurs in the New Testament only in Mark: of the crowd at 9:15, of Jesus here, and of the women at the tomb (16:5, 6) `[T]`, verified. ἀδημονέω ("to be troubled") occurs only here in Mark.
- **"My soul is very sorrowful, to death."** Περίλυπός ἐστιν ἡ ψυχή μου ἕως θανάτου (14:34). The refrain of Ps 42–43 (Swete 41:6, 12; 42:5: ἵνα τί περίλυπος εἶ, ψυχή, "why are you very sorrowful, O soul?") and Jonah 4:9 Swete: σφόδρα λελύπημαι ἐγὼ ἕως θανάτου ("I am very grieved, to death") `[T]`, verified *(moderate–high for the psalm, moderate for Jonah)*. The second Jonah contact in the book (with 4:35–41). περίλυπος ("very sorrowful") was last used of Herod (6:26) `[T]`.
- **"Abba, Father, all things are possible for you."** Αββα ὁ πατήρ, πάντα δυνατά σοι· παρένεγκε τὸ ποτήριον τοῦτο ἀπ' ἐμοῦ· ἀλλ' οὐ τί ἐγὼ θέλω ἀλλὰ τί σύ ("Abba, Father, all things are possible for you; remove this cup from me; yet not what I will, but what you will", 14:36) `[T]`. Αββα is the third Aramaic saying kept in the passion (with 15:22 Golgotha and 15:34 Eloi). "All things are possible" answers 9:23 and 10:27 (see unit 19). θέλω ("to will"): the leper's "if you will" and Jesus' "I will" (1:40–41) end here in "not what I will" `[T]`.
- **The watches, and Simon.** Σίμων, καθεύδεις; οὐκ ἴσχυσας μίαν ὥραν γρηγορῆσαι; ("Simon, are you asleep? Could you not watch one hour?", 14:37). This is the only time after 3:16 that Jesus calls Peter "Simon" `[T]`, verified: the name he had before he was named. οὐκ ἴσχυσας ("you were not able") echoes the disciples' οὐκ ἴσχυσαν ("they were not able") at 9:18 `[T]`. γρηγορέω ("to watch") three times here (14:34, 37, 38), after three times in 13:34–37 `[T]`, verified.
- **"Rise, let us go."** ἐγείρεσθε ἄγωμεν (14:42). ἄγωμεν ("let us go") occurs only at 1:38, "let us go elsewhere … that I may preach there too", and here `[T]`, verified. The mission's first "let us go" and its last.
- **The hour.** ἦλθεν ἡ ὥρα ("the hour has come", 14:41), for which he prayed that it might pass (14:35) `[T]`. The hours of the crucifixion follow: third, sixth, ninth (15:25, 33, 34) `[T]`.
- **Leaving him, they fled.** ἀφέντες αὐτὸν ἔφυγον πάντες ("leaving him, they all fled", 14:50). The first disciples ἀφέντες τὰ δίκτυα ἠκολούθησαν αὐτῷ ("leaving their nets, followed him", 1:18; 1:20) `[T]`, verified. **The call and the flight use the same participle, with the objects reversed.**
- **The naked young man.** 14:51–52 (see the overview's echo table). Amos 2:16: "the one who is stout of heart among the mighty shall flee away naked in that day". The Hebrew is עָרוֹם יָנוּס ("naked he will flee"); both Swete and Rahlfs have ὁ γυμνὸς διώξεται ("the naked one will pursue"). Mark's γυμνὸς ἔφυγεν ("naked, he fled") matches the Hebrew verb, נוּס ("to flee", verified by lemma at Amos 2:16), and not the Greek `[T]` *(moderate — another Hebrew-side contact; see the overview's note on Mark's Hebrew)*.

**Tool 11.**

**Ps 42:6, 12; 43:5 → 14:34** *(high)*. *Source context:* the Korahite lament of one far from the temple, taunted "where is your God?", whose refrain turns to hope: "hope in God, for I shall again praise him". *Book usage:* first use. *OT-to-OT:* Jonah 4:9's "grieved to death" belongs to another sufferer who argues with God *(moderate)*. *What it adds:* the Son prays the psalm of the exile from God's presence, on the night before his dereliction (15:34).

**Isa 51:17, 22 → 14:36** *(moderate — the cup)*. Move 1: Jerusalem has drunk the cup of the LORD's wrath, and the LORD says, "I have taken from your hand the cup of staggering … you shall drink no more" `[T]`. The cup removed from Jerusalem is the cup the Son asks to be removed, and drinks.

**Amos 2:16 → 14:52** *(moderate)*. Move 1: the oracle against Israel, in which on the day of the LORD's judgement even the bravest will flee naked.

*Internal:* **answers §13:33–37** — the watches (high, verified). **Answers §9:23; 10:27** — "all things possible" (moderate–high). **Answers §10:38** — the cup (high). **Answers §1:18, 20** — ἀφέντες (high, verified). **Answers §1:38** — ἄγωμεν (moderate, verified). **Plants §16:5–6** — ἐκθαμβέομαι, νεανίσκος ("young man"), περιβάλλω ("to wrap") (high, verified). **Answers §14:27** — the scattering (high). **Answers §11:17** — λῃστής ("robber", 14:48) (high).

**Translations.** At 14:33 the NASB95's "very distressed" and the ESV's "greatly distressed" both render ἐκθαμβεῖσθαι. At 16:5 both have different words ("amazed"/"alarmed"), so the link is lost. At 14:51 NASB95 "linen sheet" / ESV "linen cloth". **Pulpit divergence:** neither version keeps the σινδών ("linen cloth") link. The NASB95 moves from "linen sheet" (14:51–52) to "linen cloth" (15:46); the ESV from "linen cloth" to "linen shroud". The congregation will not hear that the young man's garment and Jesus' grave-cloth are one word unless it is pointed out.

**Pitfall.** Preaching Gethsemane as a model of resignation ("say 'your will be done'"). The prayer is the Son's own agony over *this* cup, and the disciples' failure is the book's warning. The corrective: preach the Son who alone watches and prays, and the disciples who sleep.

---

## 33. Mark 14:53–72 — The Confession and the Denial

**Position.** *Q1:* Jesus is arrested and the disciples have fled; Peter follows "from a distance" (14:54). *Q2:* the unit is the book's last sandwich `[T]`. Peter is placed in the courtyard (14:54), the trial happens inside (14:55–65), and Peter's denials complete the frame (14:66–72). Jesus confesses who he is, and Peter denies knowing him — at the same hour, in the same house.

**Structure.** *Opened:* Peter at the fire (53–54). *Inside:* false witnesses, the temple saying, silence, the high priest's question, "I am", the verdict, the mockery (55–65). *Closed:* three denials and the second cock-crow (66–72).

**Text-first findings.**

- **Following from a distance.** ἀπὸ μακρόθεν ἠκολούθησεν αὐτῷ ("he followed him from a distance", 14:54). ἀκολουθέω ("to follow") of a disciple for the last time. The next use is of the women, who "followed him and served him" in Galilee (15:41) `[T]`, verified.
- **False witness.** ἐψευδομαρτύρουν ("they bore false witness", 14:56, 57) — the commandment Jesus quoted to the rich man (10:19) broken by the court `[T]`, verified.
- **The temple saying.** "I will destroy this ναόν ("sanctuary") made with hands, and in three days build another not made with hands" (14:58) — see the overview on ναός (14:58; 15:29, 38). διὰ τριῶν ἡμερῶν ("in three days") echoes the passion predictions' "after three days" `[T]`.
- **"You are …" — the book's five Σὺ εἶ.** Σὺ εἶ ὁ χριστὸς ὁ υἱὸς τοῦ εὐλογητοῦ; ("are you the Christ, the Son of the Blessed?", 14:61). Σὺ εἶ ("you are") stands at 1:11 (the Voice: "you are my beloved Son"), 3:11 (the spirits: "you are the Son of God"), 8:29 (Peter: "you are the Christ"), 14:61 (the high priest's question) and 15:2 (Pilate: "are you the King of the Jews?") `[T]`, verified. The high priest's question combines Peter's title and the Voice's. The Voice declares, the spirits cry, Peter confesses, and the judges ask.
- **"I am."** Ἐγώ εἰμι (14:62). The only unqualified "I am" to the title question in the book. He then adds Ps 110:1 and Dan 7:13: ὄψεσθε ("you will see") `[T]`.
- **"Guilty of death."** κατέκριναν αὐτὸν ἔνοχον εἶναι θανάτου ("they condemned him as guilty of death", 14:64). ἔνοχος ("guilty") occurs only at 3:29 — ἔνοχός ἐστιν αἰωνίου ἁμαρτήματος ("is guilty of an eternal sin"), of those who attribute his work to an unclean spirit — and here `[T]`, verified. **Those who condemn him for blasphemy stand where 3:29 put the blasphemers.** *Moderate–high*.
- **"Prophesy!"** Προφήτευσον ("prophesy!", 14:65). They mock him as a prophet while, outside, his prophecy about Peter is being fulfilled (14:30, 72) `[I]`, high — the irony is structural. προφητεύω ("to prophesy") occurs only here and at 7:6 ("well did Isaiah prophesy of you") `[T]`, verified.
- **The denials.** ἠρνήσατο … ἠρνεῖτο ("he denied … he was denying", 14:68, 70); ἀναθεματίζειν καὶ ὀμνύναι ("to curse and to swear", 14:71). ὀμνύω ("to swear") was last used of Herod's oath (6:23) `[T]`, verified. Οὐκ οἶδα τὸν ἄνθρωπον τοῦτον ("I do not know this man", 14:71): the one who confessed "you are the Christ" now calls him "this man".
- **He remembered the word.** ἀνεμνήσθη ὁ Πέτρος τὸ ῥῆμα ("Peter remembered the saying", 14:72). ἀναμιμνῄσκω ("to remember") occurs at 11:21 (Peter remembers the fig tree) and here; ῥῆμα ("saying") at 9:32 (the saying they did not understand) and here `[T]`, verified. ἐπιβαλὼν ἔκλαιεν ("having thrown himself down / having thought on it, he wept", 14:72) — the participle is a known crux `[S]`.

**Tool 11.**

**Ps 110:1 + Dan 7:13 → 14:62** *(high)*. *Source context:* see units 27 and 4. *Book usage:* Ps 110 at 12:36; Dan 7 at 2:10, 8:38 and 13:26. *OT-to-OT:* both texts enthrone a figure beside God — at the right hand (Ps 110), before the Ancient of Days (Dan 7) — and Mark joins the two enthronements. *What it adds:* before the court that condemns him, Jesus claims both thrones, and the court will "see" it.

**Isa 53:7; 50:6 → 14:61, 65** *(moderate)*. Move 1: the Servant silent "like a sheep before its shearers", and the Servant who gave his back to the smiters and did not hide his face from spitting (ἐμπτυσμάτων, "spitting", Isa 50:6 Swete) `[T]`.

*Internal:* **answers §3:29** — ἔνοχος and blasphemy (moderate–high, verified). **Answers §10:19** — false witness (moderate). **Answers §8:29; 1:11** — Σὺ εἶ (high, verified). **Answers §14:30** — the prophecy fulfilled (high). **Answers §6:23** — ὀμνύω (moderate). **Answers §10:34** — ἐμπτύω ("to spit on") (high, verified). **Plants §16:7** — "and Peter" (high).

**Translations.** At 14:68 the **ESV** includes "and the rooster crowed" and the **NASB95** omits it. NA28 prints [καὶ ἀλέκτωρ ἐφώνησεν] in brackets, and the phrase is absent from א B L W `[T]`, verified in the apparatus. **Pulpit divergence:** the congregation will hear a first crowing that the NASB95 reader does not see — and 14:72's "a second time" presupposes it, so the ESV reads more consistently. At 14:72 the NASB95's "he began to weep" and the ESV's "he broke down and wept" both interpret ἐπιβαλών.

**Pitfall.** Preaching Peter's denial as a warning to try harder. The unit sets Peter's failure beside Jesus' confession, and the book answers Peter's failure with "and Peter" (16:7). The corrective: preach Jesus' faithfulness as the ground of Peter's restoration.

---

## 34. Mark 15:1–20 — The King of the Jews

**Position.** *Q1:* the council has condemned him (14:64). *Q2:* the plot of 3:6 is carried out through the Roman governor. The title Jesus never uses of himself — King of the Jews — becomes the charge, the choice, the mockery and, by 15:26, the inscription `[T]`.

**Structure.** The council at dawn, and Pilate's question (1–5); Barabbas (6–15); the soldiers' mock homage (16–20).

**Text-first findings.**

- **The plot's word.** συμβούλιον ποιήσαντες ("having held a council", 15:1). συμβούλιον ("council, plot") occurs only at 3:6 — the Pharisees' plot with the Herodians after the Sabbath healing — and here `[T]`, verified. **The plot hatched in 3:6 is carried out in 15:1.** *High*.
- **Bound and handed over.** δήσαντες … παρέδωκαν Πιλάτῳ ("having bound … they handed him over to Pilate", 15:1) — the binder of the strong man (3:27) bound; the third passion prediction's "hand him over to the Gentiles" (10:33) fulfilled `[T]`.
- **Accused.** κατηγόρουν αὐτοῦ ("they were accusing him", 15:3, 4). κατηγορέω ("to accuse") occurs only at 3:2 — they watched him ἵνα κατηγορήσωσιν αὐτοῦ ("so that they might accuse him"), in the synagogue on the Sabbath — and here `[T]`, verified. *High, with the preceding item*: the first cycle's ending (3:1–6) is the passion's beginning.
- **Silence and wonder.** οὐκέτι οὐδὲν ἀπεκρίθη, ὥστε θαυμάζειν τὸν Πιλᾶτον ("he no longer answered anything, so that Pilate was amazed", 15:5) `[T]`. Isa 53:7 (the silent Servant) *(moderate)*.
- **King of the Jews, five times in this chapter.** 15:2, 9, 12, 18, 26 — and "King of Israel" at 15:32. βασιλεύς ("king") is used of Jesus only in chapter 15 `[T]`, verified (see unit 12).
- **What evil?** Τί γὰρ ἐποίησεν κακόν; ("why, what evil has he done?", 15:14). The first controversy cycle asked "is it lawful … to do good or to do evil (κακοποιῆσαι)?" (3:4) `[T]` *(moderate)*.
- **Mock homage.** Crown, purple, Χαῖρε, βασιλεῦ τῶν Ἰουδαίων ("Hail, King of the Jews"), a reed to the head, spitting, kneeling, προσεκύνουν αὐτῷ ("they bowed down to him", 15:17–19) `[T]`. προσκυνέω ("to bow down") occurs only at 5:6 (Legion) and 15:19 `[T]`, verified. ἐμπτύω ("to spit on") fulfils 10:34 `[T]`, verified.
- **Latin in the soldiers' scene.** φραγελλώσας ("having flogged", 15:15); πραιτώριον ("praetorium", 15:16); σπεῖρα ("cohort", 15:16) `[T]` (see the overview).

**Tool 11.** **Isa 50:6; 53:7 → 15:5, 19** *(moderate)*. See units 23 and 33. *What it adds:* the Servant's silence and shame are enacted before a Gentile court.

*Internal:* **answers §3:6** — συμβούλιον (high, verified). **Answers §3:2** — κατηγορέω (high, verified). **Answers §3:27** — binding (moderate). **Answers §10:33–34** — handed over, mocked, spat on, flogged (high, verified). **Answers §6:14–29** — the second king (moderate). **Answers §5:6** — προσκυνέω (moderate). **Plants §15:26** — the title (high).

**Translations.** At 15:16 the ESV's "the palace (that is, the governor's headquarters)" hides πραιτώριον ("praetorium"); the NASB95's "the Praetorium" keeps the Latin. At 15:2 the NASB95 has "It is as you say" and the ESV "You have said so" for Σὺ λέγεις ("you say"). The ESV is more literal and keeps the ambiguity. **Pulpit divergence:** 15:2 — the ESV is better. 15:16 — a detail only.

**Pitfall.** Preaching the crowd as fickle ("Hosanna on Sunday, crucify on Friday"). Mark's crowd at 11:9 is "those going before and those following", Jesus' company, and the crowd at 15:8–15 is "stirred up" by the chief priests (15:11). The corrective: preach the chief priests' envy (φθόνος, "envy", 15:10) and the governor's wish to satisfy the crowd — the powers, not the fickle masses, drive the scene.

---

## 35. Mark 15:21–41 — The Cross, the Veil, the Confession ⭐

**Position.** *Q1:* the King of the Jews has been mocked and led out (15:16–20). *Q2:* the crucifixion is the book's climax. The Son is disclosed a third time, by a torn veil and a human confession (see the overview's arc map), at the moment of his death. Every major thread converges here — the book's question of identity, its necessity, its Scriptures and its vocabulary `[I]`, high.

**Structure.** Simon carries the cross (21); Golgotha, wine, the garments (22–24); the third hour, the inscription, the robbers (25–27); three mockeries (29–32); darkness, sixth to ninth hour (33); the cry and Elijah misheard (34–36); death, the veil, the confession (37–39); the women watching from a distance (40–41).

**Text-first findings.**

- **Simon takes up the cross.** ἵνα ἄρῃ τὸν σταυρὸν αὐτοῦ ("so that he might carry his cross", 15:21) — the words of the disciple's call, ἀράτω τὸν σταυρὸν αὐτοῦ ("let him take up his cross", 8:34) `[T]`, verified. A passer-by, not a disciple, does it.
- **Told in the words of Psalm 22.** διαμερίζονται τὰ ἱμάτια αὐτοῦ, βάλλοντες κλῆρον ("they divide his garments, casting lots", 15:24; Ps 22:19); κινοῦντες τὰς κεφαλὰς αὐτῶν ("wagging their heads", 15:29; Ps 22:8; Lam 2:15); σῶσον σεαυτόν ("save yourself", 15:30; Ps 22:9 Swete σωσάτω αὐτόν, "let him save him"); Ἐλωῒ ἐλωῒ λεμὰ σαβαχθάνι (15:34; Ps 22:2) `[T]`, verified in Swete. Only the last is marked as speech, and none is marked as a quotation *(high for 15:24, 34; moderate–high for 15:29–30)*.
- **The inscription.** ἡ ἐπιγραφὴ τῆς αἰτίας αὐτοῦ ("the inscription of the charge against him", 15:26). ἐπιγραφή ("inscription") occurs only here and at 12:16, on Caesar's coin `[T]`, verified.
- **Right and left.** ἕνα ἐκ δεξιῶν καὶ ἕνα ἐξ εὐωνύμων αὐτοῦ ("one on his right and one on his left", 15:27), answering James and John (10:37, 40) `[T]`, verified. δύο λῃστάς ("two robbers") — the den of robbers (11:17) and the robber arrested (14:48) `[T]`, verified.
- **"He saved others."** Ἄλλους ἔσωσεν, ἑαυτὸν οὐ δύναται σῶσαι ("he saved others; himself he cannot save", 15:31). σῴζω ("to save") has been used of his healings (5:23, 28, 34; 6:56; 10:52), and of the saving and losing of one's life (3:4; 8:35) `[T]`, verified. **The mockery is true in both clauses: he saved others, and he cannot save himself if he is to save them (8:35; 10:45).** `[I]`, high.
- **"That we may see and believe."** ἵνα ἴδωμεν καὶ πιστεύσωμεν ("so that we may see and believe", 15:32) — the sign demanded at 8:11–12 and refused `[T]`/`[I]`.
- **Darkness over the whole land.** 15:33 (Amos 8:9; see unit 29) `[T]`.
- **The cry, translated.** ὅ ἐστιν μεθερμηνευόμενον ("which is translated", 15:34) — the third translated Aramaic saying (5:41; 15:22, 34). Mark's Greek translation does not follow the LXX (see the overview) `[T]`. The bystanders hear Ἠλίαν φωνεῖ ("he is calling Elijah", 15:35). The book has already said that Elijah has come and suffered (9:13): no Elijah will come to take him down `[I]`, high.
- **Take him down.** καθελεῖν αὐτόν ("to take him down", 15:36). καθαιρέω ("to take down") occurs only here and at 15:46, καθελὼν αὐτόν ("having taken him down") — Joseph does it `[T]`, verified. *Moderate*: the mockery's "take him down" is answered only by the burial.
- **Death, veil, confession.** See the overview (the σχίζω / ἐκπνέω / φωνή / υἱός frame with 1:10–11) `[T]`, verified. ὅτι οὕτως ἐξέπνευσεν ("that he breathed his last *in this way*", 15:39) — the centurion confesses on seeing the *manner* of the death `[T]`. NA28 and the SBLGNT print the shorter reading; the Majority text adds κράξας ("having cried out") (NA28 apparatus, verified).
- **Women from a distance, and what they did in Galilee.** θεωροῦσαι ("watching", 15:40); ἀπὸ μακρόθεν ("from a distance", Ps 38:12 Swete 37:12, μακρόθεν ἔστησαν, "they stood far off"); ἠκολούθουν αὐτῷ καὶ διηκόνουν αὐτῷ ("they followed him and served him", 15:41) `[T]`, verified. The two verbs of discipleship, following and serving, are given to women at the cross, not to the Twelve `[T]`.

**Tool 11.**

**Ps 22 (Swete 21) → 15:24, 29–31, 34** *(high)*. *Source context:* the lament of the righteous sufferer. "My God, my God, why have you forsaken me?" (22:2); mocked, "all who see me mock me … they wag their heads, 'He trusted in the LORD; let him deliver him'" (22:8–9); encircled, pierced, his garments divided (22:17–19). The psalm then turns: "you have answered me" (22:22), praise in the congregation (22:23–27), "all the ends of the earth shall turn to the LORD … all the families of the nations shall worship before you" (22:28) `[T]`. *Book usage:* ἐξουδενηθῇ ("be treated with contempt", 9:12) may already point to Ps 22:7 *(uncertain)*. *OT-to-OT:* Ps 22 and Isa 53 both tell of a sufferer despised and then vindicated before the nations. The two have been joined throughout the passion (Isa 53 at 10:45; 14:24; 15:5; Ps 22 here). *What it adds:* the psalm's first line is the cry, and its last movement — the nations turning — is enacted in the Gentile centurion's confession two verses after the cry `[I]`, high. **The confession of 15:39 is the answer Ps 22:28 promised.**

**Amos 8:9 → 15:33** *(moderate)*. Move 1: "I will make the sun go down at noon and darken the earth in broad daylight … I will make it like the mourning for an only son (כְּאֵבֶל יָחִיד, "like mourning for an only son")" (Amos 8:9–10) `[T]`, יָחִיד ("only one") verified by lemma (3173) at Amos 8:10 and Gen 22:2 (WLC). The same word as Gen 22:2's יְחִידְךָ ("your only one"), which the LXX renders ἀγαπητός ("beloved") at Gen 22:2 and at Amos 8:10 too (Swete ὡς πένθος ἀγαπητοῦ, "as mourning for a beloved one", verified). ἀγαπητός is the Voice's word at 1:11 and 9:7, and the owner's at 12:6 (its only three uses in Mark, SBLGNT) *(moderate — synthetic)*.

**Ps 69:22 (Swete 68:22) → 15:36** *(moderate–high)*. Move 1: "for my thirst they gave me sour wine to drink" — the persecuted righteous one whose zeal for God's house has consumed him (69:10).

**Ps 38:12 (Swete 37:12) → 15:40** *(moderate)*. Move 1: "my friends and companions stand aloof; my neighbours stand far off".

*Internal:* **answers §1:10–11** — the frame (high, verified). **Answers §8:34** — the cross carried (moderate–high, verified). **Answers §10:37–40** — right and left (high, verified). **Answers §11:17; 14:48** — robbers (high). **Answers §12:16** — ἐπιγραφή (moderate–high). **Answers §3:4; 5:34; 8:35** — σῴζω (high). **Answers §8:11–12** — the sign (moderate). **Answers §9:11–13** — Elijah (high). **Answers §1:13, 31; 10:45** — διακονέω (moderate–high). **Plants §15:46** — καθαιρέω (moderate).

**Translations.** At 15:39 NASB95 "the Son of God" and ESV "the Son of God" (see the overview on the anarthrous υἱὸς θεοῦ). At 15:37 NASB95 "breathed His last" and ESV "breathed his last". Both hide the πνεῦμα ("spirit") of ἐξέπνευσεν ("he breathed out"). At 15:38 NASB95 "veil" and ESV "curtain". **Pulpit divergence:** at 15:28 the NASB95 prints the Isa 53:12 citation in brackets and the ESV omits it; the ESV follows the critical text.

**Pitfall.** Answering the cry of dereliction with the end of Ps 22 before letting it stand (see the overview's Trap 5). The corrective: the psalm's end is enacted in the narrative (15:38–39), not supplied by the preacher's gloss.

---

## 36. Mark 15:42–16:8 — He Is Going Ahead of You ⭐

**Position.** *Q1:* the Son has died, and the centurion has confessed him. *Q2:* the burial establishes the death (a corpse, a council member, a centurion's confirmation, a stone), and the tomb scene announces the resurrection without narrating an appearance. The book ends on the promise "you will see him, as he told you" and on the women's fear. It leaves the reader where the book began: at a "beginning" (1:1) `[T]`/`[I]`.

**Structure.** Joseph and Pilate (15:42–45); the burial and the women watching (15:46–47); the Sabbath past; spices; the stone (16:1–4); the young man and the message (16:5–7); the flight, silence and fear (16:8).

**Text-first findings.**

- **The death certified.** Pilate ἐθαύμασεν εἰ ἤδη τέθνηκεν ("was amazed whether he was already dead"), summons the κεντυρίων ("centurion"), and learns it; he grants τὸ πτῶμα ("the corpse", 15:44–45) `[T]`. The centurion who confessed (15:39) now certifies the death `[T]`. The Latin loanword κεντυρίων ("centurion") occurs three times (15:39, 44, 45) `[T]`, verified.
- **Joseph "dared".** τολμήσας ("having dared", 15:43). τολμάω ("to dare") occurs only here and at 12:34, οὐδεὶς οὐκέτι ἐτόλμα αὐτὸν ἐπερωτῆσαι ("no one dared any longer to question him") `[T]`, verified. Joseph was προσδεχόμενος τὴν βασιλείαν τοῦ θεοῦ ("waiting for the kingdom of God", 15:43) — the kingdom announced at 1:15 `[T]`.
- **Wrapped and laid.** ἐνείλησεν τῇ σινδόνι … ἔθηκεν αὐτὸν ἐν μνημείῳ ὃ ἦν λελατομημένον ἐκ πέτρας ("he wrapped him in the linen cloth … laid him in a tomb hewn out of rock", 15:46) `[T]`. Isa 22:16 (Shebna's hewn tomb) and Isa 53:9 ("with a rich man in his death") are *uncertain*; Mark gives no hint of either.
- **The women watch.** θεωροῦσαι ("watching", 15:40); ἐθεώρουν ποῦ τέθειται ("they were watching where he was laid", 15:47); θεωροῦσιν ὅτι ἀποκεκύλισται ὁ λίθος ("they see that the stone has been rolled away", 16:4) `[T]`. The women are the witnesses of death, burial and empty tomb `[T]`.
- **To anoint him.** ἵνα ἐλθοῦσαι ἀλείψωσιν αὐτόν ("so that they might come and anoint him", 16:1) — the anointing already done "beforehand for burial" (14:8) `[T]`.
- **"When the sun had risen."** ἀνατείλαντος τοῦ ἡλίου (16:2). The sun that was darkened (15:33) has risen `[T]`/`[I]` *(moderate)*.
- **The young man in white.** νεανίσκον καθήμενον ἐν τοῖς δεξιοῖς περιβεβλημένον στολὴν λευκήν ("a young man sitting on the right, wrapped in a white robe", 16:5) — see the overview's echo table. ἐν τοῖς δεξιοῖς ("on the right") recalls the right hand of 12:36, 14:62 and the request of 10:37 `[T]` *(uncertain as design)*.
- **The message.** "You seek Jesus the Nazarene, **τὸν ἐσταυρωμένον**" ("the one who has been crucified", a perfect participle: crucified, and still the crucified one); "ἠγέρθη ("he has been raised"); he is not here; see the place where they laid him" (16:6) `[T]`. "Go, tell his disciples *and Peter* that he is going ahead of you (προάγει) to Galilee; there you will see him, καθὼς εἶπεν ὑμῖν ("as he told you")" (16:7) — the third "as he said" (see unit 31) `[T]`, verified.
- **The ending.** ἔφυγον … εἶχεν γὰρ αὐτὰς τρόμος καὶ ἔκστασις· καὶ οὐδενὶ οὐδὲν εἶπαν, ἐφοβοῦντο γάρ ("they fled … for trembling and astonishment had seized them; and they said nothing to anyone, for they were afraid", 16:8) `[T]`. ἔφυγον ("they fled") is the disciples' verb (14:50) and the young man's (14:52). τρόμος ("trembling") answers the healed woman's τρέμουσα ("trembling", 5:33), and ἔκστασις ("astonishment") the raising of the girl, ἐξέστησαν … ἐκστάσει μεγάλῃ ("they were utterly astonished", 5:42) — ἔκστασις occurs only at 5:42 and 16:8. "Nothing to anyone" reverses 1:44. And ἐφοβοῦντο ("they were afraid") answers 4:41 `[T]`, each verified.

**Tool 11.** No quotation. **The allusive weight lies in the book itself** — this pericope is Move 4's densest. For Mal 3:20 (Swete 4:2, "the sun of righteousness shall rise") behind 16:2 *(uncertain)*, Move 1 only: the day of the LORD for those who fear his name. The book does not quote it.

*Internal:* see the overview's echo table, where more than a third of the rows resolve here. In summary: **answers §14:8** (anointing); **§14:28** (going ahead; "as he said"); **§14:51–52** (the young man; linen; flight); **§14:72; 8:34** ("and Peter"); **§4:41; 5:33, 42** (fear, trembling, astonishment); **§1:44** (nothing to anyone); **§1:24** (the Nazarene); **§1:37** (seeking); **§15:33** (the sun) — each verified or flagged at its row.

**Translations.** NASB95 "He has risen"; ESV "He has risen" (16:6) — for ἠγέρθη ("he has been raised"), an aorist passive. Both render it as active. At 16:5–6 NASB95 "amazed … Do not be amazed" and ESV "alarmed … Do not be alarmed" — see unit 32. **Pulpit divergence:** "He has risen" and "he has been raised" are both acceptable renderings, but the passive keeps the agency with God (compare 14:28, μετὰ τὸ ἐγερθῆναί με, "after I have been raised").

**Pitfall.** See the overview's Trap 6. The ending is not a failure of nerve. It is a promise the reader has twice seen Jesus keep (11:6; 14:16), set against a fear the reader has seen before (4:41) — and the book calls itself a "beginning". The corrective: preach 16:7 as the hinge of the ending, and 16:8 as the question it leaves with the hearer.

---

## 37. [Mark 16:9–20] — The Longer Ending

**Status.** Double-bracketed in the SBLGNT and NA28; bracketed in the NASB95 and ESV, with a note in the ESV. The external evidence is set out in the overview. This section records only what the text-first sweep observed.

**Text-first findings — style.** The following lemmas occur in 16:9–20 and **nowhere in 1:1–16:8** (SBLGNT index, verified):

- πορεύομαι ("to go"; 16:10, 12, 15);
- θεάομαι ("to see"; 16:11, 14);
- ἀπιστέω ("to disbelieve"; 16:11, 16);
- ἕτερος ("other"; 16:12);
- μορφή ("form"; 16:12);
- ὕστερον ("later"; 16:14);
- παρακολουθέω ("to accompany"; 16:17);
- ἐπακολουθέω ("to follow"; 16:20);
- συνεργέω ("to work with"; 16:20);
- βεβαιόω ("to confirm"; 16:20);
- ὄφις ("serpent"; 16:18);
- ἀναλαμβάνω ("to take up"; 16:19).

The narrator calls Jesus ὁ κύριος ("the Lord", 16:19–20). In 1:1–16:8 the narrator never does: every "the Lord" there is in someone's speech (5:19; 11:3; 12:9; 13:35) `[T]`, verified. εὐθύς ("immediately"), used as an adverb 41 times in 1:1–16:8 (SBLGNT; the adjective at 1:3 excluded), does not occur `[T]`, verified. This is style evidence only; it neither proves nor disproves authorship `[I]`. It is consistent with the external evidence.

**Text-first findings — content.** The passage gathers material from other books:

- the appearance to Mary Magdalene, from whom seven demons had gone out (Luke 8:2; John 20:14–18);
- the two walking in the country (Luke 24:13–35);
- the rebuke of unbelief and σκληροκαρδία ("hardness of heart"; Mark 10:5);
- the commission to preach to all creation;
- signs, including tongues and serpents (Acts 2:4; 28:3–6);
- the ascension to the right hand (Ps 110:1).

`[T]` for the Markan parallels, `[S]` for the claim that it was compiled from the other Gospels.

**Pitfall.** See the overview's Trap 6 and the textual-variants catalogue: do not build doctrine on 16:17–18. If the passage is read in public, say what it is.

---

## Cross-Passage Convergent Findings

These only become visible when the pericopes are read in sequence. **Every item here is synthetic.** Items marked *verified* have had every reference in them checked by lemma against the SBLGNT index; for the Old Testament side, the check was against Swete, Rahlfs and the WLC. Items not marked verified are capped at moderate confidence and are the first things a claim audit should test.

**1. The watches and the undoing of the call — 13:34–37 → 14:17–15:1; 1:18, 20 → 14:50; 1:38 → 14:42.** *Verified.*

- **The watches.** γρηγορέω ("to watch") occurs at 13:34, 35, 37 and at 14:34, 37, 38, and nowhere else. ἀλεκτοροφωνία ("cockcrow", 13:35) is a New Testament hapax. The four watches of 13:35 structure the passion night: evening (14:17), night, cockcrow (14:68, 72) and dawn (15:1).
- **The call undone.** The first disciples left their nets and followed (ἀφέντες, "leaving", 1:18, 20). At the arrest, ἀφέντες αὐτὸν ἔφυγον πάντες ("leaving him, they all fled", 14:50). Jesus' first ἄγωμεν ("let us go") went out to preach (1:38); his last goes out to meet the betrayer (14:42). The name "Simon", unused by Jesus since 3:16, comes back at 14:37 for the sleeping Peter.
- **What the sequence shows.** Mark tells the passion night through the discourse's watches. Every step the first disciples took towards Jesus in chapter 1 is reversed in chapter 14. The book answers the reversal only with "and Peter" (16:7).

**2. From the first plot to the passion — συμβούλιον, κατηγορέω, ἔνοχος; John's death as a rehearsal.** *Verified; design moderate–high.*

- **The plot's vocabulary.** συμβούλιον ("plot, council") occurs only at 3:6 and 15:1. κατηγορέω ("to accuse") occurs only at 3:2 and 15:3–4. ἔνοχος ("guilty") occurs only at 3:29 and 14:64.
- **John's death as rehearsal.** Five shared words link it to the passion:
  - ὀμνύω ("to swear"): 6:23 and 14:71
  - περίλυπος ("very sorrowful"): 6:26 and 14:34
  - εὔκαιρος ("opportune", 6:21) and εὐκαίρως ("opportunely", 14:11)
  - κοράσιον ("girl"): 5:41–42 and 6:22, 28
  - βασιλεύς ("king"): five verses of Herod in chapter 6, six of Jesus in chapter 15
- **What the sequence shows.** The first Galilean cycle ends with the plot (3:6) and the passion begins with its execution (15:1). The narrative of John's death, which 9:13 interprets, rehearses the vocabulary of Jesus' death in advance.

**3. Bread, blessing, shepherd — 6:34, 41; 8:6; 14:22–27.** *Verified.*

- **The meal verbs.** λαμβάνω, εὐλογέω / εὐχαριστέω, κλάω and δίδωμι ("take", "bless" / "give thanks", "break", "give") come at 6:41, 8:6 and 14:22–23. εὐχαριστέω occurs only at 8:6 and 14:23.
- **Bread.** ἄρτος ("bread") stands in 19 verses, 16 of them in 6:8–8:19.
- **The sheep and the shepherd.** ποιμήν ("shepherd") and πρόβατον ("sheep") occur only at 6:34 and 14:27. χορτάζω ("to satisfy") occurs only at 6:42; 7:27; 8:4, 8.
- **What the sequence shows.** The feedings are told with the Supper's verbs. The shepherd who feeds the shepherdless is the shepherd struck, and the disciples' hardness is a failure to understand "about the loaves" (6:52; 8:17–21).

**4. The sea, the voice, the passing by — 1:25; 4:39; 6:48–51; with Jonah 1; Job 9:8; Exod 33:19; 1 Kgs 19:11.** *Verified for the Greek wording; the theophany reading is moderate–high.*

- **In Mark.** φιμόω ("to muzzle") occurs only at 1:25 (a demon) and 4:39 (the sea). The clause ἐκόπασεν ὁ ἄνεμος ("the wind ceased") stands identically at 4:39 and 6:51. θαρσεῖτε, ἐγώ εἰμι ("take courage, I am") is at 6:50.
- **In the Old Testament.** The sea scene uses παρέρχομαι ("to pass by"), which is the verb of the LORD passing by Moses and Elijah. περιπατῶν ἐπὶ θαλάσσης ("walking on the sea") is said of God alone in Job 9:8. Jonah frames the storm (Jonah 1:10 at 4:41), and Jonah's "grieved to death" (Jonah 4:9) stands at 14:34.
- **What the sequence shows.** Mark answers his own question, "who then is this?" (4:41), with texts in which only God acts. The sweep adds a second Jonah contact at Gethsemane to the overview's one.

**5. Sins named at the start, and then only ransom and blood — ἁμαρτία at 1:4–2:10; ἄφεσις at 1:4 and 3:29; λύτρον at 10:45; διαθήκη at 14:24.** *Verified; design moderate.*

- **The nouns.** ἁμαρτία ("sin") occurs only at 1:4, 5; 2:5, 7, 9, 10. ἄφεσις ("forgiveness") occurs only at 1:4 and 3:29.
- **What comes after.** After chapter 3, the book speaks of how sins are dealt with only through the ransom "for many" (10:45) and the covenant blood "for many" (14:24). διαθήκη ("covenant") and ἐκχέω ("to pour out") occur only at 14:24.
- **What the sequence shows.** Forgiveness is announced as authority (2:10) and paid for as ransom. The book does not use the word "forgive" at the cross; it uses the Supper's words.

**6. Perceiving — νοέω at 7:18, 8:17, 13:14; παρὰ τὴν ὁδόν at 4:4, 15 and 10:46 → ἐν τῇ ὁδῷ at 10:52.** *Verified.*

- **The disciples and the reader.** The verb Jesus uses of the disciples' failure, οὔπω νοεῖτε; ("do you not yet perceive?", 8:17), is the verb the narrator addresses to the reader: ὁ ἀναγινώσκων νοείτω ("let the reader perceive", 13:14).
- **The road.** The seed "beside the road" (4:4, 15) is taken; the blind man "beside the road" (10:46) is healed and follows "on the road" (10:52).
- **What the sequence shows.** The book makes its reader the next person asked to see.

**7. Who says "you are" — Σὺ εἶ at 1:11, 3:11, 8:29, 14:61, 15:2; ἐγώ εἰμι at 6:50, 13:6, 14:62.** *Verified.*

- **The speakers.** God declares, the spirits cry out, and Peter confesses. The high priest asks, joining the Voice's title to Peter's, and Pilate asks.
- **"I am."** Jesus says ἐγώ εἰμι on the sea and before the court. False christs will say it (13:6).
- **What the sequence shows.** The one human confession of the Son in the book is the centurion's (15:39), and it comes without Σὺ εἶ ("you are"): he speaks about Jesus, not to him.

**8. Sinai in the middle of the book — 9:2–29.** *Verified in Swete; moderate–high.*

- **The mountain (9:2–7).** Six days (Exod 24:16); the overshadowing cloud (Exod 40:29 Swete, ἐπεσκίαζεν ("overshadowed"); Heb 40:35); σκηναί ("tents, tabernacles"); ἔκφοβοι ("terrified", Deut 9:19, Moses' word); ἀκούετε αὐτοῦ ("listen to him", Deut 18:15).
- **The descent (9:14–19).** A descent to a failing people (Exod 32) and "O faithless generation" (Deut 32:20).
- **The covenant blood (14:24).** The next Sinai text in Mark is Exod 24:8.
- **What the sequence shows.** The transfiguration and its sequel follow Moses' mountain and descent in order. This is a pattern the overview names only in part (Exod 24:16).

**9. The temple — Hos 9; Jer 7:11; Hag 2:15; καταλύω at 13:2, 14:58, 15:29; ναός at 14:58, 15:29, 15:38.** *Verified; Haggai moderate.*

- **The fig and the house.** One chapter of Hosea supplies the fig, "my house" and the dried roots (Hos 9:10, 15, 16).
- **Stone on stone.** Haggai's "stone upon stone" (Hag 2:15), spoken of the second temple's refounding, is reversed at 13:2.
- **The accusation.** καταλύω ("to destroy") carries the prediction into the false charge and the mockery. The veil of the ναός ("sanctuary") is torn at the death.
- **Where Jesus sits.** κατέναντι ("opposite") places Jesus opposite the treasury (12:41) and opposite the temple (13:3).
- **What the sequence shows.** Mark's temple judgement is told through the Prophets' words about the first and second temples. It is completed at the cross, not at AD 70.

**10. Glory, and who gets the right and the left — δόξα at 8:38, 10:37, 13:26; εὐώνυμος at 10:40 and 15:27; Dan 7:14 at 10:45; πάντα δυνατά at 9:23, 10:27, 14:36.** *Verified.*

- **The request.** James and John ask for glory at his right and left (10:37). They get two robbers (15:27).
- **The Son of Man.** In Dan 7:14 (Theodotion) the one like a son of man is served (δουλεύουσιν, "they serve"). Mark's Son of Man comes to serve (10:45).
- **"All things are possible."** The phrase is used of the father's faith (9:23) and of the rich man's salvation (10:27), and it is prayed back to the Father in Gethsemane (14:36), where the cup is not removed.
- **What the sequence shows.** In Mark, glory is reached by way of the cup.

**11. The women who frame the end — 12:41–44; 14:3–9; 15:40–41, 47; 16:1–8.** *Verified for the words; the frame is moderate.*

- **Around the discourse.** A widow gives ὅλον τὸν βίον αὐτῆς ("her whole living", 12:44). A woman anoints him for burial (14:3–9). Between them stands the discourse on the temple's end.
- **At the cross and the tomb.** The women who "followed and served" (15:41) are given the Twelve's two verbs. θεωρέω ("to watch") makes them the witnesses of the death, the burial and the empty tomb (15:40, 47; 16:4). Jesus himself θεωρεῖ ("watches") the widow at 12:41.
- **The leper.** λεπρός ("leper") occurs only at 1:40 and 14:3.
- **What the sequence shows.** The passion's faithful witnesses are the ones the book has least prepared the reader to expect.

**12. The King of the Jews — βασιλεύς in ch. 15; ἐπιγραφή at 12:16 and 15:26; προσκυνέω at 5:6 and 15:19; the anointing and the garments (1 Sam 10:1; 2 Kgs 9:6, 13; Zech 9:9).** *Verified; royal pattern moderate.*

- **The title.** Jesus is called βασιλεύς ("king") only in chapter 15: in Pilate's questions, the soldiers' mockery, the inscription and the priests' taunt.
- **The inscription and the homage.** The inscription (ἐπιγραφή) that answered "whose image?" (12:16) now bears his charge (15:26). The mock homage (προσκυνέω, "to bow down", 15:19) is the verb's only use besides Legion's (5:6).
- **The anointing and the garments.** A private anointing on the head (14:3) follows the pattern of Saul and Jehu. Garments are spread for the entry (11:8), as they were for Jehu.
- **What the sequence shows.** The kingship is enacted by those who reject it.

**13. The book fulfils its own words — καθὼς εἶπεν at 11:6, 14:16, 16:7; 14:30 → 14:72; ἀναμιμνῄσκω and ῥῆμα at 14:72.** *Verified.*

- **"As he said."** Twice the disciples find things "as he said" (11:6; 14:16). The young man invokes it a third time for the meeting in Galilee (16:7).
- **Peter.** Peter remembers τὸ ῥῆμα ("the saying", 14:72) at the moment it comes true — while the guards mock Jesus as a prophet (14:65).
- **What the sequence shows.** The ending's promise rests on a pattern the reader has watched hold. This is the strongest text-internal answer to the charge that 16:8 is a failure.

---

## Book-Overview Tensions

These are surfaced, not resolved. The overview was drafted in this session and is marked Draft v0.1.0. These are the points a Finalise pass should work through first.

**1. Hosea 9 should replace the uncertain Jeremiah row at 11:12–21.** The overview lists Jer 8:13 "with Hos 9:10; Mic 7:1" at *uncertain*. The sweep finds three verbal contacts in one chapter, each verified in Swete, Rahlfs and the WLC:

- **the fig:** συκῆ, Hos 9:10
- **the expulsion:** ἐκ τοῦ οἴκου μου ἐκβαλῶ ("I will drive them out of my house"), Hos 9:15; Hebrew מִבֵּיתִי אֲגָרְשֵׁם, the same words
- **the roots and the fruit:** roots dried up and no more fruit, Hos 9:16; the WLC ketiv is בלי

Together they span the intercalation. **Recommend** a new row for Hos 9:10–17 at *moderate–high*, with Jeremiah as a secondary witness. Hosea becomes live, since Hos 6:6 already stands at 12:33.

**2. The Isa 63:19 row should carry its context.** The overview traces 1:10 to Isa 63:19 through the Hebrew. Four verses earlier the same prayer has the one "brought up out of the sea" with "the shepherd of his flock", and "his Holy Spirit" (63:11). Then comes the Spirit "coming down" (63:14 Swete, κατέβη). Mark's "coming up out of the water … the Spirit … coming down" (1:10) matches the sequence. **Recommend** widening the row to Isa 63:11–64:1. The confidence stays *moderate*, because this is a synthetic claim resting on three verses.

**3. The overview's "nearer the Hebrew" list should gain a seventh item, and the 13:24 row a second source.**

- **Amos 2:16 at 14:52.** Mark has γυμνὸς ἔφυγεν ("naked, he fled"). The Hebrew is עָרוֹם יָנוּס ("naked he will flee"); נוּס is verified by lemma. Swete and Rahlfs both read ὁ γυμνὸς διώξεται ("the naked one will pursue") `[T]`. This is category 3, the NT's own text.
- **13:24.** Swete's Isa 13:10 reads φῶς ("light"), where Mark has φέγγος ("light, radiance"). Mark's word is Joel 2:10's. This is a conflation of two Greek texts, not a Hebrew-side contact; Joel 2:10 should be added to the overview's 13:24–25 row.

**4. The Sinai pattern at 9:2–29 is richer than the overview's single row (Exod 24:16).** **Add rows** for:

- Exod 40:29 Swete (Heb 40:35), ἐπεσκίαζεν ("overshadowed"), with σκηνή ("tent")
- Deut 9:19, ἔκφοβος ("terrified")
- Exod 32:15–24 at 9:14–19 (moderate)
- Deut 32:20 at 9:19 (moderate–high)

Exodus and Deuteronomy are already live; this strengthens both.

**5. Add-rows for the intertextual map, each verified in Swete or the WLC.**

- Lev 2:13 (ἁλισθήσεται, "will be salted") at 9:49
- Dan 7:14 Theodotion (δουλεύουσιν, "they serve") at 10:45
- Gen 18:14 at 10:27
- Hag 2:15 (λίθον ἐπὶ λίθον, "stone upon stone") at 13:2
- Joel 2:10 (φέγγος, "light") at 13:24
- Isa 40:8 at 13:31 (moderate; the wording differs)
- 1 Sam 10:1 and 2 Kgs 9:6 (oil poured on the head) at 14:3
- Exod 12:14 (μνημόσυνον, "memorial") at 14:9
- Isa 51:17, 22 (the cup of wrath) at 14:36
- Jonah 4:9 at 14:34, which makes Jonah live
- Amos 2:16 at 14:52
- Amos 8:10 (mourning for an only son, יָחִיד; ἀγαπητοῦ in Swete) at 15:33
- Ps 38:12 (Swete 37:12, μακρόθεν, "far off") at 15:40
- 2 Kgs 9:13 (garments spread for Jehu) at 11:8

**6. Daniel's order should be noted.** The overview lists Dan 9:27, 11:31 and 12:11 at 13:14, and Dan 12:1 at 13:19, as separate rows. The sweep notes that Mark keeps Daniel's sequence, the abomination and then the unparalleled tribulation. **Recommend** one note on the Daniel rows. The design is `[I]`.

**7. "Where the English Hides the Greek" should gain six rows.** The sweep compared the ESV (2025 US) and the NASB95 at each of these points:

- **13:14.** The masculine ἑστηκότα ("standing"). The ESV's "where *he* ought not to be" keeps it; the NASB95's "where *it* should not be" levels it.
- **13:33–37 / 14:34–38.** γρηγορέω ("to watch"). The ESV has "keep awake / stay awake" and then "watch"; the NASB95 has "on the alert" and then "keep watch". Neither translation lets the listener hear one word in both chapters.
- **14:68.** "And the rooster crowed" appears in the ESV and not in the NASB95. NA28 brackets it; א B L W Ψ* omit it.
- **15:2.** Σὺ λέγεις ("you say"). The ESV's "You have said so" keeps its ambiguity; the NASB95's "It is as you say" resolves it.
- **15:16.** πραιτώριον ("praetorium"). The NASB95 keeps "Praetorium"; the ESV has "governor's headquarters".
- **12:14.** κῆνσος ("poll-tax"). The NASB95 keeps "poll-tax"; the ESV has "taxes".

**Also add the text-critical points** where the ESV prints a reading the SBLGNT does not:

- 3:14 ("whom he also named apostles")
- 7:24 ("and Sidon")
- 7:28 ("Yes, Lord")

**8. The σινδών row needs one correction of emphasis.** The overview's English column is accurate. The sweep adds that *neither* translation keeps the link: the NASB95 moves from "sheet" to "cloth", and the ESV from "cloth" to "shroud". The overview's wording could be read as saying the NASB95 half-keeps it.

**9. The overview's live-source ranking should record two passion-night concentrations.**

- **Zechariah** — 9:9, 9:11, 13:7 and 14:4 — is concentrated in chs. 11–14.
- **Jonah** now has two contacts, 4:41 and 14:34.

Both are text-first sweep findings. **Recommend** Jonah as a live source at *moderate*.

**10. Additions to the echo table, each verified.**

- συμβούλιον ("plot, council"): 3:6 → 15:1
- κατηγορέω ("to accuse"): 3:2 → 15:3–4
- ἔνοχος ("guilty"): 3:29 → 14:64
- ἀφέντες ("leaving"): 1:18, 20 → 14:50
- ἄγωμεν ("let us go"): 1:38 → 14:42
- Σίμων ("Simon"): 3:16 → 14:37
- καθὼς εἶπεν ("as he said"): 11:6 → 14:16 → 16:7
- νοέω ("to perceive"): 8:17 → 13:14
- φιμόω ("to muzzle"): 1:25 → 4:39
- ἐκόπασεν ὁ ἄνεμος ("the wind ceased"): 4:39 → 6:51
- ποιμήν and πρόβατον ("shepherd", "sheep"): 6:34 → 14:27
- εὐχαριστέω ("to give thanks"): 8:6 → 14:23
- λεπρός ("leper"): 1:40 → 14:3
- ἐπιγραφή ("inscription"): 12:16 → 15:26
- καθαιρέω ("to take down"): 15:36 → 15:46
- περίλυπος ("very sorrowful"): 6:26 → 14:34
- ὀμνύω ("to swear"): 6:23 → 14:71

Several of these are stronger than rows the overview already carries.

**11. The overview's claims that the sweep tested and confirmed.** All of the following held:

- σχίζω ("to tear") at 1:10 and 15:38
- ἀγαπητός ("beloved") at three places
- the three πώρωσις/πωρόω ("hardness") verses
- γρηγορέω ("to watch") and ἀλεκτοροφωνία ("cockcrow")
- νεανίσκος ("young man"), περιβάλλω ("to wrap") and σινδών ("linen cloth")
- ναός ("sanctuary") at three places
- ἐκθαμβέομαι ("to be distressed") in Mark only
- the doubled "no one … nothing" (1:44; 16:8)
- δεῖ ("it is necessary") in six verses
- εὐθύς ("immediately"), 41 times as an adverb

The ESV's "torn open" at 1:10 and "on the way" at 10:52 were confirmed in the export. **No overview claim failed** in the sweep. The earlier restatements (the four named together at 1:29; ἐκβάλλω in 16 verses; ESV "body" at 6:29) were made before the overview was issued.

**12. The presenting situation holds.** Every pericope's Q2 answer is compatible with the overview's reconstruction: a Gentile audience under pressure, holding a crucified Messiah and failing disciples together. Several pericopes sharpen it:

- 13:9–13, where the disciples' future is told in the words of Jesus' trial
- 10:12, where a wife divorcing her husband fits Roman rather than Jewish law `[S]`
- 13:14 and 13:37, where the reader is addressed directly

It remains `[I]`.

---

## Preaching Pitfalls (book level)

Pitfalls for single passages are given at each pericope. These four run across the whole book.

### Pitfall: preaching Mark as a book of heroes and villains

- **What it looks like:** "Be like Bartimaeus; don't be like Peter; be like the widow; don't be like the rich man."
- **Why it is wrong:** Mark sets the disciples' call (1:16–20) and their flight (14:50) in the same words, and the book's grace falls on the one who failed worst: "and Peter" (16:7). The faithful figures are recipients before they are examples. The one human who confesses the Son is his executioner (15:39).
- **The corrective:** ask of every scene *what does this show about who Jesus is and what he must do?* before asking *who should I imitate?*

### Pitfall: preaching the miracles apart from the meals and the cross

- **What it looks like:** a series of healings and nature miracles preached as "Jesus can do it for you".
- **Why it is wrong:** the miracles are told in the vocabulary of the passion. The feedings use the Supper's verbs. The sea is "muzzled" like a demon. "He saved others" (15:31) gathers every σῴζω ("to save") of the healings into the one act he refuses for himself.
- **The corrective:** preach each miracle with its forward link, as a disclosure that points to the ransom.

### Pitfall: preaching chapter 13 without chapter 14, or chapter 14 without chapter 13

- **What it looks like:** Mark 13 as an end-times chart, and Gethsemane as a lesson in resignation.
- **Why it is wrong:** the discourse's watches are the passion night's, and its "stay awake" is first failed in Gethsemane. The disciples' future before councils and governors (13:9) is the trial Jesus undergoes days later.
- **The corrective:** preach them as a pair. The discourse tells the church how to wait. The passion shows the one who watched when they could not.

### Pitfall: supplying the ending the book withholds

- **What it looks like:** preaching 16:1–8 with the appearances from Matthew, Luke or John, or from 16:9–20, so that the silence is resolved at once.
- **Why it is wrong:** the book ends on a promise ("there you will see him, as he told you") and on fear. Its own pattern of kept words (11:6; 14:16; 14:72) is the ground it offers for trusting the promise. Its first word called all of it a "beginning".
- **The corrective:** let 16:7 carry the sermon. Ask the congregation where they stand: with the women's fear, or with the promise.

---

## Open Questions / Uncertainties

1. **1:41, ὀργισθείς ("angered") or σπλαγχνισθείς ("moved with compassion").** This is carried from the overview. No sweep finding depends on it. **Check the full NA28 evidence and the major commentaries** before 1:40–45 is preached.
2. **16:8 as an intended ending.** The sweep's findings on the ending (Convergent Finding 13; unit 36) show that 16:8 reads coherently as an ending. They cannot show intention. **Ask Logos** for the state of the question.
3. **Isa 6:9–10 at 4:12, "be forgiven".** Mark follows neither the Hebrew nor Swete. The Targum's reading is `[S]`. **Check the Targum** in Logos.
4. **Isa 63:11–14 behind 1:10.** It was found through the Hebrew and Swete. **Check whether commentators argue it**, and from which text.
5. **Hos 9 behind 11:12–21.** This is the sweep's most attractive untested claim. It rests on three contacts, and the Hebrew agrees with the Greek at 9:15. **A claim audit should test it** before it enters the overview as more than moderate–high.
6. **Amos 2:16 behind 14:52.** Mark agrees with the Hebrew verb against the Greek. Whether the young man is meant to evoke Amos's "day of the LORD" flight is `[I]`, uncertain. **Do not preach it as the point.**
7. **13:30, "this generation".** Named and not resolved (unit 29). **Check the major commentaries** before 13:24–37 is preached.
8. **14:72, ἐπιβαλών.** The meaning of the participle ("having thrown himself down", "having thought on it", "breaking down") is a crux. **Check the lexica.**
9. **15:39, the anarthrous υἱὸς θεοῦ ("God's Son").** This is carried from the overview. **Check Colwell's rule and the state of the question.**
10. **7:24 "and Sidon"; 7:28 ναί ("yes"); 3:14 "whom he also named apostles"; 14:68 "and the rooster crowed".** In each place the ESV prints a reading the SBLGNT does not. The NA28 apparatus was read. **Check Metzger** for the reasoning before a sermon point rests on any of them.
11. **Ps 22:7 at 9:12 (ἐξουδενηθῇ, "be treated with contempt").** Uncertain in the overview and in the sweep. If it holds, Ps 22 is planted in the Way section before the cross.
12. **Isa 22:16 and Isa 53:9 behind 15:46.** Both are uncertain. Mark gives no hint of either. **Do not enter either in the overview.**

---

## Text-First Declaration

**Mode:** Multi-Passage Sweep, 37 pericopes, following the overview's 37 preaching units exactly. Unit 37 ([16:9–20]) is treated as a text note, not as Mark.

**Primary texts actually opened:**

- **SBLGNT** `greek-nt-sblgnt/02-Mark.txt`: **all 661 verses of 1:1–16:8 were read in Greek before any English was consulted**, and the endings were read separately.
- **The MorphGNT lemma index** `_index/02-Mark.tsv`: used for every count and chain, with the shorter and longer endings trimmed.
- **The SBLGNT index files for the other NT books:** used for New Testament-wide uniqueness claims (ἐκθαμβέομαι, "to be distressed"; ἀλεκτοροφωνία, "cockcrow"; ἀδημονέω, "to be troubled"; εὐκαίρως, "opportunely") and for Synoptic comparisons.
- **NA28** `logos-exports/02-New-Testament/02-Mark-NA28.txt` and `02-Mark-NA28-apparatus.txt`: brackets and apparatus entries at 1:1, 1:41, 3:14, 6:14, 6:22, 7:24, 7:28, 14:24, 14:30, 14:68, 14:72, 15:34, 15:39, 16:8 and 16:9.
- **The NASB95 and ESV exports:** every English quotation of Mark was copied from them.

**Editions named:**

- Every Greek NT count is stated against the **SBLGNT**.
- Every Greek OT wording is stated against **Swete**. The **Rahlfs–Hanhart text exports** were opened at Hos 9:15–16, Amos 2:16 and Zech 13:7, together with the overview's list, and agree with Swete at each.
- Every Hebrew form is stated against the **WLC**.
- The **BHS apparatus** was read at Zech 13:7 (note b).
- **There is no LXX apparatus in the folder.** No finding rests on an LXX variant.

**Secondary sources present in context:** only the Draft overview, from this session and by the same model (see the independence caveat at the head of the report). No commentary or monograph was opened. Every `[S]` item is from general knowledge of the literature and none is load-bearing. The items are:

- the Targum at 4:12
- Roman divorce law at 10:12
- the legion's emblem
- Sir 48:10
- the 1 Kgs 19 / Exod 33 retelling
- the meaning of ἐπιβαλών
- the manuscript history of the endings
- the court of the nations
- the claim that 16:9–20 was compiled from the other Gospels

**Tools worked before secondary sources were consulted:** confirmed for every pericope. The overview's threads were held in peripheral vision (Phase 0.5). Its specific claims were checked only after each pericope's Greek work, and every claim tested appears in *Book-Overview Tensions*.

**Passage text:** verified. Every Greek quotation is copied from the corpus files, not reconstructed. SBLGNT sigla are removed from the quotations.

**Reference files viewed:**

- **Viewed:** core tool files 01–07; the extensions `preacher-extras`, `historical-background`, `original-audience`, `original-languages`, `textual-variants`, `biblical-theology`, `difficult-verses` and `christological-reading`; the worked example `romans-8-31to39-worked.md` from `_skill-examples/`, as the calibration anchor; `_texts/README.md`; and the Luke sweep, as the format model.
- **Not viewed:** `schnittjer-pass.md` (N/A, not Torah), `claim-audit-format.md` and `macro-synthesis-format.md` (N/A, neither mode is active).

**Depth floors:** this is Sweep mode, so the solo floors do not apply. Each pericope carries:

- the Positional Necessity Check
- a structure note
- text-first findings with warrants
- Tool 11, with the Citation Triad on every direct quotation and high-confidence allusion, and an explicit Move 4
- a pitfall
- Translations, with the NASB95 and ESV compared at every unit
- Difficulty notes where live

Totals: Headline Findings, 5; cross-passage findings, 13; book-level pitfalls, 4; open questions, 12.

**Chains verified:**

- **The sweep gate** (`gate2.py`) checked **74 chains exactly against the SBLGNT index**. It compared each claimed verse list with the index as a set, after trimming both endings, and all 74 passed. They include:
  - 57 "occurs only at" claims
  - δεῖ ("it is necessary") by parse code: the six verses, with Peter's δέῃ at 14:31 the last
  - εὐθύς ("immediately") as an adverb: 41
  - ἄρτος ("bread"): 16 of 19 verses in 6:8–8:19
  - ἀκούω ("to hear"): 13 times in 4:1–34
  - λόγος ("word"): 8 times in 4:14–20
  - twelve lemmas absent from 1:1–16:8 and present in 16:9–20
- **The overview's gate** (59 chains) was re-used for every chain the sweep inherited, not re-run.
- **Checked by listing, one at a time:** ἁμαρτία ("sin"; 1:4–2:10), Σίμων ("Simon"; Jesus uses it only at 14:37 after 3:16), ἄγω ("to go"; 1:38, 13:11, 14:42), Σὺ εἶ ("you are", five places), καθὼς εἶπεν ("as he said", three places), vocative Κύριε ("Lord", 7:28 only), ἀφέντες ("leaving", 1:18, 20; 14:50) and εἷς τῶν δώδεκα ("one of the twelve"; 14:10, 20, 43).
- **The Hebrew**, checked with `find.py verify`:
  - קָרַע ("to tear") and יָרַד ("to come down") at Isa 63:19
  - שָׁלַח ("to send"), מַלְאָךְ ("messenger"), פָּנָה ("to turn, clear") and דֶּרֶךְ ("way") at Exod 23:20, Mal 3:1 and Isa 40:3
  - Hos 9:10, 15, 16 (lemmas 3001, 1644, 6529 and 8384)
  - נוּס ("to flee") at Amos 2:16
  - יָחִיד ("only one") at Amos 8:10 and Gen 22:2
  - רַב ("many") and עָרָה ("to pour out") at Isa 53:12
  - בְּרִית ("covenant") at Exod 24:8 and Zech 9:11
  - דֶּרֶךְ ("way") at Isa 35:8

**Controls:**

- **Negative controls.** `find.py verify 3173 Isa:53:12` and `verify 7167 Isa:63:18` both failed with exit status 1, as they should. The sweep gate rejected a deliberately false claim (ἐκλεκτός, "elect", at 13:21).
- **Positive controls.** εὐαγγέλιον ("gospel") at 16:15 in the untrimmed index confirmed that the ending trim works, and a known verse was confirmed for every phrase search.
- **Controls that failed, and were caught:**
  - (a) An accent-sensitive phrase search missed 4:15 (see *What the corpus showed*).
  - (b) Final ς was not normalised in one early hand search.
  - (c) The first δεῖ gate used the wrong parse pattern and returned an empty list. It was flagged as a failure rather than reported as an absence, and was corrected to 3PA[IS].
  - (d) ἐκχύννω and ἐκθαμβέω returned silent zeros, because MorphGNT files them as ἐκχέω and ἐκθαμβέομαι.

**Three-way triage applied** at nine Hebrew–Greek divergences:

- Mal 3:1 / Isa 40:3 at 1:2 (category 3)
- Isa 63:19 at 1:10 (category 3)
- Isa 6:9–10 at 4:12 (category 3)
- Joel 4:13 at 4:29 (category 3)
- Isa 29:13 at 7:6–7 (category 3; Mark follows the Greek)
- Isa 5:7's wordplay at 12:1 (category 1)
- Zech 13:7 at 14:27 (category 3, with the BHS apparatus)
- Amos 2:16 at 14:52 (category 3)
- Ps 22:2 at 15:34 (category 3)

Ketiv forms are quoted unpointed (Jer 16:16; Hos 9:16). No divergence is reported as a split between translation traditions, and none is resolved by preferring one text by default.

**Tool 8 divergence check ran against the declared pulpit text (ESV 2025 US) at every unit.**

- **Where the ESV serves the findings better:** 1:2 ("before your face"), 1:10 ("torn open"), 10:52 ("on the way"), 13:14 ("he") and 15:2 ("You have said so").
- **Where the NASB95 serves them better:** 9:5 ("tabernacles"), 12:14 ("poll-tax") and 15:16 ("Praetorium").
- **Where neither version keeps a thread:** 1:12 (ἐκβάλλω, "to drive out"), 13:33–14:38 (γρηγορέω, "to watch"), 14:51–15:46 (σινδών, "linen cloth") and 16:6 (ἠγέρθη, "he has been raised", rendered as active).

**Synthetic-claim discipline:** all thirteen Cross-Passage Convergent Findings are marked synthetic. Every one is verified in its Greek parts. The design readings (5, 9, 11 and 12) are capped at moderate or moderate–high. **No cross-passage claim from this sweep should enter the book overview until it has been audited.**

**Warrant counts** (tag occurrences across the whole report, including the legend in *How to Read*): `[T]` 405 · `[I]` 105 · `[S]` 24 (none load-bearing; listed under *Secondary sources*).

*Health note:* this report could **not** have been written by someone who read the overview without opening the Greek.

- **Absent from the overview:** of the thirteen cross-passage findings, eight are not in it: 1 (the call undone), 2 (the plot to passion), 3 (the Supper-shaped feedings, beyond ἄρτος), 5, 6, 8, 12 and 13.
- **Corrections:** the Tensions section corrects or extends the overview at eleven points.
- **The weakness** is the one the independence caveat names. The overview and the sweep share an author, so a claim audit by a separate run is the proper next step. It should start with Hosea 9, Isaiah 63:11–14 and Amos 2:16.
