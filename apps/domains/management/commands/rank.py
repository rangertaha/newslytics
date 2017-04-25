import os.path
import time
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from time import mktime
from datetime import datetime


import hashlib
from datetime import datetime

import json
import tldextract
from bs4 import BeautifulSoup
import geograpy
from geograpy import extraction, places
import newspaper
from langdetect import detect
import feedparser

from apps.domains.models import Domain, Crawl, Feed
from apps.articles.models import Article, Language, Keyword
from apps.places.models import Place
from apps.people.models import Person


class Command(BaseCommand):
    help = 'Rank domains'

    def handle(self, *args, **options):
        pass