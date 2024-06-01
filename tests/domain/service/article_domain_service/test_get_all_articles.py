from articles.domain.service import ArticleService
from tests.factory import ArticleEntityFactory


class TestGetAllArticles:

    def test_when_no_articles(
            self,
            article_domain_service: ArticleService,
    ) -> None:
        result = article_domain_service.get_all_articles()
        assert not result

    def test_when_articles(
            self,
            article_domain_service: ArticleService
    ) -> None:
        articles = ArticleEntityFactory.create_batch(5)
        result = article_domain_service.get_all_articles()
        assert len(articles) == len(result)
