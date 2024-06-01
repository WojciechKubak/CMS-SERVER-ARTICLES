from articles.infrastructure.persistance.repository import TagRepository
from tests.factory import TagEntityFactory


def test_find_many_by_id(tag_repository: TagRepository) -> None:
    tags = TagEntityFactory.create_batch(5)
    tags_id = [tag.id for tag in tags]

    result = tag_repository.find_many_by_id(tags_id)

    assert tags == result
