from articles.infrastructure.db.entity import TagEntity
from articles.domain.model import Tag


def test_from_domain() -> None:
    tag = Tag(id_=1, name='name')
    result = TagEntity.from_domain(tag)
    assert tag.id_ == result.id
    assert tag.name == result.name
