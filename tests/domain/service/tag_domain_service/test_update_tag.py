from articles.domain.service import TagService
from articles.domain.errors import TagNotFoundError, TagNameExistsError
from articles.infrastructure.persistance.entity import TagEntity
from tests.factory import TagEntityFactory, TagFactory
import pytest


class TestUpdateTag:

    def test_when_not_found(self, tag_domain_service: TagService) -> None:
        tag = TagFactory()
        with pytest.raises(TagNotFoundError) as e:
            tag_domain_service.update_tag(tag)
        assert TagNotFoundError().message == str(e.value)

    def test_when_name_exists(self, tag_domain_service: TagService) -> None:
        tag_dao_first, tag_dao_second = TagEntityFactory.create_batch(2)
        tag = TagFactory(id_=tag_dao_first.id, name=tag_dao_second.name)

        with pytest.raises(TagNameExistsError) as e:
            tag_domain_service.update_tag(tag)

        assert TagNameExistsError().message == str(e.value)

    def test_when_updated(self, tag_domain_service: TagService) -> None:
        tag_dao = TagEntityFactory()
        new_name = f"new_{tag_dao.name}"
        tag = TagFactory(id_=tag_dao.id, name=new_name)

        result = tag_domain_service.update_tag(tag)

        assert TagEntity.query.filter_by(id=result.id_).first().name == new_name
