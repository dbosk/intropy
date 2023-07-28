LATEXFLAGS=		-shell-escape
TEX_PYTHONTEX=	yes

.PHONY: all
all: article.pdf

article.pdf: article.tex
article.pdf: bibliography.bib
article.pdf: preamble.tex

article.pdf: introduction.tex
article.pdf: background.tex
article.pdf: method.tex
article.pdf: results-overview.tex

article.pdf: classes.tex
article.pdf: conditionals.tex
article.pdf: functions-variables.tex
article.pdf: problem-solving.tex
article.pdf: repetitions.tex
article.pdf: tools.tex
article.pdf: types.tex

.PHONY: clean
clean:
	latexmk -C
	${RM} article.bbl article.run.xml

INCLUDE_MAKEFILES?=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
