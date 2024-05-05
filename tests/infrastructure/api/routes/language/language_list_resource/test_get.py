from articles.infrastructure.db.entity import LanguageEntity
from flask.testing import Client
from sqlalchemy.orm import Session


def test_language_list_resource_get(client: Client, db_session: Session) -> None:
    languages_dto = [
        LanguageEntity(name='name1', code='code1'), 
        LanguageEntity(name='name2', code='code2')
    ]
    db_session.bulk_save_objects(languages_dto)
    db_session.commit()
    response = client.get('articles/languages')
    assert 200 == response.status_code
    assert len(languages_dto) == len(response.json)
