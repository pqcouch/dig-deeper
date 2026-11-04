#!/usr/bin/env python3
"""Apply claim audit 5 (4 Nov 2026) to the Colossians digs. All-or-nothing."""
import re, sys, os
os.chdir(sys.argv[1])
errors, files = [], {}
def load(f):
    if f not in files: files[f] = open(f, encoding='utf-8').read()
    return files[f]
def bump(f):
    t = load(f); m = re.search(r'\*\*Version:\*\* (\d+)\.(\d+)( \(|\\)', t)
    if not m: errors.append(f'{f}: no version'); return None
    new = f"{m.group(1)}.{int(m.group(2))+1}"
    if m.group(3) == '\\':
        rep_ = f"**Version:** {new} (4 November 2026: claim audit 5 applied — see *Claim audit 5 (v{new})*; earlier: v{m.group(1)}.{m.group(2)})\\"
    else:
        rep_ = f"**Version:** {new} (4 November 2026: claim audit 5 applied — see *Claim audit 5 (v{new})*; earlier: "
    files[f] = t[:m.start()] + rep_ + t[m.end():]
    return new
def oq(f, prefix, add):
    lines = load(f).split('\n'); h = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    if len(h) != 1: errors.append(f'{f}: hits {len(h)}: {prefix!r}'); return
    lines[h[0]] = lines[h[0]].rstrip() + ' ' + add; files[f] = '\n'.join(lines)
def tail(f, text):
    files[f] = load(f).rstrip('\n') + '\n\n---\n\n' + text.strip('\n') + '\n'
SRC = ("*Source: `Colossians/dig-deeper-colossians-claim-audit-5.md` (two blind auditors; results reproduced in the main "
       "session). This section governs the paragraphs above where they differ. Tag `[S: audit 5]`.*")
D = 'dig-deeper-colossians-'
A5 = '`[S: audit 5]`'

f = D + '1-1to14.md'; v = bump(f)
oq(f, '4. **The passage does not end at 1:14',
   f'**v{v} (claim audit 5)** {A5}: the shift is confirmed in the critical text, and the inclusive "we" occurs in Colossians only here and at 2:13–14 (both auditors, independently). But the move is Paul\'s habit when stating the saving act (1 Thess 1:9–10; Gal 1:3–4; Eph 2:1–5), it does not recur at the third forgiveness statement (3:13), and the NASB95 levels it at 1:12 ("qualified us"). Read it as Pauline confessional idiom, not a design peculiar to Colossians (*low–moderate* as design; *high* on the pronouns).')
tail(f, f"""## Claim audit 5 (v{v})

{SRC}

| Item | Before | After |
|---|---|---|
| Headline 4, "you" → "us" (C67) | moderate–high as design | pronouns **high**; inclusive "we" only at 1:13–14 and 2:13–14 **moderate–high**; Colossian design **low–moderate** (Paul's habit; not at 3:13) |
| Ps 106 LXX (C61) | low–moderate (queued) | **low**, as "redeemed from darkness" idiom shared with Luke 1:74–79; Isa 42:7, 16 an equal partner |
| Deut 9:26–29 (C62) | moderate (queued) | **low–moderate**; the receiving formula μερὶς καὶ κλῆρος ("portion and lot", Deut 10:9; Acts 8:21 — the only other NT verse with both words) explains 1:12 better |
| Luke 1:68–79 (C63) | moderate | **moderate**, as idiom; the rescue + redeem pair alone is within chance; rare only with forgiveness and darkness |
| Lukan affinities (C69) | moderate | **moderate–high for 1:12–14** (Acts 26:18; Luke 22:53, "the authority of darkness", the only other NT use; Acts 8:21); **low for the letter** (Colossians is the least Lukan of the thirteen Pauline letters overall); Luke 8:15 → shared sower tradition |
| Exodus pattern (C70), Headline 5 | four texts, moderate | **moderate, anchored in Exod 6:6–8** (rescue + redeem + lot); Ps 106 removed; ῥύομαι ("rescue") alone is not an exodus marker in Swete |
| Instrument | — | the scan is nearly blind at 1:12–14 (ἐρρύσατο, μεθίστημι, ἀπολύτρωσις/λυτρόω unlinked; a false "forgiveness" at Isa 59); ranks for this passage should not be quoted |

**Candidates queued by the audit (C73–C76):** Luke 22:53; the "portion and lot" formula; the darkness plague (Exod 10:23; Wis 18:1–9); Esther Addition C.

**Headlines:** Headline 4 qualified (above); Headline 5's texts renamed; ratings otherwise unchanged. Trigger 2 for point-purpose on 1:1–14 is cleared by this patch.""")

