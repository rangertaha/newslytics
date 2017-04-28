# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import threading
from django.db import models

from satori.rtm.client import make_client, SubscriptionMode


class Channel(models.Model):
    endpoint = models.CharField(max_length=30, default='wss://open-data.api.satori.com')
    name = models.CharField(max_length=30, blank=True, null=True)
    appkey = models.CharField(max_length=130, blank=True, null=True)

    def __unicode__(self):
        return self. name

    def sub(self):
       pass
