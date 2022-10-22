"""
Word counter module
"""


def count_occurrences(words: list) -> dict:
    """
    Count the occurrences of words in list of words.
    :param words: list of words
    :return: dictionary, with (word, count) pairs
    """
    occurrences = {}
    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1
    return occurrences
