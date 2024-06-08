from articles.domain.service import CategoryService
from articles.domain.errors import CategoryNotFoundError, CategoryNameExistsError
from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryEntityFactory, CategoryFactory
import pytest


class TestUpdateCategory:

    def test_when_not_found(self, category_domain_service: CategoryService) -> None:
        category = CategoryFactory()
        with pytest.raises(CategoryNotFoundError) as e:
            category_domain_service.update_category(category)
        assert CategoryNotFoundError().message == str(e.value)

    def test_when_name_exists(self, category_domain_service: CategoryService) -> None:
        category_dao_first, category_dao_second = CategoryEntityFactory.create_batch(2)
        category = CategoryFactory(
            id_=category_dao_first.id, name=category_dao_second.name
        )

        with pytest.raises(CategoryNameExistsError) as e:
            category_domain_service.update_category(category)

        assert CategoryNameExistsError().message == str(e.value)

    def test_when_updated(self, category_domain_service: CategoryService) -> None:
        category_dao = CategoryEntityFactory()
        new_name = f"new_{category_dao.name}"
        category = CategoryFactory(id_=category_dao.id, name=new_name)

        result = category_domain_service.update_category(category)

        assert CategoryEntity.query.filter_by(id=result.id_).first().name == new_name
