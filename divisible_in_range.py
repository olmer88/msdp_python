def divisible_in_range_lambda(start, end):
    return list(filter(lambda n: n % 7 == 0 and n % 5 != 0, range(start, end + 1)))


def divisible_in_range(start, end):
    return [n for n in range(start, end + 1) if n % 7 == 0 and n % 5 != 0]


def test_divisible_in_range():
    assert divisible_in_range(0, 0) == []
    assert divisible_in_range(0, 7) == [7]
    assert divisible_in_range(0, 35) == [7, 14, 21, 28]
    assert divisible_in_range(0, 77) == [7, 14, 21, 28, 42, 49, 56, 63, 77]


def test_divisible_in_range_lambda():
    assert divisible_in_range(0, 77) == [7, 14, 21, 28, 42, 49, 56, 63, 77]
