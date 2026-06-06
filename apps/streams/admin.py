
from django.contrib import admin

from .models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'appkey')
    list_display_links = ('name', 'appkey')

