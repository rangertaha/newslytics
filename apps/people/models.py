# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models


class Person(models.Model):
    first = models.CharField(max_length=100, blank=True)
    middle = models.CharField(max_length=100, blank=True)
    last = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return '%s %s %s' % (self.first, self.middle, self.last)

    # @models.permalink
    # def get_absolute_url(self):
    #     return 'people:detail', (self.pk, )
