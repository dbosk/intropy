.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=	preamble.tex
SRC+=	abstract.tex contents.tex

SRC+=	examples/any-all.py
SRC+=	examples/enum.py
SRC+=	examples/filtering.py
SRC+=	examples/filter-lambda.py
SRC+=	examples/filter-lists.py
SRC+=	examples/filter-strings.py
SRC+=	examples/filter-strints.py
SRC+=	examples/func.py
SRC+=	examples/input-int-default.py
SRC+=	examples/input-int.py
SRC+=	examples/input-type.py
SRC+=	examples/mapping-own.py
SRC+=	examples/mapping.py
SRC+=	examples/summera.py
SRC+=	examples/zip.py

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
