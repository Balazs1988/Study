import random

choices = ('r', 'p', 's')
game_on = False
while not game_on:
    rounds = int(input('How many rounds do you want? '))
    if rounds % 2 == 0:
        print('Please type an odd number!')
    else:
        game_on = True
comp_points = 0
player_points = 0
for i in range(rounds):
    comp_choice = random.choice(choices)
    player_choice = input('Please choose! (r - "rock", p - "paper", s - "scissors": ')
    if player_choice == comp_choice:
        print("It's a tie, no points to anyone!")
    elif player_choice == 'r' and comp_choice == 'p':
        print('You lost this time.')
        comp_points += 1
    elif player_choice == 'r' and comp_choice == 's':
        print('You won this time.')
        player_points += 1
    elif player_choice == 'p' and comp_choice == 'r':
        print('You won this time.')
        player_points += 1
    elif player_choice == 'p' and comp_choice == 's':
        print('You lost this time.')
        comp_points += 1
    elif player_choice == 's' and comp_choice == 'r':
        print('You lost this time.')
        comp_points += 1
    elif player_choice == 's' and comp_choice == 'p':
        print('You won this time.')
        player_points += 1
    else:
        print('Sorry, you typed an unknown character, so you lost this time.')
        comp_points += 1
print(f'Final points: YOU: {player_points}, COMPUTER: {comp_points}')
