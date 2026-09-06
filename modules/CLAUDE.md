# Module slide decks

Each module has one or more deck directories (`slides*/`) building two PDFs
from one source: `slides.pdf` (beamer) and `notes.pdf` (memoir +
beamerarticle: full lecture notes with the slides' content woven in), both
`\input`ing the shared `contents.tex`.

## The deck standard

`computational-thinking/slides` is the model deck (tracking issue #269;
the finished decks of variables, conditionals, exceptions, iterations,
containers and helloworld follow it — `exceptions/slides` is the most
compact worked example). A deck is done when it has:

- `contents.nw` — the literate single source (below); prose lecture notes
  between the frames (article mode), try-first questions before
  explanations, one `example`/`exercise` environment per case.
- `abstract.tex` — Översikt, Lärandemål as `restatable` `lo` environments
  labelled `<Module>LO<Aspect>` (restated where the notes meet them),
  Förkunskaper; the week page's Lo-codes kept in a comment.
- `\ltnote`s (instructor notes) for every design choice: which LO, what
  varies and what stays invariant, which misconception an activity targets.
  `\parencite` is used only inside `\ltnote`s.
- `ltnotes.bib` — every entry carries a provenance block (`CLAIM`,
  `FOUND-VIA`, `PICKED`, `QUOTE`, `VERIFIED`, `COUNTER`, `DATE`; see the
  `backing-claims` skill and `check_provenance.py`).
- `sokprotokoll.tex` — appendices: Bilaga A (the method, for students),
  then one chapter per backed claim (question as title, Metod with the
  query table, Resultat, Slutsats answering the question in its first
  sentence, hit list `\input` from `litteratursokning/`). Every appendix
  chapter opens with the verbatim `\chapterprecis{Författaren har ännu inte
  granskat resultaten i den här bilagan i sin helhet.}`.
- A claim already backed in another deck is not redone: cite the same
  source with the provenance block copied (plus `% FOUND-VIA (here): backed
  in <deck>, bilaga <X>`) and point to it in prose — "det vetenskapliga
  underlaget finns i föreläsningen \emph{Funktioner}, bilaga B" (`\cref`
  cannot cross documents). Backed so far: algorithm components, stepwise
  refinement, literate programming, DRY (*Algoritmiskt tänkande* B–E); SRP
  and KISS (*Funktioner* B–C); exception misconceptions and catch-all
  (*Felhantering* B–C); loop misconceptions and productive failure
  (*Upprepningar* B–C); "Hello, World!" origin, interpreter, error messages
  (*Hello World!* B–D); language chronology and origins (*Hello World!* E).

### Language rules (from the author's reviews)

- Swedish throughout; Swedish term first, English once in parentheses:
  "spårutskrift (\foreignlanguage{english}{traceback})".
