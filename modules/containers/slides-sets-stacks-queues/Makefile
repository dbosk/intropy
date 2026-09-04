.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are run and their output embedded with PythonTeX.
TEX_PYTHONTEX=	yes
# notes and slides share one output directory, so they share PythonTeX's
# cache (ltxobj/pythontex_data.pkl).  Without --rerun=always the second job
# built finds everything cached, writes no <job>.pytxmcr, and latexmk's
# custom dependency then fails with "did not make the destination" on every
# subsequent run.  The programs are tiny, so rerunning them is cheap.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled from
# it (the examples/ directory is all generated files).  See
# modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
SRC+=		ltnotes.bib

EXAMPLES+=	examples/mangder.py
EXAMPLES+=	examples/mangdoperationer.py
EXAMPLES+=	examples/pile.py
EXAMPLES+=	examples/queue.py
EXAMPLES+=	examples/diska.py

contents.tex: contents.nw

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so the rule is spelled out here.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

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
