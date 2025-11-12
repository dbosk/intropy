LATEXFLAGS+=	-shell-escape
TEX_PYTHONTEX=	yes

.PHONY: all
all: notes.pdf slides.pdf

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
