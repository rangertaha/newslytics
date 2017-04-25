# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Topic


class ListView(generic.ListView):
    model = Topic


class DetailView(generic.DetailView):
    model = Topic
