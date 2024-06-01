from articles.domain.service import TagService
from articles.domain.errors import TagNameExistsError
from articles.infrastructure.persistance.entity import TagEntity
from tests.factory import TagEntityFactory, TagFactory
import pytest


class TestCreateTag:

    def test_when_name_exists(self, tag_domain_service: TagService) -> None:
        tag_dao = TagEntityFactory()
        tag = TagFactory(name=tag_dao.name)

        with pytest.raises(TagNameExistsError) as e:
            tag_domain_service.create_tag(tag)

        assert TagNameExistsError().message == str(e.value)

    def test_when_created(self, tag_domain_service: TagService) -> None:
        tag = TagFactory()
        result = tag_domain_service.create_tag(tag)
        assert TagEntity.query.filter_by(id=result.id_).first()
