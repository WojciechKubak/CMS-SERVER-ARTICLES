from articles.domain.model import Tag


def test_to_json() -> None:
    tag = Tag(id_=1, name='name')
    result = tag.to_json()
    tag_ad_dict = tag.__dict__
    assert tag_ad_dict.pop('id_') == result['id']
    assert tag_ad_dict.items() < result.items()
