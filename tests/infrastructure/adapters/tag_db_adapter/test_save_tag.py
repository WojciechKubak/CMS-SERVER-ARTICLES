from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.persistance.entity import TagEntity
from tests.factory import TagFactory


def test_save_tag(tag_db_adapter: TagDbAdapter) -> None:
    tag = TagFactory()
    result = tag_db_adapter.save_tag(tag)
    assert TagEntity.query.filter_by(id=result.id_).first()
