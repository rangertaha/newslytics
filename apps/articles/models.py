# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from filer.fields.image import FilerImageField


class Keyword(models.Model):
    word = models.CharField(max_length=30, blank=False)
    freq = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.word


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
    icon = FilerImageField(related_name="article", blank=True, null=True)

    domain = models.ForeignKey('domains.Domain', related_name='articles', blank=True, null=True)
    authors = models.ManyToManyField('people.Person', related_name='articles', blank=True)
    places = models.ManyToManyField('places.Place', related_name='articles', blank=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    language = models.ForeignKey(Language, blank=True, null=True)

    def __unicode__(self):
        return self.title

    # @models.permalink
    # def get_absolute_url(self):
    #     return 'articles:detail', (self.slug, )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
