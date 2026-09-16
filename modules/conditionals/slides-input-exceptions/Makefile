.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are run and their terminal sessions embedded with
# PythonTeX (didactic's \runpython).  The tracebacks in the second half
# are produced by the tangled programs themselves, so a shown error
# message cannot drift from the code that raises it.
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

EXAMPLES+=	examples/age1.py
EXAMPLES+=	examples/age2.py
EXAMPLES+=	examples/plus1.py
EXAMPLES+=	examples/plus2.py
EXAMPLES+=	examples/heltalsdivision.py
EXAMPLES+=	examples/strangoperationer.py
EXAMPLES+=	examples/strangmetoder.py
EXAMPLES+=	examples/age3.py
EXAMPLES+=	examples/age-try.py
EXAMPLES+=	examples/age-isdigit.py
EXAMPLES+=	examples/average.py
EXAMPLES+=	examples/age-catchall.py
EXAMPLES+=	examples/age-raise.py

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
