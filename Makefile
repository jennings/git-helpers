TEST_FILES := $(wildcard *_test.py)

.PHONY: all
all: test

.PHONY: test
test:
	python3 ${TEST_FILES}

.PHONY: install
install:

ifeq ($(OS),Windows_NT)
	-mkdir %USERPROFILE%\bin
	echo >%USERPROFILE%\bin\git-upstream-url.cmd @python3 $(CURDIR)\git-upstream-url
else
	mkdir -p "${HOME}/bin"
	ln -fs "$(shell pwd)/git-upstream-url" "${HOME}/bin/git-upstream-url"
endif
