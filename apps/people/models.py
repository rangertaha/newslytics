from django.contrib.postgres.fields import ArrayField
from django.db import models
from filer.fields.image import FilerImageField


class Person(models.Model):
    first = models.CharField(max_length=100, blank=True)
    middle = models.CharField(max_length=100, blank=True)
    last = models.CharField(max_length=100, blank=True)
    suffix = models.CharField(max_length=100, blank=True)
    aliases = ArrayField(
        models.CharField(max_length=50), blank=True, null=True)
    image = FilerImageField(
        related_name="people", on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sentiment = models.JSONField(blank=True, null=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.name()

    def name(self):
        return ' '.join(p for p in (self.first, self.middle, self.last) if p)


class SocialAccount(models.Model):
    ACCOUNT_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
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
        ('yikyak', 'Yik Yak'),
        ('shots', 'Shots'),
        ('periscope', 'Periscope'),
    )
    person = models.ForeignKey(
        Person, related_name='accounts', on_delete=models.CASCADE,
        blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True)
    type = models.CharField(
        max_length=20, choices=ACCOUNT_CHOICES, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True)

    class Meta:
        verbose_name_plural = "Accounts"
