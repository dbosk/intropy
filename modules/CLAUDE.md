# Module slide decks

**Load the `didactic-decks` skill before touching a deck**, and its
`references/house-style-sv.md`: every deck here is in Swedish. That skill
holds everything about how a deck is built, authored and checked; the
pedagogy lives in `try-first-tell-later`, `variation-theory` and
`didactic-notes`, the citations and appendices in `backing-claims`, the
review loop in `remarkable` and `worktree-subagents`. This file holds only
what is true of this course. Before writing a new rule here, ask: would it
hold in another course too? Then it belongs in a skill, not here. A rule
in two places is a defect.

## The decks

Each module has one or more deck directories (`slides*/`) building
`slides.pdf` and `notes.pdf` from one `contents.nw`. The model deck is
`computational-thinking/slides` (tracking issue #269); `helloworld/slides`
is the build template the skill's `assets/deck-template/` was copied from
(re-sync the template when its wiring changes); `exceptions/slides` is the
most compact worked example. `modules/Makefile` excludes functions,
exceptions, recap, scipy and debug from the course-wide build. Six decks
still lack a backed-claim chapter: `classes/slides-more`
(Operatoröverlagring) and the five `containers/slides-*` decks — run the
claim audit there in their next rounds.

Canonical deck titles, used when one deck points at another in prose
(`\cref` cannot cross documents; write "föreläsningen \emph{Funktioner},
bilaga B" and say what that appendix answers): *Algoritmiskt tänkande*;
*Hello, World!*; *Variabler och utskrifter*; *Funktioner*; *Inmatning och
datatyper*; *Villkor och styrstrukturer*; *Felhantering*; *Upprepningar*;
*Moduler och paket*; *Behållare: Listor*, *Behållare: Tupler*,
*Behållare: Uppslagslistor*, *Behållare: Mängder, stackar och köer*,
*Behållare: Ett gissningsspel*; *Klasser och objekt*;
*Operatoröverlagring*; *Praktiska tillämpningar av klasser*; *Arbeta med
filer*.

The reMarkable review family of a deck is `<Titel> — notes (review) vN`
(the Hello World family keeps its old spelling). Learning objectives carry
the week page's Lo-codes in a comment (`learning-outcomes.md`, `vecka.md`).

## Course-specific rules

- Example data names: never the author's. "Malvina" is the default single
  name; when several are needed, Astrid Lindgren's strong characters in
  order — Ronja, Pippi, Madicken — then their side characters (Birk,
  Annika, Lisabet). "Ada" (Lovelace) is also fine (author, 2026-09-06);
  "Beda" was only ever its one-letter partner.
- Hidden cultural facts in example data: the birth year 1927 is the
  founding year of Kvinnliga Teknologers Sammanslutning, today Malvina, at
  KTH (bib key `MalvinaHistoria`). The fact stays out of the student text
  and is recorded, with its source, in an `\ltnote`.
- The author's own misconceptions manuscript is cited as
  `SooriBosk2026` (`@unpublished`, provenance block in the decks that use
  it), never by nickname.
- Every appendix chapter opens with the verbatim
  `\chapterprecis{Författaren har ännu inte granskat resultaten i den här
  bilagan i sin helhet.}`.
- "Laboration 0: kom igång med Hello World" is the name of a Canvas item;
  it keeps its spelling.

## Backed claims (the ledger)

A claim already backed in another deck is not redone: cite the same
source with the provenance block copied (plus `% FOUND-VIA (here): backed
in <deck>, bilaga <X>`) and point to it in prose, saying what the appendix
answers and stating the claim at the strength the appendix supports.

Backed so far (question → answer):
- *Algoritmiskt tänkande* B: algorithm components → sequence, selection,
  repetition, data hold across three traditions, two reservations on
  use; C: stepwise refinement → Wirth's, established for getting
  started, a simplification as a full design method; D: literate
  programming → Knuth's, noweb is Ramsey's form, never dominant; E: DRY →
  Hunt and Thomas, the risk is real when copies change inconsistently,
  but no absolute rule (both origin and benefit are covered).
- *Funktioner* B: SRP → Martin 2003 (not 2000), established, "one
  responsibility" is a judgement; C: KISS → NOT Kelly Johnson's (in
  print 1958, attribution rests on a memoir), simplicity as a design
  value is established.
- *Felhantering* B: exception misconceptions → backed (Java, late-stage
  students); C: catch-all → a known bad habit, but the actual bugs are
  rarer than the habit, so the advice is "fånga det ni vet hur ni ska
  svara på", not "aldrig".
- *Upprepningar* B: loop misconceptions → five of six backed in primary
  sources; C: productive failure → moderate effect, from comparing the
  attempt with the answer, not from delay itself.
- *Hello, World!* B: origin → Kernighan (B tutorial), tradition
  questioned since 1996; C: interpreter reads statement by statement →
  yes, but bytecode first; D: error messages → a real obstacle, first
  errors are mostly typos, rewritten messages not shown to help; E:
  chronology → holds, only two of seven years are clean release dates.
- *Villkor* B and *Inmatning* B: misconceptions → backed, frequencies
  in this population unknown.
- *Arbeta med filer* B: misconception backed (one source no longer open);
  C: memory hierarchy orders of magnitude → textbook values; D: Python's
  file functions → as stated, default encoding platform-dependent; E:
  CSV is not a standard (informational RFC), JSON is.
- *Moduler och paket* B: modules/import as a novice difficulty → NOT
  backed (no direct study).
- *Klasser och objekt* B: class/object misconceptions → three backed
  (Java, Smalltalk); C: encapsulation → established, from Parnas, loosely
  defined and contested in its classic form. *Praktiska tillämpningar*
  B: composition over inheritance → Design Patterns, established,
  maintenance experiments on inheritance point both ways.
- *Variabler och utskrifter* B: PEP 8 helps the reader → partly and
  weaker than assumed: names, short lines, indentation supported; the
  guide as a whole and several rules (four spaces) not.
- No backed-claim chapters yet: *Operatoröverlagring*, the five
  *Behållare* decks (method chapter only) — run the claim audit there.

## Build environment

The **makefiles submodule must be on the `tominted-default-weave`
lineage** (currently 1571556; it makes the highlighted weave the
default). In a fresh worktree run `git submodule update --init --checkout
makefiles` (`--checkout` because the repo config has
`submodule.makefiles.update=none`). The main checkout's `makefiles` is not
on that lineage: after the campaign branch is merged to master, run
`git submodule update` there. Tracked hand-written activity inputs such as
`files/slides/examples/scb/*.py` are exempt from `black --check`; the
tangled `hello.lean` needs the elan toolchain `+leanprover/lean4:v4.25.1`.

## Where the general rules went (2026-09-07)

| Was in this file | Now in |
|---|---|
| Deck anatomy, drivers, preamble, build wiring, gotchas, checks | `didactic-decks` (SKILL.md + `references/`) |
| Chunk rules, `\runpython`, floats and captions, `\ltnote` queue | `didactic-decks/references/` |
| Swedish term first, no week or course-event references, exekverar/utför, "tagit del av", name the action, appendix-pointer wording | `didactic-decks/references/house-style-sv.md` |
| Exercises that do not narrate the answer, the open question | `try-first-tell-later` |
| Generalisation sequences, labels matching what varies | `variation-theory` |
| Note visibility, margin queue, summary vs remark, side captions | `didactic-notes/references/` |
| Citations in floats, unnumbered crefs, two-line displays | `latex-writing/references/` |
| latexmk/PythonTeX/biber gotchas, tangle rules | `literate-programming/references/` |
| Pointers beside the claim, cross-deck reuse, no nicknames, claim audit, Fortsatt arbete | `backing-claims/references/` |
| Review rounds, transcription, fix and reader agents, cleanup | `remarkable`, `worktree-subagents` |
