.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs' terminal sessions are run and embedded with
# PythonTeX (didactic's \runpython[transcript]), so code and output cannot
# drift apart.
TEX_PYTHONTEX=	yes
# The two jobs share ltxobj, so the second job would otherwise reuse the
# first job's PythonTeX cache.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled from
# it (the examples/ directory is all generated files).  noweb.mk provides
# the weave (tominted, which finds its bundled Pygments lexer itself) and
# the tangle rules.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendices \input the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

# One line per tangled example program.  Recaps re-display these files
# with \inputminted, so they must be built before the PDFs.
# The tkinter programs cannot be run by \runpython (they need a display and
# they never terminate); their results are the screenshots in figs/.
EXAMPLES+=	examples/term_clock.py
EXAMPLES+=	examples/overwrite.py
EXAMPLES+=	examples/clock_loop.py
EXAMPLES+=	examples/clock.py
EXAMPLES+=	examples/countdown.py
EXAMPLES+=	examples/timer.py
EXAMPLES+=	examples/draw_colors.py
EXAMPLES+=	examples/draw_rect.py

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


# PROJECT: adjust the relative path to the shared makefiles submodule.
INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
