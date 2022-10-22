"""
Test cases for the factorial function
"""

import pytest

from factorial import calc_factorial


@pytest.mark.parametrize('n, result', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24)
])
def test_valid_factorials(n, result):
    assert calc_factorial(n) == result
