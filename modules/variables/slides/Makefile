.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are executed and their output embedded with
# PythonTeX, so the code shown and the output shown cannot drift apart.
TEX_PYTHONTEX=	yes
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and every example program is tangled from
# it, so examples/ is entirely generated.  See modules/CLAUDE.md.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The hit lists of the search protocol are generated from the scholar
# session exports and \input by the appendix chapters.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/age.py

EXAMPLES+=	examples/state-keep.py examples/state-change.py
EXAMPLES+=	examples/state-greeting.py examples/state-recompute.py
EXAMPLES+=	examples/assign-eq-a.py examples/assign-eq-b.py
EXAMPLES+=	examples/division.py examples/division-types.py
EXAMPLES+=	examples/string-number.py
EXAMPLES+=	examples/relation.py
EXAMPLES+=	examples/concat-error.py examples/concat.py
EXAMPLES+=	examples/naming-clear.py examples/naming-opaque.py
EXAMPLES+=	examples/naming-lying.py
EXAMPLES+=	examples/comment-what.py examples/comment-why.py
EXAMPLES+=	examples/long-line.py examples/long-line-space.py

# noweb names every chunk label after the woven file (NW<hash of name>-...),
# and every deck's source is called contents.nw, so in the course book
# (book/), which binds the decks into one document, all decks would get
# the same labels.  Weave the file under its path from modules/ instead:
# it is the same file, but the name, and so the labels, are the deck's own.
NOWEB_NAME=	../../$(notdir $(abspath ..))/$(notdir ${CURDIR})/contents.nw
contents.tex: contents.nw
	noweave ${NOWEAVEFLAGS.tex} ${NOWEB_NAME} > $@

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

# The two line-break programs are tangled raw, without black: black
# rewrites a backslash continuation in an assignment into parentheses,
# which would erase the form long-line.py shows, and long-line-space.py
# does not parse at all (a space after the backslash is its point).  Both
# must also be excluded from the style check:
#
#     build_deck.sh --deck ... --exempt 'examples/long-line*.py'
#
# The space is invisible and an editor may strip it, so the build fails
# if it is gone instead of silently showing a program that runs.
examples/long-line.py: contents.nw
	@mkdir -p ${@D}
	notangle -R"[[$(@F)]]" $< | ${CPIF} $@

examples/long-line-space.py: contents.nw
	@mkdir -p ${@D}
	notangle -R"[[$(@F)]]" $< | ${CPIF} $@
	@grep -q '\\ $$' $@ || { \
	  echo "$@: the space after the backslash is gone" >&2; \
	  ${RM} $@; exit 1; }

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
