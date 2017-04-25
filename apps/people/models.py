# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from filer.fields.image import FilerImageField
from fontawesome.fields import IconField
from django.db import models


class Person(models.Model):
    first = models.CharField(max_length=100, blank=True)
    middle = models.CharField(max_length=100, blank=True)
    last = models.CharField(max_length=100, blank=True)
    image = FilerImageField(related_name="people", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s' % (self.first, self.middle, self.last)


class SocialAccount(models.Model):
    icon = IconField()
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True)

    person = models.ForeignKey(
        Person, related_name='accounts', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Social Accounts"