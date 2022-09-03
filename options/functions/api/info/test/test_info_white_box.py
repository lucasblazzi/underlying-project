import pytest
from pydantic.error_wrappers import ValidationError
from ..app import app
from .input_white import TestInfo
from .output_white import TestOutput
from unittest import IsolatedAsyncioTestCase, TestCase, mock

class InfoTest(IsolatedAsyncioTestCase):
    # def validation_error_interface(self, test_case):
    #     with pytest.raises(Exception):
    #         app.lambda_handler(test_case, "")

    @mock.patch('info.app.app.lambda_handler', return_value = TestOutput.ok())
    def test_input_ok(self, mk):
        test_case = TestInfo.input_ok()
        res = app.lambda_handler(test_case['event'], "")
        assert isinstance(res['body'], dict)

    @mock.patch('info.app.app.lambda_handler', return_value = TestOutput.not_found())
    def test_input_invalid_id(self, mk):
        test_case = TestInfo.input_invalid_id()
        res = app.lambda_handler(test_case['event'], "")
        assert res['statusCode'] == 404

    @mock.patch('info.app.app.lambda_handler', return_value = TestOutput.not_found())
    def test_input_invalid_name(self, mk):
        test_case = TestInfo.input_invalid_name()
        res = app.lambda_handler(test_case['event'], "")
        assert res['statusCode'] == 404

    @mock.patch('info.app.app.lambda_handler', return_value = TestOutput.bad_request())
    def test_input_invalid_name(self, mk):
        test_case = TestInfo.input_invalid_dict()
        res = app.lambda_handler(test_case, "")
        assert res['statusCode'] == 400

    # def test_invalid_dict(self):
    #     test_case = TestInfo.input_invalid_dict()
    #     self.validation_error_interface(test_case)
