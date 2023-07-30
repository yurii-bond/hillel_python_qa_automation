import pytest
from ..lecture_18.app import calc

@pytest.fixture
def _calc():
    return calc.Calculator()

# add tests
def test_add_func_zero_zero(_calc):
    assert _calc.add(0, 0) == 0

def test_add_two_positive_numbers(_calc):
    assert _calc.add(2, 2) == 4

def test_add_two_negative_numbers(_calc):
    assert _calc.add(-2, -2) == -4

def test_add_number_and_zero(_calc):
    assert _calc.add(0, 7) == 7

def test_add_func_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.add('a', 2)

    # division tests
def test_division_by_zero(_calc):
    with pytest.raises(ZeroDivisionError):
        _calc.div(5, 0)

def test_division_number_and_number(_calc):
    assert _calc.div(2, 2) == 1

def test_division_minus_number_and_number(_calc):
    assert _calc.div(-9, 3) == -3

def test_division_number_and_minus_number(_calc):
    assert _calc.div(9, -3) == -3

def test_division_zero_and_minus_number(_calc):
    assert _calc.div(0, -3) == 0

    # multiply tests

def test_mult_func_number_and_number(_calc):
    assert _calc.mult(2, 6) == 12

def test_mult_func_number_and_float(_calc):
    assert _calc.mult(2, 5.0) == 10

def test_mult_func_float_and_float(_calc):
    assert _calc.mult(2.1, 5.0) == 10.5

def test_mult_number_and_number_not_equal(_calc):
    assert _calc.mult(2.1, 5.0) != 150.5

# subtract tests
def test_subtract_number_and_number(_calc):
    assert _calc.subsctract(2, 5) == -3

def test_subtract_number_and_float_number(_calc):
    assert _calc.subsctract(2, 0.1) == 1.9

def test_subtract_zero_and_float_number(_calc):
    assert _calc.subsctract(0, 0.11) == -0.11

def test_subtract_number_and_number_not_equal(_calc):
    assert _calc.subsctract(2, 5) != 150

# power tests
def test_number_and_power_number(_calc):
    assert _calc.power(4, 2) == 16

def test_number_and_power_float_number(_calc):
    assert _calc.power(5, 2.5) == 55.90169943749474

def test_number_and_power_zero_number(_calc):
    assert _calc.power(5545454, 0) == 1

def test_number_and_power_number_not_equal(_calc):
    assert _calc.power(4, 2) != 13535346

# square_root tests
def test_square_root_number(_calc):
    assert _calc.square_root(4) == 2

def test_square_root_float_number(_calc):
    assert _calc.square_root(5) == 2.23606797749979

def test_square_root_zero_number(_calc):
    assert _calc.square_root(0) == 0

def test_square_root_number_not_equal(_calc):
    assert _calc.square_root(4) != 13535346
