.PHONY: all
all: divider divider.pdf

CPPFLAGS+= -g

divider: divider.cpp

divider.cpp: divider.cpp.nw
	${NOTANGLE.cpp}

divider.pdf: divider.cpp.nw
	${NOWEAVE.pdf}


.PHONY: clean
clean:
	${RM} divider divider.pdf
	git restore divider.cpp


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
