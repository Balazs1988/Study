"""
Test cases for letter counting
"""

import pytest

from letter_counter import count_letter


@pytest.mark.parametrize('text, letter, count', [
    ('', 'a', 0),
    ('a', 'a', 1),
    ('abcdef', 'c', 1),
    ('abbbbcd', 'b', 4),
    ('abbbbcd', 'f', 0),
    ('aaaaaaaa', 'a', 8)
])
def test_letter_counting(text, letter, count):
    assert count_letter(text, letter) == count
