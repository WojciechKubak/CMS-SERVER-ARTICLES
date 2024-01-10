from articles.infrastructure.db.entity import TagEntity


def test_to_domain() -> None:
    tag_dao = TagEntity(id=1, name='name')
    result = tag_dao.to_domain()
    assert tag_dao.id == result.id_
    assert tag_dao.name == result.name
