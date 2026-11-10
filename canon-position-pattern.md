# Canon Position — a Harvested Pattern

**Status:** Reference document. Harvested 4 September 2026 from three imported book overviews.
**Purpose:** to preserve, before those overviews are superseded or discarded, the one thing they contain that no document produced by this toolkit contains — an explicit statement of where a book stands in the canon and what that position does to the reading.
**Companion:** Amendment B in `dig-deeper-skill-amendments.md`, which proposes requiring this of every Old Testament passage. This document is its worked example.

---

## Why this was harvested

Of the thirty-three book overviews in this folder, **three carry a canon-position section, and all three were imported rather than produced here**:

| Document | Heading | Canon division |
|---|---|---|
| `Torah/Genesis/book-overview-genesis.md` | `HEBREW CANON POSITION` | Torah |
| `Ezra-Nehemiah/book-overview-ezra-nehemiah.md` | `HEBREW CANON POSITION` | Ketuvim |
| `1 Peter/book-overview-1-peter.md` | `CANONICAL POSITION` | General Epistles |

A fourth imported document, `Acts/dig-deeper-acts-book-overview.md`, has no such section — it is a differently shaped document that also names the NIV 2011 rather than the ESV as its pulpit text.

**The harvesting is a precaution, and the precedent is recent.** Two other imported overviews, Jeremiah and Leviticus, were superseded by fresh text-first builds on 28 August 2026. Both rebuilds wrote to the same filenames, and the repository's history begins on that same day with no commit touching any book-overview file. **Git holds no earlier copy of either.** Whatever those two contained is gone, and nobody looked before overwriting. If the remaining imported overviews go the same way, this section goes with them.

## The pattern

Reading the three together, a canon-position section is doing five jobs. The first three appear in all of them; the last two only in the fuller specimens.

| Field | The question it answers | Why it earns its place |
|---|---|---|
| **Section** | Which canon division, and where within it | The bare fact. Cheap to state, and it is what everything else hangs on |
| **Reading implication** | What does standing *there* do to how the book is read? | The interpretive payload. A section that stops at the label has not done the work |
| **Presupposes** | What has a reader of *this* sequence already met by the time they arrive? | **The field that does the most.** It converts canonical position from a label into a reading instruction, and it is testable — every item is a reference that either supports the claim or does not |
| **Handoff** | What does the book pass to the one that follows it? | Catches the seam. Genesis ends with a coffin and a command; Exodus 1:7 answers Genesis 1:28 |
| **Neighbours / unique contribution** | What sits either side, and what would be missing without this book? | Useful for a series; least load-bearing of the five |

**The distinguishing mark of a good one** is that it is *falsifiable*. "Ruth stands in the Ketuvim" is a fact. "A reader of the Ketuvim sequence arrives at Ruth having just been asked who can find a woman of worth" is a claim — and it can be checked.

## Worked example: Ruth

The strongest case for the whole amendment, because the reading it produces cannot exist in English Bible order, and because it verifies exactly.

- **Section:** Ketuvim, among the Megilloth. In the order BHS prints, Ruth stands **immediately after Proverbs**.
- **Reading implication:** Ruth is not an appendix to Judges. It is a Writings reflection, read by a community that already knows how the monarchy ended, on how the line to David ran through *ḥesed* and through a Moabite.
- **Presupposes:** Proverbs — and specifically its closing poem. Deuteronomy 23:3–4 (no Moabite in the assembly). Genesis 38 (Tamar, named at Ruth 4:12). The Judges period as setting, not as literary neighbour.
- **The seam, verified:** Proverbs closes by asking *ʾēšet-ḥayil mî yimṣāʾ* — "a woman of worth, who can find?" (31:10). The next book in the sequence answers: *kî ʾēšet ḥayil ʾātt* — "for you are a woman of worth" (Ruth 3:11), said of a Moabite by the whole town gate.

**Verification.** The phrase אֵשֶׁת חַיִל occurs three times in the Hebrew Bible: Proverbs 12:4, Proverbs 31:10, and Ruth 3:11. Counted from `_texts/hebrew-wlc/` by searching for lemma 802 immediately followed by lemma 2428. *(One further adjacency, Proverbs 31:3, is a different construction — "do not give your strength to women" — and is not the phrase; the search finds it because the two lemmas stand next to each other there too. Reported so the count is honest.)*

In English Bible order this reading is unavailable. Ruth sits after Judges; Proverbs is nineteen books away; the question and its answer never meet.

---


