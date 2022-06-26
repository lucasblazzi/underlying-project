import sys

sys.path.insert(1, "../../../../test_env")

import pytest
from pydantic.error_wrappers import ValidationError
from ..app.app import UpdateInterface
from .input import TestSuiteA1,TestSuiteCombinatorial


def validation_error_interface(test_case):
    with pytest.raises(ValidationError):
        UpdateInterface.validate_share(test_case)
        ##validate_share(test_case)

def test_c1():
    test_case = TestSuiteA1.input_c1()
    res =  UpdateInterface.validate_share(test_case)
    assert len(res["id"]) == 36

def test_c2():
    test_case = TestSuiteA1.input_c2()
    validation_error_interface(test_case)

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
    res = UpdateInterface.validate_share(test_case)
    assert isinstance(res["id"], str)

def test_c7():
    test_case = TestSuiteA1.input_c7()
    validation_error_interface(test_case)   

def test_c8():
    test_case = TestSuiteA1.input_c8()
    validation_error_interface(test_case)   

def test_c9():
    test_case = TestSuiteA1.input_c9()
    validation_error_interface(test_case)      

def test_c10():
    test_case = TestSuiteA1.input_c10()
    res = UpdateInterface.validate_share(test_case)
    assert isinstance(res["shared"], bool)

def test_c11():
    test_case = TestSuiteA1.input_c11()
    validation_error_interface(test_case) 

def test_c12():
    test_case = TestSuiteA1.input_c12()
    validation_error_interface(test_case) 

def test_c13():
    test_case = TestSuiteA1.input_c13()
    validation_error_interface(test_case) 



def test_tc01():
    test_case = TestSuiteCombinatorial.input_tc01()
    res =  UpdateInterface.validate_share(test_case)
    assert len(res["id"]) == 36
    assert isinstance(res["shared"], bool)

def test_tc03():
  test_case = TestSuiteCombinatorial.input_tc03()
  validation_error_interface(test_case)

def test_tc04():
  test_case = TestSuiteCombinatorial.input_tc04()
  validation_error_interface(test_case)

def test_tc05():
  test_case = TestSuiteCombinatorial.input_tc05()
  validation_error_interface(test_case)
