"""newslytics URL Configuration

https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('domains/', include('apps.domains.urls')),
    path('news/', include('apps.news.urls')),
    path('objects/', include('apps.objects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
