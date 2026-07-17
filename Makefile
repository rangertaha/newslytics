PYTHON ?= python3
VENV   ?= .venv
PIP    := $(VENV)/bin/pip
MANAGE := $(VENV)/bin/python manage.py

.PHONY: help venv install lock nltk-data migrate run test lint audit db docker-build clean

help:            ## Show this help
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "%-14s %s\n", $$1, $$2}'

venv:            ## Create the local virtualenv
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -U pip setuptools wheel

install: venv    ## Install dependencies (including the lxml security override)
	$(PIP) install -r requirements.txt -r requirements-dev.txt
	$(PIP) install -U "lxml>=6.1.1" "lxml-html-clean>=0.4.5"

lock:            ## Re-pin requirements.lock.txt from the current venv
	$(PIP) freeze | grep -vE '^(pip|setuptools|wheel)==' > requirements.lock.txt

nltk-data:       ## Download NLTK data needed by article.nlp()
	$(VENV)/bin/python -m nltk.downloader punkt punkt_tab

migrate:         ## Apply database migrations
	$(MANAGE) migrate

run:             ## Start the development server
	$(MANAGE) runserver

test:            ## Run the test suite
	$(MANAGE) test

lint:            ## Run ruff over the project
	$(VENV)/bin/ruff check .

audit:           ## Audit installed dependencies for known vulnerabilities
	$(VENV)/bin/pip-audit

db:              ## Start a local Postgres 16 in Docker
	docker run -d --name newslytics-pg \
		-e POSTGRES_DB=newslytics -e POSTGRES_USER=newslytics \
		-e POSTGRES_PASSWORD=newslytics -p 5432:5432 postgres:16-alpine

docker-build:    ## Build the application image
	docker build -t newslytics .

clean:           ## Remove caches and build artifacts
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf .ruff_cache
