SUBDIR+=		slides-lists
SUBDIR+=		slides-tuples
SUBDIR+=		slides-example-guess
SUBDIR+=		slides-sets-stacks-queues
SUBDIR+=		slides-dicts
SUBDIR+=		tutorial
SUBDIR_GOALS=	all clean distclean

HTML_FILES= 	lecture.html

PANDOCFLAGS= 	--filter pandoc-xnos


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

lecture.html: lecture.md


.PHONY: clean
clean:
	${RM} ${HTML_FILES} ${PDF_FILES}


include ../../html.mk
MAKEFILES_INCLUDE=../../makefiles
include ${MAKEFILES_INCLUDE}/subdir.mk
