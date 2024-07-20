import boto3

class CloudStorage:
    def __init__(self, bucket_name):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def upload_file(self, file_name, file_data):
        self.s3.put_object(Body=file_data, Bucket=self.bucket_name, Key=file_name)

    def download_file(self, file_name):
        response = self.s3.get_object(Bucket=self.bucket_name, Key=file_name)
        return response["Body"].read()
