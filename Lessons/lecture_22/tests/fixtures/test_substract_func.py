def test_subsctract_func(_calc):
    assert _calc.subsctract(4, 2) == 2


def test_subsctract_zero(calculator):
    assert calculator.subsctract(4, 0) == 4


def test_subsctract_bigger_number(_calculator):
    assert _calculator.subsctract(4, 6) == -2


def test_subsctract_bigger_number_from_zero(_calc_):
    assert _calc_.subsctract(0, 6) == -6


def test_subsctract_float_number_from_zero(_calc):
    assert _calc.subsctract(0, 0.6) == -0.6