import unittest
import calculator
from calculator import logarithm, hypotenuse, square_root

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertEqual(calculator.divide(-2, 10), -5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):  # Or ValueError depending on your implementation
            divide(10, 0)

    import math

    def test_logarithm(self):
        # Test valid logarithm calculation (e.g., log base 10 of 100 is 2, or natural log)
        result = logarithm(100, 10)  # Assuming arguments are (value, base)
        self.assertEqual(result, 2)

    def test_log_invalid_base(self):
        # Ensure invalid bases raise an exception (e.g., ValueError)
        with self.assertRaises(ValueError):
            logarithm(10, 1)  # Base 1 is invalid for logarithms

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 5), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)


# Do not touch this
if __name__ == "__main__":
    unittest.main()