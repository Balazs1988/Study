"""
Word counting module
"""


def count_specific_words(words: tuple, is_first=False) -> int:
    """
    Count the words in a tuple which contains letter 'L'.
    :param words: tuple of string objects
    :param is_first: when True, then only the first letter matters
    :return: count of words
    """
    if words == ():
        raise ValueError('The tuple should not be empty!')
    count = 0
    for word in words:
        if is_first:
            if word.startswith('L'):
                count += 1
        elif 'L' in word:
            count += 1
    return count
