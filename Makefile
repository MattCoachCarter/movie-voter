SOURCES     = $(wildcard src/*.py)
DOC_SOURCES = $(wildcard docs/* docs/*/*)
MANIFEST    = $(SOURCES) $(wildcard *.py api/*.* AUTHORS* README* LICENSE*)
VERSION     = 0.1
PRODUCT     = MANIFEST doc
OS          = `uname -s | tr A-Z a-z`

.PHONY: clean test

test:
	PYTHONPATH=src:$(PYTHONPATH) pytest

clean:
	find . -name __pycache__ | xargs rm -rf
	find . -name '*.pyc' | xargs rm -rf

#EOF
