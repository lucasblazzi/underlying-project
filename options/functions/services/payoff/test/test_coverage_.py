

import pytest
from pydantic.error_wrappers import ValidationError
from ..app.app import lambda_handler
from .input import TestPayoff


def validation_error_interface(test_case):
    with pytest.raises(Exception):
        lambda_handler(test_case, "")


# def test_strategy_true():
#     test_case = TestPayoff.input_strategy_true()
#     res = lambda_handler(test_case, "")
#     assert isinstance(res, list)

def test_strategy_false():
    test_case = TestPayoff.input_strategy_false()
    res = lambda_handler(test_case, "")
    assert isinstance(res, list)

def test_invalid_dict():
    test_case = TestPayoff.input_invalid_dict()
    validation_error_interface(test_case)
