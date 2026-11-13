NOWEAVEFLAGS=-option swedish
LATEXFLAGS=-shell-escape
PYTEST?=	pytest

.PHONY: all
all: datorprov.pdf datorprov.sh dra.py dra.pdf

.INTERMEDIATE: datorprov.tex
datorprov.pdf: datorprov.tex

datorprov.sh: datorprov.sh.nw
	${NOTANGLE}
	chmod +x $@

.INTERMEDIATE: dra.tex
dra.pdf: dra.tex

dra.py: dra.nw
	${NOTANGLE.py}
	chmod +x $@

test_dra.py: dra.nw
	${NOTANGLE.py}

.PHONY: test
test: dra.py test_dra.py
	${PYTEST} -q test_dra.py

.PHONY: clean
clean:
	${RM} datorprov.tex datorprov.sh datorprov.pdf
	${RM} dra.tex dra.py dra.pdf test_dra.py
	${RM} -R __pycache__ .pytest_cache
	${RM} *.minted
	${RM} *.aux *.fdb_latexmk *.fls *.log *.toc

INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
