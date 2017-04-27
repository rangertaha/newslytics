from django.core.management.base import BaseCommand, CommandError
from apps.domains.models import Domain


class Command(BaseCommand):
    help = 'Create crawling groups based on frequincy of new articles'

    # def add_arguments(self, parser):
    #     parser.add_argument('file', nargs='+', type=str,
    #                         default='data/sites.txt')

    def handle(self, *args, **options):
        pass
