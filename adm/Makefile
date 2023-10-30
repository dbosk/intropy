.PHONY: all
all: addresses.sh addresses.pdf

.INTERMEDIATE: addresses.tex
addresses.pdf: addresses.sh.nw
	${NOWEAVE.pdf}

addresses.sh: addresses.sh.nw
	${NOTANGLE}
	chmod +x $@

.PHONY: clean
clean:
	${RM} addresses.tex addresses.sh addresses.pdf

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
