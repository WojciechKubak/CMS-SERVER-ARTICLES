from articles.domain.service import CategoryService
from articles.domain.errors import CategoryNotFoundError
from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryEntityFactory
import pytest


class TestDeleteCategory:

    def test_when_not_found(self, category_domain_service: CategoryService) -> None:
        with pytest.raises(CategoryNotFoundError) as e:
            category_domain_service.delete_category(999)
        assert CategoryNotFoundError().message == str(e.value)

    def test_when_deleted(self, category_domain_service: CategoryService) -> None:
        category = CategoryEntityFactory()
        id_ = category_domain_service.delete_category(category.id)
        assert not CategoryEntity.query.filter_by(id=id_).first()
