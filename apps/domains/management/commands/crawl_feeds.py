from django.core.management.base import BaseCommand, CommandError
import newspaper

from apps.domains.models import Domain, Feed


class Command(BaseCommand):
    help = 'Get RSS feeds from news sites'

    def handle(self, *args, **options):
        for domain in Domain.objects.filter(enabled=True):
            try:
                paper = newspaper.build(domain.url, memoize_articles=False)
                for feed_url in paper.feed_urls():
                    feed, created = Feed.objects.get_or_create(
                        url=feed_url, domain=domain)
            except Exception as e:
                pass
