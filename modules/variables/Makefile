SUBDIR+=		slides
SUBDIR_GOALS=	all clean distclean

HTML_FILES= 	lecture.html exercise.html tutorial.html

PANDOCFLAGS= 	--filter pandoc-xnos


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

lecture.html: lecture.md
exercise.html: exercise.md
tutorial.html: tutorial.md


.PHONY: clean
clean:
	${RM} ${HTML_FILES} ${PDF_FILES}


include ../../html.mk

INCLUDE_MAKEFILES?=../../makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
