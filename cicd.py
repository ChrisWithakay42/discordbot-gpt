import boto3


class AwsSecretManagerManager:

    def __init__(self, client):
        self.client = client
