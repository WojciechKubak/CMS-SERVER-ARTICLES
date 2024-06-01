from articles.domain.service import TagService
from articles.domain.errors import TagNotFoundError
from articles.infrastructure.persistance.entity import TagEntity
from tests.factory import TagEntityFactory
import pytest


class TestDeleteTag:

    def test_when_not_found(self, tag_domain_service: TagService) -> None:
        with pytest.raises(TagNotFoundError) as e:
            tag_domain_service.delete_tag(999)
        assert TagNotFoundError().message == str(e.value)

    def test_when_deleted(self, tag_domain_service: TagService) -> None:
        tag = TagEntityFactory()
        result = tag_domain_service.delete_tag(tag.id)
        assert not TagEntity.query.filter_by(id=result).first()
