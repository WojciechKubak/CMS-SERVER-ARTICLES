from tests.factory import ArticleFactory


def test_change_content() -> None:
    article = ArticleFactory()
    new_content = f"new_{article.content}"

    result = article.change_content(new_content)

    assert new_content == result.content
