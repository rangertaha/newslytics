# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Article, Language


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('published', 'title')
    list_display_links = ('published', 'title')
    prepopulated_fields = {'slug': ('title',), }
    list_select_related = ('language', 'thumb')
    raw_id_fields = ('authors', 'things', 'people')
    search_fields = ('title', 'description', 'url', 'text', 'html')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

