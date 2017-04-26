# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..domains.models import Domain


class Crawl(models.Model):
    TYPE_CHOICES = (
        ('article', 'Article'),
        ('feed:urls', 'Feed URLs'),
        ('feed:entries', 'Feed Entries'),
    )
    otype = models.CharField(
        max_length=30, choices=TYPE_CHOICES, blank=True, null=True)
    domain = models.ForeignKey(Domain, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=True, null=True)
    count = models.IntegerField(default=0)
    error = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.domain, )
