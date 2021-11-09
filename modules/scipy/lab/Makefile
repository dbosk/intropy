.PHONY: all
all: instruction.html

instruction.html: graphs.md eqns.md
	cat $^ | pandoc -f markdown -o $@

include ../../../html.mk
