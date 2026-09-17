.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# Every example program's terminal session is run and embedded with
# PythonTeX (didactic's \runpython), so the solutions' code and their
# output cannot drift apart.
TEX_PYTHONTEX=	yes
# Both jobs share ltxobj, so the second job must not reuse the first
# job's PythonTeX cache; and the interpreter must be python3.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled
# from it (the examples/ directory is all generated files).  noweb.mk
# provides the weave (tominted, which finds its own bundled Pygments
# lexer) and the tangle rules; the tangle rule pipes the Python files
# through black, which reads ../pyproject.toml (79 columns).  See
# modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
SRC+=		ltnotes.bib

# One line per tangled solution program.  The last section re-displays
# these files with \inputminted, so they must be built before the PDFs.
EXAMPLES+=	examples/book.py
EXAMPLES+=	examples/read500.py
EXAMPLES+=	examples/trace1.py
EXAMPLES+=	examples/trace2.py
EXAMPLES+=	examples/shelf.py
EXAMPLES+=	examples/same.py
EXAMPLES+=	examples/review.py
EXAMPLES+=	examples/review_better.py
EXAMPLES+=	examples/borrowed.py

contents.tex: contents.nw

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so spell out one rule per suffix.
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
