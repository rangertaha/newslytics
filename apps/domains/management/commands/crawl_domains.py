import os.path
import time
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

from apps.domains.models import Domain
from apps.news.models import Article, Language
from apps.crawling.models import Crawl
from apps.people.models import Person


class Command(BaseCommand):
    help = 'Crawl domains for articles'

    # def add_arguments(self, parser):
    #     parser.add_argument('rank', nargs='+', type=int)

    def handle(self, *args, **options):
        domains = Domain.objects.filter(enabled=True)
        for domain in domains:
            self.crawl(domain=domain)

    def crawl(self, domain=None, memoize=False):
        crawling = Crawl.objects.create(domain=domain, dtype='articles')
        crawling.count = 0
        try:
            paper = newspaper.build(domain.url, memoize_articles=memoize)
            for article in paper.articles:
                article.download()
                soup = BeautifulSoup(article.html)
                article.html = soup.prettify()

                article.parse()
                article.nlp()
                if article.summary and article.title:
                    self.save(domain, article)
                    crawling.count = crawling.count + 1

            crawling.success = True
        except Exception as e:
            crawling.error = e
            print e
        crawling.save()

    def save(self, domain, article):
        language, created = Language.objects.get_or_create(
            code=self._language(article)
        )
        atcl, created = Article.objects.get_or_create(
            url=article.url,
            domain=domain,
            title=article.title)

        atcl.description = article.summary
        atcl.text = article.text
        atcl.html = article.html
        atcl.published = self._published(article)
        atcl.language = language

        for person in self._authors(article):
            atcl.authors.add(person)

        # for keyword in self._keywords(article):
        #     atcl.keywords.add(keyword)

        # for location in self._locations(article):
        #     article.places.add(location)

        print atcl.title
        atcl.save()

    def _published(self, article):
        if article:
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
