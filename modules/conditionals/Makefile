SUBDIR+=		slides-input-exceptions
SUBDIR+=		slides-conditionals
# The tutorial is a deck of the same kind as the slides directories:
# one contents.nw building notes.pdf and slides.pdf.
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
