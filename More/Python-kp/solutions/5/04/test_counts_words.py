import counts_words


def test_count_words():
    words_list = ['one', 'one', 'two', 'three', 'two', 'one', 'four', 'four', 'five']
    assert counts_words.counts_words(words_list) == {'one': 3, 'two': 2, 'three': 1, 'four': 2, 'five': 1}


def test_count_words_empty():
    words_list = []
    assert counts_words.counts_words(words_list) == {}


def test_count_words_numbers():
    words_list = ['1', '1', '2', '3', '2', '1', '4', '4', '5']
    assert counts_words.counts_words(words_list) == {'1': 3, '2': 2, '3': 1, '4': 2, '5': 1}