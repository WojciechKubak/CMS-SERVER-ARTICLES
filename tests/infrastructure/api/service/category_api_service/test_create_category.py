from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session
import pytest


class TestCreateCategory:

    def test_when_name_exists(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        db_session.add(CategoryEntity(name='name', description='dummy'))
        db_session.commit()
        category_dto = {'name': 'name'}
        with pytest.raises(ValueError) as err:
            category_api_service.create_category(category_dto)
            assert 'Category name already exists' == str(err.value)

    def test_when_created(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        result = category_api_service.create_category({'name': 'name', 'description': 'dummy'})
        assert db_session.query(CategoryEntity).filter_by(id=result.id_).first()
