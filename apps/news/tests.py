from django.test import TestCase
from django.urls import reverse

from .crawl import save_article
from .models import Article, Feed, Language


class ArticleModelTests(TestCase):
    def test_slug_generated_from_title(self):
        article = Article.objects.create(
            url='https://example.com/a', title='Breaking News Today')
        self.assertEqual(article.slug, 'breaking-news-today')

    def test_slug_preserved_on_resave(self):
        article = Article.objects.create(
            url='https://example.com/a', title='Original Title',
            slug='custom-slug')
        article.title = 'Changed Title'
        article.save()
        article.refresh_from_db()
        self.assertEqual(article.slug, 'custom-slug')

    def test_duplicate_titles_get_unique_slugs(self):
        first = Article.objects.create(
            url='https://example.com/a', title='Same Title')
        second = Article.objects.create(
            url='https://example.com/b', title='Same Title')
        self.assertEqual(first.slug, 'same-title')
        self.assertEqual(second.slug, 'same-title-2')

    def test_get_absolute_url(self):
        article = Article.objects.create(
            url='https://example.com/a', title='Some Story')
        self.assertEqual(article.get_absolute_url(), '/news/some-story/')


class FeedModelTests(TestCase):
    def test_str_with_null_url(self):
        self.assertEqual(str(Feed()), '')


class LanguageModelTests(TestCase):
    def test_regional_code_fits(self):
        language = Language.objects.create(code='zh-cn')
        language.refresh_from_db()
        self.assertEqual(language.code, 'zh-cn')


class FakeParsedArticle:
    """Duck-typed stand-in for a parsed newspaper.Article."""

    url = 'https://example.com/n1'
    title = 'Crawled Title'
    summary = 'A summary.'
    text = 'Body.'
    html = '<html></html>'
    meta_lang = 'en'
    publish_date = None
    authors = ['Jane Doe']


class SaveArticleTests(TestCase):
    def test_creates_article_with_author_and_language(self):
        atcl = save_article(None, FakeParsedArticle())
        self.assertEqual(atcl.title, 'Crawled Title')
        self.assertEqual(atcl.language.code, 'en')
        self.assertEqual(atcl.authors.get().first, 'Jane Doe')

    def test_recrawl_refreshes_title_but_keeps_slug(self):
        save_article(None, FakeParsedArticle())
        updated = FakeParsedArticle()
        updated.title = 'Corrected Title'
        atcl = save_article(None, updated)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(atcl.title, 'Corrected Title')
        self.assertEqual(atcl.slug, 'crawled-title')


class ArticleViewTests(TestCase):
    def test_list_view(self):
        Article.objects.create(url='https://example.com/a', title='Story One')
        response = self.client.get(reverse('news:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Story One')

    def test_detail_view(self):
        article = Article.objects.create(
            url='https://example.com/a', title='Story One', text='Body text.')
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Body text.')
