.PHONY: all
all: bok-larare.pdf bok.pdf

# The decks the book binds, read from the \deck lines of book-body.tex, so
# there is one list: a \deck{<module>/<deck>}{...} line, or, when \deck has
# an optional argument over several lines, its closing ]{<module>/<deck>}.
# Paths from modules/.
DECKS:=		$(shell sed -n 's/^\(\\deck\|\]\){\([^}]*\)}.*/\2/p' \
		  book-body.tex)

DECK_DIRS=	$(addprefix ../modules/,${DECKS})

LATEXFLAGS+=	-shell-escape
# didactic decides from the previous pass whether a repeated citation gets
# a margin note of its own, and a decision can move the pages after it.
# Since didactic 2.11 (footnotereuse=compact by default) and marginfix
# anchoring notes by their place in the source, a clean build of the
# student edition (603 pages) takes 7 pdflatex passes and a small edit 4;
# latexmk stops at five by default.  tex.mk's own command, with a higher
# limit.
PDFLATEX=	latexmk -pdf -use-make -8bit -e '$$max_repeat=10'
TEX_PYTHONTEX=	yes
# Mentipy decks (Algoritmiskt tänkande, Hello, World!, Repetition: kursens
# grunder) import mentipy in their PythonTeX code, and the system python3
# cannot (pipx isolates it), so PythonTeX runs in a virtualenv of the
# book's own, made on the first build.  --rerun=always: both editions
# share ltxobj.
MENTIPY_VENV=	$(CURDIR)/.venv
PYTHONTEXFLAGS=	--interpreter python:${MENTIPY_VENV}/bin/python3 --rerun=always

${MENTIPY_VENV}/bin/python3:
	mentipy init --venv ${MENTIPY_VENV}

# The recap deck imports ContextSnippet and file_snippet, which mentipy
# has since 0.13, and 0.14 shows the options before that context on the
# student's phone.  The rule above makes the venv only once, so a venv
# keeps the mentipy of its first build; a stamp named after the version
# upgrades it once.  The upgrade rebuilds the book and removes the
# PythonTeX output, which latexmk otherwise reruns only when the code
# changed.  Order-only on the venv: its timestamp must not trigger an
# upgrade.
MENTIPY_VERSION=	0.14
MENTIPY_STAMP=	${MENTIPY_VENV}/mentipy-${MENTIPY_VERSION}

${MENTIPY_STAMP}: | ${MENTIPY_VENV}/bin/python3
	${MENTIPY_VENV}/bin/python3 -m pip install 'mentipy>=${MENTIPY_VERSION}'
	${RM} ${TEX_OUTDIR}/*.pytxmcr
	touch $@

bok.pdf bok-larare.pdf: ${MENTIPY_STAMP}

# minted looks up its cache files with \IfFileExists, which under
# \subimport tries the deck's directory first.  With the decks' cache
# name, ltxobj/_minted, the book read a built deck's style and highlights:
# <MINTED> placeholders, or "grouping levels=255" on a clean build (#368).
# The book's cache is ltxobj/_minted-bok (preamble.tex).  The check: after
# a book build, the recorder's .fls lists no file read from a _minted/
# directory.  It means something only when some deck was built first:
#   make -C ../modules/recap/slides notes.pdf
#   rm -rf ltxobj && make bok-larare.pdf && make check-minted-cache
.PHONY: check-minted-cache
check-minted-cache:
	@fls="$(wildcard ltxobj/bok.fls ltxobj/bok-larare.fls)"; \
	  test -n "$$fls" || { echo "no ltxobj/bok*.fls: build the book first"; \
	    exit 1; }; \
	  if grep -H '^INPUT .*/_minted/' $$fls; then \
	    echo "the book read another document's minted cache"; exit 1; \
	  else echo "minted cache: only ltxobj/_minted-bok ($$fls)"; fi

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
# changed in a deck would lose to its old copy.  bibtool keeps one entry
# per key without looking at the others, so a key must mean the same in
# every deck: check_bib.py fails the merge when it does not.
DECK_BIBS=	$(addsuffix /ltnotes.bib,${DECK_DIRS})
ltnotes.bib: ${DECK_BIBS} book-body.tex
	python3 check_bib.py book-body.tex
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
