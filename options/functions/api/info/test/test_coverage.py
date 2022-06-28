import sys

from .test_env.resources import s3_option_series
from .test_env.aws import aws_credentials, lambda_context, s3_client


from ..app.app import lambda_handler
#from .input_coverage import CoverageInput


def test_lambda_handler_update(aws_credentials, s3_option_series, s3_client, lambda_context):
    #event = CoverageInput.input_update()
    temp = {
            "event": {
                "body": '{"id": "60137665a3315885b579abe6803b55d0", "name": "BOVAA100"}'
            },
            "context": None
        }
    res = lambda_handler(temp['event'], temp['context'])
    assert res["statusCode"] == 200


# def test_lambda_handler_share(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
#     event = CoverageInput.input_share()
#     res = lambda_handler(event, lambda_context)
#     assert res["statusCode"] == 200


# def test_lambda_handler_delete(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
#     event = CoverageInput.input_delete()
#     res = lambda_handler(event, lambda_context)
#     assert res["statusCode"] == 200


# def test_lambda_handler_error_422(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
#     event = CoverageInput.input_error_422()
#     res = lambda_handler(event, lambda_context)
#     assert res["statusCode"] == 422


# def test_lambda_handler_error_500(aws_credentials, dynamodb_strategies, dynamodb_resource, lambda_context):
#     event = CoverageInput.input_error_500()
#     res = lambda_handler(event, lambda_context)
#     assert res["statusCode"] == 500