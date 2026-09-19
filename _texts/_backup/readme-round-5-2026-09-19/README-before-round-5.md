# `_texts/` — the primary-text corpus

**Built:** 2 September 2026 · **Purpose:** to make the substrate of every dig-deeper
run local, reproducible and searchable, so that no run depends on a text being
pasted in, and so that any claimed lexical chain can be checked mechanically
before it reaches an overview.

The rule this corpus exists to serve, in the words the Exodus claim audit
settled on: **research tools are for the state of a scholarly question;
primary texts are for the data. Do not ask a search engine what a verse says.**

---

## What is here, and what each layer is *not*

| Layer | Edition | Use it for | Do **not** use it for |
|---|---|---|---|
| `hebrew-wlc/` | Westminster Leningrad Codex (Open Scriptures / morphhb) | The Hebrew substrate: reading, counting, root and Leitwort work, petuchot/setumot | Citing *BHS* as such. It is the same manuscript BHS prints (Leningrad B19a), but not BHS's apparatus or editorial decisions |
| `greek-lxx-swete/` | Swete, *The Old Testament in Greek* (1909–30) | Reading and searching the Greek OT; whole-canon word searches | Citing *Rahlfs* or *Rahlfs-Hanhart*. Swete is Vaticanus-based and diverges from Rahlfs in real places |
| `greek-nt-sblgnt/` | SBLGNT with MorphGNT parsing | The Greek NT substrate: reading, counting, lemma work | Citing *NA28*. No apparatus; the SBLGNT omits 5:4 and brackets 7:53–8:11 in John, and text-critical decisions differ from NA28 in a few dozen places |
| `logos-exports/` | Your own Logos exports — BHS, Rahlfs-Hanhart LXX, NASB95, ESV, NIV84, NA28, and whatever else you upload. Laid out book-first in the Tanak sections; see below | **Citation of record**, wherever a reading is load-bearing | Whole-canon searching — coverage is only what has been exported so far |

**The honest summary.** Three of these four layers are *proxies*. They are the
right tool for finding, counting and checking; they are the wrong tool for
citing. When a finding turns on a particular reading — a variant, an apparatus
question, a Rahlfs-vs-Swete divergence, an NA28 decision — go to Logos and cite
that. **Every count or chain in a report should name the edition it came from.**

## Observe versus cite

The distinction that governs everything else here. **Observe from the corpus; cite from
Logos.** They are different acts and they want different editions.

**Observation** is reading, counting, searching, checking a chain, seeing whether a root
recurs. It needs breadth and reproducibility, and the corpus gives both: the whole canon,
locally, lemma-indexed, re-checkable in a single command months later.

**Citation** is the moment a finding rests on a particular reading — a variant, an
apparatus question, a divergence between editions, a claim about what "the LXX" says.
There the corpus is not enough, because three of its four layers are proxies. Go to
Logos and name the edition you cite.

### Why Swete here, and Rahlfs there

Not an accident of licensing, though the licence decided it. The two editions do
different jobs:

| | Kind | What it shows you |
|---|---|---|
| **Swete** (1909–30) | **Diplomatic** — prints Codex Vaticanus, filling gaps from Sinaiticus and Alexandrinus | What a scribe actually wrote |
| **Rahlfs / Rahlfs-Hanhart** | **Eclectic** — a reconstruction of the earliest recoverable Greek | What an editor concluded |
| **Göttingen** | Fully critical, book by book, still incomplete | The scholarly best account, where it exists |

For a method that exists because *editorial interpretation may skew a text-focussed
reading*, the diplomatic edition is the right observation layer: it shows a manuscript
rather than a judgement. Rahlfs has already made choices on your behalf — well made, but
made.

The honest counterweight: a diplomatic text carries its manuscript's own slips, and in
Judges, Vaticanus represents a distinctly different recension. Closer to a scribe is not
automatically closer to the original. Both editions are interpretations; they are
different *kinds* of interpretation, and the discipline is knowing which you are looking
at.

