# Claim Audit: John — Lincoln, "The Divine Courtroom and the Gospel of John"

**Source audited:** Andrew T. Lincoln, "A Life of Jesus as Testimony: The Divine Courtroom and the Gospel of John," ch. 9 in *The Divine Courtroom in Comparative Perspective* (BIS 132; Leiden: Brill, 2015), 145–166. Local study copy at `John/_sources/`.
**Passages engaged:** book-wide, with concentrations at 1:6–18; 5:19–47; 8:12–59; 9:1–41; 12:31–50; 13:31–16:33; 18:28–19:37; 20:31.
**Date:** 23 August 2026
**Version:** 1.1 — Claim 3 upgraded to "verified on both sides" and Claim 6's Volume raised, following a Logos check of the Rahlfs LXX at Isaiah 43:10. Changes tagged `[revised: logos-research]`.
**Mode:** Claim Audit (dig-deeper Phase 0.5b)
**Purpose:** Test Lincoln's claims before incorporating them into `book-overview-john` v0.2.0 — which reached a forensic reading of John independently, from the counts, and now has a scholarly interlocutor who has written the monograph on it.

**Standing caution.** Lincoln is the author of *Truth on Trial: The Lawsuit Motif in the Gospel of John* (Baker, 2000), which this chapter revisits (his n. 1). On this subject the prior sits with him, and a "Discard" verdict here would need to be a genuine textual finding, not a preference. In the event none of the ten claims is discarded.

---

## Verification basis

All Greek counts below were taken by scripted sweep over the **SBLGNT** texts of Matthew, Mark, Luke and John. Where a count in this audit differs from one in `dig-deeper-john-sweep` v1.1, **this audit supersedes the sweep** — see Confidence Change Propagation.

**A methodological note that matters for reading the verdicts.** My first pass appeared to contradict Lincoln on four of his seven vocabulary statistics. Every one of those apparent contradictions was an artefact of my own regexes, not an error of his:

- **μαρτυρέω** — I initially counted 28 in John against his 33. The gap was the reduplicated perfect (μεμαρτύρηκεν, μεμαρτύρηκα, μεμαρτύρηκας, μεμαρτύρηκε — 5 tokens), which a `(ε)?μαρτυρ` pattern misses. With them: **33**.
- **Synoptic μαρτυρέω** — I counted 7 against his 2. Five of my seven were **μαρτύρων**, the genitive plural of the *noun* μάρτυς (Matt 18:16; 26:65; Mark 14:63), not the participle. Disambiguating by context: **2**.
- **ἀληθής** — I counted 28 against his 14, having let an `εια` alternative catch ἀλήθεια. Corrected: **14**.
- **κρίνω** — I counted 21 against his 19, having caught κρίθινος ("barley," 6:9, 13) and κρίμα. Corrected: **19**.

The lesson is worth recording: **lemma-level claims cannot be audited with surface-form regexes**, and where this audit and a tagged lexical database disagree, the database should be preferred unless the disagreement can be explained form by form.

---

## Claims Audited

### Claim 1: The forensic-vocabulary statistics

**Source:** Lincoln §1, "The frequency of forensic language in GJ is another indicator of its distinctiveness."
**Claim:** μαρτυρία 14× in John / 4× in the Synoptics; μαρτυρέω 33× / 2×; κρίνω 19× / Matt 6, Luke 6; κρίσις 11× / Luke 4, Matt 12; ἀλήθεια 25× / 7×; ἀληθής 14× / Mark 1, Matt 1; ἀληθινός 9× / Luke 1.

**Hays criteria:** *N/A — this is a countable factual claim, not an allusion claim.* Verified directly instead:

