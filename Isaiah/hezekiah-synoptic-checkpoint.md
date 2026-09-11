# Synoptic run checkpoint — Isa 36:1–39:8 // 2 Kgs 18:13–20:21

**Date:** 11 September 2026 · **Mode:** Synoptic (Phase 0.5d, adopted on trial) · **Direction of dependence: OPEN — declare, do not settle**
**Status:** mechanical diff complete and verified; two headline-grade findings in hand. Tools not yet worked. **A fresh session can resume from here.**

## Corpus note — one gap, stated before proceeding

**There is no `NASB95 Isaiah.txt` in `logos-exports/`.** Present for Isaiah: BHS, LXX, ESV. Present for Kings: BHS, LXX, NASB95, ESV. The declared study text is NASB95, so the Isaiah side has no study-text export.

**Handling:** the substrate is the Hebrew (WLC, verified), which is unaffected. For the English parallel display, **ESV is used on both sides** — both exports verified — so that the two columns are the same version and the comparison is not an artefact of mixed translations. NASB95 is quoted on the Kings side where a finding turns on it. *Not a silent fallback: if the NASB95 Isaiah export is added, the English column can be rebuilt cheaply.*

## The mechanical diff (WLC; reproducible)

Script: `_texts/tools/synoptic_diff2.py` (committed). Two passes — consonantal (NFD-strip combining marks; maqqef ־, paseq ׀, sof pasuq ׃ normalised to spaces) and skeletal (additionally deleting waw, yod and word-final he, so plene/defective spelling collapses to identity).

**Alignment corrections the diff forced** (a naive sequential alignment breaks; both are findings):

- **Isa 37:15–16 = 2 Kgs 19:15.** Isaiah splits into two verses what Kings carries as one; the offset runs to the end of the chapter, so Isa 37:38 = 2 Kgs 19:37.
- **2 Kgs 20:7–8 = Isa 38:21–22 — transposed.** The fig-cake cure and Hezekiah's request for a sign stand *mid-episode* in Kings and *at the very end*, after the psalm, in Isaiah.

| Category | Units | Share |
|---|---:|---:|
| Identical to the consonant | 8 | 10% |
| Orthographic difference only (plene/defective) | 13 | 17% |
| Minor — 1–2 words differing | 33 | 43% |
| Moderate — 3–6 words | 15 | 19% |
| **Major — 7+ words** | **8** | **10%** |
| **Total aligned units** | **77** | |

Words in aligned material: **Isaiah 1,246 · Kings 1,347** — Kings longer by 101 (≈8%).

**Identical to the consonant:** Isa 36:9=2 Kgs 18:24 · 37:1=19:1 · 37:3=19:3 · 37:5=19:5 · 37:8=19:8 · 37:22=19:21 · 37:31=19:30 · 37:37=19:36.

**The eight major divergences:** Isa 36:2 · 36:17 · 36:18 · **38:5 · 38:6 · 38:7 · 38:8 · 38:22**.

> **Six of the eight fall in Isaiah 38 // 2 Kings 20.** The Rabshakeh material runs near-verbatim; the illness episode is where the two texts genuinely part company. Patrick's original instinct — to dig Isa 38 // 2 Kgs 20:1–11 — was pointing at the right chapter.

**Material unique to one side:**

- **Isaiah only:** 38:9–20 — Hezekiah's psalm, 12 verses, absent from Kings entirely.
- **Kings only:** 18:14–16 — the tribute, Hezekiah stripping the temple and palace doors for Sennacherib; and 20:20–21 — the conduit, the source-citation formula and the death notice.

## Headline-grade finding 1 — the two divine titles pull in opposite directions

**יְהוָה צְבָאוֹת in Isaiah's version, plain יְהוָה in Kings', three times out of three:** Isa 37:16 / 2 Kgs 19:15; Isa 37:32 / 2 Kgs 19:31; Isa 39:5 / 2 Kgs 20:16. Never the reverse. Book-wide (WLC): **צבאות in 60 verses of Isaiah, in 5 verses of the whole of 1–2 Kings.** The divergence runs exactly along each book's own idiom. `[T]`

**But קְדוֹשׁ יִשְׂרָאֵל, "the Holy One of Israel", stands in *both* at Isa 37:23 = 2 Kgs 19:22** — and book-wide it occurs in **24 verses of Isaiah and in exactly one verse of the whole of 1–2 Kings: that one.** Kings' sole use of the most distinctively Isaianic title in the canon sits inside the shared block. `[T]`

**The two data cut opposite ways** — the first looks like Isaiah's idiom in the shared text, the second like Isaiah's idiom inside Kings — **and neither settles the direction.** This is the "open" case behaving exactly as Amendment G says it should.

## Still to do

Phase 0.55 canonical position (both books); Phase 0.6 twice (once per book); the sixteen tools; extensions; checking stage; the LXX pass (Rahlfs Isaiah + Rahlfs Kings both now in `logos-exports/`, and 1QIsa-a is a live question this run cannot answer from the corpus); Book-Overview Tensions against *both* overviews, with the maturity gap between them reported as required by Amendment G point 6.

**Filing (Patrick's decision, 10 Sep 2026, overriding the skill's "file above both" rule, which assumes a shared parent — Isaiah and Kings have none):** real file in `Isaiah/`, one-line pointer page in `Kings/`.
