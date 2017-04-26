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
from apps.articles.models import Article, Language
from apps.places.models import Place
from apps.people.models import Person


class Command(BaseCommand):
    help = 'Get feed items'

    def handle(self, *args, **options):
        feeds = Feed.objects.all()
        for feed in feeds:
            d = feedparser.parse(feed.url)
            for i in d.entries:
                self.crawl(url=i.link, datetime=i.published_parsed)

    def crawl(self, url=None, datetime=None, memoize=False):
        try:
            article = newspaper.Article(url=url)
            article.build()
            self.save(datetime, article)
        except Exception as e:
            pass
            # print e

    def save(self, dtime, article):
        language, created = Language.objects.get_or_create(
            code=self._language(article)
        )
        sub, dm, suffix = self._domain(article)
        domain, created = Domain.objects.get_or_create(
            sub=sub, domain=dm, suffix=suffix)
        print article.url
        atcl, created = Article.objects.get_or_create(
            url=article.url,
            domain=domain,
            title=article.title)

        atcl.description = article.summary
        atcl.text = article.text
        atcl.html = article.html
        atcl.published = self._published(article, dtime)
        atcl.language = language

        for person in self._authors(article):
            atcl.authors.add(person)

        # for keyword in self._keywords(article):
        #     atcl.keywords.add(keyword)

        # for location in self._locations(article):
        #     article.places.add(location)

        # print atcl.title
        atcl.save()

    def _published(self, article, dtime):
        if dtime:
            return datetime.fromtimestamp(mktime(dtime))
        if article.publish_date:
            return article.publish_date
        return

    def _language(self, article):
        if not article.meta_lang:
            text = article.title + ' ' + article.summary
            return detect(text)
        return article.meta_lang

    def _authors(self, article):
        for author in article.authors:
            person, created = Person.objects.get_or_create(first=author)
            yield person

    # def _keywords(self, article):
    #     for keyword in article.keywords:
    #         word, created = Keyword.objects.get_or_create(word=keyword)
    #         yield word

    def _locations(self, article):
        # for location in ?:
        #     place = Place.objects.get_or_create(...)
        #     yield place
        pass

    def _domain(self, article):
        d = tldextract.extract(article.url)
        return d.subdomain, d.domain, d.suffix