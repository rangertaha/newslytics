import os.path

import tldextract
from django.core.management.base import BaseCommand

from apps.domains.models import Domain


class Command(BaseCommand):
    help = 'Load domains from file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str,
                            default='data/domains.txt')

    def handle(self, *args, **options):
        for lpath in options.get('file'):
            if os.path.isfile(lpath):
                with open(lpath) as f:
                    for url in f:
                        url = url.strip()
                        if not url:
                            continue
                        proto = 'http'
                        if url.startswith('https'):
                            proto = 'https'

                        try:
                            d = tldextract.extract(url)
                            dobj, created = Domain.objects.get_or_create(
                                proto=proto,
                                sub=d.subdomain,
                                domain=d.domain,
                                suffix=d.suffix,
                                url=url)
                        except Exception as e:
                            self.stdout.write(
                                self.style.ERROR(f'Error: {e}'))
