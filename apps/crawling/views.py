
from django.views import generic

from .models import Crawl


class ListView(generic.ListView):
    model = Crawl


class DetailView(generic.DetailView):
    model = Crawl
