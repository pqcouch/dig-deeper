#!/usr/bin/env python3
"""Apply the Genesis claim-audit corrections to the whole-book sweep.

Reports every edit; exits non-zero if any anchor fails to match, so a silent
miss is impossible.
"""
import sys

P = 'dig-deeper-genesis-whole-book.md'
s = open(P, encoding='utf-8').read()
edits = []
fails = []

def rep(label, old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        fails.append(f'{label}: expected {count} match(es), found {n}')
        return
    s = s.replace(old, new, count)
    edits.append(label)

# ---------------------------------------------------------------- 1. header
rep('header',
"""**Translation:** ESV (Anglicised) — the pulpit text at CCH; wording transfers directly to `/sermon-creator`
**Date:** 14 July 2026
**Mode:** Multi-Passage Sweep (16 preaching units, §1–§16), proportional depth
**Book-overview context:** In conversation — `Genesis_Book_Overview.md` (which already folds in prior dig-deeper runs, treated here as a secondary source to check against, not the substrate)
**Series context:** 16-week Genesis series (baseline Focus throughout; §8, §9, §12 carry live splits)""",
"""**Primary texts:** WLC Hebrew and Swete LXX from `_texts/` for observation; `_texts/logos-exports/` (BHS Genesis, Rahlfs-based LXX Genesis, NASB95 Genesis) for citation
**Study text:** NASB95 (1995 edition)
**Pulpit text:** None declared — no sermon is in view for a sweep. Where a unit is taken to the pulpit, declare the text then and re-run Tool 8's divergence check
**Date:** 14 July 2026 · **revised 7 September 2026 (v2.0.0)**
**Mode:** Multi-Passage Sweep (16 preaching units, §1–§16), proportional depth
**Book-overview context:** `book-overview-genesis.md` v1.0.0 (7 September 2026, text-first) — rebased at revision; the July run was built against the imported `Genesis_Book_Overview.md`, now superseded
**Claim audit:** `dig-deeper-genesis-claim-audit.md` v1.0.0 — its verdicts are applied throughout and tagged `[S: audit]`
**Series context:** 16-week Genesis series (baseline Focus throughout; §8, §9, §12 carry live splits)

---

## Revision note — what changed on 7 September 2026

This document was written on 14 July, seven weeks before the `_texts/` corpus existed. Its original Text-First Declaration was candid about the consequence: every wording-dependent finding had been *"checked against the Hebrew as recalled."* On 7 September all of it was checked mechanically for the first time, against the WLC lemma index, and the results are in `dig-deeper-genesis-claim-audit.md`.

Of 28 checkable claims in this sweep, 14 were confirmed outright, 7 confirmed with a nuance, 4 needed reframing, 2 were wrong, and 1 open question is now closed. **Every failure was a number or a superlative; no claim about meaning failed.** The corrections are applied below and each is marked `[S: audit]` where it changes what the sweep said. Two findings the sweep missed have been added: the *taḥat* at 50:19, and the Genesis 3:15 LXX divergence.

The header has also been rebased: NASB95 is now the study text, no pulpit text is assumed for a sweep, and the book-overview thread-set below comes from the September text-first overview rather than the imported document the July run used.""")

# ------------------------------------------------- 2. book-level threads
rep('threads/intertextual',
"""**Intertextual map.** Live external sources are thin (Genesis is mostly *alluded to* rather than *alluding*); the dense intertextuality is **internal** (early↔late echoes) and **forward** (the NT reading Genesis). Key internal welds: 3:5 "like God" ↔ 50:19 "Am I in the place of God?"; 1:28 ↔ 47:27 (near-verbatim); Table of 70 nations (10) ↔ 70 descendants (46:8–27); Babel's grasped name (11:4) ↔ Abram's given name (12:2); *tēbâ* (ark, 6–9 / Moses' basket) and *ʾārôn* (Joseph's coffin, 50:26). The verbal welds proving Gen 38's placement: *haker-nāʾ* (37:32 ↔ 38:25) and *ʿārēv* (38:17–18 ↔ 43:9/44:32).""",
"""**Intertextual map.** **Genesis quotes nothing and alludes to nothing** — there is no earlier scriptural source, and the September overview establishes this as the book's defining intertextual fact rather than a gap in the sweep. The consequence for every unit below: **Tool 11 Move 2 has nothing to track in the normal direction, and Move 4 (internal echo) carries the whole load.** The dense intertextuality is internal (early↔late echoes) and forward (the NT reading Genesis).

*Verbal welds — each verified by lemma against `_texts/hebrew-wlc/`:* *haker-nāʾ* at 37:32 ↔ 38:25 (identical form, Hiphil imperative + נָא); *ʿārēv* — one root, two words: *ʿērābôn* 38:17, 18, 20 ↔ *ʿārav* 43:9, 44:32; *taḥat* "instead of" 22:13 → 44:33 → **50:19** (see §16); *tēbâ* (6–9, and Moses' basket, Exod 2:3, 5 — the only occurrences in the canon) ↔ *ʾārôn* (50:26, its only occurrence in Genesis); Babel's grasped *šēm* (11:4) ↔ Abram's given *šēm* (12:2); *pāqōd yipqōd* (50:24) ↔ *pāqōd pāqadtî* (Exod 3:16).

*Two links reclassified at the September audit* `[S: audit]`**:** 1:28 ↔ 47:27 is a **two-root echo** (*pārāh* + *rābāh*), not near-verbatim — 9:1 is the near-verbatim partner of 1:28; and 3:5 "like God" ↔ 50:19 "in the place of God" is **conceptual, not verbal** — the only shared word is *ʾĕlōhîm*. The seventy-to-seventy link is likewise mixed: 46:27 **states** שִׁבְעִים `[T]`, while the seventy of ch. 10 is a scholarly count the chapter never makes `[S]` — and the LXX reads **seventy-five** at 46:27, which Acts 7:14 follows.""")

rep('threads/presenting',
"""**Presenting situation.** Wilderness Israel, redeemed from Egypt, camped between Egypt and a land of giants — frightened, prone to return. Genesis is *pastoral literature before it is history*: it strengthens faith. It runs a polemic against ANE cosmologies (the moon is a lamp, 1:16; the sea is gathered water). Moses writes looking back; the tabernacle stands among the first hearers, re-opening the question of presence Eden closed. Dominant emotional register: **faithful waiting under threat**.""",
"""**Presenting situation.** `[S: audit — rebased on the September overview]` The wilderness-Israel setting used throughout the July run is a **reconstruction, not a datum of the book**: Genesis names no author, no audience and no occasion, and the Mosaic attribution comes from elsewhere in the canon and from tradition. Tag it `[S]` wherever it does work below, and do not let it become `[T]`. What the book *does* show on its page is a narrator writing long after the events (12:6; 36:31; six "to this day" asides at 19:37, 38; 26:33; 32:32 [Heb 32:33]; 35:20; 47:26) and a reader standing at the head of the canon with no prior text behind him. The measurable pressure the book answers: *bārak* runs 6× in chapters 1–11 and 67× in 12–50, against *ʾārar* 5× and 4× — the dominant word inverts at the call of Abram. Dominant emotional register: **faithful waiting under threat**.""")

# ------------------------------------------------------------ 3. §1 counts
rep('§1 counts',
"""**The seven-structure [S, overview]:** 1:1 = seven Hebrew words; 1:2 = fourteen; "it was good" ×7; God speaks ten times; 2:1–3 = 35 words. Numerical completeness is the text's own signal. Flagged for the preacher; *moderate* on the exact counts without re-counting.""",
"""**The seven-structure — all five counts verified** `[S: audit]` **[T]** *high*: 1:1 = **7** accent-unit tokens; 1:2 = **14**; *ṭôv* "good" **7×** (1:4, 10, 12, 18, 21, 25, 31); God speaks **10×** (*wayyōʾmer*, 1:3, 6, 9, 11, 14, 20, 24, 26, 28, 29); 2:1–3 = **35** tokens. Counted in the WLC. What the July run flagged *moderate* on recall is now high-confidence and reproducible in one command; numerical completeness is the text's own signal.""")

# --------------------------------------------------------- 4. §3 LXX 3:15
rep('§3 LXX',
"""### Difficult / Contested Verses
3:16 ("your desire shall be for your husband, and he shall rule over you")""",
"""### Translations / Ancient versions (Tool 8) — added at revision `[S: audit]`
The July run worked 3:15 from the Hebrew alone and never ran the ancient-versions check on the book's most-preached verse. It matters here. **The LXX reads αὐτός** — a *masculine* singular pronoun against the *neuter* antecedent σπέρμα: αὐτός σου τηρήσει κεφαλήν. Verified in Swete and in the Rahlfs-based export; the two agree. Under the Three-Way Triage this is **category 1 shading into category 3** — the Greek personalises what the Hebrew leaves collective, and that reading is what stands behind the NT's own handling of the seed. *The divergence: high confidence. The translator's messianic intent: genuinely disputed — do not preach the grammatical mismatch as proof.* **[T]** on the datum, **[S]** on the intention.

### Difficult / Contested Verses
3:16 ("your desire shall be for your husband, and he shall rule over you")""")

# ------------------------------------------------------------ 5. §5 nuach
rep('§5 nuach',
"""- *nûaḥ* ("rest") puns on *Nōaḥ* ("Noah," cf. 5:29, "he shall bring us relief"). *High.* **[T]**""",
"""- *Nōaḥ* and rest — **corrected at the September audit** `[S: audit]`. The July run claimed the name puns on *nûaḥ* "cf. 5:29"; **5:29's verb is *nāḥam*** (5162, "comfort"), not *nûaḥ*. The mismatch between the name and the etymology 5:29 supplies is a real crux, not something to resolve silently. **And the finding underneath is better:** *nûaḥ* (5117) occurs **exactly once in Genesis — 8:4**, where the ark *rested* (וַתָּנַח) on Ararat. The one place Genesis uses the verb the name sounds like is of Noah's own vessel coming to rest. *High* on both facts. **[T]**""")

rep('§5 schnittjer leading word',
"""(2) *leading word* — *tēbâ* welds Noah↔Moses **[T]**;""",
"""(2) *leading word* — *tēbâ* welds Noah↔Moses; 8392 occurs 28× in the canon, 26 of them in Gen 6–9 and the other two at Exod 2:3, 5 **[T]** *verified*;""")

# ------------------------------------------------------------- 6. §6 seventy
rep('§6 seventy',
"""Genealogy (10; 11:10–26) is theological architecture, not filler — note the 70 nations (the number matters: 70 ↔ Jacob's 70, 46:27). The Table maps the *world* Abram is sent to bless. **[T]**""",
"""Genealogy (10; 11:10–26) is theological architecture, not filler. **On the seventy, be exact** `[S: audit]`: Genesis 10 nowhere says seventy — the figure is a count that requires editorial decisions the chapter does not make (whether cities, gentilic plurals and Nimrod are counted), and the WLC yields 86 distinct proper-noun lemmas before any of them are taken. **[S]/[I]** Genesis 46:27, by contrast, *states* שִׁבְעִים **[T]** — and the LXX there reads **seventy-five**, which is the number Acts 7:14 uses. Preach the correspondence if you wish; do not present the ch. 10 seventy as something the text counts out. The Table maps the *world* Abram is sent to bless. **[T]**""")

# ------------------------------------------------------------ 7. §7 stem
rep('§7 stem',
"""- 12:3 *wĕnivrĕkû* ("shall be blessed"; niphal/possibly hithpael) — passive "be blessed" or reflexive "bless themselves"; Paul reads the passive (Gal 3:8). *Moderate* on the stem; *high* on Paul's use. **[T]/[S: NT]**""",
"""- 12:3 *wĕnivrĕkû* — **the stem is settled, and it is not one stem but two** `[S: audit]`. Checked word by word in the WLC morphology: **niphal** at 12:3 (VNp3cp), 18:18 (VNq3cp) and 28:14 (VNp3cp); **hithpael** at 22:18 (Vtq3cp) and 26:4 (Vtq3cp). The nations-blessing refrain occurs five times and **alternates**. Paul quotes it passively (Gal 3:8, ἐνευλογηθήσονται). *High* on the morphology; the *meaning* of the alternation remains the open question — a better one than the July run left standing. **[T]/[S: NT]**""")

# ----------------------------------------------------- 8. §9 tachat triad
rep('§9 tachat',
"""- *taḥat* (22:13) — the ram offered "*instead of*" his son; the first term in the book's substitution grammar (→ 44:33). *High.* **[T]** *(cross-report §15, Cross-Passage capstone.)*""",
"""- *taḥat* (22:13) — the ram offered "*instead of*" his son; the first term in a **three-term** substitution grammar `[S: audit]`. 8478 occurs 30× in Genesis, almost all as the ordinary preposition "under"; three carry the substitutionary sense — the ram *taḥat* the son (22:13), Judah *taḥat* the boy (44:33), and **Joseph refusing to stand *taḥat* God (50:19)**. *High.* **[T]** *(cross-report §15, §16, Cross-Passage capstone.)*""")

# ------------------------------------------- 9. §11/§13 goat chain on izzim
rep('§11 goat',
"""The deception of 27 turns on the senses (blind Isaac feels, smells, tastes) and the *goat-kid* (27:9, 16) — the same goat-deception motif that recurs at 37:31 and 38:17. **[T]**""",
"""The deception of 27 turns on the senses (blind Isaac feels, smells, tastes) and the goat (27:9, 16) — the same goat-deception motif that recurs at 37:31 and 38:17. **The chain runs on *ʿizzîm* (5795), not on *gədî*** `[S: audit]`: *gədî* stands at 27:9, 16 and 38:17, 20, 23 but **not at 37:31**, which reads שְׂעִיר עִזִּים. Stated on *ʿizzîm* the chain holds at all three points. **[T]** *verified*""")

rep('§13 goat',
"""- The *goat-kid* deception motif: Jacob deceived Isaac with a goat (27:9,16); the brothers dip Joseph's robe in *goat's blood* (37:31); Judah sends a *goat* to Tamar (38:17). *High.* **[T]**""",
"""- The goat-deception motif, **stated on the word that actually runs through it** `[S: audit]`: *ʿizzîm* (5795) at 27:9, 16 (Jacob deceives Isaac); 37:31 (the brothers dip the robe in the blood of a שְׂעִיר עִזִּים); 38:17, 20 (Judah's pledge-goat to Tamar). The July run ran the chain on *gədî*, which is absent from 37:31 — the middle term failed and the motif did not. *High.* **[T]** *verified*""")

rep('§13 schnittjer goat',
"""(2) *foreshadowing/goat motif* — 27→37→38 **[T]**;""",
"""(2) *foreshadowing/goat motif* — 27→37→38, on *ʿizzîm* **[T]** *verified*;""")

# ------------------------------------------------ 10. §14 presence + tsaleach
rep('§14 presence',
"""- "the LORD was *with* him" (39:2, 21) — the **presence** vocabulary (cf. 26:24; 28:15; 46:4), the book's second originated programme, running to Immanuel (Matt 1:23). *High.* **[T]**
- *ṣālēaḥ* ("succeed/prosper," 39:2–3, 23) — Joseph prospers because the LORD makes him prosper, not by self-help. *High.* **[T]**""",
"""- "the LORD was *with* him" — **four times in ch. 39, not three** `[S: audit]`: 39:2, **39:3** ("his master saw that the LORD was with him" — the one an Egyptian can see), 39:21, 39:23. And the programme is far wider than the July run claimed: the formula also stands at 21:20, 21:22, 26:3, 26:24, 26:28, 28:15, 28:20, 31:3, 31:5, 35:3, 46:4 and 48:21 — sixteen places, including an outsider's observation (21:22) and Jacob's conditional (28:20). It runs to Immanuel (Matt 1:23). *High.* **[T]** *verified*
- *ṣālēaḥ* ("succeed/prosper," 39:2, 3, 23) — Joseph prospers because the LORD makes him prosper, not by self-help. **And it is a shared thread, not a Joseph word** `[S: audit]`: 6743 also stands four times in ch. 24 (vv. 21, 40, 42, 56), of the servant's journey. The same verb carries the providence of §10 and the providence of §14. *High.* **[T]** *verified*""")

# ---------------------------------------------- 11. §15 longest-speech
rep('§15 structure speech',
"""Two journeys (42; 43–44) building to Judah's speech (44:18–34, the longest speech in Genesis — narrative braking = weight) and the reveal (45:1–15). "God sent me" recurs three times in 45:5–8 — the interpretive drumbeat. **[T]**""",
"""Two journeys (42; 43–44) building to Judah's speech (44:18–34) and the reveal (45:1–15). **The superlative is withdrawn** `[S: audit]`: counted in accent units from the WLC, Judah's speech runs to **186**, against **198** for the servant's speech at 24:34–49 and **249** for Jacob's blessing at 49:1–27. It is the longest speech by any of the twelve brothers, and the narrative-braking argument does not need more than that. *šālaḥ* recurs three times at 45:5, 7, 8 — and note the third is contrastive ("it was not **you** who sent me here, but God"), which is the drumbeat's point. **[T]** *verified*""")

rep('§15 schnittjer speech',
"""(1) *narrative braking* — Judah's speech is the longest, marking the moral peak **[T]**;""",
"""(1) *narrative braking* — Judah's speech is the longest by any of the brothers, marking the moral peak **[T]** *(the "longest in Genesis" superlative withdrawn at the September audit)*;""")

# ------------------------------------------------------- 12. §16 bookends
rep('§16 bookends',
"""- 1:28 "be fruitful and multiply" ↔ 47:27 "were fruitful and multiplied greatly" (near-verbatim) — the mandate fulfilled, but in Egypt.
- Table of 70 nations (10) ↔ 70 descendants (46:8–27) — a new humanity.
- 3:5 / 11:4 "be like God / make a name" ↔ 50:19 "Am I in the place of God?" — the god-complex thread *resolved*: what Adam and Babel grasped, Joseph refuses.""",
"""- 1:28 "be fruitful and multiply" ↔ 47:27 "were fruitful and multiplied greatly" — **a two-root echo (*pārāh* + *rābāh*), not near-verbatim** `[S: audit]`; 9:1 is the near-verbatim partner of 1:28. The theological point stands undamaged: the mandate is reported fulfilled, and in Egypt. *moderate*
- The seventy of ch. 10 ↔ the seventy of 46:8–27 — **mixed warrant** `[S: audit]`: 46:27 states שִׁבְעִים **[T]**, ch. 10 never states a number **[S]**, and the LXX reads seventy-five at 46:27, which is what Acts 7:14 follows. Name the variant rather than preaching a tidy 70↔70.
- 3:5 / 11:4 "be like God / make a name" ↔ 50:19 "Am I in the place of God?" — the god-complex thread *resolved*: what Adam and Babel grasped, Joseph refuses. **Conceptual, not verbal** `[S: audit]` — the only word 3:5 and 50:19 share is *ʾĕlōhîm*. *moderate*
- ***taḥat*, and this one *is* verbal — the audit's own find** `[S: audit]`. 50:19 reads הֲתַחַת אֱלֹהִים אָנִי. The word is the substitution word: the ram stands *taḥat* the son (22:13), Judah offers to stand *taḥat* the boy (44:33), and Joseph refuses to stand *taḥat* God (50:19). The book's substitution grammar and its god-complex thread **meet in a single word at the closing scene**, and the July run tracked both without noticing they converge. *High.* **[T]** *verified*""")

# --------------------------------------------------- 13. cross-passage fixes
rep('cross 2',
"""**2. The Judah arc is the patriarchal narrative's moral spine. [strong]** Fall (37:26, §13) → nadir (38:26, §13) → surety (43:9, §15) → substitution (44:33, §15) → throne (49:8–12, §16). The two welds (*haker-nāʾ*, *ʿārēv*) prove it is one designed arc. Judah, not Joseph, carries the king's line — by grace, through moral wreckage. A series that reaches ch. 44 without naming this has missed the moral heart of the book. **[T]**""",
"""**2. The Judah arc is the patriarchal narrative's moral spine. [strong]** Fall (37:26, §13) → nadir (38:26, §13) → surety (43:9, §15) → substitution (44:33, §15) → throne (49:8–12, §16). The two welds prove it is one designed arc — *hakker-nāʾ* at identical form (37:32 ↔ 38:25) and the ʿ-r-b root in two words (*ʿērābôn* 38:17, 18, 20 ↔ *ʿārav* 43:9, 44:32), both verified by lemma. Judah, not Joseph, carries the king's line — by grace, through moral wreckage. A series that reaches ch. 44 without naming this has missed the moral heart of the book. **[T]** *(the "longest speech in Genesis" claim once attached here is withdrawn — see §15.)*""")

rep('cross 3',
"""**3. A substitution vocabulary climbs toward the cross. [high]** Ram *taḥat* Isaac (22:13, §9) → Judah *taḥat* Benjamin (44:33, §15); "did not spare" (LXX 22:16) → Rom 8:32; "God will provide the lamb" (22:8) → John 1:29; singular seed (22:17) → Gal 3:16. The grammar of substitution is built incrementally and detonated in the NT. **[T/S: NT]**""",
"""**3. A substitution vocabulary climbs toward the cross — and it has three terms, not two. [high]** Ram *taḥat* Isaac (22:13, §9) → Judah *taḥat* Benjamin (44:33, §15) → **Joseph refusing to stand *taḥat* God (50:19, §16)** `[S: audit]`; "did not spare" (LXX 22:16, οὐκ ἐφείσω) → Rom 8:32 (οὐκ ἐφείσατο — Paul's verb is the LXX's); "God will provide the lamb" (22:8) → John 1:29; singular seed (22:17, אֹיְבָיו 3ms — verified) → Gal 3:16. **One correction to carry to the pulpit** `[S: audit]`: the LXX renders *yāḥîd* at 22:2, 12, 16 as **ἀγαπητός**, not μονογενής — *monogenēs* for Isaac comes from Heb 11:17, not from the Greek Genesis. The grammar of substitution is built incrementally and detonated in the NT. **[T/S: NT]**""")

rep('cross 5',
"""**5. Presence is the book's second originated programme, running to Immanuel. [strong→high]** "The LORD was with X" (26:24; 28:15, §11; 39:2,21, §14; 46:4, §16) → Exod 3:12 → Matt 1:23;""",
"""**5. Presence is the book's second originated programme, running to Immanuel. [strong→high]** "The LORD was with X" — **sixteen places, not five** `[S: audit]`: 21:20, 21:22, 26:3, 26:24, 26:28, 28:15, 28:20, 31:3, 31:5, 35:3, 39:2, 39:3, 39:21, 39:23, 46:4, 48:21 → Exod 3:12 → Matt 1:23;""")

rep('cross 6',
"""**6. The patriarchal narrative is the conscious answer to 1–11. [strong]** The call reverses Babel (12:2 name *given* vs 11:4 name *grasped*; 12:3 "all families" = the scattered 70, §6→§7); the §16 bookends (*bĕrēʾšît/ʾaḥărît*; 1:28/47:27; 70/70; 3:5,11:4/50:19; *tēbâ/ʾārôn*) close the bracket. Genesis is one cumulative case, not sixteen lessons. **[T]**""",
"""**6. The patriarchal narrative is the conscious answer to 1–11. [strong]** The call reverses Babel (12:2 name *given* vs 11:4 name *grasped*; 12:3 "all families", §6→§7); the §16 bookends close the bracket — *bĕrēʾšît/ʾaḥărît*; *tēbâ/ʾārôn* (both verified as exclusive); the *taḥat* triad landing at 50:19; and, with the warrant now stated honestly `[S: audit]`, the two-root 1:28/47:27 echo, the mixed-warrant seventy/seventy, and the conceptual 3:5/50:19 resolution. **And the strongest measurement of all sits underneath the whole argument:** *bārak* 6× in chs. 1–11 against 67× in 12–50; *ʾārar* 5× against 4×. The book's dominant word inverts at the hinge. Genesis is one cumulative case, not sixteen lessons. **[T]** *verified*""")

rep('cross 8',
"""**8. Measure-for-measure justice is built into the structure. [strong]** The deceiver is repaid in his own coin: Jacob's theft (27, §11) → Laban's elder-for-younger (29:25, §12); Judah's *haker-nāʾ* (37→38, §13); the goat-kid motif (27→37→38); the brothers' selling (37) → their testing (42–44, §15). **[T]**""",
"""**8. Measure-for-measure justice is built into the structure. [strong]** The deceiver is repaid in his own coin: Jacob's theft (27, §11) → Laban's elder-for-younger (29:25, §12); Judah's *hakker-nāʾ* (37:32→38:25, §13, identical form); the goat motif on *ʿizzîm* (27:9, 16 → 37:31 → 38:17, 20, §13) `[S: audit]`; the brothers' selling (37) → their testing (42–44, §15). **Add the recognition chain the July run half-saw:** *nākar* (5234) occurs in exactly eight verses in Genesis — 27:23 (Isaac fails to recognise Jacob), 31:32, 37:32–33, 38:25–26, 42:7–8 (Joseph recognises; they do not) — four scenes of recognition and its failure, all of them judgement scenes. **[T]** *verified*""")

# ------------------------------------------------------- 14. open questions
rep('open q 12:3',
"""- **12:3 wĕnivrĕkû stem (§7):** niphal passive ("be blessed," so Paul, Gal 3:8) vs hithpael reflexive ("bless themselves"). Paul's use is high-confidence; the Hebrew stem is *moderate* — worth a lexicon/commentary check if load-bearing.
""",
"""- ~~**12:3 wĕnivrĕkû stem (§7)**~~ — **closed at the September audit.** The morphology settles it and the answer is two stems, not one: niphal at 12:3, 18:18, 28:14; hithpael at 22:18, 26:4. What remains open is what the alternation *means*.
""")

rep('open q el-names',
"""- **El-name triptych (§8) and several diction-welds** were reached partly via the overview/prior-audit (`[S]`); they are text-confirmable and I have re-checked the Hebrew where load-bearing, but a solo run on each HIGH unit should verify independently before the pulpit.""",
"""- **El-name triptych (§8):** all three names verified on the page (14:18–20; 16:13; 17:1) — but they are a **selection, not the set** `[S: audit]`. Genesis also has *El Olam* (21:33), *El Elohe-Israel* (33:20) and *El Bethel* (35:7). Present the triptych as a cluster within one unit, not as Genesis's complete El-naming.
- **Every diction-weld in this document has now been checked by lemma** (`dig-deeper-genesis-claim-audit.md`). What remains unaudited is the sweep's *interpretive* work — the structural readings, the Christological trajectories, the Schnittjer findings. A clean count is not a warrant for a reading, and a solo run on each ⭐ HIGH unit should still be made before the pulpit.""")

# ------------------------------------------------- 15. book-overview tensions
rep('tensions',
"""The overview is unusually thorough and already incorporates prior dig-deeper runs, so this sweep *confirms* far more than it contests. Points of note rather than disagreement:

- **No substantive contradictions surfaced.** The overview's spine (seed survives → a king is coming; the diction-welds; the Judah arc; the presence programme; election by grace) is text-confirmable and this sweep endorses it.
- **Method caution (not a tension):** because the overview embeds prior audit findings, several of this sweep's `[S→T]` items (welds, El-names, the "did not spare"/Rom 8:32 link) risk *looking* independently derived when they were partly overview-primed. I have re-worked the Hebrew for the load-bearing ones, but the warrant counts below flag the residual `[S]` honestly. A genuinely independent solo run on each ⭐ HIGH unit is the right check before preaching.
- **One refinement carried forward, not originated here:** the "clearest pre-sacrificial type" superlative for Judah's substitution (44:33) is best held as *one of several* competing types (ram 22:13; Moses Exod 32:32; Passover lamb; scapegoat Lev 16) — the overview already reflects this refinement (§15 audit); the sweep concurs.""",
"""*Rewritten at the September revision. The overview this section originally addressed — the imported `Genesis_Book_Overview.md` — has been superseded by `book-overview-genesis.md` v1.0.0, a text-first build. The tensions below are against the new document.*

- **Agreement on the load-bearing structural fact.** The September overview's central intertextual finding — that Genesis quotes nothing and alludes to nothing, so Move 2 is empty and Move 4 carries the whole load — is exactly what this sweep found unit by unit without having framed it that way. Independently reached, so the agreement is earned.
- **Agreement, independently, on the substitution and recognition threads**, on the *tēbâ*/*ʾārôn* bracket, and on *lek-lekā* as the Abraham cycle's inclusio.
- **The sweep extends the overview at two points, and both should be folded in.** (i) The *taḥat* triad now includes **50:19**, which converges the substitution grammar and the god-complex thread in one word at the book's close — the overview's echo table does not carry it. (ii) The **22:17 → 24:60** clause, near-identical but for its final noun (*ʾōyēv* → *śōnēʾ*), found by the Genesis 24 dig and absent from the overview.
- **The overview corrects the sweep at four points**, all applied above: the 1:28/47:27 overstatement, the seventy/seventy warrant, the 3:5/50:19 classification, and the presenting situation, which the July run stated as a wilderness-Israel datum where it is a reconstruction.
- **One refinement carried forward, not originated here:** the "clearest pre-sacrificial type" superlative for Judah's substitution (44:33) is best held as *one of several* competing types (ram 22:13; Moses Exod 32:32; Passover lamb; scapegoat Lev 16). The sweep concurs.""")

# ------------------------------------------------------ 16. declaration
rep('declaration',
"""**Secondary sources present in context:** `Genesis_Book_Overview.md` (which itself embeds a prior claim-audit and macro-synthesis). No separate commentary, transcript, or standalone prior report was in context.
**Tools worked before secondary sources consulted:** Confirmed for the core diction/structure findings — the Hebrew welds, wordplay, and structural brackets were derived from the text; the overview was then used to confirm and to supply the audit-level refinements (El-name triptych, the two-criminals downgrade, the substitution-superlative refinement), tagged `[S]`/`[S→T]` accordingly.
**Passage text:** Wording-dependent findings (welds, puns, *taḥat/ʿārēv/haker-nāʾ/pāqōd*, Jabbok pun, 1:28↔47:27) checked against the Hebrew as recalled; high-frequency items are *high* confidence, and any load-bearing lexical claim carries a flag. A solo run should re-verify from a printed text before the pulpit.""",
"""**Secondary sources present in context (July run):** `Genesis_Book_Overview.md` (imported, now superseded). **At the September revision:** `book-overview-genesis.md` v1.0.0 and `dig-deeper-genesis-claim-audit.md` v1.0.0.
**Tools worked before secondary sources consulted:** Confirmed for the core diction/structure findings — the Hebrew welds, wordplay, and structural brackets were derived from the text; the overview was then used to confirm and to supply audit-level refinements, tagged `[S]`/`[S→T]` accordingly.
**Passage text — the July position, stated as it stood:** wording-dependent findings were *"checked against the Hebrew as recalled"*. There was no corpus to check them against; `_texts/` was built seven weeks later.
**Passage text — the September position:** every chain and count claim in this document has now been searched by lemma against `_texts/hebrew-wlc/_index/`, with each claimed reference confirmed to contain the word. Fourteen claims confirmed outright, seven with a nuance, four reframed, two withdrawn, one open question closed. Full verdicts and reasoning: `dig-deeper-genesis-claim-audit.md`. **Every failure was a number or a superlative; no claim about meaning failed.**""")

rep('declaration warrants',
"""**Warrant counts (approximate, across the sweep):** [T] dominant (~70%) · [I] ~15% · [S]/[S→T] ~15% (concentrated in audit-level refinements and the El-name/two-criminals items).
**Health note:** This is a genuine sweep, not a reformatting of the overview: the load-bearing findings are text-derivable Hebrew diction and structure, and where a finding came from the overview it is tagged `[S]`. But the overview's richness is a live risk — the honest `[S]` share (~15%) marks where independence is thinnest. **For any ⭐ HIGH unit (§1, §3, §7, §8, §9, §11, §12, §13, §15, §16), run a full solo dig-deeper from a printed text before preaching.** Sweep depth is planning-grade.""",
"""**Chains verified:** every chain claim in this document, by lemma, against the WLC index; counts name their edition throughout.
**Warrant counts (approximate, across the sweep):** [T] dominant (~70%) · [I] ~15% · [S]/[S→T] ~15%, now including the `[S: audit]` corrections.
**Health note:** This is a genuine sweep, not a reformatting of an overview: the load-bearing findings are text-derivable Hebrew diction and structure. What the September audit changed is not the sweep's judgement but its arithmetic — and that is the standing lesson, recorded here for the next sweep: **the numbers are where it was wrong, and the numbers are the cheapest thing to check.** What remains unverified is the interpretive layer, which no lemma index can test. **For any ⭐ HIGH unit (§1, §3, §7, §8, §9, §11, §12, §13, §15, §16), run a full solo dig-deeper before preaching.** Sweep depth is planning-grade.""")

# ----------------------------------------------------------------- finish
if fails:
    print('FAILED ANCHORS:')
    for f in fails:
        print('  -', f)
    sys.exit(1)

open(P, 'w', encoding='utf-8').write(s)
print(f'applied {len(edits)} edits:')
for e in edits:
    print('  ✓', e)
