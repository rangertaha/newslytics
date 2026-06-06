from django.urls import path

from . import views

app_name = 'streams'

urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
]
