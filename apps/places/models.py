# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


class Place(models.Model):
    name = models.CharField(max_length=30, blank=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'places:detail', (self.slug,)

    def save(self):
        instance = super(Place, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        return instance
