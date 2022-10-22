import datetime, random

zeros = random.randint(1, 25)
print('Please count the zeros below!')
print(zeros * '0')
start = datetime.datetime.now()
player_choice = int(input('Zeros: '))
stop = datetime.datetime.now()
if zeros == player_choice:
    print('Well done! Correct counting')
else:
    print('Sorry, incorrect counting')

print(f'Time elapsed: {stop-start}')
