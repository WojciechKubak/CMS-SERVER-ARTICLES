from articles.domain.service import CategoryService
from articles.domain.errors import CategoryNameExistsError
from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryEntityFactory, CategoryFactory
import pytest


class TestCreateCategory:

    def test_when_name_exists(
            self,
            category_domain_service: CategoryService
    ) -> None:
        category_dao = CategoryEntityFactory()
        category = CategoryFactory(name=category_dao.name)

        with pytest.raises(CategoryNameExistsError) as e:
            category_domain_service.create_category(category)

        assert CategoryNameExistsError().message == str(e.value)

    def test_when_created(
            self,
            category_domain_service: CategoryService
    ) -> None:
        category = CategoryFactory()
        result = category_domain_service.create_category(category)
        assert CategoryEntity.query.filter_by(id=result.id_).first()
