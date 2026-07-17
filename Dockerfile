FROM python:3.12-slim

# Production defaults: DEBUG off; DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS
# must be provided at runtime. Static files are served by WhiteNoise.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_DEBUG=0

WORKDIR /app

COPY requirements.txt requirements.lock.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    # Security override past newspaper4k's lxml<6 cap (see requirements.txt)
    && pip install --no-cache-dir -U "lxml>=6.1.1" "lxml-html-clean>=0.4.5" \
    && python -m nltk.downloader -d /usr/local/share/nltk_data punkt punkt_tab

COPY . .

RUN DJANGO_SECRET_KEY=collectstatic-placeholder \
    python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "newslytics.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
