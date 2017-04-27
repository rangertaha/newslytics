# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Crawl, Group


@admin.register(Crawl)
class CrawlAdmin(admin.ModelAdmin):
    list_display = ('otype', 'domain', 'created', 'duration', 'count')
    list_display_links = ('otype', 'domain', 'created', 'duration', 'count')


@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    raw_id_fields = ('domains', )
