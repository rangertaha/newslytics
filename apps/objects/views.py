
from django.views import generic

from .models import Thing


class ListView(generic.ListView):
    model = Thing


class DetailView(generic.DetailView):
    model = Thing
