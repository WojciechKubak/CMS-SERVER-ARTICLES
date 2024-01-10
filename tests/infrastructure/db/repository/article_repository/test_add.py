from articles.infrastructure.db.repository import ArticleRepository
from articles.infrastructure.db.entity import CategoryEntity, ArticleEntity, TagEntity
from sqlalchemy.orm import Session


def test_add(article_repository: ArticleRepository, db_session: Session) -> None:
    category = CategoryEntity(name='category')
    tags = [TagEntity(name=''), TagEntity(name='')]
    db_session.bulk_save_objects([category, *tags])
    db_session.commit()

    article = ArticleEntity(title='title', category=category, tags=tags)
    article_repository.add(article)
    assert db_session.query(ArticleEntity).filter_by(title=article.title).first()
