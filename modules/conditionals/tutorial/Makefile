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

# noweb.mk knows tangle rules only for some suffixes; declare any others
# this deck uses before including it.  (default_tangling gives each of
# them empty NOTANGLEFLAGS, which is what a teaching example wants.)
# autolang infers the minted lexer from the chunk name.
# NOWEB_SUFFIXES+=	.s .js .lean

# Teaching examples must match the slides byte for byte: no #line
# directives in the tangled sources.  Add one line per compiled language
# the deck shows.
# NOTANGLEFLAGS.c=
# NOTANGLEFLAGS.cpp=
# NOTANGLEFLAGS.hs=

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
SRC+=		ltnotes.bib

# One line per tangled example program.  Recaps re-display these files
# with \inputminted, so they must be built before the PDFs.
EXAMPLES+=	examples/bomben.py
EXAMPLES+=	examples/tradar.py
EXAMPLES+=	examples/biobiljetter1.py
EXAMPLES+=	examples/biobiljetter2.py
EXAMPLES+=	examples/fraga.py
EXAMPLES+=	examples/fragesport.py
EXAMPLES+=	examples/vagvisare.py
EXAMPLES+=	examples/vagvisare2.py
EXAMPLES+=	examples/instruktioner.py
EXAMPLES+=	examples/korridoren.py
EXAMPLES+=	examples/korridoren2.py
EXAMPLES+=	examples/korridoren3.py

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
