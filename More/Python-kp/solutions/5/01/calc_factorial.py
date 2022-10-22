def calc_factorial(number):
    final_sum = 1
    for _ in range(1, number + 1):
        final_sum *= _
    return final_sum
