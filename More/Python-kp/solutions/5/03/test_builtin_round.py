def test_round_down():
    value = 2.12
    assert round(value) == 2


def test_round_up():
    value = 2.51
    assert round(value) == 3


def test_round_none():
    value = 2
    assert round(value) == 2


def test_round_down_neg():
    value = -2.5
    assert round(value) == -2


def test_round_up_neg():
    value = -2.51
    assert round(value) == -3
