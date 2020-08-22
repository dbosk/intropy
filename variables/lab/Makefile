HTML_FILES= 	instruktion.html

PANDOCFLAGS= 	--filter pandoc-xnos --mathml


.PHONY: all
all: ${HTML_FILES} ${PDF_FILES}

instruktion.html: instruktion.md


.PHONY: clean
clean:
	${RM} ${HTML_FILES} ${PDF_FILES}


include ../../html.mk

