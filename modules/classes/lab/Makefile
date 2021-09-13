HTML_FILES= 	instruction.html

PANDOCFLAGS= 	--no-highlight --filter pandoc-xnos --mathml


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

instruction.html: instruction.md


.PHONY: clean
clean:
	${RM} ${HTML_FILES} ${PDF_FILES}


include ../../../html.mk

