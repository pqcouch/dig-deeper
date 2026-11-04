#!/usr/bin/env python3
"""Round 5 follow-up (second paste, 4 Nov 2026). Same all-or-nothing rule as apply_round5.py."""
import sys, os
os.chdir(sys.argv[1])
errors, files = [], {}
def load(f):
    if f not in files: files[f] = open(f, encoding='utf-8').read()
    return files[f]
def rep(f, old, new):
    t = load(f); n = t.count(old)
    if n != 1: errors.append(f'{f}: rep count {n}: {old[:80]!r}'); return
    files[f] = t.replace(old, new)
def oq(f, prefix, add):
    lines = load(f).split('\n'); h = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    if len(h) != 1: errors.append(f'{f}: oq hits {len(h)}: {prefix!r}'); return
    lines[h[0]] = lines[h[0]].rstrip() + ' ' + add; files[f] = '\n'.join(lines)
def after(f, prefix, newline):
    lines = load(f).split('\n'); h = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    if len(h) != 1: errors.append(f'{f}: after hits {len(h)}: {prefix!r}'); return
    lines.insert(h[0] + 1, newline); files[f] = '\n'.join(lines)
D = 'dig-deeper-colossians-'
FU = '**Follow-up (pasted, 4 November)** `[S: Logos 5]`:'

# ---- 1:21-23
f = D + '1-21to23.md'
rep(f, "is a presentation before God, and", "is a presentation \"before him\" (God or Christ — see Difficult Verses; v1.1 follow-up), and")
oq(f, "- **What an honest exegesis surfaces:** 1:19–20 makes God",
   f"{FU} Dunn (NIGTC, 107): the thought \"reverts to … reconciliation through Christ to God … but here with Christ as subject\", as in Eph 2:16; Pao (ZECNT, 106–7): \"the implied subject … should be Christ himself\", the ambiguity perhaps intentional; Bird: Christ; Wright (TNTC): \"God has now reconciled you\". **This dig did not weigh Eph 2:16**, the only use of ἀποκαταλλάσσω outside Col 1:20, 22, where Christ is the subject (\"that he might reconcile both to God in one body through the cross\") `[T]`. The verb's two other uses divide as the commentators do. **God, moderate–high → open: God or Christ, moderate either way.** The suggested handling stands.")
rep(f, "The Assistant's two summaries of Dunn conflict (round 4: \"reverts to … through Christ to God\"; round 5: \"maintains Christ as subject\"); his p. 107 is needed. *God, moderate–high on the text; unchanged. Christ now has an owned holder.*",
       f"{FU} both summaries of Dunn were half right — he writes \"reverts to … through Christ to God\" *and* \"but here with Christ as subject\" (107, as Eph 2:16). Pao (106–7) also takes Christ; Wright takes God. ἀποκαταλλάσσω: Col 1:20 (God, through Christ), Col 1:22, Eph 2:16 (Christ) `[T]`. **God moderate–high → open: God or Christ, moderate either way.** \"Before him\": Christ for Pao and Bird. The NIV84 (\"by Christ's physical body\") has decided for God; the ESV and NASB95 leave it open `[T]`.")
oq(f, "1. **1:22, active or passive?**",
   f"{FU} Dunn (n. 1): the passive \"meets all the criteria to be counted as original\" (𝔓⁴⁶ B; it explains the others; the hardest), yet the early correction was \"wholly justified\". Pao (n. 120) rejects it because it cannot govern the infinitive; he notes that Metzger, Moo and Sumney take it as original. *Divided; unchanged.*")
rep(f, "the summary's further claim that he prefers the present is the Assistant's. *Eschatological, moderate–high; unchanged.*",
       f"{FU} Pao does take the present (108–9): \"as in Rom 12:1 … this progressive reading … is confirmed by the use of the same verb in v. 28\". Dunn (109–10): final — \"not yet … the final climax\", borne out by 1:23–24 (against Lightfoot, Lohse, Aletti). Wright: has / is / will, ending in the final presentation \"before God\". κατενώπιον: in Paul only Eph 1:4 and here; Jude 24, the only other NT use, is final `[T]`. *Eschatological, moderate–high; unchanged.*")
