.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are run and their terminal sessions embedded with
# PythonTeX (didactic's \runpython).
TEX_PYTHONTEX=	yes
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled from
# it, so examples/ is entirely generated.  See modules/CLAUDE.md.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendix \inputs the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/jamforelse.py
EXAMPLES+=	examples/villkor.py
EXAMPLES+=	examples/kombinera.py
EXAMPLES+=	examples/olika.py
EXAMPLES+=	examples/temp1.py
EXAMPLES+=	examples/halka.py
EXAMPLES+=	examples/temp2.py
EXAMPLES+=	examples/fodelsear1.py
EXAMPLES+=	examples/fodelsear2.py
EXAMPLES+=	examples/temp3.py
EXAMPLES+=	examples/klader.py
EXAMPLES+=	examples/bed.py
EXAMPLES+=	examples/nedrakning.py
EXAMPLES+=	examples/rabatt.py
EXAMPLES+=	examples/gissa.py
EXAMPLES+=	examples/fraga-utan-slinga.py
EXAMPLES+=	examples/varv.py
EXAMPLES+=	examples/bed2.py

contents.tex: contents.nw

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so the tangle rule is spelled out here.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

# examples/villkor.py is the one program in the deck that must NOT parse:
# it is the demonstration of what a single equals sign in a condition
# does, and the slide shows Python's own syntax error.  The default .py
# tangle rule pipes the file through black, which cannot format a file it
# cannot parse, so this one target overrides the rule above and tangles
# raw.  It must also be excluded from the style check:
#
#     build_deck.sh --deck ... --exempt 'examples/villkor.py'
#
examples/villkor.py: contents.nw
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
