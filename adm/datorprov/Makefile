NOWEAVEFLAGS=-option swedish

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
	${RM} *.minted
	${RM} *.aux *.fdb_latexmk *.fls *.log *.toc

INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
