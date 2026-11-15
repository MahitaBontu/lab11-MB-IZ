import unittest
import calculator
from calculator import logarithm, hypotenuse, square_root

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

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