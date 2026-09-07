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
| `logos-exports/` | Your own Logos exports — BHS, Rahlfs-Hanhart LXX, NASB95, ESV, and whatever else you upload | **Citation of record**, wherever a reading is load-bearing | Whole-canon searching — coverage is only what has been exported so far |

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

`logos-exports/` is where those go. Name them as they already are —
`BHS Ruth.txt`, `LXX Isaiah.txt`, `ESV Leviticus.txt`, `NASB95 Ruth.txt` — so the
source is visible in the filename. **Name the edition, not just the version:** the
NASB95 and the 2020 revision are substantially different texts, and a file called
`NASB Ruth.txt` will be ambiguous within a year. Logos caps a single export at 100 pages, so a long
book comes in parts; that split is an export artefact and means nothing.

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
├── logos-exports/             your BHS / LXX / ESV / NASB95 exports
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
