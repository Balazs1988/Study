"""
Test cases for word counting
"""

import pytest

from word_counter import count_specific_words


def test_empty_tuple():
    with pytest.raises(ValueError) as exc_info:
        _ = count_specific_words(())
    assert str(exc_info.value) == 'The tuple should not be empty!'


def test_non_specific():
    words = ('non', 'specific', 'words')
    assert count_specific_words(words) == 0


def test_one_specific():
    words = ('There', 'is', 'an', 'L', 'letter')
    assert count_specific_words(words) == 1


def test_more_specific():
    words = ('There', 'are', 'L', 'Letter', 'and', 'ALL')
    assert count_specific_words(words) == 3


def test_only_first_letters():
    words = ('There', 'are', 'L', 'Letter', 'and', 'ALL')
    assert count_specific_words(words, is_first=True) == 2
