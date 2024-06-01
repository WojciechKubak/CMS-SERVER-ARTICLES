from articles.domain.service import CategoryService
from tests.factory import CategoryEntityFactory


class TestGetAllCategories:

    def test_when_no_categores(
            self,
            category_domain_service: CategoryService
    ) -> None:
        result = category_domain_service.get_all_categories()
        assert not result

    def test_when_categories(
            self,
            category_domain_service: CategoryService
    ) -> None:
        categories = CategoryEntityFactory.create_batch(5)
        result = category_domain_service.get_all_categories()
        assert len(categories) == len(result)