**There is in any case no single Septuagint**, and the corpus shows it rather than hiding
it. Judges has two texts. So do Daniel, Susanna, Bel and Tobit — and the Swete layer
holds each pair side by side (`Daniel-OG` / `Daniel-Theodotion`, `Tobit-BA` /
`Tobit-Sinaiticus`) because Swete printed them side by side. Jeremiah's Greek is about an
eighth shorter than the Hebrew, on a different *Vorlage*; Job's is about a sixth shorter.
An eclectic text would have handed you one reading where the evidence offers two.

**So: Swete to observe, Rahlfs to cite, Göttingen where it exists and something turns on
it.** When a commentary says "the LXX", it means Rahlfs-Hanhart — which is why the Logos
exports are the citation of record and this layer is not.

## What still has to come from Logos

- **BHS** — apparatus, Masorah, editorial notes
- **Rahlfs-Hanhart LXX** — the critical text and apparatus
- **NA28 / UBS5** — the Greek NT apparatus
- **ESV** — no redistributable bulk text; export per book as needed
- **NASB95** — the study text. Lockman copyright, no redistributable source; export per book as needed

`logos-exports/` is where those go, and since **13 September 2026** it is laid out
**book-first**, in the same Tanak skeleton as `hebrew-wlc/`:

```
logos-exports/
├── 01-Old-Testament/
│   ├── 01-Torah/
│   ├── 02-Neviim/01-Former/
│   ├── 02-Neviim/02-Latter/   (04-The-Twelve/ nested beneath)
│   └── 03-Ketuvim/
└── 02-New-Testament/          flat, as `greek-nt-sblgnt/` is
```

**Filename: `NN-Book-VERSION.txt`** — `01-Genesis-BHS.txt`, `02-Jeremiah-LXX.txt`,
`05-Acts-NA28-apparatus.txt`. The number is the book's position in its section,
matching `hebrew-wlc/` exactly, including the a/b suffixes where a version splits
a book the Hebrew canon counts as one (the WLC's `03a-1-Samuel.txt` beside
the export `03-Samuel-BHS.txt`; every Logos export and NIV84 file holds the
whole book in one file). Book first means every version of a book sits together and
the books stand in canonical order — which is the arrangement the work actually
wants, since a dig opens four versions of one book rather than eleven books of one
version.

**Keep the version in the filename**, and **name the edition, not just the
version:** the NASB95 and the 2020 revision are substantially different texts, and
a file called `04-Ruth-NASB.txt` will be ambiguous within a year. Logos exports
arrive named `NASB95 Ruth.txt`, so filing a new one means a rename into this shape.

**The sections are a finding aid, not a claim.** Torah / Nevi'im / Ketuvim is the
*Hebrew* canon's architecture. Swete's LXX has its own — ordered by genre, and
carrying books the Tanak does not — and the NIV84 and ESV follow the Christian
order. Filing every version into the Hebrew sections makes them findable together;
it says nothing about how any of those collections orders itself.

Logos caps a single export at 100 pages, so a long book comes in parts; that split
is an export artefact and means nothing.

---

## Directory map

```
_texts/
├── README.md                  this file
├── hebrew-wlc/                BHS printed order (Torah / Nevi'im / Ketuvim)
│   ├── 01-Torah/
│   ├── 02-Neviim/01-Former/
│   ├── 02-Neviim/02-Latter/   (04-The-Twelve/ nested beneath)
│   ├── 03-Ketuvim/
│   └── _index/                word-level TSV, mirroring the same tree
├── greek-lxx-swete/           60 books, in the LXX's own order
├── greek-nt-sblgnt/
│   └── _index/                word-level TSV
├── logos-exports/             your BHS / LXX / ESV / NASB95 / NIV84 / NA28 exports
│   ├── 01-Old-Testament/      Tanak sections, as above; files NN-Book-VERSION.txt
│   └── 02-New-Testament/      flat
├── source/                    unmodified downloads (for reproducibility)
└── tools/                     build and search scripts
```

### On the order of the Hebrew books

The OT is laid out in **Tanak order**, because canonical position is part of
the evidence: Ruth stands in the Ketuvim among the Megilloth, not after Judges;
Daniel is in the Writings, not among the Prophets; Chronicles closes the canon.

