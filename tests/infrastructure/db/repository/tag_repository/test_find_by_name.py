from articles.infrastructure.persistance.repository import TagRepository
from tests.factory import TagEntityFactory


def test_find_by_name(tag_repository: TagRepository) -> None:
    tag = TagEntityFactory()
    result = tag_repository.find_by_name(tag.name)
    assert tag == result
