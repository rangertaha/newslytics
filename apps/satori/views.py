# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Article


class ListView(generic.ListView):
    model = Article


class DetailView(generic.DetailView):
    model = Article
