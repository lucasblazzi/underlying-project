import sys

sys.path.insert(1, "../../../../test_env")

import pytest
from pydantic.error_wrappers import ValidationError
from ..app.app import validate_item
from .input import TestSuiteA1, TestSuiteA2, TestSuiteCombinatorial


def validation_error_interface(test_case):
    with pytest.raises(ValidationError):
        validate_item(test_case)


def test_c1():
    test_case = TestSuiteA1.input_c1()
    res = validate_item(test_case)
    assert len(res["name"]) == 3


def test_c2():
    test_case = TestSuiteA1.input_c2()
    res = validate_item(test_case)
    assert len(res["name"]) == 40


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
    res = validate_item(test_case)
    assert isinstance(res["name"], str)


def test_c7():
    test_case = TestSuiteA1.input_c7()
    validation_error_interface(test_case)


def test_c8():
    test_case = TestSuiteA1.input_c8()
    res = validate_item(test_case)
    assert isinstance(res["name"], str)


def test_c9():
    test_case = TestSuiteA1.input_c9()
    res = validate_item(test_case)
    assert len(res["strategy"]) == 1


def test_c10():
    test_case = TestSuiteA1.input_c10()
    res = validate_item(test_case)
    assert len(res["strategy"]) == 2


def test_c11():
    test_case = TestSuiteA1.input_c11()
    validation_error_interface(test_case)


def test_c12():
    test_case = TestSuiteA1.input_c12()
    res = validate_item(test_case)
    assert isinstance(res["strategy"], list)


def test_c13():
    test_case = TestSuiteA1.input_c13()
    validation_error_interface(test_case)


def test_c14():
    test_case = TestSuiteA1.input_c14()
    validation_error_interface(test_case)


def test_c15():
    test_case = TestSuiteA1.input_c15()
    res = validate_item(test_case)
    assert len(res["username"]) == 6


def test_c16():
    test_case = TestSuiteA1.input_c16()
    res = validate_item(test_case)
    assert len(res["username"]) == 20


def test_c17():
    test_case = TestSuiteA1.input_c17()
    validation_error_interface(test_case)


def test_c18():
    test_case = TestSuiteA1.input_c18()
    validation_error_interface(test_case)


def test_c19():
    test_case = TestSuiteA1.input_c19()
    validation_error_interface(test_case)


def test_c20():
    test_case = TestSuiteA1.input_c20()
    res = validate_item(test_case)
    assert isinstance(res["username"], str)


def test_c21():
    test_case = TestSuiteA1.input_c21()
    validation_error_interface(test_case)


def test_c22():
    test_case = TestSuiteA1.input_c22()
    validation_error_interface(test_case)


def test_c23():
    test_case = TestSuiteA2.input_c23()
    res = validate_item(test_case)
    assert len(res["strategy"][0]["name"]) == 3


def test_c24():
    test_case = TestSuiteA2.input_c24()
    res = validate_item(test_case)
    assert len(res["strategy"][0]["name"]) == 40


def test_c25():
    test_case = TestSuiteA2.input_c25()
    validation_error_interface(test_case)


def test_c26():
    test_case = TestSuiteA2.input_c26()
    validation_error_interface(test_case)


def test_c27():
    test_case = TestSuiteA2.input_c27()
    validation_error_interface(test_case)


def test_c28():
    test_case = TestSuiteA2.input_c28()
    res = validate_item(test_case)
    assert isinstance(res["strategy"][0]["name"], str)


def test_c29():
    test_case = TestSuiteA2.input_c29()
    validation_error_interface(test_case)


def test_c30():
    test_case = TestSuiteA2.input_c30()
    res = validate_item(test_case)
    assert isinstance(res["strategy"][0]["name"], str)


def test_c31():
    test_case = TestSuiteA2.input_c31()
    res = validate_item(test_case)
    assert isinstance(res["strategy"][0]["type"], str)


def test_c32():
    test_case = TestSuiteA2.input_c32()
    validation_error_interface(test_case)


def test_c33():
    test_case = TestSuiteA2.input_c33()
    validation_error_interface(test_case)


def test_c34():
    test_case = TestSuiteA2.input_c34()
    res = validate_item(test_case)
    assert res["strategy"][0]["type"] == "CALL"


def test_c35():
    test_case = TestSuiteA2.input_c35()
    res = validate_item(test_case)
    assert res["strategy"][0]["type"] == "PUT"


