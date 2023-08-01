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

    def test_mult_two_positive_numbers(self):
        self.assertEqual(_calc.mult(2, 2), 4)

    def test_mult_two_negative_numbers(self):
        self.assertEqual(_calc.mult(-2, -2), 4)

    def test_mult_number_and_zero(self):
        self.assertEqual(_calc.mult(2, 0), 0)

    def test_mult_positive_and_negative_numbers(self):
        self.assertEqual(_calc.mult(2, -2), -4)

    def test_div_two_positive_numbers(self):
        self.assertEqual(_calc.div(2, 2), 1)

    def test_div_two_negative_numbers(self):
        self.assertEqual(_calc.div(-2, -2), 1)

    def test_div_number_and_zero(self):
        self.assertEqual(_calc.div(0, 2), 0)

    def test_div_positive_and_negative_numbers(self):
        self.assertEqual(_calc.div(2, -2), -1)

    def test_subsctract_two_positive_numbers(self):
        self.assertEqual(_calc.subsctract(2, 2), 0)

    def test_subsctract_two_negative_numbers(self):
        self.assertEqual(_calc.subsctract(-2, -2), 0)

    def test_subsctract_number_and_zero(self):
        self.assertEqual(_calc.subsctract(0, 2), -2)

    def test_subsctract_positive_and_negative_numbers(self):
        self.assertEqual(_calc.subsctract(2, -2), 4)

    def test_power_two_positive_numbers(self):
        self.assertEqual(_calc.power(2, 2), 4)

    def test_power_two_negative_numbers(self):
        self.assertEqual(_calc.power(-2, -2), 0.25)

    def test_power_number_and_zero(self):
        self.assertEqual(_calc.power(2, 0), 1)

    def test_power_positive_and_negative_numbers(self):
        self.assertEqual(_calc.power(-2, 2), 4)

    def test_square_root_with_positive_number(self):
        self.assertEqual(_calc.square_root(4), 2)

    def test_square_root_with_zero(self):
        self.assertEqual(_calc.square_root(0), 0)

    def test_square_root_with_float_numbers(self):
        self.assertEqual(_calc.square_root(4.84), 2.2)

    def test_square_root_with_negative_number(self):
        with self.assertRaises(ValueError):
            _calc.square_root(-4)


if __name__ == '__main__':
    unittest.main()
