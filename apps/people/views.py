# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Person


class ListView(generic.ListView):
    model = Person


class DetailView(generic.DetailView):
    model = Person
