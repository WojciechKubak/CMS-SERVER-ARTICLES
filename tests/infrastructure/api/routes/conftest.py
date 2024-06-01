import pytest


@pytest.fixture(scope='session')
def base_path() -> str:
    return 'articles.infrastructure.api.routes'
