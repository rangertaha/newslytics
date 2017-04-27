from django.core.management.base import BaseCommand, CommandError
import newspaper

from apps.news.models import Feed
from apps.domains.models import Domain
from apps.crawling.models import Crawl


class Command(BaseCommand):
    help = 'Get RSS feeds from news sites'

    def handle(self, *args, **options):
        for domain in Domain.objects.filter(valid=True):
            crawling = Crawl.objects.create(domain=domain, otype='feed:urls')
            crawling.count = 0
            try:
                paper = newspaper.build(domain.url, memoize_articles=True)
                for feed_url in paper.feed_urls():
                    feed, created = Feed.objects.get_or_create(
                        url=feed_url, domain=domain)
                    if feed:
                        crawling.count = crawling.count + 1
                print domain.url

            except Exception as e:
                crawling.error = e
            crawling.save()
            domain.valid = False
            domain.save()
