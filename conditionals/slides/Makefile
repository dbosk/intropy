.PHONY: all
all: notes.pdf slides.pdf slides-more.pdf

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}

slides-more.pdf: preamble.tex abstract.tex more.tex figs/docs-strings.png
slides-more.pdf: ../../exceptions/slides/contents.tex


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
