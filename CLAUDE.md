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

From week 44 on (the author arranged weeks 44–45 by hand, 2026-10-26: "New
shape for all") a module opens with two pages, then three sections, each
opened by a text header:

1. Page `Veckoöversikt: <vecka>`
2. Page `Föreläsning: <vecka>`
3. Header `Föreläsningsanteckningar` (`Föreläsningsanteckningar och
   förinspelade videos` when the week has videos), then per deck, in the
   lecture page's deck order, `<Deck> (föreläsningsanteckningar)` (a
   FeedbackFruits document the author makes from the approved `notes.pdf`)
   followed by `<Deck> (videoföreläsning)` if it has one. `<Deck>` is the
   canonical deck title from `modules/CLAUDE.md`; a deck with two videos
   keeps its part names (`Behållare: Listor, del 1 (videoföreläsning)`)
4. Header `Övningsanteckningar`, then other material for the övning (week
   44: *Läsförståelse: Dokumentation för olika behållare*), the page
   `Övning: <vecka>` and `<Vecka> (övningsanteckningar)`, author-made
5. Header `Laboration`, then `Laboration (N) …` and the week's quizzes
   (week 44: the topic quiz)

Until a section's first document exists its header reads `… kommer`
(`Föreläsningsanteckningar kommer`) and is renamed when the document is
added; within a deck, notes come before the video (author, 2026-10-26). An
item may be listed again in a later week where it helps: week 46 lists
*Repetition (föreläsningsanteckningar)* in its lecture section (author,
2026-10-26: keep it). Week 44's lecture is a recap of the whole course, and
the week's four decks are taught at the övningar (author, 2026-10-10).

Weeks 37–41 were taught before this shape and keep their layout: weeks
39–41 the shape of 2026-09-20 (overview, lecture, notes, videos, Övning,
its notes, lab); weeks 37–38 predate even that.

The imported items of the previous course design are detached and
unpublished, never deleted: `Övning <vecka>`, `Fördjupande övning <vecka>`,
the page `Fler kommande FeedbackFruits-videor`, and the old unsuffixed video
assignments of week 39. *Summativ bedömning (datorprov)* and *Projektet* are
not week modules of this shape.

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

Övningar (all optional): in 2026 weeks 37–39 they were in half-class groups
A–F / G–L; from week 40 (author, 2026-09-28) they are for the whole class,
the first occasion in D37 + Zoom, the second a continuation on the week's
topic in D37 + Zoom with, at every second occasion, a parallel repetition
in a Zoom breakout room led by a TA: usually Emelie (emewas, "hen"),
another TA when Emelie is not booked (author, 2026-09-28). Since
2026-09-30 TimeEdit lists the Övningar without groups and without E32
("Övning (helklass) — D37, Zoom"), so the schedule blocks are generated
again (`make update-schedule`); who leads the repetition is said in the
week overview's text, not in the schedule. Labs and
redovisning keep their groups. Next year the first weeks are half-class
again.
