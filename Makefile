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

gendiff:
	poetry run gendiff -h

.PHONY: install package-install build  package-reinstall lint gendiff
