#!/usr/bin/env python3
"""Apply Colossians Logos round 5 (4 Nov 2026) to the digs and claim audit 4.
Every edit must match exactly once; otherwise it is reported and the file is NOT written."""
import re, sys, os
os.chdir(sys.argv[1])
L5 = '`[S: Logos 5]`'
SRC = ("*Source: Patrick's fifth Logos round (`Colossians/colossians-logos-answers-round-5-assessment.md`), "
       "checked against the NA28 text and apparatus, the SBLGNT, Swete and the Rahlfs Psalter, with the whole "
       "Clementine Vulgate and KJV of Colossians now filed in `_texts/logos-exports/02-New-Testament/`. Changes are "
       "made in place and tagged `[S: Logos 5]`. No claim-audit rating is changed.*")
errors = []
files = {}

def load(f):
    if f not in files:
        files[f] = open(f, encoding='utf-8').read()
    return files[f]

def rep(f, old, new):
    t = load(f); n = t.count(old)
    if n != 1:
        errors.append(f'{f}: rep count {n}: {old[:70]!r}'); return
    files[f] = t.replace(old, new)

def oq(f, prefix, add):
    """append text to the end of the (single) line that starts with prefix (after stripping leading spaces)"""
    lines = load(f).split('\n'); hits = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    if len(hits) != 1:
        errors.append(f'{f}: oq hits {len(hits)}: {prefix!r}'); return
    i = hits[0]; lines[i] = lines[i].rstrip() + ' ' + add
    files[f] = '\n'.join(lines)

def after(f, prefix, newline):
    lines = load(f).split('\n'); hits = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    if len(hits) != 1:
        errors.append(f'{f}: after hits {len(hits)}: {prefix!r}'); return
    lines.insert(hits[0] + 1, newline); files[f] = '\n'.join(lines)

def inline(f, prefix, old, new):
    lines = load(f).split('\n'); hits = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    if len(hits) != 1 or lines[hits[0]].count(old) != 1:
        errors.append(f'{f}: inline {prefix!r} / {old[:50]!r}'); return
    lines[hits[0]] = lines[hits[0]].replace(old, new); files[f] = '\n'.join(lines)

def tail(f, text):
    files[f] = load(f).rstrip('\n') + '\n\n---\n\n' + text.strip('\n') + '\n'

D = 'dig-deeper-colossians-'

# ---------------------------------------------------------------- 1:1-14  v1.2
f = D + '1-1to14.md'
rep(f, "**Version:** 1.1 (claim audit 4 applied, 31 October 2026; see *Revision v1.1*)",
       "**Version:** 1.2 (claim audit 4 applied, 31 October 2026; Patrick's fifth Logos round, 4 November 2026; see *Revision v1.1* and *v1.2*)")
rep(f, "*(moderate confidence — from recall; the Clementine text for this passage is not in the corpus)*",
       "*(v1.2: verified in the Clementine text, now filed as `12-Colossians-Vulgate-Clementine.txt`)* `[T]`")
rep(f, "*(moderate — recall)*", "*(verified, v1.2)* `[T]`")
rep(f, "*Uncertain — consider verifying both against the Clementine export if a Vulgate check is wanted.*",
       "**v1.2:** both verified `[T]`.")
oq(f, "1. **The punctuation of 1:11–12**",
   f"**v1.2** {L5}: Pao (ZECNT, 73) takes μετὰ χαρᾶς (\"with joy\") with the thanksgiving: each of the three earlier participial phrases carries a prepositional phrase, and Paul gives thanks \"with joy\" at Phil 1:4. Dunn, Wright and Bird were not returned. NA28 punctuates before Μετὰ χαρᾶς; the KJV (\"longsuffering with joyfulness; Giving thanks\") takes it with what precedes `[T]`. *Slight lean to the thanksgiving, low–moderate; still open.*")
oq(f, "2. **\"The saints in light\" (1:12)**",
   f"**v1.2** {L5}: believers — Wright (TNTC, 64–65, n. 12, against the angelic reading), Pao (74–75: from 1:2, 4, and the land texts Deut 32:9; Josh 19:9), Dunn (77: human saints, with Qumran as a picture of shared worship), Osborne (28); open to angels — Bird (42–43: 1QS 11:7–8; light with angels at 1QS 3:20; cf. 2:18). Wis 5:5 is cited by Dunn and Witherington; Qumran by Dunn, Pao, Witherington and Bird, with references. *Believers, moderate–high; unchanged, now with owned holders.* 1QH is cited under two numbering systems; check against one edition before quoting.")
oq(f, "3. **1:7 ὑμῶν / ἡμῶν**",
   f"**v1.2** {L5}: Dunn and Pao were not returned; Robertson (*Word Pictures*) holds ἡμῶν (\"our\") \"clearly correct\". The Vulgate (*pro vobis*) and the KJV (\"for you\") follow ὑμῶν (\"your\") with the Latin and Byzantine witnesses `[T]`. *Uncertain; unchanged.* Next: the *Lexham Textual Notes* (owned).")
oq(f, "7. **μεθίστημι (1:13)**",
   f"**v1.2** {L5}: Barclay (NDSB, 129), Barnes (246: Josephus, *Ant.* 9.11.1) and O'Brien, through Anders (294: *Ant.* 9.235, Tiglath-pileser moving the Transjordanian tribes, \"the same verb\"), make the case with a named text. Josephus is not in the corpus, so \"the same verb\" is unverified. *Uncertain → low–moderate.*")
oq(f, "8. **The Vulgate at 1:12–13**",
   "**Closed (v1.2):** both verified in the Clementine text (`_texts/logos-exports/02-New-Testament/12-Colossians-Vulgate-Clementine.txt`) `[T]`.")
