# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project does not currently cut versioned releases; changes are grouped by
date of landing on `master`.

## [Unreleased] - 2026-07-17

### Added

- Web UI templates for every app (base layout plus list/detail pages for
  articles, domains, people, places, things, crawls, and stream channels) —
  previously every non-admin page raised `TemplateDoesNotExist`.
- URL routes for the `people`, `places`, `streams`, and `crawling` apps, and a
  root URL that redirects to the article list.
- Test suite: model tests (slugs, names, language codes) and smoke tests that
  every list page renders; 14 tests running against PostgreSQL.
- GitHub Actions CI: ruff lint, Django system checks, missing-migration check,
  and the test suite on Python 3.10–3.12 with a Postgres service.
- `Makefile` with `install`, `db`, `migrate`, `run`, `test`, `lint`, `audit`,
  `lock`, `nltk-data`, and `docker-build` targets (replaces the stray empty
  `Make` file).
- `Dockerfile` (previously empty): python:3.12-slim, gunicorn, NLTK data, and
  collectstatic baked in.
- `pyproject.toml` with ruff configuration and `requirements-dev.txt` for dev
  tooling (ruff, pip-audit).
- Shared article-ingestion module `apps/news/crawl.py` — the
  `crawl_articles`, `crawl_domains`, and `get_feed_items` commands previously
  each carried their own near-identical copy of the save pipeline.
- WhiteNoise for serving static files from the app process (used by the
  Docker image).
- Language admin page (was commented out).
- Proper `README.md` and this changelog.

### Changed

- Detail pages for models without slug fields (domains, people, things,
  crawls, stream channels) are addressed by primary key instead of a slug the
  lookup could never match.
- `Article.save()` / `Place.save()` no longer regenerate the slug on every
  save; slugs are now unique, generated once, and de-duplicated with a numeric
  suffix. The migrations backfill and de-duplicate existing slugs before the
  unique constraint is added, so they apply cleanly to populated databases.
- `Language.code` widened from 4 to 8 characters so regional codes such as
  `zh-cn` returned by langdetect fit.
- `Person.name()`/`__str__` no longer render double spaces when a name part is
  missing.
- Crawl commands create articles keyed by URL only, fixing an
  `IntegrityError` when a known URL was re-crawled with a changed title;
  re-crawls now refresh the title and domain along with the content (the slug
  stays stable).
- Language detection falls back to `und` instead of crashing when langdetect
  cannot classify the text.
- `load_domains`/`clean_domains` strip whitespace and skip blank lines, so
  trailing newlines no longer corrupt stored URLs.
- Refreshed dependency lock (Django 5.2.16, django-filer 3.5.0, and other
  compatible updates); added gunicorn and whitenoise for deployment.

### Fixed

- `get_feed_items` crashed with `AttributeError` on feed entries without a
  publication date, and silently discarded articles that failed to download;
  failures are now logged to stderr and the run continues.
- `Feed.__str__` crashed the admin when a feed had no URL.
- `SocialAccount` choice typos: `linkedlin` → `linkedin` (with a data
  migration for existing rows), "Yik Yah" → "Yik Yak".

### Removed

- Duplicate `get_feed_items` command in the `domains` app (identical copy of
  the `news` one, which shadowed it anyway).
- Empty/dead command modules: `topics`, `locations`, and `live_ticker` (the
  Google/Yahoo Finance endpoints it referenced no longer exist).

### Security

- Forced `lxml >= 6.1.1` (PYSEC-2026-87, XXE local file read) and
  `lxml-html-clean >= 0.4.5` (PYSEC-2026-2614, `javascript:` URLs surviving
  cleaning) past newspaper4k's `lxml < 6` cap. See the README security note.

## Historical

- **2025–2026** — Migrated to Django 5.2 LTS and PostgreSQL via psycopg 3;
  replaced the unmaintained `newspaper` library with `newspaper4k`; stubbed
  out the Satori-based live-stream commands after the service shut down;
  introduced `requirements.lock.txt`.
- **2017-04-20** — Initial development: Django project with `news`, `domains`,
  `people`, `places`, `objects`, `crawling`, `analysis`, and `streams` apps;
  crawling via `newspaper`, RSS discovery, VADER sentiment scoring, and Satori
  live streams.
