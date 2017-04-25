from django.conf.urls import url

from . import views

app_name = 'satori'

urlpatterns = [
    url(r'^domains$',
        views.ListView.as_view(), name='list'),

    url(r'^domains/(?P<slug>[\w]+)/$',
        views.DetailView.as_view(), name='detail'),

]