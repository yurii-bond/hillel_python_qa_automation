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

    def test_add_two_positive_numbers(self):
        self.assertEqual(_calc.add(2, 2), 4)

    def test_add_two_negative_numbers(self):
        self.assertEqual(_calc.add(-2, -2), -4)

    def test_add_number_and_zero(self):
        self.assertEqual(_calc.add(2, 0), 2)

    def test_add_func_type_error(self):
        with self.assertRaises(TypeError):
            _calc.add('a', '2')

    def test_devision_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _calc.div(4, 0)

    def test_mult_positive(self):
        self.assertEqual(_calc.mult(2, 2), 4)

    def test_mult_one_float_number(self):
        self.assertEqual(_calc.add(0.2, 2), 2.2)

    def test_mult_two_float_number(self):
        self.assertEqual(_calc.mult(0.1, 0.1), 0.010000000000000002)

    def test_mult_one_negative(self):
        self.assertEqual(_calc.mult(-3, 2), -6)

    def test_division_positive(self):
        self.assertEqual(_calc.div(6, 2), 3)

    def test_division_negative(self):
        self.assertEqual(_calc.div(6, -2), -3.0)

    def test_division_one_float(self):
        self.assertEqual(_calc.div(6.6, 2), 3.3)

    def test_division_two_floats(self):
        self.assertEqual(_calc.div(0.25, 0.4), 0.625)

    def test_subtract_positive(self):
        self.assertEqual(_calc.subsctract(10, 2), 8)

    def test_subtract_negative(self):
        self.assertEqual(_calc.subsctract(-5, -1), -4)

    def test_subtract_two_floats(self):
        self.assertEqual(_calc.subsctract(4.5, 2.6), 1.9)

    def test_subtract_negative_float(self):
        self.assertEqual(_calc.subsctract(-7.7, 8), -15.7)

    def test_power_positive(self):
        self.assertEqual(_calc.power(2, 4), 16)

    def test_power_one_float(self):
        self.assertEqual(_calc.power(2.1, 2), 4.41)

    def test_power_negative(self):
        self.assertEqual(_calc.power(-2.4, 4), 33.1776)

    def test_power_two_floats(self):
        self.assertEqual(_calc.power(0.2, 0.1), 0.8513399225207846)

    def test_square_root_positive(self):
        self.assertEqual(_calc.square_root(16), 4)

    def test_square_root_positive2(self):
        self.assertEqual(_calc.square_root(4), 2)

    def test_square_root(self):
        self.assertEqual(_calc.square_root(64), 8)

    def test_square_root_2(self):
        self.assertEqual(_calc.square_root(100), 10)


if __name__ == '__main__':
    unittest.main()