oq(f, "4. **εἴ γε**", f"{FU} Wright: \"This promise, like most, has a condition. The hope holds good, if Christians hold on to it\"; 1:23 \"almost certainly\" echoes 1:4–5.")
rep(f, "| Open Questions 2 (subject; \"before him\") | God, moderate–high | unchanged; Bird holds Christ; Dunn's summaries conflict (p. 107 needed) |",
       "| Open Questions 2; Difficult Verses; Headline 3 (subject; \"before him\") | God, moderate–high | **open: God or Christ, moderate either way** (follow-up: Dunn, Pao and Bird take Christ, Wright God; Eph 2:16 has Christ as subject of the same verb, which v1.0 had not weighed) |")
rep(f, "| Open Questions 3 (timing) | eschatological, moderate–high | unchanged; Bird for the final presentation; Pao's page needed |",
       "| Open Questions 3 (timing) | eschatological, moderate–high | unchanged; Dunn, Wright, Bird final; Pao present (follow-up, pasted) |")
rep(f, "**Library status:** owned and cited here — Dunn, Pao, Bird, Robertson (*Grammar*), the Cornerstone commentary (vol. 16), EDNT.\n\n**Headlines:** unchanged.",
       "**Library status:** owned and cited here — Dunn, Pao, Bird, Wright, Robertson (*Grammar*), the Cornerstone commentary (vol. 16), EDNT.\n\n**Headlines:** Headline 3 reworded (\"before him\", God or Christ); otherwise unchanged.")

# ---- 1:1-14
f = D + '1-1to14.md'
rep(f, "Dunn, Wright and Bird were not returned. NA28 punctuates",
       "Dunn and Bird were not returned; Wright (follow-up, pasted): \"it is impossible to tell … it makes little overall difference\". NA28 punctuates")
oq(f, "3. **1:7 ὑμῶν / ἡμῶν**", f"{FU} the *Lexham Textual Notes* print ὑπὲρ ἡμῶν as their text (\"attested by many early manuscripts\"), without argument. *Unchanged.*")

# ---- 1:15-20
f = D + '1-15to20.md'
after(f, "| Dunn's page for 1:20 |",
      "| Dwelling at 1:19 (follow-up) | — | Pao (101–2, pasted): κατοικέω evokes God's heavenly (1 Kgs 8:39, 43, 49; 2 Chr 6:30, 33, 39) and earthly (2 Chr 6:18, 21) dwelling — \"Christ fulfills the role of the temple\"; Ps 68 as a transfer of presence from Sinai to Zion to Christ (n. 92, with Beetham). References verified in Swete. Pao does not join 1:19 to 3:16 | Tool 11; Open Questions 4 |")

# ---- 3:5-11
f = D + '3-5to11.md'
oq(f, "1. **3:6 — the bracketed phrase.**",
   f"{FU} Wright (TNTC, n. 57) keeps the phrase: with it, ἐν οἷς (\"among whom\") and ἐν τούτοις (\"in these\") in 3:7 have different antecedents, which he prefers to making both refer back to δι᾽ ἅ. The *Lexham Textual Notes*: \"two very early manuscripts\" omit it; the majority includes it. *Divided; unchanged* — but Wright's is the best internal case for inclusion: with the phrase, 3:7 reads \"among whom you also once walked, when you lived in these things\", two referents and no redundancy `[I]`.")
rep(f, "so neither Wright nor Bird is confirmed.",
       "so neither was confirmed. **Follow-up (pasted):** Wright is causal after all — \"*since* you have taken off your old self … and have put on the new self\", the aorists marking \"actions that are unique and unrepeatable\", with baptismal imagery. Bird is still unconfirmed.")
rep(f, "| Open Questions 1 (3:6) | divided | unchanged; Pao leans to omission but brackets; the Vulgate and KJV include |",
       "| Open Questions 1 (3:6) | divided | unchanged; Pao leans to omission but brackets; the Vulgate and KJV include; Wright keeps it on an internal argument from 3:7 (follow-up) |")
rep(f, "| Open Questions 2 (3:9–10) | causal, moderate–high | unchanged; Wilson holds it (Wright and Bird misfiled by the Assistant); **the KJV is causal** |",
       "| Open Questions 2 (3:9–10) | causal, moderate–high | unchanged; Wilson and **Wright (pasted, follow-up)** hold it; Bird unconfirmed; **the KJV is causal** |")

