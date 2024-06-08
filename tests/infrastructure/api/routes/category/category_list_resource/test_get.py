from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


def test_category_list_resource_get(client: Client, base_path: str) -> None:
    mock_category = MagicMock()
    mock_category.to_dict.return_value = {"id": 1, "name": "test_name"}

    with patch(
        f"{base_path}.category_service.get_all_categories"
    ) as mock_get_categorys:
        mock_get_categorys.return_value = [mock_category]
        response = client.get(url_for("categorylistresource"))

    mock_get_categorys.assert_called_once()
    assert 200 == response.status_code
    assert [{"id": 1, "name": "test_name"}] == response.get_json()
