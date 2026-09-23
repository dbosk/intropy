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
# The appendices \input the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

# One line per tangled example program.  Recaps re-display these files
# with \inputminted, so they must be built before the PDFs.
EXAMPLES+=	examples/epost.py
EXAMPLES+=	examples/letters.py
EXAMPLES+=	examples/counter.py
EXAMPLES+=	examples/fraction.py
EXAMPLES+=	examples/nyckel.py
EXAMPLES+=	examples/bank.py
EXAMPLES+=	examples/banken.py
EXAMPLES+=	examples/angra.py
EXAMPLES+=	examples/ko_utan_r.py
EXAMPLES+=	examples/cowsay.py
EXAMPLES+=	examples/fortune.py
EXAMPLES+=	examples/humor.py
# The transcript of epost.py is produced by feeding it this file, so the
# run in the notes is exactly the run the reader can reproduce.
EXAMPLES+=	examples/epost.in

contents.tex: contents.nw

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so spell out one rule per suffix.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

# .in is not one of noweb.mk's suffixes, and the file must not be piped
# through black.
examples/epost.in: contents.nw
	@mkdir -p ${@D}
	notangle -R'[[epost.in]]' $< > $@

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
