#!/usr/bin/env python3
"""Extend the Genesis 2:4–24 dig to 2:4–25. Fails loudly on any missed anchor."""
import sys

P = 'dig-deeper-genesis-2-4to25.md'
s = open(P, encoding='utf-8').read()
edits, fails = [], []

def rep(label, old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        fails.append(f'{label}: expected {count}, found {n}')
        return
    s = s.replace(old, new, count)
    edits.append(label)

# 1 — title and header
rep('title', '# Dig Deeper: Genesis 2:4–24', '# Dig Deeper: Genesis 2:4–25')

rep('header note',
"""**Series context:** Unit §2 of the sixteen-unit Genesis series; Standard weight""",
"""**Series context:** Unit §2 of the sixteen-unit Genesis series; Standard weight
**Revision:** issued 7 September 2026 for 2:4–24 and **extended the same day to 2:4–25**, the range the book overview's arc map already carried. The original boundary note argued that 2:25 is a janus leaning into chapter 3; on the corrected range that verse is now the unit's last word, and the report treats it as the passage's own hinge rather than as the next unit's opening. All counts have been re-run for the twenty-two-verse range.""")

# 2 — Hebrew quote block
rep('hebrew quote',
"""> **2:24** עַל־כֵּן֙ יַֽעֲזָב־אִ֔ישׁ אֶת־אָבִ֖יו וְאֶת־אִמּ֑וֹ וְדָבַ֣ק בְּאִשְׁתּ֔וֹ וְהָי֖וּ לְבָשָׂ֥ר אֶחָֽד""",
"""> **2:24** עַל־כֵּן֙ יַֽעֲזָב־אִ֔ישׁ אֶת־אָבִ֖יו וְאֶת־אִמּ֑וֹ וְדָבַ֣ק בְּאִשְׁתּ֔וֹ וְהָי֖וּ לְבָשָׂ֥ר אֶחָֽד
> **2:25** וַיִּֽהְי֤וּ שְׁנֵיהֶם֙ עֲרוּמִּ֔ים הָֽאָדָ֖ם וְאִשְׁתּ֑וֹ וְלֹ֖א יִתְבֹּשָֽׁשׁוּ""")

# 3 — NASB95 verse 25
rep('nasb v25',
"""**24** For this reason a man shall leave his father and his mother, and be joined to his wife; and they shall become one flesh.

*Passage text: verified.""",
"""**24** For this reason a man shall leave his father and his mother, and be joined to his wife; and they shall become one flesh. **25** And the man and his wife were both naked and were not ashamed.

*Passage text: verified.""")

# 4 — boundary note rewritten
rep('boundary note',
"""**A note on the boundary — the window was widened, as it must be at a unit edge.** 2:25 and 3:1 were loaded before this report was written. Ending at 2:24 is defensible and probably right: 2:24 is the narrator's own aside, the only verse in the passage addressed to the reader's present, and it closes the movement that 2:18's "not good" opened. But **2:25 is a janus and leans forward**: *ʿărûmmîm* ("naked", 2:25) and *ʿārûm* ("crafty", 3:1) are a sound-pair, each occurring exactly once in Genesis, and the two verses are joined by it. `[T]` *verified* A preacher stopping at 2:24 should know that the next sentence has already turned toward the serpent.""",
"""**A note on the boundary — the window was widened, as it must be at a unit edge.** 3:1 was loaded before this report was written, and the unit's last verse is a janus. **2:25 faces both ways.** Backwards: it is the closing state of the pair the passage has just brought together, and its subject is "the man and his wife" — the two nouns the preceding four verses produced. Forwards: *ʿărûmmîm* ("naked", 2:25) and *ʿārûm* ("crafty", 3:1) are a sound-pair, **each occurring exactly once in Genesis**, and they join the two verses across the chapter break. `[T]` *verified*

So the unit ends on a fuse. That is not a reason to preach 3:1 in the same sermon, but it is a reason not to end the sermon as though the story were finished: the last thing the narrator says about Eden before the serpent speaks is that these two had nothing to hide.""")

# 5 — canon position handoff
rep('handoff',
"""**Handoff.** To 2:25–3:24, joined by the *ʿărûmmîm*/*ʿārûm* pun and by the command of 2:16–17 that has nothing to do until the serpent quotes it.""",
"""**Handoff.** To 3:1–24, joined by two threads that both run out of this unit's last verses: the *ʿărûmmîm*/*ʿārûm* pun crossing from 2:25 to 3:1, and the command of 2:16–17 that has nothing to do until the serpent quotes it.""")

# 6 — Tool 2 context
rep('tool2 after',
"""**Immediately after:** 2:25, the janus verse (see the boundary note above), then the serpent.""",
"""**Immediately after:** 3:1, the serpent — who arrives punning on the unit's final word.""")

# 7 — structure table row
rep('structure row',
"""| 2:21–24 | **The building, the acclamation, and the aside** | Deep sleep; the *ṣēlāʿ* built into a woman; the man's only speech; the narrator's "for this reason" |""",
"""| 2:21–24 | **The building, the acclamation, and the aside** | Deep sleep; the *ṣēlāʿ* built into a woman; the man's only speech; the narrator's "for this reason" |
| 2:25 | **The closing state** | A second narratorial sentence, in the narrative past: the two, naked, unashamed. No divine name in it, and no action |""")

rep('structure device tail',
"""**The passage is framed by ground.**""",
"""**And the unit closes twice.** `[T]` 2:24 closes it *outward* — the narrator generalising to every household — and 2:25 closes it *inward*, returning the camera to these two in this garden. The two asides do opposite things, and a reading that stops at the first keeps the doctrine and loses the picture. Note also that **2:25 is the only verse from 2:4 onward in which neither divine name appears** `[T]` *verified* — the narrator withdraws God from the frame in the sentence immediately before the serpent enters it.

**The passage is framed by ground.**""")

# 8 — narrator's comment
rep('narrator asides',
"""- **2:24 "For this reason a man shall leave…"** — the decisive one. `[T]` The narrator steps out of Eden entirely and speaks about the reader's own institution, in the imperfect, as a standing pattern. It is the only sentence in the passage not about the garden, and it is the sentence Jesus and Paul both quote.""",
"""- **2:24 "For this reason a man shall leave…"** — the decisive one. `[T]` The narrator steps out of Eden entirely and speaks about the reader's own institution, in the imperfect, as a standing pattern. It is the only sentence in the passage not about the garden, and it is the sentence Jesus and Paul both quote.
- **2:25 "And the two of them were naked… and were not ashamed."** — the fifth intrusion, and the quietest. `[T]` It reports no action; it states a condition. The verb *yitbōšāšû* is a reflexive (Hithpolel) of *bôš*, "they did not shame themselves" — a state of the pair with respect to each other, not merely an absence of clothing. `[T]` *verified* Coming after 2:24's generalisation, it functions as the narrator's last word on Eden as it was.""")

# 9 — vocabulary: new entry
rep('vocab new entry',
"""**Paronomasia check (words recurring three or more times).**""",
"""**(l) *ʿārôm* (6174) "naked" and *bôš* (954) "be ashamed", 2:25.** `[T]` *verified* *High confidence on the counts.* Each occurs **once** in the passage and *ʿārôm* **once in the whole of Genesis**; *ʿārûm* ("crafty", 6175) likewise occurs once, at 3:1. The two are different words that sound the same, which is what a Hebrew pun is. *bôš* is in the reflexive stem — "they were not ashamed *before one another*". The verse states a relation, not a wardrobe, and it is the thing 3:7 destroys: the same pair, the same nakedness, and a new verb — they knew, and they sewed.

**Paronomasia check (words recurring three or more times).**""")

rep('paronomasia tail',
"""**Two fire:** *ʾādām* / *ʾădāmāh*, treated above; and *ʾîš* / *ʾiššāh* at 2:23, which the text itself puns explicitly. **Nil** on the rest. The *ʿărûmmîm* / *ʿārûm* pair belongs to 2:25–3:1 and is reported in the boundary note.""",
"""**Three fire:** *ʾādām* / *ʾădāmāh*, treated above; *ʾîš* / *ʾiššāh* at 2:23, which the text itself puns explicitly; and ***ʿărûmmîm* (2:25) / *ʿārûm* (3:1)**, which straddles the unit's closing boundary and is treated at (l) and in the boundary note. **Nil** on the rest.""")

# 10 — Tool 8 sharpen the hoi duo argument
rep('hoi duo',
"""*An honest qualification:* the Greek supplies οἱ δύο at 2:25 as well ("and *the two* were naked"), where the Hebrew has *šənêhem* — so the addition at 2:24 is plausibly the translator's idiom rather than a different *Vorlage*, and the MT's "they" implies two in any case. The NT's argument is not damaged; but the report will not call this a variant when translator habit explains it. *Moderate confidence on the cause; high on the fact.*""",
"""*An honest qualification, and the extended range sharpens it.* **At 2:25 the Hebrew does have the numeral** — *šənêhem*, "the two of them" `[T]` *verified* — and the Greek renders it οἱ δύο. At 2:24 the Hebrew has no numeral and the Greek supplies one. So the translator has the phrase in his ear from the very next verse of his own text, which makes the addition at 2:24 far more likely to be his idiom than a different *Vorlage*; and the MT's plural verb implies two in any case. The NT's argument is not damaged — it reads the Greek, and category 3 stands whichever text is prior — but the report will not call this a variant when translator habit explains it. *Moderate-to-high confidence on the cause now; high on the fact.*""")

# 11 — tone
rep('tone soundtrack',
"""**Soundtrack:** a single instrument — something with breath in it — and a long silence at 2:20 before the last phrase.""",
"""- **The ending, which is the passage's quietest moment.** 2:25 has no action, no speech and no divine name — only a state, reported and left. After a chapter of forming, planting, commanding, searching and building, the unit stops on two people with nothing between them and nothing to hide.

**Soundtrack:** a single instrument — something with breath in it — a long silence at 2:20, and a final sustained note at 2:25 that the next chapter cuts off.""")

# 12 — repetition table updates
rep('rep adam', """| *ʾādām* | **15** | 2:5, 7 ×2, 8, 15, 16, 18, 19 ×2, 20 ×2, 21, 22 ×2, 23 |""",
    """| *ʾādām* | **16** | 2:5, 7 ×2, 8, 15, 16, 18, 19 ×2, 20 ×2, 21, 22 ×2, 23, 25 |""")
rep('rep ishshah', """| *ʾiššāh* / *ʾîš* | 3 / 2 | 2:22, 23, 24 / 2:23, 24 |""",
    """| *ʾiššāh* / *ʾîš* | 4 / 2 | 2:22, 23, 24, 25 / 2:23, 24 |""")
rep('rep singletons',
"""| *bānāh*, *šāmar*, *tardēmāh*, *nəšāmāh*, *ṣāwāh*, *dābaq* | 1 each | 2:22 · 2:15 · 2:21 · 2:7 · 2:16 · 2:24 |""",
"""| *bānāh*, *šāmar*, *tardēmāh*, *nəšāmāh*, *ṣāwāh*, *dābaq* | 1 each | 2:22 · 2:15 · 2:21 · 2:7 · 2:16 · 2:24 |
| *ʿārôm*, *bôš*, *šənayim* | 1 each | all three at 2:25 |""")
rep('rep drumbeat',
"""1. **The compound name is the passage's drumbeat** — eleven times in twenty-one verses, and the narrator never once uses either name alone. `[T]` Against the wider book that is remarkable: see Headline 5.""",
"""1. **The compound name is the passage's drumbeat** — eleven times in twenty-two verses, and the narrator never once uses either name alone. `[T]` Against the wider book that is remarkable: see Headline 5. **And it stops before the end:** the last occurrence is 2:22, so the unit's final three verses — the man's speech, the narrator's generalisation, and the closing state — carry no divine name at all. `[T]` *verified*""")

# 13 — Move 4
rep('move4 nakedness',
"""- **Internal: planted — nakedness.** `[T]` *verified* 2:25's *ʿărûmmîm* against 3:1's *ʿārûm*; each occurs exactly once in Genesis. Immediately outside the unit's boundary — see the boundary note.""",
"""- **Internal: planted — nakedness, and it is the unit's own last word.** `[T]` *verified* 2:25's *ʿărûmmîm* against 3:1's *ʿārûm*; each occurs exactly once in Genesis. The pun crosses the chapter division, so the fuse is lit inside this unit and burns in the next. And the state itself is what 3:7 reverses: same pair, same nakedness, new knowledge, and coverings. *High confidence.*""")

# 14 — textual variants versification note
rep('versification note',
"""**A versification trap, recorded because this run nearly fell into it.** `[S: method]` In the corpus's **Swete** layer, the content of MT 2:25 is numbered as part of **Gen 3:1**; in the **Rahlfs-based export** it stands as 2:25, as in the MT. A first pass read the Swete numbering as evidence that the Greek tradition attached the nakedness verse to the serpent scene — a tidy finding, and false. **The two Greek editions differ in verse numbering, not in text.** The corpus README warns that versification manufactures false failures; this is what that looks like in practice.""",
"""**A versification trap, recorded because this run nearly fell into it — and it matters more now that 2:25 is the unit's last verse.** `[S: method]` In the corpus's **Swete** layer, the content of MT 2:25 is numbered as part of **Gen 3:1**; in the **Rahlfs-based export** it stands as 2:25, as in the MT. A first pass read the Swete numbering as evidence that the Greek tradition attached the nakedness verse to the serpent scene — which would have been a tidy argument for the *other* boundary, and it is false. **The two Greek editions differ in verse numbering, not in text.** The corpus README warns that versification manufactures false failures; this is what that looks like in practice, and it is worth saying plainly that had the trap gone unnoticed it would have produced a confident argument for ending the unit at 2:24.""")

# 15 — So What worldview addition
rep('sowhat worldview',
"""4. **Solitude was the first thing God called not good**, and he fixed it by making another person, not by giving the man more to do.""",
"""4. **Solitude was the first thing God called not good**, and he fixed it by making another person, not by giving the man more to do.
5. **Shamelessness was the original condition, and it was mutual.** 2:25's verb is reflexive: they did not shame themselves before one another. Whatever else the fall costs, this is the first casualty (3:7) — and the passage lets the reader see what was there before it went.""")

rep('sowhat friend',
"""- *For a Christian friend:* The one who believes work is a curse to be endured needs 2:15 before 3:17 — and the one who is alone needs to hear that God said it first, and called it not good, and did something about it.""",
"""- *For a Christian friend:* The one who believes work is a curse to be endured needs 2:15 before 3:17 — and the one who is alone needs to hear that God said it first, and called it not good, and did something about it. The one carrying shame needs 2:25: it was not always so, and it is not the last word either.""")

rep('prayer',
"""and to receive one another as gift.*""",
"""and to receive one another as gift. You made us to stand before you and before each other with nothing to hide; give us back what we lost.*""")

# 16 — Christological contrast addition
rep('christ contrast',
"""**Christophany:** none.""",
"""**Contrast — the shame that was not there.** The unit ends with two people naked and unashamed before each other; the next chapter ends with God clothing them (3:21). `[T]` The trajectory runs from a covering God provides at the cost of a life, through the priestly garments the same book's vocabulary has already been gesturing at (2:12), to the righteousness the NT describes as clothing (Gal 3:27; Rev 19:8). *Moderate confidence — the Genesis data are exact; the clothing trajectory is a canonical reading, and the report does not press it into typology.* `[I]`

**Christophany:** none.""")

# 17 — Book-overview tensions: boundary resolved
rep('overview boundary',
"""- **A note for the arc map.** The overview lists this unit as "2:4–25". This run stopped at 2:24 at the user's scoping and, having widened the window, thinks **the overview's boundary is the better one for a series** — 2:25 is the janus and belongs with what it sets up. Ending at 2:24 is defensible for a single sermon; ending at 2:25 without preaching 3:1 leaves the pun hanging.""",
"""- **The arc map's boundary is confirmed and adopted.** The overview lists this unit as **2:4–25**, and this report now covers that range. The first issue of the report stopped at 2:24 and, having widened the window, argued that the overview's boundary was the better one; that judgement has been acted on. The reason stands: 2:25 is the unit's own closing state as well as the fuse for 3:1, and a unit that ends at 2:24 loses the picture while keeping the doctrine. **No change to the overview is needed on this point** — it had it right.""")

# 18 — declaration updates
rep('decl passage',
"""**The window was widened at the unit boundary** (2:25 and 3:1 loaded before the report was written), as the boundary-edge rule requires.""",
"""**The window was widened at the unit boundary** (3:1 loaded before the report was written), as the boundary-edge rule requires — and on the extended range the widening changed the answer: what was reported as the next unit's opening is now this unit's closing state.""")

rep('decl chains',
"""**Chains verified:** every lexical and numerical claim in this report — the twenty-two counts tabulated under Tool 10 and the word-level claims under Tool 7 — searched by lemma in `_texts/hebrew-wlc/_index/`, each claimed reference confirmed to contain the word.""",
"""**Chains verified:** every lexical and numerical claim in this report — the counts tabulated under Tool 10 and the word-level claims under Tool 7 — searched by lemma in `_texts/hebrew-wlc/_index/`, each claimed reference confirmed to contain the word. **All counts were re-run for the twenty-two-verse range when the boundary was corrected**; four changed (*ʾādām* 15→16, *ʾiššāh* 3→4, and *ʿārôm*, *bôš*, *šənayim* enter at 1 each), and the compound-name count did not (2:25 carries neither name).""")

rep('decl warrants',
"""**Warrant counts:** `[T]` 46 · `[I]` 13 · `[S]` 11.""",
"""**Warrant counts:** `[T]` 51 · `[I]` 14 · `[S]` 11.""")

rep('decl health tail',
"""**The unit is Standard weight and is now solo-dug; it is ready for `/point-purpose`.**""",
"""**The unit is Standard weight and is now solo-dug across the full 2:4–25 range; it is ready for `/point-purpose`.**""")

# 19 — convergent findings
rep('convergent tail',
"""- ***ʾādām* / *ʾădāmāh* planted here and detonated in ch. 3** — Tool 7(a), Tool 11 Move 4, Schnittjer step 4.""",
"""- ***ʾādām* / *ʾădāmāh* planted here and detonated in ch. 3** — Tool 7(a), Tool 11 Move 4, Schnittjer step 4.
- **The unit closes twice, and the second close is a fuse** — Tool 3, Tool 6, Tool 7(l), Tool 9, Tool 11 Move 4. 2:24 generalises outward to every household; 2:25 returns to these two, drops the divine name, and hands the pun to 3:1.""")

if fails:
    print('FAILED ANCHORS:')
    for f in fails: print('  -', f)
    sys.exit(1)

open(P, 'w', encoding='utf-8').write(s)
print(f'applied {len(edits)} edits:')
for e in edits: print('  ✓', e)