One editorial decision, stated plainly: **the Ketuvim here begin with Psalms
and end with Chronicles, which is the order BHS prints — not the order of
Codex Leningradensis itself**, where Chronicles stands *first* among the
Writings. BHS departs from its own base manuscript at this point. The reading
that "Chronicles closes the Hebrew canon" rests on the BHS/Talmudic sequence,
not on L. If that point ever becomes load-bearing in a report, say which
sequence it depends on.

Samuel, Kings, Chronicles and Ezra–Nehemiah are **one book each** in the Hebrew
tradition. They are stored as two files apiece (`03a-`/`03b-` and so on)
because the source splits them; the pairing is in the numbering.

The Twelve are in **MT order**. The LXX orders them differently
(Hosea, Amos, Micah, Joel, Obadiah, Jonah…), and `greek-lxx-swete/` preserves
that — the divergence is itself a datum.

---

## Versification — a trap worth knowing about

**This corpus uses Hebrew versification. The reports use English.** They differ in
real places, and the difference will manufacture false failures in any automated
check that does not map between them:

| English | Hebrew | |
|---|---|---|
| Isaiah 64:8 | Isaiah 64:7 | "we are the clay, you are our potter" |
| Jeremiah 9:24 | Jeremiah 9:23 | "let him who boasts boast in this" |
| Exodus 22:16 | Exodus 22:15 | the seduction law |
| Joel 2:28–32 | Joel 3:1–5 | whole chapters offset |
| Malachi 4:1–6 | Malachi 3:19–24 | the Hebrew has three chapters |

Psalms with superscriptions are offset by one throughout wherever the
superscription is counted as verse 1, which in the Hebrew it is.

Before reporting a reference as missing a word, **check the neighbouring verse.**
The OT chain audit of 2 September found five apparent failures that were nothing
but this.

## File formats

**Reading text** — one verse per line, tab-separated:

```
Gen 1:1	בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃
```

Maqqef binds the words either side into one accent unit; paseq (׀), petuchah
and setumah stand as their own tokens — the Masoretic paragraph divisions no
English version carries.

**Word index** (`_index/*.tsv`) — one word per line:

```
ref	word	lemma	morph
Exod 40:35	הַ/מִּשְׁכָּֽן	d/4908	HTd/Ncmsa
```

Hebrew lemmas are Strong's numbers, prefixed morphemes separated by `/`
(`c/1961` = conjunction + *hayah*). Greek NT lemmas are the lexical form.
**Search the lemma column, not the pointed surface form** — pointing, prefixes
and suffixes make surface search unreliable, which is exactly how a chain gets
claimed at a verse that does not contain the word.

### Chapter markers in the Logos exports — seven conventions, no two alike

`logos-exports/` is not one format. Each version exports chapter and verse
differently, and a pattern that works on one file reports a sound file as broken
on another. It did: in the Hezekiah synoptic run of 11 September 2026 a
case-sensitive search declared a good export missing.

| Export | Chapter marker | Verse form |
|---|---|---|
| BHS | none — the chapter number prefixes verse 1 only (`1 1 <text>`) | bare number |
| ESV | **two layouts.** Some files (Genesis, Isaiah and Jeremiah among them): the first verse of each chapter carries `c:v` (`2:1`), the book's very first reads `Ge 1:1`. The rest: the chapter number stands in place of verse 1 (`2 The LORD spoke…`), as in a printed Bible | bare number, followed by a no-break space |
| NASB95 (prose) | `Chapter NN` — **title case** | bare number |
| NASB95 Psalms | `PSALM N`, under `BOOK 1`–`BOOK 5` division headings | bare number |
| LXX (Rahlfs 1979 via Logos — *not* Swete) | `CHAPTER NN` — **upper case** | bare number |
| NIV84 | none — every line is `c:v` + tab + text | `c:v` |
| NA28 | none — the chapter number stands in place of verse 1, often with a leading `*` (`*5 Μετὰ ταῦτα`); verse numbers and apparatus sigla run inline | inline, followed by a no-break space |

**Match case-insensitively, and confirm the marker in the file in front of you
before scripting against it.** The split is by version, not by book: every
NASB95 export uses `Chapter`, Kings included, and every LXX export uses
`CHAPTER`.

---

## Using it

