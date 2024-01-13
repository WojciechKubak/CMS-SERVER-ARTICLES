from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.db.entity import ArticleEntity
from articles.domain.model import Article, Category
from sqlalchemy.orm import Session


def test_update_article(article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
    db_session.add(ArticleEntity(id=1, title='title'))
    db_session.commit()

    article = Article(
        id_=1,
        title='title',
        content='dummy',
        category=Category(id_=1, name='name', description='dummy'),
        tags=[]
    )
    result = article_db_adapter.update_article(article)

    assert article == result
    assert db_session.query(ArticleEntity).filter_by(id=1).first().category
