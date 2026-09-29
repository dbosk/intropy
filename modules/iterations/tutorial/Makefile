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
# The quiz, grown one aspect at a time; the later programs import
# fragor_for.py, and all of them input_int from typed_input.py:
EXAMPLES+=	examples/fragor_for.py
EXAMPLES+=	examples/fragor_while.py
EXAMPLES+=	examples/fragor_numrerade.py
EXAMPLES+=	examples/numrering.py
EXAMPLES+=	examples/forsok.py
EXAMPLES+=	examples/meny_while.py
EXAMPLES+=	examples/meny_rekursivt.py
EXAMPLES+=	examples/lagg_till.py
EXAMPLES+=	examples/blanda.py
# typed_input.py is written in the lecture Moduler och paket; build it
# there, copy it here.  The quiz and the deepening exercises import
# input_int from it.
examples/typed_input.py: ../../packages/slides/contents.nw
	$(MAKE) -C $(<D) examples/typed_input.py
	cp $(<D)/examples/typed_input.py $@
EXAMPLES+=	examples/typed_input.py
# The deepening exercises:
EXAMPLES+=	examples/fib_anrop.py
EXAMPLES+=	examples/fib_lista.py
EXAMPLES+=	examples/streck.py
EXAMPLES+=	examples/en_tabell.py
EXAMPLES+=	examples/alla_tabeller.py
EXAMPLES+=	examples/primtal.py
EXAMPLES+=	examples/ko.py
EXAMPLES+=	examples/cowsay.py

# noweb names every chunk label after the woven file (NW<hash of name>-...),
# and every deck's source is called contents.nw, so in the course book
# (book/), which binds the decks into one document, all decks would get
# the same labels.  Weave the file under its path from modules/ instead:
# it is the same file, but the name, and so the labels, are the deck's own.
NOWEB_NAME=	../../$(notdir $(abspath ..))/$(notdir ${CURDIR})/contents.nw
contents.tex: contents.nw
	noweave ${NOWEAVEFLAGS.tex} ${NOWEB_NAME} > $@

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so spell out one rule per suffix.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

.PHONY: examples
examples: ${EXAMPLES}

# The programs a task hands the student to run, read or build on are
# committed, because the tutorial's Canvas page (../tutorial.md) links
# them for download.  check-committed tangles each one afresh, formats it
# as the tangle rule does, and compares it with the committed copy, so a
# copy left stale by a change to contents.nw is caught.
COMMITTED+=	examples/fib.py
COMMITTED+=	examples/lagg_till.py

.PHONY: check-committed
check-committed:
	@status=0; for f in ${COMMITTED}; do \
	  notangle -R"[[$$(basename $$f)]]" contents.nw | \
	    black -q --stdin-filename $$f - | \
	    diff -u $$f - || { echo "$$f: stale" >&2; status=1; }; \
	done; exit $$status

notes.pdf: notes.tex
slides.pdf: slides.tex

notes.pdf slides.pdf: ${SRC} ${EXAMPLES}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} $(filter-out ${COMMITTED},${EXAMPLES})


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