| Word | Lincoln (John) | Verified (John) | Lincoln (Syn) | Verified (Syn) | |
|------|---------------|-----------------|---------------|----------------|---|
| μαρτυρία | 14 | **14** | 4 | **4** (Mk 3, Lk 1) | ✓ |
| μαρτυρέω | 33 | **33** | 2 | **2** (Mt 1, Lk 1) | ✓ |
| κρίνω | 19 | **19** | Mt 6 / Lk 6 | **Mt 6–7 / Lk 6–7** | ✓ |
| κρίσις | 11 | **11** | Lk 4 / Mt 12 | **Lk 4 / Mt 12** | ✓ |
| ἀλήθεια | 25 | **25** | 7 | **7** (Mt 1, Mk 3, Lk 3) | ✓ |
| ἀληθής | 14 | **14** | Mk 1 / Mt 1 | **Mk 1 / Mt 2** | ✓ |
| ἀληθινός | 9 | **9** | Lk 1 | **Lk 1** | ✓ |
| παράκλητος | 4 | **4** | 0 | **0** | ✓ |

**Verdict: Confirmed.** Every figure is exact or within one on the Synoptic side, where the residual ±1 sits on my form-classification, not his.

**Reasoning:** Eight statistics, eight matches. This is unusually clean and it earns Lincoln a high prior on the rest of the chapter's data.

**Book-overview action required:** **Yes, and it is a correction to us, not to him.** The sweep's Cross-Passage table gave ἀληθ- as 55 (right in total) but the solo-dig and sweep both understated the sub-counts. Add the verified breakdown: **ἀλήθεια 25 · ἀληθής 14 · ἀληθινός 9 · ἀληθῶς 7 = 55**. Likewise μαρτυρ-: **μαρτυρία 14 · μαρτυρέω 33 = 47**, which is what the sweep's total already said.

---

### Claim 2: Deutero-Isaiah's courtroom scenes are the major literary catalyst for John's lawsuit motif

**Source:** Lincoln §2. "It is indeed the Jewish Scriptures in Greek translation, particularly Deutero-Isaiah, that provide the major literary catalyst for the evangelist's use of the lawsuit motif."
**Claim:** The *rîb*-pattern as developed in Isa 40–55 — not Graeco-Roman legal rhetoric or tragedy — is the primary source of John's forensic framework.

**Hays criteria:**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Availability | **Strong** | Demonstrated, not assumed: John quotes Isa 40–55 three times — LXX 40:3 → 1:23; 53:1 → 12:38; 54:13 → 6:45. All three verified in the SBLGNT |
| Volume | **Possible** | High at the level of *pattern* (summoned witnesses, contested truth, judge-and-prosecutor, ἐγώ εἰμι); **low at the level of quotation** — see Reasoning |
| Recurrence | **Strong** | Isaiah is John's most-worked prophet: four engagements (1:23; 6:45; 12:38; 12:40), and 12:41 makes Isaiah's vision christological |
| Thematic Coherence | **Strong** | The motif is not decorative; it organises chs. 5–12 and the passion, on our own independent reading |
| Historical Plausibility | **Strong** | A Greek-reading Jewish author of the first century |
| History of Interpretation | **Possible** | Widely held (Lincoln, Trites, Asiedu-Peprah); but **Parsenios argues a Graeco-Roman derivation and Lincoln engages him directly**, so this is a live scholarly dispute, not a consensus |
| Satisfaction | **Strong** | It explains the *shape* of John's controversies, which the Synoptic pronouncement-story form does not |

**Verdict: Confirmed with nuance.**

**Reasoning:** The claim that John read Deutero-Isaiah is demonstrated. The claim that Deutero-Isaiah's *courtroom scenes* fuelled the lawsuit motif is an inference, and the audit should say where the load sits. **None of the three verses John actually quotes from Isa 40–55 is from a trial speech.** 40:3 is the herald; 53:1 is the Servant Song's opening lament; 54:13 is new-covenant teaching. Lincoln's argument runs: John demonstrably read this part of Isaiah → the *rîb*-pattern is dominant in this part → therefore it fuelled him. That is reasonable and probably right, but it is a *proximity* argument, not a citation argument, and the audit should not let it pass as the latter. His stronger evidence is the pattern-level and ἐγώ εἰμι material in Claims 3 and 6, not the citation list.

**Book-overview action required:** Add Deutero-Isaiah's courtroom scenes to the intertextual map as a **named source of the forensic form**, replacing the generic "prophetic *rîb*" row currently tagged `[S: conv]`. Upgrade its warrant from `[S: conv]` to `[S: Lincoln]` and its confidence to **moderate–high**. Record Parsenios as the live alternative.

