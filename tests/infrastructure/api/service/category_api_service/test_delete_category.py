from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session
import pytest


class TestDeleteCategory:

    def test_when_not_found(self, category_api_service: CategoryApiService) -> None:
        with pytest.raises(ValueError) as err:
            category_api_service.delete_category(9999)
        assert 'Category does not exist' == str(err.value)

    def test_when_deleted(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name'))
        db_session.commit()
        result = category_api_service.delete_category(1)
        assert not db_session.query(CategoryEntity).filter_by(id=result).first()
