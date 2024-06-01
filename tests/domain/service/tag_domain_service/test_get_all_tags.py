from articles.domain.service import TagService
from tests.factory import TagEntityFactory


class TestGetAllTags:

    def test_when_no_tags(self, tag_domain_service: TagService) -> None:
        result = tag_domain_service.get_all_tags()
        assert not result

    def test_when_tags(self, tag_domain_service: TagService) -> None:
        tags = TagEntityFactory.create_batch(5)
        result = tag_domain_service.get_all_tags()
        assert len(tags) == len(result)