---

### Claim 3: John's ἐγώ εἰμι takes up LXX Isaiah 43:10

**Source:** Lincoln §3. "Now the language found in lxx 43:10 is taken up as Jesus in his witness calls for his audience to believe (πιστεύσητε—8:24) and know (γνώσεσθε—8:28) that I am (ὅτι ἐγώ εἰμι)."
**Claim:** LXX Isa 43:10's ἵνα γνῶτε καὶ πιστεύσητε καὶ συνῆτε ὅτι ἐγώ εἰμι supplies both the formula and the believe/know pairing at John 8:24, 28.

**Hays criteria:**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Availability | **Strong** | As Claim 2 |
| Volume | **Strong** | **Both sides now verified.** LXX Isa 43:10 (Rahlfs): *ἵνα **γνῶτε** καὶ **πιστεύσητε** καὶ συνῆτε **ὅτι ἐγώ εἰμι***. John: 8:24 **πιστεύσητε … ὅτι ἐγώ εἰμι**; 8:28 **γνώσεσθε … ὅτι ἐγώ εἰμι**; 13:19 **ἵνα πιστεύσητε … ὅτι ἐγώ εἰμι**. **πιστεύσητε is an exact form-match** — aorist subjunctive second plural in both |
| Recurrence | **Strong** | Nine absolute ἐγώ εἰμι in John (4:26; 6:20; 8:24, 28, 58; 13:19; 18:5, 6, 8) — verified |
| Thematic Coherence | **Strong** | Both texts are courtroom scenes in which witnesses are summoned to establish a contested divine identity |
| Historical Plausibility | **Strong** | — |
| History of Interpretation | **Strong** | The Isa 43 background to Johannine ἐγώ εἰμι is very widely held; Exod 3:14 is the other standard candidate |
| Satisfaction | **Strong** | It explains why 8:24/8:28 pair *believing* and *knowing* — which Exod 3:14 alone does not |

**Verdict: Confirmed — verified on both sides.** *(Upgraded from "Confirmed, pending verification" after a Logos check of the Rahlfs LXX, 23 August 2026.)* `[revised: logos-research]`

**The LXX side, now verified verbatim.** Rahlfs, Isaiah 43:10:

> γένεσθέ μοι μάρτυρες, **κἀγὼ μάρτυς**, λέγει κύριος ὁ θεός, καὶ ὁ παῖς ὃν ἐξελεξάμην, **ἵνα γνῶτε καὶ πιστεύσητε καὶ συνῆτε ὅτι ἐγώ εἰμι**, ἔμπροσθέν μου οὐκ ἐγένετο ἄλλος θεὸς καὶ μετ' ἐμὲ οὐκ ἔσται.

Lincoln quotes this accurately, word for word. The Hebrew underlying it carries the same three-verb structure — תֵּדְעוּ (know) · וְתַאֲמִינוּ (believe) · וְתָבִינוּ (understand) · כִּי־אֲנִי הוּא ("that I am He") — so the pattern is not an artefact of the Greek translator.

**Reasoning:** Lincoln's strongest verbal claim, and it holds at the highest level of precision available. **πιστεύσητε is not merely the same lemma but the same inflected form** — aorist subjunctive second plural — in LXX Isa 43:10, John 8:24 and John 13:19. Three observations strengthen the claim beyond what he states:

1. **John 13:19 is the tightest verbal match of the three, and Lincoln does not say so.** LXX has *ἵνα … πιστεύσητε … ὅτι ἐγώ εἰμι*; 13:19 has *ἵνα πιστεύσητε … ὅτι ἐγώ εἰμι* — same conjunction, same verb-form, same ὅτι-clause. He cites 8:24 and 8:28 for the believe/know pairing and treats 13:19 separately under the predictive-word argument, missing that it is the closest parallel.
2. **8:18 puts ἐγώ εἰμι and the double witness in one verse** — *ἐγώ εἰμι ὁ μαρτυρῶν περὶ ἐμαυτοῦ καὶ μαρτυρεῖ περὶ ἐμοῦ ὁ πέμψας με πατήρ* — which is the Isa 43:10 structure entire: two witnesses, contested identity, ἐγώ εἰμι as the content.
3. **8:28 fuses the ἐγώ εἰμι claim with ὑψόω in a single sentence**, so Lincoln's two separate Isaianic claims (43:10 and 52:13) converge on one verse.

