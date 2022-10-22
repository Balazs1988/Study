import calc_factorial


def test_calc_one():
    number = 1
    assert calc_factorial.calc_factorial(number) == 1


def test_calc_two():
    number = 2
    assert calc_factorial.calc_factorial(number) == 2


def test_calc_three():
    number = 3
    assert calc_factorial.calc_factorial(number) == 6
