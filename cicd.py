import boto3
from environs import Env

env = Env()
env.read_env()

session = boto3.Session(
    aws_access_key_id=env.str('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=env.str('AWS_SECRET_ACCESS_KEY'),
    region_name='eu-west-2'
)


class AwsSecretManagerManager:

    def __init__(self, client):
        self.client = client


class AwsApiGatewayManager:

    def __init__(self):
        ...


class AwsLambdaManager:

    def __init__(self):
        ...
