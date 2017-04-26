import os.path
import urllib2

from django.core.management.base import BaseCommand, CommandError


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

                            self.stdout.write(
                                self.style.SUCCESS('%s' % request.url))
                        except:
                            pass
