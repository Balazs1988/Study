import os

is_program_on = True
while is_program_on:
    text = input('Please type a command! ')
    if text in ('q', 'quit'):
        is_program_on = False
    elif text == 'list':
        os.listdir()
    elif text == 'here':
        os.getcwd()
    elif text == 'up':
        os.path.realpath(os.pardir)
    elif text == 'close':
        os.close()
