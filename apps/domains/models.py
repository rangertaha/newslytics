from django.db import models
from filer.fields.image import FilerImageField


class Domain(models.Model):
    PROTO_CHOICES = (
        ('http', 'http'),
        ('https', 'https'),
    )
    proto = models.CharField(
        max_length=5, choices=PROTO_CHOICES, default='https',
        blank=True, null=True)
    sub = models.CharField(max_length=30, blank=True, null=True)
    domain = models.CharField(max_length=100)
    suffix = models.CharField(max_length=30, blank=True)
    url = models.URLField(max_length=500, blank=True, null=True)
    favicon = models.URLField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True, null=True)
    image = FilerImageField(on_delete=models.SET_NULL, blank=True, null=True)
    rank = models.IntegerField(default=0)
    sentiment = models.JSONField(blank=True, null=True)
    valid = models.BooleanField(default=False)

    writers = models.ManyToManyField('people.Person', blank=True)

    def __str__(self):
        return f'{self.sub}.{self.domain}.{self.suffix}'
