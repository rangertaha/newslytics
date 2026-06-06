from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Place(models.Model):
    name = models.CharField(max_length=30, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
