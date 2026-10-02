# Asking the Logos Research Assistant

**Purpose:** A reference sheet for putting dig-deeper questions to the Logos Research (Study) Assistant and judging what comes back.
**Drawn from:** the Job and Matthew rounds of October 2026, and the house logos-research skill.
**Date:** 2 October 2026

---

## What the Assistant Is, and Is Not

The Assistant searches the prose of your library: commentaries, dictionaries, study Bibles and monographs. It then writes a summary with numbered citations. Three things follow from how it works.

- **It returns what ranks highest, not what is best.** Ask about 27:9–10 without naming a source, and you get the Holman Old Testament Commentary and *Hard Sayings*. You do not get France or Davies–Allison.
- **It falls back on general knowledge when the library is silent.** It does so without always saying so. An answer with no footnotes is the Assistant's own opinion.
- **It reasons from the English by default.** In the Job round it treated the NASB95's editorial heading over chapter 28 as if it were the text.

So use it for **the state of a scholarly question**: who holds which view, and on what evidence. Do not use it for **facts about the text**. Those are answered better, and more cheaply, from the corpus.

---

## Before You Ask: Is Logos the Right Tool?

| The question is about… | Best route |
|---|---|
| A count, a word chain, where a word occurs | The `_texts/` corpus: Claude can answer from it in one command |
| A manuscript reading in Matthew, Mark or Luke | The NA28 apparatus already in `_texts/logos-exports/` |
| A textual variant in another book | The Logos **Exegetical Guide**, Textual Variants section (it uses no AI credits) |
| An LXX variant (Göttingen, Rahlfs apparatus) | Open the edition itself in Logos, if you own it, at the verse |
| Paragraph markers, accents, the Masorah | Read BHS on screen; commentaries rarely discuss these |
| What commentators think, and why | **The Research Assistant** |
| Historical or cultural background | **The Research Assistant** |
| Whether scholars have noticed an allusion | **The Research Assistant** (this fills the "history of interpretation" criterion the audits leave unchecked) |

---

## Framing the Question

1. **One question per turn.** Compound questions run slowly and come back half-answered. Split them, and use follow-ups in the same conversation to narrow.
2. **Name the source.** Write "What does Davies and Allison (ICC) say about…", not "Why does Matthew…". If you do not own the work, the Assistant says so or falls back, and you learn that too.
3. **Name the series when you want a tier.** "Which major critical commentaries (ICC, NICNT, WBC, BECNT) discuss…" keeps out study Bibles and popular works.
4. **Use the scope control.** Set "All books" to a collection: make one called *Matthew commentaries* once, then select it for every Matthew question.
5. **Give the reference in plain form**, e.g. "Matthew 27:9–10". For a word, give the English gloss with the Greek or Hebrew in brackets: "the participle translated 'go' (πορευθέντες) in Matthew 28:19".
6. **Ask for views and evidence, not for a verdict.** Write "What are the main explanations, who holds each, and what evidence do they give?". Avoid "Is it true that…?" and "Explain why…", which invite agreement.
7. **Ask neutrally.** Do not put the hoped-for answer into the question. "Does Matthew 28:18–20 echo 2 Chronicles 36:23?" invites a yes. "Which commentators discuss a link between Matthew 28:18–20 and 2 Chronicles 36:23, and do any reject it?" does not.
8. **For an allusion, ask three things:** who proposes it; whether anyone argues it is shared idiom instead; and, where it matters, which direction the dependence runs.
9. **For a direction of dependence, ask for the argument, not the date.** The Assistant tends to settle direction by assuming which book is older. Ask: "What textual arguments are given for the direction of dependence between Job 3 and Jeremiah 20:14–18?"
10. **Ask for page numbers** when you will cite the work: "with page references".

---

## Question Templates

These rephrase the questions that proved hard this autumn.

