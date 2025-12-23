.PHONY: all
all: multiplier multiplier.pdf

# must add debug flag to compiler
CPPFLAGS+= -g

multiplier: multiplier.cpp

multiplier.cpp: multiplier.cpp.nw
	${NOTANGLE.cpp}

multiplier.pdf: multiplier.cpp.nw
	${NOWEAVE.pdf}
	${RM} multiplier.tex

multiplier.tex: multiplier.cpp.nw


.PHONY: clean
clean:
	${RM} multiplier multiplier.pdf
	${RM} multiplier.cpp multiplier.tex
	${RM} multiplier.aux multiplier.fdb_latexmk multiplier.fls multiplier.log


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
