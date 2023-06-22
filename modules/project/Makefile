.PHONY: all
all: present.html review.html spec.html granskningsprotokoll.md

granskningsprotokoll.md: granskningsprotokoll.odt
	pandoc $< -o $@

include ../../html.mk
