.PHONY: all
all: article.pdf

article.pdf: bibliography.bib
article.pdf: classes.tex
article.pdf: conditionals.tex
article.pdf: functions-variables.tex
article.pdf: problem-solving.tex
article.pdf: repetitions.tex
article.pdf: tools.tex
article.pdf: types.tex

article.pdf: article.tex
	latexmk -pdf $<

.PHONY: clean
clean:
	latexmk -C
	${RM} article.bbl article.run.xml
