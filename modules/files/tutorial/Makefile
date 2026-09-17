.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The solution programs are run and their real terminal sessions
# embedded with PythonTeX, so a shown output cannot drift from the
# program that produces it.
TEX_PYTHONTEX=	yes
# Both jobs share ltxobj, so PythonTeX would otherwise reuse the first
# job's cache for the second one.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the solution programs are tangled
# from it.  Only the tangled files under examples/ are generated: the
# data files examples/madicken.txt, examples/rövare.txt and
# examples/bild.jpg are committed inputs that the exercises read, and
# examples/Makefile cleans the files the programs write when they run.
# noweb.mk provides the weave (tominted, which finds its own bundled
# Pygments lexer) and the tangle rules.  See modules/CLAUDE.md.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
SRC+=		ltnotes.bib

EXAMPLES+=	examples/filer.py
EXAMPLES+=	examples/bildkoll.py
EXAMPLES+=	examples/wc.py
EXAMPLES+=	examples/wcprov.py
EXAMPLES+=	examples/rövare.py
EXAMPLES+=	examples/rövarprov.py
EXAMPLES+=	examples/fortune.py
EXAMPLES+=	examples/fortuneprov.py
EXAMPLES+=	examples/fortune2.py
EXAMPLES+=	examples/fortune2prov.py
EXAMPLES+=	examples/analys.py
EXAMPLES+=	examples/fortunes.txt
EXAMPLES+=	examples/fortunes2.txt

contents.tex: contents.nw

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

# The two fortune databases are part of the solutions, so they are
# tangled from the same source as the programs that read them.
examples/fortunes.txt: contents.nw
	@mkdir -p ${@D}
	notangle -R'[[fortunes.txt]]' $< > $@

examples/fortunes2.txt: contents.nw
	@mkdir -p ${@D}
	notangle -R'[[fortunes2.txt]]' $< > $@

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
	${MAKE} -C examples clean


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
