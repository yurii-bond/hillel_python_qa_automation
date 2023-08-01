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

    # division tests
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _calc.div(4, 0)

    def test_division_number_and_number(self):
        self.assertEqual(_calc.div(2, 2), 1)

    def test_division_minus_number_and_number(self):
        self.assertEqual(_calc.div(-9, 3), -3)

    def test_division_number_and_minus_number(self):
        self.assertEqual(_calc.div(9, -3), -3)

    def test_division_zero_and_minus_number(self):
        self.assertEqual(_calc.div(0, -3), 0)

    # multiply tests
    def test_mult_func_number_and_float(self):
        self.assertEqual(_calc.mult(2, 5.0), 10)

    def test_mult_func_float_and_float(self):
        self.assertEqual(_calc.mult(2.1, 5.0), 10.5)

    def test_mult_number_and_number_not_equal(self):
        self.assertNotEqual(_calc.mult(2.1, 5.0), 150.5)

    @parameterized.expand([
        ('minus', -5, 5, -25),
        ('zero', 0, 140, 0)
    ])
    def test_mult(self, name, a, b, expected_result):
        result = _calc.mult(a, b)
        self.assertEqual(result, expected_result)

    # subtract tests
    def test_subtract_number_and_number(self):
        self.assertEqual(_calc.subsctract(2, 5), -3)

    def test_subtract_number_and_float_number(self):
        self.assertEqual(_calc.subsctract(2, 0.1), 1.9)

    def test_subtract_zero_and_float_number(self):
        self.assertEqual(_calc.subsctract(0, 0.11), -0.11)

    def test_subtract_number_and_number_not_equal(self):
        self.assertNotEqual(_calc.subsctract(2, 5), 150.5)

    # power tests
    def test_number_and_power_number(self):
        self.assertEqual(_calc.power(4, 2), 16)

    def test_number_and_power_float_number(self):
        self.assertEqual(_calc.power(5, 2.5), 55.90169943749474)

    def test_number_and_power_zero_number(self):
        self.assertEqual(_calc.power(5545454, 0), 1)

    def test_number_and_power_number_not_equal(self):
        self.assertNotEqual(_calc.power(4, 2), 13535346)

    # square_root tests
    def test_square_root_number(self):
        self.assertEqual(_calc.square_root(4), 2)

    def test_square_root_float_number(self):
        self.assertEqual(_calc.square_root(5), 2.23606797749979)

    def test_square_root_zero_number(self):
        self.assertEqual(_calc.square_root(0), 0)

    def test_square_root_number_not_equal(self):
        self.assertNotEqual(_calc.square_root(4), 13535346)

    @parameterized.expand([
        (-8,),
        (-91,),
    ])
    def test_square_root_negative_minus_number(self, x):
        with self.assertRaises(ValueError):
            _calc.square_root(x)


if __name__ == '__main__':
    unittest.main()
