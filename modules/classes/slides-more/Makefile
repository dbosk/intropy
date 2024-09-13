.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

DEPENDS=	didactic.sty

notes.pdf: notes.tex
notes.pdf: ${SRC} ${DEPENDS}

slides.pdf: slides.tex
slides.pdf: ${SRC} ${DEPENDS}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
INCLUDE_DIDACTIC=../../../beamer-didactic
include ${INCLUDE_DIDACTIC}/didactic.mk
