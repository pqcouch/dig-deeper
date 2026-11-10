# Script rendering test — Hebrew and Greek in the house formats

This file exists to answer one question: does pointed Hebrew, and accented Greek, survive into the house `.odt` and the house two-pane `.html` without mangling? Open both and compare them against this list.

## 1. Hebrew inline in an English sentence, with a gloss

The verb שָׁכַן ("to dwell, settle") is the root behind מִשְׁכָּן ("tabernacle, dwelling-place"), and the two stand together at Exodus 40:35.

**What to check:** each Hebrew word reads right-to-left *within itself*, the sentence still runs left-to-right, and the bracket after the Hebrew sits on the correct side — `שָׁכַן ("to dwell")`, not with the opening bracket stranded.

## 2. Vowel points, accents and the special marks

- Maqqef binds two words: עַל־פְּנֵי ("upon the face of")
- Paseq stands alone: אֱלֹהִים ׀ לָאוֹר ("God … to the light")
- Sof pasuq closes the verse: הָאָֽרֶץ׃ ("the earth.")
- Final forms: מֶלֶךְ ("king"), אָרֶץ ("land"), עַם ("people")
- Sin and shin distinguished: שָׂרַי ("Sarai") against שָׁמַיִם ("heavens")

**What to check:** the points sit *under* their consonants rather than drifting, and the accents have not become boxes or question marks.

## 3. A full verse

בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃

("In the beginning God created the heavens and the earth." — Genesis 1:1, NASB95)

**What to check:** the verse begins at the *right* margin, and the cantillation accents are present.

## 4. Greek

The noun λόγος ("word") opens John's Gospel; συνάγω ("gather") and σκορπίζω ("scatter") stand opposed at John 11:52. Breathings and accents: ἀρχῇ, ἦν, οὗτος, Θεόφιλε, ἐφʼ.

**What to check:** rough and smooth breathings are visible and distinct, the iota subscript in ἀρχῇ has survived, and the apostrophe in ἐφʼ is the Greek one.

## 5. In a table

| Term | Gloss | Where |
|---|---|---|
| קְדוֹשׁ יִשְׂרָאֵל | "the Holy One of Israel" | Isaiah, 25×; Joshua–Kings, once |
| יְהוָה צְבָאוֹת | "the LORD of hosts" | Isaiah 60×; 1–2 Kings 5× |
| נָגִיד | "leader, prince" | 2 Kings 20:5 |
| ἐκκλησία | "assembly, church" | Acts 5:11 |

**What to check:** the Hebrew stays inside its own cell and does not push the column borders about.

## 6. In a heading — עֵדוּת ("testimony") and μάρτυς ("witness")

**What to check:** the heading renders at 14 pt bold like every other heading, and appears correctly in the HTML sidebar if it is an H2.

---

*If every check passes, the convention is safe: original script first, English gloss in brackets after.*
