.SILENT:

all: clean build upload

clean:
	rm -rf *.egg-info build dist

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

.PHONY: all clean build upload
