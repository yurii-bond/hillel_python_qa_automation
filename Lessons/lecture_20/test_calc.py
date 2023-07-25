import pytest


from ..lecture_18.app import calc


@pytest.fixture
def _calc():
    print('SetUp Activities')
    return calc.Calculator()


@pytest.mark.parametrize("a,b,result", [(2,2,4), (2,-2,0), (-2,-2,-4)])
@pytest.mark.add_function
def test_add_func(_calc, a, b, result):
    assert _calc.add(a, b) == result


@pytest.mark.skipif
@pytest.mark.add_function
def test_add_two_negative_numbers(_calc):
    assert _calc.add(-2, -2) == -4


@pytest.mark.division
def test_division_by_zero(_calc):
    with pytest.raises(ZeroDivisionError):
        _calc.div(3, 0)

def test_mult_two_positive_numbers(_calc):
    assert _calc.mult(2, 2) == 4

def test_mult_two_negative_numbers(_calc):
    assert _calc.mult(-2, -2) == 4

def test_mult_number_and_zero(_calc):
    assert _calc.mult(2, 0) == 0

def test_mult_positive_and_negative_numbers(_calc):
    assert _calc.mult(2, -2) == -4

def test_div_two_positive_numbers(_calc):
    assert _calc.div(2, 2) == 1

def test_div_two_negative_numbers(_calc):
    assert _calc.div(-2, -2) == 1

def test_div_number_and_zero(_calc):
    assert _calc.div(0, 2) == 0

def test_div_positive_and_negative_numbers(_calc):
    assert _calc.div(2, -2) == -1

def test_subsctract_two_positive_numbers(_calc):
    assert _calc.subsctract(2, 2) == 0

def test_subsctract_two_negative_numbers(_calc):
    assert _calc.subsctract(-2, -2) == 0

def test_subsctract_number_and_zero(_calc):
    assert _calc.subsctract(0, 2) == -2

def test_subsctract_positive_and_negative_numbers(_calc):
    assert _calc.subsctract(2, -2) == 4

def test_power_two_positive_numbers(_calc):
    assert _calc.power(2, 2) == 4

def test_power_two_negative_numbers(_calc):
    assert _calc.power(-2, -2) == 0.25

def test_power_number_and_zero(_calc):
    assert _calc.power(2, 0) == 1

def test_power_positive_and_negative_numbers(_calc):
    assert _calc.power(-2, 2) == 4

def test_square_root_with_positive_number(_calc):
    assert _calc.square_root(4) == 2

def test_square_root_with_zero(_calc):
    assert _calc.square_root(0) == 0

def test_square_root_with_float_numbers(_calc):
    assert _calc.square_root(4.84) == 2.2

def test_square_root_with_negative_number(_calc):
    with pytest.raises(ValueError):
        _calc.square_root(-4)