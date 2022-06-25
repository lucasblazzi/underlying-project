import sys

sys.path.insert(1, "../../../../test_env")

import pytest
from pydantic.error_wrappers import ValidationError
from ..app.app import validate_option_input
from .input import TestSuiteA1, TestSuiteCombinatorial


def validation_error_interface(test_case):
    with pytest.raises(ValidationError):
        validate_option_input(test_case)


def test_c1():
    test_case = TestSuiteA1.input_c1()
    res = validate_option_input(test_case)
    assert len(res["name"]) == 5


def test_c2():
    test_case = TestSuiteA1.input_c2()
    res = validate_option_input(test_case)
    assert len(res["name"]) == 8


def test_c3():
    test_case = TestSuiteA1.input_c3()
    validation_error_interface(test_case)


def test_c4():
    test_case = TestSuiteA1.input_c4()
    validation_error_interface(test_case)


def test_c5():
    test_case = TestSuiteA1.input_c5()
    validation_error_interface(test_case)


def test_c6():
    test_case = TestSuiteA1.input_c6()
    res = validate_option_input(test_case)
    assert isinstance(res["name"], str)


def test_c7():
    test_case = TestSuiteA1.input_c7()
    validation_error_interface(test_case)


def test_c8():
    test_case = TestSuiteA1.input_c8()
    validation_error_interface(test_case)

def test_c9():
    test_case = TestSuiteA1.input_c9()
    res = validate_option_input(test_case)
    assert len(res["id"]) == 32

def test_c10():
    test_case = TestSuiteA1.input_c10()
    validation_error_interface(test_case)

def test_c11():
    test_case = TestSuiteA1.input_c11()
    validation_error_interface(test_case)

def test_c12():
    test_case = TestSuiteA1.input_c12()
    res = validate_option_input(test_case)
    assert isinstance(res["id"], str)


def test_c13():
    test_case = TestSuiteA1.input_c13()
    validation_error_interface(test_case)


def test_c14():
    test_case = TestSuiteA1.input_c14()
    validation_error_interface(test_case)

def test_ct1():
    test_case = TestSuiteCombinatorial.input_ct1()
    res = validate_option_input(test_case)
    assert res == test_case

def test_ct2():
    test_case = TestSuiteCombinatorial.input_ct2()
    validation_error_interface(test_case)


def test_ct3():
    test_case = TestSuiteCombinatorial.input_ct3()
    validation_error_interface(test_case)


def test_ct4():
    test_case = TestSuiteCombinatorial.input_ct4()
    validation_error_interface(test_case)
