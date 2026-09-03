.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs are run and their real output embedded with
# PythonTeX (didactic's \runpython[transcript]), so a shown transcript
# --- import errors and the interpreter's rename hint included ---
# cannot drift from the program that produces it.
TEX_PYTHONTEX=	yes

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled
# from it (the examples/ directory is all generated files).  noweb.mk
# provides the weave (tominted, which finds its own bundled Pygments
# lexer, so no noweb_lexer.py copy is needed here) and the tangle
# rules.  See modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendices \input the generated hit-list tables; a regenerated
# table must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib
SRC+=		figs/pypi.png figs/pypi-scipy.png

# The programs, in order of presentation.  The modules are imported by
# the programs next to them: python3 puts the script's own directory
# first on the module search path, so a run of examples/age-import.py
# finds examples/typed_input.py without any further setup.
EXAMPLES+=	examples/age.py
EXAMPLES+=	examples/dice.py
EXAMPLES+=	examples/typed_input.py
EXAMPLES+=	examples/age-import.py
EXAMPLES+=	examples/age-bare.py
EXAMPLES+=	examples/age-from.py
EXAMPLES+=	examples/age-as.py
EXAMPLES+=	examples/circle.py
EXAMPLES+=	examples/square.py
EXAMPLES+=	examples/areas-star.py
EXAMPLES+=	examples/areas.py
EXAMPLES+=	examples/hello.py
EXAMPLES+=	examples/use_hello.py
EXAMPLES+=	examples/whoami.py
EXAMPLES+=	examples/use_whoami.py
EXAMPLES+=	examples/lookup.py
EXAMPLES+=	examples/mean.py
# The shadowing example is a file named like a standard-library module.
# It lives in its own directory so that it hides the real statistics
# module only from itself, not from the other examples.
EXAMPLES+=	examples/shadow/statistics.py
EXAMPLES+=	examples/symalg.py

contents.tex: contents.nw

# The pattern matches examples/shadow/statistics.py too: with a slash
# in the pattern, % matches across directory boundaries, and the tangle
# recipe asks for the chunk named after $(notdir $@).
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

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
	${RM} -r examples/__pycache__ examples/shadow/__pycache__


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