- Never tie text to weeks, lecture order or course events ("förra
  veckan", "vecka 38", "föreläsningens första halva", "på laborationen"):
  refer to topics, deck titles and activities ("tidigare", "föreläsningen
  \emph{Funktioner}", "när ni programmerar"). Förkunskaper say "tagit del
  av föreläsningen …", not "sett".
- "Ett program utför en uppgift; processorn/datorn/tolken exekverar
  programmet": whoever runs code exekverar it (noun "exekvering"); a
  program or a person utför a task; "köra" stays as the everyday word.
- Appendix pointers read "det vetenskapliga underlaget finns i \cref{app:…}"
  and stand beside the claim they back, once: in the same sentence (a
  parenthesis or a following clause), never as a trailing sentence a
  sentence or more away, never twice for one appendix in a paragraph.
  No ambiguous sentence-initial pronouns in the appendices ("Sökningen
  gjordes …", not "Den gjordes …").
- Name the action, not the position: "något måste översätta det vi skriver
  till det processorn exekverar", not "något måste stå emellan". A title
  that names a literal reproduces it exactly ("Hello, World!").
- Learning objectives say what the student can do, in plain words, without
  restating the mechanism. Exercises do not hint at the critical aspect —
  nor do example titles or lead-ins ("Ett program med ett fel", not "… med
  ett stavfel"), nor the program's own payload (a printed string like "Den
  här raden hinner köras." discerns the answer for the student; print
  "Välkommen!" and let them discern it). A try-first question comes after
  everything it presupposes, and the example that answers it shows the
  full answer. The question itself stays open ("Vad skriver programmet
  ut?", not "Vad är felet?"): it gives the critical aspect a chance to
  surface in the answers without pointing at it.
- In a generalisation sequence (the same task in language after language,
  editor after editor) the invariant holds from the first case: the very
  first example performs the same task as the last. Each step asks how the
  new case relates to the previous one ("Hur förhåller sig detta till
  assembler?"), and each case carries its own motivation in the body —
  why this language exists, what is special about it — not only in a
  later summary subsection. A case added to the sequence is added to every
  sentence that enumerates the cases.
- What exists only in an `\ltnote` does not exist for the student: if the
  student is meant to notice a development or a reason, say it in the
  prose. Do not pre-announce a `summary` block with a one-line paragraph
  saying what it is about to say.
- Never refer to physical position ("på nästa bild", "ovan"): `\cref`. Every
  figure is referenced from the prose (not only from an `\ltnote`) and
  placed near the reference; captions are side captions in the notes.
- Blocks that close a section by summarising it are `summary`, not `remark`.
- Overlay staging that hides an answer on the slide (`\item<3->`) collapses
  in the notes: stage structurally (example, exercise, prose, second example).
- Chunk names short ("ta hand om felen"). Where a program handles several
  errors, ask first what can go wrong, then show the handlers.

## Literate decks (contents.nw)

`helloworld/slides` is the build template — copy from it. In a literate
deck, `contents.nw` is the single source:

- `contents.tex` is **woven** from it (`noweb.mk`'s `%.tex: %.nw` rule;
  the default weave runs the dbosk noweb fork's `autolang` + `tominted`
  pipeline, so chunks come out as syntax-highlighted `minted`
  environments).
- The presented example programs are **tangled** from it into `examples/`
  (`notangle -R"[[<filename>]]"`), so `examples/` is entirely generated
  (data files a deck reads, like `files/slides/examples/scb/`, are tracked
  inputs and must be excluded from the ignore rule).
- `.gitignore` lists the PDFs, `contents.tex`, `examples/`, `latexmkrc`
  (tangled from `tex.mk.nw`), and PythonTeX's `didactic_output_*.txt`,
  `*.pytxcode`, `pythontex-files-*`; `ltxobj/` is ignored repo-wide. Only
  `contents.nw` is committed. Never edit `contents.tex`.

Before editing any `contents.nw`, activate the `literate-programming`
skill.

### Authoring rules for chunks in decks

- A code chunk replaces every `\inputminted[firstline=…,lastline=…]`:
  name the chunk after the file it tangles to, `<<[[hello.py]]>>=`, and
  place it at its point of presentation (inside the frame).
- Frames containing chunks (or any minted output) must be `[fragile]`.
- A two-line display inside an `example` must not rely on `\\` in a
  `center`: the article job collapses it to one line. Use a one-column
  `tabular` (or `\par` between the lines).
- `sidecaption` only where the margin is free: next to a figure it works
  (with `\setsidecappos{b}`), but a table on a footnote-heavy appendix
  page overprints the citation footnotes, so query tables take a plain
  `\caption`.
- `\ltnote`s longer than the margin queue forward and print beside the
  next section or the appendix; `\clearpage` does not flush them. Put
  `\mode<article>{\clearpage}` before the section they belong to, and
  before the *last* frame of a section whose notes overflow, so the queue
  drains on a page still inside the chapter (shorten notes that restate
  the prose; anchor a note where its decision is made, not at the end of
  the passage, and never within a few lines of a `sidecaption` figure).
  A margin at capacity also pushes citation footnotes to the next page.
- Pygments' GAS lexer marks `len = . - msg` as an error token, which minted
  draws as a red box: write `.set len, . - msg` in assembler chunks.
- Noweb quoting `[[…]]` cannot hold a babel shorthand pair: `[[phone["adam"]]]`
  prints `phone[ädam"]` because Swedish `"a` fires before `\code` changes
  catcodes; write such snippets with `\mintinline{python}|…|`.
- **Never start a theorem-style environment (`example`, `remark`, …)
  directly with a chunk or minted block** — the inline label and the code
  display overprint each other in the notes job. Put a short lead-in
  sentence first.
- To show the same code again later (recaps), do not redefine the chunk —
  noweb would concatenate the definitions into the tangled file. Instead
  re-display the tangled artifact: `\inputminted{python}{examples/foo.py}`
  (always the whole file, never line ranges).
- Write Python chunks black-clean (4-space indent, double quotes, two
  blank lines around top-level defs): the tangle rule pipes tangled `.py`
  files through `black`, and the tangled file must match the slide byte
  for byte. Keep source lines ≤ 79 characters.
- Multi-language decks just work: `autolang` infers each chunk's language
  from its filename-style name (`.py`, `.cpp`, `.sh`, …).
- Notes-only structure goes in `\mode<article>{\subsection{…}}`; slide-only
  tweaks in `\mode<presentation>{…}` (`\setminted{fontsize=\scriptsize}`,
  `[shrink]` frames, poster frames `\centering\huge\texttt{…}` — verbatim
  does not survive inside `\mode<presentation>{}`).
- Block and frame titles use `\texttt`, never `\mintinline` (it vanishes on
  slides). When the Berlin headline overflows, `\section[short]{long}`.
- didactic's `remark`/`summary`/`solution` are unnumbered, so `\cref` to
  them gives `??`, and `\cref` to an `example` prints "sats" in the beamer
  job: wrap such crefs in `\only<article>{…}`.
- Program output is embedded with PythonTeX (`\runpython[transcript]`,
  `TEX_PYTHONTEX= yes`); when both jobs share `ltxobj`, set
  `PYTHONTEXFLAGS= --interpreter python:python3 --rerun=always` so the
  second job does not reuse the first job's cache.

### Build wiring (deck Makefile)

See `helloworld/slides/Makefile`. The essentials:

- Include `${INCLUDE_MAKEFILES}/tex.mk` **and** `noweb.mk` (bottom of the
  Makefile, as usual); `LATEXFLAGS+= -shell-escape` for minted.
- `contents.tex: contents.nw` — the pattern rule weaves. `tominted` finds
  its bundled Pygments lexer itself; nothing depends on `noweb_lexer.py`.
- Explicit tangle rules `examples/%.py: contents.nw` (etc. per suffix)
  using `${NOTANGLE.py}` — the generic `%.py: %.nw` pattern does not
  match across the `examples/` directory boundary.
- `NOTANGLEFLAGS.cpp=` (empty) for teaching decks: the default `-L` would
  inject `#line` directives into the tangled C++.
- The PDFs depend on `${SRC}` (incl. `ltnotes.bib`, `sokprotokoll.tex`,
  `$(wildcard litteratursokning/*-full.tex)`) and `${EXAMPLES}` so recaps
  and hit lists are always fresh.

Build one job at a time, never both PDFs of one deck concurrently:

    make notes.pdf LATEXFLAGS="-shell-escape -interaction=nonstopmode"

Gotchas: latexmk under `-use-make` may not rerun biber after new bib keys
(`biber --output-directory ltxobj ltxobj/notes`, touch a source, make
again); a stuck "gave an error in previous invocation … Nothing to do"
needs `rm ltxobj/notes.fdb_latexmk`; a killed run leaves `ltxobj/_minted`
that hangs the next one (`rm -rf ltxobj/_minted`). The make-driven
latexmk can also stop before the final passes: if the last
`ltxobj/<job>.log` still says "Rerun to get cross-references right",
"There were undefined references" or "Please (re)run Biber", run biber
and `pdflatex … -output-directory=ltxobj <job>.tex` by hand until it does
not (on slides the symptom is blank table-of-contents frames at every
section and subsection, which didactic adds). Never combine `\pause` and
`\runpython` in one frame: the overlays re-execute the body and shift
PythonTeX's instance numbering for every later transcript.

The **makefiles submodule must be on the `tominted-default-weave`
lineage** (currently 1571556; it makes the highlighted weave the default).
In a fresh worktree run `git submodule update --init --checkout makefiles`
(`--checkout` because the repo config has `submodule.makefiles.update=none`).

### Checks before a deck is reviewed

0 `??` in `pdftotext` of both PDFs; 0 "empty citation"; no `^!` lines in
`ltxobj/*.log`; 0 `Overfull \vbox` in `ltxobj/slides.log`; `black --check` on the tangled
files under `examples/` (tracked hand-written activity inputs such as
`files/slides/examples/scb/*.py` are exempt); no source line > 79 characters; `check_provenance.py` and
`check_metadata.py` on `ltnotes.bib`; every tangled example runs; render
every slide (`pdftoppm -r 40` + `montage`) and every notes page and read
them; every margin footnote prints on the page that carries its marker
(`pdftotext -f N -l N`: the superscript numbers in the text against the
note numbers in the margin — a note pushed to the next page is a defect). Also: `pdftotext ltxobj/slides.pdf - | grep -c MINTED` = 0 (the
make can stop one pass short and leave literal `<MINTED>` placeholders on
every slide; one more pdflatex pass clears it), and `wc -l
ltxobj/notes.pytxcode ltxobj/slides.pytxcode` nearly equal (a frame that
combines `\pause` with `\runpython` doubles the slides job's PythonTeX
instances and the shared cache then prints the wrong outputs in the notes).
A permanent "Rerun to get cross-references" two-cycle from a margin
citation at a page boundary is harmless when `??` is 0.

### Driver wiring (slides.tex / notes.tex)

Both drivers load, after `\input{preamble.tex}` (and in notes after
beamerarticle):

```latex
\usepackage[minted]{noweb}
\noweboptions{breakcode}
```

`preamble.tex` carries, right after `\usepackage[...]{didactic}`,
`\extrafloats{200}` (didactic's margin footnotes and verbose `\autocite`s
are `\marginpar`s and exhaust LaTeX's float pool in citation-heavy
chapters: "Too many unprocessed floats" pages after the cause) and
`\ifdefined\setsidecappos\setsidecappos{b}\fi` (memoir `\rlap`s side
captions, so the default centred position overprints an `\ltnote` at the
same height). Figures use didactic's `sidecaption` environment,
`\begin{figure}[htbp]\centering\begin{sidecaption}{…}[fig:x]
\includegraphics…\end{sidecaption}\end{figure}` — no compat macros.

Do not load minted with the `[outputdir=...]` package option anywhere —
minted v3 (TeX Live 2024+) errors on it; plain `\usepackage{minted}` in
the preamble is fine (noweb's `[minted]` option tolerates it being loaded
already).

`slides.tex` (copy `helloworld/slides/slides.tex`) additionally:

- uses `\noweboptions{breakcode,nomargintag,noxref}` and neuters the chunk
  cross-referencing apparatus (`\def\sublabel#1{}` … `\def\nwprevnextdefs
  #1#2{}`): sub-page labels break under beamer overlays (`\pause`
  re-executes the frame body) and the defines/uses lists are noise on a
  slide;
- tells the translator package the Swedish block titles
  (`\uselanguage{Swedish}`, `\deftranslation[to=Swedish]{Example}{Exempel}`
  …) before `\usetheme`, or beamer's `example`/`definition` blocks come out
  in English;
- keeps the bibliography frame commented out — the sources belong to the
  notes.

The notes keep the full noweb apparatus: margin sub-page tags,
`⟨chunk 2a⟩≡` headers and cross-references are the point of the literate
notes (identifier lists hidden, dbosk/noweb#13).
