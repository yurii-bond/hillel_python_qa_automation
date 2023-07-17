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

    # substract tests
    def test_substract_int_first_more_int_second(self):
        self.assertEqual(_calc.subsctract(4, 2), 2)

    def test_substract_int_first_less_int_second(self):
        self.assertEqual(_calc.subsctract(0, 2), -2)

    def test_substract_float_first_more_float_second(self):
        self.assertEqual(_calc.subsctract(50.0, 25.5), 24.5)

    def test_substract_float_first_less_float_second(self):
        self.assertEqual(_calc.subsctract(10.2, 11.2), -1.0)

    def test_substract_negative_int_first_more_negative_int_second(self):
        self.assertEqual(_calc.subsctract(-10, -15), 5)

    def test_substract_negative_int_first_less_negative_int_second(self):
        self.assertEqual(_calc.subsctract(-12, -10), -2)

    # multiply tests

    @parameterized.expand([
        ('both_positive', 3, 5, 15),
        ('first_positive', 3, -10, -30),
        ('second_positive', -3, 10, -30),
        ('both_negative', -4, -15, 60)
    ])
    def test_multiply_positive_negative_numbers(self, name, a, b, expected_result):
        result = _calc.mult(a, b)
        self.assertEqual(result, expected_result)

    def test_multiplication_by_zero(self):
        self.assertEqual(_calc.mult(10, 0), 0)

    def test_multiplication_both_float_num(self):
        self.assertEqual(_calc.mult(12.5, 3.5), 43.75)

    def test_multiplication_int_float_num(self):
        self.assertEqual(_calc.mult(3, 12.5), 37.5)

    # division tests
    @parameterized.expand([
        ('both_positive', 10, 2, 5),
        ('first_positive', 3, -10, -0.3),
        ('second_positive', -10, 5, -2.0),
        ('both_negative', -60, -2, 30)
    ])
    def test_division_positive_negative_numbers(self, name, a, b, expected_result):
        result = _calc.div(a, b)
        self.assertEqual(result, expected_result)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _calc.div(10, 0)

    def test_division_int_by_float(self):
        self.assertEqual(_calc.div(12.4, 2), 6.2)

    def test_division_float_by_int(self):
        self.assertEqual(_calc.div(34.6, 2), 17.3)

    # power tests
    @parameterized.expand([
        ('both_positive', 3, 2, 9),
        ('first_positive', 3, -2, 0.1111111111111111),
        ('second_positive', -4, 2, 16),
        ('both_negative', -2, -3, -0.125)
    ])
    def test_division_positive_negative_numbers(self, name, a, b, expected_result):
        result = _calc.power(a, b)
        self.assertEqual(result, expected_result)

    def test_float_power_int_num(self):
        self.assertEqual(_calc.power(3.5, 2), 12.25)

    def test_int_power_float_num(self):
        self.assertEqual(_calc.power(4, 5.5), 2048.0)

    def test_int_power_by_zero(self):
        self.assertEqual(_calc.power(50, 0), 1)

    # square tests

    def test_square_int(self):
        self.assertEqual(_calc.square_root(25), 5)

    def test_square_float(self):
        self.assertEqual(_calc.square_root(9.0), 3)

    def test_square_str_num(self):
        with self.assertRaises(TypeError):
            _calc.square_root('16')

    def test_square_negative_num(self):
        with self.assertRaises(ValueError):
            _calc.square_root(-2)


if __name__ == '__main__':
    unittest.main()
