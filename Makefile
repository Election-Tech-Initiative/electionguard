.PHONY: all install lint serve build deploy

all: install serve

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
	github-label-sync --labels .github/labels.yml Election-Tech-Initiative/electionguard
	github-label-sync --labels .github/labels.yml Election-Tech-Initiative/electionguard-cpp
	github-label-sync --labels .github/labels.yml Election-Tech-Initiative/electionguard-python
	github-label-sync --labels .github/labels.yml Election-Tech-Initiative/electionguard-api-python
	github-label-sync --labels .github/labels.yml Election-Tech-Initiative/electionguard-ui

release-zip-sample-data:
	@echo 📁 ZIP SAMPLE DATA
	zip -r sample-data.zip data
