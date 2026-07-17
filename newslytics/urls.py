"""newslytics URL Configuration

https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='news:list', permanent=False)),
    path('admin/', admin.site.urls),
    path('crawling/', include('apps.crawling.urls')),
    path('domains/', include('apps.domains.urls')),
    path('news/', include('apps.news.urls')),
    path('objects/', include('apps.objects.urls')),
    path('people/', include('apps.people.urls')),
    path('places/', include('apps.places.urls')),
    path('streams/', include('apps.streams.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
