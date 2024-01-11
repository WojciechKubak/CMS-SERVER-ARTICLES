from articles.domain.service import CategoryDomainService
from articles.infrastructure.db.entity import CategoryEntity
from articles.domain.model import Category
from sqlalchemy.orm import Session
import pytest


class TestUpdateCategory:

    def test_when_not_found(self, category_domain_service: CategoryDomainService, db_session: Session) -> None:
        category = Category(id_=1, name='name', description='dummy')
        with pytest.raises(ValueError) as err:
            category_domain_service.update_category(category)
            assert 'Category does not exist' == str(err.value)

    def test_when_name_exists(self, category_domain_service: CategoryDomainService, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name', description='dummy'))
        db_session.commit()
        category = Category(id_=2, name='name', description='dummy')
        with pytest.raises(ValueError) as err:
            category_domain_service.update_category(category)
            assert 'Category name already exists' == str(err.value)

    def test_when_updated(self, category_domain_service: CategoryDomainService, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name', description='dummy'))
        db_session.commit()
        category = Category(id_=1, name='updated_name', description='dummy')
        result = category_domain_service.update_category(category)
        assert 'updated_name' == db_session.query(CategoryEntity).filter_by(id=result.id_).first().name
