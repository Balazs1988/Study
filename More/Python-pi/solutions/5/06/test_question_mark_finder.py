"""
Test cases for question mark finding
"""

import pytest

from question_mark_finder import find_longest


def test_empty():
    assert find_longest('') == 0


def test_all_question_mark():
    assert find_longest('?' * 100) == 100


@pytest.mark.parametrize('text, length', [
    ('?? ???', 3),
    ('a?b????  ', 4),
    ('a bb ccc', 0)
])
def test_general_cases(text, length):
    assert find_longest(text) == length
