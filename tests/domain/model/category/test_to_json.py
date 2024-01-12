from articles.domain.model import Category


def test_to_json() -> None:
    category = Category(id_=1, name='name', description='dummy')
    result = category.to_json()
    category_ad_dict = category.__dict__
    assert category_ad_dict.pop('id_') == result['id']
    assert category_ad_dict.items() < result.items()
