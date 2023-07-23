import unittest
from parameterized import parameterized

from ..app import calc

_calc = calc.Calculator()


class TestCalculator(unittest.TestCase):
    # @parameterized.expand([
    #     ('positive', 2, 2, 4),
    #     ('negative', -2, -2, -4),
    #     ('add_zero', 2, 0, 2),
    #     ('bigger numbers', -100, 200, 100),
    #     ('float numbers', -5.0, 7.0, 2.0),
    #     ('mixed numbers', -5.0, 7, 2.0),
    #     ('mixed numbers', -5.0, 7.0, 2),
    #     ('check string cast', '2', '2', 4),
    #     ('check string cast', '2.0', '2', 4),
    #     ('check adding str + int', '2', 2, 4)
    # ])
    # def test_add_func(self, name, a, b, result):
    #     self.assertEqual(result, _calc.add(a, b))
    #
    # # def test_add_two_positive_numbers(self):
    #     self.assertEqual(_calc.add(2, 2), 4)
    #
    # def test_add_two_negative_numbers(self):
    #     self.assertEqual(_calc.add(-2, -2), -4)
    #
    # def test_add_number_and_zero(self):
    #     self.assertEqual(_calc.add(2, 0), 2)
    #
    # def test_add_func_type_error(self):
    #     with self.assertRaises(TypeError):
    #         _calc.add('a', '2')
    #
    # def test_devision_by_zero(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         _calc.div(4, 0)

# До існуючих тестів дописати по 4 тести на кожну з непокритих тестами функцію:
# mult
    @parameterized.expand([
        ('positive numbers', 4, 3, 12),
        ('one negative', -4, 3, -12),
        ('one_zero', 4, 0, 0),
        ('negative numbers', -4, -3, 12)
    ])
    def test_mult_two_digits(self, name, a, b, result):
        self.assertEqual(_calc.mult(a, b), result)

# division
    @parameterized.expand([
        ('positive numbers', 12, 3, 4),
        ('one negative', -12, 3, -4),
        ('negative numbers', -12, -3, 4)
    ])
    def test_div_two_positive_numbers(self, name, a, b, result):
        self.assertEqual(_calc.div(a, b), result)
    def test_div_func_type_error(self):
        with self.assertRaises(TypeError):
            _calc.div('12', 3)

# subtract
    @parameterized.expand([
        ('positive numbers', 4, 3, 1),
        ('negative numbers', -4, -3, -1),
        ('one negative', -4, 3, -7)
    ])
    def test_subtract_two_positive_numbers(self, name, a, b, result):
        self.assertEqual(_calc.subsctract(a, b), result)
    def test_subtract_func_type_error(self):
        with self.assertRaises(TypeError):
            _calc.subsctract('4', 3)

# power
    @parameterized.expand([
        ('positive numbers', 4, 3, 64),
        ('one negative', -4, 3, -64),
        ('pow zero', -4, 0, 1)
    ])
    def test_power_two_positive_numbers(self, name, a, b, result):
        self.assertEqual(_calc.power(a, b), result)
    def test_power_func_type_error(self):
        with self.assertRaises(TypeError):
            _calc.power('4', 3)

  # square_root
    @parameterized.expand([
        ('positive number', 16, 4),
        ('sqrt zero', 0, 0)
    ])
    def test_sqrt_positive_number(self, name, a, result):
        self.assertEqual(_calc.square_root(a), result)
    def test_sqrt_negative_number(self):
        with self.assertRaises(ValueError):
            _calc.square_root(-16)
    def test_sqrt_func_type_error(self):
        with self.assertRaises(TypeError):
            _calc.square_root('16', 4)

if __name__ == '__main__':
    unittest.main()
