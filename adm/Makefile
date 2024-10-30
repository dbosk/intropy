.PHONY: all
all: addresses.sh addresses.pdf
all: bonus.sh bonus.pdf

.INTERMEDIATE: addresses.tex
addresses.pdf: addresses.sh.nw
	${NOWEAVE.pdf}

addresses.sh: addresses.sh.nw
	${NOTANGLE}
	chmod +x $@

.INTERMEDIATE: bonus.tex
bonus.pdf: bonus.sh.nw
	${NOWEAVE.pdf}

bonus.sh: bonus.sh.nw
	${NOTANGLE}
	chmod +x $@

.PHONY: clean
clean:
	${RM} addresses.tex addresses.sh addresses.pdf
	${RM} bonus.tex bonus.sh bonus.pdf

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
