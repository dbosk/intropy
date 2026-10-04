.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# Every example program's terminal session is run and embedded with
# PythonTeX (didactic's \runpython), so the solutions' code and their
# output cannot drift apart.
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
SRC+=		ltnotes.bib

# One line per tangled solution program.  The last section re-displays
# these files with \inputminted, so they must be built before the PDFs.
EXAMPLES+=	examples/book.py
EXAMPLES+=	examples/read500.py
EXAMPLES+=	examples/trace.py
EXAMPLES+=	examples/shelf.py
EXAMPLES+=	examples/copies.py
EXAMPLES+=	examples/same.py
EXAMPLES+=	examples/review.py
EXAMPLES+=	examples/review_better.py
EXAMPLES+=	examples/plain.py
EXAMPLES+=	examples/borrowed.py

# The class files' test programs grow one test case at a time, and the
# deck shows each case's output beside it.  Each of these programs runs
# one case (after the earlier ones, silenced); they reference the test
# chunks in contents.nw from testkorningar.nw, which is never woven.
TESTRUNS+=	examples/book_test_utskrift.py
TESTRUNS+=	examples/book_test_lasning.py
TESTRUNS+=	examples/book_test_ordning.py
TESTRUNS+=	examples/book_test_likhet.py
TESTRUNS+=	examples/borrowed_test_utskrift.py
EXAMPLES+=	${TESTRUNS}

# The dictionary that the representation exercise shows beside the
# class's constructor (\codebycode reads both sides from files); it is
# tangled from testkorningar.nw too, so it is shown only once.
EXAMPLES+=	examples/book_dict.py

# noweb names every chunk label after the woven file (NW<hash of name>-...),
# and every deck's source is called contents.nw, so in the course book
# (book/), which binds the decks into one document, all decks would get
# the same labels.  Weave the file under its path from modules/ instead:
# it is the same file, but the name, and so the labels, are the deck's own.
NOWEB_NAME=	../../$(notdir $(abspath ..))/$(notdir ${CURDIR})/contents.nw
contents.tex: contents.nw
	noweave ${NOWEAVEFLAGS.tex} ${NOWEB_NAME} > $@

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so spell out one rule per suffix.
examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

${TESTRUNS} examples/book_dict.py: testkorningar.nw

# plain.py writes out the methods PlainBook shares with Book instead of
# reusing their chunks, since the task has the student read the class
# whole; the notes say the two are word for word the same.  So that the
# copies cannot drift apart, its tangle compares each method of
# PlainBook with Book's, and fails (removing the file) if they differ.
define CHECK_PLAIN_PY
import ast
import sys

def methods(path, name):
    source = open(path, encoding="utf-8").read()
    for node in ast.parse(source).body:
        if isinstance(node, ast.ClassDef) and node.name == name:
            return {method.name: ast.get_source_segment(source, method)
                    for method in node.body
                    if isinstance(method, ast.FunctionDef)}
    return {}

plain = methods("examples/plain.py", "PlainBook")
book = methods("examples/book.py", "Book")
differ = [name for name in plain if plain[name] != book.get(name)]
if differ:
    sys.exit("examples/plain.py: PlainBook differs from Book in "
             + ", ".join(differ))
endef
export CHECK_PLAIN_PY

examples/plain.py: contents.nw examples/book.py
	@mkdir -p ${@D}
	${NOTANGLE.py}
	@python3 -c "$$CHECK_PLAIN_PY" || { ${RM} $@; exit 1; }

.PHONY: examples
examples: ${EXAMPLES}

# The programs a task hands the student to run, read or build on are
# committed, because the tutorial's Canvas page (../tutorial.md) links
# them for download.  check-committed tangles each one afresh, formats it
# as the tangle rule does, and compares it with the committed copy, so a
# copy left stale by a change to contents.nw is caught.
COMMITTED+=	examples/trace.py
COMMITTED+=	examples/review.py

.PHONY: check-committed
check-committed:
	@status=0; for f in ${COMMITTED}; do \
	  notangle -R"[[$$(basename $$f)]]" contents.nw | \
	    black -q --stdin-filename $$f - | \
	    diff -u $$f - || { echo "$$f: stale" >&2; status=1; }; \
	done; exit $$status

notes.pdf: notes.tex
slides.pdf: slides.tex

notes.pdf slides.pdf: ${SRC} ${EXAMPLES}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} $(filter-out ${COMMITTED},${EXAMPLES})


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
