import pytest


@pytest.mark.parametrize("a,b,result", [(2, 2, 4), (2, -2, 0), (-2, -2, -4)])
def test_add_func(_calc, a, b, result):
    assert _calc.add(a, b) == result


def test_add_func_add_number_and_string_number(_calc):
    assert _calc.add(2, '2') == 4


def test_add_func_add_number_and_string_char(_calc):
    with pytest.raises(TypeError):
        _calc.add(2, 'a')


def test_add_floats(calc_link_call):
    assert calc_link_call.add(0.25, 0.75) == 1.0


def test_add_something(calc_link):
    assert calc_link.add(2, 3) == 5