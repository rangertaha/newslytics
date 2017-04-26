# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Person, SocialAccount


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('image', 'first', 'middle', 'last')


@admin.register(SocialAccount)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('type', 'url')