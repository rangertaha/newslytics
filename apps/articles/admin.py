# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Article, Keyword, Language


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('published', 'title')
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('word', 'freq')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

