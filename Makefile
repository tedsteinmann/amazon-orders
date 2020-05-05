SHELL := /bin/bash

.PHONY: clean

help:
	@echo "build - build out folder struction for data project."
	@echo "install - setup virtual environment and install requirements"
	@echo "start - start virtual environment"
	@echo "build-all - build out folder struction for data project."
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-data - remove data all artifacts"
	@echo "run - run program"

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

build-all: build install start

clean:
	rm -fr data/processed

clean-data:
	rm -rI data
	rm -fr myvenv

run:
	python3 main.py