def test_c36():
    test_case = TestSuiteA2.input_c36()
    res = validate_item(test_case)
    assert res["strategy"][0]["type"] == "CALL"


def test_c37():
    test_case = TestSuiteA2.input_c37()
    validation_error_interface(test_case)


def test_c38():
    test_case = TestSuiteA2.input_c38()
    res = validate_item(test_case)
    assert isinstance(res["strategy"][0]["exercise_price"], float)


def test_c39():
    test_case = TestSuiteA2.input_c39()
    validation_error_interface(test_case)


def test_c40():
    test_case = TestSuiteA2.input_c40()
    validation_error_interface(test_case)


def test_c41():
    test_case = TestSuiteA2.input_c41()
    res = validate_item(test_case)
    assert res["strategy"][0]["exercise_price"] == 12.32


def test_c42():
    test_case = TestSuiteA2.input_c42()
    validation_error_interface(test_case)


def test_c43():
    test_case = TestSuiteA2.input_c43()
    validation_error_interface(test_case)


def test_c44():
    test_case = TestSuiteA2.input_c44()
    res = validate_item(test_case)
    assert isinstance(res["strategy"][0]["transaction_type"], str)


def test_c45():
    test_case = TestSuiteA2.input_c45()
    validation_error_interface(test_case)


def test_c46():
    test_case = TestSuiteA2.input_c46()
    validation_error_interface(test_case)


def test_c47():
    test_case = TestSuiteA2.input_c47()
    res = validate_item(test_case)
    assert res["strategy"][0]["transaction_type"] == "LONG"


def test_c48():
    test_case = TestSuiteA2.input_c48()
    res = validate_item(test_case)
    assert res["strategy"][0]["transaction_type"] == "SHORT"


def test_c49():
    test_case = TestSuiteA2.input_c49()
    res = validate_item(test_case)
    assert res["strategy"][0]["transaction_type"] == "SHORT"


def test_c50():
    test_case = TestSuiteA2.input_c50()
    validation_error_interface(test_case)


def test_c51():
    test_case = TestSuiteA2.input_c51()
    res = validate_item(test_case)
    assert isinstance(res["strategy"][0]["close_price"], float)


def test_c52():
    test_case = TestSuiteA2.input_c52()
    validation_error_interface(test_case)


def test_c53():
    test_case = TestSuiteA2.input_c53()
    validation_error_interface(test_case)


def test_c54():
    test_case = TestSuiteA2.input_c54()
    res = validate_item(test_case)
    assert res["strategy"][0]["close_price"] == 11.24


def test_c55():
    test_case = TestSuiteA2.input_c55()
    validation_error_interface(test_case)


def test_c56():
    test_case = TestSuiteA2.input_c56()
    validation_error_interface(test_case)


def test_c57():
    test_case = TestSuiteA2.input_c57()
    res = validate_item(test_case)
    assert isinstance(res["strategy"][0]["contracts"], int)


def test_c58():
    test_case = TestSuiteA2.input_c58()
    validation_error_interface(test_case)


def test_c59():
    test_case = TestSuiteA2.input_c59()
    validation_error_interface(test_case)


def test_c60():
    test_case = TestSuiteA2.input_c60()
    res = validate_item(test_case)
    assert res["strategy"][0]["contracts"] == 1


def test_c61():
    test_case = TestSuiteA2.input_c61()
    validation_error_interface(test_case)


def test_c62():
    test_case = TestSuiteA2.input_c62()
    res = validate_item(test_case)
    assert res["strategy"][0]["contracts"] == 80


def test_c63():
    test_case = TestSuiteA2.input_c63()
    validation_error_interface(test_case)


def test_ct1():
    test_case = TestSuiteCombinatorial.input_ct1()
    res = validate_item(test_case)
    res.pop("shared")
    res.pop("id")
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


def test_ct5():
    test_case = TestSuiteCombinatorial.input_ct5()
    validation_error_interface(test_case)


def test_ct6():
    test_case = TestSuiteCombinatorial.input_ct6()
    validation_error_interface(test_case)


def test_ct7():
    test_case = TestSuiteCombinatorial.input_ct7()
    validation_error_interface(test_case)


def test_ct8():
    test_case = TestSuiteCombinatorial.input_ct8()
    validation_error_interface(test_case)