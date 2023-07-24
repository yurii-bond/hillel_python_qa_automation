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
