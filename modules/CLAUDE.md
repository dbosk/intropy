# Module slide decks

Each module has one or more deck directories (`slides*/`) building two PDFs
from one source: `slides.pdf` (beamer) and `notes.pdf` (article +
beamerarticle, to become memoir), both `\input`ing the shared
`contents.tex`.

## Literate decks (contents.nw)

Decks are being converted to literate programs (tracking issue #269;
`helloworld/slides` is the established template — copy from it). In a
literate deck, `contents.nw` is the single source:

- `contents.tex` is **woven** from it (`noweb.mk`'s `%.tex: %.nw` rule;
  the default weave runs the dbosk noweb fork's `autolang` + `tominted`
  pipeline, so chunks come out as syntax-highlighted `minted`
  environments).
- The presented example programs are **tangled** from it into `examples/`
  (`notangle -R"[[<filename>]]"`), so `examples/` is entirely generated.
- Consequently `.gitignore` lists `contents.tex`, `noweb_lexer.py` and
  `examples/`; only `contents.nw` is committed. Never edit `contents.tex`.

Before editing any `contents.nw`, activate the `literate-programming`
skill.

### Authoring rules for chunks in decks

- A code chunk replaces every `\inputminted[firstline=…,lastline=…]`:
  name the chunk after the file it tangles to, `<<[[hello.py]]>>=`, and
  place it at its point of presentation (inside the frame).
- Frames containing chunks (or any minted output) must be `[fragile]`.
- **Never start a theorem-style environment (`example`, `remark`, …)
  directly with a chunk or minted block** — the inline label and the code
  display overprint each other in the article/notes job. Put a short
  lead-in sentence first.
- To show the same code again later (recaps), do not redefine the chunk —
  noweb would concatenate the definitions into the tangled file. Instead
  re-display the tangled artifact: `\inputminted{python}{examples/foo.py}`
  (always the whole file, never line ranges).
- Write Python chunks black-clean (4-space indent, double quotes, two
  blank lines around top-level defs): the tangle rule pipes tangled `.py`
  files through `black`, and the tangled file must match the slide byte
  for byte.
- Multi-language decks just work: `autolang` infers each chunk's language
  from its filename-style name (`.py`, `.cpp`, `.sh`, …).

### Build wiring (deck Makefile)

See `helloworld/slides/Makefile`. The essentials:

- Include `${INCLUDE_MAKEFILES}/tex.mk` **and** `noweb.mk` (bottom of the
  Makefile, as usual).
- `contents.tex: contents.nw noweb_lexer.py` — the pattern rule weaves;
  `noweb.mk` provides the `noweb_lexer.py:` copy rule (Pygments needs the
  fork's lexer classes next to the `.tex` at compile time, so both PDFs
  also depend on `noweb_lexer.py`).
- Explicit tangle rules `examples/%.py: contents.nw` (etc. per suffix)
  using `${NOTANGLE.py}` — the generic `%.py: %.nw` pattern does not
  match across the `examples/` directory boundary.
- `NOTANGLEFLAGS.cpp=` (empty) for teaching decks: the default `-L` would
  inject `#line` directives into the tangled C++.
- The PDFs depend on `${EXAMPLES}` so `\inputminted` recaps always see
  freshly tangled files.

The **makefiles submodule must be on the `tominted-default-weave`
lineage** (it makes the highlighted weave the default and ships the
`noweb_lexer.py` rule). Note: that branch and `f870419` (biber-by-default
`tex.mk`, pinned by the files-notes work) have not been merged yet; until
they are, decks without a `.bib` see a harmless failing
`ltxobj/*.bbl` (bibtexu) sub-make under latexmk's `-use-make`.

### Driver wiring (slides.tex / notes.tex)

Both drivers load, after `\input{preamble.tex}` (and in notes after
beamerarticle):

```latex
\usepackage[minted]{noweb}
\noweboptions{breakcode}
```

Do not load minted with the `[outputdir=...]` package option anywhere —
minted v3 (TeX Live 2024+) errors on it; plain `\usepackage{minted}` in
the preamble is fine (noweb's `[minted]` option tolerates it being loaded
already).

`slides.tex` additionally neuters the chunk cross-referencing apparatus
(and uses `\noweboptions{breakcode,nomargintag}`): sub-page labels break
under beamer overlays (`\pause` re-executes the frame body, so `\sublabel`
would define every label twice) and the defines/uses lists are noise on a
slide. Copy the `\def\sublabel#1{}` … block from
`helloworld/slides/slides.tex`. The notes keep the full apparatus: margin
sub-page tags, `⟨chunk 2a⟩≡` headers and cross-references are the point
of the literate notes.
