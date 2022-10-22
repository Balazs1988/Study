import longest_series


def test_longest_series_one():
    text = '?'
    assert longest_series.longest_series(text) == 1


def test_longest_series_zero():
    text = 'no question mark'
    assert longest_series.longest_series(text) == 0


def test_longest_series_two():
    text = '??'
    assert longest_series.longest_series(text) == 2


def test_longest_series_two_separated():
    text = '?two??'
    assert longest_series.longest_series(text) == 2


def test_longest_series_three_separated():
    text = '???three?one??two'
    assert longest_series.longest_series(text) == 3
