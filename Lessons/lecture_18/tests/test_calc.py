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
        ('check adding str + int', '2', 2, 4),

        # test for fun mult
        ('mult_positive', 2, 3, 6),
        ('mult_negative', -2, 3, -6),
        ('mult_zero', 2, 0, 0),
        ('mult_float_numbers', -2.5, 4, -10.0),

        # test for  fun division
        ('division_positive', 6, 3, 2),
        ('division_negative', -6, 3, -2),
        ('division_by_zero', 4, 0, ZeroDivisionError),

        # test for fun subtract
        ('subtract_positive', 5, 3, 2),
        ('subtract_negative', 3, 5, -2),
        ('subtract_zero', 5, 0, 5),
        ('subtract_float_numbers', 5.5, 3.2, 2.3),

        # test for fun power
        ('power_positive', 2, 3, 8),
        ('power_negative', 2, -3, 0.125),
        ('power_zero', 5, 0, 1),
        # test for fun square_root
        ('square_root_positive', 25, 5),
        ('square_root_float', 2.25, 1.5),
        ('square_root_negative', -25, ValueError)
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


if __name__ == '__main__':
    unittest.main()