oq(f, "9. **The Anglicised ESV**", "**v1.2:** not owned in Logos; on pre-order. *Open.*")
tail(f, f"""## Revision v1.2 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.1 | v1.2 |
|---|---|---|
| Open Questions 1 (with joy) | genuinely open | **slight lean to the thanksgiving, low–moderate** (Pao; NA28's punctuation) |
| Open Questions 2 (the saints) | believers moderate–high; holders wanted | unchanged; owned holders named both ways |
| Open Questions 3 (1:7) | uncertain | unchanged; Robertson for ἡμῶν; the Vulgate and KJV for ὑμῶν |
| Open Questions 7 (μεθίστημι) | uncertain | **low–moderate** (Barclay; Barnes; O'Brien via Anders; Josephus, *Ant.* 9.235) |
| Ancient versions check; Open Questions 8 | Vulgate recalled | **verified** (Clementine) |
| Lukan affinities (1:12–14 and Acts 26:18) | no holder | Dunn reports Aletti, who "wonders whether it points to Lukan authorship"; Pao (76) reads Acts 26:18 as shared confessional wording. For claim audit 5; any authorship inference stays `[I]` |
| "You → us" (1:12–13) | no holder | Osborne (28) and Wilson (*ESV EC*, 11:215–16) read the shift as deliberate and inclusive. **For the preacher:** the KJV levels it ("made us meet … delivered us", following ἡμᾶς at 1:12 with A C D F G K L P Ψ 𝔪 lat), and so does the Vulgate (*dignos nos fecit*) `[T]` |
| C46, C48, C50 (claim audit 4) | history pending | holders recorded in claim audit 4 v1.1 |

**Library status:** owned and cited here — Dunn, Pao, Wright, Witherington, Bird, Osborne, Barclay, Barnes, Anders, Robertson (*Word Pictures*), Wilson (*ESV Expository Commentary*). Aletti and O'Brien at second hand.

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 1:15-20  v1.7
f = D + '1-15to20.md'
rep(f, "**Version:** 1.6 (", "**Version:** 1.7 (")
rep(f, "from his fourth — see *What Changed in v1.2* to *v1.6*)",
       "from his fourth; v1.7 on 4 November 2026 from his fifth — see *What Changed in v1.2* to *v1.7*)")
t = load(f)
m = re.findall(r"The confession['’]s vocabulary was familiar\.", t)
if len(m) != 1: errors.append(f'{f}: confession sentence count {len(m)}')
else:
    files[f] = t.replace(m[0],
      f"**v1.7** {L5}, `[T]` for Philo's wording: the Greek is now seen (Colson's text, LCL 4:88–90 and vol. 3, from Patrick's page scans; filed in `_texts/logos-exports/03-Other-Ancient-Texts/`). *Conf.* 146 has κατὰ τὸν πρωτόγονον αὐτοῦ λόγον (\"according to his first-born Word\"), and names the Logos ἀρχή (\"Beginning\") and ὁ κατ᾽ εἰκόνα ἄνθρωπος (\"the man after the image\"). *Conf.* 147 has τῆς ἀειδοῦς εἰκόνος αὐτοῦ (\"his unseen image\") and θεοῦ γὰρ εἰκὼν λόγος ὁ πρεσβύτατος (\"for God's image is the eldest Word\"). *Agr.* 51 has πρωτόγονον υἱόν (\"first-born son\"). Colossians has πρωτότοκος (\"firstborn\") and ἀοράτου (\"invisible\"): on two of the three titles the words differ, and only εἰκών (\"image\") and ἀρχή (\"beginning\", 1:18) are shared. The confession's *ideas* were familiar; its words are not Philo's.")
oq(f, "7. **Philo's εἰκών and πρωτόγονος for the Logos**",
   f"**Closed (v1.7)** {L5}: the Greek is seen — πρωτόγονος at *Conf.* 146 and *Agr.* 51; ἀειδοῦς (\"unseen\") at *Conf.* 147, where Colossians has ἀοράτου (\"invisible\"); πρεσβύτατος (\"eldest\") confirmed. Yonge's \"eternal\" presumably reflects ἀιδίου (\"eternal\") in an older printed text — an inference, unverified. *A conceptual background, not a verbal one.*")
t = load(f); n = t.count('104 or 107')
if n: files[f] = t.replace('104 or 107', '104 (confirmed, v1.7)')
tail(f, f"""## What Changed in v1.7

*4 November 2026.* {SRC}

| Item | v1.6 | v1.7 | Where |
|---|---|---|---|
| Philo | numbering closed; Greek unseen; "invisible / eternal" flagged | **Greek seen**: πρωτόγονος (*Conf.* 146; *Agr.* 51), ἀειδοῦς (*Conf.* 147), πρεσβύτατος; Colossians' πρωτότοκος and ἀοράτου are different words. **Conceptual background only** | Historical Background 2; Open Questions 7 |
| Dunn's page for 1:20 | 104 or 107 | **104** (Patrick's check) | Tool 8 §2; Open Questions 2 ({n} place(s) updated) |

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 1:21-23  v1.1
f = D + '1-21to23.md'
rep(f, "**Version:** 1.0\\", "**Version:** 1.1 (4 November 2026: Patrick's fifth Logos round; see *Revision v1.1*)\\")
rep(f, "*(moderate confidence — from recall; the Clementine text for this passage is not in the corpus)*",
       "*(v1.1: verified in the Clementine text, now filed; punctuation aside)* `[T]`")
rep(f, "*Uncertain — verify if the Latin is to be cited.*",
       "**v1.1:** verified. The Vulgate renders εἴ γε (\"if indeed\") as *si tamen* (\"if only\") `[T]`.")
