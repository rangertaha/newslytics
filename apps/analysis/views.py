# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Sentiment


class ListView(generic.ListView):
    model = Sentiment


class DetailView(generic.DetailView):
    model = Sentiment
