from articles.domain.model import Article


def test_from_dto() -> None:
    article_dto = {
        'id': 1,
        'title': 'title',
        'content': 'dummy',
        'category_id': 1,
        'tags_id':  [1, 2, 3]
    }
    result = Article.from_dto(article_dto)
    assert article_dto['id'] == result.id_
    assert article_dto['category_id'] == result.category.id_
    assert article_dto['tags_id'] == [tag.id_ for tag in result.tags]
