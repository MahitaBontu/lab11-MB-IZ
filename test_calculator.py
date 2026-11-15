
import unittest
import calculator
from calculator import logarithm, hypotenuse, square_root
from calculator import add, subtract, mul, div, exp


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-2, 10), -5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    ######## Partner 2

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        result = logarithm(10, 100)
        self.assertAlmostEqual(result, 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 5), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

    def test_exponent(self):
        self.assertEqual(exp(2, 3), 8)


if __name__ == '__main__':
    unittest.main()
