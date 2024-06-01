from tests.factory import ArticleFactory, CategoryFactory, TagFactory


def test_change_category_and_tags() -> None:
    article = ArticleFactory()
    category = CategoryFactory()
    tags = TagFactory.create_batch(5)

    result = article.change_category_and_tags(category, tags)

    assert tags == result.tags
    assert category == result.category