**A small citation correction.** Lincoln writes that "in both 43:10 and 43:13 the lxx has two witnesses, adding God's witness (κἀγω µάρτυς) alongside Israel's." The doubled witness is verified at **43:10** and at **43:12** (*ὑμεῖς ἐμοὶ μάρτυρες κἀγὼ μάρτυς, λέγει κύριος ὁ θεός*), not 43:13, which begins *ἔτι ἀπ' ἀρχῆς*. His 43:9 citation (*εἰπάτωσαν ἀληθῆ*) is verified as accurate.

**Book-overview action required:** Add LXX Isa 43:10 to the intertextual map as a named source for the absolute ἐγώ εἰμι, alongside Exod 3:14, at **high** confidence pending the LXX check. The overview currently lists "Exodus 3:14 / Isaiah 43:10–13" jointly; Lincoln's contribution is to specify *which verse* and *why the believe/know pairing follows*.

---

### Claim 4: ὑψόω carries Deutero-Isaiah's servant-vindication sense

**Source:** Lincoln §3. "GJ employs the 'lifting up' language of the servant's vindication with a new double meaning that combines suffering and glorious vindication," citing LXX Isa 52:13 (ὑψωθήσεται καὶ δοξασθήσεται).
**Claim:** The ὑψόω of 3:14; 8:28; 12:32–34 draws its exaltation-sense from Isa 52:13.

**Hays criteria:**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Availability | **Strong** | John quotes Isa 53:1 at 12:38 — the Servant Song is demonstrably in hand |
| Volume | **Possible** | ὑψόω is a common verb; the distinctive element is its *pairing with glorification*, which is where Isa 52:13 bites |
| Recurrence | **Strong** | ὑψόω 5× in 4 verses (3:14; 8:28; 12:32, 34×2) — verified; δοξάζω 22× |
| Thematic Coherence | **Strong** | John fuses crucifixion and exaltation, and glosses ὑψόω as crucifixion at 12:33 |
| Historical Plausibility | **Strong** | — |
| History of Interpretation | **Strong** | Standard in Johannine scholarship |
| Satisfaction | **Strong** | It explains the fusion, which Num 21 alone cannot |

**Verdict: Confirmed with nuance.**

**Reasoning:** A nuance Lincoln does not make and the audit should. **John himself supplies a different source for the verb**: 3:14 says *καθὼς Μωϋσῆς ὕψωσεν τὸν ὄφιν ἐν τῇ ἐρήμῳ* — the stated warrant is Numbers 21:9, not Isaiah. So the two sources are doing different work, and separating them sharpens both: **Numbers supplies the verb, the image and the looking-to-be-healed logic; Isaiah 52:13 supplies the fusion of lifting-up with glorification, which Numbers cannot.** That John does fuse them is verifiable — 12:23–33 and 13:31 put ὑψόω and δοξάζω in the same movement. Lincoln's claim survives and is strengthened by being narrowed.

**Book-overview action required:** Keep Numbers 21:8–9 as the stated source of ὑψόω. Add Isa 52:13 as the source of the *exaltation-sense*, **moderate–high**, with the distinction stated.

---

### Claim 5: John 5:37b echoes LXX Isaiah 48:8

**Source:** Lincoln §3, parenthetically: "echoes of YHWH's accusations against Israel—'you have never heard' (5:37b, cf. lxx Isa 48:8)."
**Claim:** 5:37's οὔτε φωνὴν αὐτοῦ πώποτε ἀκηκόατε echoes LXX Isa 48:8.

