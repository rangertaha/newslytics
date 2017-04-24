# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Person, Social


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'middle', 'last')


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')