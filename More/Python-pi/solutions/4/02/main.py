import smath


if __name__ == '__main__':
    distances = [5, -1, -2, 5, 3]
    result = smath.calc_square_sum(distances)
    count = smath.count_negative_integers(distances)
    print(f'Sum of squares: {result}')
    print(f'Count of negative numbers: {count}')
