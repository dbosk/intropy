.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape
# The example programs' terminal sessions are run and embedded with
# PythonTeX (didactic's \runpython), so code and output cannot drift apart.
TEX_PYTHONTEX=	yes
# Every exercise is a Mentipy question, rendered from PythonTeX.  `import
# mentipy` fails in the system python3 (pipx isolates the CLI), so
# PythonTeX runs in a deck-local virtualenv, which mentipy init creates
# (and installs mentipy into) on the first build.  The two jobs share
# ltxobj, so the second job would otherwise reuse the first job's cache.
MENTIPY_VENV=	$(CURDIR)/.venv
PYTHONTEXFLAGS=	--interpreter python:${MENTIPY_VENV}/bin/python3 --rerun=always

${MENTIPY_VENV}/bin/python3:
	mentipy init --venv ${MENTIPY_VENV}

# Order-only: the venv must exist before latexmk runs pythontex, but its
# timestamp must not trigger a rebuild.
notes.pdf slides.pdf: | ${MENTIPY_VENV}/bin/python3

# mentipy serve rewrites the QR images and their .pdf_tex sidecars (the
# address under each QR code) when the poll's address changes, so a
# rebuilt slide deck must follow them.  The wildcard is empty until the
# first build has written them, which is fine: that build makes them.
notes.pdf slides.pdf: $(wildcard mentipy-obj/Q-*.pdf_tex)

# The deck is a literate program: contents.nw is the single source.
# contents.tex is woven from it and the example programs are tangled from
# it (the examples/ directory is all generated files).

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex bilaga-repetition.tex bilaga-flippat.tex
# The appendices \input the generated hit-list tables; a regenerated table
# must trigger a rebuild even when no .tex source changed.
SRC+=		$(wildcard litteratursokning/*.tex)
SRC+=		ltnotes.bib
# The pictures: the shared package, and the gallery's picture macros that
# the deck reuses (contents.nw \inputs them).
SRC+=		pythonfigs.sty ../gallery/pictures.tex

# One line per tangled example program, in the order the deck shows them.
EXAMPLES+=	examples/valkommen.py
EXAMPLES+=	examples/temperatur.py
EXAMPLES+=	examples/saldo.py
EXAMPLES+=	examples/insattning1.py
EXAMPLES+=	examples/insattning2.py
EXAMPLES+=	examples/inmatning1.py
EXAMPLES+=	examples/inmatning2.py
EXAMPLES+=	examples/uttag1.py
EXAMPLES+=	examples/uttag2.py
EXAMPLES+=	examples/summa.py
EXAMPLES+=	examples/pin.py
EXAMPLES+=	examples/lista.py
EXAMPLES+=	examples/tupel1.py
EXAMPLES+=	examples/tupel2.py
EXAMPLES+=	examples/konto1.py
EXAMPLES+=	examples/kassa1.py
EXAMPLES+=	examples/konton1.py
EXAMPLES+=	examples/konton2.py
EXAMPLES+=	examples/bank.py
EXAMPLES+=	examples/objekt.py
EXAMPLES+=	examples/behallare.py
EXAMPLES+=	examples/belopp1.py
EXAMPLES+=	examples/belopp2.py
EXAMPLES+=	examples/sparkonto.py
EXAMPLES+=	examples/banken.py
EXAMPLES+=	examples/fil1.py
EXAMPLES+=	examples/fil2.py
EXAMPLES+=	examples/bankomat.py
EXAMPLES+=	examples/uttagsprov.py
EXAMPLES+=	examples/pilar.py

# noweb names every chunk label after the woven file, and every deck's
# source is called contents.nw, so in the course book all decks would get
# the same labels.  Weave the file under its path from modules/ instead:
# the same file, but the labels are the deck's own.
NOWEB_NAME=	../../$(notdir $(abspath ..))/$(notdir ${CURDIR})/contents.nw
contents.tex: contents.nw
	noweave ${NOWEAVEFLAGS.tex} ${NOWEB_NAME} > $@

# The generic %.py: %.nw pattern does not match across the examples/
# directory boundary, so spell out the rule.
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
