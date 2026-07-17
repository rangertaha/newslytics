from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from filer.fields.image import FilerImageField


class Language(models.Model):
    # Long enough for regional codes such as "zh-cn" that langdetect returns.
    code = models.CharField(max_length=8, blank=False)
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    url = models.URLField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    thumb = FilerImageField(
        related_name="article", on_delete=models.SET_NULL, blank=True, null=True)

    domain = models.ForeignKey(
        'domains.Domain', on_delete=models.CASCADE, blank=True, null=True)
    authors = models.ManyToManyField('people.Person', blank=True,
                                     related_name='authors')
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, blank=True, null=True)
    people = models.ManyToManyField('people.Person', blank=True)
    things = models.ManyToManyField('objects.Thing', blank=True)
    sentiment = models.JSONField(blank=True, null=True)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._unique_slug()
        super().save(*args, **kwargs)

    def _unique_slug(self):
        base = slugify(self.title)[:240] or 'article'
        taken = set(
            Article.objects.exclude(pk=self.pk)
            .filter(slug__startswith=base)
            .values_list('slug', flat=True))
        slug = base
        suffix = 2
        while slug in taken:
            slug = f'{base}-{suffix}'
            suffix += 1
        return slug


class Feed(models.Model):
    domain = models.ForeignKey(
        'domains.Domain', related_name='feeds', on_delete=models.CASCADE,
        blank=True, null=True)
    url = models.URLField(max_length=250, blank=False, null=True)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.url or ''