**Hays criteria:**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Availability | **Strong** | As above |
| Volume | **Weak** | "You have not heard" is not a distinctive phrase. The John side is verified; the LXX side is not |
| Recurrence | **Possible** | Isa 48 is not among John's four Isaiah engagements |
| Thematic Coherence | **Possible** | Both are divine accusations of non-perception, which fits |
| Historical Plausibility | **Strong** | — |
| History of Interpretation | **Weak** | Lincoln offers it in a parenthesis without argument, and I cannot confirm others make it |
| Satisfaction | **Possible** | It adds atmosphere rather than explanation; 5:37 is intelligible without it |

**Verdict: Uncertain — flag for research.**

**Reasoning:** The weakest of Lincoln's verbal claims, and he presents it as a passing "cf." rather than an argument, so the audit is not resisting anything he insists on. **πώποτε is the interesting datum and he does not use it**: it occurs 4× in John (1:18; 5:37; 6:35; 8:33 — verified), and 1:18 and 5:37 are the two theologically weighted uses, forming an internal pair ("no one has ever seen God" / "you have never heard his voice nor seen his form"). That internal echo is stronger and better attested than the proposed Isaianic one.

**Book-overview action required:** None. Do not add to the intertextual map. The 1:18 ↔ 5:37 internal echo is already in the solo dig on the Prologue.

---

### Claim 6: The collaborative witness of 8:18 reflects LXX Isaiah 43:10's two witnesses

**Source:** Lincoln §3. "the complete dependence of the Son as agent on the Father as authorizer enables their witness, like that of YHWH and the servant in lxx 43:10, to be depicted as a collaborative one."
**Claim:** LXX Isa 43:10's doubled witness (God's κἀγὼ μάρτυς alongside Israel's) stands behind John 8:18.

**Hays criteria:**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Availability | **Strong** | — |
| Volume | **Possible–Strong** | **Upgraded.** The LXX doubling is now verified: *κἀγὼ μάρτυς* at Isa 43:10 and again at 43:12. So the "two witnesses" feature Lincoln builds on is genuinely there in the Greek. The verbal overlap with John 8:18 is still the ἐγώ εἰμι rather than the witness-vocabulary `[revised: logos-research]` |
| Recurrence | **Strong** | The two-witness requirement recurs at 5:31–37 and 8:17 |
| Thematic Coherence | **Strong** | — |
| Historical Plausibility | **Strong** | — |
| History of Interpretation | **Possible** | The LXX's doubled witness at 43:10 is a real feature; its application to 8:18 is Lincoln's |
| Satisfaction | **Possible** | It illuminates, but a simpler explanation is available |

**Verdict: Needs reframing.**

**Reasoning:** **John names his own source one verse earlier.** 8:17 reads *καὶ ἐν τῷ νόμῳ δὲ τῷ ὑμετέρῳ γέγραπται ὅτι δύο ἀνθρώπων ἡ μαρτυρία ἀληθής ἐστιν* — the two-witness rule of Deut 19:15, cited explicitly as "your law." The doubling at 8:18 is therefore *stated* to satisfy Deuteronomy. Isa 43:10's LXX doubling may be a further resonance, but it cannot be the primary warrant when the text supplies one. Reframe as: **Deuteronomy 19:15 is the stated warrant; LXX Isa 43:10 is a possible additional resonance, given that 8:18 opens with ἐγώ εἰμι** — which is a real observation and belongs to Claim 3 rather than standing alone.

**Book-overview action required:** Keep Deut 19:15 → 8:17 at high confidence. Add the Isa 43:10 resonance as a note under the ἐγώ εἰμι row, not as a separate source.

---

### Claim 7: Testimony forms an inclusio framing the whole Gospel

**Source:** Lincoln §1. "Reference to the testimony of John twice interrupts the Gospel's prologue (1:6–8, 15) and in its epilogue the narrative as a whole is attributed to the true testimony of the Beloved Disciple (21:24; cf. also 19:35). In this way the notion of testimony provides an inclusio that frames the Gospel as a whole."
**Claim:** John is framed as written testimony in a legal process.

**Hays criteria:** *N/A — a structural claim about John, not an allusion.* Verified directly:

