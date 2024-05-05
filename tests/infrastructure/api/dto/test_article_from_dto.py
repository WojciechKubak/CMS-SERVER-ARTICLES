from articles.infrastructure.api.dto import ArticleDTO


def test_from_dto() -> None:
    article_dto = {
        'id_': 1,
        'title': 'title',
        'content': 'dummy',
        'category_id': 1,
        'tags_id':  [1, 2, 3]
    }
    result = ArticleDTO.from_dto(article_dto)
    assert article_dto['id_'] == result.id_
    assert article_dto['category_id'] == result.category_id
    assert article_dto['tags_id'] == result.tags_id
