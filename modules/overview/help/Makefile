HTML_FILES= 	help.html

PANDOCFLAGS= 	--filter pandoc-xnos


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

help.html: help.md
help.html: invite.png new-meeting.png participants.png queue.png


.PHONY: clean
clean:
	${RM} ${HTML_FILES}


include ../../../html.mk

