.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are run and their real terminal sessions (the
# FileNotFoundError traceback included) embedded with PythonTeX, so a
# shown output cannot drift from the program that produces it.
TEX_PYTHONTEX=	yes
# Both jobs share ltxobj, so PythonTeX would otherwise reuse the first
# job's cache for the second one.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled
# from it.  Only the tangled files under examples/ are generated: the
# SCB data files and the two SCB programs under examples/scb/ are
# committed inputs for the SCB activity, and examples/Makefile cleans
# the files the example programs write.  noweb.mk provides the weave
# (tominted, which finds its own bundled Pygments lexer, so no
# noweb_lexer.py copy is needed here) and the tangle rules.  See
# modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
SRC+=		ltnotes.bib
SRC+=		$(wildcard figs/*.png)

EXAMPLES+=	examples/open_close.py
EXAMPLES+=	examples/tal.txt
EXAMPLES+=	examples/read_missing.py
EXAMPLES+=	examples/ask_for_file.py
EXAMPLES+=	examples/write_text.py
EXAMPLES+=	examples/read_all.py
EXAMPLES+=	examples/read_lines.py
EXAMPLES+=	examples/write_append.py
EXAMPLES+=	examples/xy.py
EXAMPLES+=	examples/xy_csv.py
EXAMPLES+=	examples/contacts_json.py

contents.tex: contents.nw

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

# The one-line data file the open/close examples read is tangled too, so
# the transcript in the notes reads exactly the file the slide shows.
examples/tal.txt: contents.nw
	@mkdir -p ${@D}
	notangle -R'[[tal.txt]]' $< > $@

.PHONY: examples
examples: ${EXAMPLES}

notes.pdf: notes.tex
slides.pdf: slides.tex

notes.pdf slides.pdf: ${SRC} ${EXAMPLES}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} ${EXAMPLES}
	${MAKE} -C examples clean


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
