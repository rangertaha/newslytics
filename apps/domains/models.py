# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from filer.fields.image import FilerImageField
from django.contrib.postgres.fields import JSONField


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
    image = FilerImageField(blank=True, null=True)
    rank = models.IntegerField(default=0)
    sentiment = JSONField(blank=True, null=True)
    valid = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0}.{1}.{2}'.format(self.sub, self.domain, self.suffix)
