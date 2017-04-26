from django.conf.urls import url

from . import views

app_name = 'analysis'

urlpatterns = [
    url(r'^analysis',
        views.ListView.as_view(), name='list'),

    url(r'^analysis/(?P<slug>[\w]+)/$',
        views.DetailView.as_view(), name='detail'),

]