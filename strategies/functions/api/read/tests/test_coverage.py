import sys

from .test-env.resources import dynamodb_strategies
from .test-env.aws import aws_credentials, lambda_context, dynamodb_resource


from ..app.app import lambda_handler
from .input_coverage import CoverageInput


def test_lambda_handler_x(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_x()
    res = lambda_handler(event, lambda_context)
    print(res)
    assert res["statusCode"] == 200


def test_lambda_handler_y(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_y()
    res = lambda_handler(event, lambda_context)
    print(res)
    assert res["statusCode"] == 200
