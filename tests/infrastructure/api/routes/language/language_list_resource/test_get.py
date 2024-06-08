from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


def test_language_list_resource_get(client: Client, base_path: str) -> None:
    mock_language = MagicMock()
    mock_language.to_dict.return_value = {"id": 1, "name": "test_name"}

    with patch(f"{base_path}.language_service.get_all_languages") as mock_get_languages:
        mock_get_languages.return_value = [mock_language]
        response = client.get(url_for("languagelistresource"))

    mock_get_languages.assert_called_once()
    assert 200 == response.status_code
    assert [{"id": 1, "name": "test_name"}] == response.get_json()