| Need | Template | Example |
|---|---|---|
| A named commentator's view | What does [author] ([series]) say about [issue] in [ref]? | What does Davies and Allison (ICC) say about why Matthew 27:9 attributes the quotation to Jeremiah? |
| The state of a debate | What are the main explanations of [issue] in [ref], who holds each, and what evidence do they give? | What are the main explanations of "Zechariah son of Barachiah" in Matthew 23:35, and who holds each? |
| An allusion | Which commentators discuss a link between [ref] and [OT ref], what wording do they point to, and does anyone reject it? | Which commentators discuss a link between Matthew 8:24–25 and Jonah 1:4–6, and does anyone reject it? |
| Grammar | How do the standard grammars (Wallace, BDF, Robertson) classify [form] in [ref]? | How does Wallace classify the aorist participle translated "go" in Matthew 28:19? |
| A textual point in prose | What does Metzger's *Textual Commentary* say about [ref]? | What does Metzger's *Textual Commentary* say about Asaph and Amos in Matthew 1:7–10? |
| An LXX variant | What does the Göttingen Septuagint apparatus record at [ref] for [reading]? | What does the Göttingen apparatus record at Isaiah 7:14 for "will conceive" / "will have in the womb"? (Use only if you own Ziegler's *Isaias*.) |
| Background | What was [custom / institution] in first-century Judaism, and what is the evidence for it? | What was the temple tax in first-century Judaism, and what is the evidence for it? |
| A follow-up | You mentioned [author]. What exactly does he say on page [n], and what reasons does he give? | — |

---

## Reading the Answer

Run these checks before trusting a sentence.

1. **Is it cited?** A sentence without a footnote number is general knowledge. Treat it as an unsupported claim.
2. **What tier is the source?** A critical commentary or a specialist monograph carries weight. A study Bible, a popular commentary or a "hard sayings" book does not, on a technical question. Note the series beside every source.
3. **Did it answer your question?** In the Job round, a question about paragraph markers came back as an answer about 27:1.
4. **Is it reasoning from the English?** Look for headings, chapter titles, or an English word (such as "Ten Commandments" for עֲשֶׂרֶת הַדְּבָרִים, "the ten words") treated as the text.
5. **Is a date assumption doing the work?** "Ezekiel predates Job, so Job borrowed" is an assumption, not evidence.
6. **Watch the inflating words.** Phrases such as "broad scholarly agreement", "structurally intentional" and "clearly" are often the Assistant's own glosses on one source. Check how many footnotes stand behind them.
7. **Does it contradict itself?** It sometimes gives a direction of dependence in one paragraph and its opposite in the next.
8. **Does a claim about the text match the text?** Any wording, count or manuscript claim should be checked against the corpus. Claude can do this in one step when you bring the answer back.

---

## Bringing the Answers Back

- **Paste the whole answer, with its footnotes.** Numbers in square brackets such as [1] are fine; they will be read as pointers to the notes.
- **Put the question you asked above each answer.** How it was asked affects how far it can be trusted.
- **Tag each block with its source**, in one word, as the lean-upload checklist asks. For example: `[Logos RA]`, or `[commentary: Cooper]` for your own excerpts.
- **Say which questions got no usable answer.** A gap is useful information: it tells Claude where to go next.
- **What happens next.** Claude tests each answer against the corpus. It records cited views as `[S: author]` and folds them into the overview or the queue at the next Finalise pass. An answer never replaces a finding from the text; it confirms, nuances or resists one.

---

## Questions the Assistant Usually Cannot Answer

- **How widely a reading is attested in the manuscripts.** Use the apparatus or the Exegetical Guide.
- **Counts and word distributions.** Use the corpus.
- **Masoretic paragraphing and accents.** Use BHS on screen, or an Aleppo-based edition.
- **Anything resting on a work you do not own.** The Assistant may answer anyway from general knowledge, so check for footnotes.

---

## One-Line Checklist

**Before:** is this a question about scholars (Logos) or about the text (corpus)?
**Ask:** one question; named source or series; scoped collection; views and evidence; neutral wording; page numbers.
**Read:** cited? what tier? on the question? from the English? a date assumption? an inflated summary? matches the text?
**Return:** whole answer, with its footnotes, under the question asked, tagged.
