from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.persistance.entity import TagEntity
from tests.factory import TagEntityFactory


def test_delete_tag(tag_db_adapter: TagDbAdapter) -> None:
    tag = TagEntityFactory()
    tag_db_adapter.delete_tag(tag.id)
    assert not TagEntity.query.filter_by(id=tag.id).first()
