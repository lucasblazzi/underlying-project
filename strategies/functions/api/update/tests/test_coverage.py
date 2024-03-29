import sys

from .testenv.resources import dynamodb_strategies
from .testenv.aws import aws_credentials, lambda_context, dynamodb_resource


from ..app.app import lambda_handler
from .input_coverage import CoverageInput


def test_lambda_handler_update(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_update()
    res = lambda_handler(event, lambda_context)
    assert res["statusCode"] == 200


def test_lambda_handler_share(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_share()
    res = lambda_handler(event, lambda_context)
    assert res["statusCode"] == 200


def test_lambda_handler_delete(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_delete()
    res = lambda_handler(event, lambda_context)
    assert res["statusCode"] == 200


def test_lambda_handler_error_422(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_error_422()
    res = lambda_handler(event, lambda_context)
    assert res["statusCode"] == 422


def test_lambda_handler_error_500(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
    event = CoverageInput.input_error_500()
    res = lambda_handler(event, lambda_context)
    assert res["statusCode"] == 500