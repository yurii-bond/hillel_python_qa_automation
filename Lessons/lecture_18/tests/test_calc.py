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

    # multiply tests

    @parameterized.expand([
        ('both_positive', 3, 5, 15),
        ('both_negative', -4, -15, 60)
    ])
    def test_multiply_positive_negative_numbers(self, name, a, b, expected_result):
        result = _calc.mult(a, b)
        self.assertEqual(result, expected_result)

    def test_multiplication_both_float_num(self):
        self.assertEqual(_calc.mult(1.5, 15.5), 23.25)

    def test_multiplication_int_float_num(self):
        self.assertEqual(_calc.mult(3, 15.5), 46.5)

    # division tests
    @parameterized.expand([
        ('both_positive', 10, 2, 5),
        ('both_negative', -50, -2, 25)
    ])
    def test_division_positive_negative_numbers(self, name, a, b, expected_result):
        result = _calc.div(a, b)
        self.assertEqual(result, expected_result)

    def test_division_int_by_float(self):
        self.assertEqual(_calc.div(10.4, 2), 5.2)

    def test_division_float_by_int(self):
        self.assertEqual(_calc.div(15.6, 2), 7.8)

    # subtract tests
    def test_subtract_number_and_number(self):
        self.assertEqual(_calc.subsctract(5, 15), -10)

    def test_subtract_number_and_float_number(self):
        self.assertEqual(_calc.subsctract(5, 0.5), 4.5)

    def test_subtract_zero_and_float_number(self):
        self.assertEqual(_calc.subsctract(0, 0.5), -0.5)

    def test_subtract_two_float_number(self):
        self.assertEqual(_calc.subsctract(55.6, 0.5), 55.1)

    # power tests
    @parameterized.expand([
        ('both_positive', 3, 2, 9),
        ('both_negative', -2, -3, -0.125)
    ])
    def test_division_positive_negative_numbers(self, name, a, b, expected_result):
        result = _calc.power(a, b)
        self.assertEqual(result, expected_result)

    def test_float_power_int_num(self):
        self.assertEqual(_calc.power(3.5, 2), 12.25)

    def test_int_power_by_zero(self):
        self.assertEqual(_calc.power(50, 0), 1)

    # square tests

    def test_square_int(self):
        self.assertEqual(_calc.square_root(36), 6)

    def test_square_float(self):
        self.assertEqual(_calc.square_root(9.0), 3)

    def test_square_root_zero_number(self):
        self.assertEqual(_calc.square_root(0), 0)

    def test_square_root_number_not_equal(self):
        self.assertNotEqual(_calc.square_root(5), 477866777)

if __name__ == '__main__':
    unittest.main()
