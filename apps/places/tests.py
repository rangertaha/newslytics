from django.test import TestCase

from .models import Place


class PlaceModelTests(TestCase):
    def test_slug_generated_from_name(self):
        place = Place.objects.create(name='New York')
        self.assertEqual(place.slug, 'new-york')

    def test_duplicate_names_get_unique_slugs(self):
        Place.objects.create(name='Springfield')
        second = Place.objects.create(name='Springfield')
        self.assertEqual(second.slug, 'springfield-2')
