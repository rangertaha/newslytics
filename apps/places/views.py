
from django.views import generic

from .models import Place


class ListView(generic.ListView):
    model = Place


class DetailView(generic.DetailView):
    model = Place
