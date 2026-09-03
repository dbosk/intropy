.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are run and their output embedded with PythonTeX.
TEX_PYTHONTEX=	yes

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled from
# it (the examples/ directory is all generated files).  See
# modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
SRC+=		ltnotes.bib

EXAMPLES+=	examples/namnlista.py
EXAMPLES+=	examples/langd.py
EXAMPLES+=	examples/skivning.py
EXAMPLES+=	examples/byt.py
EXAMPLES+=	examples/extend_lists.py
EXAMPLES+=	examples/ta_bort.py
EXAMPLES+=	examples/alias.py
EXAMPLES+=	examples/likhet.py
EXAMPLES+=	examples/genomgang.py
EXAMPLES+=	examples/andra_under.py
EXAMPLES+=	examples/andra_ratt.py
EXAMPLES+=	examples/listbyggare.py
EXAMPLES+=	examples/isin.py
EXAMPLES+=	examples/search.py
EXAMPLES+=	examples/partial_search.py
EXAMPLES+=	examples/sortera.py
EXAMPLES+=	examples/strang_sortering.py
EXAMPLES+=	examples/sorterings_nyckel.py

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
