import random

WIN_PAIRS = [
    ('rock', 'scissor'),
    ('paper', 'rock'),
    ('scissor', 'paper')
]


def start():
    """
    Start a new Rock-Scissors-Paper game.
    :return: None
    """
    n_rounds = require_rounds()
    player_score = 0
    machine_score = 0
    for round_ in range(1, n_rounds + 1):
        print(f'\n== Round {round_} ==')
        machine_choice = random.choice(['rock', 'paper', 'scissor'])
        player_choice = require_choice()
        print(f'Machine choice: {machine_choice}')
        if (player_choice, machine_choice) in WIN_PAIRS:
            player_score += 1
            print('--> Score for the machine.')
        elif player_choice == machine_choice:
            print('--> Nobody win the round.')
        else:
            print('--> Score for the machine.')
            machine_score += 1
    display_result(player_score, machine_score)


def require_rounds():
    """
    Require the number of rounds from the user.
    :return: number of rounds
    """
    while True:
        try:
            n_rounds = int(input('Number of rounds? '))
            if n_rounds > 0 and n_rounds % 2 == 1:
                return n_rounds
            else:
                print('Invalid number of rounds!')
        except ValueError:
            print('Invalid number format!')


def require_choice() -> str:
    """
    Require the choice from the player.
    :return: the choice
    """
    choice = ''
    while choice not in ['rock', 'paper', 'scissor']:
        choice = input('Choose! "rock", "paper" or "scissor"? ')
    return choice


def display_result(player_score: int, machine_score: int):
    """
    Display the result of the game.
    :param player_score: scores of the player
    :param machine_score: scores of the machine
    :return: None
    """
    print(f'Player: {player_score} scores, Machine: {machine_score} scores')
    if player_score > machine_score:
        print('You are the winner! :)')
    elif player_score == machine_score:
        print('Same scores.')
    else:
        print('The machine is the winner.')
