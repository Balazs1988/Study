"""
Finder module
"""


def find_last(words: list, skip_first=0, need_cleaning=False) -> int:
    """
    Find the index of the last, non-empty string in a list.
    :param words: list of strings
    :param skip_first: skip the first some words
    :param need_cleaning: use the strip for cleaning
    :return: index of the last non-empty string
    """
    if not words:
        raise ValueError('Empty list not allowed!')
    if skip_first > len(words):
        raise ValueError('Too many skipped!')
    index = len(words) - 1
    while index > skip_first:
        if need_cleaning:
            if words[index].strip() != '':
                return index
        else:
            if words[index] != '':
                return index
        index -= 1
    if index < skip_first:
        raise ValueError('There is no non-empty word!')
    return index
