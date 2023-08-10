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

    # mult tests


def test_mult_int_float_num(_calc):
    assert _calc.mult(3, 15.5) == 46.5


def test_mult_both_positive(_calc):
    assert _calc.mult(5, 3) == 15


def test_mult_both_negative(_calc):
    assert _calc.mult(-4, -15) == 60


def test_mult_both_flot(_calc):
    assert _calc.mult(1.5, 15.5) == 23.25

    # division tests


def test_division_int_by_float(_calc):
    assert _calc.div(10.4, 2) == 5.2


def test_division_float_by_int(_calc):
    assert _calc.div(15.6, 2) == 7.8


def test_division_both_positive(_calc):
    assert _calc.div(10, 2) == 5


def test_division_both_negative(_calc):
    assert _calc.div(-50, -2) == 25


# subtract tests
def test_subtract_number_and_number(_calc):
    assert _calc.subsctract(5, 15) == -10


def test_subtract_number_and_float_number(_calc):
    assert _calc.subsctract(5, 0.5) == 4.5


def test_subtract_zero_and_float_number(_calc):
    assert _calc.subsctract(0, 0.5) == -0.5


def test_subtract_two_float_number(_calc):
    assert _calc.subsctract(55.6, 0.5) == 55.1


# power tests
def test_power_both_positive(_calc):
    assert _calc.power(3, 2) == 9


def test_power_both_negative(_calc):
    assert _calc.power(-2, -3) == -0.125


def test_power_float_int_num(_calc):
    assert _calc.power(3.5, 2) == 12.25


def test_power_int_by_zerol(_calc):
    assert _calc.power(50, 0) == 1


# square_root tests
def test_square_int(_calc):
    assert _calc.square_root(36) == 6


def test_square_float(_calc):
    assert _calc.square_root(9.0) == 3


def test_square_root_zero_number(_calc):
    assert _calc.square_root(0) == 0


def test_square_root_number_not_equal(_calc):
    assert _calc.square_root(5) != 477866777
