NOWEAVEFLAGS=-option "shift,longchunks,swedish,longxref"
LATEXFLAGS=-shell-escape

.PHONY: all
all: redovisningar.pdf redovisningar.sh

.INTERMEDIATE: redovisningar.tex
redovisningar.pdf: redovisningar.tex

redovisningar.sh: redovisningar.sh.nw
	${NOTANGLE}
	chmod +x $@

.PHONY: clean
clean:
	${RM} redovisningar.tex redovisningar.sh redovisningar.pdf

INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
