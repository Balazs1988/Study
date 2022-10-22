"""
Substring counter module
"""


def count_substrings(text: str, pattern: str) -> int:
    """
    Count the occurrences of a substring in a text.
    :param text: arbitrary string
    :param pattern: a substring which should be counted
    :return: count of the occurrences of the substring
    """
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        s = text[i:i + len(pattern)]
        if s == pattern:
            count += 1
    return count
