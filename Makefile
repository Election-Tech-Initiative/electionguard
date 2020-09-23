.PHONY: all install lint serve build deploy

all: install serve

install:
	pip install --upgrade pip
	pip install mkdocs
	mkdocs --version
	pip install mkdocs-material

lint:
	mkdocs build --strict

serve:
	mkdocs serve

build:
	mkdocs build

deploy:
	mkdocs gh-deploy --force
