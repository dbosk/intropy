.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are executed and their output embedded with
# PythonTeX, so the code shown and the output shown cannot drift apart.
TEX_PYTHONTEX=	yes

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and every example program is tangled from
# it, so examples/ is entirely generated.  See modules/CLAUDE.md.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendix \inputs the generated hit-list table; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/age-repeat.py examples/age-funcs.py
EXAMPLES+=	examples/add.py
EXAMPLES+=	examples/sum-variable.py examples/sum-function.py
EXAMPLES+=	examples/defined-only.py examples/defined-and-called.py
EXAMPLES+=	examples/return-value.py examples/print-value.py
EXAMPLES+=	examples/return-ends.py examples/return-last.py
EXAMPLES+=	examples/degrees.py
EXAMPLES+=	examples/welcome.py
EXAMPLES+=	examples/scope-same-names.py examples/scope-other-names.py
EXAMPLES+=	examples/hello.py examples/hello-default.py

contents.tex: contents.nw

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
