# Old Testament Chain Audit

**Mode:** Claim Audit — mechanical verification of verbal-chain claims against the primary text
**Date:** 2 September 2026
**Scope:** all 124 Old Testament markdown documents in the Dig Deeper folder
**Substrate:** `_texts/hebrew-wlc/` (Westminster Leningrad Codex with lemma index), built 2 September 2026
**Method:** every Hebrew-script word paired with the verse references standing in its own clause or table cell was checked, by lemma, at each reference claimed for it.

---

## Headline findings

**1. Four confirmed errors, and every one of them is in the same document** — `dig-deeper-jeremiah-sweep.md`. No other Old Testament document produced a confirmed error.

**2. All four are the same failure.** Each is a word attributed to a verse that does not contain it. That is the failure mode the Jonah claim audit named — *"a verbal chain extended by inference into a verse that does not contain the word"* — previously found three times, in Exodus and Jonah, both times by hand. It is now found four more times, mechanically, in a book nobody had audited.

**3. One of the four inverts its own point.** The Jeremiah sweep says Moab's oracle applies שְׁאֵרִית to Moab. The word is not at the verse cited, and it is not in Jeremiah 48 at all. The nearest occurrences, 47:4 and 47:5, are about **Philistia**. The observation is not merely unsupported; the vocabulary it appeals to belongs to a different nation.

**4. Isaiah came out clean.** Isaiah carried more Hebrew-script claims than any other book — the sweep and overview together produced 241 of the 616 checks — and not one survived as an error. Given that the Isaiah work was built directly on supplied BHS and LXX exports, this is a result about method, not luck.

**5. A systematic trap was found that is nobody's error.** The reports use English versification; the Hebrew text uses Hebrew versification. Isaiah 64:8 is Hebrew 64:7; Jeremiah 9:24 is Hebrew 9:23; Exodus 22:16 is Hebrew 22:15. Any future automated check must map between the two or it will manufacture false failures. It has been noted in the corpus README.

---

## What was checked

| | |
|---|---|
| Documents in scope | 124 |
| Documents containing Hebrew-script claims | 17 |
| Claims extracted | 423 |
| Word-to-reference checks performed | 616 |
| Verified present | 555 (90%) |
| Failed the automated check | 50 |
| Word not resolvable to a lemma | 10 |
| Reference not in the Hebrew text | 1 |
| **Confirmed as real errors after hand-checking** | **4** |
| Real but nuanced | 1 |

Every one of the 61 non-passing checks was read in its own context before being reported. **The automated pass is a screen, not a verdict.** It narrowed 616 checks to 61 for human attention; 56 of those 61 turned out to be artefacts of the checker rather than faults in the reports. That ratio is the honest headline about the method: it finds real errors, and it must never be believed without reading.

---

## The four confirmed errors

### 1. Jeremiah 12:16 — "plant" (נטע) is not there

> **29:5's "build houses… plant gardens" repurposes two of the six commissioning verbs from 1:10… Previously "build" (בנה) and "plant" (נטע) have appeared only as divine first-person action (12:16; 18:9; 24:6).** `[T]`, high confidence

**Verified:** נטע occurs at 18:9 and 24:6. It does **not** occur at 12:16. בנה occurs at all three.

Jeremiah 12:16 reads *וְנִבְנוּ בְּתוֹךְ עַמִּי* — "they shall be built up in the midst of my people." One verb, not two, and it is a niphal — "they shall be built" — so the verse does not support "divine first-person action" either.

**This is the clearest instance in the folder of the named failure mode**, and it carries the strongest possible warrant: `[T]`, high confidence. The substantive claim survives — 29:5 does repurpose commissioning verbs — but its evidence base is two verses, not three.

**Fix:** drop 12:16 from the list, or restate as "(18:9; 24:6; and 12:16 for 'build' alone)". Re-examine the "first-person" characterisation.

### 2. Jeremiah 32:15 — בַּכֶּסֶף is not in the verse

> 32:15's שָׂדֹות בַּכֶּסֶף… בָּתִּים וְשָׂדֹות וּכְרָמִים ("houses and fields and vineyards shall again be bought") `[T]`/`[I]`

**Verified:** Jeremiah 32:15 reads *עוֹד יִקָּנוּ בָתִּים וְשָׂדוֹת וּכְרָמִים בָּאָרֶץ הַזֹּאת*. The three-term inventory is exactly right. **כֶּסֶף is not in the verse**; in Jeremiah 32 it stands at verses 9, 10, 25 and 44.

The argument — a three-term inventory planted for a later echo — is untouched. The quotation attached to it is not the verse's wording.

**Fix:** delete `שָׂדֹות בַּכֶּסֶף…` from the quotation. If the money language is wanted, cite 32:9 or 32:44.

### 3. Jeremiah 48:47 — שְׁאֵרִית is not there, and the point reverses

> Moab's oracle uses שְׁאֵרִית ("remnant") of Moab's own future in the same term applied to Judah's surviving community elsewhere in the book (48:47's echo of the "remnant" vocabulary tracked in §12) — worth noting that the term's application is not exclusive to Israel. `[T]`, moderate confidence

**Verified:** Jeremiah 48:47 reads *וְשַׁבְתִּי שְׁבוּת־מוֹאָב בְּאַחֲרִית הַיָּמִים* — "I will restore the fortunes of Moab in the latter days." **שְׁאֵרִית does not occur at 48:47, nor anywhere in Jeremiah 48.** The nearest occurrences in the oracles against the nations are 47:4 and 47:5, and both concern **the Philistines**.

Note what is probably behind the slip: 48:47 contains בְּאַחֲרִית ("in the latter [days]"), which shares its consonants with שְׁאֵרִית save the opening letter. The observation that remnant vocabulary is applied outside Israel is defensible — but from Jeremiah 47 and Philistia, not from 48:47 and Moab.

