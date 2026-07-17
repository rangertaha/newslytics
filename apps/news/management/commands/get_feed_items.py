from datetime import datetime
from time import mktime

import feedparser
import newspaper
import tldextract
from django.core.management.base import BaseCommand

from apps.domains.models import Domain
from apps.news.crawl import save_article
from apps.news.models import Feed


class Command(BaseCommand):
    help = 'Get feed items'

    def handle(self, *args, **options):
        feeds = Feed.objects.all()
        for feed in feeds:
            d = feedparser.parse(feed.url)
            for entry in d.entries:
                # Entries without a pubDate have no published_parsed at all.
                self.crawl(url=entry.link,
                           published=entry.get('published_parsed'))

    def crawl(self, url=None, published=None):
        try:
            article = newspaper.Article(url=url)
            article.build()
        except Exception as e:
            self.stderr.write(f'{url}: {e}')
            return
        domain = self._domain(article)
        atcl = save_article(domain, article,
                            published=self._published(published))
        self.stdout.write(atcl.url)

    def _published(self, published):
        if published:
            return datetime.fromtimestamp(mktime(published))
        return None

    def _domain(self, article):
        d = tldextract.extract(article.url)
        domain, _ = Domain.objects.get_or_create(
            sub=d.subdomain, domain=d.domain, suffix=d.suffix)
        return domain
