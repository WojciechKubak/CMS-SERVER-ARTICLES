from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.domain.model import Article, Category, Tag
from articles.infrastructure.db.entity import ArticleEntity
from sqlalchemy.orm import Session


def test_save_article(article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
    article = Article(
        id_=1,
        title='title',
        content='dummy',
        category=Category(id_=1, name='name', description='dummy'),
        tags=[Tag(id_=1, name='name')]
    )
    result = article_db_adapter.save_article(article)
    assert article == result
    assert db_session.query(ArticleEntity).filter_by(id=1).first()
