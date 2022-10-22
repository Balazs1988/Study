"""
Test cases for the strip method of string
"""

import pytest


@pytest.mark.parametrize('text, stripped', [
    ('', ''),
    ('   ', ''),
    ('abc', 'abc'),
    ('abc  ', 'abc'),
    ('  abc', 'abc'),
    ('  abc  ', 'abc'),
    ('  \t\tabc\n\t\t\n  ', 'abc')
])
def test_general_cases(text, stripped):
    assert text.strip() == stripped
