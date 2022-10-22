import os

if __name__ == '__main__':
    while True:
        command = input('$ ')
        if command == 'list':
            print(os.listdir())
        elif command == 'here':
            print(os.getcwd())
        elif command == 'up':
            os.chdir('..')
        elif command == 'quit':
            print('Terminate... [OK]')
            break
        else:
            parts = command.split(' ')
            if len(parts) > 1 and parts[0] == 'go':
                os.chdir(parts[1])
            else:
                print('Invalid command!')
