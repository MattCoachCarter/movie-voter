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
	echo "TODO"

#EOF
