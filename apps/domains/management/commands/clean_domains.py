import os.path
import time
import urllib.request

import tldextract
from django.core.management.base import BaseCommand

from apps.domains.models import Domain


class Command(BaseCommand):
    help = 'Clean domains from file and output to stdout'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str,
                            default='data/sites.txt')

    def handle(self, *args, **options):
        for lpath in options.get('file'):
            if os.path.isfile(lpath):
                with open(lpath) as f:
                    lines = f.readlines()
                    for line in lines:
                        url = 'http://' + line

                        try:
                            opener = urllib.request.build_opener(
                                urllib.request.HTTPRedirectHandler)
                            response = opener.open(url)

                            proto = 'http'
                            if response.url.startswith('https'):
                                proto = 'https'

                            d = tldextract.extract(response.url)
                            dobj, created = Domain.objects.get_or_create(
                                proto=proto,
                                sub=d.subdomain,
                                domain=d.domain,
                                suffix=d.suffix,
                                url=response.url,
                                valid=True)

                            self.stdout.write(
                                self.style.SUCCESS(f'{dobj.url}'))
                            time.sleep(0.5)
                        except Exception as e:
                            self.stderr.write(str(e))
