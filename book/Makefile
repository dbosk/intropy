.PHONY: all
all: bok-larare.pdf bok.pdf

# The decks the book binds, in book order (book-body.tex has their \deck
# lines).  Paths from modules/.
DECKS+=		computational-thinking/slides
DECKS+=		helloworld/slides
DECKS+=		variables/slides-functions

DECK_DIRS=	$(addprefix ../modules/,${DECKS})

LATEXFLAGS+=	-shell-escape
TEX_PYTHONTEX=	yes
# Mentipy decks (Algoritmiskt tänkande, Hello, World!) import mentipy in
# their PythonTeX code, and the system python3 cannot (pipx isolates it), so
# PythonTeX runs in a virtualenv of the book's own, made on the first build.
# --rerun=always: both editions share ltxobj.
MENTIPY_VENV=	$(CURDIR)/.venv
PYTHONTEXFLAGS=	--interpreter python:${MENTIPY_VENV}/bin/python3 --rerun=always

${MENTIPY_VENV}/bin/python3:
	mentipy init --venv ${MENTIPY_VENV}

# Order-only: the venv must exist, but its timestamp must not rebuild.
bok.pdf bok-larare.pdf: | ${MENTIPY_VENV}/bin/python3

# Each deck weaves its contents.tex and tangles its examples/ with its own
# Makefile, so the book reads exactly what the deck's notes read.
DECK_TEX=	$(addsuffix /contents.tex,${DECK_DIRS})
${DECK_TEX}: %/contents.tex: %/contents.nw
	${MAKE} -C $* contents.tex examples

# Force the decks' weave and tangle, e.g. after examples/ was removed.
.PHONY: decks
decks:
	$(foreach d,${DECK_DIRS},${MAKE} -C ${d} contents.tex examples &&) true

DECK_SRC=	$(foreach d,${DECK_DIRS},\
		  $(wildcard ${d}/*.tex ${d}/litteratursokning/*.tex ${d}/figs/*))
DECK_SRC:=	$(filter-out %/slides.tex %/notes.tex,${DECK_SRC})

# One bibliography for the book: tex.mk's ARCHIVE.bib merges each deck's
# ltnotes.bib into this one with bibtool (sorted, duplicate keys dropped).
# It appends to what is there, so start from an empty file, or an entry
# changed in a deck would lose to its old copy.  A key must mean the same
# in every deck; phase 2 adds check_bib.py for that.
DECK_BIBS=	$(addsuffix /ltnotes.bib,${DECK_DIRS})
ltnotes.bib: ${DECK_BIBS}
	${RM} $@
	${MAKE} merge-bib
.PHONY: merge-bib
merge-bib: ltnotes.bib(${DECK_BIBS})

# A label defined in two decks resolves to the wrong one in the book.
.PHONY: check-labels
check-labels: ${DECK_TEX}
	python3 check_labels.py book-body.tex

bok.pdf bok-larare.pdf: preamble.tex book-body.tex ltnotes.bib
bok.pdf bok-larare.pdf: ${DECK_TEX} ${DECK_SRC} | check-labels
bok.pdf: bok.tex
bok-larare.pdf: bok-larare.tex


.PHONY: clean
clean:
	${RM} bok.pdf bok-larare.pdf ltnotes.bib

.PHONY: distclean
distclean: clean
	${RM} -r ltxobj ${MENTIPY_VENV}


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
