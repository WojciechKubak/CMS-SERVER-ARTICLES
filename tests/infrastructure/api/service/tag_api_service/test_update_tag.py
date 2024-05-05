from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.db.entity import TagEntity
from articles.infrastructure.api.dto import TagDTO
from sqlalchemy.orm import Session
import pytest


class TestUpdateTag:

    def test_when_not_found(self, tag_api_service: TagApiService) -> None:
        tag_dto = TagDTO(
            id_=1,
            name='name'
        )
        with pytest.raises(ValueError) as err:
            tag_api_service.update_tag(tag_dto)
            assert 'Tag does not exist' == str(err.value)

    def test_when_name_exists(self, tag_api_service: TagApiService, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        tag_dto = TagDTO(
            id_=2,
            name='name'
        )
        with pytest.raises(ValueError) as err:
            tag_api_service.update_tag(tag_dto)
            assert 'Tag name already exists' == str(err.value)

    def test_when_updated(self, tag_api_service: TagApiService, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        tag_dto = TagDTO(
            id_=1,
            name='updated_name'
        )
        result = tag_api_service.update_tag(tag_dto)
        assert 'updated_name' == db_session.query(TagEntity).filter_by(id=result.id_).first().name
