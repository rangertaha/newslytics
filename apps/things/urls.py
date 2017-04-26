from django.conf.urls import url

from . import views

app_name = 'things'

urlpatterns = [
    url(r'^things',
        views.ListView.as_view(), name='list'),

    url(r'^things/(?P<slug>[\w]+)/$',
        views.DetailView.as_view(), name='detail'),

]