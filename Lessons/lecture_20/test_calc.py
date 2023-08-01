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



 #test_subsctact

@pytest.mark.substract
@pytest.mark.parametrize("a,b,result", [(5, 8, -3), (5, -2, 7), (-2, -10, --8)])
def test_substract_func(_calc, a, b, result):
    assert _calc.subsctract(a, b) == result

@pytest.mark.substract
def test_subsctract_zero_and_numbers(_calc):
    assert _calc.subsctract(0, 10) == -10

@pytest.mark.substract
def test_subsctract_number_and_float(_calc):
    assert _calc.subsctract(20, 15.5) == 4.5


  #test_div
@pytest.mark.devision
def test_devision_by_float(_calc):
    assert _calc.div(5, 3.5) == 1.4285714285714286

@pytest.mark.devision
def test_devision_by_big_number(_calc):
    assert _calc.div(2, 1545) == 0.0012944983818770227

@pytest.mark.devision
def test_devision_by_str(_calc):
    with pytest.raises(TypeError):
            _calc.div(4, "i")

@pytest.mark.devision
def test_devision_by_minus_number(_calc):
    assert _calc.div(-352, 5) == -70.4


   #test_power

@pytest.mark.power
def test_power_positive_number(_calc):
    assert _calc.power(5, 2) == 25

@pytest.mark.power
def test_power_negative_number(_calc):
    assert _calc.power(5, -2) == 0.04

@pytest.mark.power
def test_power_by_zero(_calc):
    assert _calc.power(5, 0) == 1

@pytest.mark.power
def test_power_big_number(_calc):
     with pytest.raises(OverflowError):
        _calc.power(5, 200000)


   #testmult

@pytest.mark.mult
@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    [
        (4757575, 425454500, 2024131692837500),
       pytest.param(-2, 5, -10, marks=pytest.mark.skipif(sys.platform.startswith("win"), reason="The tests should be executed on Windows")),
       pytest.param(0, 2, 0, marks=pytest.mark.skip("is not case")),
        (-53, 0.5, -26.5),
       pytest.param('q', 2, 'error', marks=pytest.mark.xfail(run=False))
    ]
)
def test_mult(_calc, a, b, result):
    assert _calc.mult(a, b) == result


    #test_square_root
@pytest.mark.square_root
def test_square_root_positive_number(_calc):
    assert _calc.square_root(9) == 3

@pytest.mark.square_root
def test_square_root_zero(_calc):
    assert _calc.square_root(0) == 0

@pytest.mark.square_root
@pytest.mark.parametrize(
    ("a", "result"),
    [(14780004343, 121573.04118512459),
    pytest.param(-5, "error", marks=pytest.mark.xfail(raises=ValueError))
     ]
)
def test_square_root_with_error_big_numbers(_calc, a, result):
     assert _calc.square_root(a) == result




