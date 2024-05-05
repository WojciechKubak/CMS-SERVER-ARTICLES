from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.db.entity import CategoryEntity
from articles.infrastructure.api.dto import CategoryDTO
from sqlalchemy.orm import Session
import pytest


class TestCreateCategory:

    def test_when_name_exists(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        db_session.add(CategoryEntity(name='name', description='dummy'))
        db_session.commit()
        category_dto = CategoryDTO(
            id_=None,
            name='name',
            description='dummy'
        )
        with pytest.raises(ValueError) as err:
            category_api_service.create_category(category_dto)
            assert 'Category name already exists' == str(err.value)

    def test_when_created(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        category_dto = CategoryDTO(
            id_=None,
            name='name',
            description='dummy'
        )
        result = category_api_service.create_category(category_dto)
        assert db_session.query(CategoryEntity).filter_by(id=result.id_).first()