```
python3 tools/find.py lemma 7931              every OT verse with shakan
python3 tools/find.py lemma 7931 Exodus       ... within one book
python3 tools/find.py verify 7931 Exod:40:34 Exod:40:35
python3 tools/find.py glemma λόγος John       Greek NT lemma
python3 tools/find.py show "Gen 1:1"          the verse in every layer
```

`verify` exits non-zero if any claimed reference fails, so it can gate a
script. It is the mechanical form of the discipline the Jonah and Exodus claim
audits arrived at independently: **re-verify every claimed chain against the
text before it reaches an overview.**

Worked example — the error the Exodus audit found by hand:

```
$ python3 tools/find.py verify 7931 Exod:40:34 Exod:40:35
FAIL Exod 40:34
OK   Exod 40:35
```

*šākan* is at 40:35. At 40:34 there is only the noun *miškān* (4908). The
descent-spine chain had been extended by inference into a verse that does not
contain the word — the failure mode named in the Jonah audit, and now caught
in one line.

---

## Rebuilding

```
python3 tools/build_hebrew.py     # from source/wlc-osis
python3 tools/build_greek.py      # from source/swete-lxx and source/sblgnt-morph
```

`source/` holds the unmodified downloads. Nothing in the generated layers is
edited by hand; if something is wrong, fix the build script and re-run, so the
corpus stays reproducible.

## Provenance and licences

- **WLC** — Open Scriptures Hebrew Bible (`openscriptures/morphhb`), CC BY 4.0.
  Text of Codex Leningradensis with morphology.
- **Swete LXX** — `eliranwong/LXX-Swete-1930`, compiled from the public-domain
  Swete volumes (archive.org). Public-domain source text.
- **SBLGNT / MorphGNT** — `morphgnt/sblgnt`. SBLGNT © Logos Bible Software and
  the Society of Biblical Literature; MorphGNT parsing CC BY-SA.
- **Rahlfs 1935** is deliberately *not* here. Every free machine-readable
  Rahlfs descends from CCAT/CATSS at Penn, whose licence asks the user to send
  a declaration before downloading. Rahlfs-Hanhart comes from Logos instead.

The doublets in the LXX layer — `Daniel-OG` / `Daniel-Theodotion`,
`Susanna-OG` / `Susanna-Theodotion`, `Bel-…-OG` / `Bel-…-Theodotion`,
`Tobit-BA` / `Tobit-Sinaiticus` — are Swete's parallel texts. The
OG/Theodotion labelling follows the source's own naming pattern and has **not**
been verified against Swete's printed volumes; check before relying on it.

## Verification carried out at build

| Check | Result |
|---|---|
| Hebrew verse total | 23,213 — the standard BHS figure |
| Hebrew word total | 305,507 |
| Leviticus verses | 859 — matches the count made independently for `book-overview-leviticus` |
| Jeremiah verses | 1,364 — matches the count made independently for `book-overview-jeremiah` |
| John verses (SBLGNT) | 866 — matches the count made independently for `book-overview-john` |
| Ruth, Hebrew vs Swete | 85 verses each |
| Proverbs, Hebrew vs Swete | 915 vs 902 — consistent with `proverbs-lxx-pluses-survey` |
| Pointing, maqqef, paseq, sof pasuq | intact (Deut 6:4, Gen 1:1, Ruth 4:22 inspected) |
| Chain-verification gate | reproduces the Exodus audit's *šākan* correction, exit status 1 |

---

## Audit of `logos-exports/`, 16 September 2026

All 345 files were checked for names, encoding, edition stamps and verse coverage:
BHS against WLC, NA28 against SBLGNT, and ESV and NASB95 against NIV84. The LXX files
and both apparatus layers were checked for chapter coverage. A copy of every changed
file, and of this README before the change, is in `_backup/logos-exports-2026-09-16/`.

### Tidied

- **Lemma tags removed: 4,991 of them, from 53 files.** A Logos visual filter had written
  transliterated Hebrew lemmas into the text after the words they tag: `(erets)` ×3,022,
  `(adam)` ×831, `(davar)` ×300, `(adama)`, `(shamar)`, `(mishphat)`, `(torah)`,
  `(mitsvah)`, `(yachal)`, `(hoq)`, `(eduth)`, `(hevel)`, `(savar)`, `(chakah)` and
  `(imrah)`. The affected files were ESV, NASB95, LXX and BHS files, *including the
  Greek and the Hebrew*. The tags broke phrase searches. **Switch that filter off before
  the next export.** The NIV84 footnote "man (adam)" at Gen 2:7 is genuine and stays.
