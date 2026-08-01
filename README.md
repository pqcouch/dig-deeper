# Dig Deeper — reports folder

Source-of-truth markdown for Dig Deeper exegetical reports. These `.md` files are
the format Claude reads back in when preparing later passages, auditing claims, or
drawing a book together (macro-synthesis). Human-facing copies (`.odt` for print,
`.html` for on-screen reading) can be kept elsewhere; only the markdown needs to
live here.

## Naming convention

`dig-deeper-[book]-[passage].md` — lower-case, hyphenated, no spaces. Examples:
- `dig-deeper-song-of-solomon-sweep.md` (a full-book sweep)
- `dig-deeper-ruth-1-1to22.md`
- `dig-deeper-romans-8-1to11.md`

## Why this feeds future work

When a new Dig Deeper run is done on the same book, its checking stage pulls in
prior reports on neighbouring passages (and always the book's opening chapters) to
catch cross-passage echoes and tensions. A tidy folder of these markdown files is
exactly what that step consumes — so the archive makes later runs sharper, not
just tidier.

## Contents

- `dig-deeper-song-of-solomon-sweep.md` — 8-unit sweep across the whole Song of Solomon (fresh exegesis, text-first). Added 14 July 2026.
