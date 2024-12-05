NOWEAVEFLAGS=-option "shift,longchunks,swedish,longxref"

.PHONY: all
all: addresses.sh addresses.pdf
all: datorprov.pdf datorprov.sh

.INTERMEDIATE: addresses.tex
addresses.pdf: addresses.sh.nw
	${NOWEAVE.pdf}

addresses.sh: addresses.sh.nw
	${NOTANGLE}
	chmod +x $@

.INTERMEDIATE: datorprov.tex
datorprov.pdf: datorprov.sh.nw
	${NOWEAVE.pdf}

datorprov.sh: datorprov.sh.nw
	${NOTANGLE}
	chmod +x $@

.PHONY: clean
clean:
	${RM} addresses.tex addresses.sh addresses.pdf
	${RM} datorprov.tex datorprov.sh datorprov.pdf

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
