from dataclasses import dataclass
import boto3
import uuid


@dataclass
class S3BucketManager:
    access_key_id: str
    secret_access_key: str
    bucket_name: str
    bucket_subfolder_name: str

    def __post_init__(self):
        self.s3 = boto3.client('s3',
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key
        )

    def upload_to_file(self, content: str, file_extension: str = 'txt') -> str:
        file_name = f"{uuid.uuid4().hex}.{file_extension}"
        file_path = f"{self.bucket_subfolder_name}/{file_name}"
        
        self.s3.put_object(
            Body=content,
            Bucket=self.bucket_name,
            Key=file_path
        )
        
        return file_path

    def update_file_content(self, file_path: str, new_content: str) -> None:
        self.s3.put_object(
            Body=new_content,
            Bucket=self.bucket_name,
            Key=file_path
        )

    def delete_file(self, file_path: str) -> None:
        self.s3.delete_object(
            Bucket=self.bucket_name,
            Key=file_path
        )
    
    def read_file_content(self, file_path: str) -> str:
        response = self.s3.get_object(
            Bucket=self.bucket_name,
            Key=file_path
        )
        content = response['Body'].read().decode('utf-8')
        return content
