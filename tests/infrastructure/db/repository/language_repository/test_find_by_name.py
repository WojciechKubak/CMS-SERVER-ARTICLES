from articles.infrastructure.db.entity import LanguageEntity
from articles.infrastructure.db.repository import LanguageRepository
from sqlalchemy.orm import Session


def test_find_by_name(db_session: Session, language_repository: LanguageRepository) -> None:
    language_name = 'language'
    language = LanguageEntity(id=1, name=language_name, code='CODE')
    db_session.add(language)
    db_session.commit()

    result = language_repository.find_by_name(language_name)
    assert language_name == result.name
