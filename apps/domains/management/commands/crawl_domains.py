import newspaper
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from apps.crawling.models import Crawl
from apps.domains.models import Domain
from apps.news.crawl import save_article


class Command(BaseCommand):
    help = 'Crawl domains for articles'

    def handle(self, *args, **options):
        domains = Domain.objects.filter(valid=True)
        for domain in domains:
            self.crawl(domain=domain)

    def crawl(self, domain=None, memoize=False):
        crawling = Crawl.objects.create(domain=domain, otype='article')
        crawling.count = 0
        try:
            paper = newspaper.build(domain.url, memoize_articles=memoize)
            for article in paper.articles:
                article.download()
                soup = BeautifulSoup(article.html, 'html.parser')
                article.html = soup.prettify()

                article.parse()
                article.nlp()
                if article.summary and article.title:
                    atcl = save_article(domain, article)
                    self.stdout.write(atcl.title)
                    crawling.count = crawling.count + 1
        except Exception as e:
            crawling.error = str(e)
            self.stderr.write(str(e))
        crawling.save()
