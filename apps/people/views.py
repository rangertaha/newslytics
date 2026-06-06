
from django.views import generic

from .models import Person


class ListView(generic.ListView):
    model = Person


class DetailView(generic.DetailView):
    model = Person
