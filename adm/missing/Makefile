NOWEAVEFLAGS=-option "shift,longchunks,swedish,longxref"
LATEXFLAGS=-shell-escape

.PHONY: all
all: missing.pdf missing.sh

.INTERMEDIATE: missing.tex
missing.pdf: missing.tex

missing.sh: missing.sh.nw
	${NOTANGLE}
	chmod +x $@

.PHONY: clean
clean:
	${RM} missing.tex missing.sh missing.pdf

INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
