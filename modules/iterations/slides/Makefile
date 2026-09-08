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
# contents.tex is woven from it and every example program is tangled
# from it, so examples/ is entirely generated.  See modules/CLAUDE.md
# for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendix \inputs the generated hit-list tables; a regenerated
# table must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/hej.py
EXAMPLES+=	examples/hej_while.py
EXAMPLES+=	examples/hej_rekursion.py
EXAMPLES+=	examples/loop_text.py
EXAMPLES+=	examples/loop_variabel.py
EXAMPLES+=	examples/loop_range.py
EXAMPLES+=	examples/loop_strang.py
EXAMPLES+=	examples/inuti.py
EXAMPLES+=	examples/efter.py
EXAMPLES+=	examples/multtable.py
EXAMPLES+=	examples/rakna.py
EXAMPLES+=	examples/rabatt_while.py
EXAMPLES+=	examples/rabatt_if.py
EXAMPLES+=	examples/fakultet.py
EXAMPLES+=	examples/siffersumma.py
EXAMPLES+=	examples/fraga_rekursivt.py
EXAMPLES+=	examples/fraga_tal.py
EXAMPLES+=	examples/guess.py

contents.tex: contents.nw

# The generic %.py: %.nw pattern rule does not match across the
# examples/ directory boundary, so the tangle rule is spelled out.
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
	${RM} contents.tex noweb_lexer.py
	${RM} ${EXAMPLES}


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
