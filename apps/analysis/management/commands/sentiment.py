from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer


import os.path
import time
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from time import mktime
from datetime import datetime


import hashlib
from datetime import datetime

import json
import tldextract
from bs4 import BeautifulSoup
import geograpy
from geograpy import extraction, places
import newspaper
from langdetect import detect
import feedparser

from apps.domains.models import Domain, Crawl, Feed
from apps.articles.models import Article, Language, Keyword
from apps.places.models import Place
from apps.people.models import Person
from apps.analysis.models import Sentiment


class Command(BaseCommand):
    help = 'Create sentiment scores for objects'
    analyzer = SentimentIntensityAnalyzer()

    def handle(self, *args, **options):
        self._articles()

    def _articles(self):
        for article in Article.objects.all():
            vs = self.analyzer.polarity_scores(article.text)
            print type(vs)
            # sentiment, created = Sentiment.objects.get_or_create(
            #     pos=vs.get('pos'),
            #     neu=vs.get('neu'),
            #     neg=vs.get('neg'),
            #     compound=vs.get('compound'),
            # )
            # article.sentiment = sentiment
            # article.save()
            #
            # print sentiment
            print vs

    def _people(self):
        # for person in Person.objects.all():
        #     vs = self.analyzer.polarity_scores(article.text)
        #     sentiment, created = Sentiment.objects.get_or_create(
        #         pos=vs.get('pos'),
        #         neu=vs.get('neu'),
        #         neg=vs.get('neg'),
        #         compound=vs.get('compound'),
        #     )
        #     article.sentiment = sentiment
        #     article.save()
        #
        #     print sentiment
        pass



















#
#
# # --- examples -------
# sentences = ["VADER is smart, handsome, and funny.",      # positive sentence example
#             "VADER is not smart, handsome, nor funny.",   # negation sentence example
#             "VADER is smart, handsome, and funny!",       # punctuation emphasis handled correctly (sentiment intensity adjusted)
#             "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
#             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
#             "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
#             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",# booster words & punctuation make this close to ceiling for score
#             "The book was good.",                                     # positive sentence
#             "The book was kind of good.",                 # qualified positive sentence is handled correctly (intensity adjusted)
#             "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
#             "At least it isn't a horrible book.",         # negated negative sentence with contraction
#             "Make sure you :) or :D today!",              # emoticons handled
#             "Today SUX!",                                 # negative slang with capitalization emphasis
#             "Today only kinda sux! But I'll get by, lol"  # mixed sentiment example with slang and constrastive conjunction "but"
#              ]
#
# analyzer = SentimentIntensityAnalyzer()
# for sentence in sentences:
#     vs = analyzer.polarity_scores(sentence)
#     print("{:-<65} {}".format(sentence, str(vs)))
