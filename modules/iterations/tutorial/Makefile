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
SRC+=		ltnotes.bib

# One line per tangled example program.  Recaps re-display these files
# with \inputminted, so they must be built before the PDFs.
# The exercise that asks the reader to find the faults in a program:
EXAMPLES+=	examples/fib.py
EXAMPLES+=	examples/fib2.py
# The quiz, grown one aspect at a time:
EXAMPLES+=	examples/fragor_for.py
EXAMPLES+=	examples/fragor_while.py
EXAMPLES+=	examples/fragor_numrerade.py
EXAMPLES+=	examples/numrering.py
EXAMPLES+=	examples/forsok.py
EXAMPLES+=	examples/meny_while.py
EXAMPLES+=	examples/meny_rekursivt.py
EXAMPLES+=	examples/lagg_till.py
# The module, and the two programs that import it:
EXAMPLES+=	examples/fragor.py
EXAMPLES+=	examples/fragesport.py
EXAMPLES+=	examples/blanda.py
# The deepening exercises:
EXAMPLES+=	examples/fib_anrop.py
EXAMPLES+=	examples/fib_lista.py
EXAMPLES+=	examples/streck.py
EXAMPLES+=	examples/en_tabell.py
EXAMPLES+=	examples/alla_tabeller.py
EXAMPLES+=	examples/primtal.py
EXAMPLES+=	examples/ko.py
EXAMPLES+=	examples/cowsay.py

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
