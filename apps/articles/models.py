# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from filer.fields.image import FilerImageField
from django.contrib.postgres.fields import JSONField


class Language(models.Model):
    code = models.CharField(max_length=4, blank=False)
    name = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    slug = models.SlugField(max_length=250)
    url = models.URLField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    thumb = FilerImageField(related_name="article", blank=True, null=True)

    domain = models.ForeignKey('domains.Domain', blank=True, null=True)
    authors = models.ManyToManyField('people.Person', blank=True,
                                     related_name='authors')
    language = models.ForeignKey(Language, blank=True, null=True)
    people = models.ManyToManyField('people.Person', blank=True)
    sentiment = JSONField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    # @models.permalink
    # def get_absolute_url(self):
    #     return 'articles:detail', (self.slug, )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
