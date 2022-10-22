"""
Test cases for substring counting
"""

import pytest

from substring_counter import count_substrings


@pytest.fixture
def sample_text():
    return 'Substring strtrtrtr sample str'


@pytest.mark.parametrize('pattern, count', [
    ('sample', 1),
    ('str', 3),
    ('missing', 0),
    (' ', 3),
    ('trtr', 3)
])
def test_count_substrings(sample_text, pattern, count):
    assert count_substrings(sample_text, pattern) == count
