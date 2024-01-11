from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity
from sqlalchemy.orm import Session


class TestGetArticleById:

    def test_when_not_found(self, article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
        result = article_db_adapter.get_article_by_id(1111)
        assert not result
        assert not db_session.query(ArticleEntity).filter_by(id=1111).first()

    def test_when_found(self, article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='title',content='dummy'))
        db_session.commit()
        result = article_db_adapter.get_article_by_id(1)
        assert 1 == result.id_
