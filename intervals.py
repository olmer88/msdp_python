def is_in_range(n):
    return -15 <= n <= 12 or 14 <= n <= 17 or 19 <= n


if __name__ == '__main__':
    print(is_in_range(int(input("Enter a number: "))))


def test_is_in_range():
    assert not is_in_range(-16)
    assert is_in_range(-15)
    assert is_in_range(3)
    assert is_in_range(12)
    assert not is_in_range(13)
    assert is_in_range(14)
    assert is_in_range(15)
    assert is_in_range(17)
    assert not is_in_range(18)
    assert is_in_range(19)
    assert is_in_range(1000000)