**Fix:** either restate the claim on 47:4–5 and Philistia, or withdraw it. As written it cannot stand.

### 4. Jeremiah 2:16 — the city is נֹף, not מֹף

> 2:16: "מֹף וְתַחְפַּנְחֵס" (Memphis and Tahpanhes)

**Verified:** Jeremiah 2:16 reads *גַּם־בְּנֵי־נֹף ותחפנס* — **נֹף** with nun. (מֹף with mem is the form at Hosea 9:6.) The second name is also the ketiv *ותחפנס*, not the fuller spelling given.

A one-letter transcription slip with nothing hanging on it, recorded for completeness rather than because it matters.

**Fix:** correct the quotation to נֹף.

---

## One real but nuanced case

### Jeremiah 2:13 — the cistern motif starts at 38:6, not 2:13

> **The cistern (בּוֹר) motif tracked since 2:13/38:6 (§11) recurs a third time at 41:7, 9** `[T]`

**Verified:** 38:6 and 41:7, 9 all contain בּוֹר (H953). Jeremiah 2:13 does **not**. It reads *בֹּארוֹת בֹּארֹת נִשְׁבָּרִים* — **בֹּאר** (H877), a different lexeme.

This is not a mistake of substance. Broken cisterns at 2:13 and the cistern at 38:6 are the same image, and the reading — misplaced trust, then affliction, then a mass grave — is a good one. But it is a **thematic** chain, not a **verbal** one, and it is presented as verbal and tagged `[T]`.

**Fix:** say so. "The cistern image (בֹּאר at 2:13; בּוֹר from 38:6)" costs four words and makes the claim true.

---

## What the failures were *not*

Fifty-six of the sixty-one non-passing checks were faults in the checker. Recording the classes matters, because it says what a future run of this audit must handle:

| Class | Count | What it is |
|---|---|---|
| Cross-pairing within a clause | ~35 | A clause holds two words and two references — "57:5's הַנֵּחָמִים and 57:6's אֶנָּחֵם" — and the checker paired each word with both references. The reports were right; the pairing was wrong. |
| Root citation vs inflected form | ~10 | The reports cite roots (√נצל, √אכל, √שׂבע). A root is often not itself an attested surface form, so the lemma lookup finds nothing. A root-aware matcher is needed. |
| English vs Hebrew versification | 5 | Isaiah 64:8 = Hebrew 64:7; Jeremiah 9:24 = Hebrew 9:23; Exodus 22:16 = Hebrew 22:15. |
| Book mis-resolution | 4 | "Leviticus 25:10 … אָשָׁם at 53:10" — the checker carried Leviticus forward into an Isaiah reference. |
| Negative claims read as positive | 2 | "צֶמַח … is **distinct from** the vine imagery of 2:21/11:16" is a claim that the word is *not* there. |

One of these deserves singling out. `point-purpose-proverbs-1-1to7.md` says *"1:7 reads רֵאשִׁית, 9:10 reads תְּחִלַּת"* and marks it "✅ Confirmed against BHS, 21 August". The checker crossed the pair and reported two failures. **The report was right and had already done this work properly.** That is worth knowing: where a document records that it checked, it had.

---

## Limitations — what this audit does *not* cover

**Transliterated claims are not checked.** This is the significant gap. Most Torah documents — the Exodus sweep and its fifteen solo digs above all — carry their lexical work in transliteration (*šākan*, *kābēd*, *ʿābad*) rather than Hebrew script, and no automated check reached them. **The three previously known errors, in Exodus and Jonah, are all in that untested population.** A second pass needs a reverse-transliteration layer; until it runs, the Torah documents are unaudited, not cleared.

**Root citations are not checked**, for the reason given above.

**Claims without explicit verse references are not checked** — "the root runs throughout chapters 5–8" cannot be tested mechanically. Those need a reader.

**Only verbal presence is tested.** That a word occurs where it is claimed says nothing about whether the chain means what the report says it means.

---

## What this means for revisiting the digs

The question that prompted this audit was whether the existing digs should be re-run. On the Hebrew-script evidence, the answer is **no, with one exception**.

- **`dig-deeper-jeremiah-sweep.md` needs a corrections pass.** Four errors, one of which reverses its own point. Nothing here requires re-running the sweep; all four are local fixes to specific claims.
- **Everything else in Hebrew script is clean.** Isaiah, Proverbs, Psalms, Ruth, Leviticus, Ezra-Nehemiah, Genesis, Exodus: no confirmed errors.
- **The Torah documents remain untested**, because their lexical work is transliterated. That is the next audit, not a re-run.

This also confirms, from a third book, the finding the Exodus overview recorded and the Jonah audit named: **errors cluster in synthetic, book-level, sweep-depth work.** All four errors are in a whole-book sweep. None is in a solo dig, an overview, or a point-purpose plan.

---

## Reproducing this

```
python3 _audit/extract_verify.py
```

Checkpoints, all in `_audit/`:

| File | Contents |
|---|---|
| `01-documents.tsv` | the 124 documents in scope |
| `02-claims.tsv` | 423 extracted claims with context |
| `03-verdicts.tsv` | 616 word-to-reference checks with verdicts |

Individual claims can be re-checked directly:

```
python3 _texts/tools/find.py verify 5193 Jer:12:16 Jer:18:9 Jer:24:6
```

---

*Prepared with the Dig Deeper toolkit in Claim Audit Mode, 2 September 2026. Every claim reported as an error was read in its own context and verified against the Westminster Leningrad Codex before being listed. Confirmation by the originating run was not accepted as evidence.*
