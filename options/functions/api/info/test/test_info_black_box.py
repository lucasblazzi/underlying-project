import pytest
import pandas as pd
import boto3
import botocore
import logging

from pandas.testing import assert_frame_equal
from moto import mock_s3
from io import BytesIO
from unittest import IsolatedAsyncioTestCase, TestCase, mock

import sys
sys.path.insert(0, '../app/')

from ..test.input import TestInput
from ..test.output import TestOutput

from ..app import app
MY_BUCKET = 'testBucket'

class TestInfo(TestCase):
    def test_preprocess_payload(self):
        _preprocess_payload_input = TestInput.preprocess_payload_input()['option']
        _preprocess_payload_output = TestOutput.preprocess_payload_output()
        result = app.preprocess_payload(_preprocess_payload_input)
        self.assertEqual(result, _preprocess_payload_output)

@mock_s3
class TestInfoAsyncio(IsolatedAsyncioTestCase):
    boto3.DEFAULT_SESSION = None
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("TestInfoAsyncio.show_bucket").setLevel(logging.DEBUG)
    logging.getLogger("TestInfoAsyncio.test_get_option").setLevel(logging.DEBUG)
    
    def setUp(self):
        
        client = boto3.client(
            "s3",
            region_name="us-east-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
            )
        try:
            s3 = boto3.resource(
                "s3",
                region_name="us-east-1",
                aws_access_key_id="fake_access_key",
                aws_secret_access_key="fake_secret_key",
                )
            s3.meta.client.head_bucket(Bucket=MY_BUCKET)
        except botocore.exceptions.ClientError:
            pass
        else:
            err = "{bucket} should not exist.".format(bucket=MY_BUCKET)
            raise EnvironmentError(err)
        client.create_bucket(Bucket=MY_BUCKET)
        self.dataframe_to_s3(MY_BUCKET)
        self.show_bucket(MY_BUCKET, s3)
    def tearDown(self):
        s3 = boto3.resource(
            "s3",
            region_name="us-east-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
            )
        bucket = s3.Bucket(MY_BUCKET)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()


    def dataframe_to_s3(self, bucket_name):
        s3_client = boto3.client("s3")
        out_buffer = BytesIO()
        TestOutput.get_option_output().to_parquet(out_buffer, index=False)
        filepath = f"name={TestInput.get_option_input()['option']['name']}"
        s3_client.put_object(Bucket=bucket_name, Key=filepath, Body=out_buffer.getvalue())

    def show_bucket(self, bucket, s3):
        my_bucket = s3.Bucket(bucket)
        log = logging.getLogger("TestInfoAsyncio.show_bucket")
        for my_bucket_object in my_bucket.objects.all():
            log.debug(my_bucket_object)

    async def test_get_option_except(self):
        _get_option_input = TestInput.get_option_input()['option']
        _get_option_output = TestOutput.get_option_output()
        with pytest.raises(Exception):
            result = await app.get_option(_get_option_input)
        

    @mock.patch('info.app.app.get_option', return_value = TestOutput.get_option_output())
    async def test_get_option(self, mk_get_option):
        _get_option_input = TestInput.get_option_input()['option']
        _get_option_output = TestOutput.get_option_output()
        result = await app.get_option(_get_option_input)
        assert_frame_equal(result, _get_option_output)

    @mock.patch('info.app.app.get_payoff', return_value = TestOutput.get_payoff_output())
    async def test_get_payoff(self, mk_get_payoff):
        _get_payoff_input = TestInput.get_payoff_input()['option']
        _get_payoff_output = TestOutput.get_payoff_output()
        result = await app.get_payoff(_get_payoff_input)
        self.assertEqual(result, _get_payoff_output)

    @mock.patch('info.app.app.handler', return_value = TestOutput.handler_output())
    async def test_handler(self, mk_handler):
        _handler_input = TestInput.handler_input()['event']
        _handler_output = TestOutput.handler_output()
        result = await app.handler(_handler_input)
        self.assertEqual(result, _handler_output)
    
    @mock.patch('info.app.app.lambda_handler', return_value = TestOutput.lambda_handler_output())
    def test_lambda_handler(self, mk_test_lambda_handler):
        _lambda_handler_input = TestInput.lambda_handler_input()
        _lambda_handler_output = TestOutput.lambda_handler_output()
        result = app.lambda_handler(_lambda_handler_input['event'], _lambda_handler_input['context'])
        self.assertEqual(result, _lambda_handler_output)
