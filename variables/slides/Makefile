.PHONY: all
all: notes.pdf slides.pdf

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

DEPENDS+= 	beamer-didactic.sty


notes.pdf: notes.tex
slides.pdf: slides.tex

notes.pdf slides.pdf: ${SRC} ${DEPENDS}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../..//makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
INCLUDE_BEAMERDIDACTIC=../../beamer-didactic
include ${INCLUDE_BEAMERDIDACTIC}/beamer-didactic.mk
