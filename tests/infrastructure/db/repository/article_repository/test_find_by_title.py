from articles.infrastructure.db.entity import ArticleEntity
from articles.infrastructure.db.repository import ArticleRepository
from sqlalchemy.orm import Session


def test_find_by_name(db_session: Session, article_repository: ArticleRepository) -> None:
    article_title = 'title'
    category = ArticleEntity(id=1, title=article_title)
    db_session.add(category)
    db_session.commit()

    result = article_repository.find_by_title(article_title)
    assert article_title == result.title
