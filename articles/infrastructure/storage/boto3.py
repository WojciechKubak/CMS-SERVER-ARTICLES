from dataclasses import dataclass
import boto3
import uuid


@dataclass
class Boto3Service:
    """
    Service class for S3 operations using boto3.

    Attributes:
        access_key_id (str): AWS access key ID.
        secret_access_key (str): AWS secret access key.
        bucket_name (str): Name of the S3 bucket.
        bucket_subfolder_name (str): Name of the subfolder in the bucket.
    """

    access_key_id: str
    secret_access_key: str
    bucket_name: str
    bucket_subfolder_name: str

    def __post_init__(self):
        """
        Initialize the S3 client after the instance is created.
        """
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key
        )

    def upload_to_file(self, content: str, file_extension: str = 'txt') -> str:
        """
        Upload content to an S3 file.

        Args:
            content (str): Content to be uploaded.
            file_extension (str, optional): File extension. Defaults to 'txt'.

        Returns:
            str: Path of the uploaded file.
        """
        file_name = f"{uuid.uuid4().hex}.{file_extension}"
        file_path = f"{self.bucket_subfolder_name}/{file_name}"
        self.s3.put_object(
            Body=content,
            Bucket=self.bucket_name,
            Key=file_path
        )
        return file_path

    def update_file_content(self, path: str, new_content: str) -> None:
        """
        Update the content of an S3 file.

        Args:
            path (str): Path of the file to be updated.
            new_content (str): New content to be uploaded.
        """
        self.s3.put_object(Body=new_content, Bucket=self.bucket_name, Key=path)

    def delete_file(self, path: str) -> None:
        """
        Delete an S3 file.

        Args:
            path (str): Path of the file to be deleted.
        """
        self.s3.delete_object(Bucket=self.bucket_name, Key=path)

    def read_file_content(self, path: str) -> str:
        """
        Read the content of an S3 file.

        Args:
            path (str): Path of the file to be read.

        Returns:
            str: Content of the file.
        """
        response = self.s3.get_object(Bucket=self.bucket_name, Key=path)
        content = response['Body'].read().decode('utf-8')
        return content
