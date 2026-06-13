.PHONY: all install lint serve build deploy generate-sample-data release-package-sample-data release-zip-sample-data release-tar-sample-data

PYTHON ?= python3
SAMPLE_DATA_VERSION ?= 0.95.0
SAMPLE_DATA_OUTPUT ?= data/sample/generated
SAMPLE_BALLOT_COUNT ?= 5
SAMPLE_BALLOT_SPOIL_RATE ?= 50

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

generate-sample-data:
	@echo 🔁 GENERATE SAMPLE DATA
	$(PYTHON) scripts/generate_sample_data.py --clean --private-data --version $(SAMPLE_DATA_VERSION) --output-dir $(SAMPLE_DATA_OUTPUT) --number-of-ballots $(SAMPLE_BALLOT_COUNT) --spoil-rate $(SAMPLE_BALLOT_SPOIL_RATE)

release-package-sample-data: generate-sample-data release-zip-sample-data release-tar-sample-data

release-zip-sample-data:
	@echo 📁 ZIP SAMPLE DATA
	zip -r sample-data.zip $(SAMPLE_DATA_OUTPUT)

release-tar-sample-data:
	@echo 📁 TAR SAMPLE DATA
	tar -czf sample-data.tar.gz $(SAMPLE_DATA_OUTPUT)
