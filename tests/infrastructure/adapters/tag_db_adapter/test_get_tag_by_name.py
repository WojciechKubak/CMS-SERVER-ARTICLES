from articles.infrastructure.adapters.adapters import TagDbAdapter
from tests.factory import TagEntityFactory


class TestGetTagByName:

    def test_when_not_found(self, tag_db_adapter: TagDbAdapter) -> None:
        result = tag_db_adapter.get_tag_by_name('name')
        assert not result

    def test_when_found(self, tag_db_adapter: TagDbAdapter) -> None:
        tag = TagEntityFactory()
        result = tag_db_adapter.get_tag_by_name(tag.name)
        assert tag.name == result.name
