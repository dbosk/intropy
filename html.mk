.PHONY: html
html: ${target}
	pandoc ${PANDOCFLAGS} -t html $<

%.html: %.md
	pandoc --standalone ${PANDOCFLAGS} -o $@ $<

