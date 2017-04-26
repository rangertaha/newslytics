# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Crawl


@admin.register(Crawl)
class CrawlAdmin(admin.ModelAdmin):
    list_display = ('otype', 'domain', 'created', 'duration', 'count')
    list_display_links = ('otype', 'domain', 'created', 'duration', 'count')
