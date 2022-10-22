import sys

def test_equality():
    value = True
    with open('input.txt', 'r') as input_file:
        input_data = input_file.read().splitlines()
    with open('output.txt', 'r') as output_file:
        output_data = output_file.read().splitlines()
    for i in range(0, len(input_data)):
        if int(input_data[i]) * 2 != int(output_data[i]):
            value = False
    return value


if test_equality() is False:
    sys.exit("exit(1)")
