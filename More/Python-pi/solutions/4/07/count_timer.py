import random
import time


if __name__ == '__main__':
    n_zeros = random.randint(10, 20)
    print('Count the zeros!')
    print('0' * n_zeros)
    start_time = time.time()
    guess = int(input('How many zeros have printed? '))
    end_time = time.time()
    if guess == n_zeros:
        print('Correct!')
    else:
        print(f'No. The correct number is {n_zeros}.')
    elapsed_time = end_time - start_time
    print(f'The counting required {elapsed_time} seconds.')
