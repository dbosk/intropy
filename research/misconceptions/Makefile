LATEXFLAGS=		-shell-escape
TEX_PYTHONTEX=	yes

.PHONY: all
all: article.pdf slides.pdf

SRC+=theory.bib
SRC+=misconceptions.bib
SRC+=preamble.tex

SRC+=introduction.tex
SRC+=background.tex
SRC+=method.tex

SRC+=results-overview.tex

SRC+=functions-variables.tex
SRC+=debugging.tex

SRC+=conditionals.tex
SRC+=repetitions.tex
SRC+=types.tex
SRC+=classes.tex
SRC+=problem-solving.tex
SRC+=tools.tex

DEPENDS+=	fig/contrast-color.tikz
DEPENDS+=	fig/generalization-color.tikz
DEPENDS+=	fig/fusion-color.tikz

article.pdf: article.tex ${SRC} ${DEPENDS}
slides.pdf: slides.tex ${SRC} ${DEPENDS}

.PHONY: clean
clean:
	latexmk -C
	${RM} article.bbl article.run.xml

INCLUDE_MAKEFILES?=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
