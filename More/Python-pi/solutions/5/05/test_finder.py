"""
Test cases for the finder
"""

import pytest

from finder import find_last


def test_empty_list():
    with pytest.raises(ValueError) as exc_info:
        _ = find_last([])
    assert str(exc_info.value) == 'Empty list not allowed!'


def test_without_empty_string():
    assert find_last(['a', 'b', 'c']) == 2


def test_with_empty_string():
    assert find_last(['a', 'b', 'c', '', '', '']) == 2


def test_cleaning():
    assert find_last(['a', 'b', 'c', '', '   ', ''], need_cleaning=True) == 2


def test_skip_to_empty_list():
    with pytest.raises(ValueError) as exc_info:
        _ = find_last(['a', 'b', 'c'], skip_first=3)
    assert str(exc_info.value) == 'There is no non-empty word!'


def test_invalid_skip():
    with pytest.raises(ValueError) as exc_info:
        _ = find_last(['a', 'b', 'c'], skip_first=4)
    assert str(exc_info.value) == 'Too many skipped!'
