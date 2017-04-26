from django.core.management.base import BaseCommand, CommandError

from apps.news.models import Feed


class Command(BaseCommand):
    help = 'Output RSS feed urls'

    def handle(self, *args, **options):
        for feed in Feed.objects.all():
            self.stdout.write(self.style.SUCCESS('%s' % feed.url))
