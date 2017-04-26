# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Crawl


class ListView(generic.ListView):
    model = Crawl


class DetailView(generic.DetailView):
    model = Crawl
