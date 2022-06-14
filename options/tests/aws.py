import os
import boto3
import pytest

from moto import mock_s3
from moto import mock_dynamodb
from moto import mock_dynamodb2


class LambdaContext(object):

    def __init__(self, lambda_name):
        self.function_name = lambda_name
        self.function_version = "v$LATEST"
        self.memory_limit_in_mb = 256
        self.invoked_function_arn = f"arn:aws:lambda:us-east-1:12345678:function{lambda_name}"
        self.aws_request_id = "random-id-for-testing-mocks"


@pytest.fixture
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "mock_test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "mock_test"
    os.environ["AWS_SECURITY_TOKEN"] = "mock_test"
    os.environ["AWS_SESSION_TOKEN"] = "mock_test"
    os.environ["AWS_REGION_NAME"] = "mock_test"


@pytest.fixture
def lambda_context():
    return LambdaContext("test-function")


@pytest.fixture
def dynamodb_client(aws_credentials):
    with mock_dynamodb():
        yield boto3.client("dynamodb", region_name="us-east-1")


@pytest.fixture
def dynamodb_resource(aws_credentials):
    with mock_dynamodb2():
        yield boto3.resource("dynamodb", region_name="us-east-1")


@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        yield boto3.client("s3", region_name="us-east-1")
