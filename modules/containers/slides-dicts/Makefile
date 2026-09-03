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

EXAMPLES+=	examples/phone-small.py
EXAMPLES+=	examples/nyckel_inte_index.py
EXAMPLES+=	examples/lagga_till.py
EXAMPLES+=	examples/nycklar.py
EXAMPLES+=	examples/isin.py
EXAMPLES+=	examples/isin-alt.py
EXAMPLES+=	examples/hamta.py
EXAMPLES+=	examples/genomgang.py
EXAMPLES+=	examples/sorterad.py
EXAMPLES+=	examples/search.py
EXAMPLES+=	examples/phonebook.py
EXAMPLES+=	examples/phone-big.py
# The transcript of search.py is produced by feeding it this file, so the
# run in the notes is exactly the run the reader can reproduce.
EXAMPLES+=	examples/search.in

contents.tex: contents.nw

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so the rule is spelled out here.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

# .in is not one of noweb.mk's suffixes, and the file must not be piped
# through black.
examples/search.in: contents.nw
	@mkdir -p ${@D}
	notangle -R'[[search.in]]' $< > $@

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