f = D + '1-15to20.md'; v = bump(f)
tail(f, f"""## What Changed in v{v} — Claim audit 5 (v{v})

{SRC}

| Item | Before | After | Where |
|---|---|---|---|
| Ps 68:16 (67:17 LXX) at 1:19 | confirmed with nuance (audit 1) | **moderate–high**: Ps 67:17 is the only verse in Swete where εὐδοκέω ("be pleased") and κατοικέω ("dwell") have God as subject together (C72) | Tool 11; Open Questions 4 |
| The dwelling chain (1:19; 2:9; 3:16) | near the gate, read as a temple thread | 1:19/2:9 **high** as one formula; temple overtone **moderate** (κατοικέω has God as subject in about 3 % of its Swete uses); 3:16 as temple **low** — an **indwelling** thread (cf. Eph 3:17), not a temple thread | Tool 11 |

**Headlines:** unchanged.""")

f = D + '1-24to2-5.md'; v = bump(f)
tail(f, f"""## What Changed in v{v} — Claim audit 5 (v{v})

{SRC}

| Item | Before | After | Where |
|---|---|---|---|
| The frame with 4:2–18 (C65; Headline 4; Open Questions 14) | moderate | **moderate, restated**: 4:2–13 picks up 1:25–2:7 — eight rarer lemmas shared; 1.7 % of window pairs in Colossians do as well (lemmas in at most 50 NT verses); the strongest closing link of twelve Pauline letters. θέλημα ("will") in 4:12 comes from 1:9, not from this unit. The Romans comparison holds only thematically | Headline 4; Open Questions 14 |
| μυστήριον + φανερόω ("mystery" + "make manifest") within two verses | — | only Col 1:26–27; 4:3–4; 1 Tim 3:16 (SBLGNT) — the frame's sharpest strand (C77, queued) | Tool 10 |
| 1:23 → 1:25 ("of which I became a minister") | strong | **high**, confirmed; the strong welds are distance echoes, not seams (C71) | Move 4 |

**Headlines:** Headline 4 stands at moderate, with the restatement above.""")

f = D + '2-6to15.md'; v = bump(f)
tail(f, f"""## What Changed in v{v} — Claim audit 5 (v{v})

{SRC}

| Item | Before | After | Where |
|---|---|---|---|
| 2:13, "you … us" (C67) | design reading | the inclusive "we" occurs in Colossians only at 1:13–14 and 2:13–14; the move is Paul's habit (Eph 2:1–5 is the twin) — **low–moderate** as Colossian design; the KJV and the majority level it | Original Languages; Tool 8 |
| 2:15 → 3:9, ἀπεκδύομαι ("strip off") | internal echo | NT only Col 2:15 and 3:9 (with ἀπέκδυσις at 2:11): a **distance echo**, which audit 5 finds is the letter's real linking device | Move 4 |
| 2:5 → 2:6–7 weld | walk, Lord, learned, faith | corrected: walk and Lord pair at 1:10 and 2:6; "learned" is 1:7; the weld to 2:5 is πίστις ("faith") alone | Tool 2 |

**Headlines:** unchanged.""")

