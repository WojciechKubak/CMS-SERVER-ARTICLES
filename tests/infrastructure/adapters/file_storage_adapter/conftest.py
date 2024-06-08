from articles.infrastructure.storage.boto3 import Boto3Service
from moto import mock_aws
import boto3
import pytest


@pytest.fixture
def bucket_name() -> str:
    return "bucket_name"


@pytest.fixture
def conn() -> boto3.resource:
    with mock_aws():
        conn = boto3.resource("s3")
        yield conn


@pytest.fixture
def service(conn, bucket_name: str) -> Boto3Service:
    conn.create_bucket(Bucket=bucket_name)
    service = Boto3Service(
        "access_key_id", "secret_access_key", "bucket_name", "bucket_subfolder_name"
    )
    yield service
