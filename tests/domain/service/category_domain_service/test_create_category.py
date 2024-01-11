from articles.domain.service import CategoryDomainService
from articles.infrastructure.db.entity import CategoryEntity
from articles.domain.model import Category
from sqlalchemy.orm import Session
import pytest


class TestCreateCategory:

    def test_when_name_exists(self, category_domain_service: CategoryDomainService, db_session: Session) -> None:
        db_session.add(CategoryEntity(name='name'))
        db_session.commit()
        category = Category(id_=None, name='name', description='dummy')
        with pytest.raises(ValueError) as err:
            category_domain_service.create_category(category)
            assert 'Category name already exists' == str(err.value)

    def test_when_created(self, category_domain_service: CategoryDomainService, db_session: Session) -> None:
        category = Category(id_=None, name='name', description='dummy')
        result = category_domain_service.create_category(category)
        assert db_session.query(CategoryEntity).filter_by(id=result.id_).first()
