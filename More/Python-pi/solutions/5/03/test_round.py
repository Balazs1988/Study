"""
Test cases for the builtin round function
"""

import pytest


@pytest.mark.parametrize('n', [
    -3, -2, -1, 0, 1, 2, 3
])
def test_integers(n):
    assert round(n) == n


def test_half_way_positive():
    assert round(30.5) == 30


def test_half_way_negative():
    assert round(-30.5) == -30


@pytest.mark.parametrize('n, rounded', [
    (1.1, 1),
    (-1.1, -1),
    (8.6, 9),
    (-8.6, -9)
])
def test_general_cases(n, rounded):
    assert round(n) == rounded
