.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The programs that end are run and their terminal sessions embedded with
# PythonTeX (didactic's \runpython and \runshell), so code and output
# cannot drift apart.
TEX_PYTHONTEX=	yes
# The two jobs share ltxobj, so the second job would otherwise reuse the
# first job's PythonTeX cache.
PYTHONTEXFLAGS=	--interpreter python:python3 --rerun=always

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled from
# it.  noweb.mk provides the weave (tominted, which finds its bundled
# Pygments lexer itself) and the tangle rules.

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex
# The appendices \input the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*-full.tex)
SRC+=		ltnotes.bib
SRC+=		$(wildcard figs/*.png) $(wildcard figs/*.txt)

# One line per tangled example program.  Recaps re-display these files
# with \inputminted, so they must be built before the PDFs.
# The tkinter programs cannot be run by \runpython (they need a display
# and they do not end until the window is closed); what they do is shown
# by the screenshots and the captured session in figs/.
EXAMPLES+=	examples/events1.py
EXAMPLES+=	examples/events2.py
EXAMPLES+=	examples/helloworld.py
EXAMPLES+=	examples/hello_user1.py
EXAMPLES+=	examples/hello_user2.py
EXAMPLES+=	examples/check_greeting.py
EXAMPLES+=	examples/hello_user3.py
EXAMPLES+=	examples/hello_user4.py
# draw.py is also handed out on Canvas (the tutorial's page links to it
# on GitHub) and imported by the tutorial, so it is committed: see
# .gitignore.
EXAMPLES+=	examples/draw.py
EXAMPLES+=	examples/draw_debug.py
EXAMPLES+=	examples/draw_buttons.py

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

.PHONY: examples
examples: ${EXAMPLES}

notes.pdf: notes.tex
slides.pdf: slides.tex

notes.pdf slides.pdf: ${SRC} ${EXAMPLES}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} $(filter-out examples/draw.py,${EXAMPLES})


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