- μαρτυρ- in ch. 1: **7 occurrences**, all of the Baptist, at 1:7 (×2), 1:8, 1:15, 1:19, 1:32, 1:34 — verified.
- The two prologue insertions (1:6–8, 15) interrupt hymnic material — independently reached in the solo dig on 1:1–18.
- 19:35 (ὁ ἑωρακὼς μεμαρτύρηκεν) and 21:24 (οὗτός ἐστιν ὁ μαθητὴς ὁ μαρτυρῶν … καὶ οἴδαμεν ὅτι ἀληθὴς αὐτοῦ ἡ μαρτυρία ἐστίν) — verified.

**Verdict: Confirmed.**

**Reasoning:** Independently reached before Lincoln was opened — the sweep's Cross-Passage Finding 15 and the Prologue dig's Headline Finding 3 both identified the Baptist insertions as structural and the μαρτυρ- density as the book's epistemology. **This is an earned confirmation and it is the audit's most valuable result**, because our text-first reading and the field's leading monograph on the motif converged without contact.

**Book-overview action required:** None to the substance. Add Lincoln as the citable authority for the inclusio, so the overview's claim is no longer resting on our own reading alone.

---

### Claim 8: The setting is local expulsion, not a general Jamnia ban

**Source:** Lincoln §4. "It is also far more likely that there were a range of synagogue responses … and that the experience reflected was in one particular location rather than the result of a general ban formulated at Jamnia and linked to the twelfth of the Eighteen Benedictions."
**Claim:** The three ἀποσυνάγωγος references reflect a real, local, traumatic experience — but not the *Birkat ha-Minim* reconstruction.

**Hays criteria:** *N/A — a historical-setting claim.*

**Verdict: Confirmed.**

**Reasoning:** The textual base is verified: ἀποσυνάγωγος occurs exactly 3× (9:22; 12:42; 16:2), and the sequence is narrator → narrator → Jesus. Lincoln affirms the pressure as real and resists the Jamnia reconstruction — **which is precisely the position `book-overview-john` took independently**, marking the pressure `[T]` and the *Birkat ha-Minim* setting `[S]` and disputed. He goes further than we did in offering a positive reconstruction (local, traumatic, involving interrogation, with excommunication as a substitute for the death penalty), and flags that the external evidence is disputed.

**Book-overview action required:** Add Lincoln as support for the caution already in the presenting situation. Optionally record his positive reconstruction as `[S: Lincoln]`, clearly marked as a reconstruction rather than a datum.

---

### Claim 9: πέμπω 25× and ἀποστέλλω 17×, used interchangeably

**Source:** Lincoln §3. "the verbs πέµπειν (25x) and ἀποστέλλειν (17x) are used interchangeably."

**Verdict: Needs reframing.**

**Reasoning:** The **lemma totals in John are πέμπω 32 and ἀποστέλλω 28** (verified; ἀπόστολος at 13:16 excluded). Lincoln's figures are lower and do not match either total. His sentence says "in such contexts," i.e. contexts of divine agency, so the figures are almost certainly *context-restricted* counts rather than lemma totals — and as proxies, the participial "the one who sent me" forms of πέμπω number **27**, and the finite/perfect "sent" forms of ἀποστέλλω number **21**, which is the right order of magnitude. **The claim is not wrong, but the figures are easily misread as lemma totals and should not be quoted as such.** The substantive point — that the two verbs are used interchangeably for the sending — is sound and independently visible: the sweep found 23 verses carrying the sending formula across both verbs.

**Book-overview action required:** If quoting counts, use the verified lemma totals (32 / 28) and state that Lincoln's 25 / 17 are agency-context figures.

---

### Claim 10: The Paraclete is a forensic advocate, designated four times

**Source:** Lincoln §3. "On four occasions this Spirit is designated in a way distinctive to GJ, as ὁ παράκλητος (14:16, 17, 26; 15:26; 16:7–15), and on three of these is further designated as 'the Spirit of truth' (14:17; 15:26; 16:13)."

**Verdict: Confirmed with nuance.**

