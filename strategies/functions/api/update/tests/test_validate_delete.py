import sys

sys.path.insert(1, "../../../../test_env")

import pytest
from pydantic.error_wrappers import ValidationError
from ..app.app import UpdateInterface
from .input import TestSuiteA2, TestSuiteCombinatorial


def validation_error_interface(test_case):
    with pytest.raises(ValidationError):
        UpdateInterface.validate_delete(test_case)

def test_c14():
    test_case = TestSuiteA2.input_c14()
    res =  UpdateInterface.validate_delete(test_case)
    assert len(res["id"]) == 36

def test_c15():
    test_case = TestSuiteA2.input_c15()
    validation_error_interface(test_case)

def test_c16():
    test_case = TestSuiteA2.input_c16()
    validation_error_interface(test_case)

def test_c17():
    test_case = TestSuiteA2.input_c17()
    validation_error_interface(test_case)

def test_c18():
    test_case = TestSuiteA2.input_c18()
    validation_error_interface(test_case)    

def test_c19():
    test_case = TestSuiteA2.input_c19()
    res = UpdateInterface.validate_delete(test_case)
    assert isinstance(res["id"], str)

def test_c20():
    test_case = TestSuiteA2.input_c20()
    validation_error_interface(test_case)   

def test_c21():
    test_case = TestSuiteA2.input_c21()
    validation_error_interface(test_case)   

def test_c22():
    test_case = TestSuiteA2.input_c22()
    validation_error_interface(test_case)      

def test_c23():
    test_case = TestSuiteA2.input_c23()
    res = UpdateInterface.validate_delete(test_case)
    assert isinstance(res["deleted"], bool)

def test_c24():
    test_case = TestSuiteA2.input_c24()
    validation_error_interface(test_case) 

def test_c25():
    test_case = TestSuiteA2.input_c25()
    validation_error_interface(test_case) 

def test_c26():
    test_case = TestSuiteA2.input_c26()
    validation_error_interface(test_case) 


def test_tc02():
    test_case = TestSuiteCombinatorial.input_tc02()
    res =  UpdateInterface.validate_delete(test_case)
    assert len(res["id"]) == 36
    assert isinstance(res["deleted"], bool)

def test_tc06():
  test_case = TestSuiteCombinatorial.input_tc06()
  validation_error_interface(test_case)

def test_tc07():
  test_case = TestSuiteCombinatorial.input_tc07()
  validation_error_interface(test_case)

def test_tc08():
  test_case = TestSuiteCombinatorial.input_tc08()
  validation_error_interface(test_case)