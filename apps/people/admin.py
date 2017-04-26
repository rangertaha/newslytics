# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Person, SocialAccount

class SocialAccountInline(admin.TabularInline):
    model = SocialAccount
    fk_name = "person"

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('image', 'first', 'middle', 'last')
    inlines = [
        SocialAccountInline,
    ]

