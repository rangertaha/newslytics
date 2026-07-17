from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Place(models.Model):
    name = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._unique_slug()
        super().save(*args, **kwargs)

    def _unique_slug(self):
        base = slugify(self.name)[:40] or 'place'
        taken = set(
            Place.objects.exclude(pk=self.pk)
            .filter(slug__startswith=base)
            .values_list('slug', flat=True))
        slug = base
        suffix = 2
        while slug in taken:
            slug = f'{base}-{suffix}'
            suffix += 1
        return slug
