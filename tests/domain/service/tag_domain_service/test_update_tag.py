from articles.domain.service import TagDomainService
from articles.infrastructure.db.entity import TagEntity
from articles.domain.model import Tag
from sqlalchemy.orm import Session
import pytest


class TestUpdateTag:

    def test_when_not_found(self, tag_domain_service: TagDomainService, db_session: Session) -> None:
        tag = Tag(id_=1, name='name')
        with pytest.raises(ValueError) as err:
            tag_domain_service.update_tag(tag)
            assert 'Tag does not exist' == str(err.value)

    def test_when_name_exists(self, tag_domain_service: TagDomainService, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        tag = Tag(id_=2, name='name')
        with pytest.raises(ValueError) as err:
            tag_domain_service.update_tag(tag)
            assert 'Tag name already exists' == str(err.value)

    def test_when_updated(self, tag_domain_service: TagDomainService, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        tag = Tag(id_=1, name='updated_name')
        result = tag_domain_service.update_tag(tag)
        assert 'updated_name' == db_session.query(TagEntity).filter_by(id=result.id_).first().name
