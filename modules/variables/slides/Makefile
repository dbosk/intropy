.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are executed and their output embedded with
# PythonTeX, so the code shown and the output shown cannot drift apart.
TEX_PYTHONTEX=	yes
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and every example program is tangled from
# it, so examples/ is entirely generated.  See modules/CLAUDE.md.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The hit lists of the search protocol are generated from the scholar
# session exports and \input by the appendix chapters.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/age.py

EXAMPLES+=	examples/state-keep.py examples/state-change.py
EXAMPLES+=	examples/state-greeting.py examples/state-recompute.py
EXAMPLES+=	examples/increment.py examples/compare.py
EXAMPLES+=	examples/division.py examples/string-number.py
EXAMPLES+=	examples/concat.py
EXAMPLES+=	examples/naming-clear.py examples/naming-opaque.py
EXAMPLES+=	examples/naming-lying.py
EXAMPLES+=	examples/comment-what.py examples/comment-why.py

contents.tex: contents.nw

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
