.PHONY: all
all: article.pdf

article.pdf: article.tex
	latexmk -pdf $<

.PHONY: clean
clean:
	latexmk -C
