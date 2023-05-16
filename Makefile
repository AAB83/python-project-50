install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

gendiff-help:
	poetry run gendiff -h

gendiff:
	poetry run gendiff tests/data/file1.json tests/data/file2.json

.PHONY: install package-install build  package-reinstall lint gendiff-help gendiff
