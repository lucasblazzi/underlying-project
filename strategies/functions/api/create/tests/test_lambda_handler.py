# import sys
#
# sys.path.insert(1, "../../../../../test_env")
#
# import pytest
# import json
# from ..app.app import lambda_handler
# from .input import TestSuiteA1
#
#
# def test_lambda_handler_200():
#     event = {"body": json.dumps(TestSuiteA1.input_c1())}
#     res = lambda_handler(event, "")
#     assert res["statusCode"] == 200
#
#
# def test_lambda_handler_500():
#     event = {}
#     res = lambda_handler(event, "")
#     assert res["statusCode"] == 500
#
#
# def test_lambda_handler_422():
#     event = {"body": json.dumps(TestSuiteA1.input_c4())}
#     res = lambda_handler(event, "")
#     assert res["statusCode"] == 422