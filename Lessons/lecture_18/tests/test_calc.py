import unittest
from parameterized import parameterized

from ..app import calc

_calc = calc.Calculator()


class TestCalculator(unittest.TestCase):
    @parameterized.expand([
        ('positive', 2, 2, 4),
        ('negative', -2, -2, -4),
        ('add_zero', 2, 0, 2),
        ('bigger numbers', -100, 200, 100),
        ('float numbers', -5.0, 7.0, 2.0),
        ('mixed numbers', -5.0, 7, 2.0),
        ('mixed numbers', -5.0, 7.0, 2),
        ('check string cast', '2', '2', 4),
        ('check string cast', '2.0', '2', 4),
        ('check adding str + int', '2', 2, 4)
    ])
    def test_add_func(self, name, a, b, result):
        self.assertEqual(result, _calc.add(a, b))

    @parameterized.expand([
        ('mult_positive', 2, 3, 6),
        ('mult_negative', -2, 3, -6),
    ])
    def test_mult(self, name, a, b, result):
        self.assertEqual(result, _calc.mult(a, b))

    @parameterized.expand([
        ('division_positive', 6, 3, 2),
        ('division_negative', -6, 3, -2),
    ])
    def test_division(self, name, a, b, result):
        if isinstance(result, type):
            with self.assertRaises(result):
                _calc.div(a, b)
        else:
            self.assertEqual(result, _calc.div(a, b))

    @parameterized.expand([
        ('subtract_positive', 5, 3, 2),
        ('subtract_negative', 3, 5, -2),
    ])
    def test_subtract(self, name, a, b, result):
        self.assertEqual(result, _calc.subtract(a, b))

    @parameterized.expand([
        ('power_positive', 2, 3, 8),
        ('power_negative', 2, -3, 0.125),
    ])
    def test_power(self, name, a, b, result):
        self.assertEqual(result, _calc.power(a, b))

    @parameterized.expand([
        ('square_root_positive', 25, 5),
        ('square_root_float', 2.25, 1.5),
    ])
    def test_square_root(self, name, a, result):
        if isinstance(result, type):
            with self.assertRaises(result):
                _calc.square_root(a)
        else:
            self.assertEqual(result, _calc.square_root(a))


if __name__ == '__main__':
    unittest.main()
