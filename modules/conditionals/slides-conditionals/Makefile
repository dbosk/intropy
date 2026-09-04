.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are run and their terminal sessions embedded with
# PythonTeX (didactic's \runpython).
TEX_PYTHONTEX=	yes
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled from
# it, so examples/ is entirely generated.  See modules/CLAUDE.md.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendix \inputs the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/olika.py
EXAMPLES+=	examples/olika-fel.py
EXAMPLES+=	examples/temp-varmt.py
EXAMPLES+=	examples/temp-kallt.py
EXAMPLES+=	examples/temp-elif.py
EXAMPLES+=	examples/temp-fusion.py
EXAMPLES+=	examples/fodelsear-fel.py
EXAMPLES+=	examples/fodelsear.py
EXAMPLES+=	examples/bed.py
EXAMPLES+=	examples/nedrakning.py
EXAMPLES+=	examples/rabatt-if.py
EXAMPLES+=	examples/rabatt-while.py
EXAMPLES+=	examples/gissa.py
EXAMPLES+=	examples/fraga-utan-slinga.py

contents.tex: contents.nw

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so the tangle rule is spelled out here.
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
