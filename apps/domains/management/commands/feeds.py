import os.path
from django.core.management.base import BaseCommand, CommandError
import urllib2
import tldextract

import newspaper
from apps.domains.models import Domain


class Command(BaseCommand):
    help = 'Get RSS feeds from news sites'

    def handle(self, *args, **options):
        for domain in Domain.objects.filter(enabled=True):
            paper = newspaper.build(domain.url, memoize_articles=True)
            for article in paper.articles:
                article.download()



        for lpath in options.get('get'):
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
