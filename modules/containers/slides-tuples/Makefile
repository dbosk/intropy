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

EXAMPLES+=	examples/tupler.py
EXAMPLES+=	examples/tupel1.py
EXAMPLES+=	examples/uppackning.py
EXAMPLES+=	examples/fullname.py
EXAMPLES+=	examples/fullname-alt.py
EXAMPLES+=	examples/my_enumerate.py
EXAMPLES+=	examples/tuples.py
EXAMPLES+=	examples/numrering.py

contents.tex: contents.nw

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so the rule is spelled out here.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

# examples/fullname-alt.py exists to show the optional parentheses around
# the unpacking, `(first, last) = ...` and `return (firstname, lastname)`.
# The default .py tangle rule pipes the file through black, which strips
# exactly those parentheses, so the program on the slide and the program
# that ran would differ.  This target tangles raw; the file must also be
# excluded from the style check:
#
#     build_deck.sh --deck ... --exempt 'examples/fullname-alt.py'
#
examples/fullname-alt.py: contents.nw
	@mkdir -p ${@D}
	notangle -R"[[$(@F)]]" $< | ${CPIF} $@

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
