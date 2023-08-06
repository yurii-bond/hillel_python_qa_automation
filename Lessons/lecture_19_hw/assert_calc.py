import unittest
from parameterized import parameterized


from ..lecture_18_hw.app import calc

# _calc = calc.Calculator()


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('TearDownClass')

    def setUp(self) -> None:
        print('setup')
        self._calc = calc.Calculator()
        print(id(self._calc))

    def tearDown(self) -> None:
        print('tearDown')
        del self._calc

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
        # time.sleep(5)
        print('test_add_func')
        self.assertEqual(result, self._calc.add(a, b))

    def test_add_two_positive_numbers(self):
        # time.sleep(5)
        self.assertEqual(self._calc.add(2, 2), 4)

    def test_add_two_negative_numbers(self):
        # time.sleep(5)
        self.assertEqual(self._calc.add(-2, -2), -4)

    def test_add_number_and_zero(self):
        self.assertEqual(self._calc.add(2, 0), 2)

    def test_add_func_type_error(self):
        with self.assertRaises(TypeError):
            self._calc.add('a', '2')

    def test_devision_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self._calc.div(4, 0)


if __name__ == '__main__':
    unittest.main()
