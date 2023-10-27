.PHONY: all install lint serve build deploy

all: install serve

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	mkdocs --version

lint:
	mkdocs build

serve:
	mkdocs serve

build:
	mkdocs build

deploy:
	mkdocs gh-deploy --force

# To run this, ensure GITHUB_ACCESS_TOKEN environment variable set
labels:
	npm install -g github-label-sync
	github-label-sync --labels .github/labels.yml microsoft/electionguard
	github-label-sync --labels .github/labels.yml microsoft/electionguard-cpp
	github-label-sync --labels .github/labels.yml microsoft/electionguard-python
	github-label-sync --labels .github/labels.yml microsoft/electionguard-api-python
	github-label-sync --labels .github/labels.yml microsoft/electionguard-ui

release-zip-sample-data:
	@echo 📁 ZIP SAMPLE DATA
	zip -r sample-data.zip data
