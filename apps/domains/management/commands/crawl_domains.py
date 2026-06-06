import newspaper
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from langdetect import detect

from apps.crawling.models import Crawl
from apps.domains.models import Domain
from apps.news.models import Article, Language
from apps.people.models import Person


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
                    self.save(domain, article)
                    crawling.count = crawling.count + 1
        except Exception as e:
            crawling.error = str(e)
            self.stderr.write(str(e))
        crawling.save()

    def save(self, domain, article):
        language, created = Language.objects.get_or_create(
            code=self._language(article)
        )
        atcl, created = Article.objects.get_or_create(
            url=article.url,
            domain=domain,
            title=article.title)

        atcl.description = article.summary
        atcl.text = article.text
        atcl.html = article.html
        atcl.published = self._published(article)
        atcl.language = language

        for person in self._authors(article):
            atcl.authors.add(person)

        self.stdout.write(atcl.title)
        atcl.save()

    def _published(self, article):
        if article:
            return article.publish_date
        return None

    def _language(self, article):
        if not article.meta_lang:
            text = article.title + ' ' + article.summary
            return detect(text)
        return article.meta_lang

    def _authors(self, article):
        for author in article.authors:
            person, created = Person.objects.get_or_create(first=author)
            yield person
