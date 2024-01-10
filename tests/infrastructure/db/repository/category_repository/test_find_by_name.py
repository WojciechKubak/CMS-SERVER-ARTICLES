from articles.infrastructure.db.entity import CategoryEntity
from articles.infrastructure.db.repository import CategoryRepository
from sqlalchemy.orm import Session


def test_find_by_name(db_session: Session, category_repository: CategoryRepository) -> None:
    category_name = 'name'
    category = CategoryEntity(id=1, name=category_name)
    db_session.add(category)
    db_session.commit()

    result = category_repository.find_by_name(category_name)
    assert category_name == result.name