## The three harvested sections, verbatim

Reproduced exactly as they stand in the source documents, with inner headings demoted so they nest here. Nothing has been edited, corrected or modernised: the point is the shape, and an edited specimen is no specimen.

### Genesis

*Source: `Torah/Genesis/book-overview-genesis.md` (v5.0, May 2026). Canon division: Torah — opening scroll.*

- **Section:** Torah — first of the five books of Moses (the Pentateuch as a single five-scroll work)
- **Reading implication:** Genesis opens the Torah and thereby opens the entire Tanakh (Torah → Nevi'im → Ketuvim). As the Torah's opening scroll, it establishes the categories — creation, humanity, image, blessing, seed, land, covenant — within which all subsequent revelation operates. The Torah has been read as having an ABCB′A′ concentric structure (Genesis↔Deuteronomy, Exodus↔Numbers, Leviticus at the centre) — a literary proposal associated with Mary Douglas and developed theologically by Morales; defensible but not scholarly consensus, and weakest on the Exodus↔Numbers leg. What *is* strong, and load-bearing here, is the Genesis↔Deuteronomy pairing: both end with a patriarch/leader blessing the twelve tribes before dying outside the land. The "beginning" (*bereshit*) is paired throughout Scripture with "the end" (*ahrit hayyamim*, "last days"), signalling that creation has a trajectory and a goal — the book itself uses this frame (1:1 and 49:1).
- **Presupposes:** Nothing prior — Genesis is the origin point. However, its first readers encountered it in a context already shaped by the Exodus and Sinai events: the tabernacle was with them when they received this text (see Presenting Situation), meaning they would read creation, the garden, and the loss of the divine presence through that lens.
- **Handoff within the Tanakh:** Genesis ends in Egypt with a coffin and a command (50:24–26); Exodus 1:7 immediately shows the fulfilment of "be fruitful and multiply" (Gen 1:28) and Exodus 2:24 records God "remembering his covenant" — the deliberate echo of Genesis 8:1 ("God remembered Noah"). The Nevi'im begins with Joshua, which presupposes the entire Torah's unresolved tension (the land still not possessed) and answers it.

### Ezra-Nehemiah

*Source: `Ezra-Nehemiah/book-overview-ezra-nehemiah.md` (undated). Canon division: Ketuvim — the closing historical group.*

| Question                | Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Section**             | Writings (כְּתוּבִים) — in the final, forward-looking historical section (Esther, Daniel, Ezra-Nehemiah, Chronicles)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Reading implication** | Reflection literature, not straightforward history; the reader has already encountered the Torah's covenant promises and curses, the Prophets' announcements of exile and restoration, and Daniel's apocalyptic vision of the seventy sevens. Ezra-Nehemiah presupposes all of this and narrates the *partial* historical fulfilment — a return that is real but profoundly incomplete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Presupposes**         | **Torah:** Genesis 1–11 (creation, Babel/Shinar, Abrahamic promise); Exodus 12 (plundering Egypt — typologically replayed); Leviticus 5–6 (reparation offering behind mass divorce); Leviticus 23 (festivals — Tabernacles, Passover); Leviticus 26:40–45 (exile confession leading to covenant remembrance); Deuteronomy 7:1–4 (prohibition against covenant-breaking marriages); Deuteronomy 23:3–8 (law of the assembly); Deuteronomy 28–30 (covenant curses, exile, and the promise of return — but critically, Nehemiah stops short of Deut 30:6, circumcision of the heart). **Prophets:** Isaiah 40–55 (new exodus, Cyrus named in 44:28–45:1, "stirred up" language in 45:13); Isaiah 56–66 (the vision of restored Zion, servants, and glory that Ezra-Nehemiah positions us as still awaiting); Jeremiah 25:11–12; 29:10 (seventy years); Haggai 1:14 ("stirred up the spirit"); Haggai 2:3–9 (glory of the latter house — promised but not yet arrived); Zechariah 8:23 (nations grabbing hems). **Writings:** Daniel 9 (seventy weeks — the exile is not over until the Messiah comes); Psalms 89, 106, 132, 137 (exile prayers using "remember" language that Nehemiah echoes). |

**The crucial hermeneutical key:** Ezra-Nehemiah is placed in the Writings, not the Prophets, because its function is not to announce God's word fresh but to *narrate what happened when the prophetic promises began to be fulfilled* — and to show that the fulfilment, while real, is devastatingly partial. It is the Bible's record of what Dempster calls "exile in the land" — a return in body but not in spirit. The seventy years of Jeremiah may be over, but the seventy weeks of Daniel have only just begun.

### 1 Peter

*Source: `1 Peter/book-overview-1-peter.md` (undated). Canon division: General Epistles.*

##### Section
- **Collection:** General Epistles (Hebrews–Jude)
- **This book's position:** Middle of the General Epistles; the first of two Petrine letters
- **Reading implication:** Non-Pauline apostolic letter; pastoral instruction to churches the author did not plant but has apostolic responsibility for. Broadens the NT's voice beyond Paul — Peter and Paul share common tradition (cf. 1 Cor 15:11) but Peter's emphasis on exile identity and the suffering-to-glory pattern is distinctive
- **Presupposes:** Torah (Exodus 12, 19, 24; Leviticus holiness code; Genesis — Abraham/Sarah, Noah); Prophets (Isaiah extensively — chs. 8, 11, 28, 40, 43, 52–53); Psalms (34, 118); Hosea 1–2; Proverbs 3, 11; the Gospel events (Christ's death, resurrection, ascension); early Christian tradition shared with Paul
- **Building or reflecting?** Building — constructing a theological framework for how the eschatological people of God should live as a marginalised minority in a hostile society, grounded in Christ's suffering-to-glory pattern
- **Preceding book (canonical):** James — shares diaspora language (Jas 1:1) and concern for practical conduct, but addresses internal community issues (wealth, speech, favouritism) while 1 Peter addresses the community's relationship with hostile outsiders
- **This book's unique contribution:** The NT's most sustained treatment of how gospel identity shapes conduct under social pressure — neither accommodating nor retaliating, but doing good under fire, following Christ's pattern, trusting the righteous Judge
- **Handoff to next book:** 2 Peter shifts from external threats (social hostility) to internal threats (false teachers). The "stand firm" of 1 Peter 5:12 becomes the "grow in grace and knowledge" of 2 Peter 3:18 — having weathered persecution, the church must now guard its doctrine

##### This Matters Because
1 Peter is the New Testament's most concentrated treatment of how the gospel of Jesus Christ shapes the believer's engagement with a hostile culture. It draws more heavily on the OT per verse than almost any other NT book, and its hermeneutical key (1:10–12) explicitly claims that the prophets wrote *to serve* these communities. Peter constructs the church's identity from Israel's Scriptures and then shows what that identity demands in the midst of social suffering. Without 1 Peter, the canon would lack a sustained, apostolic treatment of Christian identity and conduct under social pressure — neither retreating nor retaliating but doing good while trusting God for vindication.


---

## Health warning on the content

**Keep the shape; test the claims.** These sections are secondary-source work by nature. The Genesis one names its sources at the head of its document — Cornhill Plus lecture transcripts, Dempster's *Dominion and Dynasty*, Morales's *Who Shall Ascend the Mountain of the Lord*, Schnittjer — and its claims are `[S]` accordingly. It is candid about this in places (the ABCB′A′ Torah structure is flagged as "defensible but not scholarly consensus, and weakest on the Exodus↔Numbers leg"), which is a good sign, but candour is not verification.

Three specific things to test before any of this content is reused:

1. **Every item in a `Presupposes` list is a reference**, and every reference is checkable. The Ezra-Nehemiah list is long and precise — Leviticus 26:40–45, Deuteronomy 30:6, Haggai 1:14, Daniel 9 — which makes it the most useful and the most auditable of the three.
2. **The Ezra-Nehemiah entry's sharpest claim** — that Nehemiah "stops short of Deut 30:6, circumcision of the heart" — is an argument from absence. Under the toolkit's own rule, an absence may be reported only where the pattern that makes it visible can be cited with instances. It may well hold; it has not been shown here.
3. **The 1 Peter section's canonical neighbours** (James before, 2 Peter after) are stated as though the ordering were doing interpretive work. In the General Epistles that ordering is far less settled than the Tanak's, and the claim should be weighted accordingly.

## What to do with this

- **Amendment B** carries the field template and the Ruth worked example, so the pattern survives independently of these three documents.
- **The three source documents** can now be superseded, rebuilt or retired without losing the section.
- **When our own overviews gain a canon-position section**, the `Presupposes` field is the one to spend effort on, and the one to verify — it is the only field that produces testable claims rather than orientation.

---

*Harvested 4 September 2026. The three sections below the pattern are reproduced verbatim from their source documents; the pattern, the Ruth example and this warning are new.*
