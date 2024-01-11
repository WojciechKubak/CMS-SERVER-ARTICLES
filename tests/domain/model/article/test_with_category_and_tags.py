from articles.domain.model import Article, Tag, Category


def test_with_category_and_tags() -> None:
    article = Article(id_=1, title='title', content='dummy', category=None, tags=[])
    tags = [Tag(id_=1, name='name'), Tag(id_=1, name='name')]
    category = Category(id_=1, name='name', description='dummy')
    result = article.with_category_and_tags(category, tags)
    assert tags == result.tags
    assert category == result.category
