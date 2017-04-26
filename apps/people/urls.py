from django.conf.urls import url

from . import views

app_name = 'people'

urlpatterns = [
    url(r'^$',
        views.ListView.as_view(), name='list'),

    url(r'/(?P<slug>[\w]+)/$',
        views.DetailView.as_view(), name='detail'),

]