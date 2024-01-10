from articles.infrastructure.db.entity import CategoryEntity


def test_to_domain() -> None:
    category_dao = CategoryEntity(id=1, name='name', description='dummy')
    result = category_dao.to_domain()
    assert category_dao.id == result.id_
    assert category_dao.name == result.name
