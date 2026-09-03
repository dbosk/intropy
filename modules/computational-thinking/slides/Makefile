.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The assembled program's output is executed and embedded with PythonTeX.
TEX_PYTHONTEX=	yes

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example program is tangled from
# it.  See modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendices \input the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/pannkakor.py
# The dishwashing pseudocode is tangled too, so the notes can show the
# fully assembled algorithm (\inputminted) next to its refined form.  The
# root chunks carry no filename, so the generic [[...]] rule cannot apply.
EXAMPLES+=	examples/handdisk.txt examples/handdisk-funktion.txt

contents.tex: contents.nw

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

examples/handdisk.txt: contents.nw
	@mkdir -p ${@D}
	notangle -R'diska allt' $< > $@

examples/handdisk-funktion.txt: contents.nw
	@mkdir -p ${@D}
	notangle -R'diska allt, med funktion' $< > $@

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
