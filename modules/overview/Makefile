SUBDIR+=		slides
SUBDIR_GOALS=	all clean distclean

HTML_FILES= 	kurspm.html

PANDOCFLAGS= 	--filter pandoc-xnos


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

kurspm.html: kurspm.md


.PHONY: clean
clean:
	${RM} ${HTML_FILES} ${PDF_FILES}


include ../../html.mk

INCLUDE_MAKEFILES?=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/subdir.mk
