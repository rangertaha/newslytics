from django.db import models


class Channel(models.Model):
    endpoint = models.CharField(
        max_length=60, default='wss://open-data.api.satori.com')
    name = models.CharField(max_length=30, blank=True, null=True)
    appkey = models.CharField(max_length=130, blank=True, null=True)

    def __str__(self):
        return self.name or ''

    def sub(self):
        # The Satori real-time data service this used to subscribe to has been
        # shut down. Left as a stub; wire up a replacement pub/sub here.
        pass
