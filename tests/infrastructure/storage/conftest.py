from articles.infrastructure.storage.boto3 import Boto3Service
from moto import mock_aws
from boto3 import resource
import pytest


@pytest.fixture(scope="session")
def bucket_name() -> str:
    return "bucket_name"


@pytest.fixture(scope="session")
def conn() -> resource:
    with mock_aws():
        conn = resource("s3")
        yield conn


@pytest.fixture(scope="session")
def boto3_service(conn, bucket_name: str) -> Boto3Service:
    conn.create_bucket(Bucket=bucket_name)
    service = Boto3Service(
        "access_key_id", "secret_access_key", "bucket_name", "subfolder_name"
    )
    yield service
