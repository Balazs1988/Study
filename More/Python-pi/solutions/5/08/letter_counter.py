"""
Module for letter counting
"""


def count_letter(text: str, letter: str) -> int:
    """
    Count a letter in a text.
    :param text: arbitrary string
    :param letter: the counted letter
    :return: count of the letter
    """
    count = 0
    for c in text:
        if c == letter:
            count += 1
    return count
