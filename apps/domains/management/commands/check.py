import os.path
import time
import urllib2
import requests
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

import hashlib
from datetime import datetime

import json
import tldextract
from bs4 import BeautifulSoup
import geograpy
from geograpy import extraction, places
import newspaper
from langdetect import detect

from apps.domains.models import Domain, Crawl
from apps.articles.models import Article, Language, Keyword
from apps.places.models import Place
from apps.people.models import Person


class Command(BaseCommand):
    help = 'Check domains'

    def handle(self, *args, **options):
        domains = Domain.objects.filter(enabled=True)
        for domain in domains:
            self.check_domain(domain.url)

    def check_domain(self, url):
        opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
        request = opener.open(url)
        print request.url
