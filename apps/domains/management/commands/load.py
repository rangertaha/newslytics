import os.path
from django.core.management.base import BaseCommand, CommandError
import urllib2
import tldextract
from apps.domains.models import Domain


class Command(BaseCommand):
    help = 'Load domains from file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str,
                            default='data/sites.txt')

    def handle(self, *args, **options):
        for lpath in options.get('file'):
            if os.path.isfile(lpath):
                with open(lpath, 'r') as f:
                    lines = f.readlines()
                    for l in lines:
                        url = 'http://' + l

                        try:
                            opener = urllib2.build_opener(
                                urllib2.HTTPRedirectHandler)
                            request = opener.open(url)

                            d = tldextract.extract(request.url)
                            dobj, created = Domain.objects.get_or_create(
                                sub=d.subdomain,
                                domain=d.domain,
                                suffix=d.suffix,
                                url=request.url)

                            self.stdout.write(
                                self.style.SUCCESS('Site: %s' % request.url))
                        except Exception as e:
                            self.stdout.write(
                                self.style.ERROR('Error: %s' % e))
