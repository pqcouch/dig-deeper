# Claim Audit: Mark

**Claims audited:** 21 Old Testament allusion claims that the Mark sweep proposed to add to, or upgrade in, the book overview. They fall at Mark 1:10; 9:5–7, 14–19, 49; 10:27, 45; 11:8, 12–21; 13:2, 14–19, 24, 31; 14:3, 9, 34, 36, 52; 15:33, 40.
**Date:** 29 September 2026
**Purpose:** To test these claims before any of them enters `Mark/book-overview-mark.md`. The sweep named them as synthetic and capped them at moderate confidence until audited. The three it flagged first were Hosea 9, Isaiah 63:11–14 and Amos 2:16.
**Texts:** Mark from the SBLGNT, with the MorphGNT index, counted in 1:1–16:8. Greek OT from Swete (observation) and the Rahlfs–Hanhart exports (citation). Hebrew from the WLC, checked with `find.py`. NA28 apparatus for Mark. There is no LXX apparatus in the folder.
**Consumes:** `Mark/book-overview-mark.md` Draft v0.1.0 and `Mark/dig-deeper-mark-sweep.md`, both from 29 September 2026.

---

## How This Audit Was Run

**Independence.** The overview and the sweep were written by the same model in one session, so an audit by that same author could only agree with itself. To avoid that, the 21 claims went to **three fresh auditors**, each a separate run with no access to the sweep or its reasoning. They were grouped as the Prophets (claims 1–7), Torah and Daniel (8–15), and the passion (16–21).

- Each auditor was given the bare claim and the overview's current rating. Nothing else was supplied.
- Each was told to try to *break* the claim.
- Each was to work only from the corpus on the device, and to report under the Hays criteria.

The auditors could grep the overview's Intertextual Map, and nothing else in the Mark folder. None opened a commentary.

**Baselines.** The main test was frequency, not fit. For each claim the auditors asked:

- How many verses and chapters in Swete, or in the WLC, contain the shared word?
- How many contain the same *combination* of words?
- Does Mark use the phrase anyway, in places where nobody proposes a source? This is the random-passage test.

A claim built on common words, or on a habit of Mark's own speech, was downgraded however well it fitted the theme.

**Checking the checkers.** The auditors' reports were then read here, and their decisive findings were re-run on the corpus. The following all reproduced exactly:

- Rahlfs Isa 63:11 reads ἐκ τῆς γῆς ("out of the land").
- Rahlfs Gen 39:12 reads καταλιπὼν … ἔφυγεν ("leaving … he fled").
- Hebrew Isa 63:14 has the cattle, not the Spirit, going down.
- Hebrew Jonah 4:9 has חָרָה ("to be angry", 2734).
- Isa 13:10 has נגה ("to shine", 5050).
- Sir 37:2 has λύπη … ἕως θανάτου ("grief … to the point of death").
- Swete Exod 10:22, Exod 11:6, Num 10:34 and Dan 12:11 (OG) read as the auditors reported.
- Theodotion Dan 7:14 has οὐ παρελεύσεται ("will not pass away").
- διακονέω ("to serve") does not occur as a verb anywhere in Swete. The only hit is the noun διάκονος ("servant") in the Prov 10:4 addition.
- The NA28 apparatus at Mark 9:49 cites Lev 2:13 for D and the Majority text.
- Heb 12:21 quotes ἔκφοβός εἰμι ("I am terrified").
- Mark's μακρόθεν ("from a distance") occurs in five verses, always as ἀπὸ μακρόθεν.

**Warrant tags** apply in the body: `[T]` for the text on the page, `[I]` for inference, and `[S]` for secondary knowledge, which here was never opened, only recalled.

---

## Summary

