.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs' terminal sessions are run and embedded with
# PythonTeX (didactic's \runpython[transcript]), so code and output cannot
# drift apart.
TEX_PYTHONTEX=	yes

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled
# from it (the examples/ directory is all generated files).  noweb.mk
# provides the weave (tominted, which finds its bundled Pygments lexer
# itself) and the tangle rules.  See modules/CLAUDE.md for the pattern.

# The greeting is shown in seven languages; noweb.mk only knows tangle
# rules for some of the suffixes, so declare the rest before including it.
# (default_tangling gives each of them empty NOTANGLEFLAGS, which is what a
# teaching example wants.)  autolang infers the minted lexer from the chunk
# name: gas for .s, lean4 for .lean, javascript for .js.
NOWEB_SUFFIXES+=	.s .js .lean

# Teaching examples must match the slides byte for byte: no #line
# directives in the tangled C, C++ or Haskell.
NOTANGLEFLAGS.c=
NOTANGLEFLAGS.cpp=
NOTANGLEFLAGS.hs=

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendices \input the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/hello.s
EXAMPLES+=	examples/hello.c
EXAMPLES+=	examples/hello.cpp
EXAMPLES+=	examples/hello.hs
EXAMPLES+=	examples/hello.py
EXAMPLES+=	examples/hello.js
EXAMPLES+=	examples/hello.lean
EXAMPLES+=	examples/hello.sh
EXAMPLES+=	examples/hello-name.py
EXAMPLES+=	examples/hello-function.py
EXAMPLES+=	examples/hello-error.py

contents.tex: contents.nw

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}
examples/%.s: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.s}
examples/%.c: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.c}
examples/%.cpp: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.cpp}
examples/%.hs: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.hs}
examples/%.js: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.js}
examples/%.lean: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.lean}
examples/%.sh: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.sh}

.PHONY: examples
examples: ${EXAMPLES}

notes.pdf: notes.tex
slides.pdf: slides.tex

notes.pdf slides.pdf: ${SRC} ${EXAMPLES}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} ${EXAMPLES}


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
