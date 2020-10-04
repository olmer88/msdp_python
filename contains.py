def contains_200(d):
    return 200 in list(d.values())


def test_contains_200():
    assert contains_200({"a": 100, "b": 200, "c": 300})
    assert not contains_200({})
    assert not contains_200({"a": 100})
    assert contains_200({"a": 200})
