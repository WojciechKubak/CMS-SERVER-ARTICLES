from articles.infrastructure.storage.boto3 import Boto3Service
from boto3 import resource


def test_upload_to_txt_file(
        conn: resource,
        service: Boto3Service,
        bucket_name: str
) -> None:
    file_content = 'Hello, World!'

    result = service.upload_to_file(file_content, 'subfolder')
    expected = conn.Object(bucket_name, result).get()['Body'].read() \
        .decode('utf-8')

    assert expected == file_content
