.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled
# from it (the examples/ directory is all generated files).  noweb.mk
# provides the weave (tominted, so the PDFs need the Pygments lexer
# classes in ${NOWEB_LEXER} at compile time) and the tangle rules.

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

contents.tex: contents.nw noweb_lexer.py

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

notes.pdf slides.pdf: ${SRC} ${EXAMPLES} noweb_lexer.py


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex noweb_lexer.py
	${RM} ${EXAMPLES}


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
