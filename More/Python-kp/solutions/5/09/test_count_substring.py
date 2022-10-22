import count_substring
import pytest


@pytest.fixture
def sample_string():
    return 'kuka'


def test_count_substring_one(sample_string):
    string2 = 'makuka'
    assert count_substring.count_substring(sample_string, string2) == 1


def test_count_substring_two(sample_string):
    string2 = 'makukakuka'
    assert count_substring.count_substring(sample_string, string2) == 2


def test_count_substring_zero(sample_string):
    string2 = 'ma'
    assert count_substring.count_substring(sample_string, string2) == 0
