SHELL := /bin/bash

.PHONY: clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-data - remove data artifacts"
	@echo "build - build out folder struction for data project."
	@echo "install - setup virtual environment and install requirements"
	@echo "load - load base classes for data manipulation"
	@echo "start - start virtual environment"


build:
	mkdir data
	mkdir data/lookup
	mkdir data/processed
	mkdir data/raw
	mkdir src
	mkdir src/classes

install:
	python3 -m venv myvenv
	source myvenv/bin/activate
	pip install -r requirements.txt

load:
	curl -o src/classes/config.py https://gist.githubusercontent.com/tedsteinmann/0af9d6c9e7caaee7c7faa7359009fe3a/raw/fdbcfec1f1ff1ba2c5c9fabc06fe49cbe0935851/config.py
	curl -o src/classes/reader.py https://gist.githubusercontent.com/tedsteinmann/0af9d6c9e7caaee7c7faa7359009fe3a/raw/fdbcfec1f1ff1ba2c5c9fabc06fe49cbe0935851/reader.py
	curl -o src/classes/writer.py https://gist.githubusercontent.com/tedsteinmann/0af9d6c9e7caaee7c7faa7359009fe3a/raw/fdbcfec1f1ff1ba2c5c9fabc06fe49cbe0935851/writer.py

start:
	source myvenv/bin/activate

build-all: build install load start

clean:
	rm -fr data
	rm -fr src
	rm -fr myvenv
	conda deactivate

clean-data:
		rm -fr data/processed
