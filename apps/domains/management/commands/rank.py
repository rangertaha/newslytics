from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Rank domains'

    def handle(self, *args, **options):
        pass
