from django.conf.urls import url

from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$',
        views.ListView.as_view(), name='list'),

    url(r'^(?P<slug>[\w]+)/$',
        views.DetailView.as_view(), name='detail'),

]