.PHONY: all
all: qgame.pdf

LATEXFLAGS+=	-shell-escape

qgame.pdf: qgame.tex
qgame.tex: qgame.nw


.PHONY:
all: qgame.py

qgame.py: qgame.nw
	${NOTANGLE.py}
	black $@


.PHONY: clean
clean:
	${RM} qgame.py qgame.pdf qgame.tex


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
