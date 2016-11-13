TEST_PYPI_URL := https://testpypi.python.org/pypi

test-register:
	python setup.py register -r $(TEST_PYPI_URL)

test-upload:
	python setup.py sdist upload -r $(TEST_PYPI_URL)

register:
	python setup.py register

upload:
	python setup.py sdist upload

