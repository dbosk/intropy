# intropy (DD1317, Canvas course prgi26)

The slide decks and tutorials have their own rules in `modules/CLAUDE.md`.
This file holds what is true of the course's Canvas side. **Load the
`canvas-course-repo` skill before any write to Canvas**; it owns the general
rules (files are the source of truth, authoritative `modules:` front matter,
the empty-body hazard, sandbox rehearsal, `--no-cache`). A rule that would
hold in another course belongs there, not here.

## Canvas (prgi26, course id 63874)

Every Python week has a Canvas module, listed in order in
`canvas-modules.txt`, and a directory `modules/<module>/` holding its pages:

| File | Canvas page |
|---|---|
| `vecka.md` | `Veckoöversikt: <vecka>`, first in the module; the schedule block between `<!-- schema:start -->` and `<!-- schema:end -->` is generated from TimeEdit by `bin/veckoschema.py`, driven by the `weeks:` field |
| `lecture.md` | `Föreläsning: <vecka>`: one page per week from week 39 on. Weeks 37–38 have one page per deck, the second named `lecture-<deck>.md` |
| `tutorial.md` | `Övning: <vecka>` |
| `lab/instruction.md` | pushed into the lab's FeedbackFruits assignment; `regex` is the Canvas assignment id |

`modules/overview-python/pythondelen.md` is the course-wide overview with
all learning objectives: update it when a week's objectives change.

### The shape of a week module

The author arranged *Inmatning, felhantering och styrstrukturer* by hand
(2026-09-20) and asked for the other weeks to follow it:

1. Page `Veckoöversikt: <vecka>`
2. Page `Föreläsning: <vecka>`
3. `<Deck> (föreläsningsanteckningar)` per deck: a FeedbackFruits document
   the author makes from the approved `notes.pdf`. Until it exists, one
   text header `Föreläsningsanteckningar kommer`
4. `<Deck> (videoföreläsning)` per deck that has a video, in the lecture
   page's deck order. `<Deck>` is the canonical deck title from
   `modules/CLAUDE.md`; a deck with two videos keeps its part names
   (`Behållare: Listor, del 1 (videoföreläsning)`)
5. Page `Övning: <vecka>`
6. `Övning: <vecka> (övningsanteckningar)`, FeedbackFruits, author-made.
   Until then the text header `Övningsanteckningar kommer`
7. `Laboration (N) …`
8. anything else the module holds (week 42: *Läsförståelse: Dokumentation
   för olika behållare*)

The imported items of the previous course design are detached and
unpublished, never deleted: `Övning <vecka>`, `Fördjupande övning <vecka>`,
the page `Fler kommande FeedbackFruits-videor`, and the old unsuffixed video
assignments of week 39. Weeks 37–38 were taught before the shape existed and
keep their layout. *Summativ bedömning (datorprov)* and *Projektet* are not
week modules of this shape.

A page's `position:` is where it sits in Canvas now. When a placeholder
header is added or replaced by several documents, change the positions of
the pages below it in the same commit. When the author publishes a page in
Canvas, flip `published:` in its file before the next push.

### Make targets (`canvas.mk`, included from the root `Makefile`)

- `make update-schedule && make push-pages` when TimeEdit changes.
- `make push-pages` pushes changed `PAGES` without `--create`; the stamps
  live in the main checkout, so from a worktree push single files with
  `canvaslms --no-cache pages edit -c '^prgi26$' -f <file>`.
- `make create-pages`, `make create-modules`: one-shot. Rehearse with
  `CANVAS_COURSE='^Sandbox dbosk$'`.
- `make push-labs` converts `lab/instruction.md` with pandoc `--mathjax`
  and sends only name and description, so the FeedbackFruits settings stay.
- A new page: write the file, add it to `PAGES` (or `WEEK_PAGES` for a
  `vecka.md`), create it once with `pages edit --create`.

Course design since 2026-09-01: no Torus, no flipped classroom; a week runs
live lecture (recording and notes as the alternative), then övning, then
laboration. Slides are shown at the lecture and not linked.
