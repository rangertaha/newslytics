from django.core.management.base import BaseCommand

from apps.domains.models import Domain


class Command(BaseCommand):
    help = 'Output RSS feed urls'

    def handle(self, *args, **options):
        for feed in Domain.objects.all():
            if feed.sub:
                self.stdout.write(
                    self.style.SUCCESS(f'{feed.proto}://{feed.sub}.{feed.domain}.{feed.suffix}'))
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'{feed.proto}://{feed.domain}.{feed.suffix}'))
