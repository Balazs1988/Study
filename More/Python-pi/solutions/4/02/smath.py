def calc_square_sum(values: list) -> int:
    """
    Calculating the sum of squares from a given list of integers.
    :param values: list of integers
    :return: square sum
    """
    s = 0
    for value in values:
        s += value * value
    return s


def count_negative_integers(values: list) -> int:
    """
    Count the negative integer values.
    :param values: list of integers
    :return: count of negative integers
    """
    count = 0
    for value in values:
        if value < 0:
            count += 1
    return count

