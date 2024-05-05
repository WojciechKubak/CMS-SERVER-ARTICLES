from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.db.entity import CategoryEntity
from articles.infrastructure.api.dto import CategoryDTO
from sqlalchemy.orm import Session
import pytest


class TestUpdateCategory:

    def test_when_not_found(self, category_api_service: CategoryApiService) -> None:
        category_dto = CategoryDTO(
            id_=1,
            name='name',
            description='dummy'
        )
        with pytest.raises(ValueError) as err:
            category_api_service.update_category(category_dto)
            assert 'Category does not exist' == str(err.value)

    def test_when_name_exists(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name', description='dummy'))
        db_session.commit()
        category_dto = CategoryDTO(
            id_=2,
            name='name',
            description='dummy'
        )
        with pytest.raises(ValueError) as err:
            category_api_service.update_category(category_dto)
            assert 'Category name already exists' == str(err.value)

    def test_when_updated(self, category_api_service: CategoryApiService, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name', description='dummy'))
        db_session.commit()
        category_dto = CategoryDTO(
            id_=1,
            name='updated_name',
            description='dummy'
        )
        result = category_api_service.update_category(category_dto)
        assert 'updated_name' == db_session.query(CategoryEntity).filter_by(id=result.id_).first().name
