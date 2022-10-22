with open('input.txt', 'r') as text_file:
    i = text_file.read().splitlines()
    for num in i:
        out_num = int(num) * 2
        with open('output.txt', 'a') as out_file:
            out_file.write(f'{out_num}\n')
