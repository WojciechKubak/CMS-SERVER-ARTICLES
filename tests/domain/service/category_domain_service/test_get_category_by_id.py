from articles.domain.service import CategoryService
from articles.domain.errors import CategoryNotFoundError
from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryEntityFactory
import pytest


class TestGetCategoryById:

    def test_when_not_found(self, category_domain_service: CategoryService) -> None:
        with pytest.raises(CategoryNotFoundError) as e:
            category_domain_service.get_category_by_id(999)
        assert CategoryNotFoundError().message == str(e.value)

    def test_when_found(self, category_domain_service: CategoryService) -> None:
        category = CategoryEntityFactory()
        result = category_domain_service.get_category_by_id(category.id)
        assert CategoryEntity.query.filter_by(id=result.id_).first()
