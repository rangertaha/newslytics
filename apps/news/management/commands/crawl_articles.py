import newspaper
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from apps.crawling.models import Crawl
from apps.domains.models import Domain
from apps.news.crawl import save_article


class Command(BaseCommand):
    help = 'Crawl domains for articles'
    analyzer = SentimentIntensityAnalyzer()

    def handle(self, *args, **options):
        domains = Domain.objects.filter(valid=False)
        for domain in domains:
            self.crawl(domain=domain)
            domain.valid = True
            domain.save()

    def crawl(self, domain=None, memoize=True):
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
                    atcl = save_article(
                        domain, article,
                        sentiment=self.analyzer.polarity_scores(article.text))
                    domain.writers.add(*atcl.authors.all())
                    self.stdout.write(atcl.title)
                    crawling.count = crawling.count + 1

        except Exception as e:
            crawling.error = str(e)
        crawling.save()
