TEST_FILES := *_test.py

.PHONY: test
test:
	python3 ${TEST_FILES}
