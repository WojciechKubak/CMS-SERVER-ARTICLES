from articles.infrastructure.persistance.entity import TagEntity
from tests.factory import TagFactory


def test_from_domain() -> None:
    tag = TagFactory()
    result = TagEntity.from_domain(tag)
    assert tag.id_ == result.id
    assert tag.name == result.name
