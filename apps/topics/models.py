# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import threading
from django.db import models

from satori.rtm.client import make_client, SubscriptionMode

#
# class Channel(models.Model):
#     endpoint = models.CharField(max_length=30, default='wss://open-data.api.satori.com')
#     name = models.CharField(max_length=30, blank=True, null=True)
#     appkey = models.CharField(max_length=130, blank=True, null=True)
#
#     def __unicode__(self):
#         return self. name
#
#     def sub(self):
#         with make_client(
#                 endpoint=self.endpoint, appkey=self.appkey) as client:
#
#             print('Connected!')
#
#             mailbox = []
#             got_message_event = threading.Event()
#
#             class SubscriptionObserver(object):
#                 def on_subscription_data(self, data):
#                     for message in data['messages']:
#                         mailbox.append(message)
#                     got_message_event.set()
#
#             subscription_observer = SubscriptionObserver()
#             client.subscribe(
#                 self.name,
#                 SubscriptionMode.SIMPLE,
#                 subscription_observer)
#
#             if not got_message_event.wait(10):
#                 print("Timeout while waiting for a message")
#                 sys.exit(1)
#
#             for message in mailbox:
#                 print('Got message "{0}"'.format(message))
#                 yield message
#
#
# class Event(models.Model):
#     SIGNAL_CHOICES = (
#         ('save', 'Save'),
#         ('update', 'Update'),
#     )
#     signal = models.CharField(
#         max_length=5, choices=SIGNAL_CHOICES, default='save')
#     name = models.CharField(max_length=30, blank=True, null=True)
#     #topic = models.ForeignKey('topics.Topic', blank=True, null=True)
#     channel = models.ForeignKey(Channel, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name
