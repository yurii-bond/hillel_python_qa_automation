import pytest
from parameterized import parameterized
from ..lecture_18.app import calc


@pytest.fixture
def _calc():
    return calc.Calculator()


def test_mult_two_positive_numbers(_calc):
    assert _calc.mult(4, 3) == 12


def test_mult_one_negative_numbers(_calc):
    assert _calc.mult(-4, 3) == -12


def test_mult_two_negative_numbers(_calc):
    assert _calc.mult(-4, -3) == 12


def test_mult_type_error(_calc):
    with pytest.raises(TypeError):
        _calc('4', 3)


def test_div_two_positive_numbers(_calc):
    assert _calc.div(12, 3) == 4


def test_div_one_negative_number(_calc):
    assert _calc.div(-12, 3) == -4


def test_div_two_negative_numbers(_calc):
    assert _calc.div(-12, -3) == 4


def test_div_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.div('12', 0)


def test_subtract_two_positive_numbers(_calc):
    assert _calc.subsctract(4, 3) == 1


def test_subtract_two_negative_numbers(_calc):
    assert _calc.subsctract(-4, -3) == -1


def test_subtract_one_negative_numbers(_calc):
    assert _calc.subsctract(-4, 3) == -7


def test_subtract_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.subsctract('12', 0)


def test_power_two_positive_numbers(_calc):
    assert _calc.power(4, 3) == 64


def test_power_one_negative_numbers(_calc):
    assert _calc.power(-4, 3) == -64


def test_power_zero(_calc):
    assert _calc.power(-4, 0) == 1


def test_power_func_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.power('4', 0)


def test_sqrt_positive_number(_calc):
    assert _calc.square_root(16) == 4


def test_sqrt_zero(_calc):
    assert _calc.square_root(0) == 0


def test_sqrt_negative_number(_calc):
    with pytest.raises(ValueError):
        _calc.square_root(-16)


def test_sqrt_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.square_root('16')
