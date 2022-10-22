"""
Test cases for the word counter
"""

from word_counter import count_occurrences


def test_empty_list():
    assert count_occurrences([]) == {}


def test_one_word():
    assert count_occurrences(['one']) == {'one': 1}


def test_two_words():
    assert count_occurrences(['one', 'one']) == {'one': 2}


def test_more_words():
    words = ['a', 'b', 'b', 'a', 'c']
    occurrences = {'a': 2, 'b': 2, 'c': 1}
    assert count_occurrences(words) == occurrences
