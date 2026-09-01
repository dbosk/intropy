.PHONY: all
all:

SUBDIR+= 	bin
SUBDIR+= 	modules
SUBDIR_GOALS=	all clean distclean

INCLUDE_MAKEFILES=./makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
include canvas.mk
