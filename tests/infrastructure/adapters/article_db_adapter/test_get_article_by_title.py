from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity
from sqlalchemy.orm import Session


class TestGetArticleByTitle:

    def test_when_not_found(self, article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
        result = article_db_adapter.get_article_by_title('abcdef')
        assert not result
        assert not db_session.query(ArticleEntity).filter_by(title='abcdef').first()

    def test_when_found(self, article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
        db_session.add(ArticleEntity(
            id=1,
            title='title',
            category=CategoryEntity(id=1, name='name', description='dummy')
            )
        )
        db_session.commit()
        result = article_db_adapter.get_article_by_title('title')
        assert 'title' == result.title
