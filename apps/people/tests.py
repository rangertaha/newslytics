from django.test import TestCase

from .models import Person


class PersonModelTests(TestCase):
    def test_name_skips_missing_parts(self):
        person = Person(first='Ada', last='Lovelace')
        self.assertEqual(person.name(), 'Ada Lovelace')
        self.assertEqual(str(person), 'Ada Lovelace')

    def test_name_with_middle(self):
        person = Person(first='Ada', middle='King', last='Lovelace')
        self.assertEqual(person.name(), 'Ada King Lovelace')
