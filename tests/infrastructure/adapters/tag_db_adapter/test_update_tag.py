from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.persistance.entity import TagEntity
from tests.factory import TagEntityFactory, TagFactory


def test_update_tag(tag_db_adapter: TagDbAdapter) -> None:
    tag_dao = TagEntityFactory()
    new_name = f"new_{tag_dao.name}"
    tag = TagFactory(name=new_name)

    result = tag_db_adapter.update_tag(tag)

    assert TagEntity.query.filter_by(id=result.id_).first().name == new_name
