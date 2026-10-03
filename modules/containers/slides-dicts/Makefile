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

EXAMPLES+=	examples/tva_listor.py
EXAMPLES+=	examples/par_lista.py
EXAMPLES+=	examples/phone-small.py
EXAMPLES+=	examples/uppslag.py
EXAMPLES+=	examples/uppslag_lista.py
EXAMPLES+=	examples/lagga_till.py
EXAMPLES+=	examples/nummer.py
EXAMPLES+=	examples/nycklar.py
EXAMPLES+=	examples/ordning.py
EXAMPLES+=	examples/avstand.py
EXAMPLES+=	examples/isin.py
EXAMPLES+=	examples/isin-alt.py
EXAMPLES+=	examples/hamta.py
EXAMPLES+=	examples/slinga.py
EXAMPLES+=	examples/genomgang.py
EXAMPLES+=	examples/sorterad.py
EXAMPLES+=	examples/search.py
EXAMPLES+=	examples/phonebook.py
EXAMPLES+=	examples/phone-big.py
EXAMPLES+=	examples/person_tupel.py
EXAMPLES+=	examples/person_uppslag.py
# phonebook.py's test program grows one test case at a time, and the
# deck shows each case's output beside it.  Each of these programs runs
# one case; they reference the test chunks in contents.nw from
# testkorningar.nw, which is never woven.
TESTRUNS+=	examples/phonebook_test_kolumner.py
TESTRUNS+=	examples/phonebook_test_lang_rad.py
EXAMPLES+=	${TESTRUNS}
# The transcript of search.py is produced by feeding it this file, so the
# run in the notes is exactly the run the reader can reproduce.
EXAMPLES+=	examples/search.in

# noweb names every chunk label after the woven file (NW<hash of name>-...),
# and every deck's source is called contents.nw, so in the course book
# (book/), which binds the decks into one document, all decks would get
# the same labels.  Weave the file under its path from modules/ instead:
# it is the same file, but the name, and so the labels, are the deck's own.
NOWEB_NAME=	../../$(notdir $(abspath ..))/$(notdir ${CURDIR})/contents.nw
contents.tex: contents.nw
	noweave ${NOWEAVEFLAGS.tex} ${NOWEB_NAME} > $@

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so the rule is spelled out here.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

${TESTRUNS}: testkorningar.nw

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
