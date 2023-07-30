import pytest
from ..app import calc

_calc = calc.Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (-2, -2, -4),
    (2, 0, 2),
    (-100, 200, 100),
    (-5.0, 7.0, 2.0),
    (-5.0, 7, 2.0),
    (-5.0, 7.0, 2),
    ('2', '2', 4),
    ('2.0', '2', 4),
    ('2', 2, 4),
])
def test_add(a, b, expected):
    assert _calc.add(a, b) == expected

# Test multiplication
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, -3, 6),
    (2, 0, 0),
])
def test_mult(a, b, expected):
    assert _calc.mult(a, b) == expected

# Test division
@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (-6, -2, 3),
])
def test_division(a, b, expected):
    assert _calc.div(a, b) == expected

# Test division by zero
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        _calc.div(4, 0)

# Test power
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (-2, 2, 4),
    (5, 0, 1),
])
def test_power(a, b, expected):
    assert _calc.power(a, b) == expected

# Test square root
@pytest.mark.parametrize("a, expected", [
    (16, 4),
    (0, 0),
])
def test_square_root(a, expected):
    assert _calc.square_root(a) == expected

# Test square root of a negative number
def test_square_root_of_negative():
    with pytest.raises(ValueError):
        _calc.square_root(-16)

# Test invalid inputs
@pytest.mark.parametrize("a, b", [
    ('a', 2),
    (2, 'b'),
    ('a', 'b'),
])
def test_invalid_input(a, b):
    with pytest.raises(TypeError):
        _calc.add(a, b)
        _calc.subtract(a, b)
        _calc.mult(a, b)
        _calc.div(a, b)
        _calc.power(a, b)

if __name__ == '__main__':
    pytest.main()
