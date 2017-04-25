# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'appkey')
    list_display_links = ('name', 'appkey')
