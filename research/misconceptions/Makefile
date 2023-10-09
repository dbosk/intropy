.PHONY: all
all: article.pdf

article.pdf: article.tex
	latexmk -shell-escape -pdf $<

article.pdf: abstract.tex
article.pdf: bibliography.bib
article.pdf: preamble.tex
article.pdf: classes.tex
article.pdf: conditionals.tex
article.pdf: functions-variables.tex
article.pdf: problem-solving.tex
article.pdf: repetitions.tex
article.pdf: tools.tex
article.pdf: types.tex
article.pdf: background.tex
article.pdf: introduction.tex
article.pdf: method.tex

.PHONY: clean
clean:
	latexmk -C
	${RM} article.bbl article.run.xml
