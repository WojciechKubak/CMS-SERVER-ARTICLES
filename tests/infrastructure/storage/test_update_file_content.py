from articles.infrastructure.storage.boto3 import Boto3Service
from boto3 import resource


def test_update_file_content(
        conn: resource,
        boto3_service: Boto3Service,
        bucket_name: str
) -> None:
    conn.Bucket(bucket_name).put_object(Key='myfile.txt', Body='Hello, World!')
    updated_file_content = 'Hello!'

    boto3_service.update_file_content('myfile.txt', updated_file_content)
    expected = conn.Object(bucket_name, 'myfile.txt').get()['Body'].read() \
        .decode('utf-8')

    assert expected == updated_file_content