oq(f, "1. **1:22, active or passive?**",
   f"**v1.1** {L5}: Dunn and Pao were not returned on the variant. The Vulgate (*reconciliavit*) and the KJV (\"yet now hath he reconciled\") are active `[T]`. *Divided; unchanged.*")
oq(f, "2. **The subject of the verb",
   f"**v1.1** {L5}: Bird (NCCS, 61) has Christ as reconciler and \"before him\" probably as Jesus the judge. The Assistant's two summaries of Dunn conflict (round 4: \"reverts to … through Christ to God\"; round 5: \"maintains Christ as subject\"); his p. 107 is needed. *God, moderate–high on the text; unchanged. Christ now has an owned holder.*")
oq(f, "3. **The timing of the presentation**",
   f"**v1.1** {L5}: Bird — the final presentation, Christ as judge. Pao (108–9) allows either and says a future reference \"is not necessary\"; the summary's further claim that he prefers the present is the Assistant's. *Eschatological, moderate–high; unchanged.*")
oq(f, "4. **εἴ γε**",
   f"**v1.1** {L5}: Robertson's *Grammar* (1027, 1147–48): γε adds emphasis or a concessive \"at least\", and particles do not alter the class of condition. Cornerstone vol. 16 (256): conditions \"expected to be fulfilled\". Pao (109): only in Paul; more probable at 2 Cor 5:3; Eph 3:2; 4:21, less probable at Gal 3:4; at 1:23 the stress falls on the conditionality as a call to persevere. The SBLGNT has five (2 Cor 5:3; Gal 3:4; Eph 3:2; 4:21; Col 1:23) `[T]`, against EDNT's \"six\". *A confident condition, moderate–high* — but not confident at Gal 3:4. **For the overview's Trap 6 (Finalise pass):** \"confident in most of Paul's uses (not Gal 3:4)\".")
