from articles.infrastructure.persistance.repository import ArticleRepository
from tests.factory import ArticleEntityFactory


def test_find_by_name(article_repository: ArticleRepository) -> None:
    article = ArticleEntityFactory()
    result = article_repository.find_by_title(article.title)
    assert article == result
