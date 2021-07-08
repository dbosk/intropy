.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

DEPENDS+=	examples/helloworld.py
DEPENDS+=	examples/hello_user_bad.py
DEPENDS+=	examples/hello_user_good.py
DEPENDS+=	examples/hello_user_counter.py
DEPENDS+=	examples/hello_user_better.py
DEPENDS+=	examples/hello_user_even_better.py
DEPENDS+=	examples/draw.py
DEPENDS+=	examples/draw_debug.py
DEPENDS+=	examples/draw_colors.py

notes.pdf: notes.tex
notes.pdf: ${SRC} ${DEPENDS}

slides.pdf: slides.tex
slides.pdf: ${SRC} ${DEPENDS}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
