from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


def test_tag_list_resource_get(client: Client, base_path: str) -> None:
    mock_tag = MagicMock()
    mock_tag.to_dict.return_value = {
        'id': 1,
        'name': 'test_name'
    }

    with patch(
        f'{base_path}.tag_service.get_all_tags'
    ) as mock_get_tags:
        mock_get_tags.return_value = [mock_tag]
        response = client.get(url_for('taglistresource'))

    mock_get_tags.assert_called_once()
    assert 200 == response.status_code
    assert [{'id': 1, 'name': 'test_name'}] == response.get_json()
