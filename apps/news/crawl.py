"""Shared article-ingestion helpers used by the crawl management commands."""
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

from apps.news.models import Article, Language
from apps.people.models import Person


def detect_language(article):
    if article.meta_lang:
        return article.meta_lang
    try:
        return detect(f'{article.title} {article.summary}')
    except LangDetectException:
        return 'und'


def save_article(domain, article, published=None, sentiment=None):
    """Create or refresh the Article row for a parsed newspaper article.

    Articles are keyed by URL; everything else (including the title, which a
    publisher may correct between crawls) is refreshed on re-crawl. The slug
    is generated once in Article.save() and kept stable after that.
    """
    language, _ = Language.objects.get_or_create(code=detect_language(article))
    atcl, _ = Article.objects.get_or_create(
        url=article.url,
        defaults={'domain': domain, 'title': article.title})
    atcl.domain = domain
    atcl.title = article.title
    atcl.description = article.summary
    atcl.text = article.text
    atcl.html = article.html
    atcl.published = published or article.publish_date
    atcl.language = language
    if sentiment is not None:
        atcl.sentiment = sentiment
    atcl.save()

    for author in article.authors:
        person, _ = Person.objects.get_or_create(first=author)
        atcl.authors.add(person)
    return atcl
