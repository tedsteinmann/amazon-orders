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

install:
	python3 -m venv myvenv
	source myvenv/bin/activate
	pip install -r requirements.txt

start:
	source myvenv/bin/activate

build-all: build install load start

clean-all:
	rm -fr data
	rm -fr myvenv
	conda deactivate

clean:
		rm -fr data/processed

run:
	python3 main.py
