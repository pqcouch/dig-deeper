# How to run the card-transmission check

**What this is for.** A skill proposal card replaces a whole `SKILL.md` by retyping it. Twice now that has gone wrong silently — Round 3 lost a paragraph, Round 4 damaged three Hebrew words. So after any card is saved, the installed file is checked against the text that was intended. This folder holds everything needed to do that.

---

## The one thing that has to be true first

**It must be a genuinely new session.** The copy of the installed skill that Claude can read is a snapshot taken when the session starts, and it does **not** refresh part-way through. A card saved at 09:45 will still look unsaved to a session that began at 08:38 — which is exactly what happened on 19 September 2026.

So: save the card, then **start a new task** and ask for the check there. Running it in the same session that produced the card proves nothing.

---

## What Claude should do (paste this, or just say "run the Round 5 card check")

The two files live on the Mac, in this folder. The installed `SKILL.md` lives in Claude's cloud container. They have to be brought together, which is two steps:

**1. Stage both files from the folder into the container**

`mcp__remote-devices__device_stage_files` with:

- `…/Theology/Bible/dig-deeper/_skill-backup/check_card_transmission.py`
- `…/Theology/Bible/dig-deeper/_skill-backup/SKILL-dig-deeper-round-5-intended.md`

**2. Run it in the container against the installed skill**

```bash
python3 <staged check_card_transmission.py> \
        "$(ls /root/.claude/skills/synced/*/dig-deeper/SKILL.md)" \
        <staged SKILL-dig-deeper-round-5-intended.md>
```

Optionally add a third argument — the path to a `hebrew-wlc` directory — to check every Hebrew string against the corpus as well. That needs the corpus staged too, so it is usually not worth it; the stray-codepoint check is the one that catches the Round 4 failure and needs no corpus.

---

## Reading the result

| It says | It means |
|---|---|
| **BYTE-IDENTICAL** | The card transmitted the file exactly. Done — nothing else to check. |
| **CANONICALLY EQUAL under NFC** | The files differ only in the *order* of combining marks. This is the known, harmless difference: a card applies NFC, the WLC corpus does not. Renders identically, compares equal under NFD-stripping, chain verification unaffected. Treat as clean. |
| **NOT canonically equal** + changed lines | A real difference. Read the changed lines. If it is only line 144, that is the Round 5 gate item and the card has simply not been saved yet. Anything else is damage — fix with a second card. |
| **STRAY NON-HEBREW CODEPOINTS** | The Round 4 failure. An Arabic or other letter has replaced a Hebrew one. Fix with a second card. |
| **Hebrew present in one file and not the other** | If the missing string is וְרַב־וחסד, the card has not been saved. If anything else is missing, the card dropped it. |

Exit status 0 = clean, 1 = look at it.

---

## What is expected, once the card *has* been saved

The intended file differs from the pre-amendment file in **exactly one line — 144** — and adds **exactly one Hebrew string**, וְרַב־וחסד (which matches Neh 9:17 in the WLC character for character). Nothing else in 711 lines changes. So a clean result is either byte-identical or NFC-equivalent with no Hebrew findings.

---

## Files in this folder

| File | What it is |
|---|---|
| `check_card_transmission.py` | The check. Self-tested both ways on 19 Sep 2026. |
| `SKILL-dig-deeper-round-5-intended.md` | 88,269 bytes, 711 lines — what the card should have produced. |
| `SKILL-dig-deeper-2026-09-19-preamendment.md` | 86,496 bytes — what was installed before. |
| `SKILL-book-overview-round-5-intended.md` | The book-overview equivalent (delivered as a plugin, not a card, so the check is less critical). |
| `SKILL-book-overview-2026-09-19-preamendment.md` | Its pre-amendment copy. |
| `book-overview-0.2.1-round-5.plugin` | The packaged plugin as delivered. |

See `toolkit-amendments-round-5.md` at the folder root for what the amendments are and why.
