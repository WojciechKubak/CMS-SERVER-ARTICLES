from articles.domain.service import TagDomainService
from articles.infrastructure.db.entity import TagEntity
from articles.domain.model import Tag
from sqlalchemy.orm import Session
import pytest


class TestCreateTag:

    def test_when_name_exists(self, tag_domain_service: TagDomainService, db_session: Session) -> None:
        db_session.add(TagEntity(name='name'))
        db_session.commit()
        tag = Tag(id_=None, name='name')
        with pytest.raises(ValueError) as err:
            tag_domain_service.create_tag(tag)
            assert 'Tag name already exists' == str(err.value)

    def test_when_created(self, tag_domain_service: TagDomainService, db_session: Session) -> None:
        tag = Tag(id_=None, name='name')
        result = tag_domain_service.create_tag(tag)
        assert db_session.query(TagEntity).filter_by(id=result.id_).first()