# ---- 3:12-17
f = D + '3-12to17.md'
oq(f, "2. **The songs",
   f"{FU} Pao's pages give four grounds: Eph 5:19; 1 Cor 14:26; the instrumental datives; and the parallel ἐν … participle structure (BDF §491). He allows that the songs are also sung (\"To God, they are to sing these songs\"). His nn. 50–51 name the holders: with the singing — Harris, Lohse, Schweizer, Sumney; with the teaching — Lightfoot, O'Brien, Barth–Blanke, MacDonald, Callow, Moo. *Unchanged.*")
oq(f, "3. **ἐν [τῇ] χάριτι",
   f"{FU} Pao (249–50): \"with gratitude\" — the thanksgiving frame (vv. 15, 17) and Paul's χάρις for thanks (Rom 6:17; 7:25; 1 Cor 10:30; 15:57; 2 Cor 2:14; 8:16; 9:15; 2 Tim 1:3). \"Grace\" (KJV; Lightfoot) is stronger if the article is read, and the article has strong support — 𝔓⁴⁶ א² B D* F G Ψ 6 1505 1739, as in the NA28 apparatus `[T]`. The ESV and NASB95 have \"thankfulness\" `[T]`. *Open → slight lean to \"with thankfulness\", moderate.*")
after(f, "| Open Questions 2 (the songs) |",
      "| Open Questions 3 (ἐν [τῇ] χάριτι) | moderate, open | **slight lean to \"with thankfulness\", moderate** (Pao, pasted; follow-up) |")
after(f, "| Open Questions 3 (ἐν [τῇ] χάριτι) |",
      "| 3:16 ἐνοικείτω and the dwelling chain (follow-up) | — | Pao does not join 3:16 to 1:19 / 2:9. He compares Rom 8:11, 2 Cor 6:16 and 1 Cor 3:16 — two of them temple texts (2 Cor 6:16 has ἐνοικέω inside \"we are the temple of the living God\") `[T]`; the temple link at 3:16 is an inference `[I]`. Beale's *Temple*: no reference to 3:16. For claim audit 5 |")

# ---- 4:2-6
f = D + '4-2to6.md'
rep(f, "LSJ (owned) can test the non-biblical use with καιρός (\"time, opportunity\").",
       f"{FU} LSJ (580): \"buy up\" is a non-biblical sense (Plutarch, *Crassus* 2). The middle with τὸν καιρόν is cited only from Col 4:5 and Eph 5:16, \"but\" the active at Dan 2:8; both Greek texts of Dan 2:8 have ἐξαγοράζετε, and Col 4:5 the middle `[T]`. No non-biblical use of the phrase with καιρός is recorded.")
oq(f, "2. **Daniel 2 at 4:2–5 (C57)**", f"{FU} LSJ marks the change of voice (active in Daniel, middle in Paul). Dan 2:8 stays the only Greek precedent for the phrase, in another voice and another sense.")

# ---- 4:7-18
f = D + '4-7to18.md'
oq(f, "1. **4:8 variant**", f"{FU} the *Lexham Textual Notes* set out both readings, and add that unaccented ΓΝΩ can be \"he may know\" or \"I may know\" (the apparatus prints γνω) `[T]`. *Unchanged.*")
oq(f, "3. **συναιχμάλωτος**", f"{FU} Wright (TNTC): possibly metaphorical, \"but the literal meaning ('fellow-prisoner-of-war') suggests that he, too, is literally imprisoned\" — Wright leans literal, with Dunn. Mark's possible visit, with Phlm 22, shows a place of writing \"not too far distant from Colosse\".")
rep(f, "| Open Questions 3 (συναιχμάλωτος) | open | unchanged; Pao figurative, Dunn literal |",
       "| Open Questions 3 (συναιχμάλωτος) | open | unchanged; Pao figurative; Dunn and Wright (follow-up) literal |")

# ---- claim audit 4
f = D + 'claim-audit-4.md'
rep(f, "**Logos 5:** Osborne, Pao and Dunn cite Dan 2:8 ",
       "**Logos 5:** Osborne, Pao and Dunn cite Dan 2:8; LSJ records no non-biblical use of the phrase and marks the change of voice (active in Daniel, middle in Paul) ")

if errors:
    print('NOT WRITTEN — errors:'); [print(' ', e) for e in errors]; sys.exit(1)
for f, t in files.items(): open(f, 'w', encoding='utf-8').write(t)
print('written:', len(files)); [print(' ', f) for f in files]
