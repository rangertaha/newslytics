from django.db import models
from filer.fields.image import FilerImageField


class Thing(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = FilerImageField(
        related_name="things", on_delete=models.SET_NULL, blank=True, null=True)
    body = models.JSONField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    sentiment = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
