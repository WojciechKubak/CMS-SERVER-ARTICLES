from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session
import pytest


class TestGetCategoryById:

    def test_when_not_found(self, category_api_service: CategoryApiService) -> None:
        with pytest.raises(ValueError) as err:
            category_api_service.get_category_by_id(9999)
        assert 'Category does not exist' == str(err.value)

    def test_when_found(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name'))
        db_session.commit()
        result = category_api_service.get_category_by_id(1)
        assert db_session.query(CategoryEntity).filter_by(id=result.id_).first()
