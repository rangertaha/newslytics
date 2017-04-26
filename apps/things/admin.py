# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Thing


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ('created', 'title')
    list_display_links = ('created', 'title')
    search_fields = ('title', 'description', 'body', 'sentiment')
