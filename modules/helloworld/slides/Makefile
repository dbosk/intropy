.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled
# from it (the examples/ directory is all generated files).  noweb.mk
# provides the weave (tominted, which finds its bundled Pygments lexer
# itself) and the tangle rules.  See modules/CLAUDE.md for the pattern.

# Teaching examples must match the slides byte for byte: no #line
# directives in the tangled C++.
NOTANGLEFLAGS.cpp=

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

EXAMPLES+=	examples/hello.py
EXAMPLES+=	examples/hello.cpp
EXAMPLES+=	examples/hello.sh
EXAMPLES+=	examples/hello-name.py
EXAMPLES+=	examples/hello-function.py

contents.tex: contents.nw

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}
examples/%.cpp: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.cpp}
examples/%.sh: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.sh}

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
