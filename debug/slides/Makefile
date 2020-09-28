.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

DEPENDS+= 	examples/multiplier.pdf
DEPENDS+= 	examples/multiplier.tex


notes.pdf: notes.tex
notes.pdf: ${SRC} ${DEPENDS}

slides.pdf: slides.tex
slides.pdf: ${SRC} ${DEPENDS}

examples/multiplier.tex examples/multiplier.pdf:
	${MAKE} -C $(dir $@) $(notdir $@)



.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${MAKE} -C examples $@



INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
