NOWEAVEFLAGS=-option "shift,longchunks,swedish,longxref"

.PHONY: all
all: datorprov.pdf datorprov.sh

.INTERMEDIATE: datorprov.tex
datorprov.pdf: datorprov.sh.nw
	${NOWEAVE.pdf}

datorprov.sh: datorprov.sh.nw
	${NOTANGLE}
	chmod +x $@

.PHONY: clean
clean:
	${RM} datorprov.tex datorprov.sh datorprov.pdf

INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
