

import pytest
from pydantic.error_wrappers import ValidationError
from ..app.app import lambda_handler
from .input import TestPayoff


def validation_error_interface(test_case):
    with pytest.raises(ValidationError):
        lambda_handler(test_case, "")


def test_valid_strategy():
    test_case = TestPayoff.input_valid_strategy()
    res = lambda_handler(test_case, "")
    assert res["statusCode"] == 200

def test_invalid_strategy():
    test_case = TestPayoff.input_invalid_strategy()
    res = lambda_handler(test_case, "")
    assert res["statusCode"] == 500

def test_no_type_strategy():
    test_case = TestPayoff.input_no_type_strategy()
    res = lambda_handler(test_case, "")
    assert res["statusCode"] == 500

