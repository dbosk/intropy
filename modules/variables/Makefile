SUBDIR+=		slides
SUBDIR+=		slides-functions
SUBDIR+=		tutorial
SUBDIR_GOALS=	all clean distclean

HTML_FILES= 	lecture.html pythonic.html

PANDOCFLAGS= 	--filter pandoc-xnos


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

lecture.html: lecture.md
pythonic.html: pythonic.md


.PHONY: clean
clean:
	${RM} ${HTML_FILES} ${PDF_FILES}


include ../../html.mk

INCLUDE_MAKEFILES?=../../makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
