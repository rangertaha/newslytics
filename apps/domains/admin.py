# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Domain, Crawl


@admin.register(Domain)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')


@admin.register(Crawl)
class CrawlAdmin(admin.ModelAdmin):
    list_display = ('created', 'success')