- **Non-scripture introductions removed** from ESV Exodus, Numbers, Deuteronomy and 2 Kings
  (one "Introduction" heading and paragraph each).
- **Renamed:** `02-Judges-NABS95` → `NASB95`; `11-Phiippians-*` → `11-Philippians-*` (×2);
  `05-Romans-{ESV,NA28,NASB95}` → `06-Romans-*`; `06-1-Corinthians-NA28-apparatus` → `07-`;
  `07-2-Corinthians-NA28-apparatus` → `08-`.
- **`01-Matthew-NA28-apparatus.txt` → `01-Matthew-SBLGNT-apparatus.txt`.** Its colophon is
  Holmes, *Apparatus for the Greek New Testament: SBL Edition* (2010), not NA28.
- **Other mechanical fixes:** Genesis ESV converted from CRLF to LF line endings; John 1:7 in
  the ESV had its verse number run into the text (`7He`), now separated; missing `CHAPTER`
  headings added to Deuteronomy 6 and Joshua 1 in the LXX (the text was present); and 14
  spurious `n:0 Psalm n` lines removed from the NIV84 Psalms, a leftover from the PDF
  conversion.

### Still to re-export from Logos (updated 16 September 2026, second pass)

| File | Status |
|---|---|
| `03-Ketuvim/11-Chronicles-BHS.txt` | **Fixed.** Re-exported with both volumes; all 1,765 verses match the WLC |
| `03-Ketuvim/09-Daniel-LXX.txt` | **Complete for the Old Greek only**, chapters 1–12 in Rahlfs' numbering (3:24–90 included; the OG's own gaps in chs 4–5 are genuine). **Theodotion is not in the file**, and neither are Susanna or Bel, which Rahlfs prints as separate books. If Theodotion is wanted, export it separately as `09-Daniel-LXX-Theodotion` |
| `04-The-Twelve/08-Habakkuk-BHS-App.{rtf,pdf,txt}` | **Fixed.** Complete, Cp 1–3 (notes 1:3 to 3:19), checked against the rendered PDF pages. The `.txt` is converted from the **RTF** export; the old chapter-1-only text export is in `_backup/…/third-pass/` |
| `02-New-Testament/01-Matthew-NA28-apparatus.txt` | **Fixed.** Decoded from three PDF parts (chs 1–10, 11–20, 21–28); every chapter, 1–28, is present |
| `02-New-Testament/02-Mark-NA28-apparatus.txt` | **Fixed.** Decoded from two PDF parts (chs 1–8, 9–16); every chapter, 1–16, is present. The empty file is in the backup |

The lemma-tag filter was **still on** for the second-pass exports: 2 tags in BHS Chronicles and 25 in LXX Daniel, all now removed.

### PDF exports of the apparatus — the verdict

**On the page, the PDF is faithful**: every superscript, 𝔓 with its number, 𝔐, italics, and even the pop-up notes (sigla and manuscript descriptions) printed beneath each block. **Its text layer is not**: the blackletter sigla are drawn from a Logos symbol font that plain text extraction reads as `"` `#` `$` `%` `&`, with the codes reassigned from page to page. The superscripts come out as ordinary digits, the ligatures `tt` and `Th` come out as `!` and `$`, and the Hebrew comes out in reverse visual order with the pointing detached.

The NA28 PDFs can nonetheless be decoded reliably, because each symbol glyph has a fixed *width* (𝔓 0.819 em, 𝔐 0.915 em, 𝔊 0.779 em) and superscripts are set at 9 pt. `tools/logos_apparatus_pdf2txt.py` does this (it needs `pdfplumber`). Checked against the rendered pages at Matt 1:3–8 and Matt 13:55–14:3, it reproduced them character for character, italics aside. Matthew now has 109 papyrus sigla with their numbers and Mark 136; the plain-text exports had **none**.

