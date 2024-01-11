from articles.domain.service import TagDomainService
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session
import pytest


class TestDeleteTag:

    def test_when_not_found(self, tag_domain_service: TagDomainService) -> None:
        with pytest.raises(ValueError) as err:
            tag_domain_service.delete_tag(9999)
        assert 'Tag does not exist' == str(err.value)

    def test_when_deleted(self, tag_domain_service: TagDomainService, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        result = tag_domain_service.delete_tag(1)
        assert not db_session.query(TagEntity).filter_by(id=result).first()
