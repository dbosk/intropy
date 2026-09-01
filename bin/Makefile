PYTEST?=	pytest

.PHONY: all
all: veckoschema.py veckoschema.pdf

veckoschema.py: veckoschema.nw

test_veckoschema.py: veckoschema.nw
	notangle -R'[[$@]]' $< | ${CPIF} $@ && black $@

veckoschema.tex: veckoschema.nw
veckoschema.pdf: veckoschema.tex preamble.tex

.PHONY: test
test: veckoschema.py test_veckoschema.py
	${PYTEST} -q test_veckoschema.py

.PHONY: clean
clean:
	${RM} veckoschema.pdf veckoschema.tex test_veckoschema.py
	${RM} -R __pycache__ .pytest_cache

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
