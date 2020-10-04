def divide_nums(num, devider):
    try:
        return num / devider
    except ZeroDivisionError:
        print('You cannot divide by 0')
        return None


def test_divide_nums():
    assert divide_nums(1, 1) == 1
    assert divide_nums(50, 10) == 5
    assert divide_nums(3, 2) == 1.5
    assert divide_nums(1, 0) is None
