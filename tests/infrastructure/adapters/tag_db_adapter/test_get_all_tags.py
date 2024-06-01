from articles.infrastructure.adapters.adapters import TagDbAdapter
from tests.factory import TagEntityFactory


def test_get_all_tags(tag_db_adapter: TagDbAdapter) -> None:
    tags = TagEntityFactory.create_batch(5)
    result = tag_db_adapter.get_all_tags()
    assert len(tags) == len(result)
