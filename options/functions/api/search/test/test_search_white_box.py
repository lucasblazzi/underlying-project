import pytest
from unittest import mock, TestCase, IsolatedAsyncioTestCase

import sys
sys.path.insert(0, '../app/')

from ..test.input import TestInput
from ..test.output import TestOutput

from ..app import app

class TestSeach(TestCase):
    @mock.patch('search.app.app.lambda_handler', return_value = TestOutput.lambda_handler_output())
    def test_lambda_handler(self, mock_test_lambda_handler):
        _lambda_handler_input = TestInput.lambda_handler_input()
        _lambda_handler_output = TestOutput.lambda_handler_output()
        result = app.lambda_handler(_lambda_handler_input['event'], _lambda_handler_input['context'])
        self.assertEqual(result, _lambda_handler_output)


    