import sys
sys.path.insert(1, '../app/')
import pytest
from ..app.app import lambda_handler
import json



def test_lambda_handler():
    result = lambda_handler(None, None)
    expected = {
        "statusCode": 200,
        "body": json.dumps("Health Checked!")
    }
    assert result == expected
