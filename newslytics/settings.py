"""
Django settings for the newslytics project.

https://docs.djangoproject.com/en/5.2/topics/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-w3u9g1h_w_(^8dt)grmpz)v6a7+ge%ws5_1p$3lh2xp2lesnxo",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() in ("1", "true", "yes")

ALLOWED_HOSTS = [
    h for h in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",") if h
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "apps.news",
    "apps.people",
    "apps.places",
    "apps.streams",
    "apps.objects",
    "apps.domains",
    "apps.analysis",
    "apps.crawling",

    "filer",
    "easy_thumbnails",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "newslytics.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "newslytics" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "newslytics.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
#
# PostgreSQL is required because several models use ArrayField.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "newslytics"),
        "USER": os.environ.get("POSTGRES_USER", "newslytics"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "newslytics"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", ""),
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "static"

# WhiteNoise serves STATIC_ROOT from the app process (used in the Docker
# image, where no separate web server sits in front of gunicorn).
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# django-filer / easy-thumbnails

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)
