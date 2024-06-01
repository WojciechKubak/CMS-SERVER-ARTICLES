from articles.infrastructure.adapters.adapters import TagDbAdapter
from tests.factory import TagEntityFactory


def test_get_tags_by_id(tag_db_adapter: TagDbAdapter) -> None:
    tags = TagEntityFactory.create_batch(5)
    tags_id = [tag.id for tag in tags]

    result = tag_db_adapter.get_tags_by_id(tags_id)

    assert len(tags) == len(result)
