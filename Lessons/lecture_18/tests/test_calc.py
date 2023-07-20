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


    #test_subsctact

    def test_subsctract_two_positive_numbers(self):
        self.assertEqual(_calc.subsctract(8, 3), 5)

    def test_subsctract_two_negative_numbers(self):
        self.assertEqual(_calc.subsctract(-10, -5), -5)

    def test_subsctract_one_negative_numbers(self):
        self.assertEqual(_calc.subsctract(-10, 5), -15)

    def test_subsctract_zero_and_numbers(self):
        self.assertEqual(_calc.subsctract(0, 10), -10)

    def test_subsctract_number_and_float(self):
        self.assertTrue(4.5, _calc.subsctract(20, 15.5))


  #test_div

    def test_devision_by_float(self):
        self.assertEqual(_calc.div(5, 3.5), 1.4285714285714286)

    def test_devision_by_big_number(self):
        self.assertEqual(_calc.div(2, 1545), 0.0012944983818770227)

    def test_devision_by_str(self):
        with self.assertRaises(TypeError):
            _calc.div(4, "i")

    def test_devision_by_minus_number(self):
        self.assertEqual(_calc.div(-352, 5), -70.4)


   #test_power

    def test_power_positive_number(self):
        self.assertEqual(_calc.power(5, 2), 25)

    def test_power_negative_number(self):
        self.assertEqual(_calc.power(5, -2), 0.04)

    def test_power_by_zero(self):
        self.assertTrue(1, _calc.power(5, 0))

    def test_power_big_number(self):
        with self.assertRaises(OverflowError):
            _calc.power(5, 200000)

   #testmult
    def test_mult_positive_big_number(self):
        self.assertEqual(_calc.mult(255500, 45555), 11639302500)

    def test_mult_by_zero(self):
        self.assertEqual(_calc.mult(0, 5), 0)

    def test_mult_mix(self):
        self.assertEqual(_calc.mult(-53, 0.5), -26,5)

    def test_mult_positive_number(self):
     self.assertIs(_calc.mult(2, 1), 2)




    #test_square_root

    def test_square_root_positive_number(self):
        self.assertEqual(_calc.square_root(9), 3)

    def test_square_root_zero(self):
        self.assertEqual(_calc.square_root(0), 0)

    def test_square_root_negative_number(self):
        with self.assertRaises(ValueError):
         _calc.square_root(-5)

    def test_square_root_big_number(self):
        self.assertEqual(_calc.square_root(14780004343), 121573.04118512459)


    def test_compare_two_dict(self):
        dict1 = {'a': {'b': 2, 'c': {'d': 4}}}
        dict2 = {'a': {'b': 2, 'c': {'d': 4}}}
        self.assertDictEqual(dict1, dict2)
    #знаю що ця перевірка не  підходить до  випадку з калькулятором але хотілося погратися з використанням різних asserts






















if __name__ == '__main__':
    unittest.main()
