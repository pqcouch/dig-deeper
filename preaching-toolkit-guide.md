# The Preaching Toolkit: Workflow Quick Reference

**For:** book-overview · dig-deeper · point-purpose · sermon-review
**Default translation:** ESV · **House output:** .md (canonical), .odt, .html

---

## The Order at a Glance

Book overview → make it visible to the project → book sweep → solo passage digs → finalise the overview → point-purpose → sermon-review.

The overview is **first in and last out**: it orients everything downstream, and the completed passage work flows back to finalise it. Treat it as a planning document to be *tested*, not fixed truth.

---

## Step by Step

**1. Book overview (its own skill).** Run first, before any passage work. Produces the presenting situation, arc map, microscript, intertextual map, Christological trajectory, preaching traps, an early↔late echo table, and a weighted series plan.

> "Give me a book overview of Philippians."

**2. Make it visible to the project.** For the downstream skills to *use* the overview automatically, it must be somewhere they can see it — a connected folder or the same conversation. A skill cannot consume an overview it cannot see.

**3. Book sweep (a dig-deeper mode).** A lighter, proportional-depth pass across the whole book — for auditing the overview and seeing the cross-passage network. This is planning, not pulpit prep.

> "Using the Philippians book overview, run a dig-deeper sweep across the whole book."

**4. Solo passage digs.** For each passage you will preach — especially the ⭐ HIGH ones the overview flagged — run a full solo dig. This is the deep prep the pulpit needs.

> "Dig deeper into Philippians 2:1–11, using the book overview."

**5. Finalise the overview (the loop closes).** Feed the completed runs back so the overview reflects what the passages actually demonstrated. Optionally ask for the cross-pericope synthesis.

> "Finalise the Philippians book overview using the completed digs."
> "Pull the threads together — give me a macro-synthesis of the Philippians digs."

**6. Per sermon: point-purpose, then sermon-review.**

> "Turn the dig-deeper report on Philippians 2:1–11 into a sermon backbone." *(point-purpose)*
> "Here's my sermon draft — review it and produce a final manuscript." *(sermon-review)*

---

## It's a Loop, Not a Line

```
book-overview ──Phase 0.5──► dig-deeper ──findings──► point-purpose ──► sermon-review
      ▲                           │
      └────── runs feed back ──────┘   (Finalise / macro-synthesis)
```

The first pass of the overview is a Draft, written to be corrected. Each dig tests it; the finalise pass rewrites it with what the sweep proved.

---

## Where to Keep the Files

Keep everything for a book **together in one folder per book**, inside a single prep folder connected to the project. This is what makes the loop automatic: dig-deeper picks up the overview at Phase 0.5, reconciles each passage against its *neighbouring* reports (especially the opening chapter) at its checking stage, and the finalise/macro-synthesis passes read the whole set.

**Keep the `.md` as the canonical copy.** The skills read and generate from Markdown; the `.odt` and `.html` are derived views. Storing the `.md` files (as you already do) is exactly right — keep those; the other two formats can be regenerated any time.

Suggested layout (Title-Case book folders; group the Minor Prophets under `The Twelve/`):

```
dig-deeper/
├── README.md
├── preaching-toolkit-guide.md
├── Philippians/
│   ├── book-overview-philippians.md
│   ├── dig-deeper-philippians-sweep.md
│   ├── dig-deeper-philippians-2-1to11.md
│   ├── dig-deeper-philippians-4-1to9.md
│   ├── dig-deeper-philippians-claim-audit.md        (if produced)
│   └── philippians-dig-deeper-macro-synthesis.md    (if produced)
├── Ruth/
│   └── book-overview-ruth.md ...
└── The Twelve/
    ├── Habakkuk/
    │   ├── book-overview-habakkuk.md
    │   └── dig-deeper-habakkuk-sweep.md ...
    └── Jonah/
        ├── book-overview-jonah.md
        └── dig-deeper-jonah-sweep.md ...
```

Per-book folders matter because the skills reconcile a passage against its *neighbours* — keeping a book's reports together is what lets them find each other. Folder case doesn't matter to the skills; co-location does.

---

## Filename Conventions

Use these exact patterns (lower-case, hyphenated) so the skills recognise related files as a set:

| Output | Filename pattern | Example |
|--------|------------------|---------|
| Book overview | `book-overview-[book].md` | `book-overview-ruth.md` |
| Passage dig | `dig-deeper-[book]-[chapter]-[verses].md` | `dig-deeper-philippians-4-1to9.md` |
| Book sweep | `dig-deeper-[book]-sweep.md` | `dig-deeper-philippians-sweep.md` |
| Claim audit | `dig-deeper-[book]-claim-audit.md` | `dig-deeper-jonah-claim-audit.md` |
| Macro-synthesis | `[book]-dig-deeper-macro-synthesis.md` | `ruth-dig-deeper-macro-synthesis.md` |

Verse ranges use `to` (e.g. `4-1to9`); single verses drop the range (e.g. `dig-deeper-john-3-16.md`).

---

*Keep this guide in the prep folder as a reminder of the sequence. When in doubt: overview first, digs from the text, overview finalised last.*
