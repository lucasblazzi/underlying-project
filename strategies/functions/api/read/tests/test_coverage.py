import sys

from .testenv.resources import dynamodb_strategies
from .testenv.aws import aws_credentials, lambda_context, dynamodb_resource


from ..app.app import lambda_handler
from .input_coverage import CoverageInput


def test_lambda_handler_read_strategy(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_read_strategy()
    res = lambda_handler(event, lambda_context)
    print(res)
    assert res["statusCode"] == 200


def test_lambda_handler_read_shared(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_read_shared()
    res = lambda_handler(event, lambda_context)
    print(res)
    assert res["statusCode"] == 200
