.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		./examinatorskursen.tex

notes.pdf: notes.tex didactic.sty
notes.pdf: ${SRC}

slides.pdf: slides.tex didactic.sty
slides.pdf: ${SRC}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../../../beamer-didactic
include ${INCLUDE_DIDACTIC}/didactic.mk
