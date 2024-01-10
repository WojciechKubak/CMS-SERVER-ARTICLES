from articles.infrastructure.db.connection import MySQLConnectionStringBuilder
import pytest


class TestConnectionStringBuilder:

    @pytest.fixture(scope='session')
    def default_connection_url(self) -> str:
        return 'mysql://user:user1234@localhost:3307/db_1'

    def test_with_default_configuration(self, default_connection_url: str) -> None:
        result = MySQLConnectionStringBuilder.builder().build()
        assert default_connection_url == result

    def test_with_custom_parameters(self) -> None:
        new_conifg = {'database': 'new_database', 'user': 'new_user'}
        result = MySQLConnectionStringBuilder.builder(new_conifg).build()
        assert all([property_ in result for property_ in new_conifg.values()])

    def test_with_chained_configuration(self) -> None:
        new_password = '12345'
        result = MySQLConnectionStringBuilder.builder().password(new_password).build()
        assert new_password in result
