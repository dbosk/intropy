.PHONY: all
all: notes.pdf slides.pdf

SRC+=	preamble.tex
SRC+=	abstract.tex contents.tex

SRC+=	examples/bad_module.py
SRc+= 	examples/good_module.py
SRC+=	examples/test_good_bad.py
SRC+=	examples/input_type.py

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