**RTF is better still — tested on Habakkuk, 16 September 2026.** The RTF export carries **true Unicode**: the sigla (𝔊 𝔖 𝔗 𝔔 𝔙) are stored as their proper characters, the Hebrew is in logical order with its pointing intact, superscripts are marked as superscripts, and the pop-up notes sit in separate footnote groups that are easy to drop. `tools/logos_rtf2txt.py` converts one to plain text with no guesswork, and needs no extra libraries. The converted Habakkuk apparatus matches the rendered pages. **Recommended route for any apparatus, BHS or NA28: export as RTF and convert it.** A PDF is then optional, for reading only. **Confirmed on six books (fourth pass): the BHS apparatus for Genesis–Deuteronomy and the NA28 apparatus for Galatians.**
- **Complete:** every chapter is present.
- **Nothing lost:** with superscripts set aside, every character of Hebrew, Greek and sigla is identical to the earlier plain-text exports.
- **Everything the plain-text exports lost is back.** Genesis alone has 149 restorations (𝔗ᴶ, 𝔊ᴬ, Mss, Ken 69 …) and Deuteronomy 1,273. Galatians has all 94 papyrus numbers (𝔓⁴⁶, 𝔓⁵¹ᵛⁱᵈ).
- **The Logos private-use character U+E91E is Ethiopic 𝔈** ("versio Aethiopica", confirmed in Logos at Exod 13:20 on 16 September 2026). All 38 instances across ten BHS apparatus files (the Torah, Kings, Isaiah, Ezekiel, Obadiah, Micah and Ezra–Nehemiah) are now replaced with 𝔈 (U+1D508), and `tools/logos_rtf2txt.py` makes the substitution automatically. No other private-use characters occur in `logos-exports/`.

### Limits of the exports — not fixable by tidying

- **The plain-text apparatus exports lose every superscript** (the PDF route above avoids this). None of the roughly 4,800 papyrus
  sigla in the NA28 apparatus files keeps its number (`𝔓` where the edition prints
  `𝔓⁶⁶`, `𝔓⁷⁵`), and version subscripts such as `vg^mss` and `sy^h` collapse too. The BHS
  apparatus very probably suffers the same loss. **For any reading that turns on which
  papyrus or which version, cite from Logos on screen, not from these files.** An export
  to Word format may keep the superscripts; that is worth testing.
- **The BHS text files carry the apparatus note letters inside the words**
  (`בְּרֵאשִׁ֖יתa‬`, with an invisible U+202C directional character). Search the WLC
  layer; use the BHS file to cite.
- **The ESV is Crossway's 2025 US text**, not the ESV Anglicised. Check the pulpit wording
  against the church's own edition.
- **The LXX files use Rahlfs' versification and arrangement:** Exodus 35–40, Jeremiah and
  Proverbs 24–31 are ordered differently, Kings is 3–4 Reigns, Lamentations lacks 3:22–24
  and 3:29, and `10-Ezra-Nehemiah-LXX.txt` carries **Esdras A (1 Esdras) as well as
  Esdras B**.
- **The NA28 text includes John 7:53–8:11 and Romans 16:25–27, and omits Luke 17:36 and
  Romans 16:24.** The ESV and NASB95 verse differences from NIV84 are the familiar
  omitted and bracketed verses (Matt 12:47, 17:21, 18:11; Mark 7:16 …), not export faults.
- **13 files carry no Logos citation or export stamp**, so their exact edition is
  unrecorded. The text was checked and is complete in each: BHS Genesis, Jeremiah and
  Psalms; ESV Genesis, Psalms, Isaiah and Jeremiah; NASB95 Genesis, Exodus, Numbers,
  Deuteronomy and Psalms. (The empty Mark apparatus that was listed here has been replaced.) The NASB95 wording checked
  confirms the 1995 edition ("formless and void", Gen 1:2).
- Byte-order marks are present in some files and not others; this is harmless.

### Sixth pass and final review — 17 September 2026

**All 62 apparatus files (35 BHS, 27 NA28) now come from RTF exports**, converted with `tools/logos_rtf2txt.py`; the previous `.txt` versions are in `_backup/…/sixth-pass/`.

