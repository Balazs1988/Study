import count_letter
import pytest


@pytest.fixture
def sample_text():
    return 'anything'


def test_count_letters_y(sample_text):
    char = 'y'
    assert count_letter.count_letter(sample_text, char) == 1


def test_count_letters_n(sample_text):
    char = 'n'
    assert count_letter.count_letter(sample_text, char) == 2
