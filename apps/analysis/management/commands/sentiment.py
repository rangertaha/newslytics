from django.core.management.base import BaseCommand
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from apps.news.models import Article


class Command(BaseCommand):
    help = 'Create sentiment scores for objects'
    analyzer = SentimentIntensityAnalyzer()

    def handle(self, *args, **options):
        self._articles()

    def _articles(self):
        for article in Article.objects.all():
            vs = self.analyzer.polarity_scores(article.text)
            article.sentiment = vs
            article.save()
            self.stdout.write(str(vs))