**Reasoning:** **παράκλητος occurs exactly 4× — 14:16, 14:26, 15:26, 16:7** (verified), so "four occasions" is right. The parenthetical reference list includes **14:17, where the word is not παράκλητος but "the Spirit of truth"** — a slip in the citation list, not in the claim. "Spirit of truth" at 14:17; 15:26; 16:13 is verified as three. The forensic sense of παράκλητος (advocate, one called alongside in a legal proceeding) is standard and coheres with John's giving the Spirit the prosecutorial verb ἐλέγχω at 16:8 — which the sweep found independently.

**Book-overview action required:** None. Cite 14:16, 26; 15:26; 16:7 rather than Lincoln's list.

---

## Summary

| Verdict | Count | Claims |
|---------|-------|--------|
| Confirmed | **4** | 1, 3, 7, 8 |
| Confirmed with nuance | **3** | 2, 4, 10 |
| Needs reframing | **2** | 6, 9 |
| Uncertain — flag for research | **1** | 5 |
| Discard | **0** | — |

**Reading of the result.** Nothing is discarded, and the two reframings both take the same form: **Lincoln reaches for an Isaianic source at a point where John has named a different source one or two verses earlier** (Deut 19:15 at 8:17; Num 21:9 at 3:14). That is not an error so much as a monograph's centre of gravity showing — a book about the lawsuit motif will see Isaiah first. The corrective in both cases is to let John's stated source stand as primary and place the Isaianic resonance as secondary, which in Claim 4 makes his point sharper rather than weaker.

---

## Confidence Change Propagation

| Item | Previous | New | Sections to update |
|------|----------|-----|--------------------|
| Prophetic *rîb* as source of the forensic form | `[S: conv]`, moderate | **`[S: Lincoln]`, moderate–high**, named as Deutero-Isaiah's courtroom scenes | overview Intertextual Map (*rîb* row); overview §"What changed"; sweep Cross-Passage Finding 15 |
| LXX Isa 43:10 → absolute ἐγώ εἰμι | listed jointly with Exod 3:14, high | **high — verified on both sides**, with 43:10 specified, the believe/know pairing explained, and πιστεύσητε an exact form-match at 8:24 and 13:19 | overview Intertextual Map (ἐγώ εἰμι row); sweep P17, P18, P29 |
| Isa 52:13 → the exaltation-sense of ὑψόω | absent | **moderate–high, added**, with Num 21:9 retained as the stated source | overview Intertextual Map (Num 21 row); sweep P6, P26 |
| ἀληθής / ἀληθινός sub-counts | ἀληθής/ἀληθινός given as 8 combined | **ἀλήθεια 25 · ἀληθής 14 · ἀληθινός 9 · ἀληθῶς 7** | sweep §"countable spine" table; solo dig 1:1–18 is unaffected |
| μαρτυρέω | sweep gave 26 for the verb | **33** (total μαρτυρ- 47 unchanged) | sweep §"countable spine"; sweep P11 |
| πέμπω / ἀποστέλλω | 32 / 29 | **32 / 28** (ἀπόστολος excluded) | sweep Whole-book orientation; overview Microscript note |
| Local expulsion, not Jamnia | `[S]`, disputed | **`[S]` confirmed by Lincoln**, unchanged in substance | overview Presenting Situation |

---

## What Lincoln adds that we did not have

1. **A named source for the forensic form.** Our reading had the frame but only a generic *rîb* label. Lincoln supplies Deutero-Isaiah's courtroom scenes specifically, with the Isa 41–45 trial speeches identified.
2. **The believe/know pairing at 8:24/8:28 explained.** We noted the absolute ἐγώ εἰμι and Isa 43; we had no account of why *believing* and *knowing* are paired. LXX Isa 43:10 supplies it.
3. **Two-stage structure of the cosmic trial** — through Jesus' life, then through the followers' and the Spirit's continuing witness (15:26–27). Our sweep had the Paraclete's forensic verb but not the two-stage frame.
4. **The reader-as-jury reading of 20:31**, via Kensky — that the reading process is itself a judging process.
5. **Glory as reputation/honour at stake in a forensic setting**, which explains 5:44 and 12:43 (the two verses our sweep identified as bracketing the public ministry) better than our own account did.

