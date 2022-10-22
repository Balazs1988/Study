"""
Question mark finder
"""


def find_longest(text: str) -> int:
    """
    Find the longest series of '?' chars in a text.
    :param text: arbitrary string
    :return: count of '?' chars in the longest seria
    """
    s = ''
    for c in text:
        if c == '?':
            s += '?'
        else:
            s += ' '
    parts = s.split(' ')
    max_length = 0
    for part in parts:
        if len(part) > max_length:
            max_length = len(part)
    return max_length
