"""
1.) Calculates square-sum from a list of numbers
2.) Counts the negative integers from a list of numbers
"""


def calc_square_sum(numbers: list):
    squares_sum = 0
    for i in numbers:
        squares_sum += i**2
    print(squares_sum)


def count_negative_integers(n_list: list):
    counts = 0
    for i in n_list:
        if i < 0 and type(i) == int:
            counts += 1
    print(counts)
