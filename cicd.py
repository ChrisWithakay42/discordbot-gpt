import boto3


class AwsSecretManager:

    def __init__(self, client):
        self.client = client
