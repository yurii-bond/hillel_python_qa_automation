import pytest


def test_div_func(_calc):
    assert _calc.div(4, 2) == 2


def test_div_by_zero(_calc_):
    with pytest.raises(ZeroDivisionError):
        _calc_.div(4, 0)


def test_div_by_float(_calculator):
    assert _calculator.div(4, 0.5) == 8


def test_div_float_by_float(calculator):
    assert calculator.div(0.5, 0.5) == 1