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
