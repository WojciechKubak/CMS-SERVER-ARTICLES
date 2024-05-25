from articles.infrastructure.broker.dto import TranslatedArticleDTO


def test_to_domain() -> None:
    data = {
        'article_id': 1,
        'title': 'title',
        'content_path': 'path',
        'language_id': 1,
        'author_id': 1
    }
    dto = TranslatedArticleDTO(**data)

    result = dto.to_domain()

    assert dto.article_id == result.article_id
    assert dto.title == result.title
    assert dto.content_path == result.content_path
    assert dto.language_id == result.language_id
    assert dto.author_id == result.author_id
