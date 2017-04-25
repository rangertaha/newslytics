# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Domain, Crawl, Feed


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')
    list_display_links = ('url', 'title')


@admin.register(Crawl)
class CrawlAdmin(admin.ModelAdmin):
    list_display = ('created', 'success')
    list_display_links = ('created', 'success')


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('url', )
    list_select_related = ('domain', )
    #raw_id_fields = ('domain', )

