from articles.domain.model import Article, Category, Tag


def test_to_json() -> None:
    article = Article(
        id_=1,
        title='title',
        content='dummy',
        category=Category(id_=1, name='name', description='dummy'),
        tags=[Tag(id_=1, name='name'), Tag(id_=2, name='name')]
    )
    result = article.to_json()
    assert article.id_ == result['id']
    assert isinstance(result['category'], dict)
    assert isinstance(result['tags'], list)
