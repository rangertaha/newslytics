import time
import os.path
import urllib2

import tldextract
from django.core.management.base import BaseCommand, CommandError
from apps.domains.models import Domain


class Command(BaseCommand):
    help = 'Clean domains from file and output to stdout'

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

                            proto = 'http'
                            if 'https' == request.url[:5]:
                                proto = 'https'

                            d = tldextract.extract(request.url)
                            dobj, created = Domain.objects.get_or_create(
                                proto=proto,
                                sub=d.subdomain,
                                domain=d.domain,
                                suffix=d.suffix,
                                url=request.url,
                                valid=True)

                            self.stdout.write(
                                self.style.SUCCESS('%s' % dobj.url))
                            time.sleep(0.5)
                        except Exception as e:
                            print e
