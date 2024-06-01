from articles.infrastructure.adapters.adapters import TagDbAdapter
from tests.factory import TagEntityFactory


class TestGetTagById:

    def test_when_not_found(self, tag_db_adapter: TagDbAdapter) -> None:
        result = tag_db_adapter.get_tag_by_id(999)
        assert not result

    def test_when_found(self, tag_db_adapter: TagDbAdapter) -> None:
        tag = TagEntityFactory()
        result = tag_db_adapter.get_tag_by_id(tag.id)
        assert tag.id == result.id_
