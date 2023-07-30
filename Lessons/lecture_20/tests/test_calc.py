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
    def test_mult(self):
        self.assertEqual(_calc.mult(2, 3), 6)

    def test_mult_negative(self):
        self.assertEqual(_calc.mult(-2, -3), 6)

    def test_mult_zero(self):
        self.assertEqual(_calc.mult(2, 0), 0)

    def test_mult_type(self):
        with self.assertRaises(TypeError):
            _calc.mult('a', '3')
    def test_division(self):
        self.assertEqual(_calc.div(6, 2), 3)
    def test_div_negative(self):
        self.assertEqual(_calc.div(-6, -2), 3)

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _calc.div(6, 0)
    def test_div_type(self):
        with self.assertRaises(TypeError):
            _calc.div('a', 3)

    def test_subtract(self):                        # subtract
        self.assertEqual(_calc.subsctract(6, 3), 3)

    def test_substract_negative(self):
        self.assertEqual(_calc.subsctract(-6, -3), -3)

    def test_substract_zero(self):
        self.assertEqual(_calc.subsctract(6, 0), 6)

    def test_substract_type(self):
        with self.assertRaises(TypeError):
            _calc.subsctract('a', 3)

    def test_power(self):                        # power
        self.assertEqual(_calc.power(2, 3), 8)

    def test_power_negative(self):
        self.assertEqual(_calc.power(-2, 2), 4)

    def test_power_zero(self):
        self.assertEqual(_calc.power(5, 0), 1)

    def test_power_type(self):
        with self.assertRaises(TypeError):
            _calc.power('a', 3)

    def test_square_root(self):
        self.assertAlmostEqual(_calc.square_root(16), 4)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            _calc.square_root(-16)

    def test_square_root_zero(self):
        self.assertEqual(_calc.square_root(0), 0)

    def test_square_root_type(self):
        with self.assertRaises(TypeError):
            _calc.square_root('a')

if __name__ == '__main__':
    unittest.main()
