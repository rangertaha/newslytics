# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import newspaper
from django.db import models
from langdetect import detect
from django.utils.text import slugify

from ..articles.models import Article, Language


class Domain(models.Model):
    PROTO_CHOICES = (
        ('http', 'http'),
        ('http', 'https'),
    )
    proto = models.CharField(
        max_length=5, choices=PROTO_CHOICES, default='https',
        blank=True, null=True)
    sub = models.CharField(max_length=30, blank=True, null=True)
    domain = models.CharField(max_length=100)
    suffix = models.CharField(max_length=30, blank=True)
    url = models.URLField(max_length=500, blank=True, null=True)
    favicon = models.URLField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True, null=True)
    enabled = models.BooleanField(default=True)
    rank = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    # @models.permalink
    # def get_absolute_url(self):
    #     return 'domains:detail', (self.pk, )


class Crawl(models.Model):
    domain = models.ForeignKey(Domain, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    msg = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % (self.id, )