f = D + '3-5to11.md'; v = bump(f)
tail(f, f"""## Claim audit 5 (v{v})

{SRC}

| Item | Before | After |
|---|---|---|
| The speech chain begins here (C68) | λόγος chain from 3:8–9 | λόγος ("word") is **absent from 3:8–9**; the first link is carried by βλασφημία ("slander"), αἰσχρολογία ("obscene talk"), "from your mouth" and ψεύδομαι ("lie"). The thread stands at moderate as a speech-word cluster |
| 3:10 → 3:12, ἐνδύω ("put on") | weld | confirmed; ordinary Pauline clothing idiom |

**Headlines:** unchanged.""")

f = D + '3-12to17.md'; v = bump(f)
tail(f, f"""## Claim audit 5 (v{v})

{SRC}

| Item | Before | After |
|---|---|---|
| 3:12–17 as the summary of church life (C66) | moderate | **low** as "draws on more of the letter than any other unit" (it ranks 5th–7th of twelve; 1:24–2:5 and 2:6–15 reach further); **moderate** reframed: it gathers the opening prayer, Paul's ministry, the forgiveness of 2:13, the polemic and the putting-off, and is the last lexically integrated unit before the household code, which shares no rarer lemma with any other unit. **It does not reach 1:15–20** |
| ταπεινοφροσύνη ("humility") and σύνδεσμος ("bond") | — | condemned or used in the polemic (2:18, 23; 2:19) and commended here (3:12, 14): a deliberate re-valuation (C78, queued, moderate–high) |
| ἐν χάριτι (3:16; 4:6) | — | the speech thread's most specific link (seven NT verses). If 3:16 is "with thankfulness" (v1.2) and 4:6 "gracious", the link is a play on χάρις, not one sense carried through `[I]` |
| 3:16 and the dwelling chain (C72) | candidate temple thread | **low** as temple: ἐνοικέω ("dwell in") is never used of God in Swete, and 3:16 has no temple vocabulary. An **indwelling** thread with 1:19 and 2:9 (cf. Eph 3:17) |

**Headlines:** unchanged.""")

f = D + '4-2to6.md'; v = bump(f)
tail(f, f"""## Claim audit 5 (v{v})

{SRC}

| Item | Before | After |
|---|---|---|
| The speech chain (C68) | high on words, moderate as design | unchanged in rating, **restated**: a speech-word cluster (3:8–9 → 3:16–17 → 4:3–4 → 4:6), with ἐν χάριτι (3:16; 4:6) its sharpest link; λόγος changes sense along it; 3:16–4:6 is denser in λόγος than about 96 % of 24-verse Pauline stretches, but Colossians as a whole runs at twice the Pauline rate; **Eph 4:29–6:20 has the same sequence**, so it is Paul's paraenetic pattern |
| δεῖ ("must"), 4:4 and 4:6 | only two uses | confirmed **by form**; the lemma index files δεῖ under δέω with δέδεμαι ("I am bound", 4:3) — count by form |
| μυστήριον + φανερόω (4:3–4) | — | with 1:26–27 the frame's sharpest strand (C77, queued) |

**Headlines:** unchanged.""")

f = D + '4-7to18.md'; v = bump(f)
tail(f, f"""## Claim audit 5 (v{v})

{SRC}

| Item | Before | After |
|---|---|---|
| The frame (C65) | moderate | **moderate, restated**: the shared vocabulary lies in 4:2–13; the greetings of 4:14–18 add nothing; 4:12 echoes 1:9 as strongly as 1:28–2:2 |
| 3:22–4:1 → 4:9, "the slave addressed, then named" (C71) | weld | **corrected**: Colossians never calls Onesimus a slave (4:9: "the faithful and beloved brother, who is one of you"); the link needs Philemon. Inside the letter δοῦλος ("slave") passes to Epaphras (4:12) |
| Luke at 4:14 and the setting (C69) | Lukan affinities, moderate | the Lukan idiom is confined to 1:12–14 (moderate–high); across the letter Colossians is the least Lukan of the thirteen Pauline letters |

**Headlines:** unchanged.""")

if errors:
    print('NOT WRITTEN'); [print(' ', e) for e in errors]; sys.exit(1)
for f, t in files.items(): open(f, 'w', encoding='utf-8').write(t)
print('written', len(files))
