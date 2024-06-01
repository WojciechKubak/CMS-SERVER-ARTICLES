from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.persistance.entity import ArticleEntity
from tests.factory import ArticleEntityFactory, ArticleFactory


def test_update_article(article_db_adapter: ArticleDbAdapter) -> None:
    article_dao = ArticleEntityFactory()
    new_title = f'new_{article_dao.title}'
    article = ArticleFactory(title=new_title, id_=article_dao.id)

    article_db_adapter.save_article(article)
    result = article_db_adapter.get_article_by_id(article.id_)

    assert ArticleEntity.query.filter_by(id=result.id_).first().title \
        == new_title
