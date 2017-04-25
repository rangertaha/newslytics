# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Article, Keyword, Language


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('published', 'title')
    list_display_links = ('published', 'title')
    prepopulated_fields = {'slug': ('title',), }
    list_select_related = ('language', 'icon')
    raw_id_fields = ('authors', 'places', 'keywords')
    search_fields = ('title', 'description', 'url', 'text', 'html')


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('word', 'freq')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

