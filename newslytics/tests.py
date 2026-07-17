"""Smoke tests: every wired-up list page renders."""
from django.test import TestCase
from django.urls import reverse


class ListPageSmokeTests(TestCase):
    list_routes = [
        'crawling:list',
        'domains:list',
        'news:list',
        'objects:list',
        'people:list',
        'places:list',
        'streams:list',
    ]

    def test_root_redirects_to_news(self):
        response = self.client.get('/')
        self.assertRedirects(response, reverse('news:list'))

    def test_list_pages_render(self):
        for route in self.list_routes:
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 200)
