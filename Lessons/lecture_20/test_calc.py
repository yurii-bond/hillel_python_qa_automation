import pytest

from ..lecture_18.app import calc


@pytest.fixture
def _calc():
    print('SetUp Activities')
    return calc.Calculator()


# add function
@pytest.mark.parametrize("a,b,result", [(2, 2, 4), (2, -2, 0), (-2, -2, -4)])
@pytest.mark.add_function
def test_add_func(_calc, a, b, result):
    assert _calc.add(a, b) == result


@pytest.mark.skipif
@pytest.mark.add_function
def test_add_two_negative_numbers(_calc):
    assert _calc.add(-2, -2) == -4


@pytest.mark.add_function
def test_add_int_positive_numbers(_calc):
    assert _calc.add(5, 5) == 10


@pytest.mark.add_function
def test_add_mixed_types(_calc):
    assert _calc.add(2, 4.5) == 6.5


@pytest.mark.add_function
def test_add_floats_numbers(_calc):
    assert _calc.add(4.5, 5.5) == 10


@pytest.mark.add_function
def test_add_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.add('a', 2)


# subtract tests

@pytest.mark.subtract
def test_subtract_integers(_calc):
    assert _calc.subsctract(8, 3) == 5


@pytest.mark.subtract
def test_subtract_floats(_calc):
    assert _calc.subsctract(5.5, 1.25) == 4.25


@pytest.mark.subtract
def test_subtract_mixed_types(_calc):
    assert _calc.subsctract(7, 1.5) == 5.5


@pytest.mark.subtract
def test_subtract_negative_int_numbers(_calc):
    assert _calc.subsctract(-10, -15) == 5


@pytest.mark.subtract
def test_subtract_negative_float_numbers(_calc):
    assert _calc.subsctract(-4.5, -3.5) == -1


@pytest.mark.subtract
def test_subtract_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.subsctract('T', 6)


# multiply tests
@pytest.mark.multiply
def test_multiply_int_numbers(_calc):
    assert _calc.mult(3, 5) == 15


@pytest.mark.multiply
def test_multiply_float_numbers(_calc):
    assert _calc.mult(10.5, 2.5) == 26.25


@pytest.mark.multiply
def test_multiply_mixed_numbers(_calc):
    assert _calc.mult(5, 1.5) == 7.5


@pytest.mark.multiply
def test_multiply_by_zero(_calc):
    assert _calc.mult(5, 0) == 0


@pytest.mark.multiply
def test_multiply_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.subsctract('test', 2)


# division tests
@pytest.mark.division
def test_division_by_zero(_calc):
    with pytest.raises(ZeroDivisionError):
        _calc.div(3, 0)


@pytest.mark.division
def test_div_integers(_calc):
    assert _calc.div(10, 2) == 5


@pytest.mark.division
def test_div_floats(_calc):
    assert _calc.div(7.5, 2.5) == 3


@pytest.mark.division
def test_div_mixed_types(_calc):
    assert _calc.div(9, 1.5) == 6


@pytest.mark.division
def test_division_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.subsctract('2', 2)


@pytest.mark.division
def test_div_negative_int_type(_calc):
    assert _calc.div(-30, -2) == 15


# power tests
@pytest.mark.power
def test_power_int_type(_calc):
    assert _calc.power(2, 3) == 8


@pytest.mark.power
def test_power_mixed_types(_calc):
    assert _calc.power(4, 5.5) == 2048


@pytest.mark.power
def test_power_by_zero(_calc):
    assert _calc.power(4, 0) == 1


@pytest.mark.power
def test_power_int_negative_nums(_calc):
    assert _calc.power(-2, -3) == -0.125


@pytest.mark.skipif
@pytest.mark.power
def test_power_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.subsctract('2', 2)


# square tests

@pytest.mark.square
def test_square_int_type(_calc):
    assert _calc.square_root(25) == 5


@pytest.mark.square
def test_square_float_type(_calc):
    assert _calc.square_root(9.0) == 3


@pytest.mark.square
def test_square_type_error(_calc):
    with pytest.raises(TypeError):
        _calc.square_root('9')


@pytest.mark.square
def test_square_value_error(_calc):
    with pytest.raises(ValueError):
        _calc.square_root(-25)