oq(f, "7. **The Vulgate**", "**Closed (v1.1):** verified in the Clementine text `[T]`.")
tail(f, f"""## Revision v1.1 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.0 | v1.1 |
|---|---|---|
| Open Questions 1 (active / passive) | divided | unchanged; the Vulgate and KJV are active |
| Open Questions 2 (subject; "before him") | God, moderate–high | unchanged; Bird holds Christ; Dunn's summaries conflict (p. 107 needed) |
| Open Questions 3 (timing) | eschatological, moderate–high | unchanged; Bird for the final presentation; Pao's page needed |
| Open Questions 4 (εἴ γε) | open | **confident condition, moderate–high**, except Gal 3:4 (Robertson; Cornerstone; Pao; SBLGNT count) |
| Ancient versions check; Open Questions 7 | Vulgate recalled | **verified**; *si tamen* for εἴ γε |

**Library status:** owned and cited here — Dunn, Pao, Bird, Robertson (*Grammar*), the Cornerstone commentary (vol. 16), EDNT.

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 1:24-2:5  v1.7
f = D + '1-24to2-5.md'
rep(f, "**Version:** 1.6 (", "**Version:** 1.7 (")
rep(f, "— see *What Changed in v1.1* to *v1.6*)", "; v1.7 on 4 November 2026 from his fifth Logos round — see *What Changed in v1.1* to *v1.7*)")
rep(f, "The KJV is quoted from recall, and its readings in Tool 8 are `[unverified — check wording]` beyond the variant it follows at 2:2.",
       "The KJV readings in Tool 8 were quoted from recall; **v1.7:** all verified against the whole KJV of Colossians, now filed (`12-Colossians-KJV.txt`) `[T]`.")
after(f, "13. **The ESV export**",
   f"14. **The frame with 4:2–18 (Headline 4)** — **v1.7** {L5}: Pao (ZECNT, 315–16) names the links. Epaphras's \"striving\" (4:12) is Paul's verb at 1:29; his prayer for maturity answers 1:28; and \"the will of God\" answers 1:9. Corpus (SBLGNT, Colossians): ἀγωνίζομαι (\"to strive\") 1:29 and 4:12 only, with ἀγών (\"struggle\") at 2:1; τέλειος (\"mature\") 1:28 and 4:12 only; πληροφορία (\"full assurance\") 2:2 and πληροφορέω (\"to assure fully\") 4:12 `[T]`. *An owned holder, with verses; the frame goes to claim audit 5.*")
tail(f, f"""## What Changed in v1.7

*4 November 2026.* {SRC}

| Item | v1.6 | v1.7 | Where |
|---|---|---|---|
| KJV in Tool 8 | from recall | **verified** (whole KJV of Colossians filed) | Tool 8; Text-First Declaration |
| The frame with 4:2–18 | no holder | **Pao** (315–16) names 1:28, 1:29 and 1:9 against 4:12; the verbal links are exact in the SBLGNT | Headline 4; Open Questions 14 (new) |

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 2:6-15  v1.7
f = D + '2-6to15.md'
rep(f, "**Version:** 1.6 (", "**Version:** 1.7 (")
rep(f, "— see *What Changed in v1.1* to *v1.5*)", "; v1.7 on 4 November 2026 from his fifth — see *What Changed in v1.1* to *v1.7*)")
rep(f, "The KJV is quoted from recall and marked as such.",
       "The KJV column was quoted from recall; **v1.7:** every cell is verified against the whole KJV of Colossians, now filed `[T]`.")
rep(f, "| KJV (recall) |", "| KJV (verified v1.7) |")
rep(f, "The KJV is quoted from recall and marked so in Tool 8.",
       "The KJV, quoted from recall in v1.0, is verified (v1.7) against Patrick's paste, now filed.")
oq(f, "1. **The στοιχεῖα (2:8, 20).**",
   f"**v1.7** {L5}: Chrysostom (Hom. VI) takes the elements as \"the sun and moon\", which govern the observance of days (with Gal 4:9) — an ancient holder for the calendar sense. *Uncertain; unchanged.*")
oq(f, "3. **The subject of 2:15, and ἐν αὐτῷ.**",
   f"**v1.7** {L5}: Chrysostom (Hom. VI, NPNF English) holds option 2. Christ is subject; the middle is true (\"having put off from Himself … when He became Man He put away from Himself that hold\"); the triumph is at the cross (\"when That Body was nailed to the Cross … There death received his wound\"); and ἐν παρρησίᾳ (\"openly\") is \"through His confidence in dying\" (translators' note). He does not parse ἐν αὐτῷ (\"in him / in it\") in the English, so Jamieson–Fausset–Brown's \"the Greek fathers read 'in it'\" is consistent with him, not proved by him. *Slight lean to option 2, moderate; unchanged, with a patristic holder.*")
oq(f, "4. **The certificate of debt (2:14).**",
   f"**v1.7** {L5}: Chrysostom offers three bonds — Israel's \"All that God hath said will we do\" (Exod 24:3), the obedience owed to God, or the bond of Gen 2:17 \"which the devil held\" — and takes τοῖς δόγμασιν (\"by the decrees\") as \"doctrines\", that is, faith (with Theodoret, per the NPNF note, which itself prefers the KJV's \"ordinances\"). *Unchanged.*")
tail(f, f"""## What Changed in v1.7

*4 November 2026.* {SRC}

| Item | v1.6 | v1.7 | Where |
|---|---|---|---|
| KJV column of Tool 8 | from recall | **verified**, all fourteen cells | Tool 8; Text-First Declaration |
| 2:15, subject and ἐν αὐτῷ | slight lean to option 2; Chrysostom not returned | unchanged; **Chrysostom holds option 2** (Christ, true middle, the cross) | Difficult Verses; Open Questions 3 |
| 2:8 στοιχεῖα | uncertain | unchanged; Chrysostom: "the sun and moon" | Open Questions 1 |
| 2:14 the bond | moderate | unchanged; Chrysostom's three options recorded | Open Questions 4 |

**Library status:** Chrysostom, *Homilies on Colossians* (NPNF¹ 13), owned; Homilies VI–VII filed in English in `_texts/logos-exports/03-Other-Ancient-Texts/`.

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 2:16-23  v1.5
f = D + '2-16to23.md'
rep(f, "**Version:** 1.4 (", "**Version:** 1.5 (")
rep(f, "; see *Revision v1.1* to *v1.4*)", "; 4 November 2026: Patrick's fifth Logos round (v1.5); see *Revision v1.1* to *v1.5*)")
oq(f, "3. *\"severity to the body",
   f"**v1.5** {L5}: **Chrysostom** (Hom. VII) takes this reading: \"God hath given it honor, but they use it not with honor … They dishonor the flesh, he says, depriving it, and stripping it of its liberty … God hath honored the flesh.\" *Low → low–moderate*: it rests on the NPNF English, where \"flesh\" may stand for his σῶμα (\"body\"); not higher without his Greek.")
oq(f, "1. **2:23, the last clause.**",
   f"**v1.5** {L5}: Chrysostom holds reading 3 (low → low–moderate). The Vulgate's *non ad parcendum corpori, non in honore aliquo ad saturitatem carnis* has the shape of reading 2 or 3 `[T]`. *Readings 1 and 2 level, moderate each; unchanged.*")
oq(f, "2. **2:18, \"the worship of the angels\".**",
   f"**v1.5** {L5}: Chrysostom takes the genitive as objective — \"There are some who maintain that we must be brought near by Angels, not by Christ … he said not 'introduction by,' but 'worshiping of' Angels\" — and his text has the negative (\"which he hath not seen\"), with the Vulgate (*quæ non vidit*) and the KJV; ἃ μή (\"which not\") is the reading of א² C D¹ K L Ψ 𝔪 `[T]`. He also reports a punctuation of 2:17–18: \"the Body of Christ let no man adjudge away from you\". *Still uncertain; the handling stands.*")
oq(f, "5. **The Vulgate at 2:18 and 2:23**",
   "**v1.5:** the whole Clementine Vulgate and KJV of Colossians are now filed (`12-Colossians-Vulgate-Clementine.txt`, `12-Colossians-KJV.txt`); their wording here agrees with the extracts.")
tail(f, f"""## Revision v1.5 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.4 | v1.5 |
|---|---|---|
| Difficult Verses, 2:23, reading 3 | low | **low–moderate**: Chrysostom (NPNF English) |
| Difficult Verses, 2:23, readings 1 and 2 | level, moderate each | unchanged |
| Difficult Verses, 2:18, the genitive | uncertain, holders both ways | unchanged; **Chrysostom objective** (worship directed to angels as go-betweens); his text has the negative |
| 2:16–17 | — | Chrysostom presses ἐν μέρει as "in part" (the NPNF editor calls this "exegetically wrong") and reports the punctuation "the Body of Christ let no man adjudge away from you" (2:17b with 2:18) |
| Open Questions 5 | extracts filed | whole Vulgate and KJV filed |

**Library status:** Chrysostom, *Homilies on Colossians* (NPNF¹ 13), owned; Homily VII filed in English.

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 3:1-4  v1.2
f = D + '3-1to4.md'
rep(f, "**Version:** 1.1 (claim audit 4 applied, 31 October 2026: Deut 29:29 lowered to low)",
       "**Version:** 1.2 (claim audit 4 applied, 31 October 2026: Deut 29:29 lowered to low; Patrick's fifth Logos round, 4 November 2026: see *Revision v1.2*)")
inline(f, "**Ancient versions check.** The modern versions agree on \"seated",
       "*quae sursum sunt quaerite … quae sursum sunt sapite … vita vestra abscondita est cum Christo in Deo* *(moderate confidence — from recall; not in the corpus)*",
       "*quæ sursum sunt quærite … quæ sursum sunt sapite … vita vestra est abscondita cum Christo in Deo* *(v1.2: verified in the Clementine text, now filed; the recalled word order \"abscondita est\" was wrong)*")
inline(f, "**Ancient versions check.** The modern versions agree on \"seated", " `[unverified — check wording]`", " `[T]`")
oq(f, "2. **\"Realised\" resurrection**",
   f"**v1.2** {L5}: Dunn (NIGTC, 161, 203): a real development from \"not yet\" to \"already\", yet the resurrection still lies \"as much in the future as in Romans 6\" — a change of perspective, not yet of being — and it \"need not indicate post-Pauline authorship\". Bird (NCCS, 8): Romans has the past-tense \"glorified\", and \"the future horizon remains intact\". Wright was not returned. *Emphasis, not a different theology: moderate–high.*")
oq(f, "3. **Deut 29:29**",
   f"**v1.2** {L5}: Dunn (208) cites Deut 29:29 at 3:3–4 for the κρυπτός / φανερός (\"hidden\" / \"open\") contrast, with Mark 4:22; Rom 2:28–29; 1 Cor 14:25 — a vocabulary parallel. The audit's *low* stands.")
oq(f, "5. **The Vulgate**", "**Closed (v1.2):** verified, with one correction — *vita vestra **est abscondita*** (3:3) `[T]`.")
tail(f, f"""## Revision v1.2 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.1 | v1.2 |
|---|---|---|
| Open Questions 2 (realised resurrection) | `[S]`, open | **emphasis, not theology: moderate–high** (Dunn; Bird) |
| Open Questions 3 (Deut 29:29) | low | unchanged; Dunn cites it as a vocabulary parallel |
| Ancient versions check; Open Questions 5 | Vulgate recalled | **verified, one correction**: *vita vestra est abscondita* |

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 3:5-11  v1.1
f = D + '3-5to11.md'
rep(f, "**Version:** 1.0\\", "**Version:** 1.1 (4 November 2026: Patrick's fifth Logos round; see *Revision v1.1*)\\")
inline(f, "**Ancient versions check.** The moderns agree on the causal", "*(moderate confidence — from recall)*", "*(v1.1: verified in the Clementine text, now filed)*")
inline(f, "**Ancient versions check.** The moderns agree on the causal", " `[unverified — check wording]`", " `[T]`")
inline(f, "**Ancient versions check.** The moderns agree on the causal", "No translation-tradition split is claimed.",
       "The KJV renders the participles as causal: \"seeing that ye have put off the old man\" (3:9) `[T]`. No translation-tradition split is claimed.")
oq(f, "1. **3:6 — the bracketed phrase.**",
   f"**v1.1** {L5}: Pao (ZECNT, 221) finds a slightly stronger case for omission (𝔓⁴⁶ B; a possible borrowing from Eph 5:6), yet keeps the phrase in brackets with UBS⁴ and NA²⁷. Dunn includes it in his translation, with no discussion in what was returned. The Vulgate (*super filios incredulitatis*) and the KJV include it `[T]`. *Divided; unchanged.*")
oq(f, "2. **3:9–10 — causal or imperatival participles.**",
   f"**v1.1** {L5}: causal — Wilson (*ESV Expository Commentary*, 11:241–42; owned) and Gaffin (ownership unknown). The Assistant credited these to Wright and Bird, a misfiling, so neither Wright nor Bird is confirmed. Robertson's *Grammar* comments only on μὴ ψεύδεσθε (\"do not lie\"). The KJV's \"seeing that ye have put off\" is causal `[T]`. *Moderate–high; unchanged.*")
oq(f, "3. **νέος and καινός.**",
   f"**v1.1** {L5}: EDNT (2:462): νέος (\"new\") new in time, καινός (\"new\") new in kind; Trench (*Synonyms*, 223–24) develops it. *Moderate; unchanged.* The two words overlap in Koine, so do not build a sermon point on the difference `[S]` (a recalled caution).")
oq(f, "6. **The Vulgate wording**", "**Closed (v1.1):** verified in the Clementine text `[T]`.")
tail(f, f"""## Revision v1.1 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.0 | v1.1 |
|---|---|---|
| Open Questions 1 (3:6) | divided | unchanged; Pao leans to omission but brackets; the Vulgate and KJV include |
| Open Questions 2 (3:9–10) | causal, moderate–high | unchanged; Wilson holds it (Wright and Bird misfiled by the Assistant); **the KJV is causal** |
| Open Questions 3 (νέος / καινός) | moderate | unchanged; EDNT, Trench; caution added |
| Ancient versions check; Open Questions 6 | Vulgate recalled | **verified** |

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 3:12-17  v1.2
f = D + '3-12to17.md'
rep(f, "**Version:** 1.1 (claim audit 4 applied, 31 October 2026; see *Revision v1.1*)",
       "**Version:** 1.2 (claim audit 4 applied, 31 October 2026; Patrick's fifth Logos round, 4 November 2026; see *Revision v1.1* and *v1.2*)")
rep(f, "KJV \"bowels of mercies\" *(KJV from recall)*", "KJV \"bowels of mercies\" *(KJV verified, v1.2)*")
inline(f, "10. **3:13, 3:16, 3:17 in the KJV.**", "*(from recall — moderate confidence)* `[I]`",
       "*(verified, v1.2)* `[T]`. The KJV also has \"the peace **of God**\" at 3:15 (θεοῦ, 𝔪) `[T]`")
inline(f, "**Ancient versions check.** The moderns agree on the substance throughout.", "*(from recall — moderate confidence)* `[unverified — check wording]`", "*(verified, v1.2)* `[T]`")
oq(f, "1. **\"In all wisdom\"",
   f"**v1.2** {L5}: with the teaching — Pao (ZECNT, 248–49, making this dig's 1:28 argument) and Wright (TNTC, 148–49, as summarised). Dunn was not returned. The KJV (\"dwell in you richly in all wisdom; teaching\") takes it with the dwelling `[T]`. *Moderate → moderate–high for the teaching.*")
oq(f, "2. **The songs",
   f"**v1.2** {L5}: the means of teaching — Pao (the datives; Eph 5:19; 1 Cor 14:26; with \"singing\" one would expect accusatives); Beale (BECNT, from Patrick's notes: \"by means of … teaching and admonishing in OT psalms\"); and the KJV (\"teaching … in psalms … singing\") `[T]`. Wright's position was the Assistant's inference, not quoted. *Slight lean to the means, moderate.* For the pulpit: the ESV punctuates the songs with the singing.")
oq(f, "4. **τῆς τελειότητος",
   f"**v1.2** {L5}: Lange (70): the bond \"which unites all the graces into completeness\". Dunn's p. 130, as returned, is probably his comment on 2:2; Pao (244): love's \"supreme significance\". *Moderate; unchanged.*")
oq(f, "5. **3:15 — ἑνί",
   "**v1.2:** not found in Patrick's library; Metzger is not owned. The Vulgate (*in uno corpore*) and the KJV (\"in one body\") include ἑνί (\"one\") `[T]`. *Moderate; unchanged.* Next: the *Lexham Textual Notes* (owned).")
oq(f, "7. **The Psalter-titles observation (C56)**",
   f"**v1.2** {L5}: Beale (BECNT, from Patrick's notes) holds the titles reading — **in Rahlfs only**. Rahlfs has all three words in the titles of Pss 66 and 75; Swete's Vaticanus has them only in Ps 75 (66:1 reads ψαλμὸς τῷ Δαυείδ, \"a psalm of David\") `[T]`. Brown, Merkle (on Ephesians) and Exell take the words as overlapping; none argues for Psalms only. *Unchanged; state the edition when citing.*")
oq(f, "8. **Exodus 34:6 (C54) and Deuteronomy 7 (C55)**",
   f"**v1.2** {L5}: Exod 34:6 — Gurtner (BKBC, 604; owned), with Pss 24:6; 50:1; 102:4; 144:9 in the Greek numbering. Ps 144:9 LXX is Ps 145:9, and 144:8 LXX is the Exod 34:6 formula (οἰκτίρμων … μακρόθυμος, \"compassionate … patient\") `[T]`. Also Osborne (Rom 2:4). Deut 7 — Dunn (228: \"the classic covenant text\"; Isa 44:2 for \"beloved\"), Pao (240–41), Brown, Osborne (Deut 7:6; 14:2; 26:18–19). *Audit ratings unchanged; history recorded in claim audit 4 v1.1.*")
oq(f, "9. **KJV and Vulgate wording**", "**Closed (v1.2):** all verified against the whole KJV and Vulgate, now filed `[T]`.")
tail(f, f"""## Revision v1.2 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.1 | v1.2 |
|---|---|---|
| Open Questions 1 ("in all wisdom") | moderate | **moderate–high for the teaching** (Pao; Wright; NA28; 1:28) |
| Open Questions 2 (the songs) | moderate either way | **slight lean to the means, moderate** (Pao; Beale's notes; the KJV) |
| Open Questions 4 (the bond) | moderate | unchanged; Lange |
| Open Questions 5 (ἑνί) | moderate | unchanged; not found; the Vulgate and KJV include it |
| Open Questions 7 (C56) | observation moderate | unchanged; Beale holds it, **in Rahlfs only** |
| Open Questions 8 (C54, C55) | audit ratings | unchanged; Gurtner reaches Ps 145 (as 144 LXX); four owned holders for Deut 7 |
| Tool 8; Ancient versions; Open Questions 9 | KJV and Vulgate recalled | **verified**; KJV 3:15 "peace of God" added |

**Library status:** owned and cited here — Dunn, Pao, Wright, Brown, Osborne, Gurtner (BKBC), Lange, Merkle (on Ephesians), Exell. Beale's BECNT from Patrick's own notes (marked not owned in round 4).

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 3:18-4:1  v1.4
f = D + '3-18to4-1.md'
rep(f, "**Version:** 1.3 (28 October 2026: claim audit 3 applied; 29 October 2026: Patrick's fourth Logos round; 31 October 2026: claim audit 4 applied; see *Revision v1.1*, *v1.2* and *v1.3*)",
       "**Version:** 1.4 (28 October 2026: claim audit 3 applied; 29 October 2026: Patrick's fourth Logos round; 31 October 2026: claim audit 4 applied; 4 November 2026: his fifth Logos round; see *Revision v1.1* to *v1.4*)")
t = load(f); c = t.count("`[unverified — KJV from recall]`")
if c != 4: errors.append(f"{f}: KJV tag count {c}")
else: files[f] = t.replace("`[unverified — KJV from recall]`", "`[T]` (KJV verified, v1.4)")
rep(f, "- The KJV was quoted from recall and tagged `[unverified — check wording]`.",
       "- The KJV was quoted from recall and tagged `[unverified — check wording]`. **v1.4:** verified against the whole KJV of Colossians, now filed.")
oq(f, "1. **3:24 δουλεύετε",
   f"**v1.4** {L5}: the imperative side is now named — Pao's \"majority of recent commentators\" (275, n.): Moule, Lohse, Schweizer, O'Brien, Wright, Harris, Moo, Sumney; Dunn's n. (257): Abbott, Lohse, O'Brien, Harris, NEB/REB, with Lightfoot \"otherwise\". Dunn himself reads a reminder (\"it is the Lord Christ whose slaves they are\"). *Slight lean to the indicative, moderate; unchanged.*")
oq(f, "2. **3:25 — whose wrong?**",
   f"**v1.4** {L5}: Dunn (258–59): both slaves and masters; Witherington (194): either, the first \"certainly possible in light of 4:1\"; Wright (154): slaves first, but \"equally relevant\" to masters. No one uses Phlm 18. *Both, moderate; unchanged, now with owned holders.*")
tail(f, f"""## Revision v1.4 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.3 | v1.4 |
|---|---|---|
| Move 4, 1:12 → 3:24 (C40) | Dunn reached through Brown | **Dunn at first hand** (NIGTC, 256–57): "the allusion to it already in 1:12 … strongly suggest[s] … a share in the inheritance promised to Abraham". Brown's summary was accurate |
| Difficult Verses, 3:24 | slight lean to the indicative, moderate | unchanged; the imperative holders named (Pao's list; Dunn's n.) |
| Difficult Verses, 3:25 | both, moderate | unchanged; Dunn, Witherington, Wright |
| Tool 7, the fear of the Lord (C45) | history pending | Pao (Deut 6:2, 13, 24; 10:12, 20; 1 Sam 12:24) and Bird (Deut 10:12–13); Dunn cites Ps 19:11 for ἀνταπόδοσις ("repayment") as a good outcome, a lexical use |
| Job 31 at 4:1 (C44) | history pending | none found |
| Tool 8, KJV at 3:18 | from recall | **verified** |

**Library status:** owned and cited here — Dunn, Pao, Wright, Witherington, Bird.

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 4:2-6  v1.2
f = D + '4-2to6.md'
rep(f, "**Version:** 1.1 (claim audit 4 applied, 31 October 2026; see *Revision v1.1*)",
       "**Version:** 1.2 (claim audit 4 applied, 31 October 2026; Patrick's fifth Logos round, 4 November 2026; see *Revision v1.1* and *v1.2*)")
rep(f, "KJV \"for which I am also in bonds\" *(KJV from recall)*", "KJV \"for which I am also in bonds\" *(KJV verified, v1.2)*")
rep(f, "KJV \"redeeming the time\" *(from recall)*", "KJV \"redeeming the time\" *(verified, v1.2)*")
rep(f, "gave the KJV \"redeeming the time\" *(from recall — moderate confidence)* `[unverified — check wording]`",
       "gave the KJV \"redeeming the time\" *(verified, v1.2)* `[T]`")
oq(f, "1. **ἐξαγοράζομαι τὸν καιρόν**",
   f"**v1.2** {L5}: \"buying up\" — Wright (TNTC, 157: \"snapped up like a bargain\", not that time is evil and must be redeemed), Pao (296: \"buying out\", with no theological redemption here; Eph 5:16), Dunn (265: \"gain or reclaim time\"); \"redeeming\" — Osborne (133, with Gal 3:13; 4:4–5). *Moderate–high for \"buying up\"; unchanged, now with owned holders.* LSJ (owned) can test the non-biblical use with καιρός (\"time, opportunity\").")
oq(f, "2. **Daniel 2 at 4:2–5 (C57)**",
   f"**v1.2** {L5}: Osborne, Pao and Dunn cite Dan 2:8 at 4:5. Dunn's \"gain … time\" carries Daniel's stalling sense toward Paul's without comment; Pao keeps them apart. *Audit ratings unchanged.*")
oq(f, "3. **The Jesus-tradition cluster (C58)**",
   f"**v1.2** {L5}: Dunn (262: Gethsemane \"may\" be echoed; with Moule, Houlden, Caird) and Pao (Mark 14:38). A commentary commonplace; it does not revive the cluster, which failed its baseline.")
oq(f, "7. **The KJV and Vulgate wording**", "**Closed (v1.2):** verified against the whole KJV and Vulgate, now filed `[T]`.")
tail(f, f"""## Revision v1.2 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.1 | v1.2 |
|---|---|---|
| Open Questions 1 (ἐξαγοράζομαι) | moderate–high for "buying up" | unchanged; Wright, Pao, Dunn; Osborne for "redeeming" |
| Open Questions 2 (C57) | audit ratings | unchanged; three owned commentators cite Dan 2:8 |
| Open Questions 3 (C58) | discarded | unchanged; Dunn and Pao hold the Gethsemane echo |
| Tool 8; Ancient versions; Open Questions 7 | KJV and Vulgate recalled | **verified** |

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- 4:7-18  v1.1
f = D + '4-7to18.md'
rep(f, "**Version:** 1.0\\", "**Version:** 1.1 (4 November 2026: Patrick's fifth Logos round; see *Revision v1.1*)\\")
rep(f, "\"that he might know your estate\" *(from recall)*", "\"that he might know your estate\" *(verified, v1.1)*")
rep(f, "follow the majority Greek *(from recall)* `[I]`.",
       "follow the majority Greek *(verified, v1.1)* `[T]`. The Vulgate also follows the majority at 4:8 (*ut cognoscat quæ circa vos sunt*), and its *Nympham … in domo ejus* (4:15) is ambiguous for gender `[T]`.")
oq(f, "1. **4:8 variant**",
   f"**v1.1** {L5}: Dunn (272) and Pao follow NA28; Lange (82) argues for the other reading on exegetical grounds. **The external evidence is split**: the NA28 text has A B D*·ᶜ F G P 048 33 81 …; γνῷ τὰ περὶ ὑμῶν (\"that he may know about you\") has 𝔓⁴⁶ א²ᵃ·²ᵇ C D¹ K L Ψ 1739 1881 𝔪 f vg sy `[T]`. The Assistant's \"earliest and most reliable manuscripts\" for the NA28 text is wrong. *Moderate; unchanged.* Next: the *Lexham Textual Notes* (owned); Metzger is not owned.")
oq(f, "3. **συναιχμάλωτος**",
   f"**v1.1** {L5}: Pao (422): figurative (\"in Christ Jesus\" at Phlm 23; Paul's δέσμιος, \"prisoner\", for himself); Dunn (275–76, 347–48): literal, the companions taking turns, with 4:3, 18; Vos (ownership unknown): constant attendance. *Open; owned holders both ways.*")
oq(f, "4. **Nympha**",
   f"**v1.1** {L5}: Dunn (284) and Pao (318–19) read αὐτῆς (\"her\") without discussing the variants. Apparatus: αὐτῆς B 0278 6 1739 1881 syʰ sa; αὐτῶν (\"their\") א A C P 33 81 104 … bo; αὐτοῦ (\"his\") D F G K L Ψ 𝔪; the masculine accent Νυμφᾶν is 𝔪's, the early uncials being unaccented `[T]`. *Moderate–high; unchanged.*")
oq(f, "7. **KJV wording; Rev 3:15–22 wording; Deut 31:11**",
   "**v1.1:** the KJV wording is verified against the whole KJV of Colossians, now filed `[T]`. Rev 3:15–22 and Deut 31:11 are still unchecked.")
tail(f, f"""## Revision v1.1 — Logos round 5 (4 November 2026)

{SRC}

| Where | v1.0 | v1.1 |
|---|---|---|
| Open Questions 1 (4:8) | moderate | unchanged; Dunn and Pao follow NA28; Lange the other reading; **𝔓⁴⁶ supports γνῷ … ὑμῶν** |
| Open Questions 3 (συναιχμάλωτος) | open | unchanged; Pao figurative, Dunn literal |
| Open Questions 4 (Nympha) | "her" moderate–high | unchanged; apparatus spread recorded |
| Tool 8; Ancient versions; Open Questions 7 | KJV recalled | **verified**; Vulgate at 4:8 and 4:15 added |

**Library status:** owned and cited here — Dunn, Pao, Lange.

**Headlines:** unchanged.""")

# ---------------------------------------------------------------- claim audit 4  v1.1
f = D + 'claim-audit-4.md'
rep(f, "**Version:** 1.0\\", "**Version:** 1.1 (4 November 2026: history-of-interpretation rows from Patrick's fifth Logos round)\\")
rep(f, "**No verdict below rests on this row.**",
    "**No verdict below rests on this row.** **v1.1 (4 November 2026):** the rows now carry Patrick's fifth Logos round (`Colossians/colossians-logos-answers-round-5-assessment.md`, §2), tagged `[S: Logos 5]`. No verdict changed.")
H = {
 1: "**Logos 5:** none found " + L5,
 2: "**Logos 5:** Pao (Deut 6:2, 13, 24; 10:12, 20; 1 Sam 12:24) and Bird (Deut 10:12–13) for the formula; Dunn cites Ps 19:11 for ἀνταπόδοσις as a good outcome (lexical) " + L5,
 3: "**Logos 5:** believers — Wright, Pao, Dunn, Osborne; open to angels — Bird; Wis 5:5 — Dunn, Witherington; Qumran — Dunn, Pao, Witherington, Bird; Acts 26:18 — Dunn (reporting Aletti), Pao; Ps 15:5 LXX — none " + L5,
 4: "**Logos 5:** Pao (Exod 6:6 LXX; Isa 41–44; Hos 13:14 LXX) and Osborne (Exod 6:6; 14:30; Deut 7:8); Wright and Witherington without a text " + L5,
 5: "**Logos 5:** the sower — Dunn (Mark 4:8), Pao (Luke 8:15, with the rival Acts 6:7; 12:24; 19:20); Gen 1:28 — Wright, Pao, Bird, Osborne " + L5,
 6: "**Logos 5:** Dunn (NIGTC, 208), as a vocabulary parallel " + L5,
 7: "**Logos 5:** Gurtner (BKBC, 604: Exod 34:6; Ps 144:9 LXX = Ps 145:9); Osborne (Rom 2:4); Merkle on Ephesians " + L5,
 8: "**Logos 5:** Dunn (\"the classic covenant text\"), Pao, Brown and Osborne all name Deut 7:6; Dunn adds Isa 44:2 " + L5,
 9: "**Logos 5:** Beale (BECNT, Patrick's notes) holds the titles reading — true in Rahlfs (Pss 66, 75), not in Swete (Ps 75 only); none argues for Psalms only " + L5,
 10: "**Logos 5:** Osborne, Pao and Dunn cite Dan 2:8 " + L5,
 11: "**Logos 5:** Dunn (Gethsemane, with Moule, Houlden, Caird) and Pao (Mark 14:38) " + L5,
}
t = load(f)
for q, txt in H.items():
    pats = [f"Pending Logos round 5 (Q{q})", f"pending Logos round 5 (Q{q})"]
    c = sum(t.count(p) for p in pats)
    if c != 1: errors.append(f'{f}: Q{q} count {c}'); continue
    for p in pats: t = t.replace(p, txt)
files[f] = t

if errors:
    print('NOT WRITTEN — errors:'); [print(' ', e) for e in errors]; sys.exit(1)
for f, t in files.items():
    open(f, 'w', encoding='utf-8').write(t)
print('written:', len(files)); [print(' ', f) for f in files]
