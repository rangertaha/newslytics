# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from filer.fields.image import FilerImageField
from django.contrib.postgres.fields import JSONField


class Thing(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = FilerImageField(related_name="things", blank=True, null=True)
    body = JSONField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    sentiment = JSONField(blank=True, null=True)

    def __unicode__(self):
        return self.title
