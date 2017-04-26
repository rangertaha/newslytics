# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Domain, Crawl, Feed


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('rank', 'url', 'title', 'enabled')
    list_display_links = ('url', 'title')


@admin.register(Crawl)
class CrawlAdmin(admin.ModelAdmin):
    list_display = ('created', 'success', 'failed', 'msg')
    list_display_links = ('created', 'success', 'failed', 'msg')


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('domain', 'url', )
    list_select_related = ('domain', )
    #raw_id_fields = ('domain', )

