# `_skill-examples/` — the current worked examples and changelog for `dig-deeper`

Three files here stand in for parts of the skill's reference tree that a proposal card cannot reach.

**Why they live here.** Round 4 of the September 2026 review rewrote both worked examples so that Hebrew and Greek appear in their own script with an English gloss, per Amendment S. A skill proposal card can replace `SKILL.md` but cannot reach a skill's `examples/` or `references/` folders, and the packaged `.skill` route was unavailable. So the revised anchors live in the connected prep folder, where a run can read them, and `SKILL.md`'s Required Reading points here.

| File | Supersedes | Status |
|---|---|---|
| `psalm-33-worked.md` | `examples/psalm-33-worked.md` in the skill | Current — OT calibration anchor |
| `romans-8-31to39-worked.md` | `examples/romans-8-31to39-worked.md` | Current — NT calibration anchor |
| `CHANGELOG.md` | `references/CHANGELOG.md` in the skill | Current — the installed copy stops at Round 2 |

**What changed in the examples, beyond the script.** Checking every word against the corpus turned up three things:

- `psalm-33-worked.md` — its second Headline Finding claimed כֹּל ("all") appears **five** times in Ps 33:1–9. It appears **four**. The fifth was "the earth is **full**" at v.5, where מָלְאָה הָאָרֶץ contains no כֹּל at all: the count had been made in English. The correction is written into the example as its own demonstration of gate item (e3).
- An open question was **closed**: נֵד ("heap") stands in six verses of the Hebrew Bible — Exod 15:8; Josh 3:13, 16; Isa 17:11; Ps 33:7; Ps 78:13 — and the Psalter's second occurrence falls in exactly the exodus-rehearsal psalm the Move 2 note had guessed at.
- `romans-8-31to39-worked.md` — ὑπερνικάω verified as standing **once in the New Testament**, and χωρίζω twice in Romans, both inside this passage.

Psalm 33 also gains the Text-First Declaration it predated, and both gain the header block (primary texts, study text, pulpit text N/A).

**The changelog.** The installed skill's own `references/CHANGELOG.md` ends at Round 2, so the Round 3 (Amendments K–N, plus G off trial) and Round 4 (Amendment S) entries are missing from it. `CHANGELOG.md` here is the whole record, Rounds 1–4. It is provenance only — no phase loads it — so nothing in a run depends on which copy is read; but a future round should be written against this one.

**If the reference tree is ever replaced** — by a `.skill` install that carries these files — this folder becomes redundant: the Required Reading pointer goes back to `examples/`, and this changelog is copied over the installed one. Until then, these three are the live versions.

*The packaged version is `dig-deeper.skill`, built 13 September 2026 from the post-Round-3 `SKILL.md`. It carries all three of these files but its install card has not been visible.*
