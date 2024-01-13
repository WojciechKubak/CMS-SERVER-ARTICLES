from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.db.entity import ArticleEntity
from sqlalchemy.orm import Session


def test_delete_article(article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
    db_session.add(ArticleEntity(id=1, title='title'))
    db_session.commit()
    article_db_adapter.delete_article(1)
    assert not db_session.query(ArticleEntity).filter_by(id=1).first()
