.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The test programs' terminal sessions are run and embedded with PythonTeX
# (didactic's \runpython[transcript]), so code and output cannot drift
# apart.
TEX_PYTHONTEX=	yes
# Both jobs share ltxobj, so the second job must not reuse the first
# job's PythonTeX cache; and the interpreter must be python3.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example program is tangled from
# it (the examples/ directory is all generated files).  noweb.mk
# provides the weave (tominted, which finds its own bundled Pygments
# lexer) and the tangle rules; the tangle rule pipes the Python file
# through black, which reads ../pyproject.toml (79 columns).  See
# modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
SRC+=		ltnotes.bib

EXAMPLES+=	examples/shopping.py
EXAMPLES+=	examples/items1.py
EXAMPLES+=	examples/shopping_with_items.py
EXAMPLES+=	examples/bank.py
# Each test case of the three class files is shown beside its output: a
# small program that imports the classes and runs just that test case (the
# earlier ones silently).  The programs are tangled from testkorningar.nw,
# which is never woven, together with contents.nw, where the test cases
# are.
TESTRUNS+=	examples/shopping_test_visa.py
TESTRUNS+=	examples/shopping_with_items_test_visa.py
TESTRUNS+=	examples/shopping_with_items_test_bocka.py
TESTRUNS+=	examples/bank_test_person.py
TESTRUNS+=	examples/bank_test_konto.py
TESTRUNS+=	examples/bank_test_uttag.py
EXAMPLES+=	${TESTRUNS}

contents.tex: contents.nw
${TESTRUNS}: testkorningar.nw

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


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
