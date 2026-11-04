# Claim audit — brief for a blind auditor (Colossians, audit 5)

You are one of two blind auditors. You see only this brief, your claims file, and the primary-text corpus. You must NOT
look for or read any commentary, overview, earlier audit or dig report (there are none in your corpus; do not search the
web for the claims). Your job is to test each claim against the TEXT and against CHANCE, and to return a verdict.

## Corpus (read its README first)
  CORPUS = /tmp/claude-0/-home-claude/b5a67893-f6c6-5555-9284-66588bbdb75f/scratchpad/audit5/corpus/_texts
- greek-nt-sblgnt/  SBLGNT with a lemma index (use tools/find.py: `python3 tools/find.py glemma <lemma> [Book]`,
  `python3 tools/find.py show "Col 1:13"`). Book labels as the index has them: Col, Eph, Rom, 1Cor, 2Cor, Gal, Phil,
  1Thess, Phlm, Luke, Acts ...
- greek-lxx-swete/  Swete's LXX (Vaticanus-based), one verse per line "Ref<TAB>text". NO lemma index: search by
  accent-stripped stem (NFD, strip combining marks, lower-case) and READ every hit for sense (false friends are common:
  e.g. a stem can match a different word). Psalms are in Greek numbering (Ps 106 LXX = Ps 107 Hebrew/English).
- hebrew-wlc/  Westminster Leningrad Codex with lemma index (find.py lemma <Strong's no.>).
- logos-exports/  NA28 Colossians text + apparatus; Luke and Acts NA28; Rahlfs LXX of Psalms, Deuteronomy, Isaiah;
  BHS Psalms and Deuteronomy; NASB95 Colossians. Use these to CITE a reading; use the indexed layers to COUNT.
- tools/contacts.py  `python3 tools/contacts.py ntscan Col:1:12-14` ranks Swete chapters against an NT passage
  (six runs; quote a rank only if stable across runs; `--check "<chapter>"` lists the matched words — read them).
  Known blind spots of the scan: μεθίστημι, the aorists/futures of ῥύομαι (ἐρρύσατο, ῥύσεται), oblique cases of φῶς,
  δέω. Do not trust a scan nil for these words; search them directly.

## Rules (hard)
1. Count by LEMMA where an index exists, never by surface form or English gloss. Every count names its edition
   (SBLGNT / Swete / WLC / Rahlfs).
2. Before reporting any absence or "only", run a POSITIVE CONTROL: the same search must return a verse you know contains
   the item. Report the control.
3. In Swete, read every stem hit for sense before counting it.
4. Accent-insensitive matching always; for phrases also normalise elision marks and punctuation.
5. A "design", "field", "frame" or "chain" claim must face a CHANCE BASELINE: compare the observed figure with the same
   measure taken at many other places (random passages of the same length in Paul's letters, or random cut points
   in Colossians). Report the baseline as a proportion ("X of N comparison passages do as well").
6. Distinguish: (a) Paul's own idiom elsewhere in his letters (which can explain a contact without any external
   source), (b) shared early-Christian idiom, (c) a specific source text.
7. Give original-language words in their own script with an English gloss in brackets EVERY time.
8. Write your REPORT IN PROSE AND TABLES ONLY: no code, no command lines, no script or file names, no Strong's
   numbers. State searches in words ("ῥύομαι ('rescue') + λυτρόω ('redeem') within twelve verses: Luke 1:68-74 only
   (SBLGNT)").
9. British English.

## Per claim, report
- The claim (one line), your reading of the evidence, the counts (with edition) and controls.
- A Hays table with rows: Availability · Volume · Recurrence · Thematic coherence · Historical plausibility ·
  Satisfaction — each Strong / Possible / Weak with one line of reasons. (History of interpretation is supplied by the
  main session; omit it.)
- Verdict: Confirmed / Confirmed with nuance / Needs reframing / Uncertain — flag for research / Discard.
- Recommended confidence (high / moderate–high / moderate / low–moderate / low) and one line saying what, if
  anything, should change in how the claim is stated.
- Any NEW candidate you met in passing (one line each, with suggested rating) — record only.

End with a short "What I could not test" list and a "Spot checks" list (prose sentences a reader could re-check).

Write the report to the file named in your claims file. Aim for about 3,000–5,000 words. Then reply with a 10-line
summary of verdicts.
