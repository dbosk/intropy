.PHONY: all
all: mainloop.pdf

mainloop.pdf: mainloop.svg

.PHONY: clean distclean
clean:
	${RM} mainloop.pdf mainloop.pdf_tex

distclean: clean

INCLUDE_MAKEFILES?=../../../../makefiles
include ${INCLUDE_MAKEFILES}/doc.mk
