from datetime import datetime
from time import mktime

import feedparser
import newspaper
import tldextract
from django.core.management.base import BaseCommand
from langdetect import detect

from apps.domains.models import Domain
from apps.news.models import Article, Feed, Language
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
        except Exception:
            pass

    def save(self, dtime, article):
        language, created = Language.objects.get_or_create(
            code=self._language(article)
        )
        sub, dm, suffix = self._domain(article)
        domain, created = Domain.objects.get_or_create(
            sub=sub, domain=dm, suffix=suffix)
        self.stdout.write(article.url)
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

        atcl.save()

    def _published(self, article, dtime):
        if dtime:
            return datetime.fromtimestamp(mktime(dtime))
        if article.publish_date:
            return article.publish_date
        return None

    def _language(self, article):
        if not article.meta_lang:
            text = article.title + ' ' + article.summary
            return detect(text)
        return article.meta_lang

    def _authors(self, article):
        for author in article.authors:
            person, created = Person.objects.get_or_create(first=author)
            yield person

    def _domain(self, article):
        d = tldextract.extract(article.url)
        return d.subdomain, d.domain, d.suffix
