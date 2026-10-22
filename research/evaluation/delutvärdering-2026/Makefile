# Delutvärdering prgi26 (DD1317 HT26): rapporten med bilagor.
#
#   make                bygger rapport.pdf
#   make update-svar    hämtar svaren på nytt från Canvas och gör om bilaga B
#
# Svaren (svar-canvas.tex, bilaga.tex) checkas inte in, eftersom repot är
# publikt: de hämtas från Canvas vid första bygget. Rapporttexten räknar
# med svaren per 2026-10-07 (18 st).

.PHONY: all clean update-svar

all: rapport.pdf

rapport.pdf: rapport.tex bilaga-flippat.tex bilaga.tex litteratur.bib
	latexmk -pdf -interaction=nonstopmode rapport.tex

bilaga.tex: svar-canvas.tex bilaga.py
	python3 bilaga.py

svar-canvas.tex:
	canvaslms --no-cache quizzes analyse -c 63874 -a '^Delutvärdering$$' \
		--no-ai --format latex > $@

update-svar:
	${RM} svar-canvas.tex
	${MAKE} bilaga.tex

clean:
	latexmk -C rapport.tex
	${RM} rapport.bbl rapport.run.xml
