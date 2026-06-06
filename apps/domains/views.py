
from django.views import generic

from .models import Domain


class ListView(generic.ListView):
    model = Domain


class DetailView(generic.DetailView):
    model = Domain
