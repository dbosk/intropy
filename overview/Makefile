HTML_FILES= 	kurspm.html help.html
#PDF_FILES= 		slides.pdf

PANDOCFLAGS= 	--filter pandoc-xnos


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

kurspm.html: kurspm.md
help.html: help.md
help.html: invite.png new-meeting.png participants.png queue.png
#slides.pdf: slides.tex contents.tex preamble.tex slides.tex


.PHONY: clean
clean:
	${RM} ${HTML_FILES} ${PDF_FILES}


include ../html.mk

INCLUDE_MAKEFILES?=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