| Verdict | Count | Claims |
|---|---|---|
| Confirmed | 1 | 12 (Lev 2:13 at 9:49) |
| Confirmed with nuance | 4 | 8 (Exod 40 / Num 10 cloud), 9 (Deut 9:19 ἔκφοβος, "terrified"), 11 (Deut 32:20 and the wilderness generation), 15 (Gen 18:14 cluster) |
| Needs reframing | 8 | 1 (Hos 9 → Jer 7–8 lead), 2 (Isa 63:11–14), 5 (Joel 2:10), 13 (Dan 7:14 at 10:45), 14 (Daniel's "order"), 16 (Isa 40:8), 17 (royal anointing), 20 (Isa 51 cup) |
| Uncertain — flag for research | 4 | 3 (Amos 2:16), 6 (Hag 2:15), 7 (Jonah 4:9), 18 (2 Kgs 9:13) |
| Discard | 4 | 4 (Amos 8:10), 10 (Exod 32), 19 (Exod 12:14), 21 (Ps 38:12) |

**Headline.** The sweep's allusion claims fared much worse than its lexical chains did. All 74 chains within Mark had passed their gate. Of the 21 allusions, only five survive as proposed or with nuance. The three the sweep ranked highest, Hosea 9, Isaiah 63:11–14 and Amos 2:16, all fall.

- **Hosea 9** is displaced by the Jeremiah chapter that Mark actually quotes.
- **Isaiah 63:11–14** cannot deliver its match in any single text: the Hebrew lacks the Spirit coming down, and the Rahlfs Greek lacks the sea.
- **Amos 2:16** has a better-matching rival in Gen 39:12, so it cannot be counted as a case of Mark standing nearer the Hebrew.

This fits the project's finding across three earlier books: synthetic claims made at speed fail far more often than passage-level ones.

The audit also turned up **seven rival or new sources** that the sweep missed:

- Jer 7:15 and 8:13 at 11:12–21
- Gen 39:12 at 14:52
- Sir 37:2 at 14:34
- Num 10:34 at 9:7
- Exod 11:6 at 13:19
- Isa 51:6 and Theodotion Dan 7:14 at 13:31
- Exod 10:22 at 15:33

Some of these are stronger than what they replace. None has been audited in its own right.

---

## Claims Audited

### Claim 1: Hos 9:10–17 behind Mark 11:12–21

**Source:** sweep unit 25 and Tensions 1. Proposed at moderate–high, to replace the overview's row "Jer 8:13 (with Hos 9:10; Mic 7:1)", currently rated uncertain.

**Claim:** One chapter of Hosea supplies the whole sequence: the fig (9:10); "I will drive them out of my house" (9:15), behind the expulsion and "my house" at 11:15–17; and "their root is dried up, they shall bear no fruit" (9:16), behind 11:14 and 11:20.

**Evidence.**

*Mark 11:*
- 11:13: ἰδὼν συκῆν … οὐδὲν εὗρεν εἰ μὴ φύλλα ("seeing a fig tree … he found nothing but leaves")
- 11:14: μηδεὶς καρπὸν φάγοι ("may no one eat fruit")
- 11:15: ἤρξατο ἐκβάλλειν ("he began to drive out")
- 11:17: Ὁ οἶκός μου … σπήλαιον λῃστῶν ("my house … a den of robbers")
- 11:20: ἐξηραμμένην ἐκ ῥιζῶν ("withered from the roots")

*Hosea 9:*
- **9:10.** WLC כְּבִכּוּרָה בִתְאֵנָה ("like first fruit on the fig tree"). This is a simile of God's *delight* in Israel's fathers, not a picture of a barren tree.
- **9:15.** WLC מִבֵּיתִי אֲגָרְשֵׁם ("from my house I will drive them out"). Swete and Rahlfs both read ἐκ τοῦ οἴκου μου ἐκβαλῶ αὐτούς ("I will drive them out of my house").
- **9:16.** WLC שָׁרְשָׁם יָבֵשׁ פְּרִי בלי־יַעֲשׂוּן ("their root is dried up, they will bear no fruit"). The ketiv בלי stands unpointed. Swete has καρπὸν οὐκέτι μὴ ἐνέγκῃ ("it will bear fruit no more"). Mark's verb is φάγοι ("eat"), not ἐνέγκῃ ("bear").

*The competitor.* Mark 11:17 quotes Jer 7:11, μὴ σπήλαιον λῃστῶν ὁ οἶκός μου ("is my house a den of robbers?"). That makes Jeremiah's temple sermon the passage in hand, and it already supplies "my house".

- **Jer 7:15** is an expulsion: καὶ ἀπορρίψω ὑμᾶς ἀπὸ προσώπου μου ("I will cast you from my presence").
- **Jer 8:13** (Swete) reads οὐκ ἔστιν σῦκα ἐν ταῖς συκαῖς, καὶ τὰ φύλλα κατερρύηκεν ("there are no figs on the fig trees, and the leaves have fallen"). That gives three words shared with Mark 11:13: συκῆ ("fig tree"), σῦκον ("fig") and φύλλον ("leaf"). Hosea shares only συκῆ.

**Baseline.**

- **Swete, fig words:** 35 verses in 29 chapters.
- **Fig + ἐκβαλ- ("drive out"):** 5 chapters.
- **Fig + root, and all five elements together:** Hos 9 only.
- **Fig + leaf:** 3 chapters (Gen 3, Isa 34, Jer 8).
- **WLC:** תְּאֵנָה ("fig", 8384) + גרשׁ ("drive out", 1644) occur together in 3 chapters. Fig + שֹׁרֶשׁ ("root", 8328), and all five lemmas together, occur in Hos 9 only.
- **Random-passage test:** Mark 4:6–7 already has ῥίζα ("root") + ἐξηράνθη ("withered") + καρπός ("fruit"). So the triad of root, withering and fruit is Mark's own vocabulary.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | Hosea is canonical and widely read |
| Volume | Possible | Hos 9 is the only chapter with the full cluster, but each word is common, and "my house" is already accounted for by the quoted text |
| Recurrence | Weak | Hosea elsewhere in Mark only through Hos 6:6 at 12:33 |
| Thematic Coherence | Possible | Expulsion from God's house and barrenness fit, but Hosea's fig is an image of delight |
| Historical Plausibility | Strong | A judgement reading of Hosea is plausible |
| History of Interpretation | Not checked | No secondary sources were opened. Hos 9:10 is often listed beside Jer 8:13 `[S]` |
| Satisfaction | Possible | Hosea adds the root and the drying; Jeremiah supplies the leaves and "my house" |

**Verdict:** Needs reframing. Moderate confidence for Jeremiah 7–8 as the lead source, with Hosea 9 as a secondary resonance at uncertain to moderate.

**Reasoning:** Hosea 9's cluster really is unique in both Swete and the WLC. But Mark quotes Jeremiah 7, and Jer 7:15 and 8:13 match the fig and the leaves more closely than Hosea does. Hosea cannot displace the text Mark actually cites. The sweep's case rested on "one chapter supplies everything". Against the Jeremiah context, that is no longer the whole picture.

**Book-overview action:** Do not replace the row. Revise it to "Jer 7:11 (quoted), with 7:15 and 8:13 (no figs, leaves); cf. Hos 9:10–16 (fig; 'out of my house I will drive them'; root dried, no fruit)". Raise the Jeremiah context from uncertain to **moderate**, and tag Hosea at **uncertain–moderate**.

---

### Claim 2: Isa 63:11–14 (with 63:19) behind Mark 1:10

**Source:** sweep unit 1 and Tensions 2. Proposed at moderate, to widen the overview's Isa 63:19 row, which is currently moderate.

**Claim:** The prayer that asks God to "tear the heavens and come down" (63:19, Hebrew) also speaks of one brought "up out of the sea" and of the Holy Spirit (63:11), and of the Spirit "coming down" (63:14). Together these match Mark's "coming up out of the water … the Spirit … coming down".

**Evidence.**

*Mark 1:10:* ἀναβαίνων ἐκ τοῦ ὕδατος ("coming up out of the water") … τὸ πνεῦμα … καταβαῖνον ("the Spirit … coming down").

*Isa 63:11:*
- WLC: הַמַּעֲלֵם מִיָּם אֵת רֹעֵי צֹאנוֹ ("who brought them up out of the sea with the shepherds of his flock") … אֶת־רוּחַ קָדְשׁוֹ ("his Holy Spirit").
- Swete: ἐκ τῆς θαλάσσης ("out of the sea").
- **Rahlfs: ἐκ τῆς γῆς ("out of the land")** `[T]`, re-verified. So the Greek text of record has no sea.

*Isa 63:14:*
- WLC: כַּבְּהֵמָה בַּבִּקְעָה תֵרֵד רוּחַ יְהוָה תְּנִיחֶנּוּ ("as cattle go down into the valley, the Spirit of the LORD gave them rest"). In the Hebrew it is the cattle that go down.
- Only the Greek has κατέβη πνεῦμα ("the Spirit came down").

*The verbs:* Isaiah has the causative ἀναβιβάζω ("to bring up"); Mark has ἀναβαίνω ("to go up").

*What survives:* the phrase "Holy Spirit" is rare. In canonical Swete it occurs only at Ps 50:13 and Isa 63:10, 11, and Mark 1:8 has ἐν πνεύματι ἁγίῳ ("with the Holy Spirit") two verses earlier.

**Baseline.**

- **Swete:** πνεῦμα ("spirit, wind") + a καταβ- form ("to go down") + an ἀναβ- form ("to go up") occur together in 43 chapters.
- **WLC:** עלה ("to go up", 5927), יָם ("sea", 3220), רוּחַ ("spirit, wind", 7307) and ירד ("to go down", 3381) occur together in 17 chapters.
- **Random-passage test:** Mark 5:13 has spirits and the sea, and 6:51 has ἀναβαίνω ("to go up") and the sea.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | The prayer is already in play through 63:19 |
| Volume | Weak | The cluster occurs in 17–49 chapters. The sea is in Swete only, and the Spirit's descent is in the Greek only |
| Recurrence | Possible | 63:19 is already linked to 1:10 |
| Thematic Coherence | Possible | A new-exodus shepherd given the Spirit suits a baptism |
| Historical Plausibility | Possible | Depends on which text is imagined |
| History of Interpretation | Not checked | — |
| Satisfaction | Possible | Only "Holy Spirit" is distinctive |

**Verdict:** Needs reframing. Uncertain.

**Reasoning:** No single text supplies all three elements. The Hebrew has the sea and the Holy Spirit but no descending Spirit. The Greek has the descending Spirit, but its text of record reads "land", not "sea". The sweep's triple match was assembled from different witnesses. The 63:19 link itself, קָרַע ("to tear"), is untouched by this audit.

**Book-overview action:** Do not widen the row. At most, add a clause to the 63:19 row: "the same prayer recalls the one who brought the shepherd up from the sea and put his Holy Spirit among them (63:11, Hebrew)". Mark it as context, and drop the κατέβη ("came down") argument.

---

### Claim 3: Amos 2:16 behind Mark 14:52

**Source:** sweep unit 32, Headline Finding 4 and Tensions 3. Proposed at moderate, and as a seventh case of Mark standing nearer the Hebrew than the Greek.

**Claim:** Mark's γυμνὸς ἔφυγεν ("naked, he fled") follows the Hebrew עָרוֹם יָנוּס ("naked he will flee"), against Swete and Rahlfs, which both read ὁ γυμνὸς διώξεται ("the naked one will pursue").

**Evidence.**

*Mark 14:51–52:* περιβεβλημένος σινδόνα ἐπὶ γυμνοῦ ("wearing a linen cloth over his naked body"), κρατοῦσιν αὐτόν ("they seize him"), ὁ δὲ καταλιπὼν τὴν σινδόνα γυμνὸς ἔφυγεν ("but he, leaving the linen cloth, fled naked").

*Amos 2:16:* the Hebrew and the Greek are as the claim states `[T]`.

*The competitor, Gen 39:12:*
- Rahlfs: καταλιπὼν τὰ ἱμάτια αὐτοῦ ἐν ταῖς χερσὶν αὐτῆς ἔφυγεν ("leaving his garments in her hands, he fled") `[T]`, re-verified. This is Mark's participle in Mark's order.
- WLC: וַתִּתְפְּשֵׂהוּ בְּבִגְדוֹ … וַיַּעֲזֹב בִּגְדוֹ … וַיָּנָס ("she seized him by his garment … he left his garment … and fled").
- Genesis 39 matches the seizing, the garment left behind and the flight, in both languages.

*The word "naked":* γυμνός ("naked") is already present at 14:51, so its use at 14:52 is required by the story itself.

**Baseline.**

- **WLC:** עָרוֹם ("naked", 6174) + נוס ("to flee", 5127) occur in the same verse only at Amos 2:16. עזב ("to leave", 5800) + נוס occur together in 8 verses, 4 of them in Gen 39.
- **Swete:** καταλ(ε)ιπ- ("to leave") + ἔφυγ- ("fled") occur together in 8 verses, 4 of them in Gen 39.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Weak | Two words, one of them required by the narrative |
| Recurrence | Possible | Amos 8:9 at 15:33 |
| Thematic Coherence | Possible | The collapse of the brave "in that day" fits 14:50 |
| Historical Plausibility | Possible | Needs a reader of the Hebrew |
| History of Interpretation | Not checked | Often mentioned `[S]` |
| Satisfaction | Weak | Gen 39 accounts for more of the wording |

**Verdict:** Uncertain — flag for research. Uncertain. **Discard it as a "Mark nearer the Hebrew" case.**

**Reasoning:** The Hebrew pairing is unique, but "fled naked" is what any narrator would write of a man who slips out of his only garment. Genesis 39 shares the participle, the seizing and the abandoned garment. The argument for Hebrew priority depends on Amos being the source, and that has not been shown.

**Book-overview action:** Do not add Amos 2:16 to the "nearer the Hebrew" list. If a row is wanted, make it one row at uncertain: "Gen 39:12 (seized, garment left, fled); cf. Amos 2:16 Heb".

---

### Claim 4: Amos 8:10 with 8:9 behind Mark 15:33

**Source:** sweep unit 35. Proposed as an extension of the overview's Amos 8:9 row, currently moderate.

**Claim:** Amos 8:10, "like mourning for an only son" (WLC יָחִיד, "only one"; Swete ἀγαπητοῦ, "beloved"), ties the darkness at 15:33 to the Voice's ἀγαπητός ("beloved") at 1:11, 9:7 and 12:6.

**Evidence.**

- **Mark 15 has neither ἀγαπητός ("beloved") nor any mourning word.** πενθέω ("to mourn") occurs only at 16:10, in the longer ending `[T]`.
- **The same pairing is not unique to Amos.** Jer 6:26 has it too: WLC אֵבֶל יָחִיד ("mourning for an only son"), Swete πένθος ἀγαπητοῦ ("mourning for a beloved one"). Zech 12:10 has ὡς ἐπ' ἀγαπητῷ ("as for a beloved one").
- **The overview's 8:9 row has a rival.** Swete Exod 10:22, ἐγένετο σκότος … ἐπὶ πᾶσαν γῆν Αἰγύπτου ("there came darkness … over all the land of Egypt"), is the only Swete verse pairing darkness with "the whole land". It is verbally closer to Mark's σκότος ἐγένετο ἐφ' ὅλην τὴν γῆν ("darkness came over the whole land") than Amos 8:9 is `[T]`, re-verified.

**Baseline.** יָחִיד ("only one") occurs in 12 WLC verses. It is paired with אֵבֶל ("mourning") in 2: Amos 8:10 and Jer 6:26.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Weak | The linking word is absent from Mark 15 |
| Recurrence | Possible | 8:9 is already in the overview |
| Thematic Coherence | Possible | Only through a theological reading |
| Historical Plausibility | Weak | Needs a reader to join 1:11 and Amos across the whole book |
| History of Interpretation | Not checked | — |
| Satisfaction | Weak | Explains nothing in Mark's wording |

**Verdict:** Discard as a Markan allusion. Uncertain. It may stay as a biblical-theology note, outside the map.

**Reasoning:** The link runs through a word Mark does not use, and the pairing it depends on is shared with Jer 6:26.

**Book-overview action:** Keep Amos 8:9 at moderate and do not extend it to 8:10. Add Exod 10:22 as a rival for the darkness at 15:33, at moderate, for its own audit.

---

### Claim 5: Joel 2:10 conflated with Isa 13:10 at Mark 13:24

**Source:** sweep unit 29 and Tensions 3.

**Claim:** Mark's φέγγος ("light, radiance"), where Swete's Isa 13:10 has φῶς ("light"), comes from Joel 2:10.

**Evidence.**

- **Mark 13:24 is Isa 13:10 LXX word for word except for this one noun** `[T]`.
- **In Joel the φέγγος belongs to the stars, not the moon.** Joel 2:10 and 4:15 read τὰ ἄστρα δύσουσιν τὸ φέγγος αὐτῶν ("the stars will withdraw their light"), and the verb differs as well.
- **Isaiah's own Hebrew offers another explanation.** Isa 13:10 reads וְיָרֵחַ לֹא־יַגִּיהַ אוֹרוֹ ("the moon will not *cause to shine* its light"). The verb is נגה ("to shine", 5050), verified. Its noun נֹגַהּ ("brightness") is what φέγγος renders elsewhere in the LXX. So φέγγος may come from Isaiah's own Hebrew.

**Baseline.** φέγγος occurs in about 22 canonical Swete verses. It never stands as *the moon's* light.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Weak | One noun, attached to a different subject |
| Recurrence | Possible | Joel 4:13 at 4:29 |
| Thematic Coherence | Strong | Day-of-the-LORD darkening |
| Historical Plausibility | Possible | — |
| History of Interpretation | Not checked | — |
| Satisfaction | Weak | Isaiah's Hebrew explains the noun equally well |

**Verdict:** Needs reframing. Uncertain.

**Reasoning:** The wording is Isaiah's throughout. The single divergent word has two possible explanations, and neither requires Joel.

**Book-overview action:** Keep the "Isa 13:10; 34:4" row at high. Add a note: "φέγγος against LXX φῶς: either Joel 2:10 / 4:15 or the Hebrew verb נגה of Isa 13:10 — unresolved." Do not assert a conflation.

---

### Claim 6: Hag 2:15 behind Mark 13:2

**Source:** sweep unit 28. Proposed at moderate.

**Claim:** Mark's λίθος ἐπὶ λίθον ("stone upon stone") answers Haggai's description of the second temple's founding.

**Evidence.** Hag 2:15 in Swete and Rahlfs reads πρὸ τοῦ θεῖναι λίθον ἐπὶ λίθον ἐν τῷ ναῷ Κυρίου ("before stone was laid upon stone in the temple of the Lord"). The WLC reads אֶבֶן אֶל־אֶבֶן ("stone upon stone"). Both refer to the same building as Mark, but Haggai describes construction and Mark demolition `[T]`.

**Baseline.** The phrase is **unique in the Old Testament**: one verse in Swete and one in the WLC. But it is made of the commonest words, and it is the natural idiom for razing a building.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Possible | Unique in the OT, but idiomatic |
| Recurrence | Weak | No other use of Haggai in Mark |
| Thematic Coherence | Strong | The same temple, with the action reversed |
| Historical Plausibility | Possible | — |
| History of Interpretation | Not checked | — |
| Satisfaction | Possible | Adds irony, but explains no detail |

**Verdict:** Uncertain — flag for research. Uncertain.

**Reasoning:** The rarity and the shared building make it attractive. The idiom makes it unnecessary.

**Book-overview action:** Add at most one row at uncertain, noting that the phrase is unique to Hag 2:15 in both languages but idiomatic.

---

### Claim 7: Jonah 4:9 behind Mark 14:34 (Jonah as a "live" source)

**Source:** sweep unit 32 and Tensions 5 and 9.

**Claim:** Jonah 4:9 lies behind Mark's ἕως θανάτου ("to the point of death"), and so gives Jonah a second contact in Mark.

**Evidence.**

- **Jonah 4:9 in the Greek.** Swete and Rahlfs read Σφόδρα λελύπημαι ἐγὼ ἕως θανάτου ("I am greatly grieved, to the point of death").
- **Jonah 4:9 in the Hebrew.** The WLC reads חָרָה־לִי עַד־מָוֶת ("I am *angry*, to the point of death"). Jonah is angry in the Hebrew, not grieving (חָרָה, "to be angry", 2734, verified). So the link of grief exists only in the Greek.
- **The first half of Mark's saying is already explained** by the psalm refrain ἵνα τί περίλυπος εἶ, ἡ ψυχή ("why are you very sorrowful, O soul?", Swete Ps 41:6, 12; 42:5).
- **A rival for the second half.** Sir 37:2 reads οὐχὶ λύπη ἔνι ἕως θανάτου ἑταῖρος καὶ φίλος τρεπόμενος εἰς ἔχθραν; ("is it not a grief to the point of death when a companion and friend turns to enmity?"). This is re-verified, and it fits a betrayal setting.

**Baseline.** A λυπ- word ("grief") with ἕως θανάτου ("to the point of death") in one verse: in Swete, only Jonah 4:9 and Sir 37:2.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Possible | A rare pairing, but shared with Sirach |
| Recurrence | Possible | Jonah 1:10 at 4:41 (high) |
| Thematic Coherence | Weak | Jonah's sulk over the plant sits oddly beside Gethsemane |
| Historical Plausibility | Possible | Through the Greek only |
| History of Interpretation | Not checked | — |
| Satisfaction | Weak | Two idiomatic words |

**Verdict:** Uncertain — flag for research. Uncertain.

**Reasoning:** The psalm carries this verse. Jonah contributes two words, which are shared with Sirach, and in the Hebrew Jonah is angry, not grieving.

**Book-overview action:** Keep Ps 42–43 at high. At most, add a note: "(ἕως θανάτου: cf. Jonah 4:9 Greek; Sir 37:2)" at uncertain. **Do not mark Jonah as live** on this evidence.

---

### Claim 8: Exod 40:34–35 (Swete 40:29) behind Mark 9:5–7

**Source:** sweep unit 18 and Tensions 4. Proposed as a row beside Exod 24:16.

**Claim:** Mark's νεφέλη ἐπισκιάζουσα αὐτοῖς ("a cloud overshadowing them", 9:7), together with Peter's σκηναί ("tents", 9:5), recalls the cloud over the tabernacle.

**Evidence.**

- **Exod 40.** Swete Exod 40:29 reads ἐπεσκίαζεν ἐπ' αὐτὴν ἡ νεφέλη ("the cloud overshadowed it"), with σκηνή ("tent, tabernacle") on either side. Rahlfs 40:35 is the same. The WLC has שָׁכַן ("to dwell"), so "overshadow" is the Greek translator's choice `[T]`.
- **The rival, Num 10:34.** Swete Num 10:34 reads καὶ ἡ νεφέλη ἐγένετο σκιάζουσα ἐπ' αὐτοῖς ("and the cloud came, shading them") `[T]`, re-verified. This matches Mark's syntax: ἐγένετο ("came") + participle + αὐτοῖς ("them"), and the cloud covers people. (Rahlfs numbers the verse 10:36.)

**Baseline.**

- ἐπισκιάζω ("to overshadow") occurs in 4 verses of Swete. Only one of them, Exod 40:29, pairs it with νεφέλη ("cloud").
- The combination νεφελ- + σκην- + σκια- ("cloud", "tent", "shade") occurs in 4 chapters: Exod 40, Num 9, Num 10 and Job 36.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Possible | A rare compound verb with "cloud" and "tent" |
| Recurrence | Possible | The Exod 24 row applies to the same pericope |
| Thematic Coherence | Strong | The divine presence, and Peter's wish to build dwellings |
| Historical Plausibility | Strong | — |
| History of Interpretation | Possible `[S]` | The tabernacle reading is widely discussed |
| Satisfaction | Possible | Explains why the tents and the cloud stand together |

**Verdict:** Confirmed with nuance. Moderate.

**Reasoning:** This is a real and rare lexical anchor. But it belongs to the wilderness-cloud texts (Exod 40:34–38; Num 9:15–22; 10:34), not to a single verse.

**Book-overview action:** Add a row "Exod 40:34–35 (Swete 40:29); cf. Num 10:34 | 9:5, 7 | moderate", labelled as the tabernacle-cloud complex.

---

### Claim 9: Deut 9:19 behind Mark 9:6

**Claim:** ἔκφοβοι ("terrified", 9:6) is Moses' word at Sinai: ἔκφοβός εἰμι ("I am terrified"), Deut 9:19 Swete.

**Evidence.**

- **The adjective is rare.** ἔκφοβος ("terrified") occurs in 2 Swete verses, Deut 9:19 and 1 Macc 13:2. In the New Testament it occurs at Mark 9:6 and Heb 12:21.
- **Hebrews applies the word to Sinai.** Heb 12:21 quotes Deut 9:19 and applies it to Sinai itself: Ἔκφοβός εἰμι καὶ ἔντρομος ("I am terrified and trembling") `[T]`, re-verified.
- **The Hebrew is a different word.** Deut 9:19 has יגר ("to dread", 3025), not the usual ירא ("to fear"). A negative control confirmed that ירא is absent from the verse.
- **The cause differs.** Moses fears God's wrath over the golden calf; the disciples fear a theophany of glory.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Possible | One word, but a very rare one |
| Recurrence | Possible | The pericope has a Sinai frame |
| Thematic Coherence | Possible | The theophany fits; the cause of the fear does not |
| Historical Plausibility | Strong | Hebrews shows that early readers heard the word as Moses' Sinai fear |
| History of Interpretation | Possible | Heb 12:21 |
| Satisfaction | Weak | Adds colour only |

**Verdict:** Confirmed with nuance. Uncertain to moderate.

**Reasoning:** The rarity is real, and Hebrews offers early reception of the word as Sinai language. But this is still a single adjective used of a different fear.

**Book-overview action:** Add a brief note on 9:6: "ἔκφοβοι; cf. Deut 9:19 (Swete), Heb 12:21 — lexical only". **Do not build a sermon point on it.**

---

### Claim 10: Exod 32:15–24 behind Mark 9:14–19

**Claim:** Jesus' descent to a failing crowd re-enacts Moses' descent to the golden calf.

**Evidence.**

- **No content word is shared** between Mark 9:14–19 and Exod 32:15–24 in Swete `[T]`.
- **The descent formula points elsewhere.** Mark 9:9 has καταβαινόντων αὐτῶν ἐκ τοῦ ὄρους ("as they were coming down from the mountain"). The closest form is Exod 34:29, καταβαίνοντος δὲ αὐτοῦ ἐκ τοῦ ὄρους ("as he was coming down from the mountain"), not Exod 32:15. NA28 shows ἀπό ("from") for ἐκ in several witnesses at Mark 9:9, so the preposition cannot bear weight.
- **Deut 9:15–24 fits better.** It gathers the descent, the fear (9:19) and the people's unbelief, οὐκ ἐπιστεύσατε ("you did not believe", 9:23).

**Baseline.** The descent formula κατ[ε/α]β- + ἐκ τοῦ ὄρους ("to come down from the mountain") occurs in 8 Swete verses across 7 chapters.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Weak | No shared content word |
| Recurrence | Possible | The Sinai frame |
| Thematic Coherence | Possible | There is no idol in Mark |
| Historical Plausibility | Possible | — |
| History of Interpretation | Not checked | — |
| Satisfaction | Weak | The shape fits a dozen texts |

**Verdict:** Discard as proposed.

**Reasoning:** A narrative shape with three candidate sources and no lexical anchor is not an allusion.

**Book-overview action:** Add no row for Exod 32. If a pattern note is wanted: "Sinai-descent pattern (Exod 34:29–30; Deut 9:15–24) around 9:9–19 `[I]`, uncertain".

---

### Claim 11: Deut 32:20 behind Mark 9:19

**Claim:** Ὦ γενεὰ ἄπιστος ("O faithless generation") recalls Swete Deut 32:20, γενεὰ ἐξεστραμμένη … υἱοὶ οἷς οὐκ ἔστιν πίστις ἐν αὐτοῖς ("a perverse generation … sons in whom is no faith").

**Evidence.**

- **The source text.** Deut 32:20 in the WLC reads דּוֹר תַּהְפֻּכֹת … בָּנִים לֹא־אֵמֻן בָּם ("a generation of perversities … sons with no faithfulness in them"). Rahlfs agrees with Swete.
- **Rivals:**
  - Deut 32:5, γενεὰ σκολιὰ καὶ διεστραμμένη ("a crooked and perverse generation").
  - Ps 78:8 (Swete 77:8), where the Hebrew has the same root אמן ("to be faithful").
  - Num 14:11, a doubled "how long …?" with unbelief. This matches the *shape* of Mark's doubled ἕως πότε ("how long").
- **Early reception.** Matt 17:17 and Luke 9:41 add διεστραμμένη ("perverse"), from Deut 32:5, and 𝔓⁴⁵vid, W and ƒ¹³ add it to Mark too. That is early evidence that the saying was heard against Deut 32 `[T]`.

**Baseline.**

- The vocative ὦ γενεά ("O generation") occurs nowhere in Swete.
- The only canonical Swete verses in which a generation is said to lack faith are Deut 32:20 and Ps 77:8.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Possible | γενεά ("generation") with faith negated |
| Recurrence | Strong | Mark's "this generation" motif (8:12, 38; 13:30) |
| Thematic Coherence | Strong | The Sinai frame |
| Historical Plausibility | Strong | — |
| History of Interpretation | Strong | Matthew, Luke and the scribes |
| Satisfaction | Strong | Explains the lament form |

**Verdict:** Confirmed with nuance. Moderate–high for the wilderness-generation complex; moderate for Deut 32:20 alone.

**Book-overview action:** Add a row "Deut 32:20 (with 32:5); cf. Num 14:11, 27; Ps 78:8 | 9:19 | moderate–high". Note that Matthew and Luke make the Deut 32:5 link explicit.

---

### Claim 12: Lev 2:13 behind Mark 9:49

**Claim:** Πᾶς γὰρ πυρὶ ἁλισθήσεται ("for everyone will be salted with fire") takes its verb and its sacrificial logic from Lev 2:13.

**Evidence.**

- **The source text.** Swete and Rahlfs Lev 2:13 read πᾶν δῶρον θυσίας ὑμῶν ἁλὶ ἁλισθήσεται … ἅλα διαθήκης ("every gift of your sacrifice shall be salted with salt … the salt of the covenant"). The WLC has בַּמֶּלַח תִּמְלָח … מֶלַח בְּרִית ("with salt you shall salt … salt of the covenant").
- **The form is rare.** ἁλισθήσεται ("will be salted") occurs in **one Swete verse**, and ἁλίζω ("to salt") in two canonical verses.
- **The NA28 apparatus.** At Mark 9:49 it marks "(Lv 2,13)". It reports D and some Latin witnesses reading πᾶσα γὰρ θυσία ἁλὶ ἁλισθήσεται ("for every sacrifice will be salted with salt"). A C K N Γ Θ Ψ and the Majority text read both clauses `[T]`, re-verified. Scribes heard Leviticus here and wrote it in.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Strong | An identical rare form with πᾶς ("every") in a sacrificial frame |
| Recurrence | Possible | Salt continues in 9:50 |
| Thematic Coherence | Strong | Fire and salt of the offering; "be at peace" |
| Historical Plausibility | Strong | — |
| History of Interpretation | Strong | The scribal glosses |
| Satisfaction | Strong | Makes sense of an obscure saying |

**Verdict:** Confirmed. Moderate–high, as proposed.

**Book-overview action:** Add a row "Lev 2:13 | 9:49–50 | moderate–high". Add a textual note: "D and the Majority text add Lev 2:13 wording; NA28 and the SBLGNT print the short text."

---

### Claim 13: Dan 7:14 (Theodotion) behind Mark 10:45

**Claim:** "Not to be served but to serve" deliberately reverses Dan 7:14 Theodotion, δουλεύουσιν αὐτῷ ("they serve him").

**Evidence.**

- **The verbs differ.** Mark has διακονέω ("to serve, wait on"). Theodotion has δουλεύω ("to serve as a slave"), and the Old Greek λατρεύουσα ("serving, in worship").
- **Mark's verb has no LXX background.** διακονέω does not occur as a verb anywhere in Swete, re-verified.
- **There is a pericope-level cluster that the sweep did not use.** The Old Greek of Dan 7:13–14 and Mark 10:37–45 share several terms:

| Mark 10 | Dan 7:13–14 |
|---|---|
| ἐν τῇ δόξῃ σου ("in your glory", 10:37) | πᾶσα δόξα ("all glory", OG) |
| τῶν ἐθνῶν ("of the nations") and κατεξουσιάζουσιν ("exercise authority over", 10:42) | πάντα τὰ ἔθνη ("all the nations") and ἐξουσία ("authority", OG) |
| πάντων δοῦλος ("slave of all", 10:44) | δουλεύουσιν ("they serve", Theodotion) |
| ὁ υἱὸς τοῦ ἀνθρώπου … ἦλθεν ("the Son of Man … came", 10:45) | the son of man coming (7:13) |

**Baseline.** Son of man, authority, the nations and glory occur together in one chapter in canonical Swete: Dan 7.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | Dan 7 is already live |
| Volume | Possible | The pericope cluster is distinctive; the verb is not shared |
| Recurrence | Strong | — |
| Thematic Coherence | Strong | — |
| Historical Plausibility | Strong | — |
| History of Interpretation | Possible `[S]` | — |
| Satisfaction | Possible | The reversal is the reader's construction |

**Verdict:** Needs reframing. Moderate for Dan 7:13–14 behind 10:35–45 as a whole. The "deliberate reversal" at 10:45 is uncertain and should be tagged `[I]`.

**Book-overview action:** Extend the Dan 7:13–14 row to "10:35–45" at moderate. Name the cluster (δόξα "glory", ἔθνη "nations", ἐξουσία "authority", δοῦλος/δουλεύω "slave/serve", the coming Son of Man). Tag "reversal" as `[I]`, and state that διακονέω does not occur in Swete.

---

### Claim 14: "Mark keeps Daniel's order" at 13:14–19

**Claim:** Mark 13:14 → 13:19 follows Daniel's sequence: first the abomination (Dan 11:31), then the unparalleled tribulation (Dan 12:1).

**Evidence.**

- **Daniel names the abomination on both sides of 12:1.** It appears at 9:27 and 11:31, *before* 12:1, and at 12:11, *after* it. So any order can be matched.
- **Mark's exact form comes from after 12:1.** Mark's articular τὸ βδέλυγμα τῆς ἐρημώσεως ("the abomination of desolation") matches **Old Greek Dan 12:11** exactly `[T]`, re-verified. Theodotion 12:11 has no article, and 11:31 differs in both versions.
- **The tribulation clause blends two texts.** Mark 13:19 is Theodotion Dan 12:1 plus "and never will be". That phrase matches Swete Exod 11:6, ἥτις τοιαύτη οὐ γέγονεν καὶ τοιαύτη οὐκέτι προστεθήσεται ("such as has not been, and such shall not be again"), of the last plague `[T]`, re-verified.
- **Mark 13 does not follow Daniel's order overall.** Mark puts the Son of Man's coming (13:26) after the abomination; Daniel puts it (7:13) before every abomination text.

**Verdict:** Needs reframing. The two individual rows stand at high. The "order" claim is uncertain and should be dropped.

**Book-overview action:** Add no "order" note. Annotate the Daniel rows as follows:

- 13:14 = OG Dan 12:11, word for word.
- 13:19 = Theodotion Dan 12:1 + "and never will be" (cf. Exod 11:6).

Exod 11:6 is a **new candidate** at moderate, for its own audit.

---

### Claim 15: Gen 18:14 behind Mark 10:27

**Claim:** πάντα γὰρ δυνατὰ παρὰ τῷ θεῷ ("for all things are possible with God") recalls Gen 18:14, μὴ ἀδυνατεῖ παρὰ τῷ θεῷ ῥῆμα; ("is anything impossible with God?").

**Evidence.**

- **The exact phrase.** παρὰ τῷ θεῷ ("with God") occurs in 2 canonical Swete verses, one of them Gen 18:14.
- **Rivals:**
  - **Job 42:2**, Οἶδα ὅτι πάντα δύνασαι, ἀδυνατεῖ δέ σοι οὐθέν ("I know that you can do all things, and nothing is impossible for you"). This shares more words than Gen 18:14 does.
  - **Zech 8:6.** This alone has Mark's contrast between humans and God.
  - **Jer 32:17, 27.** These have Genesis's Hebrew formula, but in Swete they are rendered with κρύπτω ("to hide"), so there is no Greek contact.
- **Luke 1:37 shows what a deliberate Gen 18:14 echo looks like.** It has ῥῆμα ("word") and a birth. Mark has neither.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Possible | A rare phrase; Job 42:2 shares as much or more |
| Recurrence | Possible | 9:23 and 14:36 repeat the idea |
| Thematic Coherence | Possible | A birth in Genesis; salvation in Mark |
| Historical Plausibility | Strong | — |
| History of Interpretation | Possible `[S]` | — |
| Satisfaction | Possible | A creedal commonplace |

**Verdict:** Confirmed with nuance. Moderate, as a cluster.

**Book-overview action:** Add a row "Gen 18:14; cf. Job 42:2; Zech 8:6 | 10:27 (and 9:23; 14:36) | moderate".

---

### Claim 16: Isa 40:8 behind Mark 13:31

**Claim:** "My words will not pass away" claims for Jesus' words what Isa 40:8 claims for God's word, and so frames the book with Isa 40 (1:3).

**Evidence.**

- **Isa 40:8 shares no words with Mark 13:31.** Swete reads τὸ δὲ ῥῆμα τοῦ θεοῦ ἡμῶν μένει εἰς τὸν αἰῶνα ("the word of our God remains for ever") `[T]`. It has no heaven, no earth and no "passing away".
- **Isa 51:6 matches the structure.** Heaven and earth wear out, "but my salvation will be for ever … my righteousness will never (οὐ μή) fail".
- **Theodotion Dan 7:14 supplies the verb.** It reads ἡ ἐξουσία αὐτοῦ ἐξουσία αἰώνιος ἥτις οὐ παρελεύσεται ("his authority is an everlasting authority which will not pass away") `[T]`, re-verified. That is Mark's verb, used of the Son of Man's rule five verses after Mark quotes Dan 7:13 (13:26).

**Baseline.** Used of something that endures, παρελευσ- ("will pass") occurs in Swete only at Ps 148:6 and Theodotion Dan 6:12 and 7:14.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Weak | Nothing is shared with Isa 40:8 |
| Recurrence | Possible | Dan 7 is cited at 13:26, which is stronger |
| Thematic Coherence | Possible | — |
| Historical Plausibility | Strong | — |
| History of Interpretation | Possible `[S]` | — |
| Satisfaction | Possible | — |

**Verdict:** Needs reframing. Isa 40:8 is uncertain. **Theodotion Dan 7:14 is a new candidate at moderate.**

**Book-overview action:** Add no Isa 40:8 row. Note at the Dan 7 row: "13:31 οὐ μὴ παρελεύσονται ('will not pass away'); cf. Dan 7:14 Th οὐ παρελεύσεται; cf. Isa 51:6". This candidate still needs its own audit.

---

### Claim 17: 1 Sam 10:1 and 2 Kgs 9:6 behind Mark 14:3

**Claim:** The pouring on Jesus' head recalls royal anointings.

**Evidence.**

- **Only κεφαλ- ("head") is shared.** Mark has καταχέω ("to pour over"), μύρον ("perfume") and ἀλάβαστρον ("alabaster jar"). Samuel and Kings have ἐπιχέω ("to pour on"), ἔλαιον ("oil") and φακός ("flask"). Mark never uses χρίω ("to anoint") here, and he interprets the act himself as burial (14:8) `[T]`.
- **Pouring on the head is priestly as well as royal.** It is used of priests (Exod 29:7; Lev 8:12; 21:10) as well as of kings.
- **The only Swete text with μύρον ("perfume") on a head is Aaron's** (Ps 132:2).
- **Song 1:12 shares more than Samuel does.** It has the king reclining and νάρδος ("nard").

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Weak | Only "head" is shared |
| Recurrence | Weak | — |
| Thematic Coherence | Possible | "Christ" means "anointed", but Mark says burial |
| Historical Plausibility | Possible | Royal or priestly |
| History of Interpretation | Possible `[S]` | — |
| Satisfaction | Weak | — |

**Verdict:** Needs reframing. Uncertain.

**Book-overview action:** Add no row. At most, a sentence: "anointing on the head evokes the anointed one (royal or priestly) without a specific source; Mark reads it as burial." Flag Song 1:12 for research only.

---

### Claim 18: 2 Kgs 9:13 behind Mark 11:8

**Claim:** The crowd spreading garments echoes Jehu's officers.

**Evidence.**

- **Only ἱμάτιον ("garment") is shared**, and that word occurs in 288 Swete verses.
- **Everything else differs.** Mark has ἔστρωσαν εἰς τὴν ὁδόν ("spread on the road"); Kings has ἔθηκαν ὑποκάτω αὐτοῦ ("put under him") on the steps. Mark's στιβάς ("leafy branch") does not occur in Swete.
- **The scene has no other OT parallel.** 2 Kgs 9:13 is the only OT scene in which garments are laid down at a royal acclamation.

| Criterion | Score | Reasoning |
|---|---|---|
| Availability | Strong | — |
| Volume | Weak | One common noun |
| Recurrence | Weak | — |
| Thematic Coherence | Possible | Jehu is an awkward type |
| Historical Plausibility | Possible | Could be custom, not a text |
| History of Interpretation | Possible `[S]` | — |
| Satisfaction | Possible | The only precedent for the act |

**Verdict:** Uncertain — flag for research. Uncertain.

**Book-overview action:** Add a low-confidence row at most: "parallel act, no verbal contact". Zech 9:9 stays the lead row for 11:1–10.

---

### Claim 19: Exod 12:14 behind Mark 14:9

**Claim:** εἰς μνημόσυνον αὐτῆς ("as a memorial of her") in a Passover setting recalls the Passover as μνημόσυνον ("memorial", Exod 12:14).

**Evidence.**

- **μνημόσυνον is common.** It occurs in 74 Swete verses across 61 chapters.
- **Exod 12:14 lacks εἰς ("as").** And its memorial is a feast day, not a deed told about someone.
- **Mark's exact phrase belongs to Leviticus.** μνημόσυνον αὐτῆς ("its memorial portion") occurs at Lev 2:2, 9, 16; 5:12; 6:15; and Num 5:26: the grain offering's memorial portion, burnt as ὀσμὴ εὐωδίας ("a fragrant aroma").
- **Exod 17:14 fits Mark's sense better.** "Write this as a memorial in a book" is a recorded deed.

**Verdict:** Discard.

**Reasoning:** The only link is a common word, and the phrase points to the grain-offering laws, not to the Passover. The Passover setting is already covered by the overview's Exod 12 row.

**Book-overview action:** Add nothing. Flag the fragrance-and-memorial link with Lev 2:2, 9 for the 14:3–9 dig, at uncertain.

---

### Claim 20: Isa 51:17, 22 behind Mark 14:36

**Claim:** "Remove this cup from me" recalls the cup of wrath that the LORD takes from Jerusalem's hand.

**Evidence.**

- **Only ποτήριον ("cup") is shared.**
- **Mark's verb is almost unused in the LXX.** παραφέρω ("to remove") occurs in Swete only at Ezra 10:7, in an unrelated sense.
- **Jer 25:15 (Swete 32:15) is closer.** It has τὸ ποτήριον … τούτου ("this cup"), the only Swete parallel to Mark's demonstrative.
- **The cup of judgement is a theme in several prophets:** Isa 51; Jer 25; Ezek 23:31–34; Ps 75:9; Lam 4:21; Hab 2:16.
- **The strongest objection is 10:39.** The disciples *will* drink Jesus' cup, which sits badly with a cup of divine wrath borne by him alone.

**Verdict:** Needs reframing. Moderate for the prophetic theme of the cup of wrath; uncertain for Isa 51 alone.

**Book-overview action:** Add a row "Isa 51:17–22; Jer 25:15–29; Ezek 23:31–34; Ps 75:9 (cup of the LORD's wrath) | 10:38–39; 14:36 | moderate". Note the 10:39 tension for the Gethsemane dig.

---

### Claim 21: Ps 38:12 (Swete 37:12) behind Mark 15:40

**Claim:** The women watching ἀπὸ μακρόθεν ("from a distance") recall "those near me stood far off".

**Evidence.**

- **The phrase is Mark's own habit.** Mark uses μακρόθεν in five verses, always as ἀπὸ μακρόθεν: 5:6; 8:3; 11:13 (a fig tree seen from a distance); 14:54; 15:40 `[T]`, re-verified. That is Mark's idiom, and the claim fails the random-passage test.
- **The women are the reverse of the psalm's deserters.** In Mark they are the followers who did not flee (15:41; cf. 14:50).
- **Luke, not Mark, moves toward the psalm.** Luke 23:49 adds the standing verb and "acquaintances" (cf. Swete Ps 87:9) `[I]`.

**Verdict:** Discard for Mark.

**Book-overview action:** Add nothing to Mark's map. Pass Ps 38:12 (with Ps 88:9) to the **Luke** overview as a candidate for Luke 23:49.

---

## Confidence Change Propagation

| Allusion | Previous confidence | New confidence | Sections to update |
|---|---|---|---|
| Jer 8:13 (+ Hos 9:10; Mic 7:1) at 11:12–21 | uncertain (overview); sweep proposed Hos 9 at moderate–high | **Jer 7:11 → 7:15; 8:13: moderate.** Hos 9:10–16: uncertain–moderate | Overview: Intertextual Map (Latter Prophets; Twelve), Live-sources summary (Hosea *not* live). Sweep: unit 25, Headline 4, Convergent 9, Tensions 1, Open Question 5 |
| Isa 63:19 at 1:10 | moderate | moderate (unchanged); 63:11 as context only | Overview: Isaiah row. Sweep: unit 1, Headline 4, Tensions 2, Open Question 4 |
| Amos 2:16 at 14:52 | — (sweep: moderate, "7th Hebrew case") | **uncertain; not a Hebrew-priority case**; Gen 39:12 named | Overview: "How Mark uses his Scriptures" list (stays at six). Sweep: unit 32, Headline 4, Tensions 3, Text-First triage list |
| Amos 8:9–10 at 15:33 | 8:9 moderate | 8:9 moderate; 8:10 discarded; Exod 10:22 rival | Overview: Twelve row. Sweep: unit 35 |
| Joel 2:10 at 13:24 | — | uncertain; note only | Overview: Isa 13:10 row note. Sweep: unit 29, Tensions 3 |
| Hag 2:15 at 13:2 | — | uncertain | Sweep: unit 28, Convergent 9, Tensions 5 |
| Jonah 4:9 at 14:34 | — | uncertain; Jonah **not** live | Overview: Ps 42–43 row note. Sweep: unit 32, Convergent 4, Tensions 5 and 9 |
| Exod 40:29 / Num 10:34 at 9:5–7 | — | **moderate** | Overview: Torah table (new row). Sweep: unit 18, Convergent 8 |
| Deut 9:19 at 9:6 | — | uncertain–moderate (note) | Overview: note on 9:6 |
| Exod 32 at 9:14–19 | — | discard | Sweep: unit 19, Convergent 8, Tensions 4 |
| Deut 32:20 complex at 9:19 | — | **moderate–high** | Overview: Torah table (new row) |
| Lev 2:13 at 9:49 | — | **moderate–high** | Overview: Torah table (new row), with the textual note |
| Dan 7:13–14 at 10:35–45 | high (13:26; 14:62); moderate (2:10) | moderate for 10:35–45; "reversal" `[I]` | Overview: Dan 7 row. Sweep: unit 23, Convergent 10, Tensions 5 |
| Daniel "order" at 13:14–19 | — | dropped; OG 12:11 and Exod 11:6 noted | Overview: Dan 9/11/12 and 12:1 rows. Sweep: unit 28, Headline 4, Tensions 6 |
| Gen 18:14 cluster at 10:27 | — | **moderate** | Overview: Torah table (new row) |
| Isa 40:8 at 13:31 | — | uncertain; Dan 7:14 Th new candidate | Sweep: unit 29, Tensions 5 |
| 1 Sam 10:1 / 2 Kgs 9:6 at 14:3 | — | uncertain | Sweep: unit 30, Convergent 12, Tensions 5 |
| 2 Kgs 9:13 at 11:8 | — | uncertain | Sweep: unit 25, Convergent 12, Tensions 5 |
| Exod 12:14 at 14:9 | — | discard | Sweep: unit 30, Tensions 5 |
| Isa 51:17, 22 at 14:36 | — | moderate as a multi-text theme | Overview: new theme row. Sweep: unit 32, Tensions 5 |
| Ps 38:12 at 15:40 | — | discard for Mark; pass to Luke | Sweep: unit 35, Tensions 5 |

## Recommended Book-Overview Revisions

1. **Rows to add at moderate or above:**
   - Exod 40:34–35 / Num 10:34 (9:5, 7)
   - Deut 32:20 complex (9:19)
   - Lev 2:13 (9:49)
   - Gen 18:14 cluster (10:27)
   - the prophetic cup of wrath (10:38–39; 14:36)
2. **Rows to revise:**
   - Jer 8:13 → Jer 7–8 at moderate, with Hos 9 as a secondary resonance.
   - Dan 7:13–14 extended to 10:35–45.
   - Daniel rows annotated with OG 12:11 and Exod 11:6.
   - Isa 13:10 row annotated with the φέγγος note.
   - Amos 8:9 row: add Exod 10:22 as a rival.
3. **Not to be added:** Amos 2:16 as a Hebrew-priority case; Amos 8:10; Exod 32; Exod 12:14; Ps 38:12; and Jonah as a live source.
4. **New candidates for a second audit:**
   - Exod 11:6 (13:19)
   - Theodotion Dan 7:14 (13:31)
   - Exod 10:22 (15:33)
   - Gen 39:12 (14:52)
   - Song 1:12 (14:3)
   - Lev 2:2, 9 (14:9)
5. **The overview's "nearer the Hebrew" list stays at six.**

## Consequences for the Sweep

The sweep is left unchanged as a record, with a post-audit note added under its header pointing here. Where the two disagree, this audit supersedes it. In particular:

- **Headline Finding 4** ("Scriptures as chapters … through the Hebrew") loses its Hosea, Isaiah 63:11–14 and Amos examples. It holds only for Ps 22 and the rows the overview already carries.
- **Convergent Findings 4, 8, 9 and 12**, and **Tensions 1–6 and 9**, are revised as set out in the propagation table.
- The sweep's **74 lexical chains within Mark are not affected**. The audit tested allusions, not chains.

## Tool Problem Found

`$HOME/work/rahlfs.py` returns the first chapter it finds with the requested number. The Rahlfs files combine 1–2 Samuel, 1–2 Kings and 1–2 Chronicles, so for the second book of each pair it returns the wrong verse. The third auditor caught this at 2 Kgs 9:13, where the helper returned 1 Kgs 9:13, and read the text by grep instead. No claim in the overview or the sweep drew on those files through the helper: the Rahlfs checks in both were in Isaiah, Hosea, Amos, Zechariah, the Psalms, Joel and Malachi. The helper should still be fixed before its next use.

## Open Questions for Logos

1. **Jer 7–8 and Hos 9 at 11:12–21.** Which do the commentaries favour, and on which text?
2. **Isa 63:11.** "Out of the sea" or "out of the land": what is the evidence in the Rahlfs apparatus?
3. **Exod 11:6 and Theodotion Dan 7:14.** Are these recognised in the literature as sources at 13:19 and 13:31?
4. **Rahlfs Theodotion Dan 7:14.** The folder's Rahlfs Daniel shows the Old Greek text, and the Theodotion export should be read for 7:14. Rahlfs and Swete differ in tense (δουλεύσουσιν / δουλεύουσιν, "will serve" / "serve").
5. **Ps 37:12.** Rahlfs has ἀπὸ μακρόθεν and Swete has μακρόθεν alone. What does the apparatus show? This is relevant to Luke, not Mark.

## Text-First Declaration

**Mode:** Claim Audit (Phase 0.5b), standalone file, 21 claims.

**Independence:** three fresh auditors, working blind to the sweep's reasoning. Each saw only the bare claim and the overview's current row. This run re-checked their decisive findings; it did not re-derive their verdicts.

**Primary texts opened by the auditors, on the device:**

- SBLGNT and the MorphGNT index for Mark and other NT books (Matthew, Luke, Hebrews).
- Swete for every OT wording and baseline.
- The Rahlfs text exports for Isaiah, Genesis, Exodus, Numbers, Deuteronomy, Leviticus, Jonah, Amos, Haggai, Daniel (OG), Job, Zechariah, Psalms and Kings.
- The WLC through `find.py` for every Hebrew form.
- The NA28 apparatus at Mark 9:9, 9:19 and 9:49.

**Controls:**

- **Negative controls.** Each of these failed with a non-zero exit, as intended:
  - `verify 3173 Amos:8:9`
  - `verify 4414 Lev:2:14`
  - `verify 3372 Deut:9:19` (which confirmed that Deut 9:19 uses יגר, "to dread", not ירא, "to fear")
  - `verify 3332 2Kgs:9:13`
- **Positive controls.** Every report of an absence or rarity was preceded by a search that returned a known hit. Examples: the ἐπισκια- pattern had to allow for the augment; the διακον- search returned the noun before the verb's absence was reported; the vocative "ὦ γενεά" pattern matched Mark 9:19 before its absence from Swete was reported.

**Problems met:**

- An accent-stripped stem search cannot tell ἁλίζω ("to salt") from ἀλισγέω ("to pollute"), or γενεά ("generation") from γένεσις ("origin"), so those counts were cleaned by hand.
- Swete's present-tense καταλείπων ("leaving") hid Gen 39 until the pattern was widened.
- The `rahlfs.py` fault described above.
- The Rahlfs exports lack the deuterocanonical books, so Rahlfs counts cover the Hebrew canon only.
- There is no LXX apparatus in the folder.

**Secondary sources:** none were opened. The History of Interpretation column says "not checked" or carries `[S]` for general knowledge, and no verdict rests on it.

**Warrant counts:** WARRANT_COUNTS.
