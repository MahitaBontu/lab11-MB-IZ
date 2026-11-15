import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError:
        raise ValueError

