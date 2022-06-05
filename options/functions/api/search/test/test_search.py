from unittest import mock, TestCase, IsolatedAsyncioTestCase
from input import TestInput
from output import TestOutput

import sys
sys.path.insert(0, '../app/')
import app

class TestSeach(TestCase):
    def test_get_query(self):
        _get_query_input = TestInput.get_query_input()['query']
        _get_query_output = TestOutput.get_query_output()
        result = app.get_query(_get_query_input)
        self.assertEqual(result, _get_query_output)
    
    @mock.patch('app.query_options', return_value = TestOutput.query_options_output())
    def test_query_options(self, mock_test_query_options):
        _query_options_input = TestInput.query_options_input()['user_input']
        _query_options_output = TestOutput.query_options_output()
        result = app.query_options(_query_options_input)
        self.assertEqual(result, _query_options_output)

    @mock.patch('app.lambda_handler', return_value = TestOutput.lambda_handler_output())
    def test_lambda_handler(self, mock_test_lambda_handler):
        _lambda_handler_input = TestInput.lambda_handler_input()
        _lambda_handler_output = TestOutput.lambda_handler_output()
        result = app.lambda_handler(_lambda_handler_input['event'], _lambda_handler_input['context'])
        self.assertEqual(result, _lambda_handler_output)

class TestSeachAsyncio(IsolatedAsyncioTestCase):
    @mock.patch('app.handler', return_value = TestOutput.handler_output())
    async def test_handler(self, mock_test_handler):
        _handler_input = TestInput.handler_input()['event']
        _handler_output = TestOutput.handler_output()
        result = await app.handler(_handler_input)
        self.assertEqual(result, _handler_output)

    