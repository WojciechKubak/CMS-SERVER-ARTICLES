from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session


def test_get_all_categories(category_api_service: CategoryApiService, db_session: Session) -> None:
    categorys_dto = [CategoryEntity(name=''), CategoryEntity(name='')]
    db_session.bulk_save_objects(categorys_dto)
    db_session.commit()
    result = category_api_service.get_all_categories()
    assert len(categorys_dto) == len(result)
