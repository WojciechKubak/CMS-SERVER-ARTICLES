from tests.factory import TagEntityFactory


def test_to_domain() -> None:
    tag = TagEntityFactory()
    result = tag.to_domain()
    assert tag.id == result.id_
    assert tag.name == result.name
