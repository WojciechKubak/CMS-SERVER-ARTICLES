from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session
import pytest


class TestCreateTag:

    def test_when_name_exists(self, tag_api_service: TagApiService, db_session: Session) -> None:
        db_session.add(TagEntity(name='name'))
        db_session.commit()
        tag_dto = {'name': 'name'}
        with pytest.raises(ValueError) as err:
            tag_api_service.create_tag(tag_dto)
            assert 'Tag name already exists' == str(err.value)

    def test_when_created(self, tag_api_service: TagApiService, db_session: Session) -> None:
        result = tag_api_service.create_tag({'name': 'name'})
        assert db_session.query(TagEntity).filter_by(id=result.id_).first()
