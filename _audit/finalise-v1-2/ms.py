from lib import D
d=D('../../Colossians/colossians-dig-deeper-macro-synthesis.md')
d.I("Companion to the Colossians Book Overview (v1.1)","Companion to the Colossians Book Overview (v1.2)")
d.R('**Date:** 31 October 2026\\',"**Date:** 31 October 2026 · **Version:** 1.1 (4 November 2026: claim audit 5 and Logos round 5; see *What Changed in v1.1*)\\")
d.R('**Runs consumed:**',"**Runs consumed:** twelve of twelve preaching units, all five ⭐ HIGH units among them; claim audits 1–5; Logos rounds 1–5")
d.I("Across four audits the words held where they were counted correctly, and the designs mostly needed reframing.","Across five audits the words held where they were counted correctly, and the designs mostly needed reframing.")
# 3
d.R('- **§6 (2:16–23).** The regimen is rejected',"- **§6 (2:16–23).** The regimen is rejected: it does nothing as a remedy for the flesh, on every reading of the last clause of 2:23 `[I]`, high. That clause is disputed. The English versions print \"of no value against fleshly indulgence\", and the Greek leans to \"not in any honour\", moderate `[S: Logos 5]`.")
# 5
L=d.t.split('\n')
s=[i for i,l in enumerate(L) if l.startswith('## 5. The Letter')][0]
e=[i for i,l in enumerate(L) if l.startswith('## 6. Salvation')][0]
new="""## 5. Rare Phrases Repeated at a Distance — Not Welded Seams

**Claim (restated in v1.1).** Colossians repeats rare words and phrases across a unit or more, so that passages some way apart answer one another. **The earlier claim, that each joint between units picks up a rare word from the passage before, is discarded as a design** `[S: audit 5]`.

**What the audit measured.** Rarer vocabulary was counted across the three verses either side of every possible cut in the letter, and the eleven real joints were compared with 20,000 random sets of eleven cuts `[S: audit 5]`:

| Rarer lemmas, up to | Mean shared at the real joints | Mean at all cuts | Random sets doing as well |
|---|---|---|---|
| 50 NT verses | 0.27 | 0.47 | 89 % |
| 100 NT verses | 0.45 | 0.66 | 82 % |

**The joints carry less rare vocabulary than an average cut point.** Editors break paragraphs where the vocabulary changes, so this is what one would expect. Philippians and Ephesians, measured the same way, sit at or slightly above their own averages.

**The links, one by one** `[S: audit 5]`:
- **High:**
  - 1:23 → 1:25, "of which I became a minister" (ἐγενόμην ἐγώ, "I became", NT only these two; §3 → §4);
  - 2:20 → 3:1, the twin conditionals (§6 → §7);
  - 3:17 → 3:23, "whatever you do", with a relative + ἐὰν ποιῆτε in the NT only here (§9 → §10). The forms differ: ὅ τι at 3:17, ὃ at 3:23. The pick-up is moderate–high, and the whole code as 3:17 applied is moderate `[S: audit 3]`;
  - ἀποκαταλλάσσω ("to reconcile"), NT only Eph 2:16 and Col 1:20, 22 (§2 → §3).
- **Distance echoes, verified:** 2:8 → 2:20, τὰ στοιχεῖα τοῦ κόσμου ("the elements of the world"; also Gal 4:3); 2:14 → 2:20, δόγμα → δογματίζομαι ("decree" → "submit to decrees"); 2:15 → 3:9, ἀπεκδύομαι ("strip off"), NT only these two, with ἀπέκδυσις at 2:11.
- **Real, but ordinary Pauline connection:** 1:14 → 1:15, the relative chain (cf. Eph 1:7); 1:20 → 1:21, καὶ ὑμᾶς ("and you", Paul's resumptive idiom, Col 2:13; Eph 2:1); 3:10 → 3:12, ἐνδύω ("put on").
- **Not rare:** 3:2 → 3:5, ἐπὶ τῆς γῆς ("on earth", 52 NT verses).
- **Corrected:**
  - 2:5 → 2:6–7: the link to 2:5 is πίστις ("faith") alone. "Walk" with "Lord" pairs 1:10 and 2:6, and "learned" is at 1:7.
  - 3:22–4:1 → 4:9: Colossians never calls Onesimus a slave. That link needs Philemon. Inside the letter δοῦλος ("slave") passes to Epaphras (4:12).

**Confidence.** High on the named pairs. **Low on the seams as a design, and discarded.** That the letter uses distance repetition *as a device* is unmeasured: audit 5 observes it but ran no baseline on it. By the rule for design claims it stands at moderate at most, and it is a target for the next audit.

**Payoff.** Preach the far echoes: the congregation can hear 3:17 in 3:23 and 2:8 in 2:20. "Open by reading the last verse of the previous unit" still stands where a real link runs (1:14/15; 1:20/21; 2:20/3:1). It is a preaching point, not a claim about how the letter was built.

---
""".split('\n')
L[s:e]=new
d.t='\n'.join(L)
# 7
d.R('- **The share and the lot** (1:12, §1).',"- **The share and the lot** (1:12, §1). μερίς (\"share\") with κλῆρος (\"lot\") is Israel's Levitical idiom, standing in eleven Swete verses `[S: audit 4]`. The idiom is moderate. In the NT the two words stand together only at Acts 8:21 and Col 1:12 `[S: audit 5]`. At Deut 9:26–29 Israel *is* God's portion, while here believers receive one, so Deut 9 is low–moderate.")
# 8
d.R('- **The dwelling** (1:19, §2; 2:9, §5).',"- **The dwelling** (1:19, §2; 2:9, §5). \"All the fullness was pleased to dwell\" in him. Ps 67:17 LXX (Ps 68:16) is the only verse in Swete where εὐδοκέω (\"be pleased\") and κατοικέω (\"dwell\") have God as subject together, of God's mountain. *Moderate–high* at 1:19; the temple overtone is moderate `[S: audit 5]`. Pao: \"Christ fulfills the role of the temple\" `[S: Logos 5]`. 2:9 adds the strongest deity statement in the letter, θεότης (\"Deity\", nowhere else in the NT) `[T]`.")
# 9
d.R('- **The word handed on** (§11).',"- **The word handed on** (§11). \"A door for the word\" (4:3) becomes \"your word\" (4:6). δεῖ (\"must\") is Paul's (4:4) and the church's (4:6), its only two uses in the letter (counted by form) `[T]`. The fuller speech thread (3:8–9 → 3:16–17 → 4:3–4 → 4:6; §8, §9, §11) is carried by a cluster of speech words, not by λόγος, which is absent from 3:8–9 and changes sense along the way. ἐν χάριτι (3:16; 4:6) is its most specific link. It is *moderate* as design, and Eph 4:29–6:20 has the same sequence, so it is Paul's paraenetic pattern `[S: audit 5]`.")
d.R('- **Epaphras prays the letter** (4:12, §12).',"- **Epaphras prays the letter** (4:12, §12). He gathers Paul's struggle (ἀγωνίζομαι, \"strive\", 1:29), maturity (τέλειος, \"complete\", 1:28), full assurance (πληροφορέω, \"be fully assured\", from πληροφορία at 2:2), and, from the opening prayer rather than the labour passage, the will of God (θέλημα, 1:9) `[T]`, high. Pao names these links (pp. 315–16) `[S: Logos 5]`.")
d.R('**The frame.** The personal material',"**The frame (restated).** 4:2–13 picks up the vocabulary of Paul's labour in 1:25–2:7, above all μυστήριον (\"mystery\") with φανερόω (\"make manifest\") within two verses (1:26–27; 4:3–4; elsewhere in the NT only 1 Tim 3:16) `[T]`. It is the strongest closing link of twelve Pauline letters on this measure, with 1.7 % of window pairs doing as well at the 50-verse threshold, though not at the strictest. The greetings of 4:14–18 add nothing, and Romans is parallel only thematically. *Moderate* `[S: audit 5]`. Eight of the overview's 23 Draft echoes land in 4:7–18 (§12).")
d.R('**Confidence: strong** for the handing-over',"**Confidence: strong** for the handing-over (§1, §4, §9, §11, §12; the words are high). **Moderate** for the frame and for the speech thread as designs.")
# 10
d.R('- **Slaves** (§8, §10, §12).',"- **Slaves** (§8, §10, §12). δοῦλος (\"slave\") at 3:11 (\"slave and free\"), then the slaves addressed at the greatest length in the code (3:22–25: 56 of 116 words), then Epaphras, \"a slave of Christ\" (4:12) `[T]`, high. **Onesimus** is \"the faithful and beloved brother, who is one of you\" (4:9) — the titles of Epaphras and Tychicus — and \"one of you\" is said only of him and of Epaphras `[T]`, high. **Colossians never calls him a slave.** That comes from Phlm 16, so the person who is the point of this line can be seen only with Philemon beside it `[S: audit 5]`.")
# 11
d.I("*Moderate* as reclaiming `[S: audit 2]`.","*Moderate* as reclaiming `[S: audit 2]`. Audit 5 queues it as C78 with a suggested *moderate–high*; it is unaudited, so *moderate* stands. Audit 5 also groups σύνδεσμος (\"bond\", 2:19 → 3:14) with it, but the word is not pejorative at 2:19, and audit 2 calls that link a continuation. It is not counted here.")
# 12
d.I("The Echo Table grew from 23 to 70 rows","The Echo Table grew from 23 to 73 rows")
d.I("**No live Old Testament source survived** in the strict sense `[S: audit 1–4]`.","**No live Old Testament source survived** in the strict sense `[S: audit 1–5]`.")
d.R('- **What held and what did not.**',"- **What held and what did not.** Across five audits and claims C1–C72, every exclusive *wording* contact held where it was correctly counted. Most rarity \"only\"s and \"most stable partner\" claims needed correcting, and design and field claims mostly needed reframing `[S: audit 1–5]`. Audit 5 ran a baseline on the letter's own architecture: the seams fell below chance, the \"summary\" unit reached only the upper third, and the frame within Colossians survived (1.7 %), as did the λόγος density (about the 96th percentile).")
d.I("and the scan is silent on several stems `[S: audit 4]`.","and the scan is silent on several stems `[S: audit 4]`. It is nearly blind at 1:12–14 `[S: audit 5]`.")
d.R('**Confidence: strong as a measured finding**',"**Confidence: strong as a measured finding** (all twelve runs; five audits).")
# CANDIDATES
d.R('| The exodus redemption | §1 only',"| The exodus redemption | §1 only (1:12–14) | One pericope. Moderate as a pattern there, anchored in Exod 6:6–8 `[S: audit 5]`. Ps 106 LXX is out. No other run found exodus language. |")
d.R('| The dwelling chain (1:19; 2:9; 3:16',"| The indwelling thread (1:19; 2:9 → 3:16 ἐνοικείτω, \"let it dwell in\") | §2, §5, §9 | Restated from a \"dwelling chain\" read as a temple thread. 1:19 with Ps 67:17 LXX is moderate–high; 1:19 and 2:9 are one formula, high as repetition, with a moderate temple overtone. **3:16 as temple is low**: ἐνοικέω is never used of God in Swete, 3:16 has no temple vocabulary, and the nearest parallel is Eph 3:17 `[S: audit 5]`. Near the gate, not macro. |")
d.R('| Lukan affinities (Acts 26:18',"| The Lukan conversion idiom (Acts 26:18; Luke 22:53; Acts 8:21; Luke 1:68–79) | §1 (1:12–14) | One pericope. Moderate–high there, and **low as a description of the letter**, which is the least Lukan of the thirteen Pauline letters. Luke 8:15 belongs to the shared sower tradition `[S: audit 5]`. |")
# CROSS-REF
d.R('| 5 | The seams welded',"| 5 | Rare phrases repeated at a distance, not welded seams | §2–§10 | high (the named pairs); discarded (seams as design); moderate at most (distance repetition as device) |")
d.R('| 9 | The apostle',"| 9 | The apostle's ministry handed to the church; the close answering the opening | §1, §4, §9, §11, §12 | strong (handing-over); moderate (frame; speech thread) |")
# SERIES
d.I("It welds each passage to the last (argument 5).","It repeats its rare phrases across its units, though its joints are no more welded than random cuts (argument 5).")
d.I("a slave called brother, Jewish co-workers,","a man whom Philemon shows to be a slave, called brother here; Jewish co-workers;")
d.I("a founder praying the letter (arguments 9–10)","and a founder praying the letter (arguments 9–10)")
d.R('- read the last verse of the previous unit first;',"- where a real link runs (1:14/15; 1:20/21; 2:20/3:1), read the last verse of the previous unit first;")
# WHAT CHANGED + DECL
d.B('## Text-First Declaration',"""## What Changed in v1.1

| Where | Change | Source |
|---|---|---|
| Argument 5 | Rewritten. Welded seams discarded as a design; the pairs kept at their ratings; two welds corrected; distance repetition capped at moderate | `[S: audit 5]` C71 |
| Argument 3 | The 2:23 line no longer quotes one reading of a disputed clause as `[T]` | `[S: Logos 5]` |
| Argument 7 | The formula and Acts 8:21 added; Deut 9 at low–moderate | `[S: audit 5]` C62 |
| Argument 8 | Ps 67:17 at moderate–high, temple overtone moderate; Pao added | `[S: audit 5]` C72 |
| Argument 9 | Frame and speech thread restated; θέλημα assigned to 1:9 | `[S: audit 5]` C65, C68 |
| Argument 10 | Onesimus: never called a slave in Colossians | `[S: audit 5]` C71 |
| Argument 11 | The σύνδεσμος grouping in audit 5 noted and not followed | this pass, on audit 2 |
| Argument 12 | Five audits; the architecture baselines added | `[S: audit 5]` |
| Candidates | Exodus, indwelling and Lukan rows restated | `[S: audit 5]` |

**The other arguments are unchanged.** There are still twelve, and argument 5 keeps its number with a new claim.

---
""")
d.R('- the Book Overview v1.0;',"- the Book Overview v1.0, and v1.2 for this revision;")
d.R('- claim audits 1–4 and Logos rounds 1–4,',"- claim audits 1–5 and Logos rounds 1–5, through the runs and the overview.")
d.R('- **New design claims:**',"- **New design claims:** distance repetition as a device (argument 5) is named for the next audit. The two named in the first version, the seams and the dwelling chain, were tested by audit 5.")
d.I("*Provenance: emergent from the twelve dig-deeper runs and reconciled with the Colossians Book Overview (v1.0 → v1.1) and claim audits 1–4.","*Provenance: emergent from the twelve dig-deeper runs and reconciled with the Colossians Book Overview (v1.2) and claim audits 1–5.")
d.save()
