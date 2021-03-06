# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Domain


class ListView(generic.ListView):
    model = Domain


class DetailView(generic.DetailView):
    model = Domain