## What we have that Lincoln does not

Recorded so the overview does not quietly lose its own findings:

1. **The countable seam at 12:37** — 16 of 17 σημεῖον before it. Lincoln treats 5:1–12:50 as the extended trial but does not use the count.
2. **The 1:19 ↔ 10:40–42 forensic bracket**, with 13 of 17 σημεῖον inside it and the crowd's verdict on the first witness at 10:41.
3. **The verbal threads** — ταράσσω (12:27; 13:21 → 14:1, 27), ἑλκύω (6:44; 12:32 → 18:10 → 21:6, 11), τίθησιν (10:11 → 13:4), ἐκμάσσω, κράζω's reversal.
4. **πατήρ absent from chapters 9 and 19** — the two interrogation chapters.
5. **Psalm 69 as the spine-psalm**, its three uses tracking the psalm's own movement. Lincoln's Isaiah focus leaves the Psalter untouched.

---

## Open Questions arising

1. ~~**LXX Isaiah 43:10, 52:13 and 48:8 could not be verified.**~~ **43:10 now verified** against the Rahlfs LXX in Logos and Claim 3 upgraded accordingly `[revised: logos-research]`. **52:13 and 48:8 remain unverified** and are the next checks: 52:13 for the ὑψωθήσεται καὶ δοξασθήσεται pairing that Claim 4 rests on, 48:8 for the "you have never heard" wording that Claim 5 turns on. Both are free lookups on the Exegetical Guide.
2. **Parsenios's Graeco-Roman derivation** has not been assessed. Lincoln resists it; the audit has taken his word for the terms of the dispute. A Study Assistant query would settle how the field currently weighs the two.
3. **Whether Lincoln's πέμπω 25 / ἀποστέλλω 17 are indeed agency-context counts** — inferred from "in such contexts," not stated.
4. **19:13 (ἐκάθισεν)** — Lincoln's n. 2 says interpreters differ only over whether the irony is implicit or explicit, which is a stronger framing than our own "grammatically open". Worth adopting.

---

## Text-First Declaration

**Secondary sources present in context:** Lincoln ch. 9 (the audited source); `book-overview-john` v0.2.0; `dig-deeper-john-sweep` v1.1; `dig-deeper-john-1-1to18` v1.2; two May 2026 conversation records.

**Independence of the confirmations:** Claims 1, 7 and 8 were confirmed against findings the overview and sweep reached **before Lincoln was in the folder** — the μαρτυρ- density, the Baptist insertions as structural, the ἀποσυνάγωγος caution, and the forensic frame itself. Those confirmations are earned. Claims 2–6, 9 and 10 were tested *after* reading him and are audits of his claims, not independent corroborations.

**Verification basis:** SBLGNT for Matthew, Mark, Luke and John, by scripted sweep; every count in this audit is reproducible. **LXX Isaiah 43:10 verified** against Rahlfs in Logos (23 August 2026), together with the underlying Hebrew — Claim 3 upgraded and Claim 6's Volume score raised. **The LXX side of Claims 4 and 5 remains unverified** (Isa 52:13; 48:8) and is the audit's residual exposure.

**Reference files viewed:** `claim-audit-format.md` (loaded before scoping, per Phase 0.5b); core tools 01–07, preacher-extras, and all seven extensions viewed earlier this session and still in context.

**Warrant counts:** `[T]` ≈ 34 · `[I]` ≈ 9 · `[S]` ≈ 12 (of which 9 are `[S: Lincoln]`)

**Health note:** The `[S]` count is higher than a passage report's, which is correct for an audit — the claims *are* the source's. What matters is that the *tests* are `[T]`: every verdict above rests on a machine-verified count or a verified Greek text, not on judgement about Lincoln's plausibility. The one exception is Claim 5, where the absence of an LXX text left me unable to test, and the verdict is "Uncertain" rather than a guess dressed as a finding.

---

*Claim audit: Lincoln, "The Divine Courtroom and the Gospel of John." Consumed at Phase 5.5 by subsequent John dig-deepers — accept verdicts as given, tag `[S: audit]`, surface tensions rather than re-deriving.*
