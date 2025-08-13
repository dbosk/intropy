.PHONY: all
all: notes.pdf slides.pdf

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		disciplinary.tex disciplinary.bib
SRC+=		qgame.py

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}

qgame.py: ../../../resources/questions-game/qgame.py
	${MAKE} -C $(dirname $<) $@
	ln -sf $< $@


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
