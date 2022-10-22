def calc_factorial(n: int) -> int:
    """
    Calculate the factorial of a number
    :param n: a non-negative integer value
    :return: the n!
    """
    if n < 0:
        raise ValueError('Only non-negative integers are accepted!')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
