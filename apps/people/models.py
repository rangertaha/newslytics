# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from filer.fields.image import FilerImageField
from fontawesome.fields import IconField
from django.db import models


class Person(models.Model):
    first = models.CharField(max_length=100, blank=True)
    middle = models.CharField(max_length=100, blank=True)
    last = models.CharField(max_length=100, blank=True)
    image = FilerImageField(related_name="people", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sentiment = JSONField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s' % (self.first, self.middle, self.last)


class SocialAccount(models.Model):
    ACCOUNT_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedlin', 'LinkedIn'),
        ('google+', 'Google+'),
        ('youtube', 'YouTube'),
        ('instagram', 'Instagram'),
        ('pinterest', 'Pinterest'),
        ('tumblr', 'Tumblr'),
        ('snapchat', 'Snapchat'),
        ('reddit', 'Reddit'),
        ('flickr', 'Flickr'),
        ('foursquare', 'Foursquare'),
        ('kik', 'Kik'),
        ('yikyak', 'Yik Yah'),
        ('shots', 'Shots'),
        ('periscope', 'Periscope'),
    )
    person = models.ForeignKey(
        Person, related_name='accounts', blank=True, null=True)
    icon = IconField()
    type = models.CharField(
        max_length=5, choices=ACCOUNT_CHOICES, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True)

    class Meta:
        verbose_name_plural = "Accounts"
