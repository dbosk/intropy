.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# Two of the example programs are run and their terminal sessions
# embedded with PythonTeX (didactic's \runpython), so code and output
# cannot drift apart.
TEX_PYTHONTEX=	yes
# Both jobs share ltxobj, so the second job must not reuse the first
# job's PythonTeX cache; and the interpreter must be python3.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled
# from it (the examples/ directory is all generated files).  noweb.mk
# provides the weave (tominted, which finds its own bundled Pygments
# lexer) and the tangle rules; the tangle rule pipes the Python files
# through black, which reads ../pyproject.toml (79 columns).  See
# modules/CLAUDE.md for the pattern.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendices \input the generated hit-list tables; a regenerated
# table must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib

EXAMPLES+=	examples/phonebook.py
EXAMPLES+=	examples/contacts.py
EXAMPLES+=	examples/person.py
EXAMPLES+=	examples/contacts_class.py
EXAMPLES+=	examples/public.py
EXAMPLES+=	examples/person_nick.py
EXAMPLES+=	examples/private.py
EXAMPLES+=	examples/two.py
EXAMPLES+=	examples/compare.py

# The class files' test programs grow one test case at a time, and the
# deck shows each case's output beside it.  Each of these programs runs
# one case (after the earlier ones, silenced); they reference the test
# chunks in contents.nw from testkorningar.nw, which is never woven.
TESTRUNS+=	examples/person_test_utskrift.py
TESTRUNS+=	examples/person_test_namnbyte.py
TESTRUNS+=	examples/person_test_sortering.py
TESTRUNS+=	examples/person_nick_test_metoder.py
EXAMPLES+=	${TESTRUNS}

contents.tex: contents.nw

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

${TESTRUNS}: testkorningar.nw

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
