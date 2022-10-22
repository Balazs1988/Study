import counts_words


def test_counts_words_none():
    given_tuple = (1, 2, 'letter')
    assert counts_words.counts_words(given_tuple) == 0


def test_counts_words_one():
    given_tuple = (1, 2, 'letter', 'Letter')
    assert counts_words.counts_words(given_tuple) == 1


def test_counts_words_two():
    given_tuple = (1, 2, 'Letter', 'paLindrome')
    assert counts_words.counts_words(given_tuple) == 2


def test_counts_words_one_a():
    given_tuple = (1, 2, 'Letter', 'paLindrome')
    is_first = True
    assert counts_words.counts_words(given_tuple, is_first) == 1


def test_counts_words_empty():
    given_tuple = ()
    assert counts_words.counts_words(given_tuple) == 0
