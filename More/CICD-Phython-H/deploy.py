with open('output.txt', 'r') as output_file:
    output_list = output_file.read().splitlines()

with open('output/index.html', 'a') as boiler_file:
    for i in output_list:
        boiler_file.write(i)