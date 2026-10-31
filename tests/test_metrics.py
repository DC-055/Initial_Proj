from example_package_DC_055.example import return_greater

def test_return_bigger_n1():
    assert return_greater(95, 76) == 95


def test_return_bigger_n2():
    assert return_greater(95, 176) == 176


def test_return_bigger_draw():
    assert return_greater(15, 15) == 15
