# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Channel


class ListView(generic.ListView):
    model = Channel


class DetailView(generic.DetailView):
    model = Channel
