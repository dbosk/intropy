.PHONY: all
all: gallery.pdf

# The picture gallery of pythonfigs.sty (../../pythonfigs.sty): the
# notes-layout gallery.pdf, which includes the pages of the beamer
# gallery-slides.pdf.  preamble.tex is a link to a deck's preamble, so
# the pictures render as they will in the decks.

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex pythonfigs.sty pictures.tex

gallery.pdf: gallery.tex gallery-slides.pdf ${SRC}
gallery-slides.pdf: gallery-slides.tex ${SRC}


.PHONY: clean
clean:
	${RM} gallery.pdf gallery-slides.pdf


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
