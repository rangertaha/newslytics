# Newslytics

[![CI](https://github.com/rangertaha/newslytics/actions/workflows/ci.yml/badge.svg)](https://github.com/rangertaha/newslytics/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Django 5.2 LTS](https://img.shields.io/badge/django-5.2%20LTS-092e20)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A Django application for crawling news sites and analyzing what they publish.
It discovers RSS feeds, downloads and parses articles, extracts authors and
language, scores sentiment, and gives you a browsable UI plus the Django admin
over all of it.

## How it works

1. **Load domains** — seed the database with news-site domains from a text file.
2. **Discover feeds** — crawl each domain for RSS/Atom feed URLs.
3. **Fetch articles** — pull feed entries and full articles
   ([newspaper4k](https://github.com/AndyTheFactory/newspaper4k)), extracting
   title, text, authors, publish date, and language.
4. **Analyze** — score article sentiment with VADER.
5. **Browse** — explore articles, domains, people, and crawl history in the web
   UI or the admin.

## Apps

| App        | Purpose                                                              |
| ---------- | -------------------------------------------------------------------- |
| `news`     | Articles, RSS feeds, and languages                                    |
| `domains`  | News-site domains and their metadata                                  |
| `people`   | Authors and their social accounts                                     |
| `places`   | Locations mentioned in coverage                                       |
| `objects`  | Generic "things" referenced by articles                               |
| `crawling` | Crawl runs, results, and domain groups                                |
| `analysis` | Analysis commands (sentiment scoring)                                 |
| `streams`  | Real-time stream channels (dormant — the Satori service was shut down)|

## Requirements

- Python 3.10+
- PostgreSQL (required — several models use `ArrayField`)

## Quickstart

```sh
# Postgres (skip if you already have one; see environment variables below)
make db

# Virtualenv + dependencies (includes a security override, see below)
make install

# NLTK data used by article summarization
make nltk-data

# Set up the schema and an admin user
make migrate
.venv/bin/python manage.py createsuperuser

# Run it
make run    # http://127.0.0.1:8000/
```

### Environment variables

| Variable               | Default                 | Purpose                          |
| ---------------------- | ----------------------- | -------------------------------- |
| `DJANGO_SECRET_KEY`    | insecure dev key        | Set a real one in production     |
| `DJANGO_DEBUG`         | `True`                  | Set to `0`/`false` in production |
| `DJANGO_ALLOWED_HOSTS` | empty (comma-separated) | Required when `DEBUG` is off     |
| `POSTGRES_DB`          | `newslytics`            | Database name                    |
| `POSTGRES_USER`        | `newslytics`            | Database user                    |
| `POSTGRES_PASSWORD`    | `newslytics`            | Database password                |
| `POSTGRES_HOST`        | `localhost`             | Database host                    |
| `POSTGRES_PORT`        | (default)               | Database port                    |

## Crawling pipeline

```sh
# 1. Seed domains from a file (one URL per line; see data/)
./manage.py load_domains data/domains.txt

# 2. Discover RSS feeds on each domain
./manage.py crawl_feeds

# 3. Fetch articles from the discovered feeds
./manage.py get_feed_items

# 4. Or crawl domains for articles directly
./manage.py crawl_articles      # crawls domains not yet marked valid
./manage.py crawl_domains       # re-crawls domains already marked valid

# 5. Score sentiment for stored articles
./manage.py sentiment
```

Other commands: `clean_domains` (resolve redirects for a site list),
`export_domains` / `export_feeds` (dump URLs to stdout), `rank` and
`create_crawling_groups` (stubs for future work). Sample inputs live in
`data/`.

## Development

```sh
make test     # test suite (needs Postgres, e.g. `make db`)
make lint     # ruff
make audit    # pip-audit against the installed environment
make lock     # re-pin requirements.lock.txt
```

## Docker

```sh
make docker-build
docker run --rm -p 8000:8000 \
  -e DJANGO_SECRET_KEY=change-me -e DJANGO_DEBUG=0 \
  -e DJANGO_ALLOWED_HOSTS=localhost -e POSTGRES_HOST=host.docker.internal \
  newslytics
```

The image defaults to `DJANGO_DEBUG=0` and serves static files itself via
WhiteNoise; you must provide `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS`.

## Security note

`newspaper4k` currently pins `lxml < 6`, but lxml releases before 6.1 are
vulnerable to PYSEC-2026-87 (XXE local file read — relevant for a crawler that
parses untrusted markup), and `lxml-html-clean < 0.4.5` to PYSEC-2026-2614.
`make install`, CI, and the Dockerfile therefore force-upgrade both packages
past newspaper4k's cap after the normal install; newspaper4k works fine on
lxml 6.x, and pip's resolver warning about it is expected. Drop the override
once newspaper4k allows lxml ≥ 6.

## License

[MIT](LICENSE)
