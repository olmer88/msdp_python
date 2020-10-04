import argparse
from math import sqrt


def area(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def test_area():
    assert area(5, 4, 3) == 6.0
    assert round(area(1, 1, 1), 3) == 0.433
    assert round(area(5, 3, 3), 3) == 4.146


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def test_is_triangle():
    assert is_triangle(1, 1, 1)
    assert not is_triangle(1, 1, 2)  # because 1 + 1 not bigger then 2


def positive_number(value):
    try:
        int_value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("%s is not number" % value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError("%s is not positive number" % value)
    return int_value


parser = argparse.ArgumentParser(description='This script finds area of triangle')
parser.add_argument("a", help="first side length", type=positive_number)
parser.add_argument("b", help="second side length", type=positive_number)
parser.add_argument("c", help="third side length", type=positive_number)


if __name__ == '__main__':
    args = parser.parse_args()
    if not is_triangle(args.a, args.b, args.c):
        raise parser.error('This is not triangle. Any two sides of the triangle should be bigger then third side')
    print(area(args.a, args.b, args.c))