**Checks run on every file:**
- **Chapter coverage:** complete for every book.
- **Content against the previous exports:** with superscripts set aside, the Hebrew, Greek and sigla are identical. The only differences are material the old exports had dropped: book titles; the Inscriptio of Matthew and John; and 𝔊^{ο´} and 𝔊^{θ´} (Old Greek and Theodotion) in Daniel.
- **Superscripts:** restored throughout. Every papyrus siglum in the NA28 files now carries its number.

**Faults found and handled:**
- **TextEdit re-saves.** Ten RTFs were re-saved by TextEdit (Psalms, Ezra–Nehemiah and Chronicles in the BHS; Matthew–Acts, Ephesians and Revelation in the NA28). Their text is intact, but the Logos export stamp is gone, and TextEdit writes paragraph breaks differently. The converter now handles that.
- **Revelation:** the RTF export omits the Inscriptio. It has been supplied from the earlier plain-text export and labelled as such.
- **Misnamed files:** `17-Titus.rtf` and `18-Philemon.rtf` were renamed to the house pattern.
- **Superscripts across paragraph breaks:** a superscript run that crossed a paragraph break (Mark 8:38/9:1) is fixed in the converter.

**Whole-folder review (414 files: 346 `.txt`, 62 `.rtf`, 6 `.pdf`):**
- **Completeness:** every one of the 62 books has every expected version.
- **Clean:** every filename fits the house pattern. No lemma tags, private-use characters, replacement characters or CR line endings remain.
- **Verse coverage:** unchanged from the first pass.
- **LXX first verses:** each file's first verse matches the corresponding Swete book. Rahlfs' Esther additions are present as lettered verses (1:1a–s and so on).

**Left as they are:**
- **Logos quirk in Amos:** the BHS apparatus at Amos 1:11 note a reads `𝔖(𝔙) wnt\r`. That is in Logos's own data (the old export has it too). It is probably the Syriac `wnṭr`.
- **Superseded PDFs:** the Matthew, Mark and Habakkuk apparatus PDFs are now superseded by their RTFs and can be kept or removed.
- **Matthew SBLGNT apparatus:** `01-Matthew-SBLGNT-apparatus.txt` is a deliberate extra.
- **Daniel LXX: now complete — Theodotion added, 17 September 2026.**
  - **File:** `09-Daniel-LXX-Theodotion.{rtf,txt}`. Logos labels it the "alternative text"; the RTF was renamed. `09-Daniel-LXX.txt` is the Old Greek.
  - **Content:** chapters 1–12, 423 verses in Rahlfs' numbering, including 3:24–90. Chapter by chapter it matches Swete's Theodotion on 87–94 % of vocabulary and his Old Greek on only 25–59 %.
  - **Order:** in 3:52–90 some verses stand in a different order in Rahlfs; that is genuine.
  - **Daniel 4:11–12: the files match Logos, but the two Greek texts look crossed.** Patrick confirmed on screen (17 September) that Logos itself has no Theodotion 4:11. Compared with Swete, whose numbering here runs three lower:
    - **Theodotion file:** there is no verse 11. Verse 12 ends with "καὶ ἡ ὅρασις αὐτοῦ μεγάλη, ἡ κορυφὴ αὐτοῦ ἤγγιζεν…", which Swete gives as **Old Greek** 4:8.
    - **Old Greek file:** 4:11 reads "ἐμεγαλύνθη τὸ δένδρον καὶ ἴσχυσεν…", which Swete gives as **Theodotion** 4:8.

    This is either Rahlfs' own editorial arrangement or a fault in Logos's data; the files cannot tell which. **The files are left exactly as Logos has them.** Before any finding rests on Dan 4:11–12 in either Greek text, check a printed Rahlfs-Hanhart (or Göttingen), and report it to Faithlife if Logos is wrong.
  - **A paste repaired, 17 September.** A paste of 5:10–13 had landed in chapter 4, replacing 4:10–13. Chapter 4 has been restored from the RTF. The misplaced version is kept as `_backup/…/sixth-pass/09-Daniel-LXX-Theodotion-with-misplaced-paste.txt`. Chapter 5 already had 5:10–13 complete.
  - **Tags:** none; the highlighting filter is now off.
- **Book titles and Inscriptio in the NA28 apparatus:** there is no Inscriptio for Romans (confirmed in Logos). Book titles are not needed, since the filename and header already name the book, so the letters need no re-export.

