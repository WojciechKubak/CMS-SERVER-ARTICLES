from articles.infrastructure.broker.dto import TranslatedArticleDTO


def test_from_json() -> None:
    data = {
        "id": 1,
        "title": "title",
        "content_path": "path",
        "language_id": 1,
        "translator_id": 1,
    }

    result = TranslatedArticleDTO.from_json(data)

    assert data["id"] == result.article_id
    assert data["title"] == result.title
    assert data["content_path"] == result.content_path
    assert data["language_id"] == result.language_id
    assert data["translator_id"] == result.author_id
