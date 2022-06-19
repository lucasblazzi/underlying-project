import sys

sys.path.insert(1, "../../../../test_env")

import pytest
from pydantic.error_wrappers import ValidationError
from ..app.app import UpdateInterface
from .input import TestSuiteA1


def validation_error_interface(test_case):
    with pytest.raises(ValidationError):
        UpdateInterface.validate_share(test_case)


def test_c1():
    test_case = TestSuiteA1.input_c1()
    res = UpdateInterface.validate_share(test_case)
    assert isinstance(res["shared"], bool)


def test_c2():
    test_case = TestSuiteA1.input_c2()
    validation_error_interface(test_case)
