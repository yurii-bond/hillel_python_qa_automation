import pytest
# pytestmark = [
#     pytest.mark.add_function,
#     pytest.mark.division
# ]

import sys

from ..lecture_18.app import calc


@pytest.fixture
def _calc():
    print('SetUp Activities')
    return calc.Calculator()


@pytest.mark.parametrize("a,b,result", [(2, 2, 4), (2, -2, 0), (-2, -2, -4)])
@pytest.mark.regression
@pytest.mark.add_function
@pytest.mark.smoke
def test_add_func(_calc, a, b, result):
    assert _calc.add(a, b) == result


@pytest.mark.skip(reason="Skipped due to incompleteness")
@pytest.mark.regression
@pytest.mark.add_function
def test_add_two_negative_numbers(_calc):
    assert _calc.add(-2, -2) == -4


@pytest.mark.division
@pytest.mark.regression
def test_division_by_zero(_calc):
    with pytest.raises(ZeroDivisionError):
        _calc.div(3, 0)


@pytest.mark.division
@pytest.mark.regression
@pytest.mark.xfail
def test_division_by_zero_xfail(_calc):
    assert _calc.div(3, 1) == 3


@pytest.mark.square_root
@pytest.mark.regression
@pytest.mark.skipif(sys.platform == 'linux', reason="Skip this test on Linux OS")
def test_sqare_root(_calc):
    print(sys.platform)
    assert _calc.square_root(4) == 2


@pytest.mark.square_root
@pytest.mark.regression
@pytest.mark.smoke
def test_sqare_root_for_four(_calc):
    print(sys.platform)
    assert _calc.square_root(4) == 2


@pytest.mark.square_root
@pytest.mark.regression
@pytest.mark.skipif(sys.platform != 'linux', reason="Skip this test if not Linux OS")
def test_sqare_root_for_sixteen(_calc):
    print(sys.platform)
    assert _calc.square_root(16) == 4


@pytest.mark.smoke
@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    [
        (2, 2, 0),
        pytest.param(11, 10, 1, marks=pytest.mark.skipif(sys.platform == 'linux',
                                                         reason="The tests shouldn't be executed on linux")),
        pytest.param(10, 9, 1, marks=pytest.mark.skip("Skipped just because")),
        (0, 2, -2),
        pytest.param('a', 5, 'error', marks=pytest.mark.xfail(run=False)),
        pytest.param('a', 5, 'error', marks=pytest.mark.xfail(reason="some bug: JIRA-1234")),
        pytest.param('a', 5, 'error', marks=pytest.mark.xfail(reason="some bug: JIRA-1234"))

    ]
)
def test_substract(_calc, a, b, result):
    assert _calc.subsctract(a, b) == result


def test_add_func(_calc):
    assert _calc.add(5, 5) == 10


def test_add_two_positive_numbers(_calc):
    assert _calc.add(2, 2) == 4


def test_add_two_negative_numbers(_calc):
    assert _calc.add(-2, -2) == -4


def test_add_number_and_zero(_calc):
    assert _calc.add(2, 0) == 2


def test_mult_positive(_calc):
    assert _calc.mult(2, 2) == 4


def test_mult_one_float_number(_calc):
    assert _calc.add(0.2, 2) == 2.2


def test_mult_two_float_number(_calc):
    assert _calc.mult(0.1, 0.1) == 0.010000000000000002


def test_mult_one_negative(_calc):
    assert _calc.mult(-3, 2) == -6


def test_division_positive(_calc):
    assert _calc.div(6, 2) == 3


def test_division_negative(_calc):
    assert _calc.div(6, -2) == -3.0


def test_division_one_float(_calc):
    assert _calc.div(6.6, 2) == 3.3


def test_division_two_floats(_calc):
    assert _calc.div(0.25, 0.4) == 0.625


# @pytest.mark.parametrize("a,b,result", [(10, 2, 8), (-5, -1, -4), (4.5, 2.6, 1.9), (-7.7, 8, -15.7)])
# def test_subtract_positive(_calc, a, b, result):
#     assert _calc.subsctract(a, b) == result         # as an option


def test_subtract_negative(_calc):
    assert _calc.subsctract(-5, -1) == -4

def test_subtract_two_floats(_calc):
    assert _calc.subsctract(4.5, 2.6) == 1.9

def test_subtract_negative_float(_calc):
    assert _calc.subsctract(-7.7, 8) == -15.7

def test_power_positive(_calc):
    assert _calc.power(2, 4) == 16


def test_power_one_float(_calc):
    assert _calc.power(2.1, 2) == 4.41


def test_power_negative(_calc):
    assert _calc.power(-2.4, 4) == 33.1776


def test_power_two_floats(_calc):
    assert _calc.power(0.2, 0.1) == 0.8513399225207846


def test_square_root_positive(_calc):
    assert _calc.square_root(16) == 4


def test_square_root_positive2(_calc):
    assert _calc.square_root(4) == 2


def test_square_root(_calc):
    assert _calc.square_root(64) == 8


def test_square_root_2(_calc):
    assert _calc.square_root(100) == 10
