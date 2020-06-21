TEST_FILES := *_test.py

.PHONY: all
all: test

.PHONY: test
test:
	python3 ${TEST_FILES}

.PHONY: install
install:
	mkdir -p "${HOME}/bin"
	ln -fs "$(shell pwd)/git-upstream-url" "${HOME}/bin/git-upstream-url"
